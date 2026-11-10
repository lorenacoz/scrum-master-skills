# Scrum Master AI Skills Library

Free AI skills for Scrum Masters: every Scrum and SAFe event, facilitation,
team conflict, risks, backlog, metrics and stakeholders. Use them in Claude,
GitHub Copilot, ChatGPT or any AI assistant.

**Website:** https://lorenacoz.github.io/scrum-master-skills/ (published by
GitHub Pages from this repo; see *Publishing the website* below)

---

A library of AI skills for Scrum Masters, plus a hands-on class for building
your own. Forty core skills cover every Scrum event, SAFe events, team
dynamics and facilitation, risks and impediments, backlog and estimation,
metrics, stakeholders and tools. They work in Claude,
GitHub Copilot, ChatGPT and any other assistant.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/lorenacoz/scrum-master-skills/main/tools/install_library.py | python3 -
```

That installs the core skills into Claude Code. For the Claude app, Copilot or
other chat tools, and to pick skills, see [LIBRARY.md](LIBRARY.md).

## What's here

```
├── LIBRARY.md                 every skill: job, level, needs, a prompt to try, credits
├── library.json               the library manifest, pinned to reviewed versions
├── skills/                    skills that ship in this repo (Agile36's own + MIT-licensed)
├── lab/
│   ├── LAB-GUIDE.md           8-module hands-on lab
│   ├── SKILL.template.md      starting point for your own skill
│   ├── test-prompts.md        test-and-fix worksheet
│   └── DEMO-KIT.md            present your two favorite skills
├── site/library.html          the website: search, filters, a page per skill, downloads
├── .github/workflows/pages.yml  builds and publishes the website on every push to main
└── tools/
    ├── install_library.py     installs the library into any tool
    ├── new_skill.py           starts a new skill from the template and lists it
    ├── validate_library.py    checks library.json and every SKILL.md
    ├── build_docs.py          regenerates LIBRARY.md and the page data from library.json
    ├── build_site.py          builds the website into _site/ (with per-skill downloads)
    ├── export_skill.py        ports a single skill (e.g. your own) to other tools
    └── export_for_website.py  exports files for an existing Next.js site
```

## The class (about 3.5 hours)

| Time | Module |
|---|---|
| 0:00 | Install and use the library (Module 0) |
| 0:30 | Read the skills + anatomy (Modules 1-2) |
| 1:20 | Choose a job + write a skill (Modules 3-4) |
| 2:15 | Test and fix (Module 5) |
| 2:45 | Port to a second tool (Module 6) |
| 3:05 | Demos of favorite two (Module 7) |

Start at [lab/LAB-GUIDE.md](lab/LAB-GUIDE.md).

## Project Manager AI Playbook

[`playbook/`](playbook/PM-PLAYBOOK.md) holds 40 skills for project managers,
grouped by phase. It works with Microsoft Copilot, ChatGPT, Gemini or GitHub
Copilot, with no Claude needed:

- [`playbook/PM-PLAYBOOK.md`](playbook/PM-PLAYBOOK.md): read it on GitHub, with a link to every skill
- [`playbook/pm-playbook.html`](playbook/pm-playbook.html): download it and open it in a browser. It works
  offline, with copy and download buttons for every skill
- `playbook/skills/`: each skill as one `.md` file (any AI) and a `.prompt.md` file (GitHub Copilot)

Edit `playbook/pm-playbook.json`, then rebuild with `python3 tools/build_playbook.py`.

## Add your own skill

```bash
python3 tools/new_skill.py sprint-goal-coach --category "Scrum events" \
  --job "Write a sharp, testable Sprint Goal" --level beginner \
  --try "Help us write a Sprint Goal for the login revamp" --author "Your Name"
```

That creates `skills/sprint-goal-coach/SKILL.md` from the template, adds the
skill to `library.json` and refreshes the docs. Write the description and
body, then check it:

```bash
python3 tools/validate_library.py
```

To list a skill that lives in someone else's repo instead, add an entry to
`library.json` with `"source": {"repo": "owner/name", "ref": "<commit sha>", "path": "folder"}`.
Pin a commit you have read, not a branch.

## Updating the library

Edit `library.json`, then run `python3 tools/build_docs.py` to refresh
`LIBRARY.md` and the page. The site's title, tagline and eyebrow text come
from the `site` block at the top of `library.json`.

## Publishing the website

1. In GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Push to `main`. The *Publish skills site* workflow validates the library,
   builds `_site/` and deploys it.

Each skill stored in this repo gets its own downloads on the site: a `.zip`
for the Claude app, a single-file `SKILL.md`, a Copilot `.prompt.md` and a
plain `.txt` for any chat. Skills from other authors link to their repo and
are never re-hosted.

Preview locally:

```bash
python3 tools/build_docs.py && python3 tools/build_site.py && python3 -m http.server -d _site 8000
```

## Credits

This library builds on the Agile36 Scrum Master skills kit. Agile36 wrote 15 of the skills: the Scrum event and SAFe skills, the team and
facilitation skills, `impediment-log`, `planning-poker`, `protect-the-sprint`
and `metrics-conversation`. Those skills, the lab, the page and the
tools are licensed [CC BY 4.0](LICENSE): share and adapt them, including
commercially, with credit to Agile36.

Other skills belong to their authors and keep their own licenses; see
[LIBRARY.md](LIBRARY.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
