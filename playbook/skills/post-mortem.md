# post-mortem

> **Use these instructions for this whole conversation.** Apply them when: Run a blameless review with a timeline, contributing causes and owned action items. Use when an incident, outage, missed launch or failed experiment needs a written review.

# Post-Mortem (Blameless Incident Review)

## Overview

A post-mortem is a structured, blameless review held after an incident, outage, regression, missed launch, or failed experiment. The goal is not to assign fault but to learn how the system (people, process, code, and organization) produced the outcome, and to commit to durable changes that reduce the chance of recurrence.

It follows the blameless post-mortem practice common in site reliability engineering, with systems-thinking sources listed under References. Where the companion `discovery/pre-mortem/` skill imagines failure before it happens, post-mortem learns from failure that already did.

## Core Capabilities

- **Severity classification** — Sev 0-4 + near-miss thresholds, with post-mortem requirement and SLA per level
- **Blameless facilitation** — five ground rules, the Dekker New View, hindsight/counterfactual removal, the Allspaw test
- **10-section authoring** — header → summary → impact → timeline → what went well/wrong → factors → RCA → actions → lessons
- **Root-cause analysis** — 5 Whys for clear chains, Causal Tree for multi-factor Sev 0/1/2; root-cause vs contributing-factor
- **Action-item discipline** — single owner, real ticket, testable acceptance criteria, recurring completion audit
- **Distribution & archive** — audience-appropriate formats; searchable, service-tagged archive

## When to Use

- **Sev 1 / Sev 2 incident** — customer-facing outage, data loss, security event, payments failure, or significant regression.
- **Sev 3 with novelty** — worth a post-mortem if it surfaced a failure class the team has not seen before.
- **Missed launch or rolled-back release** — the launch itself is the incident.
- **Failed experiment with a negative business outcome** — e.g. a pricing test that depressed revenue.
- **Customer escalation** — an exec customer call where the product was the proximate cause.
- **Near miss** — the deploy that "almost" took the site down; some of the highest-leverage learning a team gets.

If the incident is below the severity threshold and the team has seen the same class of failure recently, document the recurrence in the existing post-mortem rather than producing a new one.

## Clarify First

Before authoring the post-mortem, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Severity level:** Sev 0-4 / near-miss sets the template depth, the SLA window, and whether 5 Whys or a Causal Tree is required.
- **Incident timeline / chat transcript:** the source for the Timeline and Impact sections; without it the reconstruction is guesswork.
- **Customer / business impact:** scope, duration, and who was affected drives both the Impact section and the severity itself.
- **Root-cause method:** 5 Whys for a clear single chain vs Causal Tree for multi-factor Sev 0/1/2; drives the RCA section.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. At incident close, the incident commander assigns an author who opens `assets/post_mortem_template.md`.
2. Scaffold Header, Summary, Impact, and Timeline from the incident chat transcript.
3. Within the SLA window, draft the remaining sections, run the chosen root-cause method, and hold a 60-90 min blameless review.
4. Apply the Allspaw test, file every action item as a real ticket with an owner and due date, then publish to the searchable archive.

Default SLAs [RECOMMENDED], to replace with your organisation's: Sev 1 draft within 5 business days, Sev 2 within 7. The reason for a short window: memory and chat context fade within a week, and the timeline is the part that cannot be reconstructed later.

**Done when** the timeline has no unexplained gaps, the analysis names contributing factors (not a person), and every action item has one owner, a ticket and a testable done condition.

The blameless principles, severity thresholds, full template, workflow, and root-cause methods all live in the references below.

## Anti-Patterns

### Counterfactuals in the root-cause analysis
**Mistake:** The analysis says "if only the engineer had checked the dashboard at 14:05, this would have been caught".
**Why it happens:** Hindsight makes the right action look obvious, and a counterfactual reads like an explanation.
**Instead:** Search the draft for "if only", "would have", "should have" and "could have". Replace each with the system property behind it, such as "queue depth was not shown above the fold", and turn that into an action item.

### Stopping at a single root cause
**Mistake:** The post-mortem names one cause ("connection pool exhausted"), proposes one fix, and ends.
**Why it happens:** One clean cause feels like closure, and 5 Whys can lead to a single chain.
**Instead:** List the contributing factors that aligned: capacity settings, alert thresholds, escalation paths, runbook gaps. For multi-factor Sev 0/1/2 incidents, use the Causal Tree instead of 5 Whys, and give each factor its own action item.

### Treating a recurring incident as new
**Mistake:** This is the third incident of the same class in 8 months. Each post-mortem named a different cause and none looked back.
**Why it happens:** Each incident is written up on its own, and nobody searches the archive first.
**Instead:** Before the review meeting, search the archive for the failure class and audit the open action items from earlier post-mortems. More than 2 occurrences in 12 months means you analyze the pattern, and finishing the old items is the first action.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `assets/post_mortem_template.md` | 10-section post-mortem template |
| `assets/incident_timeline_worksheet.md` | Timeline prompts |
| `assets/action_item_tracker.md` | Cross-incident action tracker |
| `assets/what_went_well_prompts.md` | Positive-observation prompts |
| `examples/payment-processing-outage.md` | Worked post-mortem |

## References

- **[references/post-mortem-process.md](references/post-mortem-process.md)** — severity thresholds, the 10-section template, the Day 0 → Day 30 workflow, action-item follow-through, distribution/archive practice, and the assets inventory. Read when running a post-mortem end to end.
- **[references/blameless-culture-guide.md](references/blameless-culture-guide.md)** — what blameless means, the Dekker reframe, blameful vs blameless phrasing, hindsight bias, counterfactuals, establishing the culture, plus the five ground rules and the Allspaw test. Read when facilitating or when a draft feels blameful.
- **[references/5-whys-vs-causal-tree.md](references/5-whys-vs-causal-tree.md)** — both root-cause methods with worked examples, the choose-between table, and the root-cause vs contributing-factors distinction. Read before the root-cause section of the meeting.
- **[references/red-flags.md](references/red-flags.md)** — 12 anti-patterns (blame language, ownerless action items, single root cause, second-mortems...), plus the troubleshooting table and success criteria. Read before publishing or signing off.
- Foundational reading: Google SRE "Postmortem Culture"; Allspaw "Blameless PostMortems and a Just Culture" (2012); Cook "How Complex Systems Fail" (1998); Perrow *Normal Accidents* (1984); Dekker *Field Guide* (2014) and *Just Culture* (2017).

## Scope & Limitations

