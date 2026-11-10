---
description: "Plan a flag-gated rollout: classify the flag, pick a rollout shape, set kill-switch thresholds and retire the flag. Use when planning a phased rollout, a kill switch, a holdout or a cleanup of old flags."
---

# Feature Flag Strategy (PM playbook)

## Overview

A feature flag is a runtime switch that decouples deploying code from releasing a feature. Done well, flags turn high-stakes ship dates into low-stakes config changes -- launches become measured ramps, regressions become single-toggle rollbacks, and experiments live alongside production code. Done poorly, flags become permanent technical debt: hundreds of dead toggles in code, conflicting flag states across environments, and nobody remembering what the flag controls.

This skill is the **PM-facing** rollout playbook. It does not describe how to wire a flag library into your codebase (that is the engineering side, e.g. your LaunchDarkly / Statsig / Optimizely / Unleash / OpenFeature install). It describes how a PM plans a phased rollout: what kind of flag this is, how it ramps, what the gate criteria are between stages, who can flip the kill-switch, when the flag retires, and how it is named so the team can find it six months later. The frameworks behind it are Martin Fowler's "Feature Toggles" taxonomy, LaunchDarkly's rollout best practices, and Optimizely / Statsig experiment playbooks.

## Core Capabilities

- **Flag classification** -- release / experiment / ops / permission, each with its own lifespan and ownership rules.
- **Rollout shape selection** -- linear, segmented, geographic, A/B-with-holdout, dark launch, reverse ramp, mobile forced-upgrade.
- **Kill-switch design** -- pre-agreed thresholds per surface and single-config-change rollback authority for on-call.
- **Holdout design** -- short-term and global holdouts for long-term lift attribution.
- **Flag-debt governance** -- retirement dates, retirement checklist, quarterly audit, naming conventions, dependency chains.

## When to Use

- Planning a launch larger than a small team can ship cold (anything customer-facing usually warrants a flag).
- Risky changes to high-traffic surfaces (search, checkout, auth, billing -- always behind a kill-switch).
- Experiments (A/B tests) with hold-out and statistical-significance gates.
- Permission rollouts (enterprise tenants, beta participants, a specific role).
- Operational levers (throttles, circuit breakers, degrade-modes).
- Migration of a deterministic feature to AI (pair with `ai-feature-prd/`; cost gates via `engineering/llm-cost-optimizer/`).

**When NOT to use:** one-time data migrations (use a script with `--dry-run`), environment configuration, permanent A/B variants that never converge (that is personalization), or flag-flagging every change (cost > value when overused).

## Clarify First

Before drafting the rollout plan, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Flag type:** release / experiment / ops / permission sets the lifespan and whether a retirement date even applies (permanent vs temporary).
- **Rollout shape:** linear / segmented / geo / A-B-with-holdout / dark / reverse-ramp defines the stages and gate criteria of the ramp.
- **Kill-switch threshold + authority:** the metric that triggers rollback and who on-call may flip it; a flag without this is worse than no flag.
- **Retirement date:** for release/experiment flags, the date the toggle is removed; omitting it is how flag debt accrues.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Classify the flag (release, experiment, ops, permission), pick a rollout shape, and set the kill-switch threshold and who may flip it, before the first ramp.
2. Set a retirement date for release and experiment flags, name the flag with the convention, and document the plan in `assets/rollout_plan_template.md`.
3. Ramp through stages with a "green pass" gate metric per step [RECOMMENDED]; retire the flag at stable GA; audit the inventory quarterly.

**Done when** the plan names each stage's gate metric and threshold, the kill-switch owner, and the date the flag is deleted from code.

See `references/rollout-execution-playbook.md` for the full taxonomy, shape catalog, kill-switch tree, holdout governance, naming, workflow, troubleshooting, and success criteria.

## Anti-Patterns

### Ramping without reading the gate metrics
**Mistake:** The flag moves 1% to 5% to 25% to 100% on schedule, and nobody checks the dashboard at any stage. The activation drop shows up at 100%.
**Why it happens:** The ramp schedule feels like the safety mechanism, so following the dates feels like enough.
**Instead:** Name the gate metric for every stage in `assets/rollout_plan_template.md`. At each stage, post the metric values and an ADVANCE or HOLD decision before moving on. If the ramp log has no metrics, the gates were not enforced.

### Rollback that needs a code revert
**Mistake:** During an incident, turning the feature off means opening a revert PR, waiting for review and redeploying. Customers carry the impact for 45 minutes.
**Why it happens:** The flag was wired for release, and nobody tested the off path.
**Instead:** Rollback must be a single config change that on-call can make in under 60 seconds. Drill it in non-production once a quarter and time it. If it takes more than 5 minutes, the kill-switch is broken.

### Mobile flag with no client version gate
**Mistake:** A mobile flag goes to 100% and older app versions crash because they cannot handle the new server response.
**Why it happens:** Web flags take effect for everyone at once, and the same habit carries over to mobile.
**Instead:** For every mobile flag, write down the minimum client version that supports the new behavior and set it as a prerequisite on the flag. Older clients keep the old behavior. Ramp fully only once that version's adoption is high enough.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

- `references/rollout-execution-playbook.md` -- read this when planning a rollout end-to-end: flag taxonomy, all 7 rollout shapes, kill-switch decision tree + thresholds, holdouts, flag-debt retirement, naming, dependency chains, approval/audit, workflow, troubleshooting, success criteria.
- `references/fowler-feature-toggle-taxonomy-guide.md` -- read this for the deep dive on Martin Fowler's "Feature Toggles" essay, lifespans, ownership patterns, and the operational discipline behind them.
- `references/rollout-shape-comparison-guide.md` -- read this for the worked comparison of the 7 rollout shapes with example use cases and risk profiles.
- `references/red-flags.md` -- read this when reviewing a rollout plan for anti-patterns and failure modes before sign-off.

## Files

| File | Purpose |
|---|---|
| `assets/rollout_plan_template.md` | Per-feature rollout plan: stages, gates, owners, dates |
| `assets/kill_switch_decision_tree.md` | Kill-switch thresholds, authority and flip steps |
| `assets/flag_debt_retirement_checklist.md` | Retirement workflow and quarterly audit |
| `assets/flag_naming_convention.md` | Naming sheet |
| `examples/pricing-page-redesign-rollout.md` | Worked rollout |

## Scope & Limitations

**In scope:** flag taxonomy and lifespan rules; rollout shapes; kill-switch decision tree and thresholds; holdout design; flag-debt retirement workflow + audit; naming and dependency-chain governance; approval, audit-trail, and two-person-rule patterns.

