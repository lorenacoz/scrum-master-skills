---
description: "Pick a prioritization method and rank a backlog: RICE, ICE, opportunity, MoSCoW and weighted scoring, plus four reference-only methods. Use when ranking features, problems or initiatives against each other."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Prioritization Framework Expert

## Overview

Nine prioritization frameworks and when to use each. Five are scored by the tool (RICE, ICE, Opportunity Score, MoSCoW, Weighted Decision Matrix); four are reference-only and applied by hand (Eisenhower, Impact vs Effort, Risk vs Reward, Kano). The core principle: prioritize problems (opportunities), not features. Features are solutions to problems. If you prioritize features directly, you skip the step of understanding whether the problem is worth solving.

## Core Capabilities

- **9 frameworks** — RICE, ICE, Opportunity Score, Eisenhower, Impact vs Effort, Risk vs Reward, Kano, Weighted Decision Matrix, MoSCoW (full definitions, formulas, and worked examples in `references/frameworks-catalog.md`).
- **Framework selection** — a decision tree maps the thing you are prioritizing (problems, features, personal tasks, high-uncertainty bets) to the right method.
- **Automated scoring** — `prioritization_scorer.py` ranks items for RICE, ICE, Opportunity, MoSCoW, and Weighted Decision Matrix.
- **Two-step discipline** — prioritize problems first (Opportunity Score), then prioritize solutions (RICE/ICE).

## When to Use

- **Backlog Grooming** -- Too many items, need to rank them objectively.
- **Quarterly Planning** -- Deciding which initiatives to invest in.
- **Stakeholder Alignment** -- Need a structured way to resolve competing priorities.
- **Feature Triage** -- Quick sorting of a long list into actionable categories.

## Clarify First

Before scoring, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **What you're ranking:** problems/opportunities vs features vs personal tasks (the decision tree picks the framework from this).
- **Framework:** rice / ice / opportunity / moscow / weighted (each requires different score fields and emits different rankings).
- **Quality of the estimates:** measured data vs guesses for reach/impact (guesses make RICE/ICE precision misleading; switch to a coarser method).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Decide what you are ranking.** Problems first (Opportunity Score), then solutions to the chosen problems (RICE or ICE). Personal tasks: Eisenhower. Uncertain bets: Risk vs Reward. Decision tree: `references/frameworks-catalog.md`.
2. **Gather estimates with their sources.** Reach from data, Effort from engineering, Confidence capped at 50% without a written source.
3. **Score:**

```bash
python3 scripts/prioritization_scorer.py \
  --input assets/sample_rice_items.json --framework rice
# --demo --framework ice|opportunity|moscow|weighted shows each input shape; --format json for pipelines
```

4. **Verify** [RECOMMENDED] before publishing: spot-check one score by hand (the report prints each formula), check no more than 30% of items share the top Impact value, and read the top five as a group: does the order match the strategy? If not, find which estimate is wrong rather than overriding the rank.

Input schemas per framework: `references/tool-and-troubleshooting.md`. Missing fields fall back to defaults (for example, MoSCoW items without a `category` are "Could Have"), so check the report for items that all landed in one bucket.

**Exit codes:** 0 ranked; 2 missing file, invalid JSON, wrong shape, or items that do not fit the chosen framework.

## Anti-Patterns

### Every item scores massive impact
**Mistake:** Most of the backlog gets Impact = 3 on the RICE scale.
**Why it happens:** Each item has a champion, and nobody wants theirs marked minor.
**Instead:** RICE ranks items against each other, so uniform impact ranks nothing. If more than 30% of items score 3, recalibrate: only items with behavioural or revenue evidence keep it.

### Confidence padded to reach the cut line
**Mistake:** A favoured item's Confidence moves from 50% to 80% with no new evidence.
**Why it happens:** The ranking was decided first, and the score is adjusted to match it.
**Instead:** Add a Confidence Source column. An item with no written source is capped at 50%.

### Effort scored without engineering
**Mistake:** The PM sizes Effort alone, as small, medium or large.
**Why it happens:** It is quicker than booking engineers, and backend, security and migration work is hard to see from the product side.
**Instead:** Effort is the denominator, so a wrong estimate flips the ranking. Don't publish a score until an engineer has signed off on its Effort.