**In Scope:** Post-mortem authoring for incidents, outages, regressions, missed launches, failed experiments, customer escalations, and near misses. Severity classification, blameless facilitation, 5 Whys, Causal Tree analysis, action-item tracking, distribution and archival practice.

**Out of Scope:** Live incident command and on-call coordination (see `delivery-manager/`). Sprint retrospectives on team practice (see `sprint-retrospective/`). Risk surfacing before launch (see `discovery/pre-mortem/`). Quantitative reliability engineering and error-budget policy (see `engineering/` skills if present).

**Important Caveats:** Blameless culture is a prerequisite, not an output — if management uses post-mortems as a performance signal, the documents become sanitized; establish the separation in writing. Regulated industries (medical devices, aviation, financial services) that require named accountability should run a parallel internal blameless post-mortem alongside the regulator-facing report. A post-mortem is a learning artifact, not a fixing artifact: the fix lives in the action items and their follow-through, so one with zero completed action items is a failed post-mortem. (Cook's 4-page "How Complex Systems Fail" is worth reading before facilitating a complex Sev 0/1 — linked in the blameless culture guide.)

## Integration Points

| Integration | Direction | What flows |
|---|---|---|
| `discovery/pre-mortem/` | Bidirectional | Post-mortem findings update next launch's pre-mortem risk register; pre-mortem mitigations become post-mortem-checked controls |
| `delivery-manager/` | Receives from | Incident response context, severity classification, on-call handoffs |
| `sprint-retrospective/` | Bidirectional | Team-practice retros surface incident patterns; post-mortems feed retro themes |
| `daci-framework/` | Feeds into | Action items use DACI to assign owner (D), accountable (A), consulted, informed |
| `execution/dependency-map/` | Receives from | Cross-team contributing factors map to dependency-graph nodes |
| `execution/status-update-generator/` | Feeds into | Sev 0/1 incidents surface in weekly executive status updates |
| `senior-pm/` | Feeds into | Repeated incident classes feed portfolio risk register via `risk_matrix_analyzer.py` |
| `scrum-master/` | Feeds into | Action items become sprint backlog items with mitigation-focused stories |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/5-whys-vs-causal-tree.md

# 5 Whys vs Causal Tree

Two root-cause analysis methods commonly used in blameless post-mortems. They produce different artifacts and are suited to different incident shapes. This guide explains when to pick each, with worked examples.

## 5 Whys

### Origin

The 5 Whys technique originated at Toyota in the 1950s as part of the Toyota Production System, codified by Taiichi Ohno. It is the simplest root-cause method in widespread use and the most often misused.

### How it works

Start with the proximate effect — what the customer experienced or what the monitoring detected. Ask "why?" The answer becomes the next subject. Ask "why?" of that. Continue until you reach a cause the team can act on.

The number "five" is heuristic, not literal. Stop when you reach a cause that:
- The team can address, and
- Is not itself merely a symptom of a deeper cause.

### Worked example: payment API outage

**Effect: The payment API returned HTTP 500 for 22 minutes between 14:18 and 14:40 UTC.**

1. **Why?** The Stripe-facing service ran out of database connections.
2. **Why?** A nightly batch job opened 200 connections and did not release them after an error.
3. **Why?** The connection lifecycle in the batch job is managed by a Python context manager (`with` block), but a refactor introduced an early return before the `finally` block was reached.
4. **Why?** The refactor's pull request had no test that exercised the error path; reviewers focused on the happy path because the test fixture only seeded a successful database.
5. **Why?** The test fixture standard does not require both success and error paths to be covered; the linter enforces structural review, not coverage of execution paths.

**Action item:** Update the test fixture standard to require error-path coverage; add a CI check that any new code path acquiring a database connection is exercised by both success and error tests.

### Strengths

- Fast. A 5 Whys exercise fits in 15 minutes.
- Anyone can run it. No facilitator training needed.
- Produces a clear narrative that flows well in writing.
- Naturally points to one or two action items.

### Limits

- **Linear.** It traces one chain. Real incidents are usually multi-causal.
- **Stops too early.** It is tempting to stop at the first "satisfying" answer.
- **Risks naming a person as the 4th or 5th "why".** If the chain ends at "the engineer made a mistake", you have done it wrong — keep asking why the system allowed the mistake.
- **Confirmation bias.** The questioner often anticipates an answer and unconsciously leads the chain.

### Anti-patterns

- "Why did Joe push the bad code?" — names a person. Reframe as "Why did the bad code reach production?"
- Stopping at "human error". Human error is a symptom; ask why the system permitted it.
- Stopping at "we need more training". Training is rarely the durable fix; ask why the system depends on memory rather than tooling.
- Stretching to exactly five steps when the chain is naturally three or seven.

## Causal Tree

### Origin

The causal tree comes from accident-investigation methodology in safety-critical industries (aviation, healthcare, nuclear). It is the implicit model in John Allspaw's writing on Etsy's debriefing practice and in Charles Perrow's Normal Accident Theory.

### How it works

The root of the tree is the incident outcome. Each branch is a contributing factor — a condition that, if absent, would have made the incident less likely or less severe. Each contributing factor can itself have sub-factors. Branches can run in parallel and combine with AND or OR logic.

The tree captures the structural truth that complex incidents rarely have one cause; they have a set of conditions that aligned.

### Worked example: payment API outage (same incident)

```
Outcome: Payment API 500s for 22 minutes
│
├── BRANCH 1: Database connection pool exhausted
│   ├── Batch job leaked connections (the proximate trigger)
│   │   ├── Early-return in refactored code bypassed context manager
│   │   │   └── Code review did not catch the early return (no error-path test)
│   │   └── Batch job ran during peak hours
│   │       └── Cron schedule predates current peak-hour shift
│   └── Pool size was 50 (set conservatively for cost)
│       └── Capacity planning predates current traffic shape (2024 baseline still in config)
│
├── BRANCH 2: Detection was late (alert fired at minute 8)
│   ├── Alert threshold set at 95% pool utilization
│   │   └── No warning threshold at 80%
│   ├── PagerDuty escalation to on-call DBA was stale
│   │   └── On-call rotation rotated owner in March, escalation policy not updated
│   └── Dashboard for pool depth not on the on-call's default view
│
└── BRANCH 3: Mitigation took 12 minutes after detection
    ├── Runbook for pool exhaustion missing the connection-kill command
    │   └── Runbook last reviewed 18 months ago
    ├── On-call had not done a database incident before
    │   └── New on-call onboarded last month; database incident not in the drill list
    └── Mitigation required SSH bastion access
        └── Bastion access requires a fresh 2FA token; on-call had to re-auth
```

The tree exposes 11 distinct contributing factors across 3 branches. Each leaf or sub-tree maps to a candidate action item. The team can then prioritize: which factors, if changed, would most reduce probability or severity of recurrence?

**Action items from this tree (prioritized):**

1. Fix the connection leak in the batch job (P0, prevent recurrence of trigger).
2. Add a warning alert at 80% pool utilization (P0, improve detection).
3. Update PagerDuty escalation to the current on-call DBA (P0, improve detection).
4. Add the connection-kill command to the runbook; review all DBA runbooks for staleness (P1, improve mitigation).
5. Add a database incident to the on-call drill rotation (P1, improve mitigation).
6. Move the bastion 2FA token to a longer session (P2, improve mitigation).
7. Re-baseline pool size against current peak-hour traffic (P2, prevent recurrence).
8. Move batch job to off-peak hours (P2, reduce impact).

### Strengths

- Captures the multi-factor structure of complex failures.
- Each leaf maps cleanly to an action item.
- Visible structure makes it easy to spot single-point-of-failure assumptions and missing coverage.
- Encourages thinking about prevent / detect / mitigate / respond as separate dimensions.

### Limits

- Time-consuming. A causal tree for a Sev 1 can take 90 minutes of facilitated discussion.
- Requires a facilitator who can keep the discussion focused on system properties.
- Risk of analysis-paralysis: trees can grow indefinitely. Cap at 3 levels deep per branch.
- Less narrative-friendly. The post-mortem document needs prose to wrap the tree.

## How to choose

| Decision factor | 5 Whys | Causal Tree |
|---|---|---|
| Severity | Sev 3 / 4 / near miss | Sev 0 / 1 / 2 |
| Failure shape | Single clear chain | Multiple contributing factors |
| Time available | 15-30 min | 60-90 min |
| Audience | Owning team only | Owning team + cross-team + execs |
| Recurrence | First instance of this class | Recurring failure mode |
| Output format | Inline in post-mortem | Tree diagram + prose |

When in doubt for a Sev 1 or higher, default to Causal Tree. The extra time pays off in better action items and fewer recurrences.

## Combining both

For complex incidents, a hybrid pattern is effective:

1. Start with 5 Whys on the proximate trigger to get a clean chain quickly.
2. Then ask: "What other conditions, if absent, would have prevented or reduced this?"
3. The answers become parallel branches of a causal tree, with the 5 Whys chain as one branch.

This gives the team the speed and narrative clarity of 5 Whys plus the structural completeness of a causal tree.

## Common mistakes (both methods)

- Naming people in any branch or "why". Names belong only in the action-item owner column.
- Stopping at "human error" or "we need training". Always one more why.
- Counterfactuals as causes. "If only X had not happened" is not a cause; "the system permitted X" is.
- Confirmation bias. The investigator goes in with a hypothesis and the chain or tree confirms it. Counter by inviting someone outside the team to ask questions.
- Single-root-cause framing. The conclusion should say "the set of conditions that aligned", not "the root cause was".

## References

- Taiichi Ohno, *Toyota Production System: Beyond Large-Scale Production* (1988)
- Richard Cook, "How Complex Systems Fail" (1998)
- John Allspaw, *Debriefing Facilitation Guide* (Etsy)
- Charles Perrow, *Normal Accidents* (1984) — for the theoretical grounding on why single-cause framing fails in complex systems
- Sidney Dekker, *The Field Guide to Understanding "Human Error"* (3rd ed., 2014)

---

## Root Cause Methods (quick reference from SKILL.md)

### 5 Whys

A linear technique popularized by Toyota. Start with the proximate effect and ask "why?" five times. Each answer becomes the next question.

```
1. Why did the API return 500 errors for 22 minutes?
   → Because the database connection pool was exhausted.
2. Why was the connection pool exhausted?
   → Because a batch job opened 200 connections without releasing them.
3. Why did the batch job not release them?
   → Because the connection lifecycle is managed by a context manager that was bypassed on the error path.
4. Why was the error path bypassing the context manager?
   → Because a refactor in March introduced an early return before the `finally` block.
5. Why did the refactor land without catching this?
   → Because the test suite does not exercise the connection-pool exhaustion path.
```

**Strengths:** fast, anyone can run it, fits in a 15-minute slot.

**Limits:** linear — only finds one chain. Real incidents usually have multiple contributing factors that combine non-linearly. Use 5 Whys when the failure is a clear chain. Use Causal Tree when it is not.

### Causal Tree (Allspaw / SRE style)

A tree where the root is the incident outcome and the branches are the contributing factors. Each factor can have its own sub-factors. Unlike 5 Whys, the tree allows for parallel chains and AND/OR relationships.

```
Outcome: API returned 500s for 22 minutes
├── Connection pool exhausted
│   ├── Batch job leaked connections (code defect)
│   │   ├── Early-return bypassed context manager
│   │   └── Test suite did not cover error path
│   └── Pool size set conservatively for cost reasons
│       └── Capacity planning predates current traffic shape
├── Alert fired late
│   ├── Threshold set at pool 95% (no warn at 80%)
│   └── PagerDuty escalation path stale (rotated owner)
└── Mitigation took 12 minutes
    ├── Runbook missing pool-restart command
    └── New on-call had not shadowed a database incident
```

**Strengths:** captures the multi-factor nature of complex systems failures. Maps cleanly to action items (one mitigation per leaf or sub-tree).

**Limits:** longer to produce. Requires a facilitator who can keep the team from arguing the tree structure rather than the substance.

### Choosing between them

| Use 5 Whys when | Use Causal Tree when |
|---|---|
| Single clear chain of cause | Multiple contributing factors |
| Sev 3 / Sev 4 incidents | Sev 0 / Sev 1 / Sev 2 incidents |
| Pressed for time | Recurring class of failure |
| Audience is a small team | Audience includes execs, multiple teams |

## Root Cause vs Contributing Factors

A common post-mortem failure mode is to declare a single "root cause" and stop. This is Perrow's Normal Accident Theory in action: complex systems fail because multiple contributing factors align, not because one thing broke. A post-mortem that names one root cause and prescribes one fix is usually incomplete.

| | Root cause | Contributing factor |
|---|---|---|
| **Definition** | The conditions that, if absent, would have prevented the incident | Conditions that increased the probability or severity but were not individually sufficient |
| **Example** | "Connection-pool exhaustion in service X" | "Stale on-call rotation", "missing runbook entry", "no canary deploy" |
| **Action implication** | Always addressed | Each addressed unless explicitly accepted with rationale |

Allspaw's reading of Perrow argues that in tightly-coupled complex systems, there is rarely a single cause; the appropriate framing is "the set of contributing factors that aligned". Write the post-mortem accordingly.

## references/blameless-culture-guide.md

# Blameless Culture Guide

## What blameless really means

Blameless post-mortems are a practice imported from the safety-critical industries (aviation, healthcare, nuclear) and adapted by Google SRE and Etsy in the early 2010s. The core claim is empirical: organizations that punish individuals for incidents produce sanitized, defensive incident reports, learn nothing from them, and continue to suffer the same incidents. Organizations that explicitly remove personal blame from the learning process produce richer, more honest reports and reduce recurrence.

Blameless does **not** mean:
- No accountability. People are still accountable for following process, communicating clearly, and completing the action items they own.
- No consequences ever. Gross negligence and policy violations are addressed — but in HR or legal channels, not in the post-mortem document.
- Everyone is right. The post-mortem can name decisions that, in hindsight, were the wrong call. It just names them as decisions made by a system, not character flaws of a person.

Blameless **does** mean:
- Assume everyone acted reasonably given what they knew at the time.
- Focus on the conditions (code, process, tooling, organization) that produced the decision.
- Separate the learning artifact (the post-mortem) from the management artifact (performance review).

## The Dekker reframe

Sidney Dekker, in *The Field Guide to Understanding "Human Error"*, distinguishes between the **Old View** and the **New View** of human error:

| Old View | New View |
|---|---|
| Human error is the cause | Human error is a symptom |
| The system is mostly safe, humans introduce risk | The system is mostly unsafe, humans manage to make it work |
| Investigation finds the bad apple | Investigation finds the conditions that made the action locally rational |
| Fix: discipline, retraining, replacement | Fix: change the conditions |

A blameless post-mortem operates strictly in the New View. The question is never "why did Sarah deploy on a Friday?" It is "what conditions in our deploy process made a Friday deploy seem like a reasonable action to a competent engineer?"

## The Allspaw test

After writing the post-mortem, ask:

> "Would I send this document to the engineer who took the action that triggered the incident, and would they recognize their experience as fairly represented?"

If the answer is no, the document still contains blame, hindsight bias, or counterfactuals. Common signals to look for:

- Use of the word "should" (especially "should have").
- Use of "if only" or "had X happened".
- Phrases like "obvious", "clearly", "any competent X would have".
- A single person named in the narrative outside the contacts and action-item owner columns.
- The word "fault" appearing anywhere.

## Blameful vs blameless phrasing

| Blameful | Blameless |
|---|---|
| The on-call engineer should have noticed the queue depth alert. | The dashboard did not alert on queue depth exceeding 10,000 messages. |
| Sarah pushed the broken deploy. | A deploy at 16:42 UTC introduced the regression; the CI suite did not cover the affected code path. |
| The team failed to test the migration. | The migration test environment lacked production-scale data, so the lock contention pattern did not surface in pre-production. |
| Joe forgot to update the runbook. | The runbook update step is not part of the deploy checklist; runbook drift is not detected automatically. |
| If only we had run the canary properly, we would have caught it. | The canary deploy was configured to skip the affected service; canary coverage is not enforced at the service level. |
| The new engineer didn't know about the failover process. | The failover process is documented only in one engineer's personal notes; onboarding does not include a failover drill. |
| Management decided to skip the load test to ship faster. | The release calendar created pressure to ship by a specific date; the load test was deprioritized in a tradeoff decision documented in DECISION-1234. |
| Customer Support should have escalated faster. | The escalation criteria from Support to Engineering require a manager approval that the on-call manager was not paged for; the rotation for that page was stale. |

Notice the pattern: every blameless version names a system property (a dashboard threshold, a test fixture, a checklist, a documentation gap, a process gate). System properties are things the team can change. People are not.

## Hindsight bias

Hindsight bias is the cognitive distortion that makes past events seem more predictable than they actually were. Once you know the outcome, it is impossible not to see the steps that led to it. The post-mortem author's job is to deliberately strip out hindsight.

Test for hindsight bias: ask "at this moment in the timeline, what did the person know? what alerts had fired? what dashboards had they checked?" Reconstruct the information state. Often you discover that the "wrong" decision was the only reasonable decision given the information available.

A useful heuristic: if reading the timeline makes you think "well, obviously they should have done X next" — that's hindsight bias. They didn't have your view of the whole timeline. They had a noisy signal in the moment.

## Counterfactuals are not causes

A counterfactual is a statement about what would have happened if reality had been different: "if only we had run the canary, we would have caught it". Counterfactuals feel like causal claims but they are not. They are wishes.

The blameless reframe of a counterfactual is to find the system property that made the counterfactual scenario impossible or unlikely.

- Counterfactual: "If only the team had reviewed the migration script more carefully, the typo would have been caught."
- System property: "The migration review process did not include a syntax-check or dry-run; reviews relied on visual inspection of SQL."

Now you have something to change. "Review more carefully" is not actionable. "Add a CI step that runs every migration through a syntax checker and a dry-run in a staging schema" is.

## Establishing the culture

Blameless post-mortems do not happen because someone declares them. They happen because:

1. **Leadership says so explicitly and repeatedly.** A one-time email is insufficient. The CTO/VPE talks about blamelessness in all-hands, in 1:1s, and when an incident happens.
2. **Performance reviews are insulated.** Engineers know, in writing, that nothing they say in a post-mortem can be used against them in performance review. This is communicated by management and by HR.
3. **The first few post-mortems set the tone.** When the first Sev 1 happens after the policy is announced, the leadership team treats it as a model. Public praise for the author's honesty, no consequences for the engineer involved, visible action-item follow-through.
4. **Stories are told.** "Remember the time we lost three hours of writes? Here's what we learned." The retold incident becomes a cultural artifact rather than a buried embarrassment.
5. **Action items get done.** If post-mortems generate action items that never ship, engineers learn that post-mortems are theater. Completion rate is the loudest signal of how seriously leadership takes the practice.

## When blameless is genuinely hard

There are scenarios where pure blamelessness is in tension with other obligations:

- **Regulated industries** (medical devices, financial services, aviation): regulators may require named accountability in the formal report. The pattern is to run two artifacts in parallel: an internal blameless learning post-mortem, and a regulator-facing formal report. The two reference each other but serve different audiences.
- **Security incidents involving insider action**: if an engineer deliberately bypassed controls, the incident is not a blameless learning event. It belongs in HR / legal channels. The blameless post-mortem still happens for the *system* (why was the bypass possible?), separately from the personnel matter.
- **Repeated individual pattern**: if the same engineer is the proximate actor in multiple incidents, this is a management conversation about role fit, training, or workload — not a post-mortem matter. Conduct that conversation in 1:1s, not in incident review.

The mantra: blameless in the post-mortem, accountable in the action items, performance-managed in HR. Three separate channels, never mixed.

## References

- John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy, 2012)
- Richard Cook, "How Complex Systems Fail" (1998) — short paper, essential reading
- Sidney Dekker, *The Field Guide to Understanding "Human Error"* (3rd ed., 2014)
- Sidney Dekker, *Just Culture* (3rd ed., 2017)
- Google SRE Book, "Postmortem Culture: Learning from Failure" — https://sre.google/sre-book/postmortem-culture/
- Charles Perrow, *Normal Accidents: Living with High-Risk Technologies* (1984)
- Erik Hollnagel, *Safety-I and Safety-II: The Past and Future of Safety Management* (2014)