**Out of scope:** wiring flag SDKs into a codebase (engineering side); statistical analysis of experiments (pair with `discovery/brainstorm-experiments/` for design; data-analytics for stats); building gating dashboards (BI tooling); customer launch comms (`launch-playbook/`, `prfaq/`, `release-notes/`); end-of-life narrative (`eol-communication/`); code rollback strategy (git revert + deployment pipelines).

**Caveats:** flags reduce launch risk but do not eliminate it -- a flag with a broken kill-switch is worse than no flag. Flag debt grows with velocity. Permission/Ops flags are permanent; release/experiment flags are temporary, and conflating the two is the most common failure mode. Holdouts are politically hard to maintain -- document the policy with leadership sign-off. On mobile, forced-upgrade flows are user-hostile; plan around adoption curves.

## Integration Points

| Integration | Direction | Description |
|---|---|---|
| `launch-playbook/` | Pairs with | Rollout plan is the deployment ramp inside the broader launch playbook |
| `cycle-time-analyzer/` | Pairs with | Long-stuck ramps are a leading indicator of risk |
| `prfaq/` / `release-notes/` | Pairs with | External launch narrative vs the operational rollout plan that produced it |
| `eol-communication/` | Pairs with | Reverse-ramp (Shape F) is the operational side of a sunset |
| `ai-feature-prd/` | Pairs with | The AI PRD's deployment ramp (Section 11.3) executes via this skill |
| `discovery/brainstorm-experiments/` | Pairs with | Experiment toggles operationalize Lean experiments |
| `discovery/pre-mortem/` | Pairs with | Pre-mortem risks inform kill-switch thresholds |
| `engineering/llm-cost-optimizer/` | Pairs with | AI ramp gate: cost budget per stage |
| `status-update-generator/` | Feeds into | Rollout-stage pace + gates appear in weekly status |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/fowler-feature-toggle-taxonomy-guide.md

# Fowler's Feature Toggle Taxonomy Guide

A working reference for Martin Fowler's "Feature Toggles" taxonomy and how to apply it operationally. The taxonomy matters because each toggle category has different lifespan, ownership, and risk -- conflating them is the single most common cause of flag debt.

## 1. Origin

Pete Hodgson published "Feature Toggles (aka Feature Flags)" on Martin Fowler's site in 2017 (updated through 2020). The article codified what teams at LaunchDarkly, Etsy, Facebook, and Yelp had been doing for years: flags are not all the same; treat them by category.

## 2. The four categories

### Release Toggles

**Purpose.** Decouple deploy from launch. Code ships behind the toggle; product turns it on when ready.

**Lifespan.** Days to weeks. Should be **retired** within ~30 days of full rollout.

**Ownership.** The product team that built the feature. PM + Eng lead.

**Failure mode.** Never retired. Becomes "permanent" without explicit decision. Three years later, nobody remembers what `enable_new_search_v2_2023` controls.

**Discipline.**
- Set a retirement date when the flag is created.
- Track in the team's flag inventory.
- File a retirement PR as part of the launch checklist.
- The flag library should support marking "stale" toggles and alerting on them.

### Experiment Toggles

**Purpose.** A/B test variants. Allocate users to control / variant arms; measure lift.

**Lifespan.** Days to weeks. **Retire when the experiment concludes**, whether the variant ships or not.

**Ownership.** Product team + analytics / data science.

**Failure mode.** Experiment "runs forever" because the analyst is on PTO; the team forgets which is the winning variant; the analysis never finalizes.

**Discipline.**
- Pre-register the experiment: hypothesis, primary metric, sample size, run window.
- Define the decision criteria (statistical significance threshold, effect-size minimum).
- Define the decision date and the decider.
- Retire the experiment toggle within 14 days of decision.
- Keep the holdout slice open beyond the experiment for long-term lift attribution.

### Ops Toggles

**Purpose.** Operational controls: circuit breakers, throttles, kill-switches for system protection, degrade-modes.

**Lifespan.** Permanent or long-lived. They are part of the system's defensive surface.

**Ownership.** Infrastructure / SRE / platform team.

**Failure mode.** Rare; ops toggles tend to be well-maintained because they are critical to incident response.

**Discipline.**
- Document each ops toggle in the SRE runbook.
- Test the ops toggle quarterly in non-prod (and ideally in prod with a controlled drill).
- Rotate ownership when team members leave.

### Permission Toggles

**Purpose.** Gate features by user, plan tier, role, tenant, beta program enrollment.

**Lifespan.** Permanent. Lives with the product.

**Ownership.** Product + Eng.

**Failure mode.** Treated as a release toggle and "cleaned up", removing the permission boundary and exposing the feature universally.

**Discipline.**
- Distinguish permission flags from release flags in naming (`__permission`, `__beta_access`).
- Document in the product entitlement system / pricing page.
- Treat the permission flag as part of the product's contract with users, not a deploy artifact.

## 3. The lifecycle-vs-dynamism matrix

Fowler's original article includes a useful 2x2:

|  | Short-lived | Long-lived |
|---|---|---|
| **Static (per environment, per deploy)** | Release toggle | Permission toggle |
| **Dynamic (per request)** | Experiment toggle | Ops toggle |

- Release toggles are typically *static* and *short-lived*: set once for the deploy, retired after launch.
- Experiment toggles are *dynamic* (per-user evaluation) and *short-lived*.
- Permission toggles are *static* (per-tenant or per-user) and *long-lived*.
- Ops toggles are *dynamic* (often per-request) and *long-lived*.

Picking the wrong cell is a category error. A "permission" implemented as a dynamic per-request flag will hammer your flag service. A "release toggle" implemented as a long-lived permission flag will never get cleaned up.

## 4. Implementation patterns Fowler highlights

Fowler distinguishes between **toggle point** (where in code the toggle is checked) and **toggle router** (the runtime that decides). Patterns:

- **Toggle point as low-level as possible.** Each branch is small, easy to remove.
- **Toggle router as a single source.** All evaluations route through one library, one config, one audit log.
- **Inversion of control.** Code does not query "is feature X on?"; rather, the platform injects the variant. This makes A/B testing and rollout cleaner.

## 5. Lifespan disciplines

Fowler's strongest claim: the practice of feature flagging is **operationally expensive**. The investment pays off only if flags are retired aggressively. Specifically:

- **Track every flag.** A registry of all flags, their type, their owner, their last-flip timestamp.
- **Stale-flag alerting.** A flag at 100% (or 0%) for more than 30 days is stale. The flag service or CI should surface this weekly.
- **Retirement is engineering work.** Plan it into sprints; do not treat it as cleanup.
- **Limit concurrent flags.** A team running 50 active flags simultaneously is in flag-debt territory. Target 5-15 for most teams.
- **Pair every release toggle with a retirement PR opened at flag-creation time.**

## 6. Pitfalls

