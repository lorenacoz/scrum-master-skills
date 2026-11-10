---
description: "Turns meeting notes into an accountable register and diagnoses recurring meetings. Use when commitments get dropped or a series decides nothing; for a single meeting's recap use summarize-meeting."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Meeting Analyzer

Meetings fail at the seam between talking and tracking. The decision gets made
and nobody records who approved it; the action gets stated and nobody's name
lands on it; the same topic returns for the seventh week because discussing it
feels productive and deciding it feels risky. This skill closes that seam with
deterministic extraction — pattern rules, no model calls — and then follows the
commitments across meetings to see which ones actually close.

## Scope note

This is the **accountability** lens on meetings, not the summary lens. It
extracts and tracks; it does not write the polished recap. Use it on notes that
already exist, across a series, when the question is "did anything we said we
would do actually happen?"

## When to use this skill

- **Actions keep getting dropped** — items agreed in one meeting quietly
  reappear three weeks later, or never do
- **A recurring meeting feels pointless** — you need decision density and topic
  churn measured before proposing to cancel it
- **Notes exist but no register does** — months of markdown notes with decisions
  buried in prose that nobody can find or count
- **The same topic returns every week** — you need evidence of churn to force a
  decision owner and a deadline
- **Preparing a retro or a meeting audit** — completion rates and ageing per
  meeting show which rituals produce work that gets done
- **Onboarding onto an existing project** — extracting the decision log from
  past notes reconstructs why the system looks the way it does

## Inputs the skill expects

- Meeting notes or transcripts as markdown or plain text, one file per meeting
- Ideally several meetings from the same series, so trends are visible
- An action-item register with created date, due date, owner, status and
  carry-over count (the parser bootstraps this from notes)
- Per-occurrence series data: attendance, duration, decisions, actions, whether
  an agenda was posted and notes published, and the topics covered
- The reference date for ageing calculations, if not "the newest date in the data"
- Which meeting types to exclude from decision-density scoring (retros,
  brainstorms, incident reviews legitimately decide little)

## Clarify First

Before generating, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Whether owners and dates may be inferred:** the answer is no by default; a fabricated due date enters the tracker looking legitimate and is far more damaging than a flagged gap.
- **Meeting type:** a retro or brainstorm scored on decision density will look broken when it is working exactly as intended.
- **The reference date for ageing:** "overdue" is meaningless without it, and pulling from the system clock makes yesterday's report irreproducible.
- **Who sees the per-owner output:** aggregate for the team, per-person only in a 1:1; low follow-through is usually over-assignment, not under-delivery.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflows

### Workflow 1 — Extract an accountable register from raw notes

1. Point the parser at the notes file. It buckets every item into decisions,
   actions and open questions, and pulls owner and due date from each action.
2. Read the completeness rate first. Anything under 60% means the meeting
   produced intentions, not commitments.
3. Work the flagged gaps **in the room or in the thread the same day**. Asking
   "who owns this?" a week later means reconstructing a conversation nobody
   remembers, and the answer becomes whoever feels most guilty.
4. Never infer a missing owner or date. A flagged gap is the deliverable — it is
   the thing that gets fixed.
5. Add `--strict` in CI over a notes directory to fail the build when a meeting
   lands actions with no owner or date.

```bash
python3 scripts/meeting_notes_parser.py \
  --input assets/sample_notes.md \
  --format text --strict
```

### Workflow 2 — Track follow-through across a series

1. Append each meeting's extracted actions to a register in
   `assets/sample_commitments.json` shape, keeping `created`, `due`, `owner`,
   `status` and `carried_over`.
2. Run the tracker with an explicit `--as-of` so the report is reproducible.
3. Read in this order: completion rate, the ageing distribution, then per
   meeting. Per-owner comes last and never first.
4. Act on the 30+ day band — close, reassign, or explicitly drop. An action
   auto-closed at 30 days that genuinely mattered gets re-opened within a week;
   one that nobody notices did not matter.
5. Apply the three-strike rule to anything with `carried_over >= 3`: re-commit
   with a date the owner states out loud, or drop it. There is no fourth carry.

```bash
python3 scripts/commitment_tracker.py \
  --input assets/sample_commitments.json \
  --as-of 2026-07-21 --format text
```

### Workflow 3 — Diagnose a recurring meeting that decides nothing

1. Assemble 8-12 occurrences with attendance, decisions, actions, agenda and
   notes compliance, and the topics covered.