---

## Blameless Principles (quick reference from SKILL.md)

The single most-cited reason post-mortems fail to produce learning is that participants feel unsafe. Blameless does not mean "consequence-free" — accountability still exists for following process. It means: assume that everyone involved acted reasonably given what they knew at the time, and focus on the system that surrounded their decision.

### Five blameless ground rules

1. **No names in the narrative.** Refer to roles, not people. "The on-call engineer", not "Sarah". Names appear only in the contacts table and the action-item owner column.
2. **No "should have".** Replace with "the system did not surface". "The on-call should have noticed the queue depth" → "The dashboard did not alert on queue depth above 10,000".
3. **No counterfactuals in the root cause.** "If only X had not happened" is not a cause; it is a wish. Stick to mechanisms.
4. **Human error is a symptom, not a cause** (Dekker). When a human acted "incorrectly", the goal is to understand why that action was the locally rational thing to do.
5. **Hindsight bias is the enemy.** What is obvious now was not obvious then. Reconstruct what was knowable in the moment, not what is knowable now.

### The Allspaw test

Adapted from John Allspaw's writing: after writing the post-mortem, ask: *"Would I send this document to the engineer who pushed the button, and would they feel that it represented their experience fairly?"* If no, rewrite until yes.

## references/post-mortem-process.md