| Pitfall | Cause | Mitigation |
|---|---|---|
| **Flag debt** | No retirement discipline | Quarterly audit; retirement PRs at creation |
| **Configuration sprawl** | Flags pile up across environments | Single source of truth in the flag service |
| **Hidden coupling** | Feature A depends implicitly on Feature B's flag state | Explicit prerequisite dependencies in the flag service |
| **Production flag drift** | Prod flag state diverges from staging/dev | Same flag service for all environments; staging flag state mirrors prod |
| **Test matrix explosion** | N flags = 2^N combinations | Test only combinations that occur in production; retire flags to shrink N |
| **"Toggle as permission" anti-pattern** | Using a temporary toggle to gate permanent access | Convert to a permission flag explicitly; rename; transfer ownership |
| **No audit log** | Hard to debug post-incident | Flag service should log every flip with who / when / why |
| **No granular control** | "On/off" only, no percentage rollout | Use a flag library that supports percentage and segmented rollouts |

## 7. Modern updates (2020-2026)

The 2017 Fowler article remains the canonical text, but the 2020-2026 industry has settled on additional norms:

- **OpenFeature** (CNCF spec) standardizes the SDK surface across vendors. Adopted by LaunchDarkly, Flagsmith, Unleash, ConfigCat.
- **Statsig** popularized the experimentation-first flag model (deep integration with metrics and stat-sig analysis).
- **Eppo + StatSig + Optimizely** dominate the experimentation-toggle category.
- **Hypothesis-driven rollout.** Each release toggle has a stated hypothesis ("rolling this out should not regress p95 latency by more than 5%") that gates each ramp step.
- **AI-feature ramps.** For LLM features, ramps include cost and eval gates (see `ai-feature-prd/` Section 11.3).
- **Compliance flags.** EU AI Act compliance + GDPR / regional opt-outs are increasingly enforced via permission flags scoped to geography.

## 8. Anti-pattern: the "permanent release toggle"

By far the most common failure. A release toggle was created in 2023, ramped to 100%, never retired. By 2026, the code has two branches around every check; nobody is sure which branch is dead; engineers fix bugs in the dead branch; the team is afraid to clean it up because the consequences are unclear.

Prevention:
- Retirement date is a required field at flag creation.
- Stale-flag report on the team's weekly engineering review.
- Retirement PRs treated as ordinary work, not "tech debt."
- Engineering manager owns the team-level flag count metric.

## 9. Reading list

- Pete Hodgson, "Feature Toggles (aka Feature Flags)" (martinfowler.com, 2017, updated 2020)
- "Trunk-Based Development" -- trunkbaseddevelopment.com (the flag practice goes hand-in-hand with TBD)
- LaunchDarkly, "Effective Feature Management Engineering" (free e-book, multiple editions)
- OpenFeature, "Specification" (openfeature.dev)
- "Accelerate" (Forsgren, Humble, Kim) -- references feature flagging as a deployment-decoupling practice

---
**Last Updated:** 2026-05-22

## references/red-flags.md

# Red Flags: Feature Flag Strategy

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the rollout plan and flag inventory before opening any ramp stage. Each red flag shows the *bad* version next to the *good* version, anchored to Martin Fowler's flag taxonomy (release / experiment / ops / permission) and standard rollout shapes.

---

## Red Flag 1: Zombie flags (flag debt)

**Symptom.** Flag inventory has 200+ live flags. Search for flags last toggled > 90 days ago returns 140 results.

**Why it's bad.** Every live flag is technical debt. Test matrices grow combinatorially. Code branches diverge. Mystery behaviors appear when two flags interact unexpectedly. A team shipping 20 features/quarter without retirement discipline accumulates 80+ dead flags per year.

**Bad example:**
> "Flag inventory (audit Mar 2026): 217 live flags. Of those: 88 at 100% for > 60 days (release toggles that should have been retired); 24 at 0% for > 90 days (dead experiments); 31 not toggled in > 180 days (mystery)."

**Good example:**
> "Flag governance:
> • New flag creation requires a retirement date.
> • Quarterly audit: any release/experiment flag aged > 90 days surfaces in the report.
> • Retirement PR is a normal sprint task, not a periodic cleanup.
> • Flag count trend reported monthly; goal is stable or declining.
> Current state: 47 live flags, 19 retired this quarter, net -3."

**How to catch it.** Run a flag inventory. Count flags older than 90 days that are not Ops or Permission type. > 10% of total = debt is accumulating.

---

## Red Flag 2: No kill-switch criteria

**Symptom.** Rollout plan describes the ramp shape but does not say at what error rate or customer-impact threshold the team flips the kill-switch.

**Why it's bad.** Without pre-agreed thresholds, kill-switch decisions are made in the heat of incident — usually too slowly. The on-call hesitates because "is this bad enough?" Customers experience the bug for an extra 20 minutes while leadership debates.

**Bad example:**
> "Rollout plan: 'Monitor metrics during rollout. If anything looks wrong, contact PM to discuss next steps.'"

**Good example:**
> "Kill-switch criteria (pre-agreed, in rollout plan):
> • Error rate > 0.5% sustained 5 min on flagged surface OR
> • p95 latency > 2x baseline for 10 min OR
> • >= 3 independent paid-customer reports of same issue OR
> • Major-customer-blocked event.
> Authority: on-call engineer flips without escalation; logs to #incidents; PM and Eng Lead notified by automation. Flag stays off until root cause + fix; re-ramp from 0%."

**How to catch it.** Read the rollout plan. Search for numbers and "threshold". If none, the kill-switch is improvised.

---

## Red Flag 3: Release toggle treated as permanent

**Symptom.** Flag `web__new_checkout__v2` was created for the new-checkout launch in 2024. Still in the codebase 18 months later, still at 100%. Now functionally a permission gate.

**Why it's bad.** Fowler's taxonomy: release toggles are temporary; permission toggles are permanent. Conflating them means the codebase carries dead branches forever; the test matrix is bloated; the next refactor stumbles into a "flag" that nobody owns.

**Bad example:**
> "`web__new_checkout__v2` at 100% since Sept 2024. Not retired. New engineer asks: 'do I need to test both branches?' Nobody knows."

**Good example:**
> "Quarterly audit Q1: `web__new_checkout__v2` at 100% for 18 months. Retired. PR removes both code branches (`if (flag.new_checkout_v2) { newPath() } else { oldPath() }` → `newPath()` only). Config entry deleted. Documentation updated. Final state archived to flag-retirement log: 'created 2024-09, retired 2026-03, owned by checkout team, controlled the new checkout flow which is now the only flow'."

**How to catch it.** For each flag at 100% for > 30 days, ask: "is this a permanent permission gate or an unretired release toggle?" If the latter, retire.

---

## Red Flag 4: Flag flipped without metric gates

