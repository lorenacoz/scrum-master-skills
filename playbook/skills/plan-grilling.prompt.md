---
description: "Interrogate a plan, design or idea one round of questions at a time until every decision is settled. Use when stress-testing a plan before building, when a design feels underspecified, or turning a fuzzy workflow into a spec."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Plan Grilling

A plan hides a tree of decisions, most of them made by accident. This skill
makes them explicitly. The agent walks the tree in rounds, asks only questions whose
prerequisites are settled, attaches its own recommended answer to each, looks
facts up instead of asking for them, and logs everything until nothing is left
silently assumed.

## When to Use

- Before committing build effort to a plan, design or migration
- When a design "feels done" but nobody can list its decisions
- When a recurring workflow should be handed to a script, agent or teammate and is not yet written down (multi-session mode)

## Clarify First

What most shapes a grilling is what it is meant to settle. Settle the inputs below before the first round. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **The subject:** the plan, design or workflow, in writing if it exists. The tree is built from it.
- **The decision-maker:** who answers decisions. A grilling answered by someone without authority settles nothing.
- **The destination:** a go/no-go, an agreed plan, or an implementable spec. It sets the stop criteria and whether multi-session mode applies.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

```bash
# Next round: the frontier, ordered by how many questions each unblocks
python3 scripts/question_log_checker.py \
  --input assets/sample_question_log_midway.json --stage round
# -> Next round: Q4, Q6, Q5   Blocked: Q10, Q7   (the resolved sample_question_log.json prints "none")
```

```bash
# Final gate before declaring the tree resolved (flawed sample exits 1)
python3 scripts/question_log_checker.py \
  --input assets/sample_question_log_flawed.json --format json
```

```bash
# Multi-session mode: is the workflow spec implementable?
python3 scripts/workflow_spec_checker.py \
  --input assets/sample_workflow_spec.json
```

## Tools Overview

| Tool | Checks |
|------|--------|
| `question_log_checker.py` | Category coverage, out-of-order questions, missing recommendations, unconfirmed assumed decisions, facts asked of the user, cycles, ownerless deferrals; prints the next round. `--stage final` also requires closure. |
| `workflow_spec_checker.py` | Trigger, steps with one actor, checkpoints with decision and brief, output destinations, testable done-criteria, no open questions. |

### Exit code contract

| Code | Meaning |
|------|---------|
| 0 | No error findings (warnings allowed) |
| 1 | Gate failed: at least one error finding |
| 2 | Bad input: missing file, invalid JSON, wrong shape |

## Workflow

1. **Build the tree.** [PROVEN] Draft questions across the taxonomy (goal, users, constraints, success, failure modes, reversibility, sequencing, ownership, unknowns). Record `depends_on` wherever one answer would change or remove another question.
2. **Split facts from decisions.** [PROVEN] Facts (how many users, what the code does) are the agent's job: look them up and log the source. Only decisions (the user's call) go to the user.
3. **Ask the frontier, one round at a time.** [RECOMMENDED] Run the checker with `--stage round`. Send at most five decisions, numbered, each with a recommended answer and a one-line reason, worded so "yes" accepts it. Never ask a question whose prerequisite is still open.
4. **Log verbatim and recompute.** Surface contradictions with earlier answers at once; defer superseded questions.
5. **Close the open ends.** Every unknown is resolved, deferred with an owner and reason, or accepted as an assumption the decision-maker confirmed.
6. **Run the quality gate.** [RECOMMENDED] `--stage final` must exit 0, then read the decisions back to the decision-maker; their agreement is the last checklist item.
7. **Multi-session mode.** [EXPERIMENTAL] For a recurring workflow: session 1 learns tools and vocabulary; the user runs it once by hand between sessions; later sessions settle steps, late checkpoints and failure handling. Validate with `workflow_spec_checker.py`. Risk: users describe the ideal workflow, not the real one, so insist on hand-run notes.

### Stop criteria

| Signal | Action |
|--------|--------|
| Frontier empty, gate exits 0, decisions read back and agreed | Stop: tree resolved |
| Only cheap two-way doors left, or user wants to start | Accept remaining recommendations or defer them to the user; list unvisited branches; stop |
| Goal still two goals, or a one-way door lacks failure/rollback answers | Do not stop |