2. Run the diagnostic. It returns decision density, churning topics, attendance
   trend, and a KEEP / RESTRUCTURE / ASYNC / KILL verdict with a prescription.
3. Check the exclusions before acting — retros and brainstorms score badly by
   design and should be removed from the input, not accommodated by lowering
   the floor.
4. Take the churning topics to the room with the one diagnostic question: *who
   can actually decide this?* The answer picks the fix.
5. Fix hygiene before cancelling. A series at 30% agenda compliance has not yet
   been tried as a well-run meeting.

```bash
python3 scripts/meeting_series_diagnostic.py \
  --input assets/sample_series.json \
  --churn-threshold 3 --format text
```

## Decision frameworks

### The action-item completeness gate [PROVEN]

| Has owner | Has date | Verdict |
|-----------|----------|---------|
| Yes | Yes (ISO) | Tracked |
| Yes | Vague ("soon", "next sprint") | **Gap** — the owner believes they committed; nobody else does |
| Yes | None | **Gap** — reads as "someday" |
| No | Either | **Gap** — an action owned by "the team" is owned by nobody |

`we`, `the team`, `someone`, `everyone` and `TBD` are never owners, even when
they occupy the grammatical slot. Accepting them launders the gap instead of
surfacing it.

### Follow-through benchmarks [RECOMMENDED]

| Metric | Healthy | Warning | Broken |
|--------|---------|---------|--------|
| Completion rate | 75%+ | 50-75% | under 50% |
| Owner **and** date present | 90%+ | 70-90% | under 70% |
| On-time closure | 70%+ | 50-70% | under 50% |
| Open beyond 30 days | 0-1 | 2-4 | 5+ |
| Average carry-over | under 1 | 1-2 | 3+ |

Carry-over predicts abandonment better than age. An item carried three times has
usually been silently deprioritised by its owner but never formally dropped.

### Decision density verdicts [PROVEN]

Density = decisions produced / person-hours consumed.

| Density | Verdict | Action |
|---------|---------|--------|
| 0.35+ | KEEP | Healthy: a 60-min meeting of 5 produces 2+ decisions |
| 0.15-0.35 | RESTRUCTURE | Cut duration 25%; trim to the people who hold the decision |
| under 0.15 | ASYNC | Move standing content to a written update |
| under 0.15 **and** 40%+ empty occurrences | KILL | Cancel; replace with a written update and a comment window |

Exclude retros, brainstorms, incident reviews and onboarding — they decide
little by design. Exclude them explicitly rather than lowering the floor, or the
floor stops catching the status meetings it exists to catch.

### Reading low follow-through

Low follow-through has four common causes and only one of them is the person:
over-assignment (one owner holding 40%+ of open actions), deadlines set by
someone other than the owner, an unclearable blocking dependency, or a meeting
generating more actions than the team has capacity for. **When every owner looks
bad, the meeting is the problem** — see the diagnostic table and per-owner
interpretation guidance in `references/accountability-and-series-health.md`.

## Anti-Patterns

### Inferring the Missing Owner
**Mistake:** Filling in a plausible owner or date for an action the notes left blank, so the register looks complete.
**Why it happens:** An incomplete register feels like a failure of the extraction, and a model will happily supply a name. Completeness is mistaken for quality.
**Instead:** Leave it flagged. The gap **is** the finding — an unowned action is genuinely unowned, and surfacing it is the entire value. Rules under-extract and models over-extract; a fabricated due date enters the tracker looking legitimate and nobody ever questions it again.

### The Decorative Register
**Mistake:** Maintaining a meticulous action list that is reviewed by reading every row aloud at the next meeting, and never acted on.
**Why it happens:** The register becomes a performance of diligence. Reading it all feels thorough, and cutting the review feels like letting standards slip.
**Instead:** Review overdue items and third carry-overs only — under five minutes. Everything on track needs no airtime. A register that consumes twenty minutes a week to change nothing is more expensive than having no register.

### Weaponising Per-Owner Data
**Mistake:** Opening a team meeting with the per-owner follow-through table and asking the bottom name to explain themselves.
**Why it happens:** The data looks like performance data, and it is right there, ranked.
**Instead:** Share follow-through in aggregate with the team and per-person only in a 1:1, as a question rather than a verdict. When every owner looks bad, the meeting is over-generating actions — treating that as several simultaneous performance problems is both wrong and expensive, and it teaches people to accept fewer actions rather than to close more.

