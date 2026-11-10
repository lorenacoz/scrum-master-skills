---
description: "Track cross-team dependencies in one JSON file and get a risk-ranked blocker list, the longest hand-off chain and a Mermaid graph. Use when several teams depend on each other and you need to know what to chase this week."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Cross-Team Dependency Map

## Overview

Dependency tracking for multi-team initiatives: who is blocking whom, what is on the critical path, what is at risk, and what to coordinate this week. The output is a Mermaid dependency diagram, a critical-path list, a risk-ordered blocker list, and a weekly cross-team sync agenda -- all generated from a single JSON file you maintain instead of a sprawling spreadsheet.

Most cross-team programs fail at dependency management, not execution. The teams individually do good work; the gaps are at the seams. This skill makes those seams visible, prioritizes them by criticality, and produces the communication artifacts that keep them visible week over week. The underlying model uses the Critical Path Method (CPM, Kelley and Walker, 1959) for sequencing, optional DSM (Design Structure Matrix) thinking for cluster identification, and Conway's Law (Conway, 1968) framing for the organizational source of recurring dependency patterns. All outputs follow the six standard PM formats per `SHARED_OUTPUT_SCHEMA.md`.

## Core Capabilities

- **Dependency capture** — a six-field model (from/to team, description, needed-by, expected-delivery, status) maintained as one JSON file.
- **Critical path** — the longest chain of open hand-offs (A's `to_team` is B's `from_team`, dates within 30 days), with slack shown per link. It is the chain to watch, not a strict zero-slack CPM path; links with positive slack can sit on it.
- **Risk ordering** — slack and status combine into a risk-ranked blocker list.
- **Visualization & comms** — Mermaid `graph LR` rendering plus a weekly cross-team sync agenda.
- **Org diagnosis** — Conway's Law framing for recurring team-pair dependencies.

## When to Use