# Post-Mortem Process

> Read this when running a post-mortem end to end: severity thresholds, the 10-section template, the Day 0 → Day 30 workflow, action-item follow-through, distribution/archive practice, and the artifact (assets) inventory.

## Severity Thresholds

| Severity | Customer impact | Post-mortem required? | Distribution |
|---|---|---|---|
| **Sev 0 / Sev 1** | Full outage, data loss, security incident | Mandatory; within 5 business days | All engineering + execs |
| **Sev 2** | Partial outage, major degradation, payments impact | Mandatory; within 7 business days | All engineering |
| **Sev 3** | Single-feature degradation, recoverable | Optional unless novel pattern | Owning team |
| **Sev 4** | Minor issue, manual workaround available | Skip unless near-miss | None |
| **Near miss** | Almost caused Sev 0/1/2 | Recommended | Owning team + SRE |

Severity is set at incident open and confirmed at incident close; it can be revised upward but rarely downward.

## Post-Mortem Template Sections

A standard post-mortem has 10 sections, in this order:

1. **Header** — title, date, severity, duration, status (draft / final), authors.
2. **Summary** — 3-5 sentences. What happened, who was affected, how it was resolved, what the durable fix is. A reader who reads only this section should still know the headline.
3. **Impact** — customers affected (count and segments), revenue impact, SLO error budget burned, internal teams blocked.
4. **Timeline** — minute-by-minute log of events from detection to resolution. Include the trigger, detection, escalation, mitigation, and resolution timestamps. Mark "moment of decision" rows.
5. **What went well** — actions, tooling, or decisions that reduced impact. This section is critical and is the one most often skipped. It anchors the document in learning, not just blame avoidance, and surfaces practices worth replicating.
6. **What went wrong** — the system conditions that allowed the incident to happen and to persist. Phrased as system properties, not human failures.
7. **Contributing factors** — the list of conditions that, in combination, produced the outcome. Distinguish from root cause (below).
8. **Root cause analysis** — 5 Whys or Causal Tree (see `references/5-whys-vs-causal-tree.md`). Document the method used.
9. **Action items** — durable changes. Each item has an owner, a due date, a tracking issue ID, and a category (prevent / detect / mitigate / respond / process).
10. **Lessons learned** — broader patterns the team takes away. These often inform engineering standards, runbooks, or hiring.