**Symptom.** Engineer thinks "looks good, let's go to 25%". Flips the flag. No metric was the gate.

**Why it's bad.** Without metric gates, advancement is intuition. Sometimes intuition is right. Often it isn't. Production reveals a 3-percentage-point conversion drop two days after a 25% ramp because nobody was watching the right number.

**Bad example:**
> "Ramp log: '5% → 25% on Tuesday. Eng team felt good about the data. No specific metric check.'"

**Good example:**
> "Ramp gates (pre-agreed in rollout plan):
> Stage → Gate metric to advance:
> • 1% → 5%: no crashes for 24h; eval acceptance >= baseline.
> • 5% → 25%: conversion rate within 95% CI of control for 72h; error rate < baseline + 0.2%; p95 latency within +10% of baseline.
> • 25% → 50%: above metrics held for 5 days; no top-tier-customer incident.
> • 50% → 100%: above held for 7 days; positive cohort retention signal.
> Advancement decision: owner reviews the dashboard at the gate; documents pass/fail with the metric values."

**How to catch it.** Read the rollout plan. For each advancement, is the gate metric named? If not, advancement is by feel.

---

## Red Flag 5: Mobile flag without version gate

**Symptom.** Mobile feature flag flipped at 100%. App on old client version crashes because the feature requires a server response the old client cannot parse.

**Why it's bad.** Mobile clients have long-tail version distribution. ~30% of users may be on a client version > 60 days old on launch day. A flag flip without a minimum-client-version check breaks those users immediately, with no recovery until they update.

**Bad example:**
> "Flag `mobile__new_search` flipped to 100%. Day 1: crash reports from iOS 12.4 (released 3 months ago). 8% of MAU stuck on a broken app."

**Good example:**
> "Flag `mobile__new_search` configured with prerequisite: client_version >= 14.2 (released 2026-02-14, 95% adoption confirmed via app analytics). Flag returns false for older clients; old behavior persists. Older clients receive an in-app upgrade prompt. Plan: full rollout after >= 98% adoption of 14.2."

**How to catch it.** For every mobile flag, ask: "what is the minimum client version that supports the new behavior?" If unanswered, the flag is unsafe.

---

## Red Flag 6: Permissions too loose on critical flag

**Symptom.** Anyone with engineer access can flip the billing-related kill-switch. One engineer accidentally toggles it during routine work.

**Why it's bad.** Critical-surface flags (billing, auth, data deletion) need two-person rules. Loose permissions plus a single typo in the flag UI equals a self-inflicted incident.

**Bad example:**
> "`billing__new_card_flow` flag. Permissions: all engineering. One engineer toggles it from 50% to 0% by mistake during a separate task. 2 hours of revenue lost; 47 stuck transactions."

**Good example:**
> "`billing__new_card_flow` permissions: two-person rule. Toggle requires one engineer to propose + a second to approve in the flag service before the change takes effect. Authority limited to billing team + on-call rota. Audit log emails the team channel on every change. High-tier flags (billing, auth, account-deletion, data-export) all gated this way."

**How to catch it.** List the team's high-tier flags (billing, auth, etc.). For each, check who has flip authority. If > 5 people without two-person rule, permissions are loose.

---

## Red Flag 7: Holdout killed when experiment "shipped"

**Symptom.** An A/B test concludes; the team rolls the winner to 100%; the holdout group is also exposed because "the experiment is over".

**Why it's bad.** Holdouts are valuable post-launch — they let the team measure long-term lift. Killing the holdout at launch means losing 30-90 days of lift attribution data. Long-term cohort retention impacts become invisible.

**Bad example:**
> "Experiment concludes; variant wins +8% conversion. Roll to 100%, including the 5% holdout. Quarter later: cannot answer 'what was the long-term retention impact?'"

**Good example:**
> "Experiment design includes a short-term and long-term holdout:
> • Short-term: powers the experiment readout (consumed at conclusion).
> • Long-term: 5% holdout maintained for 90 days post-launch to measure retention lift.
> Holdout retirement is a separate decision after long-term measurement. Re-exposure of the holdout group is planned (likely with a small conversion event when finally exposed) and documented."

**How to catch it.** Open any experiment's design doc. Is there a long-term holdout policy? If not, the team will lose post-launch measurement.

---

## Red Flag 8: Flag name doesn't follow conventions

**Symptom.** Flag inventory includes `johnsTest`, `featureV3final`, `tryNewWay`. Six months later, nobody knows what they do.

**Why it's bad.** Flag names are read more often than written. Non-conventional names (camelCase, personal names, version suffixes without context) become unfindable in audits. Searching for "all checkout flags on web" returns nothing because nobody can match the pattern.

**Bad example:**
> "Flag names: `newCheckout`, `johnsExperiment`, `featureA`, `testFlag2`, `final_v3_v2_real`."

**Good example:**
> "Naming convention: `<scope>__<feature>__<purpose>__<version>`.
> Examples:
> • `web__checkout__new_flow__v2` (release toggle, web)
> • `api__search__relevance__experiment_q3` (experiment, API)
> • `infra__search__circuit_breaker` (ops, permanent)
> • `product__enterprise_admin__permission` (permission, permanent)
> Enforced via PR review checklist. CI lints flag names against the regex."

**How to catch it.** Open the flag inventory. Filter for names not matching `<scope>__<feature>__<purpose>__<version>`. If > 10%, the convention is unenforced.

---

## Red Flag 9: Flag dependency chains > 2 levels deep

**Symptom.** Flag A depends on flag B depends on flag C depends on flag D. The team cannot answer "what is the user experience when only A is enabled?"

**Why it's bad.** Each level of dependency multiplies the combinatorial test matrix. Beyond 2-3 levels, the team cannot reason about interactions. Mystery bugs appear when flags interact in ways nobody modeled.

**Bad example:**
> "Flag dependency graph:
> ai_chatbot → ai_chatbot_v2 → ai_chatbot_v2_premium → ai_chatbot_v2_premium_streaming → ai_chatbot_v2_premium_streaming_eu
> (Test matrix: 32 combinations. Tested: 4.)"

**Good example:**
> "Flag dependency rule: max 2 levels.
> If the natural design requires deeper chains, flatten:
> • Parent flag: `ai_chatbot_v2_full` (rolls the whole feature).
> • Child variation flags: `ai_chatbot_v2_streaming_enabled`, `ai_chatbot_v2_eu_compliance`, all flat children of the parent.
> Test matrix: parent x 2-3 children = 6-12 combos, manageable. Document the design."

**How to catch it.** Map your flag dependencies. Any chain > 2 levels = flatten before the next ramp.

---

## Red Flag 10: Rollback requires code revert

**Symptom.** Production incident. To roll back the feature, engineering must merge a revert PR and deploy. 45 minutes elapsed.

