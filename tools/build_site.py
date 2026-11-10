#!/usr/bin/env python3
"""Build the static website (GitHub Pages) from library.json and skills/.

    python3 tools/build_site.py            # writes _site/
    python3 tools/build_site.py --out dist
    python3 -m http.server -d _site 8000   # preview at http://localhost:8000

Writes:
  _site/index.html                          the library page (site/library.html)
  _site/skills/<name>/SKILL.md              single file, references folded in
  _site/skills/<name>/<name>.zip            full skill folder, for the Claude app
  _site/skills/<name>/<name>.prompt.md      GitHub Copilot prompt file
  _site/skills/<name>/<name>.txt            paste into ChatGPT, Gemini or any chat
  _site/library.json                        the manifest, for anyone who wants the data

Only skills stored in this repo get files. Skills from other authors are
listed with a link and an install command, and are never re-hosted.
Run tools/build_docs.py first so the page data matches library.json.
Standard library only.
"""
import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KIT / "tools"))
import export_skill  # noqa: E402
import install_library  # noqa: E402

TOOLS_NOTE = ("\n> This single-file version leaves out the skill's Python tools. "
              "Download the .zip for the full skill.\n")


def write_skill_files(staged: Path, out: Path):
    name = staged.name
    out.mkdir(parents=True, exist_ok=True)
    text = (staged / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^(---\n.*?\n---\n)", text, re.S).group(1)
    meta, body = export_skill.parse_skill(staged)
    full = export_skill.build_body(body, export_skill.collect_refs(staged), True)
    note = TOOLS_NOTE if (staged / "scripts").is_dir() else ""
    desc = meta["description"].replace('"', "'")

    (out / "SKILL.md").write_text(f"{front}{note}\n{full}", encoding="utf-8")
    (out / f"{name}.prompt.md").write_text(f'---\ndescription: "{desc}"\n---\n{note}\n{full}', encoding="utf-8")
    (out / f"{name}.txt").write_text(
        f"Use these instructions for this whole conversation.\n"
        f"Apply them when: {meta['description']}\n{note}\n{full}", encoding="utf-8")
    with zipfile.ZipFile(out / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(staged.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                zf.write(p, Path(name) / p.relative_to(staged))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=KIT / "_site")
    a = ap.parse_args()
    out = a.out.resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))
    shutil.copy(KIT / "site/library.html", out / "index.html")
    shutil.copy(KIT / "library.json", out / "library.json")
    (out / ".nojekyll").write_text("", encoding="utf-8")

    n = 0
    with tempfile.TemporaryDirectory() as tmp:
        for s in lib["skills"]:
            if "local" not in s["source"]:
                continue
            staged = install_library.stage(s, Path(tmp) / "stage")
            write_skill_files(staged, out / "skills" / s["install_name"])
            n += 1
    print(f"site -> {out}  ({len(lib['skills'])} skills listed, files for {n})")


if __name__ == "__main__":
    main()
