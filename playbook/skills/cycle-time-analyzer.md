# cycle-time-analyzer

> **Use these instructions for this whole conversation.** Apply them when: Compute lead time, cycle time, throughput, WIP, aging WIP and a cumulative flow diagram from issue status history. Use when diagnosing slow delivery, setting WIP limits or preparing a flow review.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Cycle Time Analyzer (Flow Metrics)

## Overview

Compute and visualize the four core Kanban flow metrics -- lead time, cycle time, throughput, and work-in-progress -- from issue history data exported from Jira, Linear, GitHub Projects, or any tracker that records status transitions. The output is a dashboard suitable for sprint retrospectives, executive reporting, and bottleneck analysis, plus a Mermaid cumulative flow diagram that visualizes work accumulation over time.

Flow metrics are the most useful diagnostic for team and process health, far more so than velocity or story points. Daniel Vacanti's work (*Actionable Agile Metrics for Predictability*, 2015) shows that predictability and throughput are governed by Little's Law (`Throughput = WIP / Cycle Time`), and that the most reliable way to improve delivery is to lower WIP and stabilize cycle time -- not to estimate harder. This skill also reports aging WIP (in-flight work older than the team's 85th-percentile cycle time -- the items most at risk) and supports the shared `--format` schema (json, markdown, mermaid, confluence, notion, linear).

## Core Capabilities

- **Four flow metrics** — lead time, cycle time (as a distribution, never an average), throughput, and WIP, tied together by Little's Law.
- **Aging WIP** — flags in-flight items older than the 85th-percentile cycle time as at-risk; the most actionable daily metric.
- **Cumulative flow diagram** — Mermaid CFD for retrospectives and exec reports.
- **Per-type filtering & trends** — bug/feature/spike breakdowns over rolling 6-8 week windows across all six output formats.

## When to Use

- **Sprint retrospective** -- A team wants data-driven discussion of why some sprints feel slow.
- **Bottleneck investigation** -- Throughput has fallen and the team needs to identify the constraining step.
- **Quarterly delivery review** -- Leadership wants a real picture of delivery performance beyond story-point velocity.
- **Predictability analysis** -- Stakeholders want delivery forecasts grounded in actual cycle time distributions (use with Monte Carlo via `scrum-master/`).
- **WIP-limit calibration** -- A Kanban team is setting WIP limits and needs a baseline of current behavior.

## When NOT to Use

- For story-point velocity tracking, use `scrum-master/velocity_analyzer.py`.
- For sprint capacity calculation, use `scrum-master/sprint_capacity_calculator.py`.
- For per-person performance evaluation -- flow metrics are team-level signals; using them to rank individuals destroys the team behavior they measure.

## Clarify First

Before running the analysis, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Issue history with status transitions:** per-item timestamps for when work started and finished (every metric is derived from these; missing transitions invalidate the numbers).
- **Workflow states that count as "in progress" vs "done":** your board's actual status names (defines where cycle time starts/stops, which changes every result).
- **Analysis window:** the rolling period (e.g. last 6-8 weeks) and any type filter (scopes throughput trend and which in-flight items are flagged as aging WIP).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Export** issue history with status transitions into the input shape (`assets/sample_issues.json`).
2. **Map your states** if your board's names differ from the defaults (`--ready-state`, `--in-progress-state`, `--done-state`, each repeatable).
3. **Run the analysis:**

```bash
python3 scripts/flow_metrics.py \
  --input assets/sample_issues.json --format markdown
# Live board: add --as-of YYYY-MM-DD (today) so aging WIP is measured to now
```

4. **Read the distribution, not the average:** quote p85 cycle time and p85 lead time, flag aging WIP above p85, read throughput as a 6-8 week trend.
5. **Verify** before sharing: completed-in-window is not zero, WIP matches the board, and the as-of date in the header is the date you meant. Re-run weekly.

**As-of date:** defaults to the latest timestamp in the data, so the sample (April-May 2026) reads the same on any day: 7 completed, 0.82 items/week, 1 aging item. For a live board pass `--as-of` with today's date; otherwise items still in progress look younger than they are.

## Tools

| Tool | Purpose | Key flags |
|------|---------|---------|
| `flow_metrics.py` | Lead time, cycle time, throughput, WIP, aging WIP, CFD | `--input F` or `--demo`, `--format json\|markdown\|mermaid\|confluence\|notion\|linear`, `--type`, `--window-days 60`, `--as-of`, `--ignore-missing`, `--output` |

**Exit codes:** 0 report written; 2 missing file, invalid JSON, empty or wrong-shape `issues`, bad `--as-of`, or malformed issue data. Full flags and schemas: `references/metrics-and-tool-reference.md`.

## Anti-Patterns

### Quoting cycle time when asked for lead time
**Mistake:** An exec asks how long a feature takes, the team says 6 days, and the customer waits 11 weeks because the item sat in the backlog first.
**Why it happens:** Cycle time is the team's own number and the one the board shows.
**Instead:** Report both, labelled. Use lead time (from when the request entered the backlog) for customer commitments and cycle time for engineering planning, each at p85.

### WIP limits set by feel
**Mistake:** The team adopts a WIP limit of 5 per engineer because "that feels manageable".
**Why it happens:** Teams pick a limit before anyone has measured current WIP.
**Instead:** Measure the team's current WIP distribution first. A starting heuristic [EXPERIMENTAL] is a limit just below its median: low enough to bind on a normal day (that is what forces finishing over starting), high enough not to idle people. A limit above the 85th percentile almost never binds, so it has no effect. Re-measure cycle time with `flow_metrics.py` after 4 weeks and adjust.

### Single-sprint throughput read as a trend
**Mistake:** "Throughput dropped to 4 items this sprint, down from 6. Investigating slowdown."
**Why it happens:** Status updates cover one sprint, so one sprint's number is what gets reported.
**Instead:** Report throughput as a rolling 6-8 week trend with its range, and annotate known causes such as PTO. Investigate only when a sprint falls outside that range.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `scripts/flow_metrics.py` | The analyzer |
| `assets/sample_issues.json` | 10-issue history (same as `--demo`) |
| `assets/flow-metrics-dashboard.md` | Dashboard template |
| `examples/wayfinder-flow-analysis.md` | Worked analysis |

## References

- `references/metrics-and-tool-reference.md` -- Precise definitions of the four metrics, Little's Law, aging WIP, the 7-step workflow, troubleshooting matrix, success criteria, and the full `flow_metrics.py` CLI flags + input/output JSON schemas. Read when running an analysis or wiring up the tool.
- `references/flow-metrics-guide.md` -- Vacanti-style deep dive: lead vs cycle, distributions vs averages, Little's Law, aging WIP, common anti-patterns. Read for narrative depth and tracker-specific export instructions.
- `references/red-flags.md` -- Bad-vs-good examples of flow-metric reporting. Read this to sanity-check a dashboard before sharing it.
- Vacanti, Daniel S. *Actionable Agile Metrics for Predictability*. ActionableAgile Press, 2015.
- Vacanti, Daniel S. *When Will It Be Done?* ActionableAgile Press, 2020.
- Little, John D. C. "A Proof for the Queuing Formula: L = λW." Operations Research, 1961.
- Anderson, David J. *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press, 2010.

## Scope & Limitations

**In Scope:**
- Lead time, cycle time, throughput, WIP, aging WIP calculation
- Cumulative flow diagram generation (Mermaid)
- Per-type filtering (bug, feature, spike)
- All six output formats per `SHARED_OUTPUT_SCHEMA.md`

**Out of Scope:**
- Monte Carlo delivery forecasting (use `scrum-master/velocity_analyzer.py`)
- Story-point velocity (use `scrum-master/`)
- Resource capacity planning (use `senior-pm/resource_capacity_planner.py`)
- Code-level metrics (PR review time, deploy frequency -- use DevOps-focused tools)

**Important Caveats:**
- Flow metrics depend on accurate status transitions. If your team batch-updates the board once a day, the cycle time data will be discretized by that batch interval.
- A team that gamifies flow metrics will produce better-looking numbers without changing real delivery. Use these metrics as a diagnostic, not a target. (Goodhart's Law.)
- Cycle time is a team property, not an individual property. Resist the urge to compute per-assignee cycle time -- it will incentivize hand-offs that hurt the team.
- AI-assisted teams: faster coding often shifts the wait into review and test states. Watch time-in-review and aging WIP there, not just total cycle time, and pair flow metrics with DORA rework rate. See the "AI-Assisted Delivery" sections in `delivery-manager/` and `scrum-master/`.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `scrum-master/` | Complementary | Flow metrics + velocity together provide the full delivery picture |
| `scrum-master/retrospective_analyzer.py` | Feeds into | Flow trends inform retro topics |
| `dependency-map/` | Complementary | Long cycle times often correlate with cross-team dependencies |
| `sprint-retrospective/` | Feeds into | CFD and aging WIP are standard retro inputs |
| `senior-pm/project_health_dashboard.py` | Feeds into | Throughput trends feed portfolio health |
| `status-update-generator/` | Feeds into | Weekly status includes throughput and aging WIP highlights |
| `agile-coach/` | Used by | Coaches use flow metrics to assess team maturity |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/flow-metrics-guide.md

# Flow Metrics Reference Guide

A practical reference for Kanban flow metrics: lead time, cycle time, throughput, WIP, and aging WIP. Built on Daniel Vacanti's body of work and David Anderson's Kanban methodology. Companion to `flow_metrics.py`.

---

## 1. Why Flow Metrics

Story-point velocity is a measure of a team's *commitment*, not its delivery. It is highly gameable, sensitive to estimation drift, and meaningless across teams. Flow metrics measure actual delivery behavior using only event timestamps already in your tracker. They are:

- **Atomic.** One completed item = one. No estimation bias.
- **Comparable.** Throughput and cycle time mean the same thing across teams.
- **Diagnostic.** When delivery slows, flow metrics tell you *where* (which step in the workflow is the bottleneck).
- **Forecasting-ready.** Cycle time distributions feed Monte Carlo forecasts directly.

The four metrics are governed by **Little's Law**:

```
Average Cycle Time = Average WIP / Average Throughput
```

Practical implication: reducing WIP is the most reliable way to reduce cycle time. Estimation accuracy is a distant second.

---

## 2. The Workflow Model

Every work item moves through a defined workflow:

```
Backlog -> Ready -> In Progress -> In Review -> Done
```

The exact state names vary by tracker and team. What matters is identifying three boundaries:

| Boundary | Meaning | Common State Names |
|----------|---------|---------------------|
| **Commitment point** | The team agrees to do this item | `Ready`, `To Do`, `Selected for Development` |
| **Start of active work** | Someone begins working on it | `In Progress`, `In Development` |
| **Delivery point** | The item ships / is accepted | `Done`, `Closed`, `Deployed`, `Accepted` |

The choice of boundaries determines the metrics:

- **Lead time** = `Delivery point` - `Commitment point`
- **Cycle time** = `Delivery point` - `Start of active work`

If your team has a long "Ready" queue (commitment to start), lead time will be much larger than cycle time. That gap is the queueing delay, often the biggest opportunity for improvement.

---

## 3. Lead Time

The customer-perceived elapsed time from commitment to delivery.

### How to Read It

Report as a **distribution**, not a single number:

| Percentile | Meaning |
|------------|---------|
| **50th (median)** | Half of items finish in this time or less |
| **85th** | The "service level expectation" -- a defensible commitment to stakeholders |
| **95th** | Worst-case for planning; outliers above this need investigation |

A stakeholder asking "when will it be done?" deserves the 85th-percentile answer, not the average. The average over-promises because the distribution is right-skewed (a few items take very long).

### Common Failures

- **Reporting average lead time only.** Hides the skew; promises overshoot reality.
- **Stale backlog inflating lead time.** Items "committed" months ago that nobody is actually working on. Either close them or measure lead time only for items committed in the last N months.
- **Mixing types.** Bugs, features, and spikes have very different lead times. Filter or split before reporting.

---

## 4. Cycle Time

The team-perceived elapsed time from start of active work to delivery.

### How to Read It

Same distribution rules as lead time. The 85th percentile is the practical "how long do things take us?" answer.

### What Increases Cycle Time

The four big drivers (in observed-impact order):

1. **High WIP.** Little's Law makes this mechanical.
2. **Cross-team dependencies.** Waiting on another team's review or deployment.
3. **Large items.** Stories that should have been split (see `story-splitting/`).
4. **Context switching.** Engineers juggling multiple items simultaneously.

### Cycle Time vs Estimation Accuracy

Teams that improve cycle time by reducing WIP and splitting work see predictability improvements much larger than teams that improve estimation accuracy. Vacanti's recommendation: stop estimating story points and instead split work into uniform-ish sizes (most teams converge on 1-3 days per item) and use throughput as the planning unit.

---

## 5. Throughput

Items completed per unit time. Most useful at the week or sprint level.

### How to Read It

| Window | Use |
|--------|-----|
| Per week | Operational dashboard |
| Per sprint | Sprint review baseline |
| Rolling 6-8 weeks | Trend reporting |
| Per quarter | Capacity planning |

### Throughput vs Velocity

| | Throughput | Story-Point Velocity |
|---|---|---|
| Counts | Completed items | Story points completed |
| Estimation needed | No | Yes |
| Comparable across teams | Yes (with type filter) | No |
| Useful for Monte Carlo | Yes | Yes (but noisier) |
| Gameable | Low (visible count) | High (point inflation) |

### Monte Carlo Forecasting

Given a throughput distribution from N past sprints, you can answer "how likely is it that we finish X items by sprint Y?" with a Monte Carlo simulation:

1. Sample N throughput values from history (with replacement).
2. Sum the samples across the forecast horizon.
3. Check the percentile of "X items completed."
4. Repeat 10,000+ times.

The result: "There is a 90% chance we deliver 30 items in the next 6 weeks; a 50% chance we deliver 40." This is far more useful than "our velocity is 35."

(For Monte Carlo specifically, hand off to `scrum-master/velocity_analyzer.py`. This skill produces the input distribution.)

---

## 6. Work-In-Progress (WIP)

The count of items currently in flight.

### Why WIP Matters

From Little's Law, WIP and cycle time are mechanically linked. Doubling WIP doubles cycle time (with throughput held constant). This is not a metaphor -- it is queueing theory.

### Setting WIP Limits

A practical starting point: WIP limit per state = team size + a small buffer. Tighten over time as the team gets comfortable finishing-before-starting.

A common refinement (Anderson): explicit WIP limits per state, displayed on the board. When a state is at capacity, no new items enter -- forcing the team to swarm on what is there and finish it.

### WIP Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|--------------|---------|-----|
| No WIP limits | Multitasking everywhere; cycle time creep | Set per-state limits at current median |
| Hidden WIP | Items in "In Progress" that nobody is actively working on | Aging WIP review; close or restart |
| Per-person WIP limits | One person dominating two items; team feels productive | WIP is a *team* limit, not a per-person limit |
| Limit busted "just this once" | Limits routinely ignored | Either lower limits or stop pretending they matter |

---

## 7. Aging WIP

The most actionable flow metric. A list of every currently-in-flight item with its age (days since start).

### How to Use Aging WIP

In daily standup, ask only one question per aging item: "What is the plan today to move this forward?"

Items older than the team's 85th-percentile cycle time are statistical outliers. They almost always:

- Have an unresolved dependency.
- Are larger than they should be (and should be split).
- Are blocked by a decision that nobody is pushing on.
- Have been quietly abandoned and need to be closed.

### Aging WIP Report Format

| ID | Title | Age (days) | Status | Assignee | Days over 85th %ile |
|----|-------|-----------:|--------|----------|--------------------:|
| ENG-201 | OAuth migration | 18 | In Progress | (any) | +7 |
| ENG-198 | Mobile push fix | 14 | In Review | (any) | +3 |

Run this report at the start of every standup. Most teams find this single change improves cycle time more than any tooling investment.

---

## 8. Cumulative Flow Diagram (CFD)

A stacked-area chart showing the count of items in each workflow state over time.

```
^  Cumulative Items
|
|        Done /////////
|        ////////////
|       /////////
|      / In Review ----
|     /  ----
|    /  In Progress ...
|   /  ...
|  /  Ready - - -
| /  - - -
|/__________________> Time
```

### What to Look For

- **Parallel bands.** Healthy flow: bands grow at roughly the same rate.
- **Widening "In Progress" band.** WIP is growing; cycle time will follow.
- **Flat "Done" band.** Delivery has stalled; debug upstream.
- **Sudden vertical jumps.** Status transitions logged in batch, not real time.
- **Bands crossing each other.** Items moving backwards through the workflow (a churn signal).

### CFD vs Burndown

| | Cumulative Flow Diagram | Burndown |
|---|---|---|
| Time horizon | Multi-sprint, multi-month | Single sprint |
| Question answered | Where is work accumulating? | Are we tracking toward the commitment? |
| Useful for | Process improvement, bottleneck detection | Sprint operational management |

Both are useful; they answer different questions.

---

## 9. Tracker-Specific Export Tips

### Jira

Use the `jira-python` library or the REST API:

```bash
# Pseudocode (Jira Cloud, as of September 2026)
# 1) Find the issues -- enhanced JQL search, token pagination
GET /rest/api/3/search/jql?jql=project=ENG AND updated >= -90d&fields=key,created,resolutiondate&maxResults=100
#    repeat with &nextPageToken=<token> until the response has no nextPageToken

# 2) Pull full status history in bulk (up to 1000 issues per request)
POST /rest/api/3/changelog/bulkfetch
{"issueIdsOrKeys": ["ENG-1", "ENG-2"], "fieldIds": ["status"]}
#    paginate with nextPageToken
```

The legacy `/rest/api/3/search` (and `/rest/api/2/search`) endpoint is deprecated and being removed (Atlassian changelog CHANGE-2046). The replacement returns no `total`, has no `startAt`, and returns only `id` unless you list `fields` explicitly. `expand=changelog` on search returns only *recent* updates, so use the changelog endpoints above for complete cycle-time history. Queries must be bounded (include a restriction such as a project or date). See the [Issue search](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/) and [Issues](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/) API reference.

Map each `issueChangeLogs[].changeHistories[].items` entry with `field == "status"` (its `fromString` -> `toString`, timestamped by the history's `created`) to `status_history` in the input JSON.

### Linear

Use Linear's GraphQL API:

```graphql
query {
  issues(first: 200, filter: { team: { key: { eq: "ENG" } } }) {
    nodes {
      identifier title createdAt
      history { nodes { fromState { name } toState { name } createdAt } }
    }
  }
}
```

Map `history.nodes` -> `status_history`.

### GitHub Projects

Less straightforward (no built-in status history); requires reading project field updates via the GraphQL API. The `events` endpoint of the issues API offers `labeled` / `unlabeled` events that approximate status if your team uses labels-as-status.

---

## 10. Common Reporting Cadences

| Cadence | Audience | Artifacts |
|---------|----------|-----------|
| **Daily standup** | Team | Aging WIP report |
| **Weekly** | Team + lead | Throughput trend, cycle-time distribution snapshot |
| **Per sprint review** | Team + stakeholders | CFD for the sprint, week-over-week throughput |
| **Quarterly** | Leadership | Rolling 12-week throughput, cycle-time stability, dependency-correlated delays |

---

## 11. Anti-Patterns to Avoid

| Anti-Pattern | Why It Backfires |
|--------------|------------------|
| Per-person cycle time | Punishes collaboration; encourages individual silos |
| Throughput target ("hit 10/week") | Encourages closing items that are not actually done; "scope-cutting to finish" |
| Cycle time SLA without WIP limit | Mathematically impossible per Little's Law |
| Reporting averages only | Hides skew; over-promises delivery |
| Mixing types in one number | Bugs and features have different distributions; combined numbers mislead |
| Tracking cycle time only for completed items | Survivorship bias; ignores items that are still in flight and aging |

---

## 12. References

- Vacanti, Daniel S. *Actionable Agile Metrics for Predictability*. ActionableAgile Press, 2015.
- Vacanti, Daniel S. *When Will It Be Done?* ActionableAgile Press, 2020.
- Anderson, David J. *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press, 2010.
- Little, John D. C. "A Proof for the Queuing Formula: L = λW." Operations Research, 9(3), 1961.
- Reinertsen, Donald G. *The Principles of Product Development Flow*. Celeritas, 2009.

## references/metrics-and-tool-reference.md

# Flow Metrics Definitions, Workflow & Tool Reference

Read this when you need the precise definitions of the four flow metrics, the step-by-step analysis workflow, troubleshooting, success criteria, or the full `flow_metrics.py` CLI flags and input/output JSON schemas. Moved verbatim from `SKILL.md`.

## The Four Flow Metrics (Vacanti)

### 1. Lead Time

The total elapsed time from the moment a work item is committed (created or moved out of backlog into "Ready") to the moment it is delivered (closed / deployed / accepted).

Lead time is the customer's view: "how long from when I asked to when I got it?"

### 2. Cycle Time

The elapsed time from when work actively started (item moves to "In Progress") to delivery. Cycle time excludes time the item sat in "Ready" or "To Do."

Cycle time is the team's view: "how long does it take us to finish what we start?"

Always report cycle time as a distribution (50th, 85th, 95th percentile), never as an average. Averages hide variability and lead to over-confident commitments.

### 3. Throughput

The count of items completed per unit time (typically per week or per sprint). Throughput is the team's delivery rate.

Throughput is more reliable than story-point velocity because it counts atomic units (one completed thing = one), avoiding estimation bias.

### 4. Work-In-Progress (WIP)

The count of items started but not yet finished at a point in time. WIP includes everything in any "in flight" state (In Progress, In Review, Blocked, etc.).

### Little's Law

The relationship that ties the four together (John D. C. Little, 1961):

```
Average Cycle Time = Average WIP / Average Throughput
```

The practical implication: **the fastest way to reduce cycle time is to reduce WIP.** Working on fewer things at once forces finishing before starting and exposes the bottlenecks.

### Aging WIP

The aging WIP report lists every item currently in flight and its age (days since started). Items older than the team's 85th-percentile cycle time are flagged as "at risk" -- they are statistical outliers and warrant explicit attention in standups and refinements.

Aging WIP is the single most actionable flow metric for daily use. Most teams ignore it. Most teams have a few items quietly aging in the corners.

## Workflow

1. **Export issue history** from your tracker as JSON. Required fields per issue: `id`, `title`, `created_at`, `status_history` (list of `{status, entered_at}`), and ideally `team` and `type`. See `references/flow-metrics-guide.md` for tracker-specific export instructions.
2. **Define your states.** Tell the tool which status names map to "Ready" (commitment), "In Progress" (active work start), and "Done" (delivery). Defaults: `Ready`/`To Do`, `In Progress`, `Done`.
3. **Run the analyzer.** `python3 scripts/flow_metrics.py --input issues.json --format markdown --as-of <today>`
4. **Review the distribution.** Look at 85th-percentile cycle time, not the average. Identify aging WIP that exceeds it.
5. **Generate the CFD.** Use `--format mermaid` to produce a cumulative flow diagram for share-back in retrospectives or exec reports.
6. **Calibrate WIP limits.** Use the WIP histogram to set per-state WIP limits at roughly the team's current 50th percentile.
7. **Re-run weekly.** Track the trend, not the snapshot. Flow metrics drift; only sustained changes are meaningful.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Cycle time looks great but team feels slow | "In Progress" defined too narrowly; long "In Review" or "Blocked" time excluded | Map all in-flight states to the active set; verify with the team that the boundary matches "start" and "finish" reality |
| Throughput is unstable week-over-week | Sprint commitment volume changes; team-size changes; vacation periods | Report a rolling 6-8 week trend; annotate the chart with known events |
| Lead time is enormous compared to cycle time | Items sit in backlog for months before commitment | Either accept (lead time is bounded by intake, not delivery) or close stale backlog items; report lead time only for items committed within the last quarter |
| Aging WIP list is enormous | Stale items left "In Progress" without movement | Triage during standup; close, split, or restart each item; consider a WIP limit to prevent recurrence |
| 85th percentile cycle time differs sharply between work types | Mixed bugs, features, spikes in one stream | Filter by `type` and report per-type cycle time; predictability comes from like-with-like comparison |
| CFD lines flatten then jump | Status transitions logged in batch (end-of-day or weekly sync) rather than real-time | Either accept the visual artifact or migrate to real-time updates in the tracker |
| Tool errors on missing `status_history` | Tracker export incomplete; some issues lack transition data | Use `--ignore-missing` to skip incomplete items; investigate the export query |

## Success Criteria

- All four flow metrics are computed and reported with both central tendency (median) and tail (85th percentile).
- The cumulative flow diagram is generated and shared in at least one retrospective per sprint.
- Aging WIP list is reviewed at least weekly; items exceeding 85th percentile cycle time get explicit attention.
- WIP limits are set per state based on observed flow rather than guessed.
- Trend reporting uses rolling windows (6-8 weeks), not single snapshots.
- Cycle time distribution is reported, never just an average.
- Flow metrics are used at the team level only; never for individual performance ranking.

## Tool Reference

### flow_metrics.py

Computes the four core flow metrics plus aging WIP and a Mermaid cumulative flow diagram from issue status-transition history.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input` | path | (required unless `--demo`) | JSON file with issue history |
| `--demo` | flag | off | Use built-in sample data instead of `--input` |
| `--format` | string | `markdown` | One of `json`, `markdown`, `mermaid`, `confluence`, `notion`, `linear` |
| `--output` | path | stdout | Output file path |
| `--ready-state` | string (repeatable) | `Ready`, `To Do` | Status name(s) representing committed-not-started |
| `--in-progress-state` | string (repeatable) | `In Progress`, `In Review` | Status name(s) representing active work |
| `--done-state` | string (repeatable) | `Done`, `Closed` | Status name(s) representing delivered |
| `--type` | string | (none) | Filter by issue type (e.g., `bug`, `feature`) |
| `--window-days` | int | 60 | Trailing window in days for throughput trend |
| `--ignore-missing` | flag | off | Skip issues that lack required fields |
| `--as-of` | YYYY-MM-DD | latest timestamp in the data | Compute metrics as of this date; pass today for a live board |

### Input JSON schema

```json
{
  "issues": [
    {
      "id": "ENG-101",
      "title": "Add CSV export",
      "type": "feature",
      "team": "platform",
      "created_at": "2026-04-01T10:00:00Z",
      "status_history": [
        {"status": "Backlog",     "entered_at": "2026-04-01T10:00:00Z"},
        {"status": "Ready",       "entered_at": "2026-04-15T09:00:00Z"},
        {"status": "In Progress", "entered_at": "2026-04-17T11:30:00Z"},
        {"status": "In Review",   "entered_at": "2026-04-22T16:00:00Z"},
        {"status": "Done",        "entered_at": "2026-04-24T10:00:00Z"}
      ]
    }
  ]
}
```

### Output JSON schema

Wrapped per `SHARED_OUTPUT_SCHEMA.md`:

```json
{
  "schema": "pm/cycle-time-analyzer/v1",
  "generated_at": "2026-05-21T00:00:00Z",
  "data": {
    "as_of": "2026-05-21",
    "summary": {
      "lead_time_p50_days": 9.5,
      "lead_time_p85_days": 22.1,
      "cycle_time_p50_days": 4.2,
      "cycle_time_p85_days": 11.0,
      "throughput_per_week": 6.4,
      "wip_count": 12
    },
    "aging_wip": [
      {"id": "ENG-117", "title": "...", "age_days": 14.2, "status": "In Progress"}
    ],
    "cumulative_flow": [
      {"date": "2026-04-01", "Backlog": 32, "Ready": 6, "In Progress": 4, "In Review": 1, "Done": 18}
    ]
  }
}
```

## references/red-flags.md

# Red Flags: Cycle Time Analyzer

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the `flow_metrics.py` output before sharing in retro or exec review. Each red flag shows the *bad* version next to the *good* version, anchored to Daniel Vacanti's flow metrics and Little's Law.

---

## Red Flag 1: Optimizing for the wrong percentile

**Symptom.** Team reports "average cycle time: 4 days, looking great". Variance is huge — 20% of items take 14+ days.

**Why it's bad.** Vacanti's central argument: report cycle time as a distribution (50th, 85th, 95th percentile), never as an average. The mean hides the long tail; commitments based on the mean miss 30-40% of the time. The team commits to "4 days" and ships 30% of items in 14 days, then is surprised when stakeholders complain.

**Bad example:**
> "Sprint metrics summary: 'Average cycle time 4.1 days. Throughput 6/week. Stable and healthy.'"

**Good example:**
> "Cycle time distribution (Vacanti style): p50 = 4 days, p85 = 11 days, p95 = 18 days. 'We finish half our work in 4 days but the long tail extends to 18 days; commitments at p50 will miss 50% of the time. Use p85 for stakeholder commitments.' Throughput: 6/week (range 3-9 across last 8 weeks)."

**How to catch it.** Look at the metrics output. If only `average` or `mean` appears (no `p85` or `p95`), the distribution is hidden.

---

## Red Flag 2: Ignoring aging WIP

**Symptom.** Daily standup reads the same 4 in-progress tickets each day. Nobody talks about the one that has been "In Progress" for 23 days.

**Why it's bad.** Aging WIP is the single most actionable flow metric for daily use. Items older than the team's p85 cycle time are statistical outliers — they will keep aging unless someone intervenes. Ignoring them means the team's actual cycle time is worse than reported, hidden in a few quiet long tails.

**Bad example:**
> "Standup: each engineer goes through their tickets. ENG-117 'still investigating' — same answer every day for 3 weeks. No one flags it."

**Good example:**
> "Standup opens with aging WIP report (auto-generated): 'ENG-117 in 'In Progress' for 23 days (p85 cycle time is 11 days; this is 2x outlier). Bartek to triage in 30 min after standup.' At triage: close it, split it, restart it, or escalate. ENG-117 either advances or is killed within 48 hours."

**How to catch it.** Pull the aging WIP list. Any item > 1.5x team's p85? If yes and it's not on the standup agenda, aging is being ignored.

---

## Red Flag 3: Flow metrics used to rank individuals

**Symptom.** "Engineer A's average cycle time is 3 days; Engineer B's is 7 days; we should coach B."

**Why it's bad.** Flow metrics are team-level signals. Per-assignee cycle time produces local optimization (engineers avoid hard tickets, hand off prematurely, gaming starts) and destroys team behavior. Vacanti and Anderson are explicit: do not use these metrics to evaluate individuals.

**Bad example:**
> "Quarterly perf review for Engineer B: 'Your average cycle time of 7 days is double the team average. Improve velocity.'"

**Good example:**
> "Flow metrics are reported team-level only. Engineer B happens to take on the most complex bugs and architecturally-risky stories — that's by design. Performance reviews use different signals (peer feedback, design quality, mentorship). Tooling does not expose per-assignee cycle time."

**How to catch it.** Look at where flow metrics are reported. If they appear in any performance review document, the line has been crossed.

---

## Red Flag 4: "In Progress" defined too narrowly

**Symptom.** Cycle time looks low (median 3 days). Team feels slow. Long "In Review" and "Blocked" periods are excluded from the calculation.

**Why it's bad.** The team's lived experience is the total time from "start" to "finish". If the metric excludes Review and Blocked, it understates real cycle time. The team distrusts the data because it does not match reality.

**Bad example:**
> "Config: `--in-progress-state 'In Progress'`. Median cycle time: 3.2 days. Team morale: 'these numbers can't be right.'"

**Good example:**
> "Config: `--in-progress-state 'In Progress' --in-progress-state 'In Review' --in-progress-state 'Blocked'`. Median cycle time: 6.8 days. Team validates: 'this matches what we feel.' Decision: investigate 'In Review' (mean 2.1 days) as the constraint."

**How to catch it.** Ask the team: "does the metric match what you feel?" If no, the state mapping is wrong.

---

## Red Flag 5: WIP limits set by guess, not by data

**Symptom.** Team adopts WIP=5 per engineer based on "feels right" rather than the team's current histogram.

**Why it's bad.** Little's Law: Throughput = WIP / Cycle Time. WIP limits below the team's current 50th percentile aggressively reduce cycle time but cause queue starvation upstream. Above the team's 85th percentile and they have no effect. Calibrating by guess produces no improvement.

**Bad example:**
> "Team standardizes on WIP limit = 5 per engineer because 'that feels manageable'."

**Good example:**
> "WIP histogram analysis: team currently averages 3.2 in-flight items per engineer, with 85th percentile at 5. New WIP limit set at 3 per engineer (just below current 50th percentile). Goal: force finishing before starting. Re-measure cycle time after 4 weeks; expect 15-25% reduction if Little's Law holds."

**How to catch it.** Ask: "how was this WIP limit set?" If the answer doesn't reference the team's actual WIP distribution, it's a guess.

---

## Red Flag 6: Story-point velocity as the primary metric

**Symptom.** Team reports "30 SP velocity, 95% completion rate" but ships less actual work than 3 quarters ago when they reported 22 SP.

**Why it's bad.** Story points are subject to estimation drift — teams inflate estimates over time. Vacanti's argument: count throughput (atomic completed units), not story points. Throughput is bias-resistant. Comparing SP-velocity over quarters compares two different yardsticks.

**Bad example:**
> "Q3 review: '30 SP velocity, up from 22 in Q2. Team is shipping more.' Engineering complains: 'we feel slower than ever.'"

**Good example:**
> "Q3 review: 'Throughput 6.2 items/week (Q2: 6.8). SP velocity increased because estimates inflated. Real picture: throughput flat, with longer-tail outliers in Q3. Investigate the 2 stories that took > p85 cycle time; they consumed 30% of capacity.'"

**How to catch it.** Compare throughput trend (items/week) to SP trend. Divergence means SP estimates are drifting.

---

## Red Flag 7: Goodhart's gaming

**Symptom.** A month after introducing cycle-time targets, the team's median cycle time drops from 6 days to 3.5 days. Throughput also drops. Customers don't notice improvement.

**Why it's bad.** Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. Teams game cycle time by splitting work artificially, marking tickets "done" before they truly are, or skipping review. The number goes down; real delivery does not improve.

**Bad example:**
> "OKR: 'reduce median cycle time from 6 days to 3 days by Q3 end.' Team hits 3 days. Throughput drops 20%. Customer-visible regressions up 3x. 'But the metric is green!'"

**Good example:**
> "Cycle time is a diagnostic, not a target. Quarterly review tracks the trend across 3 metrics: cycle time p85, throughput, and quality (escaped defects, customer-reported regressions). If cycle time drops but throughput or quality also drops, the gaming hypothesis is on the table. Goal is to lower cycle time *while sustaining* throughput and quality."

**How to catch it.** Look at cycle time trend together with throughput and quality trends. If cycle time improves and the others degrade, gaming is suspected.

---

## Red Flag 8: Mixed work types reported together

**Symptom.** "Median cycle time 4.5 days" — but the team mixes bugs (median 1 day), features (median 6 days), and spikes (median 9 days) in one number.

**Why it's bad.** Predictability comes from like-with-like comparison. A team that ships 70% bugs in March and 70% features in April will show cycle-time "improvement" in March that's actually mix shift, not improvement.

**Bad example:**
> "March: median 3 days. April: median 6 days. 'We got slower.' (Actually: March was 80% bug-fix sprint; April was 80% feature sprint. Like-with-like cycle time was unchanged.)"

**Good example:**
> "Cycle time reported per work type: bugs (p50 1.2d, p85 3d), features (p50 6d, p85 11d), spikes (p50 4d, p85 9d). Trends compared within type. Mix-adjusted overall trend shown separately."

**How to catch it.** Look for `--type` filtering in the report. If everything is aggregated, mix shift is hidden.

---

## Red Flag 9: Lead time conflated with cycle time

**Symptom.** Exec asks "how long does it take you to ship a feature?" Team answers 6 days (cycle time). Customer-perceived time from request to delivery is 11 weeks (lead time).

**Why it's bad.** Lead time is the customer view ("from when I asked to when I got it"). Cycle time is the team view ("from when we started to when we finished"). They are different metrics. Reporting cycle time as the answer to a lead-time question creates expectation mismatches.

**Bad example:**
> "Exec: 'how long to ship this?' Team: '6 days.' Exec messages customer: '6 days.' Customer's actual experience: 11 weeks because the item sat in backlog for 10 weeks before starting."

**Good example:**
> "Exec: 'how long to ship this?' Team: 'Cycle time p85 is 11 days once we start. Lead time p85 — from when the request entered the backlog — is 52 days because the backlog is currently 6 weeks deep. If you want to commit a customer to a date, use lead time.' Exec commits 11 weeks; customer is pleasantly surprised at 7."

**How to catch it.** Per stakeholder, which metric matters? Customers care about lead time. Engineering planning cares about cycle time. Report both with labels.

---

## Red Flag 10: CFD shown without context

**Symptom.** Cumulative Flow Diagram is shared in retro. Engineers stare at it. Nobody can act on it.

**Why it's bad.** A CFD is information-dense; without annotation and a narrative, it's noise. Bands widening = WIP growing. Bands flattening = throughput dropping. Without the team knowing what to look for, the diagram does not produce action.

**Bad example:**
> "Sprint retro slide: CFD chart. Caption: 'here is our CFD.' Team: 'okay.'"

**Good example:**
> "CFD with annotations: 'Note widening of 'In Review' band starting Week 12 — review backlog growing. Throughput in Week 13 dropped from 7/week to 4/week, coinciding with two engineers on PTO. Discussion: should we cap concurrent reviews per engineer to prevent recurrence?' Specific narrative + 1 question to discuss."

**How to catch it.** Read the retro deck. Does the CFD have annotations and a discussion question? If not, it's decoration.

---

## Red Flag 11: Throughput trend reported as a single sprint number

**Symptom.** Status update reads "Sprint 23 throughput: 6 items". Next sprint: 4. Next: 9. Each reported in isolation.

**Why it's bad.** Single-sprint numbers fluctuate wildly with vacations, holidays, scope of work. Trends only emerge over 6-8 sprints. Reporting one-sprint snapshots leads to false-alarm panics and false-celebration parties.

**Bad example:**
> "Sprint 24 update: 'Throughput dropped to 4 items this sprint, down from 6. Investigating slowdown.'"

**Good example:**
> "Sprint 24 update: 'Throughput 4 items this sprint. 8-week rolling: 5.8 items/week (range 3-9). Sprint 24 is within normal variance; no investigation needed. Trend is stable.' Annotations: '2 engineers on PTO this sprint.'"

**How to catch it.** Is the throughput metric reported as a single number or as a trend with a window? Single = noise.

---

## Red Flag 12: Long-stuck items hidden in backlog states

**Symptom.** Backlog has 80 items. Nobody knows that 18 of them have been in "Backlog" for over 12 months. Lead time on those is meaningless but they pollute the data.

**Why it's bad.** Stale backlog items inflate lead time without representing real work. They also distort prioritization — the team thinks they "have a lot of work" when 25% of the queue is dead. Vacanti's discipline: prune the backlog regularly; report lead time only for items committed within the last quarter.

**Bad example:**
> "Lead time p85: 142 days. 'We are slow.' (Reality: 18 items have been in backlog for 400+ days and skew the distribution.)"

**Good example:**
> "Quarterly backlog hygiene: items in 'Backlog' state > 90 days reviewed; 18 closed as stale ('no longer aligned with strategy'), 4 split into smaller stories. Lead time p85 recomputed on committed-in-last-quarter cohort: 38 days."

**How to catch it.** Filter backlog items by age. If > 20% of the backlog is older than 6 months, lead time is being polluted.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Optimizing for the wrong percentile | Is p85 (or p95) shown alongside the median? |
| 2 | Ignoring aging WIP | Is aging WIP report part of standup? |
| 3 | Per-individual ranking | Does any perf review document show per-assignee cycle time? |
| 4 | "In Progress" too narrow | Does the metric match the team's felt experience? |
| 5 | WIP limits by guess | Was the WIP limit calibrated to the team's distribution? |
| 6 | Story-point velocity as primary | Throughput trend vs SP trend — diverging? |
| 7 | Goodhart's gaming | Did cycle time improve while throughput/quality dropped? |
| 8 | Mixed work types together | Is cycle time reported per type? |
| 9 | Lead time vs cycle time confusion | Which metric matters for this stakeholder? |
| 10 | CFD without context | Does the CFD have annotations + a discussion question? |
| 11 | Single-sprint throughput | Is the trend reported with a rolling window? |
| 12 | Stale backlog polluting lead time | What % of backlog is > 6 months old? |

## Related Reading

- SKILL.md Troubleshooting
- references/flow-metrics-guide.md
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (2015)
- Daniel Vacanti, *When Will It Be Done?* (2020)
- `scrum-master/` (for SP velocity and Monte Carlo forecasting)
- `dependency-map/` (for cross-team coordination affecting cycle time)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/cycle-time-analyzer
