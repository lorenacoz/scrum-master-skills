#!/usr/bin/env python3
"""Start a new skill from the template and add it to the library.

    python3 tools/new_skill.py my-skill --category "Scrum events" \
        --job "What it does, in one line" --level beginner \
        --try "A prompt someone can paste to try it" --author "Your Name"

Creates skills/<name>/SKILL.md (from lab/SKILL.template.md) and
skills/<name>/references/, adds an entry to library.json, then refreshes
LIBRARY.md and the page. Edit SKILL.md, then commit: the site rebuilds itself.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent


def main():
    lib_path = KIT / "library.json"
    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    cats = list(dict.fromkeys(s["category"] for s in lib["skills"]))

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name", help="kebab-case, e.g. sprint-goal-coach")
    ap.add_argument("--category", required=True, help=f"existing or new. Existing: {', '.join(cats)}")
    ap.add_argument("--job", required=True, help="one line shown on the card")
    ap.add_argument("--level", choices=["beginner", "intermediate", "advanced"], default="beginner")
    ap.add_argument("--needs", default="Nothing")
    ap.add_argument("--try", dest="try_prompt", required=True, help="a prompt to try it")
    ap.add_argument("--author", required=True)
    ap.add_argument("--license", default="CC BY 4.0")
    a = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.name):
        sys.exit("name must be kebab-case: lowercase letters, digits and hyphens")
    if any(s["install_name"] == a.name for s in lib["skills"]):
        sys.exit(f"{a.name} is already in library.json")
    folder = KIT / "skills" / a.name
    if folder.exists():
        sys.exit(f"{folder} already exists")

    template = (KIT / "lab/SKILL.template.md").read_text(encoding="utf-8")
    template = template.replace("name: your-skill-name", f"name: {a.name}", 1)
    template = template.replace("# Skill Name", "# " + a.name.replace("-", " ").title(), 1)
    (folder / "references").mkdir(parents=True)
    (folder / "SKILL.md").write_text(template, encoding="utf-8")
    (folder / "references/.gitkeep").write_text("", encoding="utf-8")

    entry = {"install_name": a.name, "category": a.category, "job": a.job, "level": a.level,
             "needs": a.needs, "source": {"local": f"skills/{a.name}"},
             "license": a.license, "try_prompt": a.try_prompt, "author": a.author}
    # keep categories grouped: insert after the last skill in the same category
    idx = max((i for i, s in enumerate(lib["skills"]) if s["category"] == a.category), default=len(lib["skills"]) - 1)
    lib["skills"].insert(idx + 1, entry)
    lib_path.write_text(json.dumps(lib, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    subprocess.run([sys.executable, str(KIT / "tools/build_docs.py")], check=True)
    print(f"\nCreated {folder.relative_to(KIT)}/SKILL.md. Next: write the description and body, "
          f"then run python3 tools/validate_library.py")


if __name__ == "__main__":
    main()
