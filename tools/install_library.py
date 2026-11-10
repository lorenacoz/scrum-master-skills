#!/usr/bin/env python3
"""Install the Agile36 Scrum Master skill library in one command.

From a copy of the kit:
    python3 tools/install_library.py                  # install into Claude (~/.claude/skills)
    python3 tools/install_library.py --list           # show what's in the library
    python3 tools/install_library.py --target zip     # zips to upload in the Claude app
    python3 tools/install_library.py --target copilot # .github/ folder for GitHub Copilot
    python3 tools/install_library.py --target plain   # paste-into-any-chat text files
    python3 tools/install_library.py --only daily-scrum,sprint-review
    python3 tools/install_library.py --category "Scrum events"
    python3 tools/install_library.py --with-optional  # include optional skills

Without downloading anything first (fetches the kit from GitHub):
    curl -fsSL https://raw.githubusercontent.com/lorenacoz/scrum-master-skills/main/tools/install_library.py | python3 - [options]

Skills in the kit's skills/ folder come from the kit itself. Others download
from each author's GitHub repo at the exact commit listed in library.json, so
everyone gets the version that was reviewed. Standard library only; no GitHub
account needed.
"""
import argparse
import importlib.util
import json
import re
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

KIT_REPO = "lorenacoz/scrum-master-skills"
KIT_REF = "main"
UA = {"User-Agent": "skill-library-installer"}

try:
    KIT = Path(__file__).resolve().parent.parent
    LOCAL = (KIT / "library.json").is_file()
except NameError:  # piped into python3 -
    KIT, LOCAL = None, False


def http_get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def raw(repo, ref, path):
    return http_get(f"https://raw.githubusercontent.com/{repo}/{ref}/{path}")