## Anti-Patterns

### Asking the Whole Tree at Once
**Mistake:** Sending twenty questions in the first message, half of which depend on answers not yet given.
**Why it happens:** It feels thorough.
**Instead:** Ask only the frontier. Questions built on hypothetical answers get thrown away.

### Making the User Your Search Engine
**Mistake:** Asking "how many accounts have under ten seats?" and logging the guess.
**Why it happens:** Asking is faster than looking.
**Instead:** Resolve facts from code, data and docs, with a logged source.

### The Bare Question
**Mistake:** "How should we handle failures?" with no recommendation.
**Why it happens:** Offering an answer feels presumptuous.
**Instead:** Attach a recommended answer; agreement then costs one word.

### The Silent Assumption
**Mistake:** Filling an unanswered decision with the recommendation and moving on.
**Why it happens:** The user went quiet and momentum matters.
**Instead:** Get explicit confirmation; the checker fails unconfirmed assumed decisions.

### Grilling Without a Destination
**Mistake:** Questions continue indefinitely.
**Why it happens:** The destination was never set.
**Instead:** Fix it in Clarify First and stop on the criteria above.

## Files

| File | Purpose |
|------|---------|
| `scripts/question_log_checker.py` | Coverage, ordering, assumption and closure gate; prints the next round |
| `scripts/workflow_spec_checker.py` | Implementability gate for multi-session workflow specs |
| `assets/question_log_template.md`, `assets/workflow_spec_template.md` | Human-readable log and workflow spec templates |
| `assets/sample_question_log.json` / `_flawed.json` | Resolved grilling (exits 0) / out-of-order, assumed, cyclic log (exits 1) |
| `assets/sample_question_log_midway.json` | The same log after round 1, with a non-empty next round (exits 0 at `--stage round`) |
| `assets/sample_workflow_spec.json` / `_flawed.json` | Implementable spec (exits 0) / unready spec (exits 1) |

## Reference Documentation

- **[references/question-taxonomy.md](references/question-taxonomy.md)**: nine categories, probing questions, fact vs decision rules. Read when drafting rounds.
- **[references/running-the-grilling.md](references/running-the-grilling.md)**: frontier mechanics, round format, log fields, stop rules, multi-session mode, worked example. Read when running or resuming a session.

## Scope & Limitations

**In Scope:** building and walking a plan's decision tree in rounds; fact/decision separation; question logs with assumptions and deferrals; stop criteria; multi-session specification of recurring workflows.

**Out of Scope:**
- Imagining failure after launch and classifying risks (see `project-management/discovery/pre-mortem/`)
- Adversarial attack on a finished design or system (see `engineering/red-team/`)
- Mapping and testing assumptions with experiments (see `project-management/discovery/identify-assumptions/`)
- Breaking a large effort into decision tickets across many sessions (see `project-management/execution/wayfinder/`)

**Important Caveats:**
- The checkers verify the log's structure, not the quality of answers.
- `depends_on` and `round` are entered by hand; a wrong dependency gives a wrong frontier.

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/question-taxonomy.md

# Question Taxonomy for Plan Grilling

A grilling fails in one of two ways: it asks the wrong questions, or it asks the
right ones in the wrong order. This reference covers the first problem. Each of
the nine categories below names what it is for, the questions that usually pay
off, the answers that should make you dig further, and the questions that
usually come after it. Use it to draft rounds and to see which branches of the
tree have never been visited.

The seven **core** categories (goal, users, constraints, failure modes,
reversibility, sequencing, unknowns) must each carry at least one settled
question before a grilling can close; `question_log_checker.py` treats a missing
core category as a gate failure. **Success** and **ownership** are strongly
recommended and the checker warns when they are absent.

---

## 1. Goal

**Purpose:** pin down the outcome the plan exists to produce. Every later
answer is judged against it, so it is almost always the first round.

**Questions that pay off**