### Scoring Every Meeting on Decision Density
**Mistake:** Running the series diagnostic across the whole calendar and proposing to cancel the retro because it produced two decisions in ten weeks.
**Why it happens:** The metric is clean and comparable, which makes it tempting to apply universally.
**Instead:** Exclude retros, brainstorms, incident reviews and onboarding before scoring. Their output is shared understanding, not convergence. Excluding them keeps the floor sharp enough to catch the status meeting it was built for.

### Cancelling Before Fixing Hygiene
**Mistake:** Killing a low-density meeting that never had an agenda or published notes.
**Why it happens:** The density number is damning and cancellation is a satisfying, visible action.
**Instead:** Fix hygiene first — agenda-or-cancel plus published notes — and re-measure over four occurrences. A series at 30% agenda compliance has not been tried as a well-run meeting yet, and cancelling it moves the same unresolved topics somewhere less visible.

**Exit codes (all three tools):** `0` report produced · `1` `meeting_notes_parser.py --strict` only: an action has no owner or no date · `2` missing or unreadable file, invalid JSON, or the wrong shape. CI can tell a broken input (2) from a failed check (1).

## Files

| File | Purpose |
|------|---------|
| `scripts/meeting_notes_parser.py` | Extracts decisions, actions and questions from notes; detects owners and dates; flags gaps; `--strict` exits 1 |
| `scripts/commitment_tracker.py` | Ageing, completion and on-time rates, carry-over, per-owner and per-meeting breakdowns, deterministic `--as-of` |
| `scripts/meeting_series_diagnostic.py` | Decision density, churning topics, attendance decay, hygiene compliance, KEEP/RESTRUCTURE/ASYNC/KILL verdict |
| `references/extraction-rules-and-note-conventions.md` | Cue catalogue, owner/date detection, reflow, source-format handling, deduplication, note conventions, failure modes |
| `references/accountability-and-series-health.md` | Commitment lifecycle, benchmarks, per-owner interpretation, decision density, topic churn, action caps, escalation ladder |
| `assets/action_register_template.md` | Register: open actions, third-carry-over gate, decision log, open questions, health snapshot |
| `assets/sample_notes.md` | Wrapped markdown notes, mixed-quality actions (extracts at 33% completeness) |
| `assets/sample_notes_transcript.txt` | Labelled transcript (extracts at 100%) — the contrast shows what note conventions buy |
| `assets/sample_commitments.json` | 18-action register across 5 meetings and 7 weeks |
| `assets/sample_series.json` | 10 occurrences of a weekly alignment meeting |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/accountability-and-series-health.md

# Accountability and Meeting-Series Health

The models behind commitment tracking and recurring-meeting diagnosis: the
lifecycle an action item moves through, the benchmarks that separate a healthy
register from a decorative one, and how to tell a meeting that decides things
from one that discusses them. Read this when interpreting tracker output, when
follow-through is poor, or when deciding whether to cancel a recurring meeting.

---

## 1. The commitment lifecycle

An action item passes through five states. Most registers only model three, and
the two they skip are where the failures live.

| State | Definition | Failure at this state |
|-------|-----------|-----------------------|
| **Stated** | Said aloud in a meeting | Never written down; exists only in memory |
| **Recorded** | Written with text, owner, date | Recorded without an owner or date — the dominant failure |
| **Accepted** | The owner has acknowledged it | Assigned to someone absent, who never agreed |
| **In progress** | Work has started | Sits at "accepted" for weeks; nobody notices |
| **Closed** | Done, dropped, or explicitly reassigned | Silently abandoned instead of explicitly dropped |

**Accepted is the state teams skip.** Assigning an action to someone who was not
in the room, or who did not verbally take it, produces an item that will not
move and will not be escalated, because the assigner believes it is handled.
Rule: an action assigned to an absent person is provisional until they confirm,
and the register should show it as such.

**Closed includes dropped.** An action the team consciously decides not to do is
closed, not deleted. Deleting it destroys the signal that the meeting generated
work nobody valued — which is exactly the signal the series diagnostic needs.

---

## 2. The two accountability gaps

Every incomplete action has one of two gaps, and they fail differently.

### No owner

"The team will document the metric definitions." Nobody's name is on it, so
nobody's week is affected by it. Diffusion of responsibility is not a character
failing; it is the predictable result of a plural subject.

**Fix at capture time, not at review time.** The note-taker asks "who?" in the
room. Asking a week later means reconstructing a conversation nobody remembers,
and the answer is usually whoever feels most guilty rather than whoever is
right.