## Workflow

### Day 0 (incident close)

1. Incident commander declares the incident resolved and assigns an author.
2. Author opens the post-mortem document from `assets/post_mortem_template.md`.
3. Fill in Header, Summary (placeholder ok), Impact, and the Timeline scaffold from the incident chat transcript.
4. Schedule the post-mortem meeting within the SLA window (5 business days for Sev 1, 7 for Sev 2).

### Day 1-3 (drafting)

1. Author interviews everyone who took an action during the incident. Use the prompts in `assets/incident_timeline_worksheet.md`.
2. Refine the Timeline with every action, decision, and observation. Mark decision points.
3. Draft "What went well" using `assets/what_went_well_prompts.md`. Aim for 3-7 items minimum.
4. Draft "What went wrong" and "Contributing factors".
5. Run the chosen root-cause method (5 Whys or Causal Tree).

### Day 3-5 (review)

1. Hold the post-mortem meeting. 60-90 minutes. Agenda:
   - 5 min: blameless ground rules read aloud
   - 15 min: Timeline review
   - 15 min: What went well + what went wrong
   - 20 min: Root cause discussion
   - 20 min: Action items (owner + due date for each)
   - 5 min: Lessons learned
2. Apply the Allspaw test to the document.
3. Author finalizes and the incident commander signs off.

### Day 5-30 (follow-through)

1. Each action item is filed in `assets/action_item_tracker.md` and the team's tracker (Jira, Linear, GitHub Issues).
2. Action items are reviewed at sprint planning and at the weekly engineering review.
3. After 30 days, audit the action-item completion rate. Industry data shows ~50% of post-mortem action items are never completed; the team should track and target a higher rate.

## Action-Item Follow-Through

The single largest failure mode of post-mortems is that action items go unbuilt. Mitigations:

- **Each action item has a single named owner** (a person, not a team) and a due date no more than one sprint out for high-priority items.
- **Each action item is a real ticket** in the team's tracker, not a bullet in a doc. Link the ticket from the post-mortem.
- **Action-item review is on a recurring agenda** — weekly engineering review or monthly post-mortem audit. Completion rate is a tracked metric.
- **The owner has authority**, not just responsibility. If the action requires another team, escalate to a program manager or use `daci-framework/` to assign decision rights.
- **Acceptance criteria are testable.** "Improve monitoring" is not an action item. "Add an alert on queue depth > 5,000 with PagerDuty page to #payments-oncall" is.

## Post-Mortem Distribution & Archive

| Audience | Format | Channel |
|---|---|---|
| Owning team | Full document | Team wiki, Jira/Linear linked |
| All engineering | Full document | Engineering-wide channel, weekly digest |
| Executives (Sev 0/1) | Summary + Impact + Action items | Exec email or weekly review |
| Public (if customer-impacting) | Public-facing status-page postmortem | status.<company>.com |
| Future engineers | Searchable archive | Wiki tag `post-mortem`, indexed by service |

Post-mortems should be discoverable. A new engineer joining the team should be able to find every past incident on the services they own within 5 minutes. Tag every post-mortem with the affected services, the date, the severity, and the failure class.

## Tools / Artifacts

This skill is template-driven. No Python automation. The artifacts are:

| Artifact | Purpose |
|---|---|
| `assets/post_mortem_template.md` | Full Google SRE-style template, ready to copy and fill |
| `assets/incident_timeline_worksheet.md` | Interview prompts and timestamp scaffolding |
| `assets/action_item_tracker.md` | Spreadsheet-style tracker for action items across post-mortems |
| `assets/what_went_well_prompts.md` | 20+ prompts to draw out positive observations |
| `references/blameless-culture-guide.md` | Deep dive on blameless principles, with examples of blameful vs blameless phrasing |
| `references/5-whys-vs-causal-tree.md` | When to use each method, with worked examples |

## references/red-flags.md

# Red Flags: Post-Mortem

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the draft post-mortem and the action-item tracker before publishing or signing off. Each red flag shows the *bad* version next to the *good* version, anchored to Google SRE practice, John Allspaw's blameless tradition, Charles Perrow's Normal Accident Theory, and Sidney Dekker's *Field Guide to Understanding Human Error*.

---

## Red Flag 1: Blame language

**Symptom.** Narrative says "Sarah should have caught this" or "the team failed to deploy properly" or "if only the engineer had…".

**Why it's bad.** Blame language breaks the central premise of blameless review. Once people read their name attached to "should have", psychological safety collapses for the next incident. Engineers sanitize their narrative; the document loses learning value. Worse, it makes the discipline counterproductive.

**Bad example:**
> "At 14:08, Sarah should have noticed the queue depth alert and acted. She missed it because she was focused on her ticket. The on-call engineer failed to follow runbook step 3."

**Good example:**
> "At 14:08, queue depth had crossed the alert threshold but the dashboard did not surface this prominently — the on-call engineer was triaging a separate incident on the same dashboard. The runbook's step 3 references a tool that has been renamed; the engineer searched for the old name and did not find it."

**How to catch it.** Search the document for: "should have", "could have", "failed to", "if only", "did not". Replace each with a system property the team can change.

---

## Red Flag 2: Action items without owners

**Symptom.** Action items section lists 8 bullets: "Improve monitoring", "Update runbook", "Add tests". No names, no dates, no tracker tickets.

**Why it's bad.** Action items without owners do not get built. Industry data shows ~50% of post-mortem action items are never completed; the absence of owners is the most common reason. The post-mortem becomes a learning artifact with no follow-through.

**Bad example:**
> "Action items:
> • Improve monitoring on the queue
> • Update the runbook
> • Add integration tests for the error path"

**Good example:**
> "Action items:
> | # | Item | Owner | Due | Ticket | Category |
> | 1 | Add PagerDuty alert on queue depth > 5,000 with page to #payments-oncall | Tomas R | 2026-06-05 | ENG-2041 | Detect |
> | 2 | Update runbook step 3 to reference new tool name; add quick-link | Priya N | 2026-05-29 | DOC-104 | Respond |
> | 3 | Add integration test exercising connection-pool exhaustion path | Sarah K | 2026-06-12 | ENG-2042 | Prevent |"

**How to catch it.** Read each action item. Does it have: (1) one named owner, (2) a date, (3) a tracker ticket ID? Missing any = will not happen.

---

## Red Flag 3: Single "root cause" stops the analysis

**Symptom.** Post-mortem declares one root cause ("the connection pool was exhausted") and proposes one fix. No discussion of contributing factors.

**Why it's bad.** Charles Perrow's Normal Accident Theory: in tightly-coupled complex systems, there is rarely a single cause. The incident emerged from contributing factors aligning. A single-root analysis misses the other contributing factors; those factors will produce the next incident.

**Bad example:**
> "Root cause: connection pool was exhausted by a leaky batch job. Fix: add connection cleanup to the batch job. (Section ends.)"

**Good example:**
> "Contributing factors:
> 1. Connection pool exhausted (mechanical cause).
> 2. Pool size set conservatively for cost reasons; capacity planning predates current traffic shape.
> 3. Alert fired late — threshold at 95% with no 80% warn.
> 4. PagerDuty escalation path stale — primary owner rotated 6 weeks ago.
> 5. Runbook missing pool-restart command; on-call had not shadowed a database incident.
> Action items address each factor (see action item table). Allspaw's framing: 'the set of contributing factors that aligned' is the answer to 'what caused this'."

**How to catch it.** Does the analysis section name multiple contributing factors? Single-cause analysis is incomplete.

---

## Red Flag 4: Second-mortem (same incident class recurs)

**Symptom.** This is the third connection-pool-exhaustion incident in 8 months. Each had a post-mortem. Each named a different root cause.

**Why it's bad.** Recurring incidents in the same class mean previous post-mortems treated symptoms, not contributing factors — or action items from previous post-mortems were never completed. The team is paying the incident cost repeatedly without compounding learning.

**Bad example:**
> "Sept 2025: connection-pool incident. PM: 'fix the leak.' Done.
> Jan 2026: connection-pool incident. PM: 'fix the new leak.' Done.
> May 2026: connection-pool incident. PM: 'fix that other leak.' Done.
> (No structural learning across the three.)"

**Good example:**
> "This is the third connection-pool incident in 8 months. Pre-meeting audit: of 12 action items from prior 2 post-mortems, 6 are unfilled. The recurrence is a both-and: action items not built, and structural factor (pool sizing + alerting + runbook) not addressed across instances. New analysis treats this as a pattern, not a single incident. Action items: (1) finish the 6 outstanding items from prior post-mortems; (2) structural: convert from fixed-size pool to dynamic with auto-scaling; (3) process: monthly review of connection-pool metrics."