- What changes in the world when this is done, and for whom?
- If only half of this ships, which half must it be?
- What would make you call this a success even if the plan as written is abandoned?
- Is this the goal, or the first step towards a bigger goal? What is the bigger one?
- What are you explicitly *not* trying to achieve?

**Answers that should make you dig**

- "Both" or "all of the above" — two goals compete for every later trade-off.
  Force a ranking: "When they conflict, which wins?"
- An output instead of an outcome ("ship the dashboard"). Ask what the
  dashboard is for until you reach a behaviour or a number.
- A goal phrased as a solution ("migrate to the queue"). Ask what problem the
  queue removes.

**Usually unlocks:** success, users, constraints.

---

## 2. Users

**Purpose:** identify who is affected, who uses the result and who pays the
cost of change. Many plans name one user and silently harm a second.

**Questions that pay off**

- Who touches the result every day? Who touches it once a quarter?
- Who loses something when this ships (a report, a workaround, a habit)?
- How many of each are there? (A fact — look it up.)
- Which user's needs win when two conflict?
- Who will notice first if it breaks?

**Answers that should make you dig**

- "Everyone." There is always a primary user; name them.
- A number given from memory ("maybe 400?"). Facts belong to the agent: find the
  real figure before the next round.

**Usually unlocks:** constraints, failure modes, success.

---

## 3. Constraints

**Purpose:** list what cannot change — budgets, deadlines, contracts, formats,
regulation, headcount, systems that must keep working.

**Questions that pay off**

- What has to stay byte-identical, API-compatible or contractually unchanged?
- What is the hard deadline, and what happens on the day after it?
- What is the budget ceiling, in money and in people-weeks?
- Which approvals are mandatory, and how long do they take?
- What technology or vendor choices are already fixed?

**Answers that should make you dig**

- A deadline with no consequence attached. A deadline nobody pays for missing is
  a preference; treat it as such.
- "No constraints." Ask about the systems downstream; they are constraints.

**Usually unlocks:** sequencing, reversibility.

---

## 4. Success

**Purpose:** agree how anyone will know the goal was met, before work starts.

**Questions that pay off**

- What number moves, by how much, measured where, by when?
- What is the minimum result that still counts as success?
- What would tell us early (in days, not months) that we are off track?
- Who signs off that it worked?

**Answers that should make you dig**

- Unmeasurable words: "better", "smoother", "faster". Ask "faster than what,
  measured how?"
- A metric nobody currently collects. Then collecting it is a step in the plan.

**Usually unlocks:** failure modes, sequencing.

---

## 5. Failure modes

**Purpose:** walk the specific ways the plan breaks and decide, now, what
happens in each. This is not a full risk workshop; it is enough to make the
design decisions that failure forces.

**Questions that pay off**

- What happens when the main dependency is down for an hour? For a day?
- What happens on bad input, partial input, duplicate input?
- Who is told when it fails, how, and how fast?
- What is the blast radius of the worst plausible mistake?
- What failure would be silent — wrong but not erroring?

**Answers that should make you dig**

- "That won't happen." Ask what happened last time something similar did.
- Alerting with no recipient or no deadline.

**Usually unlocks:** reversibility, sequencing.

---

## 6. Reversibility

**Purpose:** sort decisions into one-way and two-way doors, because they deserve
different amounts of grilling. A two-way door can be decided fast and revisited;
a one-way door needs the full tree.

**Questions that pay off**

- If this turns out wrong in a month, what does undoing it cost?
- Which step destroys or migrates data, contracts or public promises?
- Can the old path stay deployable while the new one proves itself?
- What is the latest point at which we can still back out cheaply?

**Answers that should make you dig**

- "We can always roll back" with no rollback ever rehearsed.
- Any data migration described as reversible without a tested reverse script.

**Usually unlocks:** sequencing (one-way steps go last, behind evidence).

---

## 7. Sequencing

**Purpose:** decide the order of work so the riskiest unknowns are retired first
and one-way doors come after the evidence that justifies them.

**Questions that pay off**

- What is the thinnest version that proves the riskiest assumption?
- What must be true before the first irreversible step?
- What can run in parallel, and what genuinely blocks what?
- Is there a shadow or parallel-run phase, and what ends it?

