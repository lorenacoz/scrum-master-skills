---
description: "Plans releases, picks deployment strategies, runs incidents and tracks DORA metrics and error budgets. Use when preparing a Go/No-Go, choosing canary or blue-green, handling a production incident or reporting delivery health."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Delivery Manager

The agent acts as an expert delivery manager coordinating continuous software delivery. It plans releases, selects deployment strategies, manages incidents, evaluates change requests, and tracks SLA compliance with error budget calculations.

## Core Capabilities

- **Delivery maturity assessment** — locate the team on a 5-level scale (Manual → DevOps Excellence) and target one level at a time.
- **Release planning** — scope, exit criteria, rollout strategy, and a T-7/T-1/T-0/T+1 communication plan; Go/No-Go requires all exit criteria met.
- **Deployment strategy** — blue-green, canary, rolling, big-bang selection with matching rollback paths and canary success thresholds.
- **Incident response** — DETECT→TRIAGE→RESPOND→RESOLVE→REVIEW with SEV-1–SEV-4 severity, response times, and mandatory post-mortems.
- **Change & SLA governance** — CAB/Standard/Expedited/Emergency change types, SLA/error-budget burn-rate tracking, and DORA metrics.

## When to Use

- Planning a release and running a Go/No-Go against exit criteria
- Choosing a deployment strategy and its rollback plan
- Responding to a production incident or running a post-mortem
- Evaluating a change request or calculating SLA/error-budget burn
- Assessing delivery maturity or interpreting DORA metrics

## Clarify First

Before generating the plan or report, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Which task:** release readiness/Go-No-Go, deployment strategy, incident response, or SLA/error-budget tracking (each is a different workflow and artifact).
- **Exit criteria or SLA target:** the bar the release or service is measured against (Go/No-Go requires all criteria met; SLA math needs the target).
- **Deployment strategy:** blue-green, canary, rolling, or big-bang, when shipping (sets the rollout gates and rollback path).
- **Incident severity:** SEV-1 through SEV-4, when responding (sets response time, escalation, and whether a post-mortem is mandatory).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Settle the Clarify First inputs; each task maps to one reference below.
2. Measure first: run the matching tool on the team's own export (deployments, dependencies or risks).
3. Build the artifact from the reference (release plan, rollout and rollback, incident timeline, budget burn).
4. Done when Go/No-Go checks every exit criterion against evidence, every rollback path has a rehearsal date, and every DORA figure shows its sample size.

## Tools

Each tool reads one JSON file and prints a text report (`--json` for machine output).
`--example` prints the input shape; samples ship in `assets/`. Exit 0 on success, 2 on bad
input (missing file, invalid JSON, wrong shape) with a one-line error.

```bash
python3 scripts/delivery_metrics_tracker.py --data assets/sample_delivery.json --period 30
python3 scripts/dependency_mapper.py --deps assets/sample_dependencies.json
python3 scripts/risk_register.py --risks assets/sample_risks.json
```

| Tool | What it does |
|------|--------------|
| `delivery_metrics_tracker.py` | Deployment frequency, change lead time, change fail rate and failed-deployment recovery time against the 2024 DORA levels, plus rework rate when deploys carry `"rework": true`. The `--period` window ends at the file's `as_of`, else its latest deploy or incident, so a fixed export gives a fixed answer. A tier needs a minimum sample: 5 deploys for lead time and change fail rate (below that one failure moves the rate by 20+ points), 2 incidents for recovery time, and 5 deploys or a 28+ day window for frequency. Below it the metric reads "Insufficient data" and is left out of the overall level; with none classified, the overall level is "Insufficient data" too |
| `dependency_mapper.py` | Delivery order (each dependency before what needs it), cycles, bottlenecks, high-risk and unowned dependencies. Edges are `{"from": dependent, "to": dependency}` |
| `risk_register.py` | Probability x impact scores, severity, residual exposure after mitigation, unowned high risks |

## Anti-Patterns

### Rollback plan never rehearsed
**Mistake:** The release plan documents a rollback procedure that has never been run in production-like conditions.
**Why it happens:** Writing the steps feels like enough, and rehearsal takes time from the release.
**Instead:** Rehearse the rollback at least every 90 days and measure how long it takes. If it hasn't been rehearsed, treat the rollback path as theoretical in the Go/No-Go.