- **Multi-team feature** -- A feature requires platform, mobile, and data teams to coordinate.
- **Program management** -- Tracking 5-20 dependent workstreams across a quarter (see `program-manager/`).
- **Release coordination** -- A launch depends on legal review + DevOps capacity + design assets all converging.
- **Quarterly planning** -- Identifying which dependencies threaten quarterly OKR commitments.
- **Org-design diagnosis** -- Recurring dependencies between the same two teams may signal a structural problem (Conway's Law).

**When NOT to use:** single-team backlogs (use `wwas/` or `job-stories/`), pure technical dependencies inside one codebase (use Git), or stakeholder relationships (use `senior-pm/stakeholder_mapper.py`).

## Clarify First

Before mapping dependencies, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Teams / workstreams in scope:** the from/to pairs become the nodes; the wrong set produces a graph that maps the wrong program.
- **Needed-by and expected-delivery dates per dependency:** these drive slack, so they determine the critical path and the entire risk ordering.
- **Current status of each dependency:** not-started / in-progress / at-risk / done drives the risk-ordered blocker list and the weekly sync agenda.
- **Named owner per dependency:** an ownerless dependency cannot be walked weekly; owners populate the sync agenda.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Copy `assets/dependency-template.json` and fill one entry per cross-team dependency (`from_team` needs, `to_team` owes). Set `"as_of"` to the date of the snapshot.
2. Run the analyzer:

```bash
python3 scripts/dependency_graph.py \
  --input assets/dependency-template.json --format markdown
# --format mermaid for the graph; --criticality critical,high or --team Mobile to filter
```

3. Give every critical-path and at-risk item a named owner and a next action; walk them weekly with `assets/weekly-sync-agenda.md`. Update the JSON before each sync.
4. **Done when** no blocked or high-risk item lacks an owner and a date for its next conversation.

**As-of date:** `--as-of`, else the file's `as_of` field, else today. The template and `--demo` carry `as_of: 2026-05-25`, so they show the same risk mix on any day (1 blocked, 1 high, 3 medium, 2 low). Risk is driven by slack (needed-by minus expected delivery), status, and days left to the needed-by date.

**Exit codes:** 0 report written; 2 missing file, invalid JSON, empty or wrong-shape `dependencies`, bad dates or an invalid `--criticality` value.

## Anti-Patterns

### Dependencies that never reach the JSON
**Mistake:** The JSON lists 8 dependencies while 22 exist. The rest live in Slack DMs and people's heads, and one team blocks another for three weeks before anyone notices.
**Why it happens:** Only the dependencies someone remembers to report get added.
**Instead:** Run a 90-minute inventory with each team lead at the start of the planning period, and log any dependency found outside the JSON within 24 hours. If a fresh round finds more than 30% new ones, the map is incomplete.

### Tracking tasks instead of cross-team work
**Mistake:** The JSON holds 80 task-level items such as "Frontend needs button asset from Design", and the Mermaid diagram becomes unreadable.
**Why it happens:** Teams log every handoff to be thorough.
**Instead:** Track at the epic level, roughly 1-2 weeks of cross-team work each, and keep intra-team handoffs on the team's sprint board. More than about 25 dependencies per program means you should aggregate.

### Arrows pointing the wrong way
**Mistake:** A dependency is entered with `from_team` as the team delivering the work and `to_team` as the team waiting for it.
**Why it happens:** "From" reads naturally as where the work comes from.
**Instead:** `from_team` is the team that needs the work, and `to_team` is the team that owes it. Spot-check a few descriptions before running `dependency_graph.py`, because a reversed arrow breaks the critical path and the risk ordering.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `scripts/dependency_graph.py` | The analyzer |
| `assets/dependency-template.json` | Starter file and sample: 8 dependencies, one per status |
| `assets/weekly-sync-agenda.md` | Agenda for the weekly cross-team sync |
| `examples/q4-launch-cross-team-deps.md` | Worked program example |

## References

- **[references/dependency-map-operations.md](references/dependency-map-operations.md)** — read this for the operational detail: the six-field model, slack/risk derivation, critical-path computation, the 8-step weekly workflow, tool flags, input/output JSON schemas, troubleshooting, and success criteria.
- **[references/dependency-management-guide.md](references/dependency-management-guide.md)** — read this for the CPM walkthrough, DSM intro, Conway's Law applied, and recurring-dependency diagnosis.
- **[references/red-flags.md](references/red-flags.md)** — read this to see the common ways dependency-map output goes wrong (with fixes) before publishing a map.
- Kelley & Walker, "Critical-Path Planning and Scheduling" (1959); Conway, "How Do Committees Invent?" (1968); Steward, "The Design Structure System" (1981).

## Scope & Limitations

**In Scope:** cross-team dependency capture and visualization, Critical Path Method analysis, risk-ordered blocker list, Mermaid `graph LR` rendering, Conway's Law-aware quarterly review, all six formats per `SHARED_OUTPUT_SCHEMA.md`.

**Out of Scope:** resource capacity planning (`senior-pm/resource_capacity_planner.py`), stakeholder mapping (`senior-pm/stakeholder_mapper.py`), sprint-level backlog ordering (`prioritization-frameworks/`), detailed Gantt charting, risk register beyond dependency blockers (`discovery/pre-mortem/`).

**Important Caveats:** dependency maps degrade fast without weekly updates (a 4-week-old map is harmful); the critical path identifies the *currently longest* chain and can shift when a single dependency is added (re-run on every change); this skill surfaces what to talk about but does not replace the conversation.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `program-manager/` | Used by | Program managers maintain the dependency JSON across teams |
| `senior-pm/` | Feeds into | Critical-path risks flow into portfolio risk reporting |
| `senior-pm/risk_matrix_analyzer.py` | Complementary | Dependency risks plot alongside other program risks |
| `discovery/pre-mortem/` | Complementary | Pre-mortem-identified "tigers" often map to specific dependencies |
| `cycle-time-analyzer/` | Complementary | Long cycle times often correlate with cross-team blocks |
| `launch-playbook/` | Feeds into | Launch RACI references the dependency map for cross-team owners |
| `status-update-generator/` | Feeds into | Weekly status pulls critical-path summary |
| `summarize-meeting/` | Feeds into | Weekly sync notes become structured summaries |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/dependency-management-guide.md

# Cross-Team Dependency Management Reference Guide

A practical reference for tracking, analyzing, and acting on cross-team dependencies. Covers Critical Path Method (CPM), Design Structure Matrix (DSM) basics, Conway's Law-driven org diagnosis, and the recurring failure patterns this skill exists to prevent.

---

## 1. The Dependency Problem

Multi-team programs rarely fail because any single team is incompetent. They fail at the seams. Three patterns dominate post-mortems of failed cross-team programs:

1. **Silent dependencies.** Team A assumed Team B was building X; Team B never knew. Discovered at integration.
2. **Optimistic dates.** Both teams have plausible plans; both plans assume the other team's worst-case estimate is the best-case. Discovered at the deadline.
3. **Recurring dependencies that nobody owns.** Same two teams generate dependencies every quarter; nobody steps back to fix the structural cause.

A live dependency map prevents (1), exposes (2), and creates the data to drive (3).

---

## 2. The Six-Field Dependency Schema

A dependency that is missing any of these fields is not actionable. Add them before discussing the dependency, not after.

| Field | Why it matters |
|-------|----------------|
| `from_team` (consumer) | Names the party with the risk |
| `to_team` (producer) | Names the party with the obligation |
| `description` | One sentence; if you cannot say it in one sentence, it is two dependencies |
| `needed_by` | The consumer's drop-dead date |
| `expected_delivery` | The producer's commitment date |
| `status` | The current state (`not_started`, `in_progress`, `at_risk`, `blocked`, `done`) |

Optional but recommended: `owner` (named individual on the producer side), `criticality`, `notes`.

### Why `needed_by` and `expected_delivery` Are Both Required

A single "date" field collapses two pieces of information: what the consumer needs and what the producer is committing to. The gap between them is the **slack**, which is what tells you whether to worry.

- `expected_delivery <= needed_by`: positive slack, ok.
- `expected_delivery > needed_by`: negative slack, the dependency is structurally late.
- `expected_delivery > needed_by + 14 days`: critical, escalate.

---

## 3. Critical Path Method (CPM)

Kelley and Walker, 1959. Originally for chemical-plant construction, but the math is identical for any DAG of dated dependencies.

### Definition

Given a directed acyclic graph of activities (here: dependencies), each with a duration, the **critical path** is the longest chain. The total length of the critical path equals the minimum total time the program can take, regardless of how much you parallelize elsewhere.

### Why It Matters

Any delay on the critical path delays the entire program. Any delay off the critical path either:

- Eats slack but does not delay the program (until slack reaches zero), or
- Moves the critical path to a previously near-critical chain.

This means: spend coordination effort on the critical path first; spend remaining effort on near-critical chains (slack < 1 week); deprioritize the rest.

### Computing the Critical Path

For this skill's purposes, the simplified algorithm is:

1. Build a directed graph where nodes are dependencies and edges connect dependencies that share a team and form a chain (output of one team feeds another).
2. Compute earliest start and earliest finish for each node using `needed_by` and `expected_delivery`.
3. Compute latest start and latest finish via backward pass.
4. Slack = latest start - earliest start. Nodes with zero slack are on the critical path.

The tool reports the critical path plus the next-shortest-slack chain (the "near-critical").

### Limitations

- CPM assumes fixed durations. Real dependencies have probabilistic durations. PERT (Program Evaluation and Review Technique) adds uncertainty by using three-point estimates; it is overkill for most cross-team programs.
- CPM treats teams as fungible. In practice, two dependencies competing for the same person's attention behave like one (resource constraints). Watch for this.

---

## 4. Design Structure Matrix (DSM)

Steward, 1981. A square matrix where rows and columns are teams (or activities); cells mark dependencies. Useful for spotting clusters of mutual dependency that should be reorganized.

### Reading a DSM

```
              Mobile  Platform  Data  Design
Mobile          -      X        X     X
Platform        X      -        X
Data                   X        -
Design          X                     -
```

- Cell `(Mobile, Platform) = X` means Mobile depends on Platform.
- A symmetric pair (both directions filled) indicates mutual coupling -- a Conway's-Law signal.
- A cluster of dependencies along a band suggests those teams form a natural service group.

This skill does not generate DSMs directly, but the `by_team_pair` output in the JSON gives you the data you need to build one.

---

## 5. Conway's Law Applied

Conway, 1968: organizations ship copies of their communication structures. The corollary for dependency management: a recurring dependency between two teams is a feature of your org chart, not of any particular quarter's plan.

### Diagnostic

Quarterly, count dependencies by `(from_team, to_team)` pair. If a single pair accounts for >25% of all dependencies, you have a structural problem.

### Three Responses (in order of preference)

#### 1. Merge the Teams

If both teams spend more than 30% of their capacity on dependencies with each other, the boundary between them is destroying more value than it creates. Merge.

#### 2. Create a Permanent Interface

If merger is not feasible (different skills, different reporting lines, different SLAs):

- Define an explicit API or service-level agreement.
- Schedule a recurring sync (weekly to biweekly) that drains the inbox.
- Publish ownership and on-call for the interface itself.

#### 3. Add a Permanent Program Manager

For complex multi-team seams (5+ teams interacting), a dedicated program manager (see `program-manager/`) owns the dependency map and the weekly sync.

### Anti-Pattern

Renaming the dependency without fixing the structure. "We'll add a coordination meeting" without changing the org chart or interfaces will produce the same dependencies next quarter.

---

## 6. The Weekly Cross-Team Sync

The single highest-leverage coordination meeting in a multi-team program. Run it well.

### Cadence

Weekly, 30-45 minutes, same time and day. Skipping a week destroys the rhythm.

### Attendees

- Program manager or PM (facilitator)
- One named representative per team with current dependencies
- Optional: exec sponsor (monthly only, not weekly)

### Standard Agenda (45 min)

1. **Critical path walk** (15 min). Each item on the critical path: status, blockers, ask.
2. **At-risk items** (10 min). Items not on critical path but with negative or low slack.
3. **New dependencies** (5 min). Any new dependencies added since last week.
4. **Closed and unblocked** (2 min). Celebrate; mark `done` in the JSON.
5. **Conway's signals** (3 min). Anything that looks recurring; raise quarterly review topic.
6. **Action items and owners** (10 min). One owner per action; due before next sync.

### Anti-Pattern

A sync that walks every dependency in alphabetical order is a sync that nobody attends after week 3. Always lead with the critical path.

---

## 7. Recurring Failure Patterns

| Pattern | Symptom | Fix |
|---------|---------|-----|
| **Silent dependency discovered at integration** | Surprise blocker 2 weeks before launch | Mandatory monthly dependency-inventory session with team leads |
| **Optimistic delivery dates** | Slack always green, dependencies always late | Require producer team to date `expected_delivery` against current capacity, not aspirational |
| **Stale map** | Map says 12 deps; reality has 18 | Update before, not after, weekly sync; assign the update to the PM, not "everyone" |
| **Map sprawl** | 50+ dependencies, mostly noise | Aggregate at epic level; only model cross-team blocks, not within-team sequencing |
| **Conway's loop** | Same team pair causing 40% of dependencies, every quarter, no action | Quarterly Conway's review with the option to merge, interface, or PM-up the seam |
| **No owner on critical-path item** | Critical-path dep with `owner: TBD` for 3 weeks | Weekly sync requires owner on every critical-path dep; escalate to producer team lead if missing |
| **Status inflation** | Every dep is `at_risk`; signal lost | Define `at_risk` precisely (negative slack OR blocked OR within 7 days of `needed_by` with no progress); train teams |

---

## 8. Communicating Dependency Status Up

Executives do not want to read 30 dependencies. They want three numbers and one decision.

### Executive Summary Template

> **Program:** [name]
> **As of:** [date]
> **Critical path length:** [N items]
> **At-risk count:** [N]
> **Blocked count:** [N]
> **Asks of leadership:** [0-3 specific items]
> **Most-recurring team pair:** [Team A <-> Team B, N deps this quarter]

Generated by `dependency_graph.py` and pasted into the weekly status (see `status-update-generator/`).

---

## 9. JSON Maintenance Tips

- Store the JSON in a Git repo. The diff is the change log.
- One file per program. Do not mix programs in one file.
- Update the JSON via the same channel as everything else (PR, Notion edit, Confluence edit) -- not on a private spreadsheet.
- Archive done dependencies quarterly to keep the active list short. The tool can re-generate any historical view from the archive.

---

## 10. References

- Kelley, James E., and Morgan R. Walker. "Critical-Path Planning and Scheduling." Eastern Joint IRE-AIEE-ACM Computer Conference, 1959.
- Conway, Melvin E. "How Do Committees Invent?" Datamation, April 1968, 28-31.
- Steward, Donald V. "The Design Structure System: A Method for Managing the Design of Complex Systems." IEEE Transactions on Engineering Management, EM-28(3), 1981.
- Eppinger, Steven D., and Browning, Tyson R. *Design Structure Matrix Methods and Applications*. MIT Press, 2012.
- Skelton, Matthew, and Pais, Manuel. *Team Topologies*. IT Revolution Press, 2019. (Conway's Law for modern teams.)

## references/dependency-map-operations.md

# Dependency Map Operations

> Read this when you need the operational detail: the dependency data model, slack/risk derivation, critical-path computation, the step-by-step weekly workflow, the tool flags, input/output JSON schemas, troubleshooting, and success criteria.

## The Dependency Model

A **dependency** has six attributes:

| Field | Required | Notes |
|-------|:--------:|-------|
| `id` | Yes | Stable identifier (e.g., `DEP-014`) |
| `from_team` | Yes | The team that NEEDS the work (the consumer/blocked party) |
| `to_team` | Yes | The team that OWES the work (the producer/blocker) |
| `description` | Yes | One sentence: what is needed |
| `needed_by` | Yes | ISO date when the consumer needs it |
| `expected_delivery` | Yes | ISO date when the producer expects to deliver |
| `status` | Yes | `not_started` / `in_progress` / `at_risk` / `blocked` / `done` |
| `criticality` | Optional | `critical` / `high` / `medium` / `low` (default `medium`) |
| `notes` | Optional | Free text context, links, decisions |

### Slack and Risk

For each dependency:

- **Slack** = `expected_delivery - needed_by`. Negative slack = the dependency is late or will be.
- **Risk** is derived from `status` and `slack`:
    - `done`: no risk
    - `blocked`: highest risk (work has stopped)
    - `at_risk` or `slack < 0`: high risk
    - `in_progress` with positive slack: medium
    - `not_started` more than 14 days before `needed_by`: low
    - `not_started` within 14 days of `needed_by`: high

### Critical Path

The **critical path** is the longest dependency chain through the program -- the sequence whose total duration determines the earliest possible completion. Any delay on the critical path delays the entire program. Any delay off it does not (until it consumes the slack and becomes critical).

This tool computes the critical path by building a directed graph from dependencies, ordering by `needed_by` dates, and identifying the chain of nodes with zero slack. The output lists the critical chain plus its near-critical sibling chains (slack < 7 days).

## Conway's Law and Recurring Dependencies

Melvin Conway, 1968: "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations."

Practical consequence for dependency mapping: if you find the same two teams generating dependencies every quarter, the org structure is the dependency. Three responses, in order of preference:

1. **Merge the teams** if the volume of dependencies justifies it.
2. **Create a permanent interface** (API contract, service-level agreement, scheduled sync) that reduces ad-hoc coordination.
3. **Add a permanent program manager** for the seam (see `program-manager/`).

## Workflow

1. **Inventory dependencies.** With each team's lead, list every cross-team need for the planning period. One sentence per dependency. Date both `needed_by` and `expected_delivery`.
2. **Populate the JSON.** Use the schema in `assets/dependency-template.json`.
3. **Run the analyzer.** `python scripts/dependency_graph.py --input deps.json --format markdown` for the full report.
4. **Generate the Mermaid graph.** `--format mermaid` -- paste into README, Notion, Confluence.
5. **Identify the critical path.** Review the critical path list. Every item on it gets a named owner and weekly status.
6. **Run the weekly sync.** Use `assets/weekly-sync-agenda.md`. Walk the critical path, then the at-risk items, then anything newly added.
7. **Update the JSON after every sync.** The map is only useful if it reflects current state. Stale maps are worse than no map.
8. **Quarterly review.** Look at recurring dependencies between the same two teams. If volume is high, consider Conway's Law responses.

## Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `dependency_graph.py` | Compute critical path, render dependency graph, list risks | `python scripts/dependency_graph.py --input deps.json --format mermaid` |

Demo mode: `python scripts/dependency_graph.py --demo --format markdown` produces sample output without input.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Critical path is empty | All dependencies have generous slack (positive `expected_delivery - needed_by`) | Verify dates are realistic; ask teams whether their `expected_delivery` reflects current capacity |
| Same two teams appear in 60% of dependencies | Org structure is the dependency (Conway's Law) | Quarterly review; consider merging teams, adding a permanent interface, or adding a program manager |
| Map goes stale within 2 weeks | No clear update cadence; map lives in nobody's daily routine | Make the JSON the single source of truth; require update before the weekly sync |
| Dependencies modeled at task level become unmaintainable | Granularity too fine; dozens of items per team per sprint | Aggregate at the epic level; only model cross-team blocks, not within-team sequencing |
| Status field always reads `at_risk` for every dep | Teams use it as a generic "this is hard" signal | Define explicit thresholds for `at_risk`; require dates to back the label |
| Mermaid diagram unreadable with 30+ nodes | Too many dependencies on one diagram | Filter by criticality (`--criticality critical,high`) or by team |
| Critical-path item has no named owner | Owner field optional and skipped | Make the weekly sync require an owner for every critical-path dependency |

## Success Criteria

- Every cross-team dependency is captured in the JSON with all required fields.
- A weekly cross-team sync walks the critical path and at-risk dependencies.
- Mermaid dependency diagram is published in a shared location and updated weekly.
- Every critical-path dependency has a named owner and a weekly status.
- Recurring dependencies are reviewed quarterly for Conway's Law responses.
- The dependency JSON is the single source of truth; spreadsheets and side documents are retired.
- Map is updated before, not after, the weekly sync.

## Tool Reference

### dependency_graph.py

Computes critical path, lists risks, and renders the dependency graph from a JSON file of cross-team dependencies.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input` | path | (required unless `--demo`) | JSON file with dependencies |
| `--demo` | flag | off | Use built-in demo data |
| `--format` | string | `markdown` | One of `json`, `markdown`, `mermaid`, `confluence`, `notion`, `linear` |
| `--output` | path | stdout | Output file path |
| `--criticality` | string | (all) | Comma-separated filter: `critical,high,medium,low` |
| `--team` | string (repeatable) | (none) | Filter to dependencies involving these team names |
| `--as-of` | ISO date | file `as_of`, else today | Reference date for risk calculations |

### Input JSON schema

```json
{
  "program": "Q3 Mobile Launch",
  "dependencies": [
    {
      "id": "DEP-001",
      "from_team": "Mobile",
      "to_team": "Platform",
      "description": "OAuth refresh token rotation API",
      "needed_by": "2026-06-15",
      "expected_delivery": "2026-06-10",
      "status": "in_progress",
      "criticality": "critical",
      "owner": "Alex Lee",
      "notes": "Blocking iOS auth refactor"
    }
  ]
}
```

### Output JSON schema (envelope per `SHARED_OUTPUT_SCHEMA.md`)

```json
{
  "schema": "pm/dependency-map/v1",
  "generated_at": "2026-05-21T00:00:00Z",
  "data": {
    "program": "Q3 Mobile Launch",
    "as_of": "2026-05-21",
    "summary": {
      "total_dependencies": 12,
      "done": 3, "blocked": 1, "at_risk": 2,
      "critical_path_length": 5
    },
    "critical_path": [ { "id": "DEP-001", "from_team": "...", "to_team": "...", "slack_days": 0 } ],
    "at_risk": [ ... ],
    "by_team_pair": [ { "from_team": "...", "to_team": "...", "count": 4 } ],
    "all_dependencies": [ ... ]
  }
}
```

## references/red-flags.md

# Red Flags: Dependency Map

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the dependency JSON and `dependency_graph.py` output before the weekly cross-team sync. Each red flag shows the *bad* version next to the *good* version, anchored to the Critical Path Method (Kelley & Walker) and Conway's Law.

---

## Red Flag 1: Invisible dependencies

**Symptom.** A team blocks another team for 3 weeks. Only discovered at the all-hands when the blocked team's lead complains.

**Why it's bad.** Dependencies that exist but are not captured in the JSON do not get critical-path analysis, do not appear in the weekly sync, and do not get explicit ownership. They surface as surprises — usually at the worst possible time.

**Bad example:**
> "JSON has 8 dependencies. (Reality: 22 cross-team dependencies actually exist this quarter. The other 14 live in Slack DMs, sprint goals, and individual engineers' heads.)"

**Good example:**
> "Quarterly inventory session (90 min): each team lead lists every cross-team need for the planning period. Combined into a single JSON with one sentence per dependency. Updated weekly. Any dependency that surfaces outside the JSON is logged within 24 hours; root cause discussed in the next sync."

**How to catch it.** Compare the JSON's count to a fresh 90-min team-by-team interview. If you find > 30% new dependencies, the map is missing the majority.

---

## Red Flag 2: No due dates on the arrows

**Symptom.** Dependencies are listed but `needed_by` and `expected_delivery` are blank or "TBD".

**Why it's bad.** Without dates, the critical-path algorithm cannot compute slack. Risk classification fails. The team sees a graph of arrows with no urgency signal. The map looks comprehensive but is decorative.

**Bad example:**
> "DEP-014: Mobile needs OAuth refresh-token API from Platform. needed_by: TBD. expected_delivery: TBD. status: not_started. (Critical path computation: empty.)"

**Good example:**
> "DEP-014: Mobile needs OAuth refresh-token API from Platform. needed_by: 2026-06-15 (the date Mobile's iOS auth refactor hits the integration milestone). expected_delivery: 2026-06-10 (Platform's lead committed in last week's sync). status: in_progress. slack: +5 days. criticality: critical. owner: Alex Lee."

**How to catch it.** Filter the JSON for items missing `needed_by` or `expected_delivery`. Each one is invisible to critical-path analysis.

---

## Red Flag 3: Stale map (4-week-old reality)

**Symptom.** Map was updated 4 weeks ago. Three dependencies have shifted dates; two were completed; one new one emerged. None reflected.

**Why it's bad.** A 2-week-old map is misleading; a 4-week-old map is harmful. Teams plan against false signal; the weekly sync walks a graph that no longer exists; trust in the artifact erodes.

**Bad example:**
> "Mermaid diagram from Apr 8 still posted in Confluence. Current date May 22. Three dependencies have completed; one new critical dependency added in Slack but not the map."

**Good example:**
> "Map update SLA: every Friday before 4pm. Owner: the program manager. Update process: each team lead confirms their dependencies via 5-min async ping; PM applies updates; Mermaid regenerated; new critical path computed. If the map is > 7 days old, the weekly sync is cancelled until the map is refreshed (forcing the discipline)."

**How to catch it.** Look at the map's last-updated timestamp. > 7 days = stale.

---

## Red Flag 4: Recurring dependencies between same two teams ignored

**Symptom.** Mobile depends on Platform in 8 out of 14 quarterly dependencies. This has been true for 4 quarters. Nobody has raised it as a structural issue.

**Why it's bad.** Conway's Law: when the same two teams generate dependencies every quarter, the org structure *is* the dependency. Three responses exist (merge, permanent interface, dedicated program manager). Ignoring the pattern means re-litigating the same coordination problem every 90 days.

**Bad example:**
> "Q1: 6 Mobile-needs-Platform deps. Q2: 7. Q3: 8. Q4 planning: 9 already on the list. 'Same as last quarter.'"

**Good example:**
> "Quarterly Conway's Law review: Mobile↔Platform dependency volume tracked. Q4 review surfaces the pattern: '8 dependencies/quarter sustained over a year. Recommendation: either (a) consolidate Mobile and Platform under one EM with shared planning, (b) build a stable internal API contract (Platform-as-Service) with quarterly versioning so Mobile no longer ad-hoc-requests, or (c) add a permanent Mobile-Platform integration PM. Decision: option (b). Q1 next year: API contract v1 ships, Mobile self-services from it, dep count drops to 3.'"

**How to catch it.** Pivot the `by_team_pair` output across the last 4 quarters. Any pair with sustained > 5 deps/quarter is a structural problem.

---

## Red Flag 5: Granularity too fine

**Symptom.** JSON has 80 dependencies. Most are at task level ("Frontend needs button asset from Design", "Backend needs DB column from DBA").

**Why it's bad.** Task-level dependency tracking is unmaintainable. The map becomes a worse version of Jira. Real cross-team blockers get lost in noise. The Mermaid diagram is unreadable.

**Bad example:**
> "80 deps. Includes 'Frontend needs button asset', 'Mobile needs icon update', 'Backend needs column added'. Mermaid unrenderable; PM gives up on the visual."

**Good example:**
> "12 deps at the epic level. Each represents 1-2 weeks of cross-team work. Intra-team dependencies (Frontend needing asset from in-team Designer) live in the team's sprint board, not the cross-team map. The map answers: 'who is blocking whom across team boundaries this quarter?'"

**How to catch it.** Count dependencies. > ~25 per program is granularity too fine. Aggregate to epic.

---

## Red Flag 6: Status field always reads "at_risk"

**Symptom.** 60% of dependencies are status `at_risk`. Team treats it as a generic "this is hard" flag.

**Why it's bad.** When everything is at-risk, nothing is at-risk. The signal is lost. The weekly sync devolves into reading the list aloud with no prioritization.

**Bad example:**
> "16 deps, 11 marked `at_risk`. Weekly sync agenda: 'walk all 11 at-risk items'. Meeting runs 90 min; no decisions made."

**Good example:**
> "Status definitions enforced: `at_risk` = dates are slipping OR scope is changing OR owner has flagged blocker. Default for normal in-flight work is `in_progress`. Of 16 deps: 2 at_risk (specific reasons named), 10 in_progress, 3 done, 1 blocked. Weekly sync focuses on the 2 + 1 = 3 items needing decisions."

**How to catch it.** Compute the % of deps at `at_risk` or `blocked`. > 30% sustained = status definitions are loose.

---

## Red Flag 7: Critical path has no named owner

**Symptom.** The critical path includes 5 dependencies. The `owner` field is blank for 3 of them.

**Why it's bad.** Critical-path items determine the earliest possible delivery date. An unowned critical item drifts. The team will discover the slip at the next milestone, with no person to escalate to.

**Bad example:**
> "Critical path (5 items): DEP-001 owner Alex; DEP-007 owner: blank; DEP-014 owner: blank; DEP-022 owner Sarah; DEP-031 owner: blank."

**Good example:**
> "Critical path (5 items), all owned: DEP-001 (Alex L), DEP-007 (Tomas R), DEP-014 (Marcus B), DEP-022 (Sarah K), DEP-031 (Priya N). Weekly sync requires each owner to give a 30-sec status; missing owner = the program manager fills in temporarily and the team lead picks one before next sync."

**How to catch it.** Filter critical_path for items where `owner` is empty or "TBD". Any = unowned critical work.

---

## Red Flag 8: Mermaid unreadable with too many nodes

**Symptom.** Mermaid diagram has 30+ nodes. Rendered, it is an illegible spaghetti tangle. Team stops looking at it.

**Why it's bad.** A diagram that no one reads provides no coordination value. The visual stops being a tool and becomes a chore.

**Bad example:**
> "Full Mermaid render: 34 nodes, ~50 edges, three colors. Confluence page loads slowly; nobody opens it."

**Good example:**
> "Filtered views: (1) `--criticality critical,high` shows the 7 critical/high deps in a readable graph; (2) `--team Mobile,Platform` shows just the Mobile-Platform seam; (3) full graph available on request but not the default. Each filtered view is publishable as a separate Confluence section."

**How to catch it.** Open the rendered diagram. If a team member cannot trace one dependency in 5 seconds, the view is too dense — filter.

---

## Red Flag 9: Dependency JSON not the single source of truth

**Symptom.** Same dependencies live in 3 places: the JSON, a Confluence spreadsheet, and a slide in the weekly exec deck. Each has slightly different states.

**Why it's bad.** Multiple sources of truth means no source of truth. The team spends time reconciling rather than coordinating. New joiners do not know which is current.

**Bad example:**
> "Confluence sheet says DEP-014 is 'in progress'. JSON says 'at_risk'. Exec deck shows 'on track'. Three readers, three answers."

**Good example:**
> "JSON is the single source of truth. The Confluence page and exec deck are *rendered from* the JSON via `dependency_graph.py --format confluence` and `--format markdown`. The spreadsheet is retired. Update process: edit the JSON; regenerate the views; never edit downstream."

**How to catch it.** Ask 3 team members where to find the current dependency status. If they name different sources, the system is fragmented.

---

## Red Flag 10: Conversation skipped because "the map is updated"

**Symptom.** Program manager updates the JSON Friday afternoon. Skips the weekly sync. Assumes the document does the coordination work.

**Why it's bad.** The map surfaces what to talk about; the talking still has to happen. A map updated but unspoken-to does not produce coordination. Trust between teams is built in conversation, not in artifact-reading.

**Bad example:**
> "PM: 'I updated the map; please review async. Cancelling the weekly sync this week — saves us 30 min.' (4 weeks later: two teams have drifted; one critical path item slipped 2 weeks.)"

**Good example:**
> "Weekly sync is non-negotiable, 25 minutes, agenda set by the map. Walk: (1) critical path items — each owner gives 30-sec status; (2) at-risk items — 1-min decision per; (3) newly added since last week; (4) Conway's Law observation if pattern emerging. PM updates JSON during/after the meeting based on conversation."

**How to catch it.** Last sync date and last map-update date. If updates happen but no sync, talking is being skipped.

---

## Red Flag 11: Dependencies modeled in the wrong direction

**Symptom.** DEP-014 says `from_team: Platform`, `to_team: Mobile`, `description: "deliver OAuth API"`. Direction is reversed.

**Why it's bad.** The model assumes `from_team` = the team that NEEDS the work; `to_team` = the team that OWES the work. Reversed direction breaks the critical-path computation and the risk classification.

**Bad example:**
> "DEP-014: from_team: Platform (the producer). to_team: Mobile (the consumer). (Critical path computation: incorrect.)"

**Good example:**
> "DEP-014: from_team: Mobile (the consumer/blocked party). to_team: Platform (the producer/blocker). description: 'OAuth refresh-token API'. needed_by: 2026-06-15. (Mobile needs it from Platform; Platform owes it.)"

**How to catch it.** Read a few dependency descriptions. Does the arrow point from consumer to producer? If reversed, the direction convention is broken.

---

## Red Flag 12: Critical path treated as fixed

**Symptom.** Critical path was computed at the start of the quarter. Six weeks in, no one has recomputed. New dependencies have been added, but the team is still focused on the old critical path.

**Why it's bad.** The critical path is dynamic. A single new dependency can shift it. Working hard on the formerly-critical path while ignoring a newer one is misallocated attention.

**Bad example:**
> "Q3 kickoff: critical path computed (5 items). Week 7: 3 new deps added but `dependency_graph.py` not re-run. Team continues to focus on the original 5; meanwhile DEP-040 (added week 4) is now critical and unowned."

**Good example:**
> "`dependency_graph.py` runs every Friday as part of the map refresh. Critical path is recomputed; new critical items are highlighted in the weekly sync agenda. Old critical items that lost criticality are noted but no longer the top focus."

**How to catch it.** Last time the critical path was recomputed? If > 14 days and the JSON has changed since, the focus is stale.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Invisible dependencies | Fresh team-by-team interview vs JSON count |
| 2 | No due dates on arrows | Any dep with blank needed_by/expected_delivery? |
| 3 | Stale map | Map's last-updated timestamp |
| 4 | Recurring same-team deps ignored | Pivot by_team_pair across last 4 quarters |
| 5 | Granularity too fine | Total dep count > 25? |
| 6 | Always "at_risk" | What % of deps have status at_risk or blocked? |
| 7 | Critical path unowned | Any critical-path dep with empty owner? |
| 8 | Mermaid unreadable | Can a team member trace one dep in 5 seconds? |
| 9 | Multiple sources of truth | Ask 3 people where to find current status |
| 10 | Map updated but no sync | Last sync date vs last map-update date |
| 11 | Direction reversed | Does arrow point consumer → producer? |
| 12 | Critical path treated as fixed | When was critical path last recomputed? |

## Related Reading

- SKILL.md Troubleshooting
- references/dependency-management-guide.md
- Kelley, James E., and Morgan R. Walker, "Critical-Path Planning and Scheduling" (1959)
- Conway, Melvin E., "How Do Committees Invent?" (1968)
- `program-manager/` (the role that maintains the map)
- `pre-mortem/` (tigers often map to specific dependencies)
- `cycle-time-analyzer/` (long cycle times often correlate with cross-team blocks)

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/dependency-map -->