**Why it's bad.** A flag whose rollback path is a code revert defeats the purpose of having a flag. Real rollback is a single config change, in < 60 seconds. If the team has to deploy to roll back, they will hesitate, and customers experience extended impact.

**Bad example:**
> "Incident timeline: error spike at 14:02. Decision to rollback at 14:08. PR opened at 14:11; review at 14:18; merge at 14:24; deploy completes at 14:47. 45-minute customer impact."

**Good example:**
> "Incident timeline: error spike at 14:02. Decision to flip kill-switch at 14:05. On-call flips flag in LaunchDarkly UI at 14:06. Error rate normalizes at 14:08. 6-minute customer impact. Post-incident analysis happens at leisure; the kill-switch did its job."

**How to catch it.** Drill the rollback in non-production once per quarter. Time it. If > 5 minutes, the kill-switch is broken.

---

## Red Flag 11: Owner has left the company

**Symptom.** Flag `web__feature_x` exists in production. Audit asks "who owns this?" Owner field: Jane Doe. Jane Doe left 8 months ago.

**Why it's bad.** Ownership by individual is brittle. People leave. Flags persist. An unowned flag has no champion for retirement, no on-call escalation path, and accumulates dust until it causes an incident.

**Bad example:**
> "Flag `web__feature_x`: owner Jane Doe (terminated 2025-09). No re-assignment. Flag at 100% for 14 months."

**Good example:**
> "Ownership policy: flags owned by team, not individual. Field captures `owning_team`: 'checkout-team'. Onboarding for new team members includes a 30-min flag review for the team. Quarterly: orphaned flags (team disbanded / re-org) get auto-assigned to the engineering management team for triage."

**How to catch it.** Audit owner field across all flags. Cross-reference with current employee list. Orphans = re-assign to team.

---

## Red Flag 12: No metric validated before 100% ramp

**Symptom.** Flag ramped 1% → 5% → 25% → 100% on schedule. No metric was actually validated at any stage. Team realizes at 100% that activation dropped 4 points.

**Why it's bad.** Ramping is supposed to *reveal* problems at low blast radius. If the team does not look at the data at each stage, the ramp is decoration — the same blast radius as a big-bang launch, but with extra steps.

**Bad example:**
> "Ramp log: 'May 1: 1%. May 3: 5%. May 6: 25%. May 13: 100%.' Owner: 'we were busy with other things, didn't look at the dashboard.'"

**Good example:**
> "Ramp gate validation: at each stage, owner posts in #rollout-channel: 'Stage: 25%. Window: 72h. Metrics: conversion 4.1% vs control 4.0% (within CI); error rate 0.03% vs 0.04%; p95 latency 412ms vs 405ms (within 10%). Decision: ADVANCE.' Asynchronous review by Eng Lead before advancing. Documented for the launch retro."

**How to catch it.** Read the ramp log. For each stage, are metrics posted? If no, the gates were not enforced.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Zombie flags | What % of release/experiment flags are aged > 90 days? |
| 2 | No kill-switch criteria | Are thresholds (error %, latency, customer count) named? |
| 3 | Release toggle treated as permanent | Any release flag at 100% > 30 days unretired? |
| 4 | Flag flipped without metric gates | At each advancement, what number was the gate? |
| 5 | Mobile flag without version gate | What minimum client version supports the new behavior? |
| 6 | Loose permissions on critical flag | Two-person rule on billing/auth/data flags? |
| 7 | Holdout killed when experiment "shipped" | Is there a long-term (90d+) holdout post-launch? |
| 8 | Flag name doesn't follow conventions | Match against `<scope>__<feature>__<purpose>__<version>` |
| 9 | Dependency chains > 2 levels | Map dependencies; flatten if > 2 deep |
| 10 | Rollback requires code revert | Drill the kill-switch; > 5 min? |
| 11 | Owner has left the company | Cross-reference owner field with employee list |
| 12 | No metric validated before 100% | At each stage, were metrics posted? |

## Related Reading

- SKILL.md Troubleshooting
- references/fowler-feature-toggle-taxonomy-guide.md
- references/rollout-shape-comparison-guide.md
- Martin Fowler, "Feature Toggles" essay
- `launch-playbook/` (the rollout plan is part of the broader launch)
- `ai-feature-prd/` (AI deployment ramps use this skill)
- `pricing-prd/` (pricing rollouts use this skill)
- `eol-communication/` (reverse-ramp Shape F)

## references/rollout-execution-playbook.md

# Rollout Execution Playbook

Read this when planning the operational detail of a flagged rollout: choosing a flag type, picking a ramp shape, defining the kill-switch, designing holdouts, naming the flag, governing dependencies/approvals, and running the end-to-end workflow with troubleshooting and success criteria.

## Flag taxonomy (Fowler)

Martin Fowler's taxonomy classifies flags by **purpose** because lifespan and ownership differ dramatically.

| Flag type | Purpose | Lifespan | Ownership | Examples |
|---|---|---|---|---|
| **Release toggle** | Deploy code before release; decouple ship from launch | Days to weeks; **must retire after launch** | Owning team (Eng + PM) | "new_checkout_flow_v2", "search_relevance_v3" |
| **Experiment toggle** | A/B test variants; decide based on stat-sig | Days to weeks; **must retire when experiment concludes** | Owning team + analytics | "checkout_button_color_test", "onboarding_v2_experiment" |
| **Ops toggle** | Operational control: throttle, circuit-break, degrade-mode | Permanent or long-lived | Infra / SRE | "search_circuit_breaker", "rate_limit_premium_tier" |
| **Permission toggle** | Gate features by user, plan, role, tenant | Permanent (lives with the product) | Product + Eng | "enterprise_admin_panel", "beta_program_access" |

The error mode is treating a release toggle as a permission toggle ("we never turned it off, so it's now permanent"). The result is **flag debt**: thousands of dead branches in code, conflicting flag combinations, mystery behaviors.

**Rule:** every release toggle and experiment toggle has a *retirement date* set at creation. Operationally, a flag without a retirement date is treated as a defect.

## Rollout shapes

The shape of a ramp tells the team how much risk they are absorbing per step.

### Shape A: Linear ramp

```
0% -> 1% -> 5% -> 10% -> 25% -> 50% -> 100%
```

The default. Each step held for 1-3 days while metrics settle. Use for new features without strong segment hypotheses.

### Shape B: Segmented (audience-first)

```
Internal employees -> Friends-and-family -> Beta opt-in -> Free tier -> Paid tier -> All
```

Use when you have explicit risk gradients across segments -- enterprise customers wait until pro customers have validated; consumer flagship waits for ToS-aware beta opt-in.

### Shape C: Geographic / regulatory-aware

```
Single low-risk region -> Region cluster -> Global, excluding regulated regions -> Global, all regions
```