### Error budget that never bites
**Mistake:** The team has SLOs and an error budget but keeps shipping features when the budget is burned.
**Why it happens:** Roadmap pressure wins the argument every time the budget runs out.
**Instead:** Agree the consequence before the budget burns: feature freeze until reliability work restores it. Track burn rate with the SLA/error-budget workflow. If feature work has never paused for a burned budget, the budget is decoration.

### Severity that doesn't match the criteria
**Mistake:** Minor issues get logged as SEV-1, or real outages stay at SEV-3 to avoid the paperwork.
**Why it happens:** Severity drives response time and post-mortem duty, so people bend it up or down.
**Instead:** Classify against the documented SEV-1 to SEV-4 criteria. Sample 10 recent SEV-1s. If fewer than 80% meet the criteria, fix the classification before you trust the dashboard.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

- `references/release_process.md` -- Delivery maturity levels, release planning + exit criteria, change-request types, the release-readiness example, DORA metrics, cross-skill integration, troubleshooting, and success criteria. Read when planning a release or improving the pipeline.
- `references/deployment_patterns.md` -- Blue-green, canary, rolling, and big-bang strategies with rollback paths and canary stage thresholds. Read when selecting how to ship.
- `references/incident_management.md` -- Severity matrix (SEV-1–SEV-4), the 5-step incident workflow, and post-mortem requirements. Read during incident triage and response.
- `references/sla_management.md` -- SLA framework, error-budget calculation example, and burn-rate freeze thresholds. Read when tracking reliability budgets.
- `references/red-flags.md` -- Bad-vs-good examples of delivery-management output. Read this to review a release/incident plan before committing to it.
- `references/ai-assisted-delivery.md` -- What DORA's 2024 and 2025 research says about AI assistants and delivery stability, and what to track. Read when AI tooling is changing throughput or review load.

## Scope & Limitations

**In Scope:** Release planning and readiness assessment, deployment strategy selection and coordination, incident response process management, change request evaluation, SLA/error budget tracking, DORA metrics monitoring, post-mortem facilitation, delivery maturity assessment.

**Out of Scope:** Infrastructure provisioning and CI/CD pipeline engineering (hand off to DevOps/SRE), sprint-level planning and backlog management (hand off to `scrum-master/`), strategic program governance (hand off to `program-manager/`), feature prioritization and roadmapping (hand off to `senior-pm/`).

**Limitations:** Error budget calculations assume accurate incident duration tracking -- manual time entry introduces measurement error. Deployment strategies (blue-green, canary) require infrastructure support that the delivery manager recommends but does not implement. DORA metrics are trailing indicators; improvement requires upstream changes in engineering practices.

## Files

| File | Purpose |
|------|---------|
| `scripts/delivery_metrics_tracker.py`, `scripts/dependency_mapper.py`, `scripts/risk_register.py` | See Tools |
| `assets/sample_delivery.json`, `assets/sample_dependencies.json`, `assets/sample_risks.json` | Runnable inputs for each tool |
| `references/*.md` | See References |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/ai-assisted-delivery.md

# AI-Assisted Delivery

Read when AI coding assistants are changing throughput, review load or stability.


AI coding assistants change the shape of the delivery pipeline: more code arrives faster, and the constraint moves to review, testing, and recovery. What DORA's research says (as of September 2026):