### No date, or a vague one

"Lena will produce the breakdown soon." The owner is real; the deadline is not.
Vague dates are worse than absent ones because the owner believes they have
committed, and the requester believes they have received a commitment, and the
two beliefs are about different weeks.

**Ban the vague-date vocabulary explicitly:** soon, ASAP, next sprint, when I
get a chance, in the next few days, eventually. Each has a real date behind it
that the owner is avoiding saying out loud — usually because they are not sure
they can hit it, which is itself the information the room needs.

---

## 3. Follow-through benchmarks [RECOMMENDED]

| Metric | Healthy | Warning | Broken |
|--------|---------|---------|--------|
| Completion rate (closed / total) | 75%+ | 50-75% | under 50% |
| Actions with owner **and** date | 90%+ | 70-90% | under 70% |
| On-time closure (closed by due date) | 70%+ | 50-70% | under 50% |
| Open actions older than 30 days | 0-1 | 2-4 | 5+ |
| Average carry-over count | under 1 | 1-2 | 3+ |

**Completion rate below 50% means the meeting is producing intentions, not
commitments.** At that level the register has stopped being a tracking tool and
become a record of good intentions, which nobody reads and everybody stops
adding to. The recovery is not exhortation — it is cutting the number of
actions the meeting is allowed to generate.

### Carry-over is the leading indicator

Carry-over — the number of times an action has been rolled into the next
meeting without progress — predicts abandonment better than age does. An item
carried three times has usually been silently deprioritised by its owner but
never formally dropped, so it keeps consuming review minutes.

**The three-strike rule:** at the third carry-over, the item is either
re-committed with a new date **stated out loud by the owner**, or explicitly
dropped. It does not get a fourth. This one rule reclaims more review time than
any other change to the ritual.

---

## 4. Reading per-owner data without weaponising it

Per-owner follow-through is the most misusable output in this skill. Low
follow-through has four common causes and only one of them is the person.

| Signal | Likely cause | Response |
|--------|--------------|----------|
| One owner holds 40%+ of open actions | Over-assignment, not under-delivery | Redistribute; the room is defaulting to the reliable person |
| High completion, low on-time | Deadlines set by others, not the owner | Have the owner state the date in the room |
| Many `blocked` items | Dependency the owner cannot clear | Escalate the dependency, not the person |
| Low completion across every owner | The meeting generates more actions than the team has capacity for | Cap actions per meeting |

**When every owner looks bad, the meeting is the problem.** A register where
nobody clears their items is describing a capacity mismatch. Treating it as
eight simultaneous performance issues is both wrong and expensive.

Use the data in aggregate with the team, and per-person only in a 1:1 — and
then as a question, not a verdict.

---

## 5. Decision density

**Decision density = decisions produced / person-hours consumed.**

It is the best single measure of whether a recurring meeting earns its cost.
Decisions are countable, hard to inflate without actually deciding something,
and directly connected to why synchronous time is expensive: the whole reason to
put people in a room simultaneously is to converge.

| Density | Reading |
|---------|---------|
| 0.35+ | Healthy — a 60-minute meeting with 5 people produces 2+ decisions |
| 0.15-0.35 | Inefficient — real decisions, too much time or too many people |
| under 0.15 | Below the floor — this is a broadcast or a discussion group |

**What density does not measure.** Brainstorms, incident reviews, retros and
onboarding sessions legitimately produce few decisions and should be excluded
rather than scored badly. Exclude them explicitly; do not lower the floor to
accommodate them, or the floor stops flagging the status meetings it exists to
catch.

### The three diagnoses of a low-density series

1. **Wrong people.** The room lacks whoever can actually decide, so every thread
   ends in "let's take that away". Fix: shrink to the decision owner plus the
   people whose input changes the decision.
2. **Wrong format.** The content is status. Fix: convert to a written update
   with a comment window.
3. **Wrong preparation.** No agenda and no pre-read, so half the time is spent
   loading context. Fix: agenda-or-cancel, plus a pre-read circulated 24 hours
   ahead.

---

## 6. Topic churn

A topic that recurs on the agenda without ever resolving is the clearest signal
that a meeting is substituting discussion for decision.

**Detection heuristic:** a topic is churning when it has appeared 3+ times and
fewer than a third of those appearances coincided with any decision. Since notes
rarely attribute decisions to specific topics, same-occurrence decisions are the
available proxy — treat the output as a shortlist to inspect, not a verdict.

