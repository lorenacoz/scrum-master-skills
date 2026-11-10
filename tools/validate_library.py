#!/usr/bin/env python3
"""Check library.json and every skill stored in skills/ before publishing.

    python3 tools/validate_library.py

Fails (exit 1) on: missing fields, duplicate names, a local skill folder
with no SKILL.md, frontmatter without name/description, or a name that
doesn't match its install_name. Warns about template text left in place
and skill folders that aren't listed in library.json.
"""
import json
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
REQUIRED = ["install_name", "category", "job", "level", "needs", "source", "license", "try_prompt"]
LEVELS = {"beginner", "intermediate", "advanced"}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    meta, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km and not line.startswith(" "):
            key = km.group(1)
            meta[key] = "" if km.group(2).strip() in (">", "|", ">-", "|-") else km.group(2).strip()
        elif key and line.strip():
            meta[key] = (meta[key] + " " + line.strip()).strip()
    return meta


def main():
    lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))
    errors, warnings, seen = [], [], set()
    for i, s in enumerate(lib["skills"]):
        label = s.get("install_name", f"skills[{i}]")
        for f in REQUIRED:
            if not s.get(f):
                errors.append(f"{label}: missing '{f}'")
        if s.get("level") and s["level"] not in LEVELS:
            errors.append(f"{label}: level must be one of {sorted(LEVELS)}")
        if label in seen:
            errors.append(f"{label}: duplicate install_name")
        seen.add(label)
        src = s.get("source", {})
        if "local" in src:
            md = KIT / src["local"] / "SKILL.md"
            if not md.is_file():
                errors.append(f"{label}: {md.relative_to(KIT)} not found")
                continue
            text = md.read_text(encoding="utf-8")
            meta = frontmatter(text)
            if not meta or not meta.get("name") or not meta.get("description"):
                errors.append(f"{label}: SKILL.md needs frontmatter with name and description")
            elif meta["name"].strip("\"'") != label:
                errors.append(f"{label}: SKILL.md name is '{meta['name']}', expected '{label}'")
            if "[Question 1]" in text or "One to three sentences. First:" in text:
                warnings.append(f"{label}: still contains template placeholder text")
        elif not all(k in src for k in ("repo", "ref", "path")):
            errors.append(f"{label}: remote source needs repo, ref and path")

    listed = {s["source"]["local"].rstrip("/") for s in lib["skills"] if "local" in s.get("source", {})}
    for d in sorted((KIT / "skills").iterdir()):
        if d.is_dir() and f"skills/{d.name}" not in listed:
            warnings.append(f"skills/{d.name} is not listed in library.json")

    for w in warnings:
        print("warn ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(lib['skills'])} skills checked: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
