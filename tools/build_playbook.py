#!/usr/bin/env python3
"""Build the Project Manager AI Playbook from playbook/pm-playbook.json.

    python3 tools/build_playbook.py                 # fetches skills from GitHub
    python3 tools/build_playbook.py --clone PATH    # use a local clone of the upstream repo

Writes:
  playbook/PM-PLAYBOOK.md          the playbook as a page GitHub renders
  playbook/pm-playbook.html        one self-contained file: open it offline, copy or download any skill
  playbook/skills/<name>.md        each skill as one Markdown file for any AI assistant
  playbook/skills/<name>.prompt.md each skill as a GitHub Copilot prompt file
  playbook/LICENSES.md             licenses and credits for every skill

Skills are taken at the exact commit pinned in library.json / pm-playbook.json.
Standard library only.
"""
import argparse
import html
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KIT / "tools"))
import export_skill  # noqa: E402
import install_library  # noqa: E402

PB = KIT / "playbook"
FIT = 7500  # characters: a safe size for most "custom instructions" boxes


def skill_entry(item, lib, up):
    if "library" in item:
        s = next(x for x in lib["skills"] if x["install_name"] == item["library"])
        return dict(s)
    return {"install_name": item["name"], "license": up["license"],
            "source": {"repo": up["repo"], "ref": up["ref"], "path": item["upstream"]}}


def source_url(s, kit_repo):
    src = s["source"]
    if "local" in src:
        return f"https://github.com/{kit_repo}/tree/main/{src['local']}"
    return f"https://github.com/{src['repo']}/tree/{src['ref']}/{src['path']}"