Churn has three causes, distinguishable by asking one question — *who can
actually decide this?*

| Answer | Cause | Fix |
|--------|-------|-----|
| "Nobody in this room" | The decision right sits elsewhere | Escalate; take it off this agenda |
| "It depends who you ask" | Ownership is genuinely contested | Resolve ownership first — that is the real decision |
| "We could, but we keep not" | Missing information, or avoidance | Name the information needed and its owner, with a date |

The third case is the most common and the most expensive. A topic the group is
avoiding will consume ten minutes every week indefinitely, because raising it
feels productive and resolving it feels risky.

---

## 7. Attendance decay

Attendance across a series is the team's revealed preference, and it is more
honest than any survey.

**Signal:** a 15%+ drop between the first and second half of a series indicates
people have concluded it is optional. By the time attendance has decayed this
far, the meeting has usually been unproductive for two months.

Decay interacts badly with notes discipline. When notes are not published,
absentees fall behind, so attendance becomes compulsory to stay informed — which
props up attendance in a meeting nobody values. **High attendance plus low
decision density plus no published notes is a meeting held hostage**, not a
healthy one. Publishing notes is what lets attendance tell the truth.

---

## 8. The review ritual

Reviewing the register is itself a meeting cost. Keep it under five minutes.

**What to review, in order:**

1. **Overdue items only.** Not everything. On-track items need no airtime.
2. **Third-carry-over items.** Re-commit with a date, or drop. No third option.
3. **Unowned and undated items from the last meeting.** Assign now or delete —
   they will not survive another week.
4. **Nothing else.** Reading the full register aloud is how a five-minute review
   becomes a twenty-minute one, and it is why teams stop doing it.

### Escalation ladder for stale actions [RECOMMENDED]

| Age past due | Action |
|--------------|--------|
| 1-7 days | Owner posts a new date in the channel. No meeting time. |
| 8-21 days | Named in the review; owner states the blocker out loud |
| 22-30 days | Owner's manager is looped in — as a capacity question |
| 30+ days | Closed as dropped, with a note saying so |

The last row is the one that matters. **Auto-closing at 30 days is not giving
up** — it is refusing to maintain a fiction. If the item genuinely matters, its
closure will be noticed within a week and it will be re-opened with a real date.
If nobody notices, it did not matter, and the register is now honest again.

---

## 9. Capping actions per meeting

The most effective intervention on a broken register is not better tracking. It
is generating fewer commitments.

**Rule of thumb:** a 60-minute meeting of five people can absorb **three to five
actions**. Beyond that, the marginal action is a wish. Teams that leave meetings
with twelve actions close about the same absolute number as teams that leave
with four — the extra eight simply arrive stale.

| Meeting length | Attendees | Sustainable actions |
|----------------|-----------|--------------------|
| 25 min | 3-5 | 1-2 |
| 50-60 min | 4-7 | 3-5 |
| 90 min (planning) | 5-9 | 5-8 |

When the room generates more than the cap, close the meeting by asking which
three matter this week and explicitly parking the rest. Parked is a real state
and it is honest; "assigned" for something nobody will start is not.

**Watch the ratio.** Actions per decision above roughly 4:1 means the meeting is
distributing work rather than converging on choices. That is not automatically
wrong — planning meetings look like this by design — but in a session billed as
a decision forum it means the decisions are being deferred into tasks.

---

## 10. Reconstructing a decision log from history

A frequent request when joining a project: *why is the system like this?*

1. **Extract decisions from all past notes.** Ignore the actions entirely —
   they are stale and reconstructing them wastes the effort.
2. **Order chronologically and mark supersession.** Later decisions frequently
   overturn earlier ones without saying so, and an unmarked superseded decision
   is worse than a missing one because someone will act on it.
3. **Flag decisions with no recorded approver.** These are the fragile ones —
   they will be re-litigated by whoever was absent, and knowing which they are
   tells you where to expect resistance.
4. **Note what is missing.** A system behaviour with no decision behind it in
   the record was either decided informally or never decided at all. Both are
   worth knowing before you change it.
5. **Publish it once and maintain it going forward.** A reconstruction that is
   not maintained decays within a quarter and is then actively misleading.

Expect to recover perhaps 60% of the real decision history. That is enough to
answer most "why is this like this" questions and to identify the two or three
load-bearing choices worth asking a long-tenured colleague about directly.

---

## 11. Interpretation traps