**Answers that should make you dig**

- A sequence that does all the easy work first and the risky part last.
- Steps ordered by team availability rather than by dependency.

**Usually unlocks:** ownership.

---

## 8. Ownership

**Purpose:** name who decides, who builds, who runs it afterwards and who is
woken up. Plans without an owner for the "afterwards" become orphans.

**Questions that pay off**

- Who has final say when two stakeholders disagree?
- Who owns this in production six months from now?
- Who maintains the documentation and the runbook?

**Answers that should make you dig**

- A team name with no person. Ask for the person.
- "We'll figure it out after launch."

---

## 9. Unknowns

**Purpose:** list what nobody knows yet and decide, per item, whether to find
out now, defer with an owner, or accept the risk explicitly. Unknowns left
unlisted become assumptions nobody chose.

**Questions that pay off**

- What are we assuming that we have not checked?
- Which unknown, if it went the wrong way, would change the plan?
- What is the cheapest way to turn that unknown into a fact?
- Which unknowns can safely wait until after the first release?

**Answers that should make you dig**

- An empty list. Every non-trivial plan has unknowns; ask about the parts the
  team has not built before.

---

## Facts versus decisions

Every question is one of two kinds, and the kind decides who answers it.

| Kind | Example | Who answers | How |
|------|---------|-------------|-----|
| **Fact** | "How many accounts have 2–9 seats?" | The agent | Read the code, the data, the docs, the logs. Log the source. |
| **Decision** | "Do we price per seat or flat?" | The decision-maker | Put it to them with a recommended answer. |

Rules of thumb:

- If the answer exists somewhere the agent can reach, it is a fact. Asking the
  user for it wastes their attention and invites a guess.
- If two reasonable people could give different answers and both be right, it
  is a decision.
- A fact the agent cannot find becomes an **unknown**, not a question for the
  user — unless the user is the only place it exists (their preference, their
  plan, their calendar).
- Never record a decision as an "assumption" without the decision-maker
  confirming it. That is the agent deciding on the user's behalf.

---

## Writing a good question

| Property | Good | Bad |
|----------|------|-----|
| One idea | "Do we page on-call after two failures?" | "How should we handle failures and alerts and retries?" |
| Carries a recommendation | "...? Recommended: yes, page before 05:30." | "...?" |
| "Yes" accepts the recommendation | "Keep the CSV schema frozen?" | "Should we change the CSV schema or not?" |
| Answerable now | Prerequisites settled | Depends on an answer not given yet |
| Concrete | "Grace period of 7 days, then read-only?" | "What about edge cases?" |

The recommendation is not a leading trick. It shows the decision-maker the
agent's reasoning, lets them accept with one word when they agree, and turns a
disagreement into a precise correction rather than an essay.

---

## Category-to-category dependency map

The usual order in which categories unlock each other. Use it to draft the
first two rounds; after that, the actual answers decide the order.

```
goal ──► users ──► constraints ──► reversibility ──► sequencing ──► ownership
  │         │            │                ▲
  └► success └► failure_modes ────────────┘
unknowns: raised in every round, resolved or deferred before closing
```

Round 1 usually contains goal, the first users question, and any hard
constraint already visible. Ownership questions with no prerequisites can join
round 1 too.

## references/running-the-grilling.md

# Running the Grilling: Rounds, Logging, Stopping, Multi-Session Mode

This reference covers the mechanics: how to build the decision tree, how to cut
it into rounds, what to write down, when to stop, and how to stretch the same
discipline across several sessions to turn a fuzzy recurring workflow into a
spec someone else can build.

---

## 1. The decision tree

Every plan hides a tree. The root is the goal. Each answer opens the questions
that hang off it: once the goal is "stop missed exports", the next questions
are about who reads the export and what format must not change; once the
format is frozen, the rollback question becomes answerable; and so on.

Two properties matter:

- **Dependencies.** A question depends on another when a different answer to
  the first would change, or remove, the second. Record that as `depends_on`.
- **Settledness.** A question is settled when it is answered, or when it is
  stated as an assumption the decision-maker accepted (or, for a fact, that the
  agent verified and sourced). Asked-but-unanswered and deferred questions are
  not settled.