def author_of(s, up):
    src = s["source"]
    if "local" in src:
        return s.get("author") or s["license"].split("(")[1].split(")")[0]
    return up["author"] if src["repo"] == up["repo"] else src["repo"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clone", type=Path, help="local clone of the upstream repo at the pinned commit")
    a = ap.parse_args()

    cfg = json.loads((PB / "pm-playbook.json").read_text(encoding="utf-8"))
    lib = json.loads((KIT / "library.json").read_text(encoding="utf-8"))
    up, kit_repo = cfg["upstream"], lib["kit_repo"]

    if a.clone:
        clone = a.clone.resolve()

        def fetch_local(repo, ref, base, dest, skip):
            if repo != up["repo"]:
                raise RuntimeError(f"--clone only covers {up['repo']}, not {repo}")
            src = clone / base
            for p in sorted(src.rglob("*")):
                rel = p.relative_to(src).as_posix()
                if p.is_file() and rel not in skip:
                    (dest / rel).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(p, dest / rel)
        install_library.fetch_remote = fetch_local

    out_skills = PB / "skills"
    if out_skills.exists():
        shutil.rmtree(out_skills)
    out_skills.mkdir(parents=True)

    data, licenses = [], {}
    with tempfile.TemporaryDirectory() as tmp:
        for stage in cfg["stages"]:
            for item in stage["skills"]:
                s = skill_entry(item, lib, up)
                staged = install_library.stage(s, Path(tmp) / "stage")
                meta, body = export_skill.parse_skill(staged)
                refs = export_skill.collect_refs(staged)
                core = body.strip() + "\n"
                full = export_skill.build_body(body, refs, True)
                name, desc = item["name"], meta["description"]
                author, lic, url = author_of(s, up), s["license"].split(",")[0], source_url(s, kit_repo)
                credit = f"Skill by {author} · License: {lic} · Source: {url}"
                tools_note = ("\n> This skill also ships helper scripts (Python). They are not included here; "
                              "the instructions work without them.\n") if (staged / "scripts").is_dir() else ""
                head = f"# {name}\n\n> **Use these instructions for this whole conversation.** Apply them when: {desc}\n"
                any_full = f"{head}{tools_note}\n{full}\n---\n{credit}\n"
                any_core = f"{head}\n{core}"
                copilot = f'---\ndescription: "{desc.replace(chr(34), chr(39))}"\n---\n{tools_note}\n{full}\n<!-- {credit} -->\n'
                (out_skills / f"{name}.md").write_text(any_full, encoding="utf-8")
                (out_skills / f"{name}.prompt.md").write_text(copilot, encoding="utf-8")
                licenses.setdefault(lic, set()).add(name)
                data.append({"stage": stage["id"], "name": name, "when": item["when"], "try": item["try"],
                             "desc": desc, "author": author, "license": lic, "source": url,
                             "core": any_core, "full": any_full, "copilot": copilot,
                             "coreChars": len(any_core), "fullChars": len(any_full),
                             "refs": len(refs), "tools": (staged / "scripts").is_dir()})
                print(f"  {name:<28} core {len(any_core):>6,}  full {len(any_full):>7,}")

    gh = f"https://github.com/{kit_repo}/blob/main/playbook"
    write_markdown(cfg, data, gh)
    write_licenses(cfg, data, up, a.clone)
    write_html(cfg, data, kit_repo)
    print(f"\n{len(data)} skills -> playbook/PM-PLAYBOOK.md, playbook/pm-playbook.html, playbook/skills/")


HOW_TO = [
    ("Microsoft 365 Copilot (Copilot Chat)",
     ["Fastest: open a skill's `.md` file, copy everything, paste it as your first message, then ask your question.",
      "Too long to paste? Attach the `.md` file to the chat (paperclip) and say: *Follow the instructions in the attached file for this conversation.*",
      "Use it often? Create an agent (Copilot Chat → Create agent, or Copilot Studio). Paste the **core instructions** into Instructions and upload the full `.md` file as knowledge."]),
    ("ChatGPT",
     ["Paste the `.md` file as your first message, or attach it.",
      "Use it often? Create a custom GPT or a Project: core instructions in the Instructions box, the full `.md` file as a knowledge file."]),
    ("Google Gemini",
     ["Paste or attach the `.md` file at the start of the chat.",
      "Use it often? Create a Gem: core instructions as the Gem's instructions, the full `.md` file as a knowledge file."]),
    ("GitHub Copilot (VS Code, JetBrains)",
     ["Save the skill's `.prompt.md` file in your repository at `.github/prompts/`.",
      "In Copilot Chat, type `/` and pick the prompt by name."]),
]

RULES = [
    "Follow your company's AI policy. Use only AI tools your company approves, and don't paste confidential data into tools that aren't approved for it.",
    "Start a new chat for each skill, so instructions from one don't leak into the next.",
    "Give the AI your real situation: numbers, dates, constraints. The skills ask follow-up questions when something is missing; answer them.",
    "Check the output before you send it. You own the plan, the status and the decision.",
]


def write_markdown(cfg, data, gh):
    by_stage = {st["id"]: [d for d in data if d["stage"] == st["id"]] for st in cfg["stages"]}
    md = [f"# {cfg['title']}", "", cfg["subtitle"], "",
          f"**{len(data)} skills** in {len(cfg['stages'])} phases. Each skill is a set of instructions that turns a "
          "general AI assistant into a specialist for one project management job.", "",
          "**Prefer a page with copy buttons?** Download [`pm-playbook.html`](pm-playbook.html) "
          "(click *Download raw file* on GitHub) and open it in your browser. It works offline.", "",
          "## Contents", ""]
    md += [f"- [{st['name']}](#{re.sub(r'[^a-z0-9 -]', '', st['name'].lower()).replace(' ', '-')}) "
           f"({len(by_stage[st['id']])} skills)" for st in cfg["stages"]]
    md += ["- [How to use a skill at work](#how-to-use-a-skill-at-work)", "- [Ground rules](#ground-rules)", ""]
    md += ["## How to use a skill at work", ""]
    for tool, steps in HOW_TO:
        md += [f"**{tool}**", ""] + [f"{i}. {s}" for i, s in enumerate(steps, 1)] + [""]
    md += ["**Core or full?** Each skill's `.md` file is the full skill: its instructions plus reference "
           f"material. The core instructions are the first part. Instruction boxes in custom agents and GPTs are "
           f"often limited to around {FIT:,} characters, so the tables below show the core size.", "",
           "## Ground rules", ""] + [f"- {r}" for r in RULES] + [""]
    for st in cfg["stages"]:
        md += [f"## {st['name']}", "", f"*{st['goal']}*", "",
               "| Skill | Use it when | Try this | Get it |", "|---|---|---|---|"]
        for d in by_stage[st["id"]]:
            fits = "fits an instructions box" if d["coreChars"] <= FIT else "too long for most instruction boxes: attach the file"
            get = (f"[Any AI (.md)](skills/{d['name']}.md) · [Copilot prompt](skills/{d['name']}.prompt.md) · "
                   f"[Original]({d['source']})")
            md.append(f"| **{d['name']}**<br><sub>core {d['coreChars']:,} chars · {fits}</sub> | {d['when']} | "
                      f"\"{d['try']}\" | {get} |")
        md.append("")
    md += ["---", "", "Skills are by their authors and keep their own licenses: see [LICENSES.md](LICENSES.md). "
           "Rebuild with `python3 tools/build_playbook.py` after editing `playbook/pm-playbook.json`.", ""]
    (PB / "PM-PLAYBOOK.md").write_text("\n".join(md), encoding="utf-8")


def write_licenses(cfg, data, up, clone=None):
    md = ["# Licenses and credits", "",
          "Every skill in this playbook belongs to its author and keeps its own license.", "",
          "| Skill | Author | License | Source |", "|---|---|---|---|"]
    md += [f"| {d['name']} | {d['author']} | {d['license']} | [link]({d['source']}) |" for d in data]
    if clone and (clone / "LICENSE").is_file():
        up_license = (clone / "LICENSE").read_text(encoding="utf-8")
    else:
        up_license = install_library.raw(up["repo"], up["ref"], "LICENSE").decode("utf-8")
    md += ["", f"## {up['author']}", "",
           f"The skills from `{up['repo']}` are shared under the MIT license with the Commons Clause: "
           "you may use, copy and adapt them, but not sell them or a service whose value comes mainly from them. "
           "The full license text follows.", ""]
    if up_license:
        md += ["```", up_license.strip(), "```", ""]
    md += ["## Other skills", "",
           "Skills marked CC BY 4.0 are by Agile36 (https://creativecommons.org/licenses/by/4.0/). "
           "Skills marked MIT keep the license file in their folder under `skills/` in this repository.", ""]
    (PB / "LICENSES.md").write_text("\n".join(md), encoding="utf-8")


def write_html(cfg, data, kit_repo):
    tpl = (KIT / "playbook/template.html").read_text(encoding="utf-8")
    payload = {"title": cfg["title"], "subtitle": cfg["subtitle"], "fit": FIT, "repo": kit_repo,
               "stages": [{k: st[k] for k in ("id", "name", "goal")} for st in cfg["stages"]],
               "skills": data, "howTo": HOW_TO, "rules": RULES}
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    out = tpl.replace("__TITLE__", html.escape(cfg["title"])).replace("/*__DATA__*/null", blob)
    (PB / "pm-playbook.html").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
