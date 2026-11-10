#!/usr/bin/env python3
"""Package the skills as Claude plugins, with this repo as the marketplace.

    python3 tools/build_plugins.py                 # fetches upstream skills from GitHub
    python3 tools/build_plugins.py --clone PATH    # use a local clone of the upstream repo

Writes:
  .claude-plugin/marketplace.json           the marketplace: lists both plugins
  plugins/project-manager-skills/           the 40 skills in playbook/pm-playbook.json
  plugins/scrum-master-skills/              the library skills in library.json that may be redistributed
  dist/<plugin>.zip                         each plugin as one zip, for upload
  dist/skills/<plugin>/<skill>.zip          each skill as its own zip (Claude app: Settings > Skills)

Each plugin holds .claude-plugin/plugin.json, README.md, LICENSES.md and
skills/<name>/ (the full skill folder, renamed and pinned exactly as the
installer does). Skills whose authors gave no license are left out: they
stay installable with tools/install_library.py. Standard library only.
"""
import argparse
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KIT / "tools"))
import export_skill  # noqa: E402
import install_library  # noqa: E402

VERSION = "1.0.0"
OWNER = "lorenacoz"


def redistributable(s):
    return "local" in s["source"] or "MIT" in s["license"] or "CC BY" in s["license"]


def use_clone(clone: Path, repo: str):
    def fetch_local(r, ref, base, dest, skip):
        if r != repo:
            raise RuntimeError(f"--clone only covers {repo}, not {r}")
        src = clone / base
        for p in sorted(src.rglob("*")):
            rel = p.relative_to(src).as_posix()
            if p.is_file() and rel not in skip and "__pycache__" not in p.parts:
                (dest / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(p, dest / rel)
    install_library.fetch_remote = fetch_local


def author_of(s):
    src = s["source"]
    if "local" in src:
        return s.get("author") or s["license"].split("(")[1].split(")")[0]
    return src["repo"]


def build_plugin(name, description, keywords, entries, kit_repo, upstream_license, tmp):
    root = KIT / "plugins" / name
    if root.exists():
        shutil.rmtree(root)
    (root / ".claude-plugin").mkdir(parents=True)
    rows = []
    for s in entries:
        staged = install_library.stage(s, Path(tmp) / name)
        if "local" not in s["source"] and not (staged / "LICENSE").exists() and upstream_license:
            (staged / "LICENSE").write_text(upstream_license, encoding="utf-8")
        for junk in staged.rglob("__pycache__"):
            shutil.rmtree(junk)
        shutil.copytree(staged, root / "skills" / s["install_name"])
        meta, _ = export_skill.parse_skill(staged)
        rows.append((s, meta))

    manifest = {
        "name": name, "version": VERSION, "description": description,
        "author": {"name": OWNER, "url": f"https://github.com/{OWNER}"},
        "homepage": f"https://github.com/{kit_repo}",
        "repository": f"https://github.com/{kit_repo}",
        "license": "SEE LICENSE IN LICENSES.md",
        "keywords": keywords,
    }
    (root / ".claude-plugin/plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    readme = [f"# {name}", "", description, "",
              "## Install", "", "In Claude Code:", "", "```", f"/plugin marketplace add {kit_repo}",
              f"/plugin install {name}@{MARKETPLACE}", "```", "",
              "Skills load on their own when a request matches. Call one directly with "
              f"`/{name}:<skill-name>`.", "",
              f"## Skills ({len(rows)})", "", "| Skill | What it does |", "|---|---|"]
    readme += [f"| `{s['install_name']}` | {s.get('job') or meta['description'][:160]} |" for s, meta in rows]
    readme += ["", "Each skill keeps its author's license: see [LICENSES.md](LICENSES.md).", ""]
    (root / "README.md").write_text("\n".join(readme), encoding="utf-8")

    lic = ["# Licenses and credits", "", "Each skill folder in `skills/` holds its own LICENSE file.", "",
           "| Skill | Author | License |", "|---|---|---|"]
    lic += [f"| {s['install_name']} | {author_of(s)} | {s['license'].split(',')[0]} |" for s, _ in rows]
    lic += ["", "MIT + Commons Clause skills may be used, copied and adapted, but not sold. "
            "CC BY 4.0 skills (Agile36) may be reused with credit.", ""]
    (root / "LICENSES.md").write_text("\n".join(lic), encoding="utf-8")

    dist = KIT / "dist"
    dist.mkdir(exist_ok=True)
    zp = dist / f"{name}.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                zf.write(p, Path(name) / p.relative_to(root))
    one = dist / "skills" / name
    if one.exists():
        shutil.rmtree(one)
    one.mkdir(parents=True)
    for s, _ in rows:
        sk = root / "skills" / s["install_name"]
        with zipfile.ZipFile(one / f"{s['install_name']}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(sk.rglob("*")):
                if p.is_file():
                    zf.write(p, Path(s["install_name"]) / p.relative_to(sk))
    print(f"  {name}: {len(rows)} skills -> plugins/{name}/, dist/{name}.zip ({zp.stat().st_size // 1024} KB)")
    return manifest, len(rows)


MARKETPLACE = "scrum-master-skills"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clone", type=Path, help="local clone of the upstream repo at the pinned commit")
    a = ap.parse_args()

    lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))
    pb = json.loads((KIT / "playbook/pm-playbook.json").read_text(encoding="utf-8"))
    up, kit_repo = pb["upstream"], lib["kit_repo"]
    if a.clone:
        use_clone(a.clone.resolve(), up["repo"])
        upstream_license = (a.clone / "LICENSE").read_text(encoding="utf-8")
    else:
        upstream_license = install_library.raw(up["repo"], up["ref"], "LICENSE").decode("utf-8")

    by_name = {s["install_name"]: s for s in lib["skills"]}
    pm_entries = []
    for st in pb["stages"]:
        for it in st["skills"]:
            if "library" in it:
                pm_entries.append(dict(by_name[it["library"]]))
            else:
                pm_entries.append({"install_name": it["name"], "license": up["license"], "job": it["when"],
                                   "source": {"repo": up["repo"], "ref": up["ref"], "path": it["upstream"]}})
    for e, it in zip(pm_entries, [i for st in pb["stages"] for i in st["skills"]]):
        e["job"] = it["when"]
    sm_entries = [s for s in lib["skills"] if redistributable(s)]
    left_out = [s["install_name"] for s in lib["skills"] if not redistributable(s)]

    plugins = []
    with tempfile.TemporaryDirectory() as tmp:
        plugins.append(build_plugin(
            "project-manager-skills",
            "40 AI skills for project managers, by phase: start, plan, run delivery, monitor and report, "
            "communicate, launch and close, and work tools (Jira, Confluence, Notion, Linear).",
            ["project-management", "pmo", "status-report", "raid", "launch", "jira", "confluence"],
            pm_entries, kit_repo, upstream_license, tmp))
        plugins.append(build_plugin(
            "scrum-master-skills",
            "AI skills for Scrum Masters: every Scrum and SAFe event, facilitation, team conflict, risks, "
            "backlog, metrics and stakeholders.",
            ["scrum", "agile", "safe", "scrum-master", "retrospective", "sprint-planning", "facilitation"],
            sm_entries, kit_repo, upstream_license, tmp))

    market = {
        "name": MARKETPLACE,
        "owner": {"name": OWNER, "url": f"https://github.com/{OWNER}"},
        "metadata": {"description": "Scrum Master and project manager skills for Claude.", "version": VERSION},
        "plugins": [{"name": m["name"], "source": f"./plugins/{m['name']}", "description": m["description"],
                     "version": m["version"], "author": m["author"], "keywords": m["keywords"],
                     "homepage": m["homepage"]} for m, _ in plugins],
    }
    (KIT / ".claude-plugin").mkdir(exist_ok=True)
    (KIT / ".claude-plugin/marketplace.json").write_text(json.dumps(market, indent=2) + "\n", encoding="utf-8")
    print(f"marketplace '{MARKETPLACE}' -> .claude-plugin/marketplace.json")
    if left_out:
        print(f"left out (no license from their authors): {', '.join(left_out)}")


if __name__ == "__main__":
    main()
