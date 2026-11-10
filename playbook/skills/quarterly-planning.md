# quarterly-planning

> **Use these instructions for this whole conversation.** Apply them when: Run the meetings around a quarter's OKRs: homework and kickoff, weekly check-ins, the week-6 carry/kill/pivot review and the close retro. Use when running any phase of that cadence; writing the OKRs is brainstorm-okrs.

# Quarterly Planning Expert

## Overview

Quarterly planning is the operating cadence that turns annual strategy into quarterly outcomes. Done well, it produces aligned OKRs, a roadmap that delivers them, a capacity plan that respects reality, and a tracking ritual that catches drift before it compounds. Done poorly, it produces OKR theater -- a slide deck of objectives that nobody references after week two.

This skill is the **above-OKR-writing** companion to `execution/brainstorm-okrs/`. Where `brainstorm-okrs/` covers how to write good OKRs, this skill covers the full quarterly cycle around them: pre-quarter homework, kickoff agenda, mid-quarter check-in, close-of-quarter retro, and the weekly/biweekly tracking cadence. Each meeting uses a Reflect-Align-Decide agenda; the theory behind the rhythm is in `references/quarterly-planning-guide.md`.

## Core Capabilities

- **Pre-quarter homework** -- strategy review, outcome candidate list, capacity assessment, and the 1-page kickoff brief
- **Kickoff facilitation** -- the 2-3hr RAD agenda that commits OKRs, roadmap, and capacity
- **Weekly Wodtke rhythm** -- Monday Commit, Friday Celebrate, biweekly KR confidence review
- **Mid-quarter check-in** -- carry / kill / pivot / escalate decisions at week 6
- **Close retro** -- 0.0-1.0 OKR scoring, learning extraction, and next-cycle seeding

## Clarify First

Before running a phase, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Which phase:** pre-quarter/kickoff vs mid-quarter check-in vs close retro (selects the agenda and artifacts produced).
- **Position in the 13-week cycle:** what week you're in (the carry/kill/pivot check belongs at ~week 6, the retro at week 13).
- **Existing OKRs & strategy:** the committed Objective and the annual strategy it serves (the kickoff commits OKRs; every Objective must trace to a vision pillar).
- **Real team capacity:** honest capacity after PTO/on-call (a stretch slate dressed as commitments is the #1 cadence failure).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

Pick the phase from where the team is in the 13-week cycle, then run that phase's agenda from `references/cycle-playbook.md`.

| Phase | When | Output | Done when |
|---|---|---|---|
| Pre-quarter homework | Weeks -3 to -1 | 1-page kickoff brief: strategy recap, outcome candidates, real capacity | Every candidate Objective traces to a strategy pillar; capacity is in hours after PTO and on-call |
| Kickoff | Week 0 | Committed OKRs, roadmap slice, capacity plan | Commitments fit capacity; stretch is labelled as stretch |
| Weekly rhythm | Weeks 1-12 | Monday commitments, Friday wins, KR confidence every two weeks | Confidence is recorded for every KR, not just the green ones |
| Mid-quarter check-in | About week 6 | Carry / kill / pivot / escalate per KR | Each KR has a decision and an owner; anything rebaselined says why |
| Close retro | Week 13 | KR scores (0.0-1.0), lessons, seeds for next quarter | Each miss has a cause, and next quarter's homework starts from it |

Week 6 is the default for the check-in [RECOMMENDED] because it leaves enough quarter to act on a kill or pivot; move it earlier for six-week cycles.

## When to Use

- **Any phase of the quarter** listed in the Workflow table.
- **New PM joining mid-quarter.** Understand where the team is in the cycle and what is expected when.
- **Failing OKR cadence.** Team has OKRs but no one references them by week 4 -- reset the ritual.

## Anti-Patterns

### Key results that are activities
**Mistake:** "KR: launch the new pricing page by June 1." The KR is a deliverable.
**Why it happens:** Deliverables are easy to plan and score, and shipping feels like success.
**Instead:** Rewrite each KR as a measurable change, for example "free-to-paid conversion >= 4.5% by June 30", and treat the deliverable as the bet behind it. A KR built on ship, launch, build or complete with no downstream metric needs a rewrite.

### Dependencies found mid-quarter
**Mistake:** In week 6, Team A discovers it needs an API that Team B never put in its slate.
**Why it happens:** Each team plans its own slate, and the cross-team check feels like extra overhead.
**Instead:** Before kickoff, have every team list its initiatives and dependencies. Run a reconciliation session in week 0, and cut scope where the other team can't commit. No documented week-0 session means mid-quarter surprises.

### A mid-quarter check-in with no authority to rebaseline
**Mistake:** The week-6 check-in finds KR2 off-track, and the answer is "push harder".
**Why it happens:** Descoping feels like admitting failure, so nobody is given the authority.
**Instead:** Bring carry, kill, pivot and escalate options to the check-in, such as descope the KR, borrow capacity, or drop another KR. Record the decision and who signed off. A check-in with no rebaseline decisions was a status meeting.

Eight more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task -- keep this file lean and pull detail on demand:

- **[references/cycle-playbook.md](references/cycle-playbook.md)** -- the full operational playbook: pre-quarter homework + kickoff brief template, kickoff / mid-quarter / close agendas, the weekly Wodtke rhythm scripts, anti-patterns, artifacts-produced map, troubleshooting, and success criteria. Read this when running any phase of the cycle.
- **[references/quarterly-planning-guide.md](references/quarterly-planning-guide.md)** -- the framework theory (Wodtke Radical Focus, Cagan product strategy, strategy cycle, RAD ritual) with a worked Reconcile Q3 example. Read this when you need the reasoning behind the rituals.
- **[references/red-flags.md](references/red-flags.md)** -- 11 quarterly-planning anti-patterns (OKR theater, capacity in story points, stretch goals as committed slate) with symptoms and fixes. Read this when reviewing a quarter's plan or diagnosing a failing cadence.


## Files

| File | Purpose |
|---|---|
| `assets/kickoff_agenda_template.md` | Kickoff agenda |
| `assets/mid_quarter_check_in_template.md` | Week-6 check-in |
| `assets/close_retro_template.md` | Close retro |
| `assets/quarterly_review_deck_outline.md` | Quarterly review deck outline |
| `examples/northwind-q4-planning-cycle.md` | Worked cycle |

## Scope & Limitations

**In scope:** pre-quarter homework (strategy, outcomes, capacity); kickoff agenda; weekly Wodtke rhythm; biweekly KR confidence review; mid-quarter check-in; close retro; carry/kill/pivot framework; quarterly review deck outline.

**Out of scope:** writing individual OKRs (`execution/brainstorm-okrs/`); roadmap construction (`execution/outcome-roadmap/`); sprint-level planning (`scrum-master/`); multi-quarter / annual strategy (`c-level-advisor/`); performance management (`career/`); portfolio management (`program-manager/`).

**Caveats:** the cycle is the system -- skipping one ritual (especially the close retro) degrades the next quarter; OKRs are a tool for focus, not control (Wodtke argues one Objective per team per quarter); the skill assumes a 13-week quarter; it works best where the company has shared OKR practice.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `execution/brainstorm-okrs/` | Bidirectional | Quarterly cycle uses OKRs; OKR drafting is a kickoff sub-skill |
| `execution/outcome-roadmap/` | Bidirectional | Quarterly OKRs become Now-horizon roadmap; roadmap themes inform candidate outcomes |
| `execution/north-star-metric/` | Receives from | NSM is the long-term metric; quarterly KRs are short-term moves on it |
| `execution/product-vision/` | Receives from | Every Objective must trace to a vision pillar |
| `execution/dependency-map/` | Receives from | Pre-quarter dependency mapping prevents week-6 surprises |
| `execution/status-update-generator/` | Feeds into | Weekly Wodtke rhythm produces input for exec status updates |
| `execution/cycle-time-analyzer/` | Receives from | Flow metrics inform capacity assessment |
| `discovery/customer-interview-script/` | Receives from | Recent customer signal feeds the strategy review |
| `discovery/jtbd-workshop/` | Receives from | Top desired outcomes seed the outcome candidate list |
| `scrum-master/` | Feeds into | Quarterly OKRs cascade into sprint capacity planning |
| `senior-pm/` | Feeds into | Quarterly artifacts inform portfolio-level reporting |
| `career/pm-onboarding/` | Complementary | New PMs use this skill in their 30-60-90 plan to ramp on team cadence |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/cycle-playbook.md

# Quarterly Planning Cycle Playbook

Read this when you are running any phase of the quarterly cycle and need the detailed pre-quarter homework structure, the kickoff / mid-quarter / close meeting agendas, the weekly Wodtke rhythm scripts, the anti-pattern and troubleshooting tables, the artifacts-produced map, or the success criteria. `quarterly-planning-guide.md` carries the framework theory (Wodtke, Cagan, strategy cycle, RAD) with worked examples.

## The Quarterly Cycle

```
Week -3      -2       -1       0        1-5      6        7-12     13
  |          |        |        |         |       |         |        |
  |   Pre-quarter     |     Kickoff      |   Mid-quarter   |     Close
  |   homework        |     (start)      |   check-in      |     retro
  |                   |                  |                 |
  +--Strategy / Cagan-+--- Wodtke weekly Mon/Fri rhythm ---+
```

### Pre-Quarter Homework (Weeks -3 to -1)

Three workstreams happen in parallel before the kickoff:

1. **Strategy review.** Is the team's strategy still right? (Cagan's product strategy review)
2. **Outcome candidate list.** What outcomes could the team commit to? (Pulled from `discovery/jtbd-workshop/`, `execution/north-star-metric/`, `execution/outcome-roadmap/`)
3. **Capacity assessment.** What is the team actually capable of delivering? (Headcount, capacity, dependencies, on-call rotation)

