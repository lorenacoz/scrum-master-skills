#!/usr/bin/env python3
"""Regenerate LIBRARY.md and the skill data in site/library.html from library.json.

    python3 tools/build_docs.py

Run it after any change to library.json so the docs and the page stay in sync.
"""
import json
import re
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))
skills = lib["skills"]
repo = lib["kit_repo"]
site = lib.get("site", {})
title = site.get("title", "Scrum Master AI Skills Library")
core = [s for s in skills if not s.get("optional")]
cats = list(dict.fromkeys(s["category"] for s in skills))


def author(s):
    src = s["source"]
    if "local" in src:
        return s.get("author") or s["license"].split("(")[1].split(")")[0]
    return src["repo"]


def author_link(s):
    src = s["source"]
    if "local" in src:
        return author(s)
    return f"[{src['repo']}](https://github.com/{src['repo']})"


one_liner = f"curl -fsSL https://raw.githubusercontent.com/{repo}/main/tools/install_library.py | python3 -"

md = [f"# {title}", "", site.get("tagline", ""), "",
      f"{len(core)} skills for the jobs a Scrum Master does every sprint, plus "
      f"{len(skills) - len(core)} optional ones. Every Scrum event and SAFe event has its own skill. "
      "Each one is pinned to the exact version that was reviewed.", ""]
for c in cats:
    md += [f"## {c}", "", "| Skill | Job | Level | Needs |", "|---|---|---|---|"]
    for s in skills:
        if s["category"] == c:
            opt = " *(optional)*" if s.get("optional") else ""
            md.append(f"| **{s['install_name']}**{opt} | {s['job']} | {s['level'].title()} | {s['needs']} |")
    md.append("")
md += ["**Which retro skill?** `scrum-retrospective` plans and facilitates the meeting. "
       "`sprint-retrospective` builds a data pack from git history to bring to it.", "",
       "**Event skills vs. scrum-workflow:** the event skills prepare one meeting. "
       "`scrum-workflow` runs a team's sprints over time and remembers them between sessions.", "",
       "---", "", "## Install it", "",
       "Nothing to download first. In a terminal:", "", "```bash", one_liner, "```", "",
       "That installs all core skills into Claude Code. Add options after `python3 -`:", "",
       "| You use… | Add | Then |", "|---|---|---|",
       "| **Claude Code** | nothing | Start a new session. Skills load on their own |",
       "| **Claude app** (claude.ai, desktop, mobile) | `--target zip` | Upload each zip: Settings > Capabilities > Skills |",
       "| **GitHub Copilot** | `--target copilot` | Copy the `.github/` folder into your repo |",
       "| **ChatGPT, Gemini, others** | `--target plain` | Paste a `.txt` file as your first message, or save it as a custom GPT / Gem instruction |",
       "", "Other options: `--list`, `--category \"Scrum events\"`, `--only daily-scrum,sprint-review`, `--with-optional`, `--force` (update).",
       "", "Working from a copy of this repo instead? Run `python3 tools/install_library.py` with the same options.", "",
       "**Outside Claude Code**, skills marked *Nothing* under Needs work fully. Skills with Python tools still give advice "
       "without them; in the Claude app they can run their tools when code execution is on.", "",
       "---", "", "## Try each one", "", "Use a made-up team. Never paste real names or company data into a class exercise.", "",
       "| Skill | Try this |", "|---|---|"]
md += [f"| {s['install_name']} | \"{s['try_prompt']}\" |" for s in skills]
md += ["", "---", "", "## Sources and credit", "",
       "Skills credited to *Agile36* were written by Agile36 for their Scrum Master class. Skills from MIT-licensed repos are copied here with "
       "their license file (see `THIRD_PARTY_NOTICES.md`). All others download from their author's repo at install time "
       "and are not re-hosted here.", "", "| Skill | Author | License | Where it comes from |", "|---|---|---|---|"]
for s in skills:
    where = "this repo" if "local" in s["source"] else f"author's repo @ `{s['source']['ref'][:7]}`"
    md.append(f"| {s['install_name']} | {author_link(s)} | {s['license'].split(',')[0]} | {where} |")
md += ["", "Agile36's own skills, lab and tools are licensed CC BY 4.0: reuse and adapt them freely, "
       "including commercially, with credit to Agile36. See `LICENSE`.", "",
       "Three skills were renamed so they don't clash: `scrum-role-coach`, `scrum-analytics` and "
       "`scrum-workflow` were all originally called `scrum-master`.", "",
       "## Want more?", "",
       "- [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills): 400 skills, the source of many here",
       "- [Claude Skill Registry](https://majiayu000.github.io/claude-skill-registry/): searchable community catalog",
       "- [loremaster-ai/loremaster](https://github.com/loremaster-ai/loremaster): a complete AI Scrum Master system "
       "for Hermes Agent, built around a shared project wiki. Advanced; not installable skill-by-skill.", "",
       "Before installing any skill, read its `SKILL.md` in full and open any scripts, or run `skill-security-auditor` on it.", ""]
(KIT / "LIBRARY.md").write_text("\n".join(md), encoding="utf-8")

# page data
page = KIT / "site/library.html"


def source_info(s):
    src = s["source"]
    if "local" in src:
        return {"repo": None, "inRepo": True, "hasTools": (KIT / src["local"] / "scripts").is_dir(),
                "sourceUrl": f"https://github.com/{repo}/tree/main/{src['local']}",
                "rawSkill": f"skills/{s['install_name']}/SKILL.md"}
    base = f"{src['repo']}/{src['ref']}/{src['path'].rstrip('/')}"
    return {"repo": f"https://github.com/{src['repo']}", "inRepo": False, "hasTools": None,
            "sourceUrl": f"https://github.com/{src['repo']}/tree/{src['ref']}/{src['path']}",
            "rawSkill": f"https://raw.githubusercontent.com/{base}/SKILL.md"}


data = [{"slug": s["install_name"], "category": s["category"], "level": s["level"], "optional": bool(s.get("optional")),
         "job": s["job"], "needs": s["needs"], "try": s["try_prompt"], "author": author(s),
         "license": s["license"].split(",")[0], **source_info(s)} for s in skills]
block = ("/*SKILLS-START*/const SKILLS = " + json.dumps(data, ensure_ascii=False, indent=1)
         + f";\nconst SITE = {json.dumps(site, ensure_ascii=False)};\nconst KIT_REPO = {json.dumps(repo)};\nconst ONE_LINER = {json.dumps(one_liner)};/*SKILLS-END*/")
html = page.read_text(encoding="utf-8")
html, n = re.subn(r"/\*SKILLS-START\*/.*?/\*SKILLS-END\*/", lambda m: block, html, flags=re.S)
if n != 1:
    raise SystemExit("site/library.html is missing the SKILLS-START/SKILLS-END markers")
page.write_text(html, encoding="utf-8")
print(f"LIBRARY.md and site/library.html updated: {len(skills)} skills in {len(cats)} categories")
