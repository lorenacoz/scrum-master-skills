# Lab: Build Your Own Scrum Master Skill

**Goal:** leave with a working Scrum Master skill you wrote yourself, tested,
and runnable in at least two AI tools.

**You need:** a text editor and access to one AI tool. No coding required.

A skill is a folder with one file, `SKILL.md`, that teaches an AI how to do one
job your way. That's it. Everything else is optional.

---

## Module 0: Install and use the library (30 min)

Install the Agile36 library in the tool you use at work. For Claude Code:

```bash
curl -fsSL https://raw.githubusercontent.com/lorenacoz/scrum-master-skills/main/tools/install_library.py | python3 -
```

Other tools: see "Install it" in `../LIBRARY.md`. Then run the "Try this"
prompt for at least three skills, including one Scrum event skill.

**Deliverable:** which skill would you use next sprint, and for what?

## Module 1: Read the library (30 min)

Now open the skills you just used and read how they work. Start with
**daily-scrum** (`../skills/daily-scrum/SKILL.md`), Agile36's reference skill,
then one more. For each, answer:

1. **Description**: what words make it fire? Did it fire when you expected in Module 0?
2. **Scope**: what does it leave to the human?
3. **Structure**: what's in `SKILL.md` vs. `references/`?
4. **Rules**: what are its "never" and "always" lines?
5. **Portability**: would it work pasted into another AI tool?

**Deliverable:** write two lines: one thing you'd copy, one thing you'd change.

## Module 2: Anatomy of a skill (20 min)

Look at the reference skill and find these parts:

| Part | What it does | In the reference skill |
|---|---|---|
| `name` | Identifier | `daily-scrum` |
| `description` | **The trigger.** The AI reads this to decide whether to use the skill. Note the "Not for…" line pointing to other skills | Frontmatter |
| Role line | Who the AI is, and who owns the meeting | "The Daily Scrum belongs to the Developers" |
| Ask-first block | Stops it guessing | "First, find out" |
| Routing table | Picks the right play for the situation | "Pick the play" |
| `references/` | Detail loaded only when needed | None here; see `scrum-retrospective/references/` |
| Rules | The guardrails | "Rules" |

**Key idea:** the description decides *when*; the body decides *how*. Most
broken skills have a vague description.

## Module 3: Choose your job (15 min)

Pick **one** Scrum Master job. Narrow beats broad.

- Good: "Prepare a retrospective for a team that keeps repeating the same complaints"
- Too broad: "Be my Scrum Master"

Fill in:

1. The job, in one sentence an observer could check
2. Who uses it, and in what moment
3. What the AI must ask before answering
4. What it must never do (at least two)
5. What a great output looks like (paste a sample)

## Module 4: Write it (45 min)

Copy `SKILL.template.md` into a new folder named after your skill. Then:

1. Write the `description` last-but-one: include phrases a real person types
2. Fill the role line, ask-first block, rules and output defaults
3. Keep `SKILL.md` under ~100 lines. Move detail into `references/`
4. Keep rules concrete. "Don't rank individuals" beats "be fair"

## Module 5: Test it (30 min)

Use `test-prompts.md`. Write the prompts, run them, score them, and fix **one
line at a time**. Do this at least twice.

## Module 6: Make it portable (20 min)

Skills are just markdown, so any AI can use them. Different tools load them
differently:

| Tool | How it loads the skill |
|---|---|
| Claude (Code/desktop) | Folder in the skills directory. Loads by `description` |
| GitHub Copilot | `.github/instructions/*.instructions.md` or a `.github/prompts/*.prompt.md` file |
| Any other AI | Paste the body as the first message or system prompt |

Run the exporter:

```bash
python3 ../tools/export_skill.py path/to/your-skill --out out
```

It creates a Copilot version, an `AGENTS.md` version, and a paste-anywhere
version, with your `references/` files folded in (other tools don't load them
on demand). Open the output and try it in a second tool.

**Check:** does it behave the same? Note one difference.

## Module 7: Demo (see `DEMO-KIT.md`)

Present your two favorite library skills (or one plus your own).

---

## Common mistakes

- Description says "helps with agile". Nothing triggers on that.
- Skill tries to do six jobs. Split it.
- No "ask first" block, so it invents team facts.
- Rules written as values, not behaviors.
- Never tested with a prompt that should *not* trigger it.

## Instructor notes

- Module 1 and 2 can be a live walkthrough of the reference skill
- Students without terminal access can do Module 6 by pasting the body manually
- Keep the library open during Module 4; copying structure is encouraged