Output: a 1-page kickoff brief delivered 48 hours before the kickoff meeting.

### Kickoff Meeting (Week 0)

The 2-3 hour meeting that commits the quarter's OKRs, roadmap, and capacity plan. Run as a RAD session (Reflect-Align-Decide).

### Tracking Cadence (Weeks 1-12)

The Wodtke weekly rhythm:

- **Monday Commit.** 15-30 min team huddle. Each person commits to what will move the OKR this week.
- **Friday Celebrate.** 30 min team huddle. Wins, learning, blockers.

Plus a biweekly review of confidence levels on each Key Result (1-10 scale).

### Mid-Quarter Check-in (Week 6)

The 90-minute meeting that course-corrects. Review confidence, kill or carry over, address dependencies.

### Close-of-Quarter Retro (Week 13)

The 90-minute meeting that scores the OKRs (0-1.0), extracts learning, and feeds the next quarter's pre-work.

## Pre-Quarter Homework

The homework is the difference between OKR-as-aspiration and OKR-as-commitment. Skip the homework and the kickoff becomes a brainstorm rather than a commit.

### Workstream 1: Strategy Review

Owner: PM (with EM and Design Lead)

Output: A 1-page "is our strategy still right?" memo.

Questions:

- **Vision check.** Does the current vision still hold? (Use `execution/product-vision/`'s Vision Review Checklist)
- **NSM check.** Is the North Star Metric still the right one? (See `execution/north-star-metric/`)
- **Customer signal.** What has changed in the customer's world in the last quarter? (Pull from `discovery/customer-interview-script/` recent sessions)
- **Competitive signal.** What competitor moves are worth responding to?
- **Operational signal.** What has changed inside the team or company (org changes, budget shifts, exec mandates)?

If any of these has materially shifted, the strategy review escalates to a *strategy reset* before kickoff -- which may require more than one kickoff meeting.

### Workstream 2: Outcome Candidate List

Owner: PM

Output: A list of 5-10 candidate outcomes, each scored for impact and feasibility.

Sources:

- Top desired outcomes from the last `discovery/jtbd-workshop/`
- Themes in the outcome roadmap (`execution/outcome-roadmap/`)
- Open bets carried from prior quarter
- Customer-feedback opportunities surfaced in `discovery/interview-synthesis/`
- Reactive items (incidents, SLA misses, churn drivers) -- these are necessary but should not crowd the list

For each candidate, capture:

- The outcome statement (in Ulwick format from `discovery/jtbd-workshop/`)
- The hypothesis: "If we [X], then [outcome] will improve from [Y] to [Z]"
- Confidence (1-10) -- how confident are we in the hypothesis?
- Effort estimate (S/M/L/XL)

### Workstream 3: Capacity Assessment

Owner: EM (with PM)

Output: A capacity plan in person-weeks.

Account for:

- Headcount at start and end of quarter (planned hires, planned departures)
- Holidays, PTO commitments
- On-call rotation overhead
- Maintenance and support load (typically 20-30%)
- Cross-team dependencies (`execution/dependency-map/`)
- Reserve for unplanned work (typically 15-20%)

Output: "We have X person-weeks of productive capacity for new work."

### The Kickoff Brief

48 hours before kickoff, the PM circulates a 1-page brief:

```markdown
# Q[X] [Year] Kickoff Brief

**Team:** [...]
**Strategy status:** Unchanged / Updated / Reset (see attached memo)
**Vision link:** [link]
**Last quarter's score:** [average OKR score 0-1.0]

## Candidate Outcomes (5-10)

| # | Outcome | Hypothesis | Confidence | Effort |
|---|---------|-----------|------------|--------|
| 1 | [...] | [...] | 7 | M |
| ... | ... | ... | ... | ... |

## Capacity

- Total person-weeks: [X]
- Reserved (maintenance, on-call, unplanned): [Y]
- Available for new work: [X-Y]

## Carry-overs from last quarter

| # | Item | Why incomplete | Recommendation |
|---|------|----------------|-----------------|
| 1 | [...] | [...] | Kill / Carry / Restart |

## Open questions for the kickoff

- [Decision needed 1]
- [Decision needed 2]
- [Decision needed 3]
```

## Kickoff Meeting Agenda (Week 0)

**Length:** 2-3 hours (or 2 x 90 min)
**Participants:** PM, EM, Design Lead, +/- exec sponsor, +/- key cross-functional partners
**Format:** RAD (Reflect-Align-Decide)
**Materials:** Kickoff brief; whiteboard or shared doc

### 0:00 - 0:15 | Reflect: Last Quarter (15 min)

- Quick review of last quarter's OKR scores
- Top 2 learnings from the close retro
- Carry-overs: any items the team has agreed to continue?

### 0:15 - 0:45 | Align: Strategy Context (30 min)

- Strategy review memo: still valid? changes needed?
- Vision sanity check: still inspiring? Roadmap items must trace to it.
- NSM context: where do we stand? what trend are we trying to move?
- Top customer/competitive signals from pre-work

### 0:45 - 1:15 | Reflect: Candidate Outcomes Review (30 min)

- PM walks through the 5-10 candidate outcomes
- For each: hypothesis, confidence, effort
- Open Q&A and challenge

### 1:15 - 1:30 | Break (15 min)

### 1:30 - 2:15 | Decide: Commit to OKRs (45 min)

- Vote on 1-3 Objectives (Wodtke: prefer 1)
- For each Objective: 3-5 Key Results
- Each Key Result has a baseline, target, and owner
- Apply the `execution/brainstorm-okrs/` SMART validation

### 2:15 - 2:45 | Decide: Roadmap and Capacity (30 min)

- Map committed OKRs to the roadmap (Now / Next / Later)
- Confirm capacity covers commitments (with reserve)
- Identify and assign cross-team dependencies

### 2:45 - 3:00 | Decide: Tracking Cadence (15 min)

- Confirm Monday Commit / Friday Celebrate is on calendars
- Confirm biweekly KR-confidence review on calendars
- Set the mid-quarter check-in date (week 6)
- Set the close retro date (week 13)
- Assign artifact owners (OKR doc, roadmap doc, capacity plan)

## The Weekly Wodtke Rhythm

Christina Wodtke's *Radical Focus* defines a weekly rhythm that converts OKRs from posters into commitments.

### Monday Commit (15-30 min)

Format:

```text
Each team member shares:
- One thing they will do this week to advance the OKR
- Confidence level on the top KR (1-10)
- Help they need
```

The Monday Commit is not a status meeting. It is a *forward-looking* meeting -- what will happen this week, not what happened last week.

### Friday Celebrate (30 min)

Format:

```text
Each team member shares:
- One win from the week
- One thing they learned
- One blocker they could not resolve
```

The Friday Celebrate is *retrospective* -- reflecting on the week. The celebration of wins, even small ones, is the cultural mechanism that keeps the team energized through a long quarter.

### Biweekly KR Confidence Review (15 min)

Every two weeks, the team reviews each Key Result and assigns a confidence (1-10).

```text
KR1: NPS from 32 to 45 by Q[X] end. Confidence: [1-10]
KR2: Activation rate from 28% to 40%. Confidence: [1-10]
```

If confidence drops below 5 for 2+ consecutive reviews, escalate to the mid-quarter check-in (or earlier).

## Mid-Quarter Check-in Agenda (Week 6)

**Length:** 90 minutes
**Participants:** Same as kickoff
**Goal:** Course-correct -- carry, kill, or escalate

### 0:00 - 0:15 | Where are we? (15 min)

- Quick walk through each KR with current data and confidence score
- Visual: target line vs. actual progress

### 0:15 - 0:45 | What is working? (30 min)

- For each KR scoring >= 6: what is driving the progress? Can we double down?
- Wins to scale across the team

### 0:45 - 1:15 | What is not working? (30 min)

- For each KR scoring <= 5: what is the bottleneck?
- Decision per KR:
  - **Carry:** Keep going; add resources or unblock dependencies
  - **Kill:** Drop the KR; the hypothesis was wrong
  - **Pivot:** Reframe the KR with what we have learned
  - **Escalate:** Decision needs an exec or cross-team owner

### 1:15 - 1:30 | Adjust roadmap and capacity (15 min)

- Killed KRs free up capacity -- where does it go?
- Pivoted KRs may need new roadmap items
- Update the OKR doc with the changes (versioned, not overwritten)

## Close-of-Quarter Retro Agenda (Week 13)

**Length:** 90 minutes
**Participants:** Same as kickoff
**Goal:** Score the OKRs, extract learning, set up next quarter's pre-work

### 0:00 - 0:30 | Score the OKRs (30 min)

For each KR, score 0.0 to 1.0:

| Score | Interpretation |
|-------|----------------|
| 0.0 - 0.3 | Failed to move; hypothesis or execution was wrong |
| 0.4 - 0.6 | Partial progress; learn from what worked and what did not |
| 0.7 - 0.9 | Strong outcome (Wodtke's target zone) |
| 1.0 | Maximum success -- if this is too easy to achieve, KR was sandbagged |

Wodtke's heuristic: average team OKR scores in the 0.6-0.7 range over the long run indicate appropriately ambitious goals. Consistent 1.0 scores indicate sandbagging.

### 0:30 - 1:00 | What did we learn? (30 min)

Each participant shares:

- One lesson about the customer
- One lesson about the product
- One lesson about the team / process

Capture into a shared learning doc.

### 1:00 - 1:30 | What carries to next quarter? (30 min)

- Which incomplete KRs deserve to continue? Why?
- Which should be killed? (More important than which should continue)
- Which new opportunities have emerged from the quarter's learning?
- Pre-quarter homework assignments for next cycle

## Anti-Patterns

| Anti-pattern | Symptom | Fix |
|--------------|---------|-----|
| **OKR theater** | OKRs written for the deck, never referenced after week 2 | Enforce Monday Commit + Friday Celebrate; biweekly KR review |
| **Sandbagging** | Team consistently scores 1.0 on every KR | Wodtke 0.6-0.7 heuristic; in retro, ask "should the target have been higher?" |
| **Scope creep** | New work added mid-quarter without removing existing work | Mid-quarter check-in formalizes carry/kill/pivot decisions |
| **No carry-over discipline** | Items from Q1 quietly continue into Q2 without re-commit | Carry-over decisions are explicit and require re-commitment |
| **Capacity ignored** | Team commits to more than capacity allows | EM-owned capacity plan; reserve 15-20% for unplanned |
| **No customer signal in planning** | Kickoff is internally-driven; no recent customer insight | Pre-quarter homework includes customer signal from `discovery/customer-interview-script/` |
| **OKRs disconnected from vision** | Team's Q3 OKRs don't trace to the long-term direction | Each Objective references a vision pillar; if it doesn't, ask why |
| **Cross-team dependencies surprise late** | Dependencies discovered in week 6 instead of week 0 | Pre-quarter dependency mapping (`execution/dependency-map/`) |
| **Retro skipped** | Quarter ends without a retro; learning lost | Schedule the retro at kickoff (week 13 date); never let it slip |

## Workflow

1. **Three weeks before quarter start:** Open the pre-work. PM kicks off strategy review, outcome candidate list, capacity assessment.
2. **Two days before kickoff:** Circulate the kickoff brief to all participants.
3. **Week 0:** Run the 2-3 hour kickoff meeting. Commit OKRs, roadmap, capacity, cadence.
4. **Weeks 1-12:** Run Monday Commit / Friday Celebrate / biweekly KR review consistently. Do not skip.
5. **Week 6:** Run the mid-quarter check-in. Make carry/kill/pivot/escalate decisions explicitly.
6. **Week 13:** Run the close retro. Score OKRs, extract learning, set up next quarter's pre-work.
7. **Document everything.** OKR scores, lessons, carry-overs into the team wiki. The history is more valuable than the deck.
8. **Repeat.** The cycle is not optional. It is the operating system.

## Tools and Artifacts Produced

| Artifact | Owner | Cadence | Stored Where |
|----------|-------|---------|---------------|
| Strategy review memo | PM | Quarterly (pre-work) | Wiki / `documentation/delivery/` |
| Outcome candidate list | PM | Quarterly (pre-work) | Shared doc |
| Capacity plan | EM | Quarterly (pre-work) | Shared doc |
| Kickoff brief | PM | Quarterly (pre-kickoff) | Email + wiki |
| Committed OKRs | PM | Quarterly | OKR doc (versioned) |
| Roadmap (Now/Next/Later) | PM | Quarterly + updates | Roadmap tool (`execution/outcome-roadmap/`) |
| KR confidence log | PM | Biweekly | OKR doc |
| Mid-quarter check-in notes | PM | Once per quarter | Wiki |
| Close retro notes | PM | Once per quarter | Wiki |
| Quarterly review deck | PM | Once per quarter | Slides |

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| OKRs are never referenced after kickoff | Weekly rhythm not enforced; Monday Commit absent | Calendar lock Monday Commit + Friday Celebrate; tie KR confidence to biweekly review |
| Team consistently overcommits | Capacity assessment skipped or aspirational | EM-owned capacity plan; reserve 15-20% for unplanned; mid-quarter check-in adjusts |
| Mid-quarter check-in becomes a status update | No carry/kill/pivot decisions made | Force a decision per KR scoring <= 5; document the decision in the OKR log |
| Close retro skipped or rushed | Calendar pressure; perceived low value | Schedule retro at kickoff; treat it as the highest-leverage 90 min of the cycle |
| OKRs disconnect from vision | Quarterly planning becomes self-contained | Each Objective must cite a vision pillar in the OKR doc |
| Sandbagged KRs (every KR hits 1.0) | Targets set to ensure success, not stretch | In retro, ask "should the target have been higher?"; aim for 0.6-0.7 average over time |
| Cross-team dependencies surprise late | Dependencies not mapped during pre-work | Use `execution/dependency-map/` during pre-work; circulate dependency commitments before kickoff |
| Team morale drops mid-quarter | Friday Celebrate dropped; no recognition rhythm | Reinstate the celebrate ritual even if wins are small; energy compounds |

## Success Criteria

- Pre-quarter homework completed and kickoff brief circulated 48 hours before kickoff
- Kickoff produces 1-3 Objectives with 3-5 KRs each; every KR has baseline, target, owner
- Capacity plan covers committed work with 15-20% reserve
- Monday Commit + Friday Celebrate held every week (>= 90% attendance)
- Biweekly KR confidence review held without exception
- Mid-quarter check-in produces explicit carry/kill/pivot/escalate decisions
- Close retro scores every KR (0.0-1.0) and extracts >= 3 documented learnings
- Average team OKR score in the 0.6-0.7 range over multiple quarters
- Every Objective traces to a vision pillar

## references/quarterly-planning-guide.md

# Quarterly Planning Guide

A reference for the quarterly planning cycle. Combines Wodtke's *Radical Focus* (the weekly rhythm), Cagan's product strategy cycle (the strategic context), a product strategy cycle (the upstream choices), and the RAD ritual (Reflect-Align-Decide, the meeting format).

---

## 1. Why quarterly planning exists

The quarter is the natural cadence of product work. Sprints are too short to deliver outcomes; annual planning is too coarse to course-correct. A 13-week quarter is long enough to ship something meaningful and short enough to commit to with confidence.

Most teams have OKRs but lack the surrounding ritual. The OKR doc is written in week 0 and ignored until week 12. The result is "OKR theater" -- aspirational targets disconnected from actual work.

The cure is not better OKRs. The cure is a *cycle* -- pre-work, kickoff, weekly rhythm, mid-quarter check-in, close retro -- with each ritual reinforcing the others.

---

## 2. Christina Wodtke: Radical Focus

Wodtke's *Radical Focus* (2016) is the canonical text for OKR practice in startups and product teams. Three core ideas:

### 2.1 One Objective per quarter

Wodtke argues that focus is the rare resource. A team with 5 Objectives has 0 priorities. The discipline of choosing *one* Objective is uncomfortable but transformative.

In practice, most teams flex to 1-3 Objectives. Going beyond 3 is a warning sign.

### 2.2 Monday Commit / Friday Celebrate

The weekly rhythm is the operating system:

- **Monday Commit (15-30 min):** What will I do this week to advance the OKR? Confidence on the top KR (1-10).
- **Friday Celebrate (30 min):** Wins, learning, blockers from the week.

The Monday Commit is forward-looking ("what will happen"); the Friday Celebrate is retrospective ("what happened"). Both are essential.

Wodtke's insight: celebrating small wins is the cultural mechanism that sustains energy through a 13-week quarter. Teams that drop the celebration ritual see morale decay around week 8.

### 2.3 The 0.6-0.7 scoring target

OKRs are scored 0.0 to 1.0 at the end of the quarter. Wodtke's heuristic: average team scores in the 0.6-0.7 range indicate appropriately ambitious goals.

- Consistent 1.0 scores: sandbagging (targets too easy)
- Consistent 0.3 scores: targets too aggressive (or execution misaligned)
- 0.6-0.7 average: the team is reaching, sometimes missing, sometimes exceeding -- the right zone

This is a long-run average, not a per-quarter target. A team will have a 1.0 quarter and a 0.4 quarter; what matters is the trend over 4-6 quarters.

---

## 3. Marty Cagan: Product Strategy and Quarterly Bets

Cagan (in *Inspired* and *Empowered*) places quarterly planning inside a larger product strategy cycle:

```
Vision (10 years)
  |
  V
Product Strategy (2-3 years)
  |
  V
Quarterly Bets (13 weeks)  <-- this skill lives here
  |
  V
Roadmap (quarterly + ongoing)
  |
  V
Discovery + Delivery (continuous)
```

Cagan's argument: each layer must connect to the one above and below. A quarterly bet that does not trace to product strategy is opportunistic. A roadmap item that does not advance a quarterly bet is noise.

### Quarterly bets as forcing functions

Cagan calls quarterly OKRs *bets*. A bet is a hypothesis the team is willing to invest a quarter to test. The bet language reframes OKRs from "things we will do" to "hypotheses we will test" -- which changes the conversation.

When a bet does not work out (a KR scores 0.3), the framing is "we learned this hypothesis was wrong" rather than "we failed." This is the cultural shift that prevents sandbagging.

### Strategy review before quarterly planning

Cagan emphasizes that quarterly planning *starts* with a strategy review. Before committing OKRs for the next quarter, the team confirms:

- The vision is still right
- The product strategy is still right
- The customer signal supports the current direction
- No major shifts (competitive, regulatory, operational) require a re-think

If any of these has shifted, the quarter starts with strategy revision -- not just OKR writing.

---

## 4. The Product Strategy Cycle

A product strategy cycle frames quarterly planning as one node in a continuous strategy cycle:

```
Inputs:                    Process:               Outputs:
- Customer signal     -->  Strategy choices  -->  - Updated strategy doc
- Competitive signal       (build/buy,             - OKRs
- Market signal            grow/retain,            - Roadmap
- Operational signal       segment focus)          - Capacity plan
                                                   - Decision log
```

Quarterly planning is when the team makes (or re-confirms) the strategy choices. Between quarters, the team executes; at the quarter boundary, it re-examines.

### Strategy choices to make explicit

Name the strategy choices, not just the OKRs:

- **Build vs. buy vs. partner.** For each major capability, what is the path?
- **Grow vs. retain.** Where is the team investing -- new logo acquisition or existing-customer expansion?
- **Segment focus.** Which customer segments get priority? Which are deprioritized?
- **Risk posture.** Are we taking aggressive bets or safe bets this quarter?

These choices are upstream of the OKRs. Two teams with the same OKR ("grow MRR by 15%") may make completely different strategy choices to get there.

---

## 5. The RAD Ritual: Reflect-Align-Decide

The RAD format is the meeting structure used inside the kickoff, mid-quarter check-in, and close retro. It is a 3-step format:

### Reflect

Look back. What did we learn? What is the current state? What signals are coming in?

Time allocation: 20-30% of the meeting.

### Align

Discuss. What do these signals mean? Where do we agree? Where do we disagree?

Time allocation: 30-40% of the meeting.

### Decide

Commit. What are we doing? Who owns what? When do we revisit?

Time allocation: 30-40% of the meeting.

The RAD format prevents two common meeting failures:

- **Pure Reflect (status updates with no decision):** Time is spent re-stating what everyone already knows. No decisions made.
- **Pure Decide (decisions without reflection):** Decisions made without grounding in evidence. Often reversed.

A well-run RAD meeting moves through all three steps in order, with clear time-boxes per step.

---

## 6. Detailed cycle: pre-quarter through close

### Pre-Quarter (Weeks -3 to -1)

Three workstreams run in parallel:

#### Workstream 1: Strategy Review (PM owns)

Output: A 1-page memo answering "is our strategy still right?"

Questions to address:
- Vision check (`execution/product-vision/` Vision Review Checklist)
- NSM check (`execution/north-star-metric/`)
- Customer signal (recent interviews, synthesis themes)
- Competitive signal
- Operational signal (org changes, budget, exec mandates)

If any answer triggers a re-think, escalate to a strategy reset (may require additional kickoff time).

#### Workstream 2: Outcome Candidate List (PM owns)

Output: 5-10 candidate outcomes, each scored.

Sources:
- `discovery/jtbd-workshop/` top desired outcomes
- `execution/outcome-roadmap/` themes
- Carry-overs from prior quarter
- `discovery/interview-synthesis/` opportunities
- Reactive items (incidents, churn drivers, SLA misses)

For each candidate:
- Outcome statement (Ulwick format)
- Hypothesis ("If we X, then [outcome] improves from Y to Z")
- Confidence (1-10)
- Effort estimate (S/M/L/XL)

#### Workstream 3: Capacity Assessment (EM owns)

Output: "We have X person-weeks of productive capacity for new work."

Account for:
- Headcount transitions (planned hires, departures)
- Holidays, PTO
- On-call rotation overhead
- Maintenance and support (20-30% typical)
- Cross-team dependencies (`execution/dependency-map/`)
- Reserve for unplanned work (15-20%)

#### Kickoff Brief

48 hours before kickoff, PM circulates a 1-page brief combining all three workstreams (template in `assets/`).

### Kickoff Meeting (Week 0)

RAD-format meeting, 2-3 hours.

| Phase | Block | Time |
|-------|-------|------|
| Reflect | Last quarter's scores and learnings | 15 min |
| Align | Strategy context (vision, NSM, signals) | 30 min |
| Reflect | Candidate outcomes walk-through | 30 min |
| (Break) | | 15 min |
| Decide | Commit to OKRs (1-3 Objectives) | 45 min |
| Decide | Roadmap + capacity | 30 min |
| Decide | Tracking cadence + meeting dates | 15 min |

### Weekly Rhythm (Weeks 1-12)

- **Monday Commit:** 15-30 min, full team
- **Friday Celebrate:** 30 min, full team
- **Biweekly KR Confidence Review:** 15 min embedded in Friday Celebrate

### Mid-Quarter Check-in (Week 6)

90-minute RAD-format meeting.

| Phase | Block | Time |
|-------|-------|------|
| Reflect | Where are we? (KR data, confidence) | 15 min |
| Reflect | What is working? (scaling wins) | 30 min |
| Align + Decide | What is not working? (carry/kill/pivot/escalate) | 30 min |
| Decide | Adjust roadmap and capacity | 15 min |

### Close-of-Quarter Retro (Week 13)

90-minute RAD-format meeting.

| Phase | Block | Time |
|-------|-------|------|
| Reflect | Score each KR (0.0-1.0) | 30 min |
| Reflect | What did we learn? (customer, product, process) | 30 min |
| Decide | What carries to next quarter? | 30 min |

---

## 7. The carry/kill/pivot/escalate decision (mid-quarter)

At the mid-quarter check-in, every KR with confidence <= 5 requires an explicit decision:

| Decision | When to use |
|----------|-------------|
| **Carry** | The hypothesis is still right; we need more time, resources, or unblocking. Continue as planned. |
| **Kill** | The hypothesis was wrong. Drop the KR; redirect capacity. |
| **Pivot** | The general direction is right but the specific KR or approach is wrong. Reframe the KR with what we have learned. |
| **Escalate** | The decision is above the team's authority. Bring to exec or cross-team owner. |

The discipline of explicit decisions prevents the worst quarterly planning failure mode: KRs that quietly survive without progress and surprise everyone at the close.

---

## 8. Quarterly review deck outline

At the end of the quarter, most teams present results upward (to a leadership team, all-hands, or board). The deck is *not* the close retro -- it is the communication of results. Typical structure:

1. **Quarter at a glance** -- 1 slide with average OKR score and headline outcomes
2. **OKRs scored** -- 1 slide per Objective with KR scores and brief commentary
3. **Wins** -- 2-3 slides on what worked and why
4. **Learnings** -- 2-3 slides on what did not work and what we learned
5. **Carry-overs** -- 1 slide on what continues into next quarter
6. **Next quarter teaser** -- 1 slide on the proposed Objectives for next quarter (subject to kickoff)
7. **Ask** -- 1 slide on what the team needs from leadership (resources, decisions, unblocking)

---

## 9. Anti-patterns and remedies

| Anti-pattern | Remedy |
|---------------|--------|
| OKR theater (written, never referenced) | Enforce Monday Commit + Friday Celebrate |
| Sandbagging (every KR hits 1.0) | Wodtke 0.6-0.7 heuristic; retro asks "should the target have been higher?" |
| Scope creep mid-quarter | Mid-quarter check-in formalizes carry/kill/pivot decisions |
| Implicit carry-overs | Carry-over decisions are explicit and require re-commitment |
| Capacity over-commit | EM-owned capacity plan; reserve 15-20% |
| Internally-driven OKRs (no customer signal) | Strategy review includes customer signal from `discovery/customer-interview-script/` |
| OKRs disconnected from vision | Each Objective cites a vision pillar |
| Dependencies surprise late | Pre-quarter dependency mapping (`execution/dependency-map/`) |
| Retro skipped | Schedule at kickoff; never let it slip |

---

## 10. Worked example: Reconcile Q3

### Pre-quarter homework summary

- **Strategy review:** Unchanged. Vision still inspires. NSM (% of customers closing in <5 days) at 38%, target 60% by year-end.
- **Outcome candidate list (7 candidates):** Top three:
  1. Reduce close time from 5d to 3d for cohort A (B2B SaaS, 100-500 employees)
  2. Launch Xero integration (~30% of pipeline)
  3. Migrate audit log export to v2 schema
- **Capacity:** 80 person-weeks productive, 15 PW reserve (19%). Headcount steady.

### Kickoff outcome

- **Objective:** Make month-end close fast and trusted for mid-market B2B SaaS
- **KR1:** Close time for cohort A from 5 days to 3 days
- **KR2:** Xero integration shipped and adopted by 5+ paying customers
- **KR3:** Audit log v2 launched with zero customer-reported correctness issues
- **Roadmap:** Now = KR1 + KR2 work; Next = KR3; Later = multi-entity (Q4 candidate)
- **Cadence:** Monday Commit Mon 10am; Friday Celebrate Fri 4pm; Mid-check Aug 15; Close retro Sep 26

### Mid-quarter check-in (week 6)

- KR1 confidence: 7 (on track)
- KR2 confidence: 8 (Xero integration in beta with 4 customers; on track)
- KR3 confidence: 4 (audit log migration discovered schema-compat issues -- PIVOT to phased rollout, defer half to Q4)

### Close retro (week 13)

- KR1 score: 0.7 (cohort A close time 5d -> 3.5d)
- KR2 score: 0.9 (8 paying customers adopted Xero integration)
- KR3 score: 0.5 (audit log v2 phase 1 shipped; phase 2 deferred -- expected outcome of mid-quarter pivot)
- Average: 0.70 (in the Wodtke target zone)

Learnings:
- Customer: SMB segment values Xero more than enterprise expected
- Product: Audit log migrations should always be phased; lesson for future schema work
- Process: Mid-quarter pivot worked; team had confidence to make the call

---

## 11. References

- Wodtke, Christina. *Radical Focus: Achieving Your Most Important Goals with OKRs*. Cucina Media, 2016 (2nd ed. 2021).
- Cagan, Marty. *Inspired: How to Create Tech Products Customers Love*. Wiley, 2nd ed. 2017.
- Cagan, Marty & Jones, Chris. *Empowered: Ordinary People, Extraordinary Products*. Wiley, 2020.
- Doerr, John. *Measure What Matters*. Portfolio, 2018 (the canonical OKR origin text).
- Grove, Andrew S. *High Output Management*. Vintage, 1983 (foundational management cadence text).

## references/red-flags.md

# Red Flags: Quarterly Planning

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan before publishing the quarterly plan (kick-off deck, OKR doc, capacity model, mid-Q check-in, close-out retro). Each red flag is paired with bad and good examples.

---

## Red Flag 1: OKR Theater

**Symptom.** Each team writes OKRs in a vacuum, presents them at kick-off, and never references them again until close-out.
**Why it's bad.** OKRs are a coordination mechanism, not a ritual. If teams do not reference them weekly to make trade-offs, they become a parallel-track artifact -- the work that actually happens has no relation to the OKRs that were written. By close-out, scores are rationalized post-hoc.
**Bad example:**
> "OKRs were set in the Q kick-off in January. Mid-quarter check-in canceled because of release crunch. Close-out: 3/4 KRs scored 0.7+."
**Good example:**
> "OKRs reviewed in every weekly leadership sync (15 min). Mid-Q check-in surfaced that KR2 was off-track due to staffing; team explicitly re-baselined to 0.5-of-0.7 and documented the trade-off. Close-out scores match what we tracked weekly -- no surprises."
**How to catch it.** OKRs not referenced in any weekly artifact during the quarter = theater.

---

## Red Flag 2: Capacity Planned in Story Points, Reality Lived in Calendar Days

**Symptom.** "Engineering has 240 story points of capacity this quarter" -- but the team has not calibrated story points to time, and PTO / on-call / interview load are not subtracted.
**Why it's bad.** Story points are a relative-sizing tool, not a capacity-planning tool. Treating them as if they convert to days produces a fiction. Teams over-commit, slip, and learn to distrust planning.
**Bad example:**
> "Team A: 240 points capacity, committing to 240 points of work."
**Good example:**
> "Team A: 12 ICs x 60 working days = 720 IC-days. Subtract on-call (60), PTO (90), interviews (30), required maintenance (90) = 450 productive IC-days. Allocate 70% to OKR work (315 days), 20% to keep-the-lights-on (90 days), 10% buffer (45 days). Convert to ~22 story-points of OKR work at our calibrated 14 IC-days / point."
**How to catch it.** No documented PTO / on-call subtraction = capacity model is fiction.

---

## Red Flag 3: Planning Poker for Capacity

**Symptom.** "Each team voted on how many initiatives they could take. Average is 4." -- treating capacity as a democratic vote rather than a calculation.
**Why it's bad.** Planning poker is calibrated to relative effort comparisons, not to absolute capacity. When asked "how many initiatives can you ship?", engineers anchor on past quarters (which were over-committed) and the group converges on a number that is wrong in the same direction.
**Bad example:**
> "We polled all 6 teams: each said they could take 4 large initiatives this quarter. So 24 initiatives in the slate."
**Good example:**
> "Capacity model in `capacity-q2.xlsx` per team: each team has 450 productive IC-days. Average initiative size (calibrated against last 4 quarters): 90 IC-days. So 5 initiatives per team, ~30 in the slate. Then we cut 25% buffer = 22 in the committed slate."
**How to catch it.** Capacity expressed only as integer initiative counts with no IC-day basis.

---

## Red Flag 4: Kickoff Without Last Quarter's Retro

**Symptom.** New quarter kicks off Monday. Previous quarter never had a structured retrospective.
**Why it's bad.** Quarterly planning compounds knowledge. Without a retro, every team makes the same estimation mistakes, takes on the same dependencies, and misses the same external constraints. The org loses 4x learning velocity.
**Bad example:**
> "Q1 over Friday. Q2 kickoff Monday. No retro -- 'we already know what went wrong'."
**Good example:**
> "Q1 retro Tue / Wed of week 1 of Q2. Three artifacts: (1) what we got wrong about capacity, (2) which dependencies blew up, (3) which OKRs we should never have written. Outputs explicitly feed Q2 planning -- 'we will not write 'launch X' as a KR again; KRs are outcome-based'."
**How to catch it.** Kickoff date earlier than retro date = retro is missing.

---

## Red Flag 5: Stretch Goals as Committed Slate

**Symptom.** "We aim high" -- every KR is set at an aspirational level (Google-style "0.6-0.7 = great"), but the slate is committed and execs expect all KRs to hit 1.0.
**Why it's bad.** Mixing aspirational and committed goals is a category error. If execs expect 1.0, the team writes safe goals (and innovation drops). If the team writes aspirational goals, execs treat misses as failure. Pick one or split explicitly.
**Bad example:**
> "Q2 OKRs are stretch. (Side conversation with CEO: 'I expect all green at close.')"
**Good example:**
> "Q2 has two OKR tiers, explicit. Committed: 4 KRs at 1.0 expectation, scored as deliver / miss. Aspirational: 3 KRs at 0.7 expectation, scored on a 0-1 scale. Compensation review only references committed."
**How to catch it.** OKR doc has one tier + side-conversation expectations = split into two tiers.

---

## Red Flag 6: Quarter as a Container for All Strategic Work

**Symptom.** Everything strategic in the company gets squeezed into a 90-day OKR.
**Why it's bad.** Some work has a natural cadence of 18-36 months (platform rewrites, regulatory programs, new market entry). Forcing it into a 90-day OKR produces fake milestones ("KR: ship phase 1") that do not represent customer-visible outcomes.
**Bad example:**
> "KR: Complete phase 1 of the multi-region platform rewrite (year-long program)."
**Good example:**
> "Multi-region rewrite is tracked as a *program* on a separate dashboard with quarterly milestones and an annual budget. The Q2 OKR slate has one KR derived from the program ('99.95% availability in EU region, measured from June 1') -- a quarter-bounded outcome, not a phase."
**How to catch it.** KR uses words like "phase 1", "milestone X", "kick off Y" = wrong artifact.

---

## Red Flag 7: KRs That Are Activities, Not Outcomes

**Symptom.** "KR: ship the new pricing page" -- the KR is a deliverable, not a measurable change in the world.
**Why it's bad.** Activity-based KRs let the team ship and feel successful even if the shipped thing did nothing. Outcome KRs ("free-to-paid conversion at 4.5% in June") force the team to confront whether the shipped thing worked.
**Bad example:**
> "KR: launch new pricing page by June 1."
**Good example:**
> "KR: free-to-paid conversion >= 4.5% across all paid plans by June 30, measured from Q2-cohort signups. (Pricing-page redesign is the *bet* we are making on this KR, not the KR itself.)"
**How to catch it.** KR contains a verb of delivery (ship, launch, build, complete) without a downstream metric = rewrite.

---

## Red Flag 8: Cross-Team Dependencies Discovered Mid-Quarter

**Symptom.** Team A planned an initiative that needs Team B's API. Team B did not include that work in their slate. Discovered week 6.
**Why it's bad.** Mid-quarter dependency discovery is the leading cause of slippage. By week 6 there is no slack to absorb it, and one team's slip cascades into 2-3 others.
**Bad example:**
> "Team A blocked on Team B API in week 6. Team B's capacity now reallocated; their own KR3 slips."
**Good example:**
> "Pre-kickoff: every team listed initiatives + dependencies in `q2-dependencies.json`. Cross-team session week 0 reconciled 14 dependencies. 3 dependencies resulted in scope cuts (Team A descoped Initiative X because Team B could not commit). Week 6: zero new cross-team dependencies discovered."
**How to catch it.** No documented dependency-reconciliation session in week 0 = mid-Q surprises guaranteed.

---

## Red Flag 9: 14 KRs Per Team

**Symptom.** "We have 14 KRs to be comprehensive."
**Why it's bad.** Doerr's original guidance is 3-5 objectives, 3-5 KRs each, max. Beyond that, attention diffuses and *nothing* is prioritized. Teams with 14 KRs ship the easy ones and rationalize away the hard ones at close.
**Bad example:**
> "Team A Q2: O1 (3 KRs), O2 (4 KRs), O3 (3 KRs), O4 (4 KRs). 14 KRs total."
**Good example:**
> "Team A Q2: 2 objectives, 3 KRs each. 6 KRs total. Remaining work is keep-the-lights-on (tracked separately, not OKR-bound) or moved to Q3."
**How to catch it.** KR count per team > 7 = collapse or defer.

---

## Red Flag 10: Mid-Q Check-In Without Rebaselining Authority

**Symptom.** Mid-quarter check-in identifies that KR2 is off-track, but the team is told to "just push harder", with no authority to descope.
**Why it's bad.** The check-in's purpose is to surface trade-offs while there is still time to make them. Without rebaselining authority, the check-in is reduced to a status meeting and the org loses the chance to redirect.
**Bad example:**
> "Mid-Q: KR2 off-track. 'Catch up by quarter-end.' (No descope, no scope swap.)"
**Good example:**
> "Mid-Q: KR2 off-track. Three options presented: (a) descope KR2 from 5000 -> 3000 users, (b) borrow 60 IC-days from Team B who is ahead on their KR1, (c) drop KR3 to free capacity. Decision documented: option (a), CEO signs off."
**How to catch it.** Mid-Q outputs no rebaseline decisions = it was status, not planning.

---

## Red Flag 11: Quarterly Plan With No Bet Framing

**Symptom.** The plan lists what teams will do but never says *what we expect to learn* or *what could be wrong*.
**Why it's bad.** A quarterly plan is a portfolio of bets. Skipping the "what could be wrong" step means the team executes confidently on assumptions that may be false, and discovers the failure only at close-out.
**Bad example:**
> "Q2 plan: ship X, Y, Z, hit OKRs."
**Good example:**
> "Q2 plan with 5 explicit bets: (1) 'pricing redesign moves conversion from 3.2% to 4.5%' -- could be wrong if elasticity is lower than estimated; (2) 'enterprise tier launches with 8 design partners' -- could be wrong if procurement cycles are > 90 days. Each bet has a hypothesis, a tripwire, and a documented owner."
**How to catch it.** Plan does not list assumptions and tripwires = run the `pre-mortem` skill before publishing.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | OKR theater | OKRs referenced in any weekly artifact during Q? |
| 2 | Capacity in story points only | PTO / on-call / interviews subtracted? |
| 3 | Planning poker for capacity | Capacity grounded in IC-days? |
| 4 | Kickoff before last retro | Retro date < kickoff date? |
| 5 | Stretch vs committed mixed | Two tiers, explicitly labeled? |
| 6 | Multi-year work in 90-day KR | KR has "phase X" / "kick off"? |
| 7 | KRs as activities | Verb of delivery without downstream metric? |
| 8 | Dependencies discovered mid-Q | Week-0 reconciliation session held? |
| 9 | 14 KRs per team | KR count > 7 per team? |
| 10 | Check-in without rebaseline | Mid-Q outputs include scope swap / descope? |
| 11 | No bet framing | Plan lists assumptions and tripwires? |

## Related Reading

- `SKILL.md` -- the kickoff -> mid-Q -> close-out cycle
- `references/okr-patterns.md` -- OKR writing patterns
- Sibling skill: `execution/brainstorm-okrs/` -- generate candidate OKRs
- Sibling skill: `execution/prioritization-frameworks/` -- rank initiatives within the slate
- Sibling skill: `execution/dependency-map/` -- week-0 dependency reconciliation
- Sibling skill: `discovery/pre-mortem/` -- bet framing and tripwires
- Sibling skill: `sprint-retrospective/` -- quarter retro patterns

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/quarterly-planning