| Trap | Why it misleads | Correct reading |
|------|-----------------|-----------------|
| High action count read as productivity | Generating work is easy; closing it is not | Read completion rate, not volume |
| 100% completion read as excellence | Often means only trivially safe actions get recorded | Check whether hard items are being recorded at all |
| Rising completion after a review push | Owners closing easy items to clear the board | Check on-time rate and the age of what closed |
| One meeting with poor completion | May legitimately own the hardest work | Compare action *difficulty*, not just counts |
| Low decision count in a retro | Retros produce understanding, not decisions | Exclude retros from density scoring |
| Zero overdue items | Suspiciously clean; dates may be set after the fact | Check whether due dates precede closure dates |

**100% completion deserves as much scrutiny as 40%.** A register where
everything closes on time is usually a register that only receives safe,
already-started work, while the genuinely uncertain commitments are made verbally
and tracked nowhere. Ask which of the last month's hardest problems appear in
the register. If none do, the register is measuring the wrong things
successfully.

---

## 12. Wiring this into an existing ritual

The tracking only works if it attaches to something the team already does.

| Ritual | Attachment point | Duration added |
|--------|-----------------|----------------|
| Weekly working session | Parse notes after; review overdue at the top of the next | 5 min |
| Sprint retro | Bring completion rate and carry-over counts as data | 5 min |
| Meeting audit | Run the series diagnostic across the recurring calendar | one-off |
| Quarterly planning | Decision log review — what did we commit to, what changed | 15 min |

Do **not** create a new meeting to review the register. A team whose response to
poor follow-through is an additional recurring meeting has diagnosed the problem
exactly backwards, and the new meeting will itself generate actions nobody
closes.

## references/extraction-rules-and-note-conventions.md

# Extraction Rules and Note Conventions

The rule catalogue behind deterministic extraction of decisions, actions and
open questions from meeting artefacts — plus the note-taking conventions that
make extraction reliable in the first place. Read this when tuning the parser
for a team's house style, when extraction quality is poor, or when defining how
a team should take notes.

---

## 1. Why rules rather than a model

Pattern rules are the right tool here for four reasons, and it is worth being
explicit about them because the instinct is to reach for a model.

1. **Auditability.** When an action is missed, you can point at the rule that
   did not fire and add a cue. A model that missed it gives you nothing to fix.
2. **Determinism.** The same notes produce the same register every time, so a
   diff between two runs means the notes changed — not the extractor.
3. **The failure mode is safe.** Rules under-extract; they miss items. Models
   over-extract, inventing owners and dates that were never agreed. A fabricated
   due date is far more damaging than a missed line, because it enters the
   tracker looking legitimate.
4. **Cost and latency.** Extraction runs on every meeting, forever.

The trade is real: rules need note conventions to work well. Section 4 covers
the conventions, and they are worth adopting regardless — they make the notes
better for humans too.

---

## 2. Cue taxonomy

Cues split into **strong** and **weak**. Strong cues fire anywhere, including
mid-paragraph. Weak cues fire only inside a list item or under a matching
section heading, where the surrounding structure already signals intent. This
two-tier design is what keeps discussion prose out of the action register — the
single largest source of false positives.

### Decision cues [PROVEN]

| Pattern | Example it catches |
|---------|--------------------|
| `DECISION:` / `Decision -` label | `DECISION: we ship behind a flag` |
| `we decided to/that` | `We decided to defer the migration` |
| `agreed to/that/on` | `Agreed to hold the September date` |
| `we're going with` | `We're going with the stopgap importer` |
| `we will <commit verb>` | `We will build the importer` |
| `approved`, `signed off`, `resolved to` | `Approved by Priya` |

The commit-verb list matters: `we will use / adopt / ship / keep / build / hold
/ move / go`. A bare `we will` is too loose — "we will need to think about it"
is not a decision, and admitting it as one inflates the decision count, which is
the metric the series diagnostic runs on.

### Action cues

**Strong** — fire anywhere:

| Pattern | Example |
|---------|---------|
| `ACTION:` / `TODO:` / `Next step:` label | `ACTION: open the PR` |
| `@name to` / `@name will` | `@lena to confirm the schema` |
| `^Name will <verb>` / `^Name to <verb>` | `Sam will scope the importer` |
| `[ ]` checkbox | `- [ ] draft the contract` |
| `takes the action` | `Kai takes the action` |

**Weak** — only in list items or an actions section:

| Pattern | Why it is weak |
|---------|----------------|
| `will <verb>` | Matches narrative future tense: "the migration will take a week" |
| `to <task verb>` | Matches infinitives everywhere in prose |
| `owns this/it` | Matches ownership discussion, not assignment |
| `needs to` | Frequently describes a system, not a person |

### Open-question cues

**Strong:** `Open question:`, `^TBD`, `still unclear/unknown/open/undecided`,
`we don't know`, `no resolution`.
**Weak:** `needs investigation/research/input`, inline `TBD`, a line ending in
`?`.

The trailing-`?` rule must stay weak. Transcripts are full of conversational
questions that were answered thirty seconds later; only a question captured in
a structured position is genuinely open.

---

## 3. Field extraction

### Owner detection, in priority order

1. `@handle` — highest confidence, unambiguous.
2. `Owner: Name` — an explicit label.
3. `^Name will|to|owns|takes` — a capitalised name at the start of the item.

Extraction runs against the **cleaned** text — after list markers, checkboxes
and leading labels are stripped — so `ACTION: Sam to open the PR` still matches
the `^Name` anchor. Running it against the raw line is the most common reason
owner detection silently fails on well-labelled notes.

**Reject-list.** `we`, `the`, `team`, `someone`, `everyone`, `tbd` are never
owners even when they occupy the grammatical slot. "The team will handle it"
must register as **unowned**, because that is exactly what it is. Accepting
"team" as an owner is the difference between a tracker that surfaces the
accountability gap and one that launders it.

### Date detection

| Format | Example |
|--------|---------|
| ISO | `2026-07-22` |
| Day-month | `18 Jul`, `18 July 2026` |
| Month-day | `Jul 18`, `July 18, 2026` |
| Relative anchored | `by next Tuesday`, `by EOW` |

**Vague dates are recorded as a distinct gap**, not as a date: `soon`, `next
sprint`, `ASAP`, `when I can`, `in the next few days`, `eventually`, `at some
point`. These are worse than no date, because they feel like a commitment to
the person saying them and read as nothing to everyone else. Flag them
explicitly — "Lena will produce the breakdown soon" needs a different
conversation than "Lena will produce the breakdown", and the tracker should say
which one it is.

**Relative dates are not resolved to calendar dates.** "Next Tuesday" depends
on the meeting date, which the parser may not know reliably. Recording the raw
string preserves the ambiguity honestly rather than inventing precision.

---

## 4. Line reflow

Notes are hard-wrapped. Without reflow, a wrapped decision extracts as its first
line only, which truncates exactly the clause that carries the rationale.

**Rule:** a line continues the previous one when it is not a heading, not a list
item, not a blockquote, and the previous line did not end on `.`, `!` or `?`.

A line ending in `:` **does** continue — `Approver:` on its own line followed by
the name is common, and treating `:` as a terminator splits the record from its
approver.

Line numbers are preserved from the **first** line of the joined unit, so the
register still points back to a findable location in the source.

---

## 5. Note conventions that make extraction reliable [RECOMMENDED]

Adopt these and rule-based extraction reaches roughly 90% recall. Without them
it sits closer to 60%, and the gap is entirely in the items that were sloppily
recorded — which are also the items least likely to get done.

### The five conventions

1. **Label decisions and actions with a keyword at line start.** `DECISION:`
   and `ACTION:` cost two seconds and remove all ambiguity. This one convention
   does more than the other four combined.
2. **One action per line.** "Sam will scope it and Lena will confirm the schema"
   extracts as one action with one owner. Split it.
3. **Owner first, then verb, then object, then date.** `Sam to open the importer
   PR by 2026-07-22`. This ordering is what the `^Name` anchor keys on.
4. **Always an ISO date.** "By Friday" is ambiguous across timezones and
   meaningless in a register read three weeks later.
5. **Name the approver on every decision.** `Approver: Priya`. A decision with
   no approver gets re-litigated by whoever was absent.

### The template line

```
DECISION: <what was decided, past tense>. Approver: <name>. <one-clause rationale>
ACTION: <Name> to <verb> <object> by <YYYY-MM-DD>
OPEN QUESTION: <the question>. Owner: <name>. Needs an answer by <YYYY-MM-DD>
```

An open question needs an owner and a date as much as an action does. An
unowned open question is how a known unknown becomes a surprise.

---

## 6. Known failure modes