Use for features with regulatory variance (EU AI Act, GDPR-specific UI, payment-method constraints, age-verification rules).

### Shape D: A/B split with holdout

```
Variant A (control): 50%
Variant B (test): 45%
Holdout (no exposure): 5%
```

Use for experiments. The holdout group is never exposed even after rollout, so the team can measure long-term lift weeks after the experiment concludes.

### Shape E: Dark launch (shadow)

```
Code shipped to 100% -- no user-visible behavior
Backend runs the new path in shadow; results discarded but logged
```

Use to validate performance, error rate, and side effects before any user sees the new behavior. Standard for high-traffic system changes; also standard for AI features (pair with `ai-feature-prd/` Section 11.3).

### Shape F: Reverse ramp (sunset)

```
100% -> 75% -> 50% -> 25% -> 10% -> 0%
```

Use for retiring a feature. The ramp gives users time to migrate; analytics monitor whether users are healthy on the new path. Pair with `eol-communication/`.

### Shape G: Forced-upgrade (mobile)

```
Server-side flag check -> app refuses to start on old client -> user must upgrade
```

Special case for mobile when the new feature requires a client version. Always have a transition window; never flag-flip on day 1 of release.

## Kill-switch decision tree

A kill-switch is the on-call's emergency control. Three rules:

1. **Every release toggle has a kill-switch path.** "Turn the flag off" must be a single config change, not a code rollback.
2. **The kill-switch threshold is pre-agreed.** Define it during planning, not in the heat of incident.
3. **The on-call has authority to flip without escalation.** If the rollback requires VP sign-off, the system is too slow.

### Decision tree

```
Incident detected.
|
+-- Customer impact? -- No --> Monitor; document; do not flip.
|        |
|        Yes
|        |
|        v
+-- Within feature-flagged surface? -- No --> Standard incident response.
|        |
|        Yes
|        |
|        v
+-- Error rate > threshold OR major-customer-blocked? -- No --> Throttle / partial degrade.
|        |
|        Yes
|        |
|        v
+-- Flip kill-switch -- 0% rollout -- Notify owner + customers.
         |
         v
   Post-incident: root cause; flag stays off until fix lands; never re-enable without re-ramp.
```

### Kill-switch thresholds (defaults to tune per surface)

| Surface | Default threshold |
|---|---|
| Critical (checkout, auth, billing) | Error rate > 0.5% sustained for 5 min |
| Core (search, signup, dashboard) | Error rate > 2% sustained for 10 min OR top-tier-customer blocked |
| Non-critical | Error rate > 5% sustained for 15 min |
| Latency | p95 > 2x baseline for 10 min |
| Customer reports | >= 3 independent reports of the same issue from paid customers |

## Holdouts

A holdout is a slice of users (typically 1-10%) who never see the feature, even after general availability. Two uses:

**Short-term holdout** -- to measure the lift of the feature with statistical confidence over time. Required for any experiment where the team wants to attribute long-term impact.

**Long-term ("global") holdout** -- a slice that never sees *any* of the team's experiments for a quarter. Allows leadership to attribute aggregate lift to the team. Most experimentation-mature orgs run a global holdout.

### Holdout governance

- **Size**: 1-10%; smaller holdouts have less statistical power but cost less in lost feature exposure.
- **Composition**: random or stratified (by segment, geo, plan tier).
- **Duration**: at least one full retention horizon (D30 or D60); often 1-2 quarters.
- **Documentation**: holdout configuration in source control; never modified mid-experiment.
- **Re-exposure**: when the holdout ends, members are merged back; the team should plan for the conversion event.

## Flag debt and retirement

Every feature flag is technical debt by default. A live flag has a maintenance cost (test matrix, code branches, config integrity). Successful teams treat flag retirement as a first-class engineering activity.

### Retirement checklist (release toggle)

- [ ] Feature is at 100% for at least 2 weeks with stable metrics.
- [ ] No regression has been triaged that the flag would mitigate.
- [ ] Flag owner has filed a retirement PR removing both branches of code.
- [ ] Test matrix updated to remove the flag combinations.
- [ ] Config entry removed from the flag service.
- [ ] Documentation updated (runbook, customer-facing docs if any).
- [ ] Final state archived (what the flag controlled, when it retired, who owned it).

### Retirement signals

- Flag has been at 100% for 30+ days -> retire.
- Flag has been at 0% for 30+ days and the feature is dead -> retire.
- Flag has not been flipped in 60+ days and no plan to flip -> investigate and retire or convert to a permission/ops flag with explicit ownership.
- Flag is referenced in fewer than 3 places in code -> trivially retirable; remove.

### Flag-debt audit cadence

Run a flag audit at least quarterly:
- List of all live flags.
- For each: type, owner, last toggle date, retirement date.
- Flag count delta vs last quarter.
- "Aged flag" report: flags older than 90 days that are not Ops or Permission.

## Naming conventions

A flag name is read more often than it is written. Conventions:

```
<scope>__<feature>__<purpose>__<version>
```

Examples:
- `web__checkout__new_flow__v2` (release toggle on web for new checkout flow v2)
- `api__search__relevance__experiment_q3` (experiment toggle in API)
- `infra__search__circuit_breaker` (ops toggle, permanent)
- `product__enterprise_admin__permission` (permission toggle, permanent)

Rules:
- **Scope first** -- web / mobile / api / infra. Lets you search "all checkout flags on web."
- **Feature second** -- the system surface, not the marketing name.
- **Purpose third** -- release / experiment / ops / permission. Often baked into name (`__test`, `__experiment`, `__permission`, `__rollout`).
- **Version when applicable** -- experiments and major UX redesigns benefit from version suffixes.
- **No team names in the flag name** -- teams reorg; flags outlive the team.
- **No customer names** -- exception: enterprise-specific permission flags can include the tenant id.
- **lowercase + underscores or double-underscores** -- avoid camelCase to keep search predictable.

## Dependency chains

A flag depends on another when feature A only makes sense if feature B is also enabled. Two rules:

1. **The dependency is encoded explicitly** in the flag service (e.g., LaunchDarkly prerequisites) or in code with a clear check.
2. **The rollout plan reflects the dependency** -- ramp the parent flag first, hold until stable, then ramp the child.

Dependency chains beyond 2-3 levels become unmanageable. If a flag depends on three other flags, the rollout plan needs flattening.

## Approval and audit trail