- **2024 report:** every 25% increase in AI adoption was associated with an estimated 1.5% reduction in delivery throughput and 7.2% reduction in delivery stability, even as documentation quality, code quality, and review speed improved ([2024 report](https://dora.dev/research/2024/dora-report/)).
- **2025 report ("State of AI-assisted Software Development"):** 90% of respondents use AI at work and more than 80% believe it has raised their productivity, while 30% report little or no trust in AI-generated code. AI adoption now shows a positive relationship with throughput but still a negative one with stability. DORA's framing is that AI is an amplifier of an organization's existing strengths and weaknesses ([announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).
- **DORA AI Capabilities Model** (2025): seven capabilities that amplify AI's benefit: clear and communicated AI stance, healthy data ecosystems, AI-accessible internal data, strong version control practices, working in small batches, user-centric focus, and quality internal platforms ([dora.dev](https://dora.dev/ai/capabilities-model/report/)).
- **Team profiles:** the 2025 report groups teams into seven profiles (for example "foundational challenges", "legacy bottleneck", "harmonious high achievers") rather than leading with the Elite-to-Low levels. Use the profile to find the constraint before rolling out more AI tooling.

What to do as a delivery manager:

1. **Track instability, not just speed.** Report change fail rate and deployment rework rate (`delivery_metrics_tracker.py`, `"rework": true` on unplanned fix deploys) next to deployment frequency. Rising throughput with rising rework is the AI failure mode DORA describes.
2. **Measure review load.** PR count per reviewer, review wait time, and PR size. AI-generated volume that outruns review capacity shows up as longer lead time or weaker review, not as faster delivery.
3. **Keep batches small.** Hold PR size and release scope limits regardless of how fast code is produced; small batches are both a DORA capability and the main guard against AI-driven instability.
4. **Guard stability explicitly.** Canary or feature-flag every AI-heavy change set, keep rollback rehearsed, and treat a rising rework rate as a trigger to slow intake, not to add more AI.
5. **Keep a human accountable.** Every change, AI-assisted or not, has a named human owner who meets the same Definition of Done and review bar.

## references/deployment_patterns.md

# Deployment Patterns: Blue-Green, Canary, Rolling

Read this when selecting a deployment strategy and defining its rollback path and canary success thresholds. Moved verbatim from `SKILL.md`.

## Select Deployment Strategy

| Strategy | When to Use | Rollback Speed | Risk Level |
|----------|------------|----------------|------------|
| **Blue-Green** | Need instant rollback, have 2x infrastructure | Instant (switch traffic) | Low |
| **Canary** | Want to validate with subset of users first | Fast (stop traffic shift) | Low-Medium |
| **Rolling** | Cost-constrained, can tolerate mixed versions | Moderate (re-deploy old) | Medium |
| **Big Bang** | Small app, low traffic, maintenance window OK | Slow (full redeploy) | High |

**Blue-Green deployment:**
```
Load Balancer -> [BLUE v2.4 - Active] | [GREEN v2.5 - Staging]
SWITCH: Route traffic Blue -> Green
ROLLBACK: Route traffic Green -> Blue (instant)
```

**Canary deployment progression:**
```
Stage 1: 95% old / 5% new   -- Monitor for 30 min
Stage 2: 75% old / 25% new  -- Monitor for 1 hour
Stage 3: 50% old / 50% new  -- Monitor for 2 hours
Stage 4: 0% old / 100% new  -- Full rollout
```

**Validation checkpoint:** At each canary stage, check error rate (<1%), latency P99 (<threshold), and health checks. Any breach halts progression and triggers rollback.

## references/incident_management.md

# Incident Management: Severity, Response & Post-Mortem

Read this when triaging or coordinating a production incident, or defining the severity and response-time policy. Moved verbatim from `SKILL.md`.

## Manage Incidents

The agent follows the DETECT -> TRIAGE -> RESPOND -> RESOLVE -> REVIEW process:

**Severity levels:**

| Severity | Criteria | Response Time | Resolution Target |
|----------|----------|--------------|-------------------|
| SEV-1 | Complete outage or data loss | 15 minutes | 4 hours |
| SEV-2 | Major feature unavailable | 30 minutes | 8 hours |
| SEV-3 | Minor feature impact, workaround available | 2 hours | 24 hours |
| SEV-4 | Cosmetic, no customer impact | 8 hours | 5 days |

**Incident workflow:**
1. **Detect** -- Alert fires, monitoring triggers, user reports
2. **Triage** -- Assess severity, assign incident commander, notify stakeholders
3. **Respond** -- Incident commander coordinates, communicate status every 30 min (SEV-1/2)
4. **Resolve** -- Deploy fix, verify restoration, confirm with monitoring
5. **Review** -- Post-mortem within 48 hours, document timeline, root cause, action items

**Validation checkpoint:** Every SEV-1/SEV-2 incident must produce a post-mortem with action items, owners, and due dates.

## references/red-flags.md

# Red Flags: Delivery Manager

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them. Pair with the SKILL.md and Troubleshooting table.

## How to use this document

When you have just produced a release plan, incident response, change-request evaluation, or maturity assessment, scan the red flags below. Each red flag shows a *bad* and *good* version.

---

## Red Flag 1: Blame-Seeking Incident Handling

**Symptom.** Post-incident review focuses on "who did this" — naming individuals, assigning fault. Quiet rooms, defensive language, no candid contributions.

**Why it's bad.** Blame culture destroys reporting. Engineers stop flagging near-misses; small problems compound into outages. Allspaw's blameless post-mortem framing exists because the alternative empirically reduces safety. Naming a culprit is satisfying and counter-productive.

**Bad example:**
> Post-incident: "Raj deployed without proper review. Action: written warning. Lessons: be more careful."

**Good example:**
> Post-incident: "The deployment passed our review gate but our review gate did not catch the missing config flag. Root cause: review checklist did not include config-flag verification for canary deploys. Action: update checklist + add automated check. Raj's deploy followed our process; the process needs work."

**How to catch it.** Read the post-mortem. Does it name an individual as the cause? If yes, the framing is unsafe.

---

## Red Flag 2: Missing Rollback Rehearsal

**Symptom.** Release plan documents a rollback procedure, but the procedure has never been tested in production-like conditions.

**Why it's bad.** Untested rollback procedures fail when needed. The 3am incident is not the time to discover that the rollback script depends on a tool no one has installed, or that the database migration is not reversible. Maturity Level 4-5 requires rehearsed rollback.

**Bad example:**
> Release plan: "Rollback: revert deploy via Jenkins. DB migration is forward-only; data recovery via backup if needed."

**Good example:**
> Release plan: "Rollback procedure tested in staging on 2026-05-15 (signed off by EM + on-call). Migration designed as expand-contract: new columns added in week 1, code switches to new columns in week 2, old columns removed in week 3 — fully rollback-safe at each step. Rollback target time: 15 min p50, 30 min p95."

**How to catch it.** Has the rollback been rehearsed in the last 90 days, with measured target time? If not, the plan is theoretical.

---

## Red Flag 3: Error Budget Treated as Reliability Theater

**Symptom.** Team has SLOs and an "error budget" but never actually slows feature work when the budget is burned.

**Why it's bad.** The point of error budgets is to create an automatic tension between reliability and feature velocity. Budgets that never bite are decorative. Maturity Level 4-5 organizations enforce budget consequences: when burned, feature freeze until reliability work restores it.

**Bad example:**
> SLO: 99.9% uptime. Budget for the month: 43 min. Actual downtime: 4 hours. Action: noted in monthly report, continued feature work."

**Good example:**
> SLO: 99.9% uptime. Budget: 43 min/month. Actual: 4 hours (budget exceeded by 5x). Action triggered by policy: feature work paused, 100% of capacity to reliability for 2 weeks. Restoration plan: 3 named items, ETA documented. Restart criteria: budget restored to <50% consumption for 30 days."

**How to catch it.** Has your team ever paused feature work because the error budget was burned? If never, the budget is decorative.

---

## Red Flag 4: Deployment Strategy Mismatch

**Symptom.** Team uses blue-green deployment for a high-traffic, stateful service where canary would surface bugs earlier. Or rolling deployment for a service where blast-radius needs full isolation.

**Why it's bad.** Each strategy has a profile: blue-green = fast switch, double infrastructure cost, hard for stateful; canary = gradual exposure, slow validation, requires monitoring sophistication; rolling = simple, partial exposure during rollout. Mismatched strategy produces either (a) bigger blast radius than necessary or (b) unnecessary cost.

**Bad example:**
> "We use blue-green for everything." (One service has 200 GB of stateful in-memory cache; blue-green requires warming the green environment for 90 min before switch.)

**Good example:**
> "Deployment strategy per service: stateless APIs use rolling (simple, fast). Customer-facing UI uses canary (5% -> 25% -> 100% over 4 hours, with auto-rollback on error-rate spike). Stateful cache service uses blue-green with pre-warming. Documented per-service in runbook."

**How to catch it.** Can you justify the deployment strategy per service? If not, you are using one strategy for everything.

---

## Red Flag 5: Communication Plan Missing T-7/T-1/T+1

**Symptom.** Release plan covers T-0 (the deploy itself) but no pre-deploy comms, no go/no-go gate, no post-deploy follow-up.

**Why it's bad.** Surprises break trust with stakeholders. A release that ships without T-7 scope-finalization and T-1 go/no-go feels chaotic to support, sales, and customer-facing teams. A release without T+1 follow-up leaves customers and stakeholders wondering whether it landed safely.

**Bad example:**
> Release plan: "Deploy v2.5.0 on Tuesday at 10am. Slack post when done."

**Good example:**
> Release plan: "T-7 (Tue prior): scope frozen, release notes drafted, internal preview posted. T-1 (Mon): go/no-go meeting at 4pm with eng, product, support, marketing. Owner has authority to delay. T-0 (Tue 10am): deploy, monitoring on, status updates every 30 min in #release. T+1 (Wed): customer comms (changelog, release email if customer-facing), retro scheduled for following week."

**How to catch it.** Does the plan cover all four checkpoints? Missing any is a process gap.

---

## Red Flag 6: Change Advisory Board (CAB) as Rubber Stamp

**Symptom.** CAB meets weekly, approves every change request in <2 minutes per request, never blocks or modifies a change. Or, CAB blocks every change, becoming a velocity tax.

**Why it's bad.** Both ends are anti-patterns. A rubber-stamp CAB is bureaucratic theater — it adds delay without adding safety. A blocking CAB is risk-averse paranoia — it slows the org without proportionate risk reduction. Healthy CABs are *exceptions-based*: standard changes auto-approve, only high-risk changes need real review.

**Bad example:**
> CAB approves 100% of 47 requests this month, average 90 seconds per request.

**Good example:**
> Change taxonomy: Standard (pre-approved, automated, no CAB) = 80% of changes. Normal (CAB review) = 18%. Major (executive review + customer comm) = 2%. CAB only sees 'Normal' and 'Major' — about 10 requests per month, each with a real review. Standard changes flow through CI/CD."

**How to catch it.** What % of changes does CAB see? If above 50%, the taxonomy is broken. If 100% approved, the review is fake.

---

## Red Flag 7: Incident Severity Inflation or Deflation

**Symptom.** Every minor issue gets logged as Sev-1 (inflation), or genuine outages stay at Sev-3 (deflation) because higher severity triggers paperwork.

**Why it's bad.** Severity inflation desensitizes the team — "another Sev-1, ignore the page." Severity deflation hides real problems — customers experience outages while the dashboard says "green." Both produce wrong investment in reliability.

**Bad example:**
> Last 30 days: 42 Sev-1 incidents declared. 38 were minor support tickets escalated by frustrated users.

**Good example:**
> Severity rubric documented: Sev-1 = >5% of customers impacted, revenue impact, or data loss. Sev-2 = degradation affecting >1% customers. Sev-3 = isolated. Quarterly severity review by senior on-call to recalibrate. Sev-1 rate stable at 1-3 per month."

**How to catch it.** Sample 10 recent Sev-1 declarations. How many actually meet the documented criteria? Below 80% match means severity is misused.

---

## Red Flag 8: Runbook That No One Has Run Recently

**Symptom.** Runbook for database failover, dated 2022, never tested. When the failover is needed, half the commands fail because the tool changed.

**Why it's bad.** Runbooks rot faster than code. A runbook untested in 6+ months should be treated as fiction. The fix is game-day exercises — scheduled runbook executions on staging or production with safety net.

**Bad example:**
> "We have a comprehensive runbook for database failover." (Last executed 2022. Tools referenced are deprecated.)

**Good example:**
> "Quarterly game-day: rotation of critical runbooks tested by on-call engineer in staging or controlled production. Last database-failover game-day: 2026-04-10, all steps executed, 3 commands updated, runtime measured (12 min vs 18 min target). Runbook freshness tracked per item."

**How to catch it.** For your top 5 critical runbooks, when were they last executed end-to-end? If any over 6 months, that runbook is suspect.

---

## Red Flag 9: Feature Flags Used Without Cleanup

**Symptom.** Codebase has 400+ feature flags, half of them set to 100% on for 2+ years. Conditional logic everywhere, nobody knows which flags are still meaningful.

**Why it's bad.** Feature flag debt is real debt. Every flag is conditional complexity, a potential bug surface, and a cognitive tax on engineers. The discipline is flag-with-end-date.

**Bad example:**
> Feature flag inventory: 412 flags. 187 at 100% on for >18 months. 23 at 0% with no documentation on why.

**Good example:**
> Flag policy: every flag has an owner, a creation date, and a target sunset date. Monthly flag-cleanup ritual: flags past sunset date either removed or re-justified. Current inventory: 41 flags, all under 6 months old or actively managed."

**How to catch it.** How many flags are over 12 months old? If above 20, you have flag debt.

---

## Red Flag 10: Deploy Frequency Without Lead Time

**Symptom.** Team reports "we deploy 50 times per week" but lead time from commit to production is 8 days.

**Why it's bad.** Deploy frequency without lead time hides the real bottleneck. DORA's metrics work together: deployment frequency, change lead time, change fail rate, failed deployment recovery time (formerly MTTR), and, since the 2024 report, deployment rework rate. Reporting one without the others paints a misleading picture.

**Bad example:**
> Quarterly delivery report: "Deployments: 287 (industry-leading). Reliability: high."

**Good example:**
> Quarterly delivery report (DORA): Deploys per week = 50, lead time p50 = 8 days (target 3), change failure rate = 12% (target <15%), failed deployment recovery time = 42 min (target <60), rework rate = 6% of deploys. Improvement area: lead time — root cause is review queue depth, action plan in place."

**How to catch it.** Does your delivery report show all the DORA metrics (the classic four, plus rework rate if you track it)? If not, one or more is being hidden.

---

## Red Flag 11: SLA Promises Without Capacity to Meet Them

**Symptom.** Sales promises 99.99% uptime in customer contracts. Engineering has not staffed for that SLO; actual uptime is 99.5%.

**Why it's bad.** Promised reliability without engineering capacity produces breached contracts, SLA credits, and customer churn. SLOs must be co-owned by sales and engineering, with cost implications visible to both.

**Bad example:**
> "We promise 99.99% in enterprise contracts." (Engineering team of 5 supporting one region, no 24/7 on-call, last quarter uptime 99.5%.)

**Good example:**
> "SLO tiers: 99.9% standard (covered by current capacity), 99.95% premium (requires multi-region, costs $X/month, dedicated on-call rotation), 99.99% enterprise (requires both + active-active, costs $Y, contract minimums). Sales authorized to promise tier matching customer commitment."

**How to catch it.** Are your contractual SLAs aligned with your engineering capacity? If not, you are pre-paying penalties.

---

## Red Flag 12: Maturity Score Inflation

**Symptom.** Team self-assesses at Level 4 (Continuous Deployment) but actual deploys are manual, monitoring is uptime-only, and rollback is not automated.

**Why it's bad.** Inflated maturity assessments hide real gaps. Leadership invests based on the inflated number ("we're already great at delivery, invest elsewhere") while real risks accumulate. The SKILL.md's level criteria exist precisely to prevent this.

**Bad example:**
> "Self-assessment: Level 4. We deploy a lot." (No automation, no canary, no auto-rollback, basic uptime monitoring.)

**Good example:**
> "Self-assessment: Level 2 (Automated Build/Test). Evidence: CI passing, automated unit tests, manual deploys via Jenkins, basic uptime monitoring. Target Level 3 by Q4: deploy automation + comprehensive monitoring. Investment plan: $X, 2 engineers for 1 quarter."

**How to catch it.** For each level claim, name the specific evidence required by the SKILL.md's level criteria. If evidence is missing, downgrade the level.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Blame-Seeking Incident Handling | Post-mortem names individuals as cause? |
| 2 | Untested Rollback | Rollback rehearsed in last 90 days? |
| 3 | Error Budget Theater | Has feature work paused when budget burned? |
| 4 | Deployment Strategy Mismatch | Per-service strategy justified? |
| 5 | Missing T-7/T-1/T+1 | All four release checkpoints in plan? |
| 6 | CAB Rubber Stamp / Blocker | <50% of changes go to CAB, real review when they do? |
| 7 | Severity Inflation/Deflation | 80%+ of declared severities match rubric? |
| 8 | Stale Runbook | Last end-to-end execution under 6 months? |
| 9 | Feature Flag Debt | Flags over 12 months under 20 total? |
| 10 | Deploy Frequency Without Lead Time | All DORA metrics reported together? |
| 11 | SLA Beyond Capacity | Contractual SLA aligned with engineering capacity? |
| 12 | Maturity Score Inflation | Each level claim has specific evidence? |

## Related Reading

- SKILL.md Troubleshooting section (for symptom -> root cause -> resolution)
- references/release-checklist.md (if present)
- references/incident-response.md (if present)
- agile-coach/references/red-flags.md (for adjacent maturity-assessment patterns)

## references/release_process.md

# Release Process: Maturity, Planning, Change Management & DORA

Read this when assessing delivery maturity, building a release plan and exit criteria, evaluating change requests, or interpreting DORA metrics. Also contains the release-readiness worked example, the cross-skill integration map, the troubleshooting matrix, and success criteria — all moved verbatim from `SKILL.md`.

## 1. Assess Delivery Maturity

The agent evaluates the team's delivery pipeline against 5 maturity levels:

| Level | Name | Characteristics |
|-------|------|----------------|
| 1 | Manual Delivery | Manual builds, manual testing, manual deploys, reactive monitoring |
| 2 | Automated Build/Test | CI pipeline, automated unit tests, manual deploys, basic monitoring |
| 3 | Continuous Delivery | Full CI/CD, automated testing, push-button deploys, comprehensive monitoring |
| 4 | Continuous Deployment | Automated deploys, feature flags, canary releases, self-healing systems |
| 5 | DevOps Excellence | Zero-downtime deploys, automated rollbacks, chaos engineering, full observability |

**Validation checkpoint:** Identify current level and target level. Focus improvement efforts on one level at a time.

## 2. Plan Release

The agent creates a release plan covering:

1. **Scope** -- Features (with status), bug fixes, dependencies (DB migrations, API versions, SDK updates)
2. **Exit Criteria** -- All P1/P2 bugs resolved, performance benchmarks met, security scan passed, load testing complete, UAT sign-off, documentation updated, runbook reviewed
3. **Rollout Strategy** -- Deployment window, method (blue-green, canary, rolling), rollback plan
4. **Communication Plan** -- T-7 (scope finalized), T-1 (go/no-go), T-0 (release notes), T+1 (customer notification)

Check each exit criterion against the release record before the go/no-go meeting. The skill has no release-checker tool; the record below shows the expected format.

**Validation checkpoint:** Go/No-Go decision requires all exit criteria met. Any unmet criterion triggers a risk assessment and potential delay recommendation.

## 3. Evaluate Change Requests

| Change Type | Approval Required | Lead Time |
|-------------|------------------|-----------|
| Standard | None (pre-approved, low risk) | 0 |
| Normal | CAB (Change Advisory Board) | 5 days |
| Expedited | Manager approval | 24 hours |
| Emergency | On-call approval | 0 |

Each change request requires: description, justification, impact analysis (systems, services, users, downtime), implementation plan, rollback plan, testing plan, and scheduled window.

**Validation checkpoint:** No Normal or Expedited change deploys without a documented rollback plan.

## Example: Release Readiness Check

A readiness record, filled in by the delivery manager:

```text
Release Readiness: v2.5.0
=========================
Type: Minor Release (new features)
Target Date: January 25, 2024

Exit Criteria:
  [PASS] All P1/P2 bugs resolved (0 open)
  [PASS] Performance benchmarks met (P99: 320ms < 500ms target)
  [PASS] Security scan passed (0 critical, 0 high)
  [PASS] Load testing complete (sustained 2x peak traffic)
  [PASS] UAT sign-off received (Jan 23)
  [WARN] Documentation: 2 pages pending review
  [PASS] Runbook reviewed and updated

Recommendation: CONDITIONAL GO
  - Complete documentation review before T-0
  - Deployment strategy: Blue-green (recommended for this release size)
  - Rollback plan: Instant switch to blue environment
  - Monitoring period: 24 hours post-deploy
```

## DORA Metrics

DORA now defines five software delivery performance metrics, grouped as throughput and instability (as of September 2026, [dora.dev/guides/dora-metrics](https://dora.dev/guides/dora-metrics/)). The level values below are the 2024 report's cluster descriptions (2024 Accelerate State of DevOps Report, "Performance levels").

| Metric | Definition | Elite (2024) | High | Medium | Low |
|--------|-----------|--------------|------|--------|-----|
| Deployment Frequency | How often changes are deployed to production | On demand (multiple deploys per day) | Once per day to once per week | Once per week to once per month | Once per month to once every six months |
| Change Lead Time | Commit to version control to deployed in production | Less than one day | One day to one week | One week to one month | One month to six months |
| Change Fail Rate | Share of deployments that require immediate intervention | 5% | 20% | 10% | 40% |
| Failed Deployment Recovery Time (formerly MTTR) | Time to recover from a deployment that fails and needs immediate intervention | Less than one hour | Less than one day | Less than one day | One week to one month |
| Deployment Rework Rate | Share of deployments that are unplanned and made because of a production incident | No level benchmark published | | | |

Reading notes:

- The 2024 change fail rate values are not monotonic (High 20%, Medium 10%). `scripts/delivery_metrics_tracker.py` uses monotonic bands (5/10/20%) so a lower fail rate never scores worse, and treats recovery between one day and one week as Medium.
- "MTTR" is still common in tooling. The tracker reports `failed_deployment_recovery_time` and keeps `mttr` as a JSON alias.
- Rework rate is optional. Mark unplanned fix deploys with `"rework": true` in the input and the tracker reports the rate without classifying it.
- The 2025 DORA report ("State of AI-assisted Software Development") centres on seven team profiles from cluster analysis rather than leading with the Elite/High/Medium/Low levels, alongside the DORA AI Capabilities Model. Treat the 2024 levels as the latest published cut-offs, and use the profiles to diagnose *where* a team is constrained (throughput, instability, or well-being) rather than to rank teams.

Deployments themselves run through the team's own pipeline. This skill measures them: feed the deploy log to `python scripts/delivery_metrics_tracker.py --data deploys.json` for the DORA metrics above.

## Cross-Skill Integration

| Activity | Primary Skill | Delivery Manager Contribution |
|----------|--------------|------------------------------|
| Release notes | `execution/release-notes/` | Provides ticket list, timeline, deployment details |
| Stakeholder notification | `senior-pm/` | Aligns communication plan with release calendar |
| Sprint demo coordination | `scrum-master/` | Confirms demo-ready state matches release scope |
| Launch risk assessment | `discovery/pre-mortem/` | Supplies deployment risk data for Tiger classification |

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| Canary deployment shows elevated errors but feature works in staging | Environment parity gap -- staging lacks production data volume, traffic patterns, or third-party integrations | Improve staging fidelity; use traffic shadowing before canary; define canary success thresholds based on production baselines, not staging |
| Release go/no-go keeps getting deferred | Exit criteria too rigid or too many items flagged as blockers at the last moment | Separate "must-have" from "nice-to-have" criteria upfront; run readiness checks at T-7 and T-3 to surface issues early |
| Incident post-mortems produce action items that never get implemented | Actions lack owners, due dates, or priority relative to feature work | Assign every action to a named owner with a calendar date; reserve sprint capacity for reliability work; track post-mortem actions in a dedicated Jira board |
| Error budget burns through in the first week of the month | Single large incident or multiple small incidents compounding | Implement burn-rate alerting at 50% and 75% thresholds; auto-freeze non-critical deployments when burn rate exceeds 1.5x |
| Change requests bypass the CAB process | Emergency change pathway overused; teams lack awareness of change types | Audit emergency changes monthly; retrain teams on change classification; add automation to flag changes missing required approvals |
| DORA metrics stagnate despite tooling investment | Measuring deployment frequency without addressing batch size, or measuring failed deployment recovery time (MTTR) without improving observability | Focus on leading indicators (batch size, test coverage, observability depth) before expecting DORA improvement |
| Rollback takes longer than expected | Rollback plan not tested; database migrations are not backward-compatible | Require rollback rehearsal for every major release; enforce backward-compatible migration policy; blue-green with instant switch as default strategy |

## Success Criteria

- Change failure rate stays below 5% measured over a rolling 30-day window
- Failed deployment recovery time (formerly MTTR) for SEV-1/SEV-2 incidents is under 1 hour
- 100% of SEV-1/SEV-2 incidents produce a post-mortem with action items within 48 hours
- Error budget consumption stays below 80% in any given month
- Release cadence meets or exceeds the target deployment frequency (weekly or better)
- Zero deployments proceed without a documented rollback plan
- DORA metrics show quarter-over-quarter improvement across all four classified measures, with rework rate trending down where tracked

## references/sla_management.md

# SLA & Error Budget Management

Read this when calculating SLA compliance, error budgets, and burn rates, or setting deployment-freeze thresholds. Moved verbatim from `SKILL.md`.

## Track SLA and Error Budget

The skill has no SLA tool; compute the budget from your monitoring data as below.

**Error budget calculation example:**
```
SLA: 99.9% availability
Error Budget: 0.1% = 43.8 minutes/month

Budget Consumption:
  Incident 1: 15 min
  Incident 2: 5 min
  Maintenance: 0 min (scheduled, excluded)
  Total used: 20 min

Remaining: 23.8 min (54% remaining)
Burn rate: 0.8x (on track)
```

**Validation checkpoint:** If error budget burn rate exceeds 1.5x, freeze non-critical deployments until burn rate normalizes.

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/delivery-manager -->