The **frontier** is the set of open questions whose prerequisites are all
settled. Those are the only questions worth asking right now. Anything else
asks the user to answer a hypothetical: "assuming you pick per-seat pricing,
what happens at seat 11?" invites an answer that may be thrown away next round.

## 2. Rounds

A round is one batch of frontier questions, sent together, answered together.

1. Recompute the frontier from the log (`question_log_checker.py --stage round`
   prints it as "Next round", ordered so the questions that unblock the most
   others come first).
2. Resolve every **fact** on the frontier yourself first. Read the repository,
   the data, the documentation. Log each with its source. Facts that turn out to
   be unfindable become unknowns.
3. Draft each **decision** with a recommended answer and a one-line reason.
   Word it so "yes" accepts the recommendation.
4. Cap a round at about five decisions. More than that and answers get shorter
   and less considered. If the frontier is larger, send the five that unblock the
   most.
5. Send the round. Number the questions so the user can reply "1 yes, 2 no —
   because…, 3 yes".
6. Log every answer verbatim. Then recompute the frontier: answers open new
   questions and sometimes make queued ones irrelevant (mark those `deferred`
   with reason "superseded by Q7", or delete them before they are asked).

### Round format

```
Round 3 — 4 questions (unblocks 6 more)

Q7. Shadow-run old and new exporters for 7 nights before cutover?
    Recommended: yes — cut over after 7 identical diffs.
    Why: the format is frozen (Q3), so a byte diff is a complete test.

Q8. Does the payments platform team own the exporter after cutover?
    Recommended: yes — it sits next to their invoicing service.
```

### Pace

- Do not wait on a slow fact lookup to send the rest of the round. A pending
  lookup only blocks the questions that depend on it.