Eight more in `references/red-flags.md`; framework-specific mistakes in `references/prioritization-guide.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/frameworks-catalog.md](references/frameworks-catalog.md)** — full definitions, formulas, strengths/weaknesses, and worked examples for all 9 frameworks, the framework decision tree, and the "prioritize problems, not features" principle. Read when choosing or applying a specific framework.
- **[references/prioritization-guide.md](references/prioritization-guide.md)** — detailed formulas, decision tree, and facilitation tips. Read when facilitating a scoring session with a group.
- **[references/red-flags.md](references/red-flags.md)** — anti-patterns and warning signs in prioritization practice. Read when a process feels off or results are being gamed.
- **[references/tool-and-troubleshooting.md](references/tool-and-troubleshooting.md)** — `prioritization_scorer.py` flags, per-framework input JSON schemas, troubleshooting table, and success criteria. Read when running the tool or diagnosing scoring problems.

## Files

| File | Purpose |
|---|---|
| `scripts/prioritization_scorer.py` | Scores and ranks for the five scored frameworks |
| `assets/sample_rice_items.json` | Five RICE items (Advanced search scores 2666.67) |
| `assets/prioritization_matrix_template.md` | Manual scoring templates for every framework |
| `examples/rice-vs-ice-q3-backlog.md` | Same backlog ranked two ways |

## Scope & Limitations

**In Scope:**
- 9 prioritization frameworks explained
- Scored and ranked by the tool (5): RICE, ICE, Opportunity Score, MoSCoW, Weighted Decision Matrix
- Reference-only, applied by hand (4): Eisenhower, Impact vs. Effort, Risk vs. Reward, Kano
- Framework selection guidance via Decision Tree
- Demo data for each framework to illustrate input/output formats

**Out of Scope:**
- Real-time Jira/Linear backlog integration (manual JSON input required)
- Cost-of-delay or WSJF calculations (see `senior-pm/` skill for SAFe portfolio prioritization)
- User research to gather importance/satisfaction data for Opportunity Score (see `product-team/` skills)
- Strategic portfolio allocation decisions (see `senior-pm/` skill)

**Important Caveats:**
- No framework produces a "correct" answer. Prioritization frameworks are decision-support tools that structure conversation, not algorithms that replace judgment.
- RICE and ICE are best for data-rich environments. If your reach and impact estimates are pure guesses, the precision of the formula is misleading.
- The most successful teams combine frameworks: start with Opportunity Score to identify the right problems, then use RICE to rank solutions.
- For teams with 50+ people or multiple stakeholder groups, use WSJF or Weighted Decision Matrix with agreed criteria to ensure buy-in.

## Integration Points

| Integration | Direction | Description |
|------------|-----------|-------------|
| `execution/outcome-roadmap/` | Feeds into | Prioritized items inform Now/Next/Later horizon placement |
| `execution/create-prd/` | Feeds into | Top-priority items become PRD candidates with P0/P1/P2 feature labels |
| `execution/brainstorm-okrs/` | Complements | Prioritized initiatives inform which OKR theme to focus on this quarter |
| `discovery/identify-assumptions/` | Receives from | Assumption risk scores inform item confidence ratings in RICE/ICE |
| `scrum-master/` | Feeds into | Prioritized backlog items feed sprint planning commitment decisions |
| `senior-pm/` | Receives from | Portfolio-level WSJF or strategic priorities constrain team-level prioritization |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/frameworks-catalog.md

# Prioritization Frameworks Catalog

Read this when you need the full definition, formula, strengths/weaknesses, and worked example for any of the 9 frameworks, or the decision tree for choosing among them.

## Framework Decision Tree

Use this to pick the right framework for your situation:

```
START: What are you prioritizing?
  |
  +-- Customer problems/opportunities
  |     -> Opportunity Score (recommended)
  |
  +-- Features or initiatives
  |     |
  |     +-- Need a quick sort (< 15 items)?
  |     |     -> ICE or Impact vs Effort
  |     |
  |     +-- Need rigorous scoring (15+ items)?
  |     |     -> RICE
  |     |
  |     +-- Need stakeholder buy-in on criteria?
  |     |     -> Weighted Decision Matrix
  |     |
  |     +-- Need to categorize requirements?
  |           -> MoSCoW
  |
  +-- Personal PM tasks
  |     -> Eisenhower Matrix
  |
  +-- High-uncertainty initiatives
  |     -> Risk vs Reward
  |
  +-- Understanding user expectations (not prioritizing)
        -> Kano Model