**How to catch it.** Search the team's post-mortem archive for the failure class. > 2 occurrences in 12 months = the prior post-mortems missed the structural issue.

---

## Red Flag 5: "What went well" section empty

**Symptom.** Post-mortem has Timeline, What Went Wrong, Root Cause, and Action Items. "What went well" is missing or has one bullet.

**Why it's bad.** What-went-well is the section most often skipped under time pressure. It anchors the post-mortem in learning, not blame. It also surfaces practices worth replicating — incident-response actions that reduced impact. Skipping it means losing half the learning.

**Bad example:**
> "What went well:
> (empty)
> What went wrong:
> (8 detailed bullets)"

**Good example:**
> "What went well (using `assets/what_went_well_prompts.md`):
> 1. Detection: monitoring caught the error spike within 4 minutes of onset.
> 2. Incident commander designation: clear within 6 minutes; war room opened in Slack.
> 3. Customer comms: status page updated within 15 minutes; CS team had macros within 20 minutes.
> 4. Mitigation: kill-switch flipped within 12 minutes of decision; effective.
> 5. Engineering collaboration: 3 teams contributed without coordination friction.
> 6. Documentation: timeline captured live in Slack, easy to reconstruct.
> 7. Tone: blameless ground rules from the start of the meeting; nobody got defensive.
> (These practices are now standards in the incident-response runbook.)"

**How to catch it.** Count items in What Went Well. < 3 = the section was rushed; use the prompts file to expand.

---

## Red Flag 6: Counterfactuals in the root-cause analysis

**Symptom.** Analysis says "If only the engineer had checked the dashboard at 14:05, this would have been caught earlier."

**Why it's bad.** Counterfactuals are wishes, not causes. They cannot be acted on (you cannot retroactively change what someone did). They also signal hindsight bias: what is obvious now was not obvious then. Dekker's framing: replace counterfactuals with system properties.

**Bad example:**
> "If the engineer had escalated immediately, we would have caught this. If only the rollout had been slower, the bug would have surfaced in canary."

**Good example:**
> "At 14:05, the dashboard did not show queue depth above the fold; the engineer was working on an unrelated incident on the same dashboard and did not see the queue widget. (Action item 1: surface queue depth above the fold on the on-call dashboard.) The canary stage was 5%; this bug requires concurrent batch jobs to manifest, which only triggers at higher traffic. (Action item 2: extend canary duration to 24h to cover the next batch-job interval.)"

**How to catch it.** Search for: "if only", "if X had", "would have", "should have", "could have been". Each is a counterfactual.

---

## Red Flag 7: Named individuals in the narrative

**Symptom.** Narrative uses "Sarah", "Tomas", "Priya" throughout. Engineers feel exposed; one quietly asks to leave the team.

**Why it's bad.** Names in the narrative undermine blameless culture. Even when phrased neutrally, naming an individual associates them with the incident in the searchable archive. Future managers will find it. Engineers learn to hide details to avoid future naming.

**Bad example:**
> "Timeline: 14:03 Sarah deploys the batch-job refactor. 14:07 Tomas notices the error rate. 14:10 Priya checks the runbook."

**Good example:**
> "Timeline: 14:03 the batch-job refactor deploys (PR #2042). 14:07 the on-call engineer notices the error rate via PagerDuty. 14:10 the second on-call engineer checks the runbook. (Names appear only in the Contacts table at the top and the Action Item owner column at the bottom.)"

**How to catch it.** Search the narrative for any first name. If present and the post-mortem is blameless, refactor to roles.

---

## Red Flag 8: Severity downgraded after the fact

**Symptom.** Incident was declared Sev 1 during response. Three days later, post-mortem reads "Sev 3, contained, minor customer impact".

**Why it's bad.** Severity revision downward after-the-fact looks like minimizing. It also bypasses the post-mortem SLA (Sev 1 = 5 business days; Sev 3 = optional). Engineers learn to lobby for downgrades; the discipline of consistent severity erodes.

**Bad example:**
> "Initial declaration: Sev 1. Post-mortem heading: Sev 3. Reason in line 4: 'turned out to be less impactful than we thought.'"

**Good example:**
> "Severity: Sev 1 (confirmed at incident close).
> Initial declaration: Sev 1.
> Final classification: Sev 1.
> Customer impact: 22 minutes of 500 errors on the /search endpoint; 12,400 affected sessions; 6 paid-customer escalations.
> SLA: post-mortem published within 5 business days of incident close — met (4 days)."

**How to catch it.** Compare incident-open severity to post-mortem severity. Downward revisions need explicit explanation (and rarely happen — usually upward).

---

## Red Flag 9: Generic "improve X" action items

**Symptom.** Action item: "Improve monitoring". Owner: TBD. Due: TBD.

**Why it's bad.** Unspecific action items are unimplementable. "Improve monitoring" cannot be marked done; "add an alert on queue depth > 5,000 with PagerDuty page to #payments-oncall" can. Vague items inflate the action-item count without producing improvement.

**Bad example:**
> "Action items:
> • Improve monitoring
> • Update runbook
> • Better tests
> • Train the team"

**Good example:**
> "Action items (testable acceptance criteria):
> 1. Add Datadog alert: queue_depth > 5000 sustained 5 min, paging #payments-oncall. Test: simulate threshold in staging; alert fires. Owner: Tomas R. Due: Jun 5. Ticket ENG-2041.
> 2. Replace 'restart_pool' command in runbook section 7 with 'kubectl rollout restart deployment payments-svc'. Verify by walking the runbook in a non-prod incident drill. Owner: Priya N. Due: May 29. Ticket DOC-104.
> 3. Add integration test exercising connection-pool exhaustion. Test scope: 200 concurrent batch jobs against a 50-connection pool; expect graceful degradation, not crash. Owner: Sarah K. Due: Jun 12. Ticket ENG-2042."

**How to catch it.** For each action item, ask: "what is the testable acceptance criterion?" If absent, the item is not implementable.

---

## Red Flag 10: Post-mortem becomes a sweeping retrospective

**Symptom.** Document started about a 22-minute incident. Now it covers 6 unrelated org issues, 3 hiring concerns, and a 2-page essay on engineering culture.

**Why it's bad.** Sweeping post-mortems lose focus and never publish. The specific learning from the specific incident gets diluted. Adjacent topics deserve their own retrospectives; mixing them produces document paralysis.