- If the user answers a question that was not asked ("and by the way we also
  need SSO"), log it as a new question with its category and settle it — do not
  let it slip into the conversation unlogged.
- If an answer contradicts an earlier one, stop and surface the conflict
  before continuing: "Q9 says read-only after 7 days; Q4 said no access loss
  ever. Which holds?"

## 3. What the log must hold

| Field | Why |
|-------|-----|
| `id`, `question` | Reference in rounds and in the decisions list |
| `category` | Coverage check across the taxonomy |
| `kind` | Fact (agent answers) or decision (user answers) |
| `depends_on` | Frontier computation and order checking |
| `round` | Proves no question was asked before its prerequisites |
| `recommended` | Every decision put to the user carries the agent's pick |
| `answer` | Verbatim; paraphrase drifts |
| `status` | open, asked, answered, deferred, assumed |
| `resolved_by` | `agent` for facts looked up; `user` for anything the user said |
| `source` | Where an agent-resolved fact came from |
| `confirmed` | True when the user accepted an assumption |
| `owner`, `reason` | Required for every deferral |

Keep a human-readable copy (`assets/question_log_template.md`) for the
decision-maker and the JSON copy for the gate. They hold the same content.

## 4. When to stop

Stop when **all** of these hold:

1. The frontier is empty and nothing is blocked.
2. Every core category has at least one settled question.
3. No decision is recorded as an assumption without the user's confirmation.
4. Every deferral has an owner and a reason, and none of them sits on the route
   to the goal.
5. You can read the "Decisions so far" list back and the decision-maker agrees
   it is the plan.

Run `question_log_checker.py --stage final`. Exit 0 means the mechanical part of
the stop criteria holds; point 5 is a conversation, not a check.

### Stop early when

- The remaining questions are all two-way doors with cheap reversal. Record the
  recommended answers as confirmed assumptions in one batch ("Accept all
  remaining recommendations? yes/no") and stop.
- The user says they want to start. Close the log with the open questions listed
  as deferred, owner = the user, and say plainly which branches are unvisited.

### Do not stop when

- The goal is still two goals.
- A one-way door step (data migration, contract, public announcement) has no
  reversibility or failure-mode question settled.
- The user is answering with "whatever you think" to decisions that are not
  two-way doors. That is a sign they are tired, not that the tree is resolved;
  offer to pause and resume.

## 5. Facts: how to look them up

Before asking the user anything, search where facts live:

| Fact type | Where to look |
|-----------|---------------|
| Current behaviour of a system | The code, config, tests |
| Usage numbers | Analytics, logs, database counts |
| Existing commitments | Contracts, docs, tickets, roadmap |
| Constraints from other teams | Their docs, their interface definitions |
| Prior decisions | ADRs, decision logs, closed tickets |

Log every fact with its `source`. A fact without a source is an assumption, and
the checker warns about it.

## 6. Multi-session mode: fuzzy workflow → implementable spec

Use multi-session mode when the subject is a **recurring** workflow the user
wants to hand off — to a script, an agent, a teammate — and it is not yet
written down. One sitting rarely gets there: the user needs to watch the
workflow happen once or twice between sessions to answer accurately.

### The spec's sections

| Section | Settled when |
|---------|--------------|
| Trigger | The exact event or cadence (with time and timezone) is named, plus what looks like a trigger but is not |
| Inputs | Every input has a source and an example |
| Steps | Each step has one actor (agent, human, script) and a concrete action |
| Human checkpoints | Each states the decision asked and the brief shown; or the workflow is marked autonomous with a reason |
| Outputs | Each has a destination and a reader |
| Failure handling | What happens on a failed step and who hears about it |
| Done definition | Each criterion can be checked by someone who was not in the grilling |
| Vocabulary | The user's own terms are pinned down |

### Session structure

1. **Session 1 — the world.** Before specifying anything, learn the user's
   tools, channels and vocabulary. Record terms in the spec's Vocabulary
   section. Draft the trigger and outputs only.
2. **Between sessions** — the user runs the workflow by hand once and notes
   what they actually did. This is the most valuable input in the whole mode.
3. **Session 2 — the steps.** Walk the notes step by step. For each step: who
   does it, what they read, what they produce. Identify the judgment calls; those
   are checkpoint candidates.
4. **Session 3 — checkpoints and failure.** Push each checkpoint as late as it
   can go, so the human is asked once, with everything prepared, and reads a
   brief rather than raw output. Settle failure handling and the done
   definition.
5. **Gate.** Run `workflow_spec_checker.py`. Exit 0 means no open questions,
   every step has an actor, every checkpoint has a decision and a brief, every
   output has a destination, and the done definition is testable.

### Resuming a session

Open the question log and the spec. Recompute the frontier. Start the session
with a three-line recap — what was decided, what is open, what the user was
going to observe in between — then send the first round. Never re-ask a settled
question; if the user's view has changed, log a new question that supersedes the
old one and mark the old one deferred with reason "superseded".

### Checkpoint placement

| Placement | Effect |
|-----------|--------|
| Early (after step 1 of 6) | Human asked before anything is prepared; likely asked again later |
| Late (after the brief is written) | Human asked once, with the full picture; fast review |
| None, with reason | Autonomous; acceptable when every failure is cheap and reversible |
| None, no reason | A gap. The checker fails it. |

## 7. Worked example (compressed)

**Plan:** replace a nightly cron export with a queue-driven exporter.

- **Round 1** (frontier = no-dependency questions): goal (stop misses vs.
  real-time?), constraints (freeze the CSV format?), ownership (payments
  platform?). Users question resolved by the agent from bucket access logs.
- **Round 2:** success (30 days, zero misses?), failure modes (page on-call
  after two failures?), reversibility (keep cron deployable for 14 days?).
- **Round 3:** sequencing (shadow-run 7 nights, diff, then cut over?) — only
  answerable once reversibility and success were settled. One unknown (move to
  an API push?) deferred with an owner.
- **Gate:** `question_log_checker.py --input assets/sample_question_log.json`
  exits 0. The decisions list is read back; the plan is agreed.

The flawed sample (`assets/sample_question_log_flawed.json`) shows the common
failures: a goal answered "both", a fact put to the user and guessed, a decision
asked before its prerequisite, a decision silently assumed, a cycle, a
dangling dependency and a deferral without an owner. The checker exits 1 on it.

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/discovery/plan-grilling -->