def load_export_skill(tmp: Path):
    if LOCAL:
        path = KIT / "tools/export_skill.py"
    else:
        path = tmp / "export_skill.py"
        path.write_bytes(raw(KIT_REPO, KIT_REF, "tools/export_skill.py"))
    spec = importlib.util.spec_from_file_location("export_skill", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def list_dir(repo, ref, path):
    items = json.loads(http_get(f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"))
    out = []
    for it in items:
        if it["type"] == "file":
            out.append(it["path"])
        elif it["type"] == "dir":
            out += list_dir(repo, ref, it["path"])
    return out


_trees = {}


def repo_files(repo, ref, base):
    key = (repo, ref)
    if key not in _trees:
        _trees[key] = json.loads(http_get(f"https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"))
    tree = _trees[key]
    files = [t["path"] for t in tree["tree"]
             if t["type"] == "blob" and t["path"].startswith(base + "/")]
    if not files and tree.get("truncated"):
        files = list_dir(repo, ref, base)  # huge repos: walk just this folder
    return files


def fetch_remote(repo, ref, base, dest: Path, skip):
    base = base.rstrip("/")
    files = repo_files(repo, ref, base)
    if not files:
        raise RuntimeError(f"no files found at {repo}/{base}@{ref[:7]}")
    for f in files:
        rel = f[len(base) + 1:]
        if rel in skip:
            continue
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(raw(repo, ref, f))


def stage(skill, workdir: Path) -> Path:
    """Put the skill's files in workdir/<install_name>, renamed and ready."""
    name = skill["install_name"]
    dest = workdir / name
    src = skill["source"]
    skip = set(skill.get("skip", []))
    if "local" in src:
        if LOCAL:
            shutil.copytree(KIT / src["local"], dest)
        else:
            fetch_remote(KIT_REPO, KIT_REF, src["local"], dest, skip)
    else:
        fetch_remote(src["repo"], src["ref"], src["path"], dest, skip)
    md = dest / "SKILL.md"
    text = md.read_text(encoding="utf-8")
    # rename in frontmatter so skills with the same upstream name don't clash
    text = re.sub(r"^(---\n(?:.*\n)*?)name:[^\n]*\n", rf"\1name: {name}\n", text, count=1)
    if "path" in src:  # upstream docs give repo-relative script paths; make them skill-relative
        text = text.replace(src["path"].rstrip("/") + "/", "")
    for old, new in skill.get("rewrite", {}).items():
        text = text.replace(old, new)
    md.write_text(text, encoding="utf-8")
    return dest


def to_claude(staged: Path, root: Path, force: bool):
    target = root / staged.name
    if target.exists():
        if not force:
            print(f"  skip   {target} already exists (use --force to replace)")
            return
        shutil.rmtree(target)
    root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(staged, target)
    print(f"  ok     {target}")


def to_zip(staged: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    z = out / f"{staged.name}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(staged.rglob("*")):
            if p.is_file():
                zf.write(p, Path(staged.name) / p.relative_to(staged))
    print(f"  ok     {z}")


def to_text(ex, staged: Path, out: Path, target: str):
    meta, body = ex.parse_skill(staged)
    full = ex.build_body(body, ex.collect_refs(staged), True)
    name, desc = meta["name"], meta["description"].replace('"', "'")
    note = ("\n> Note: the Claude version of this skill also ships scripts. "
            "They are not included here.\n" if (staged / "scripts").is_dir() else "")
    if target == "copilot":
        ex.write(out / ".github/prompts" / f"{name}.prompt.md",
                 f'---\ndescription: "{desc}"\n---\n{note}\n{full}')
        ex.write(out / ".github/instructions" / f"{name}.instructions.md",
                 f'---\napplyTo: "**"\ndescription: "{desc}"\n---\n{note}\n{full}')
    elif target == "agents":
        ex.write(out / f"{name}.AGENTS.md", f"# {name}\n\n> {desc}\n{note}\n{full}")
    else:
        ex.write(out / f"{name}.txt",
                 f"Use these instructions for this whole conversation.\n"
                 f"Apply them when: {meta['description']}\n{note}\n{full}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", choices=["claude", "zip", "copilot", "agents", "plain"],
                    default="claude")
    ap.add_argument("--dest", type=Path, help="where to install/write (default depends on target)")
    ap.add_argument("--only", help="comma-separated install names")
    ap.add_argument("--category", help="install one category, e.g. 'Scrum events'")
    ap.add_argument("--with-optional", action="store_true")
    ap.add_argument("--force", action="store_true", help="replace skills already installed")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if LOCAL:
        lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))["skills"]
    else:
        lib = json.loads(raw(KIT_REPO, KIT_REF, "library.json"))["skills"]

    if a.list:
        cat = None
        for s in lib:
            if s["category"] != cat:
                cat = s["category"]
                print(f"\n{cat.upper()}")
            opt = " (optional)" if s.get("optional") else ""
            print(f"  {s['install_name']:<26} {s['level']:<13} {s['job']}{opt}")
        print(f"\n{len(lib)} skills. Details and licenses: LIBRARY.md")
        return

    chosen = lib
    if a.only:
        want = {w.strip() for w in a.only.split(",")}
        unknown = want - {s["install_name"] for s in lib}
        if unknown:
            sys.exit(f"unknown skill(s): {', '.join(sorted(unknown))}. Try --list")
        chosen = [s for s in lib if s["install_name"] in want]
    else:
        if a.category:
            chosen = [s for s in chosen if s["category"].lower() == a.category.lower()]
            if not chosen:
                cats = sorted({s["category"] for s in lib})
                sys.exit(f"unknown category. Choose one of: {', '.join(cats)}")
        if not a.with_optional:
            chosen = [s for s in chosen if not s.get("optional")]

    defaults = {"claude": Path.home() / ".claude/skills", "zip": Path("skill-zips"),
                "copilot": Path("copilot-export"), "agents": Path("agents-export"),
                "plain": Path("plain-export")}
    dest = (a.dest or defaults[a.target]).expanduser()
    print(f"Installing {len(chosen)} skill(s) -> {a.target}: {dest}")

    failed = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        ex = load_export_skill(tmp) if a.target in ("copilot", "agents", "plain") else None
        for s in chosen:
            print(f"- {s['install_name']}")
            try:
                staged = stage(s, tmp / "stage")
                if a.target == "claude":
                    to_claude(staged, dest, a.force)
                elif a.target == "zip":
                    to_zip(staged, dest)
                else:
                    to_text(ex, staged, dest, a.target)
            except Exception as e:  # keep going; report at the end
                print(f"  FAILED {e}")
                failed.append(s["install_name"])
    if failed:
        sys.exit(f"\n{len(failed)} failed: {', '.join(failed)}")
    print("\nDone.")
    if a.target == "claude":
        print("Start a new Claude Code session to pick up the skills.")
    elif a.target == "zip":
        print("Upload each zip in the Claude app: Settings > Capabilities > Skills.")


if __name__ == "__main__":
    main()