| Failure | Cause | Mitigation |
|---------|-------|------------|
| Decision counted twice | Restated in a summary section at the end | Deduplicate on normalised text before counting |
| Discussion prose in the action list | A weak cue fired inside a section heading's scope | Narrow the section heading match, or move prose out of labelled sections |
| Action missed entirely | Phrased passively: "the importer needs opening" | Convention 3; passive actions have no owner by construction, so the gap is real |
| Owner detected as a false name | Sentence starts with a capitalised non-name | Extend the reject-list with the team's recurring vocabulary |
| Question captured mid-transcript that was answered | Trailing `?` in a conversational line | Keep the `?` rule weak; rely on `OPEN QUESTION:` labels |
| Everything extracts as one giant item | File uses single line breaks between paragraphs | Ensure blank lines between paragraphs before parsing |

### Calibrating on a team's own notes

Run the parser over four past meetings, then have the note-taker mark what it
missed and what it invented. Two rounds of cue additions typically close most of
the gap. Track recall (found / actually present) rather than raw counts —
a parser that finds 20 items when 30 exist looks productive and is not.

**Never tune toward higher extraction counts.** The metric is agreement with a
human reading of the same notes. A parser tuned to maximise items found becomes
a parser that reports discussion as commitment, and the register stops being
trustworthy — which is the only property it has.

---

## 7. Source-format handling

Different artefacts fail differently. Know which one you have before judging
the output.

| Source | Extraction quality | Characteristic problem | Preparation |
|--------|-------------------|------------------------|-------------|
| **Structured markdown notes** | Best | Wrapped lines truncating items | Ensure blank lines between paragraphs |
| **Labelled transcript** | Good | Conversational noise, filler questions | Keep the `DECISION:` / `ACTION:` blocks the note-taker added |
| **Raw auto-transcript** | Poor | No labels, no structure, decisions phrased conversationally | Have a human insert labels first; accept low recall otherwise |
| **Chat log** | Poor to fair | Decisions split across many short messages | Extract the summary message, not the whole thread |
| **Slide deck** | Very poor | Content is fragmentary and context-free | Do not parse; use the notes taken alongside it |

**Raw auto-transcripts are the hard case.** A decision in speech rarely looks
like one in text — "yeah, let's just do the six then" is a real decision that no
defensible rule set will catch without also catching a great deal of noise.
Ten seconds of a note-taker typing `DECISION:` at the moment it happens is worth
more than any amount of rule tuning after the fact.

### Handling a backlog of unlabelled notes

When extracting from months of past notes with no conventions:

1. Run the parser and expect roughly 50-60% recall. Treat it as a shortlist.
2. Focus on the decisions, not the actions. Old actions are stale; old decisions
   are still load-bearing and are what you actually need reconstructed.
3. Read the source around each hit — the parser points at a location, and the
   surrounding paragraph carries the rationale that makes the decision usable.
4. Write the recovered decisions into a proper log going forward. Do not attempt
   to retro-fix the source notes; that work is never finished and never used.

---

## 8. Deduplication

Meetings restate. A decision made mid-meeting and repeated in a closing summary
extracts twice, which inflates decision counts and corrupts the density metric
the series diagnostic runs on.

**Normalise before counting:** lowercase, strip punctuation, collapse
whitespace, drop leading labels, then compare. Items sharing a normalised prefix
of 60+ characters are near-certainly the same item.

Prefer the **later** occurrence when deduplicating decisions — a closing summary
usually states the final form, after amendments. Prefer the **earlier**
occurrence for actions, since that is where the owner and date were negotiated.

Do not deduplicate across meetings. The same action appearing in three
consecutive meetings is not a duplicate; it is a **carry-over**, and it is one
of the most valuable signals in the register. Collapsing carry-overs into one
item destroys exactly the data that predicts abandonment.

---

## 9. Quick reference — the conventions card

Give this to whoever takes notes. It is the whole intervention.

```
DECISION: <what was decided, past tense>. Approver: <one name>. <why, one clause>
ACTION:   <Name> to <verb> <object> by <YYYY-MM-DD>
OPEN QUESTION: <the question>. Owner: <name>. Answer needed by <YYYY-MM-DD>

Never write:  "the team will", "we should", "someone needs to"
Never write:  "soon", "ASAP", "next sprint", "when I get a chance"
One action per line. One owner per action. ISO dates only.
```

Five lines, adopted consistently, move rule-based extraction from roughly 60%
recall to roughly 90% — and they improve the notes for human readers by exactly
the same mechanism, because everything that makes an item machine-extractable
also makes it unambiguous to a person reading it three weeks later.

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/meeting-analyzer -->