Flag flips on critical surfaces should require:
- **Pre-approved owner** -- who can flip without further sign-off (usually the team's PM + the on-call engineer).
- **Change log entry** -- automatic; every flip logged with who, when, what, why.
- **Two-person rule** for high-tier surfaces -- billing, auth, data deletion. One person proposes, another approves before flip.
- **Audit retention** -- 90+ days of flag-change history available to the on-call.

## Workflow

1. **Classify the flag** (release / experiment / ops / permission). The lifespan and ownership follow.
2. **Pick the rollout shape** (A-G above) and the gate criteria between stages.
3. **Define the kill-switch** thresholds and authority.
4. **Set the retirement date** (release/experiment toggles only). Add it to the team's flag-audit list.
5. **Name the flag** using the convention.
6. **Document the plan** in the `assets/rollout_plan_template.md`. Share with eng, on-call, sponsor.
7. **Wire the flag** (engineering side; PM does not do this).
8. **Ramp** through the stages, holding each step long enough for metrics to settle.
9. **Monitor**. Watch the same dashboard for each step. Declare each step a "green pass" before advancing.
10. **Retire** the flag when GA is stable. Add to next sprint's retirement PRs.
11. **Audit** flag inventory quarterly; remove stragglers.

## Tools

This skill is template-based; no Python tool. Artifacts are markdown plans.

| Template | Purpose |
|---|---|
| `assets/rollout_plan_template.md` | Per-feature rollout plan with stages, gates, owners, dates |
| `assets/kill_switch_decision_tree.md` | Pre-incident thresholds + authority + flip steps |
| `assets/flag_debt_retirement_checklist.md` | Flag-retirement workflow + quarterly audit |
| `assets/flag_naming_convention.md` | Naming sheet for the team |

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| Flag inventory has 200+ live flags | No retirement discipline; release toggles never deleted | Run a quarterly audit; mass-retire anything 100% > 30 days; lock new flag creation behind a retirement-date requirement |
| Rollback during incident requires a code revert | Flag is on but the rollback path is not wired | Every release toggle has a kill-switch path (single config change); rehearse the flip in non-prod once a quarter |
| Mobile feature flag broke users on old app version | Flag flipped before client adoption; no version gate | Always gate mobile flags on minimum client version; transition window of at least one release cycle |
| Two flags interact in unexpected ways | Implicit dependency; flag combinations not tested | Encode dependencies in the flag service; cover the cross-product in test matrix; flatten dependency chains > 2 levels |
| Experiment "shipped" but holdout was killed | Holdout retired with the experiment; no long-term measurement | Keep the holdout open for at least one retention horizon after launch; document re-exposure as a separate step |
| Owner of a flag has left the company | No ownership succession on flags | Flag ownership is by team, not by individual; team owner reviews the flag list during onboarding |
| Flag-flip incident: wrong person flipped | Permissions too loose; no two-person rule on critical flags | Critical surfaces require two-person approval; rotate the kill-switch authority to the on-call rota |
| Feature ramped to 100% but metrics never validated | No gate criteria between stages | Pre-agree the gate metrics; do not advance without a "green pass" from the owner |

## Success Criteria

- Every release / experiment toggle has a documented type, owner, kill-switch threshold, and retirement date.
- The rollout plan names the gate metric between each stage.
- The kill-switch can be flipped by the on-call without escalation.
- Mobile flags are gated on a minimum client version.
- Quarterly flag audit runs; flag count is stable or decreasing over time.
- Naming convention is enforced (linter or PR review).
- Experiments include a holdout that survives launch.
- Flag-debt retirement is part of every sprint, not a periodic cleanup.

## references/rollout-shape-comparison-guide.md

# Rollout Shape Comparison Guide

A side-by-side reference for the seven common rollout shapes, with use cases, risk profiles, and worked examples. Each shape implies a different gate-criteria pattern between stages.

## Quick comparison table

| Shape | Pattern | Risk profile | Time to GA (typical) | Best for |
|---|---|---|---|---|
| A. Linear ramp | 0 -> 1% -> 5% -> 25% -> 50% -> 100% | Low risk per step | 2-3 weeks | Most new features |
| B. Segmented | Internal -> Beta -> Free -> Paid | Risk varies by audience | 4-8 weeks | Features with explicit risk gradients |
| C. Geographic / regulatory | Region 1 -> Region cluster -> Global | Risk varies by region | 4-12 weeks | Features with regulatory / regional differences |
| D. A/B split with holdout | A 50% / B 45% / Holdout 5% | Risk per arm | 2-4 weeks (experiment) | A/B tests with long-term measurement |
| E. Dark launch (shadow) | 100% code, 0% UX | Performance / load risk only | 1 week | High-traffic system changes; AI features |
| F. Reverse ramp (sunset) | 100% -> 75% -> 25% -> 0% | Risk of customer churn | 4-26 weeks | Feature deprecation |
| G. Mobile forced-upgrade | Server enforces minimum client version | Risk of locking out users | 4-12 weeks | Mobile features requiring new client |

## Shape A: Linear ramp

### When to use

The default. Use for any new feature where you do not have strong segment-specific hypotheses and the surface is well-understood.

### Standard cadence

| Stage | % | Hold | Gate criteria |
|---|---|---|---|
| 1 | 1% | 24-48h | No error spike; p95 latency in band; no top-customer reports |
| 2 | 5% | 24-48h | Same |
| 3 | 10% | 24-48h | Same + adoption metric in band |
| 4 | 25% | 48-72h | Same + business KPI not regressed |
| 5 | 50% | 48-72h | Same |
| 6 | 100% | -- | Stable for 1-2 weeks; retire flag |

### Risk profile

- Smooth ramp; easy to roll back at any step.
- Gate criteria are mostly the same across steps; later steps add business-KPI checks.
- A 1% ramp catches outright bugs but rarely catches subtle behavioral issues -- those surface at 10-25%.

### Pitfalls

- Skipping steps under deadline pressure. Each step exists for a reason.
- Not waiting long enough for metrics to settle. New traffic can take 24+ hours to fully reflect in dashboards.
- Treating "no error spike" as the only gate. Behavioral metrics matter too.

## Shape B: Segmented (audience-first)

### When to use

Audiences have explicit risk gradients. Enterprise tenants run on stricter SLAs; consumer beta users tolerate more breakage.

### Example cadence

| Stage | Audience | Gate criteria |
|---|---|---|
| 1 | Internal employees | Used by 50+ employees for 1 week; no P0 |
| 2 | Friends-and-family invites | 200+ external users for 1 week; satisfaction >= 70% |
| 3 | Public beta opt-in | 1000+ users for 1-2 weeks; metric in band |
| 4 | Free tier | Full free-tier rollout; week of stable metrics |
| 5 | Pro tier | 1-2 weeks at 100% on free; no enterprise-impacting regression |
| 6 | Enterprise tier | All segments stable; account-level sign-off in place |

### Risk profile

- Higher tier customers have higher SLAs but you also reach them later -- this is intentional risk-shedding.
- Each segment is a different "blast radius" if something goes wrong.

### Pitfalls

- Going faster on segments that complain less. Free-tier users complain less but are still real users.
- Treating internal as "real testing." Employees are not customers; their workflow is not the customer's workflow.

## Shape C: Geographic / regulatory-aware

### When to use

Features have regulatory variance (EU AI Act tier-specific UX, GDPR consent flows, age-verification rules, region-specific payment methods).

### Example cadence

| Stage | Region | Gate criteria |
|---|---|---|
| 1 | One low-risk region (e.g., AU + NZ) | 1-2 weeks; no regulator inquiries |
| 2 | English-speaking cluster (US, UK, CA, AU, NZ) | 2-3 weeks; no escalations |
| 3 | EU (with GDPR + AI Act variants) | 2-4 weeks; legal review of consent flows |
| 4 | Asia (with regional adjustments) | Region-specific gates |
| 5 | Global, regulated regions | Last; explicit regulatory sign-off |

### Risk profile

- Earliest regions absorb the risk of new compliance flows.
- Legal/Compliance is on every gate.
- Region-specific UX variants live alongside the rollout flag; this can become complex quickly.

### Pitfalls

- Ignoring data-residency constraints (region 1 may not be allowed to process region 2 data).
- Underestimating regulatory review time -- often weeks, not days.

## Shape D: A/B split with holdout

### When to use

A/B experiments where the team wants to measure short-term lift (during the experiment) and long-term impact (weeks/months after launch).

### Example structure

| Arm | Allocation | Purpose |
|---|---|---|
| Control (A) | 47.5% | Existing behavior |
| Variant (B) | 47.5% | New behavior |
| Short-term holdout | 5% | Never exposed during experiment; baseline for long-term lift |
| (Optional) Long-term global holdout | 1-5% (separate) | Across all experiments; quarterly baseline |

### Gate criteria

- Pre-registered hypothesis and primary metric.
- Sample size calculated from minimum detectable effect.
- Experiment run window determined by sample size + traffic.
- Stat-sig threshold (often p < 0.05 with multi-testing correction).
- Counter-metrics monitored alongside primary.

### Risk profile

- Risk is bounded to the variant arm.
- Holdout protects against treatment-effect interactions during launch.
- Long-term holdout lets leadership attribute aggregate lift to the team's experiment portfolio.

### Pitfalls

- Peeking (looking at the experiment before completion) inflates false-positive rate.
- Killing the holdout to "ship faster." Reduces statistical confidence on long-term impact.
- Running too many experiments on the same surface simultaneously without orthogonal design.

## Shape E: Dark launch (shadow)

### When to use

- High-traffic system changes where you need to validate performance and error rate without user impact.
- AI features (per `ai-feature-prd/` Section 11.3) where the model output is mirrored, logged, and compared offline.
- Migrations where the new path must produce the same output as the old path.

### Example flow

```
Request hits the system.
|
+-- Old path runs; result returned to user.
|
+-- New path runs in parallel; result discarded (or logged for comparison).
|
+-- Compare logs offline; flag any divergence.
```

### Gate criteria

- New path's error rate within tolerance.
- New path's latency within tolerance.
- New path's output matches old path (where determinism is expected) or is acceptable (where it is not).
- No resource contention on the production path.

### Risk profile

- Lowest risk shape. User-visible behavior is unchanged.
- Cost is doubled for the duration of the shadow.

### Pitfalls

- Shadow runs forever. Set an exit criterion; do not let shadow become a permanent cost.
- Shadow load affects production. Throttle if necessary.
- Logging volume is enormous; sample if needed.

## Shape F: Reverse ramp (sunset)

### When to use

Retiring a feature. Customers need time to migrate; the team needs to validate they have.

### Example cadence

| Stage | Audience still exposed | Gate to next |
|---|---|---|
| 1 | 100% | Communication out; migration path live |
| 2 | 75% | Migration adoption > 30%; support team prepared |
| 3 | 50% | Migration adoption > 60%; no major-customer blockers |
| 4 | 25% | Migration adoption > 85%; escalations resolved |
| 5 | 10% | Migration adoption > 95%; remaining users identified |
| 6 | 0% | Feature removed; final EOL communication |

### Gate criteria

- Customer-facing communication ahead of each step (see `eol-communication/`).
- Migration adoption metric -- did the affected customer move to the new path?
- Major-customer-impact check -- nobody is locked out without preparation.

### Risk profile

- Each step risks customer churn.
- Communication is the primary control surface, not the toggle.

### Pitfalls

- Skipping communication; angry tickets follow.
- Treating "we announced it" as "we communicated it" -- watch the open / acknowledgment rates.
- Removing 100% of users in one step. Always taper.

## Shape G: Mobile forced-upgrade

### When to use

Mobile feature requires a new client version (new API, new permission, new SDK).

### Example flow

```
1. New client version released to app stores.
2. Adoption climbs over 2-4 weeks (most users update within 30 days).
3. Server-side flag: minimum supported client version.
4. Old clients see a "please update" screen on launch.
5. After full migration, old client paths can be removed.
```

### Gate criteria

- New client adoption > 80% before any forced flow.
- Two-week notice in the app and via email/push.
- Migration support for non-updatable devices (rare but real).

### Risk profile

- High user impact. A forced upgrade is friction.
- Mistakes cannot be rolled back from the client side -- must be fixed server-side.

### Pitfalls

- Forcing too early; users on slow networks or older devices get locked out.
- No alternative path for users who cannot update (corporate-managed devices, end-of-life OS).
- Forced upgrade message that does not explain why.

## Decision flow: which shape?

```
Is this a sunset / EOL?
  Yes -> Shape F (reverse ramp).
  No -> continue

Is this an A/B test with measurement requirements?
  Yes -> Shape D (split with holdout).
  No -> continue

Is the feature server-only and high-traffic?
  Yes -> Start with Shape E (dark launch) before any user exposure, then Shape A.
  No -> continue

Does the audience have explicit risk gradients?
  Yes -> Shape B (segmented).
  No -> continue

Are there regional / regulatory variants?
  Yes -> Shape C (geographic).
  No -> continue

Is this a mobile feature requiring a client version bump?
  Yes -> Shape G (forced upgrade) combined with Shape A on the server.
  No -> continue

Default: Shape A (linear ramp).
```

## Combining shapes

Most real launches combine shapes. Examples:

- **AI feature launch** = Shape E (dark) -> Shape B (internal -> beta -> all) -> Shape A (percent ramp).
- **EU regulatory launch** = Shape C (region) -> Shape D (with holdout for impact measurement).
- **Mobile + server** = Shape G (client adoption) -> Shape A (server percent ramp).

The rollout plan template (`assets/rollout_plan_template.md`) supports combined shapes; specify the sequence in the stages table.

---
**Last Updated:** 2026-05-22

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/feature-flag-strategy -->