**Bad example:**
> "Post-mortem draft (week 3 of writing): 18 pages. Covers: the 22-minute incident, broader on-call burden, hiring backlog in SRE, the new team's onboarding gaps, last quarter's reorg, and a section titled 'culture observations'."

**Good example:**
> "Post-mortem strictly scoped to this incident. 4 pages. Adjacent themes the author noticed during interviews:
> • On-call burden — surface in next sprint retro
> • SRE hiring backlog — escalate to Eng Director separately
> • Onboarding gaps — propose a topic for the team's monthly engineering review
> Each spun off as its own work item; not in this post-mortem."

**How to catch it.** Post-mortem length. > 8 pages for a routine incident = scope creep. Compress or split.

---

## Red Flag 11: Allspaw test failure

**Symptom.** Author writes the post-mortem; doesn't ask whether the engineers in it would feel fairly represented. Three engineers separately complain in 1:1s after publication.

**Why it's bad.** Allspaw test failure is silent in the document but loud in the team. Engineers stop participating fully in future post-mortems. Future authors get sanitized narratives. The discipline degrades over months without any single visible breakdown.

**Bad example:**
> "PM publishes the post-mortem at 17:00 Friday. Sunday: two engineers DM the manager: 'I don't think the timeline represents what actually happened. It makes it look like I was the cause.'"

**Good example:**
> "Pre-publish step: Allspaw test. Author sends draft to each engineer named in the Contacts table or referenced in the timeline (by role). Question: 'does this fairly represent your experience? If not, what should change?' Wait for response or explicit OK before publishing. Of last 8 post-mortems: 3 went through revision after Allspaw test surfaced an issue. The test is a normal pre-publish gate."

**How to catch it.** Has the Allspaw test been run? If no, run it before publishing.

---

## Red Flag 12: Action-item completion not audited

**Symptom.** Post-mortem published with 9 action items. 6 months later, audit reveals: 4 completed, 3 in-progress, 2 unfilled (never tracker ticketed). Same class of incident recurs.

**Why it's bad.** Unaudited action items become "we wrote it down" theater. The team feels productive after the post-mortem and then doesn't follow through. Industry baseline of 50% completion is the result of no audit; teams with audit hit 80-90%.

**Bad example:**
> "9 action items filed. Nobody tracks completion. 6 months later, no one knows the status of most."

**Good example:**
> "Action-item audit cadence (in `assets/action_item_tracker.md`):
> Weekly: each action item owner reports status at engineering review.
> Monthly: cross-incident audit — completion rate target >= 80% at 30 days.
> Quarterly: full audit of last quarter's post-mortems; completion rate is a tracked engineering metric.
> 90-day target: >= 90% completion.
> Any item slipping past due date is escalated to the EM, who decides: accelerate, defer with rationale, or accept and document the residual risk."

**How to catch it.** Open any post-mortem from > 60 days ago. Pull the action items. What % are complete?

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Blame language | Search for: should have, could have, failed to, if only |
| 2 | Action items without owners | Each item: owner + date + ticket ID? |
| 3 | Single root cause | Are multiple contributing factors named? |
| 4 | Second-mortem | Has this class of incident recurred in the archive? |
| 5 | What-went-well empty | Count items: < 3 = rushed |
| 6 | Counterfactuals | Search for: if only, would have, should have |
| 7 | Named individuals in narrative | Search for any first name |
| 8 | Severity downgraded after the fact | Compare incident-open vs post-mortem severity |
| 9 | Generic "improve X" action items | What is the testable acceptance criterion? |
| 10 | Post-mortem as sweeping retrospective | Document length > 8 pages? |
| 11 | Allspaw test failure | Has the draft been Allspaw-tested? |
| 12 | Action-item completion not audited | What % of items from > 60 days ago are complete? |

## Related Reading

- SKILL.md Troubleshooting
- references/blameless-culture-guide.md
- references/5-whys-vs-causal-tree.md
- Google SRE Book, "Postmortem Culture: Learning from Failure"
- John Allspaw, "Blameless PostMortems and a Just Culture" (2012)
- Richard Cook, "How Complex Systems Fail" (1998)
- Charles Perrow, *Normal Accidents* (1984)
- Sidney Dekker, *The Field Guide to Understanding Human Error* (3rd ed., 2014)
- Sidney Dekker, *Just Culture* (3rd ed., 2017)
- `discovery/pre-mortem/` (pre-mortem before incidents; post-mortem after)
- `daci-framework/` (action item owner assignment)

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| Post-mortem feels blameful despite no names | Counterfactuals ("if only", "should have") embedded in narrative | Search the document for "should", "could have", "if only"; rewrite each as a system property the team can change |
| Action items never get completed | No single owner, no tracker ticket, or no recurring review | Each item must have one named owner and a real Jira/Linear ticket; review completion in weekly engineering ops |
| Same incident class recurs | First post-mortem identified a symptom, not contributing factors; or contributing-factor action items were dropped | Re-run with Causal Tree instead of 5 Whys; audit what action items from the prior post-mortem were filed but not completed |
| Team avoids difficult observations | Psychological safety low; managers in the room creating power dynamics | Run an anonymous pre-meeting survey; consider a facilitator outside the team; separate post-mortems from performance reviews explicitly |
| Post-mortem takes more than 2 weeks to publish | Author has competing priorities or scope crept into a sweeping retrospective | Set a hard "first draft within 3 business days" rule; cut anything not directly tied to this incident; spin off broader themes into a separate retrospective |
| Executives push for a single root cause | Cultural expectation of accountability framed as blame | Educate using Normal Accident Theory framing; provide the contributing-factor list as the answer to "what caused this"; offer one-line summary that lists top 3 contributing factors |
| "What went well" section is empty | Author skipped the section under time pressure, or team culture undervalues positive observations | Use `assets/what_went_well_prompts.md`; require minimum 3 items before publishing; surface positives in distribution channels |

## Success Criteria

- Every Sev 0 / Sev 1 / Sev 2 incident has a post-mortem published within the SLA window (5 / 5 / 7 business days)
- 100% of post-mortems pass the Allspaw test ("would I send this to the engineer who pushed the button?")
- Each post-mortem has at least one item in "What went well" (minimum 3 preferred)
- Every action item has a named owner, a tracker ticket, and a due date
- Post-mortem action-item 30-day completion rate >= 70%; 90-day completion rate >= 90%
- Recurring incident classes (same failure mode within 90 days) decrease quarter over quarter
- New engineers can find post-mortems for their service within 5 minutes of starting
- Post-mortems are explicitly disconnected from performance review processes; no engineer has ever been disciplined as a direct result of a post-mortem narrative

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/post-mortem