```

## The 9 Frameworks

### 1. Opportunity Score (Recommended for Customer Problems)

**Source:** Dan Olsen, *Lean Product Playbook*

**Formula:** `Score = Importance x (1 - Satisfaction)`

- **Importance** (0-10): How important is this problem to the customer?
- **Satisfaction** (0-1): How well do existing solutions satisfy this need? (0 = not at all, 1 = perfectly)

**Why it works:** It identifies the biggest gaps between what customers need and what they currently have. High importance + low satisfaction = high opportunity.

**Example:**

| Problem | Importance | Satisfaction | Score |
|---------|-----------|-------------|-------|
| Finding products quickly | 9 | 0.3 | 6.3 |
| Comparing prices | 7 | 0.8 | 1.4 |
| Tracking order status | 8 | 0.6 | 3.2 |

"Finding products quickly" scores highest because it is very important and poorly solved today.

### 2. ICE -- Impact x Confidence x Ease

**Best for:** Quick prioritization of a short list (under 15 items).

**Formula:** `Score = Impact x Confidence x Ease`

All three scored 1-10:
- **Impact:** How much will this move the target metric?
- **Confidence:** How sure are we about the impact estimate?
- **Ease:** How easy is this to implement? (10 = trivial, 1 = massive effort)

**Strengths:** Fast, simple, includes uncertainty.
**Weakness:** Subjective. Different people give different scores. Best used as a starting point for discussion, not a final answer.

### 3. RICE -- (Reach x Impact x Confidence) / Effort

**Best for:** Rigorous prioritization of a longer list.

**Formula:** `Score = (Reach x Impact x Confidence) / Effort`

- **Reach:** How many users/customers will this affect in a given time period? (number)
- **Impact:** How much will it affect each user? (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal)
- **Confidence:** How sure are we? (100% = high, 80% = medium, 50% = low)
- **Effort:** Person-months of work required (number)

**Strengths:** Reach adds a dimension that ICE misses. Effort is estimated in real units, not abstract scores.
**Weakness:** Requires more data (reach estimates, effort sizing).

### 4. Eisenhower Matrix

**Best for:** Personal task management for PMs, not product prioritization.

**Quadrants:**

|  | Urgent | Not Urgent |
|--|--------|------------|
| **Important** | Do First | Schedule |
| **Not Important** | Delegate | Eliminate |

- **Q1 (Do First):** Crisis, deadline-driven. Handle immediately.
- **Q2 (Schedule):** Strategic work, planning, prevention. This is where PMs should spend most of their time.
- **Q3 (Delegate):** Interruptions, some meetings, some emails. Hand off if possible.
- **Q4 (Eliminate):** Time-wasters, unnecessary meetings. Stop doing these.

### 5. Impact vs Effort (2x2 Matrix)

**Best for:** Quick visual triage in a group setting.

**Quadrants:**

|  | Low Effort | High Effort |
|--|-----------|-------------|
| **High Impact** | Quick Wins (do first) | Major Projects (plan carefully) |
| **Low Impact** | Fill-ins (do if time allows) | Money Pits (avoid) |

**How to use:** Plot items on a whiteboard. Discuss placement. The conversation matters more than the exact position.

### 6. Risk vs Reward

**Best for:** Initiatives with significant uncertainty.

**Extension of Impact vs Effort** that adds an uncertainty dimension:

- **Reward** = Expected impact if successful
- **Risk** = Probability of failure x cost of failure

**Quadrants:**

|  | Low Risk | High Risk |
|--|---------|-----------|
| **High Reward** | Safe Bets (prioritize) | Bold Bets (invest selectively) |
| **Low Reward** | Incremental (batch) | Avoid |

### 7. Kano Model

**Best for:** Understanding customer expectations. Not for prioritization directly.

**Categories:**

- **Must-Be (Basic):** Customers expect these. Absence causes dissatisfaction. Presence does not cause delight. (Example: a login page works.)
- **One-Dimensional (Performance):** More is better, linearly. (Example: faster page loads = happier users.)
- **Attractive (Delighters):** Unexpected features that create excitement. Absence does not cause dissatisfaction. (Example: automatic dark mode based on system setting.)
- **Indifferent:** Customers do not care either way.
- **Reverse:** Some customers actively dislike this feature.

**Use Kano to understand**, then use another framework (RICE, ICE) to prioritize.

### 8. Weighted Decision Matrix

**Best for:** Multi-factor decisions that need stakeholder buy-in.

**Process:**
1. Define criteria (e.g., customer impact, revenue potential, technical feasibility, strategic alignment).
2. Assign weights to each criterion (must sum to 100%).
3. Score each option against each criterion (1-5 or 1-10).
4. Multiply scores by weights and sum.
5. Rank by total weighted score.

**Strengths:** Transparent, auditable, gets stakeholders to agree on criteria before scoring.
**Weakness:** Time-consuming. Best for 5-10 high-stakes decisions, not 50-item backlogs.

### 9. MoSCoW

**Best for:** Requirements categorization within a fixed scope.

**Categories:**
- **Must Have:** Non-negotiable. Without these, the release has no value.
- **Should Have:** Important but not critical. Painful to leave out but the release still works.
- **Could Have:** Desirable. Include if time and resources allow.
- **Won't Have (this time):** Explicitly out of scope. Acknowledged but deferred.

**Rule of thumb:** Must-Haves should be no more than 60% of the total effort. If everything is a Must-Have, nothing is.

## Core Principle: Prioritize Problems, Not Features

Features are solutions. Problems are what matter. Two teams can build different features to solve the same problem. If you prioritize features, you lock in a solution before understanding the problem space.

**Workflow:**
1. List customer problems (use Opportunity Score to rank them).
2. Pick the top problems to solve.
3. Generate multiple solution ideas for each problem.
4. Prioritize solutions using RICE or ICE.
5. Build the highest-scoring solutions.

This two-step approach (prioritize problems, then prioritize solutions) produces better outcomes than a single pass over a feature list.

## references/prioritization-guide.md

# Prioritization Frameworks Guide

Detailed reference for each framework with formulas, when to use, common mistakes, and facilitation tips.

---

## Framework Formulas

### Opportunity Score

```
Score = Importance x (1 - Satisfaction)
```

- **Importance** (0-10): Survey customers. Ask: "How important is [problem/need] to you?"
- **Satisfaction** (0-1): Survey customers. Ask: "How satisfied are you with current solutions for [problem/need]?"

**Interpretation:** A score above 6 represents a strong opportunity. The highest-scoring problems are both very important and poorly served by current solutions.

### ICE

```
Score = Impact x Confidence x Ease
```

All on a 1-10 scale:
- **Impact**: Expected effect on the target metric
- **Confidence**: How certain you are about the impact estimate
- **Ease**: How easy to implement (10 = trivial, 1 = very hard)

**Score range:** 1 to 1,000. Items scoring 500+ are strong candidates.

### RICE

```
Score = (Reach x Impact x Confidence) / Effort
```

- **Reach**: Number of users/customers affected per quarter (raw number, e.g., 5000)
- **Impact**: Degree of effect per user (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal)
- **Confidence**: Certainty as percentage (100% = high data, 80% = some data, 50% = gut feel)
- **Effort**: Person-months of work (e.g., 3 = three person-months)

**Note:** Confidence as a percentage naturally discounts items where you are guessing. A high-impact item with 50% confidence scores half of a high-impact item with 100% confidence.

### Weighted Decision Matrix

```
Score = Sum(criterion_score_i x criterion_weight_i) for all criteria
```

Weights must sum to 1.0 (or 100%).

### MoSCoW

No formula. Categorization only. Rule: Must-Haves should be no more than 60% of total effort.

---

## When to Use Each Framework

| Situation | Recommended Framework | Why |
|-----------|----------------------|-----|
| Ranking customer problems | Opportunity Score | Directly measures problem-solution gap |
| Quick triage of small list | ICE | Fast, low overhead, good enough for short lists |
| Rigorous ranking of large backlog | RICE | Reach dimension matters at scale |
| Personal PM task management | Eisenhower Matrix | Urgent/Important is the right lens for tasks |
| Quick visual group exercise | Impact vs Effort | Physical, collaborative, intuitive |
| High-uncertainty initiatives | Risk vs Reward | Accounts for downside, not just upside |
| Understanding expectations | Kano Model | Classifies needs by type, not priority |
| Multi-stakeholder decisions | Weighted Decision Matrix | Transparent, auditable, builds consensus |
| Scoping a release | MoSCoW | Clear categories for requirement negotiation |

---

## Common Mistakes Per Framework

### Opportunity Score

- **Mistake:** Using internal estimates instead of customer data for importance and satisfaction.
- **Fix:** Survey at least 15-20 customers per segment. Internal estimates are biased toward what the team wants to build.

- **Mistake:** Using demographics to define the segment being surveyed.
- **Fix:** Define segments by the problem they face, then survey that group.

### ICE

- **Mistake:** Scoring in isolation. One person assigns all scores without discussion.
- **Fix:** Have 3-5 people score independently, then discuss discrepancies. The discussion reveals hidden assumptions.

- **Mistake:** All items score 7-8-9 on every dimension (no differentiation).
- **Fix:** Force-rank first, then score. Or use a wider scale to create separation.

### RICE

- **Mistake:** Inflating reach estimates to game the system.
- **Fix:** Define reach precisely: "How many users will encounter this feature in Q2?" Use data, not hopes.

- **Mistake:** Giving everything 100% confidence.
- **Fix:** Reserve 100% for items with strong data. Use 80% for informed estimates, 50% for guesses.

### MoSCoW

- **Mistake:** Everything is "Must Have."
- **Fix:** The test: "If we ship without this, does the product have zero value?" If no, it is not a Must Have.

- **Mistake:** "Won't Have" treated as "never" instead of "not this time."
- **Fix:** Relabel to "Won't Have This Time" to make deferral explicit and non-permanent.

### Weighted Decision Matrix

- **Mistake:** Choosing criteria after seeing the options (biasing toward a preferred choice).
- **Fix:** Define and weight criteria before anyone scores any options.

- **Mistake:** Too many criteria (10+). Dilutes each criterion's influence.
- **Fix:** Maximum 5-6 criteria. If more seem needed, combine related ones.

---

## Combining Frameworks

Frameworks are not mutually exclusive. A common combination:

1. **Opportunity Score** to rank problems worth solving.
2. **RICE** to rank solution ideas for the top problems.
3. **MoSCoW** to scope the first release of the winning solution.

Another combination for team prioritization:

1. **Impact vs Effort** for a quick visual sort in a group setting.
2. **ICE** to add rigor to the top quadrant items.
3. **Eisenhower** for the PM's personal task list afterward.

---

## Facilitating Prioritization Sessions

### Before the Session

1. **Define the decision**: What exactly are we prioritizing? (Features? Problems? Initiatives?)
2. **Choose the framework**: Match to the situation using the decision tree.
3. **Prepare the data**: List all items. Include brief descriptions. Remove duplicates.
4. **Pre-score (optional)**: Have participants score independently before the session. Discuss discrepancies during the session.

### During the Session

1. **Align on criteria** (5 min): Confirm what the scores mean. What is a 9 vs a 7 for impact?
2. **Score independently** (10 min): Each participant scores in silence. No groupthink.
3. **Reveal and discuss** (20 min): Show scores. Focus on items with high variance between scorers. That is where hidden assumptions live.
4. **Converge** (10 min): Agree on final scores. Use the median, not the average (less susceptible to outliers).
5. **Rank and decide** (5 min): Sort by score. Confirm the top 3-5 items feel right. If the ranking feels wrong, you missed a criterion.

### After the Session

1. Document the scores and the rationale.
2. Share with stakeholders who were not in the room.
3. Revisit in 4-6 weeks to see if priorities changed based on new data.

### Facilitation Tips

- **Time-box**: 60 minutes maximum. Prioritization sessions that run long produce worse decisions, not better ones.
- **Separate scoring from debating**: Score first, discuss second. If people discuss first, anchoring bias takes over.
- **Use a parking lot**: Items that spark long debates go on a parking lot list. Score them last, after simpler items calibrate the group.
- **The gut check**: After scoring, ask: "Does this ranking feel right?" If the top item feels wrong, explore why. Sometimes intuition catches what frameworks miss.

---

## Framework Comparison Table

| Framework | Speed | Rigor | Best For | Worst For |
|-----------|-------|-------|----------|-----------|
| Opportunity Score | Medium | High | Customer problems | Internal initiatives |
| ICE | Fast | Low | Quick triage | Large backlogs |
| RICE | Medium | High | Feature prioritization | Early-stage ideation |
| Eisenhower | Fast | Low | Personal tasks | Product decisions |
| Impact vs Effort | Fast | Low | Group visual triage | Detailed ranking |
| Risk vs Reward | Medium | Medium | Uncertain bets | Well-understood items |
| Kano | Slow | High | Understanding needs | Ranking priorities |
| Weighted Matrix | Slow | High | Multi-stakeholder | Quick decisions |
| MoSCoW | Fast | Medium | Release scoping | Strategic planning |

## references/red-flags.md

# Red Flags: Prioritization Frameworks

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan before sharing a prioritization output (a ranked backlog, a RICE table, an opportunity score). Each red flag has a `bad` and `good` quoted example. If your output matches a bad example, fix it before the artifact leaves your machine.

---

## Red Flag 1: Everything Scores High Impact

**Symptom.** Every item in the backlog gets Impact = 3 (massive) on the RICE scale.
**Why it's bad.** RICE is a *relative* ranking tool. If every item is "massive", you've ranked nothing -- the score collapses to Reach x Confidence / Effort, and Impact loses signal. Worse, leadership starts ignoring impact entirely because it never differentiates.
**Bad example:**
> | Item | Reach | Impact | Confidence | Effort | RICE |
> | --- | --- | --- | --- | --- | --- |
> | Dark mode | 5000 | 3 (massive) | 80% | 2 | 6000 |
> | Onboarding redesign | 4000 | 3 (massive) | 70% | 4 | 2100 |
> | Tax form export | 800 | 3 (massive) | 90% | 1 | 2160 |
**Good example:**
> | Item | Reach | Impact | Confidence | Effort | RICE |
> | --- | --- | --- | --- | --- | --- |
> | Dark mode | 5000 | 0.5 (low) | 80% | 2 | 1000 |
> | Onboarding redesign | 4000 | 2 (high) | 70% | 4 | 1400 |
> | Tax form export | 800 | 3 (massive) | 90% | 1 | 2160 |
**How to catch it.** Histogram Impact across the backlog. If more than 30% of items score "massive" (3.0), force a recalibration round: only items with documented behavioral or revenue evidence keep the 3.

---

## Red Flag 2: Confidence Padding to Hit a Target Rank

**Symptom.** A favored item's Confidence is bumped from 50% to 80% with no new evidence, just to push it above the cut line.
**Why it's bad.** Confidence is supposed to *discount* unvalidated ideas. Padding it converts RICE from a calibration tool into a rubber stamp, and the resulting plan systematically over-invests in pet projects.
**Bad example:**
> "Marketing wants Item X in the quarter. Bumped Confidence from 50% to 80% so it crosses the line. We will revisit after launch."
**Good example:**
> "Marketing wants Item X. Current Confidence is 50% because we have no usage data. Running a 2-week landing-page test next sprint to gather signal -- if click-through > 4%, Confidence moves to 80% and the item re-enters scoring."
**How to catch it.** Require a written Confidence Source column. Empty source = Confidence capped at 50%.

---

## Red Flag 3: Effort Estimated Without Engineering

**Symptom.** The PM scored Effort solo, using "small / medium / large" gut feel.
**Why it's bad.** Effort is the only denominator in RICE / ICE. Get it wrong and the entire rank flips. PMs systematically under-estimate backend, security, and migration work because they don't see it.
**Bad example:**
> "Effort: 2 person-months. (Set by PM during planning.)"
**Good example:**
> "Effort: 4 person-months. Tech-lead estimate after spike: 2.5 weeks frontend + 3 weeks backend (new event-bus integration) + 1 week QA + 2 weeks security review. Logged in `effort-estimates.md`."
**How to catch it.** Reject any score where Effort lacks an engineering co-signer.

---

## Red Flag 4: Reach Counted as TAM, Not Quarterly Touch

**Symptom.** Reach = total addressable market (millions) instead of users who will encounter the feature in the next quarter.
**Why it's bad.** RICE's Reach is "people impacted per time unit" (Intercom's original definition was "per quarter"). Using TAM makes every B2C feature dominate every B2B feature, breaking comparability.
**Bad example:**
> "Reach: 50,000,000 (all US adults could theoretically use this)."
**Good example:**
> "Reach: 8,400 active users / quarter. Source: MAU report Q1 2026, filtered to users who hit the relevant flow at least once. See `reach-source.csv`."
**How to catch it.** Reach > 5x your quarterly MAU = wrong unit. Require a data source column.

---

## Red Flag 5: ICE for 80-Item Backlogs

**Symptom.** A 75-item backlog scored with ICE on a 1-10 scale.
**Why it's bad.** ICE is meant for quick triage on small lists (< 15 items). At 75 items the noise dominates -- a 7 and an 8 are statistically indistinguishable but appear adjacent in the rank. Teams treat the order as meaningful and ship low-value work.
**Bad example:**
> "Sorted 75 items by ICE. Top 12 go in the quarter."
**Good example:**
> "ICE-triaged 75 items down to top 30 candidates. Re-scored top 30 with RICE using engineering effort estimates. Top 12 by RICE go in the quarter."
**How to catch it.** Item count > 15 + framework = ICE = re-rank top tertile with RICE.

---

## Red Flag 6: MoSCoW with No Must / Should / Could Caps

**Symptom.** 70% of items are tagged "Must" and 25% are "Should". "Could" and "Won't" are empty.
**Why it's bad.** MoSCoW's value is the forcing function -- a deliverable scope where Musts are roughly 60% of effort, Shoulds 20%, Coulds 20%. Without caps it degenerates into "everything is critical", which is just a flat list.
**Bad example:**
> "Must: 23 items. Should: 8 items. Could: 0. Won't: 0."
**Good example:**
> "Must: 8 items (~55% of capacity). Should: 5 items (~25%). Could: 6 items (~20%, drop if Musts slip). Won't (this release): 14 items, documented in `wont-this-release.md`."
**How to catch it.** Must >= 75% of items = MoSCoW abuse. Re-run with explicit capacity caps.

---

## Red Flag 7: Opportunity Score Sourced from a 12-Person Survey

**Symptom.** Opportunity scores (Importance + Unsatisfaction) calculated from a 12-respondent internal survey.
**Why it's bad.** Ulwick's Outcome-Driven Innovation requires n >= 180 to separate signal from noise (and ideally 300+ across segments). Twelve responses produce wide confidence intervals and the rank can be reshuffled by 2-3 respondents changing minds.
**Bad example:**
> "Opportunity score for 'reduce time to first invoice' = 14.2. (n = 12 internal pilot users.)"
**Good example:**
> "Opportunity score for 'reduce time to first invoice' = 14.2 (95% CI: 12.8 - 15.6). n = 247 customers, segmented by ARR band and persona. Survey instrument and raw data in `odi-q1-2026/`."
**How to catch it.** Any opportunity score without n, segmentation, and confidence interval should be marked draft and not used for prioritization.

---

## Red Flag 8: WSJF Without Job-Size Calibration

**Symptom.** WSJF (Cost of Delay / Job Size) used on a team that has never calibrated story points.
**Why it's bad.** WSJF amplifies the denominator. If Job Size estimates are noisy (which they always are in an uncalibrated team), the rank is dominated by whoever shouted "small!" loudest, not by actual value-per-effort.
**Bad example:**
> "Item A: CoD = 80, Size = 1, WSJF = 80. Item B: CoD = 200, Size = 5, WSJF = 40. Ship A first."
**Good example:**
> "Item A: CoD = 80, Size = 1 (calibrated against 6 reference stories from last quarter; 80% confidence). Item B: CoD = 200, Size = 5 (same calibration). WSJF still favors A, but flagged for review because Item B has a hard deadline -- moving to CD3 framework instead."
**How to catch it.** No reference-story calibration = WSJF is not the right framework. Use Impact x Effort 2x2 instead.

---

## Red Flag 9: Kano Model Without Recent User Research

**Symptom.** Features classified as Delighter / Performance / Must-Have based on PM intuition, not Kano survey data.
**Why it's bad.** Kano categories shift over time -- yesterday's Delighter is today's Must-Have (think: search bar, dark mode, single-sign-on). Classifying from intuition produces a snapshot of *the PM's* mental model, not the market's.
**Bad example:**
> "Two-factor auth: Delighter. Users will love that we offer it."
**Good example:**
> "Two-factor auth: Must-Have for enterprise segment, Performance for SMB. Source: Kano survey Q4 2025 (n=412, both functional + dysfunctional questions). 78% of enterprise respondents in 'I expect it' band; SMB split 45 / 40."
**How to catch it.** Kano classification without a survey reference is fan-fiction.

---

## Red Flag 10: No Tie-Breaker Rule for Identical Scores

**Symptom.** Three items tied at RICE = 1400, no documented rule for picking which goes first.
**Why it's bad.** Ties get resolved by hallway politics. The most senior voice picks the winner, and the prioritization process loses credibility ("they were going to pick that one anyway").
**Bad example:**
> "Items A, B, C all scored 1400. Picked A because it was easiest to start."
**Good example:**
> "Items A, B, C all scored 1400. Tie-breaker rule (from `prioritization-charter.md`): strategic theme alignment first, then customer commitments, then team dependencies. A and B align to 'Activation' theme; B has a Q1 customer commitment. Picked B."
**How to catch it.** Identical scores without a documented tie-breaker = bring the charter, not the loudest voice.

---

## Red Flag 11: Mixing Frameworks Without Explanation

**Symptom.** Backlog spreadsheet has RICE for half the items, ICE for others, and MoSCoW tags on the rest -- combined into a single rank.
**Why it's bad.** Different frameworks produce different score distributions. Mixing them is like ranking athletes by combining marathon times with weightlifting kilos. The result looks rigorous but is meaningless.
**Bad example:**
> "Top of the backlog: RICE = 2400. Next item: ICE = 9. Next: MoSCoW = Must. Sorted by 'priority score'."
**Good example:**
> "Backlog split into three buckets: opportunities (ranked by Opportunity Score, n=247), features (ranked by RICE), and constraints (ranked by MoSCoW). Quarterly slate pulls top items from each bucket according to capacity rules in `prioritization-charter.md`."
**How to catch it.** A single sort column that mixes framework outputs is always wrong.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Everything is Impact = massive | Histogram Impact; >30% massive triggers recalibration |
| 2 | Confidence padding | Require a Confidence Source column |
| 3 | Effort estimated solo | Reject scores without engineering co-signer |
| 4 | Reach = TAM | Reach > 5x quarterly MAU = wrong unit |
| 5 | ICE for big backlogs | >15 items + ICE = re-rank top tertile with RICE |
| 6 | MoSCoW with no caps | Must >= 75% of items = abuse |
| 7 | Opportunity score, n=12 | Require n, segmentation, confidence interval |
| 8 | WSJF, no calibration | No reference-story calibration = use 2x2 instead |
| 9 | Kano from intuition | No survey reference = fan-fiction |
| 10 | Ties resolved by politics | Document a tie-breaker rule in charter |
| 11 | Mixed framework rank | Single sort column mixing outputs = always wrong |

## Related Reading

- `SKILL.md` -- framework decision tree (which framework when)
- `references/frameworks.md` -- the 9 frameworks with worked examples
- `scripts/prioritization_scorer.py --help` -- the scoring tool
- Sibling skill: `execution/backlog-refinement/` -- INVEST / DoR / DoD
- Sibling skill: `discovery/identify-assumptions/` -- before scoring, validate the assumption

## references/tool-and-troubleshooting.md

# Tool Reference, Troubleshooting & Success Criteria

Read this when running `prioritization_scorer.py` (input schemas, flags), diagnosing a scoring problem, or checking whether a prioritization exercise met its bar.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| RICE scores dominated by high-reach items regardless of impact | Reach values vary by orders of magnitude, drowning out other factors | Normalize reach to a consistent time window (e.g., users per quarter); consider log-scale for extreme ranges |
| ICE scores feel arbitrary and inconsistent across raters | No calibration on 1-10 scale definitions; different people use different anchors | Define what 1, 5, and 10 mean for each dimension; score independently first, then discuss outliers |
| MoSCoW results in 80% Must-Haves | Team reluctant to deprioritize anything, or no effort constraint applied | Enforce the rule: Must-Haves should be no more than 60% of total effort; make the constraint visible |
| Opportunity Score returns 0 for satisfied needs | Satisfaction scored at 1.0 (fully satisfied), zeroing out the score | Verify satisfaction is on 0-1 scale; values above 1 are auto-converted from 0-10 scale |
| Weighted Decision Matrix produces tied scores | Criteria weights are too evenly distributed, or scoring lacks variance | Increase weight differentiation; force-rank criteria by importance; use the full 1-10 scoring range |
| Framework selection is itself a bottleneck | Team spends time debating which framework to use instead of scoring | Use the Decision Tree in this skill; default to RICE for 15+ items with data, ICE for quick sorts under 15 items |
| Stakeholders disagree with prioritization results | Framework selected does not match stakeholder values, or inputs not transparent | Use Weighted Decision Matrix when multiple stakeholder groups are involved; agree on criteria and weights before scoring |

## Success Criteria

- Prioritization framework selected using the Decision Tree, not by habit or preference
- All items scored with consistent definitions for each dimension (documented before scoring begins)
- Results reviewed and discussed as a team, not treated as a mechanical ranking
- Top-priority items have clear next steps (assigned to sprints, PRDs, or experiments)
- Prioritization is repeated at least quarterly, or when significant new information arrives
- The two-step approach is followed: prioritize problems first (Opportunity Score), then prioritize solutions (RICE/ICE)
- MoSCoW Must-Haves never exceed 60% of total effort for a release

## Tool Reference

### prioritization_scorer.py

Scores and ranks items using 5 supported prioritization frameworks. Outputs sorted results with scores, formulas, and category breakdowns.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input` | string | (required, mutually exclusive with --demo) | Path to JSON file containing items to score |
| `--demo` | flag | off | Run scoring on built-in demo data for the selected framework |
| `--framework` | choice | (required) | Framework to use: `rice`, `ice`, `opportunity`, `moscow`, `weighted` |
| `--format` | choice | `text` | Output format: `text` or `json` |

**Input JSON schema by framework:**

- **RICE:** `{"items": [{"name": "...", "reach": N, "impact": N, "confidence": N, "effort": N}]}`
- **ICE:** `{"items": [{"name": "...", "impact": N, "confidence": N, "ease": N}]}`
- **Opportunity:** `{"items": [{"name": "...", "importance": N, "satisfaction": N}]}`
- **MoSCoW:** `{"items": [{"name": "...", "category": "must|should|could|wont", "effort": N}]}`
- **Weighted:** `{"items": [{"name": "...", "scores": {"criterion": N}}], "criteria": [{"name": "...", "weight": N}]}`

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/prioritization-frameworks -->
