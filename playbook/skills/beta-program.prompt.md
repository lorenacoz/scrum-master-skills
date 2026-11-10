---
description: "Plan and run a closed beta: cohorts, exit gates agreed before recruiting, weekly cadence and a Greenlight/Extend/Pivot/Kill memo. Use when running a closed beta or design-partner program before general availability."
---

# Closed Beta Program Playbook

## Overview

A structured playbook for running a closed beta that produces clear learning, retained design partners, and an unambiguous decision on whether to proceed to general availability. Most betas fail not because the product is wrong, but because the program is run informally: recruitment is opportunistic, success criteria are implicit, communication is sporadic, and exit gates are never defined. This skill replaces all of that with concrete templates and decision rules.

A good closed beta runs 4-8 weeks, recruits 10-30 participants from three concentric cohorts ("friends, family, fanatics"), publishes a weekly cadence the team commits to, and exits on pre-agreed criteria rather than the calendar. The outputs are a beta program plan, a recruitment script, a weekly cadence template, and an exit memo that either greenlights GA, extends the beta, or kills the feature.

## When to Use

- **Pre-GA validation** -- A feature has cleared internal alpha but needs external validation under real workloads before a public launch.
- **High-risk feature** -- Significant blast radius, regulatory exposure, or pricing changes that warrant a controlled rollout to a small group first.
- **Design partner program** -- Recruiting a small set of customers whose feedback shapes v1 scope and pricing.
- **Enterprise rollout** -- New module that needs reference customers and case studies before broad sales enablement.

## When NOT to Use

- Continuous trunk-based delivery where every change ships to all users behind feature flags (use `launch-playbook/` and a progressive rollout instead).
- Pure usability testing with 5-7 participants (use a research protocol, not a beta program).
- Internal-only dogfooding (run a 2-week alpha with engineering and customer-facing staff).

## Clarify First

Before building the beta plan, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Beta hypothesis & headline outcome:** what you are trying to learn and the one result that matters (drives the whole plan and which exit gates you set).
- **Exit gates:** the quantitative + qualitative success criteria, agreed *before* recruiting (resolve to Greenlight / Extend / Pivot / Kill — the decision rule of the program).
- **Target cohort & size:** Friends / Family / Fanatics mix and participant count (drives the recruitment script and how you weight feedback).
- **Duration:** the 4-8 week window (drives the weekly cadence and when the exit memo is due).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Frame the beta hypothesis, target cohort and headline outcome (from `create-prd/`).
2. Set exit gates in `assets/beta-program-plan.md` and get PM, Eng and sponsor sign-off **before** recruiting. Gates set afterwards drift toward whatever the beta happened to show.
3. Recruit via `assets/recruitment-script.md`. Defaults [RECOMMENDED], to adjust for your context:
   - **Over-recruit about 2x:** roughly half of recruited participants go quiet by week 2, so 2x keeps the active cohort at target. A 6-account enterprise beta with contracted participants needs far less.
   - **Fanatics at 30% or more:** friends and colleagues are polite; cold-recruited users with active pain are the ones who report real friction.
   - **Weight Fanatic feedback about 2x** when tallying, for the same reason; say so in the exit memo.
4. Stand up the comms channel and publish the cadence on day 1; run it weekly (`assets/weekly-cadence-template.md`).
5. **Decide** at the pre-agreed date with `assets/exit-memo.md`: Greenlight, Extend, Pivot or Kill, against the gates as written.

**Done when** the exit memo records each gate's result against its pre-agreed threshold and a decision signed by the same people who signed the gates.

Framework tables, troubleshooting and success criteria: `references/beta-framework.md`.

## Anti-Patterns

### Recruiting only friends
**Mistake:** The cohort is 30 employees and 5 advisor friends, with no Fanatics cold-recruited from the ICP.
**Why it happens:** Friends say yes within two days, and cold recruiting is slow.
**Instead:** Sequence Friends, then Family, then Fanatics, and keep Fanatics at 30% of the cohort or more. Screen them for active pain in the problem area.

### Recruitment that leads with the feature
**Mistake:** The outreach email opens "We're launching an exciting new AI assistant, want to try it?"
**Why it happens:** The team is proud of what it built and leads with it.
**Instead:** Name the participant's problem in the first paragraph, then the ask (hours per week, duration) and the payoff. Target people who described this pain in discovery, starting from `assets/recruitment-script.md`.

### Building one-offs for a single participant
**Mistake:** The largest beta customer asks for a custom export format, and engineering builds it in week 3 for that customer alone.
**Why it happens:** The participant is a paying account, and keeping them happy feels like protecting the beta.
**Instead:** Log the request in the `customer-feedback-triage/` queue with the rest of the beta input. Commit to it for v1.1 only if the broader signal supports it, and track sales-promised customizations separately.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `assets/beta-program-plan.md` | Plan template: gates, cohort sizing, timeline |
| `assets/recruitment-script.md` | Outreach templates for the three cohorts, screening questions |
| `assets/weekly-cadence-template.md` | Monday digest, office hours, review, Friday snapshot |
| `assets/exit-memo.md` | Exit decision memo (Greenlight / Extend / Pivot / Kill) |
| `examples/shared-dashboards-closed-beta.md` | Worked beta |

## References

- `references/beta-framework.md` -- Full framework (cohort, Kano, success gates, cadence, exit gates), the 8-step workflow, troubleshooting matrix, and success criteria. Read this when building the plan, setting gates, running the cadence, or diagnosing problems.
- `references/beta-program-guide.md` -- Practical reference guide: why betas fail, cohort sequencing, Kano deep dive, exit-gate worked examples, common failure modes. Read this for narrative depth and worked examples.
- `references/red-flags.md` -- Bad-vs-good examples for the beta plan, recruitment script, cadence, and exit memo. Read this to review beta artifacts before opening recruitment.
- Kano, Noriaki. "Attractive Quality and Must-Be Quality." Journal of the Japanese Society for Quality Control, 1984.

## Scope & Limitations

**In Scope:**
- Closed beta planning, recruitment, cadence, and exit-gate decisions
- Three-cohort sequencing (Friends, Family, Fanatics)
- Kano scoping for beta feature set
- Weekly communication templates and exit memo
- Beta-to-GA handoff to `launch-playbook/`

**Out of Scope:**
- Public open beta or waitlist management (different mechanics; treat as a soft launch via `launch-playbook/`)
- A/B testing and statistical experiment design (see `discovery/brainstorm-experiments/`)
- Pricing experiments (run a dedicated pricing test, not piggybacked on beta)
- Marketing campaign execution for the beta (light recruitment only; full GTM lives in `launch-playbook/`)

**Important Caveats:**
- A 30-person closed beta is not statistically representative. Treat outcome metrics as directional, not conclusive.
- Friends-cohort feedback is biased toward "this is great" -- weight Fanatics-cohort feedback 2x in the exit decision.
- If your beta participants are also paying customers, any service disruption is a real incident. Run beta features behind a feature flag with a documented rollback path (see `delivery-manager/`).

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `create-prd/` | Receives from | PRD defines the hypothesis and headline outcome that beta gates measure |
| `discovery/identify-assumptions/` | Receives from | Riskiest assumptions become the beta's primary learning goals |
| `discovery/brainstorm-experiments/` | Complementary | Beta is one experiment type; brainstorm-experiments covers smaller/faster alternatives |
| `daci-framework/` | Uses | DACI driver owns the exit-gate decision |
| `launch-playbook/` | Feeds into | Greenlit beta hands testimonials, case studies, and known issues to launch |
| `release-notes/` | Feeds into | Beta release notes preview the GA changelog |
| `summarize-meeting/` | Complementary | Office hours and 1:1 notes become structured weekly summaries |
| `senior-pm/` | Reports to | Exec sponsor receives the exit memo and signs the GA decision |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/beta-framework.md

# Closed Beta Framework, Workflow & Troubleshooting

Read this when you are building the beta plan, setting exit gates, running the weekly cadence, or diagnosing a beta that is going sideways. Contains the full framework tables (cohorts, Kano scope, success gates, cadence, exit gates), the step-by-step workflow, the troubleshooting matrix, and success criteria moved verbatim from `SKILL.md`.

## The Closed Beta Framework

### Cohort Design: Friends, Family, Fanatics

A widely-used pattern among early-stage operators for sequencing beta recruitment in three concentric rings of decreasing trust and increasing signal.

| Cohort | Who | Goal | Typical Size | Tolerance for Rough Edges |
|--------|-----|------|--------------|---------------------------|
| **Friends** | Internal employees, advisors, immediate network | Find the worst bugs without reputational risk | 5-10 | Very high |
| **Family** | Existing customers who explicitly opted in, design partners | Validate the workflow fits real jobs and produces value | 10-20 | High |
| **Fanatics** | Cold-recruited prospects matching the ICP who actively want to solve the problem | Validate that the feature drives acquisition, not just retention | 10-15 | Medium |

Run the cohorts sequentially (Friends -> Family -> Fanatics) or with deliberate overlap. Do not skip Friends to "save time" -- this is where every embarrassing crash should surface.

### Kano Model for Beta Scope

Use the Kano model (Noriaki Kano, 1984) to decide what is in scope for the beta build:

| Kano Category | Definition | Beta Decision |
|---------------|------------|---------------|
| **Must-be** | Basic expectations; absence causes immediate dissatisfaction | Must be present and stable on day 1 of beta |
| **Performance** | More-is-better attributes that scale with investment | Include enough to demonstrate the value curve |
| **Delight** | Unexpected features that produce strong positive reactions | Pick 1-2 delight features for the beta -- this is where you generate quotes for the launch |
| **Indifferent** | Features the user does not care about | Cut from beta scope; revisit post-GA |
| **Reverse** | Features that some users actively dislike | Make them opt-in; track who turns them off |

The most common mistake is shipping a beta with only Must-be features. Without at least one Delight feature, your beta produces neutral feedback and no quotable testimonials.

### Beta Success Criteria (Set Before Recruitment)

Define quantitative and qualitative gates before opening recruitment. If you set them after the beta starts, they will be rationalized to match what you already see.

| Gate Type | Example Metric | Example Target |
|-----------|----------------|----------------|
| **Activation** | % of beta users who reach the first key action within 7 days | >= 70% |
| **Engagement** | Median sessions per active beta user per week | >= 3 |
| **Retention** | % of beta users still active in week 4 | >= 60% |
| **Outcome** | % of beta users who achieve the headline outcome (saves X minutes, reduces Y, etc.) | >= 50% |
| **NPS / CSAT** | Net Promoter Score within the beta cohort | >= 30 |
| **Crash-free sessions** | Crash-free session rate across beta | >= 99.5% |
| **P0 bug count** | Open P0 bugs at exit-gate review | 0 |
| **Quotable testimonials** | Named customers willing to be quoted in launch materials | >= 3 |

### Weekly Communication Cadence

A beta dies of silence. Commit to a weekly rhythm and publish it to participants on day 1.

| Day | Action | Owner |
|-----|--------|-------|
| **Monday** | Weekly digest to participants: what shipped, known issues, what to try this week | PM |
| **Tuesday** | Office hours (30 min open Zoom or async thread) | PM + Eng Lead |
| **Wednesday** | Internal beta health review: metrics, bugs, themes | PM |
| **Thursday** | One-on-one with rotating subset (2-3 participants/week) | PM or PMM |
| **Friday** | Weekly metrics snapshot posted to participants Slack/Discord | PM |

### Beta-to-GA Exit Gates

At the end of the planned beta window (typically 4-8 weeks), run an exit-gate review against the pre-agreed criteria. There are exactly four outcomes:

1. **Greenlight GA** -- All gates met. Proceed to launch using `launch-playbook/`.
2. **Extend beta** -- Most gates met, 1-2 gaps with a clear plan to close in 2-4 more weeks.
3. **Pivot** -- Engagement/outcome gates failed; usage pattern reveals a different job-to-be-done. Rewrite the PRD.
4. **Kill** -- Both engagement and outcome gates failed with no compelling alternative pattern. Write the postmortem and free the team.

The decision should be made by the DACI driver (see `daci-framework/`) with documented input from engineering, design, marketing, and at least one beta participant.

## Workflow

1. **Frame the beta.** Define the hypothesis, the target cohort definition, and the headline outcome you expect beta users to achieve. Reference the PRD from `create-prd/`.
2. **Set exit gates.** Fill in `assets/beta-program-plan.md` with quantitative and qualitative gates. Get explicit sign-off from PM, Engineering, and the executive sponsor.
3. **Build the recruitment funnel.** Use `assets/recruitment-script.md` to draft outreach for each of the three cohorts. Aim to over-recruit by 2x (expect 50% activation).
4. **Stand up the participant comms channel.** Slack Connect, Discord, or shared email list. Publish the weekly cadence on day 1.
5. **Run the cadence.** Hold weekly Monday digests, Tuesday office hours, Wednesday internal reviews, Thursday 1:1s, Friday metric snapshots. Use `assets/weekly-cadence-template.md`.
6. **Run the exit-gate review.** At week N, populate `assets/exit-memo.md` with actual data vs. each gate. The DACI driver picks one of the four outcomes.
7. **Communicate the decision.** Tell participants what happens next: GA timeline, extension plan, pivot, or sunset. Honor any commitments (early access, pricing, credits).
8. **Hand off to launch.** If greenlit, hand the beta artifacts (testimonials, case studies, known issues, gate data) to `launch-playbook/`.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Recruitment misses target by >50% | Recruitment script led with features instead of the participant's pain; cohort definition too narrow | Rewrite outreach to lead with the problem and the participant's payoff; widen the cohort by one dimension (industry, role, or company size) |
| Engagement collapses after week 2 | No clear "what to try this week" prompt; users hit a rough edge and bounced | Re-establish the Monday digest with a specific weekly task; ship a hotfix for the top friction point within the same week |
| Beta participants stop responding to outreach | Cadence is too heavy or asks generic questions | Cut to one async ping per week with a specific question tied to that week's release; offer credits for completed feedback |
| Exit-gate metrics look good but team has no quotes | Beta lacked Delight features; outreach never asked for permission to quote | Add 1-2 Delight features in an extension week; explicitly ask for quotable testimonials in the week-3 1:1 |
| Exec sponsor pushes to skip exit gates and ship | Gates were set without sponsor buy-in; gates conflict with a hard launch date | Re-run the decision with the DACI driver; document the override and the risk in `assets/exit-memo.md` |
| Beta drags 12+ weeks with no decision | No pre-agreed exit window; team keeps adding scope | Enforce a 6-week default; any extension requires a written 2-week plan with measurable gates |
| Participants leak the beta publicly | NDA was implied, not explicit; participants felt the embargo was unfair | Send a one-page beta agreement at activation; offer an early-public-praise window in the final week to channel enthusiasm |

## Success Criteria

- Recruitment hits >= 100% of the planned cohort size across all three rings (Friends, Family, Fanatics).
- Exit-gate criteria are documented, quantitative, and signed off before recruitment opens.
- Weekly cadence runs every week of the beta with documented attendance and themes.
- At least 50% of activated participants achieve the headline outcome by the exit-gate review.
- The exit-gate review produces a single documented decision (Greenlight / Extend / Pivot / Kill) within 5 business days of beta end.
- At least 3 named participants agree to be quoted in launch materials.
- Beta artifacts (gate data, testimonials, known issues, customer requests) are handed off to the launch team in a single bundle.

## references/beta-program-guide.md

# Closed Beta Program Reference Guide

A practical reference for running closed betas that produce real learning and clean GA decisions. This guide expands on the patterns in `SKILL.md` and includes worked examples, anti-patterns, and decision rules drawn from common SaaS and B2B beta programs.

---

## 1. Why Most Betas Fail

Across post-mortems of failed betas, the same five causes recur:

1. **No pre-agreed exit gates.** The team starts the beta with a vague "let's see how it goes." When the launch date approaches, success criteria are reverse-engineered to match whatever the data shows.
2. **Recruitment is opportunistic.** PMs sign up whoever raises a hand. The resulting cohort is heavily skewed toward super-fans who would have loved anything.
3. **Communication collapses after week 2.** Engineering is heads-down on bug fixes; PM is fielding 1:1 requests; nobody owns the weekly digest. Participants drift.
4. **No delight features.** The beta is all Must-be features. Engagement is fine, but no participant says anything memorable. Launch lacks quotes.
5. **The decision is never made.** The beta drags 12+ weeks. Engineering moves on. The feature ships by default without a real GA decision.

Every section below maps to one of these failure modes.

---

## 2. Cohort Sequencing: Friends, Family, Fanatics

### Sequencing Logic

| Phase | Cohort | Duration | Primary Question |
|-------|--------|----------|------------------|
| **Phase 1** | Friends | Week 1-2 | Does it run at all? What is most embarrassing? |
| **Phase 2** | Family | Week 2-5 | Does it fit a real workflow and produce value? |
| **Phase 3** | Fanatics | Week 4-8 | Would a stranger pay for this? |

Phases overlap deliberately. By week 4, all three cohorts are active and the comparison across them is the most valuable signal in the beta.

### Cohort Recruitment Targets

| Cohort | Recruitment Channel | Conversion to Active | Recommended Outreach Volume |
|--------|--------------------|--------------------:|----------------------------:|
| Friends | Internal Slack, advisor network | 80-90% | 1.2x cohort size |
| Family | CS warm intros, existing-customer email | 30-50% | 3x cohort size |
| Fanatics | Cold outreach, LinkedIn, community | 5-15% | 10x cohort size |

If Fanatics conversion is below 5%, the problem is your value proposition, not your outreach. Pause Fanatics recruitment and rerun positioning before scaling.

### Cohort Bias Adjustment

Weight feedback by cohort distance from your team:

- Friends-cohort positive feedback: weight **0.5x** (assume bias toward niceness)
- Family-cohort feedback: weight **1.0x** (closest to baseline)
- Fanatics-cohort feedback: weight **2.0x** (this is your acquisition signal)

For example, a 4.8/5 satisfaction from Friends and 3.2/5 from Fanatics is a real warning sign even though the blended average looks fine.

---

## 3. Kano Model for Beta Scope

The Kano model distinguishes five categories of features by how user satisfaction responds to investment.

```
Satisfaction
   ^
   |                           Delight (curve: starts low, accelerates up)
   |                          /
   |                         /
   |               Performance (linear: more = better)
   |              /
   |  ----------+----------> Investment
   |          /
   |         /
   | Must-be (curve: starts very low, plateaus at "neutral")
```

### Beta Scoping Decisions

| Category | Beta Scoping Rule |
|----------|-------------------|
| **Must-be** | All Must-be features ship before beta day 1. Cutting one of these is a non-starter -- the beta will produce "this is broken" feedback that drowns everything else. |
| **Performance** | Ship enough Performance features to demonstrate the value curve. You do not need to be best-in-class on every Performance axis. |
| **Delight** | Pick 1-2 Delight features. These are where you generate quotable testimonials. If you ship zero Delight features, your beta produces neutral feedback and no launch story. |
| **Indifferent** | Cut from beta. Revisit post-GA if usage data supports it. |
| **Reverse** | Make opt-in. Track who turns them off; that data will help with GA positioning. |

### Worked Example: Beta Scope Decision

A team building a new dashboard feature could ship:
- Filters (Must-be)
- Saved views (Must-be)
- CSV export (Performance)
- Schedule daily email digest (Performance)
- AI-generated narrative summary (Delight)
- White-label theming (Indifferent for the beta cohort)
- Forced password rotation (Reverse)

**Good beta scope:** All Must-bes + 1 Performance (CSV) + 1 Delight (AI summary). Drop the rest.

**Bad beta scope:** All Must-bes + every Performance feature + zero Delights. The beta will run, but no participant will be excited.

---

## 4. Exit-Gate Design

### Gate Categories (Set Before Recruitment)

Every gate is one of four categories:

| Category | Question Answered | Example Gate |
|----------|-------------------|--------------|
| **Activation** | Are participants reaching first value? | >= 70% reach the first key action in 7 days |
| **Engagement** | Are participants using it repeatedly? | Median >= 3 sessions/week in week 2-4 |
| **Outcome** | Are participants getting the promised result? | >= 50% achieve the headline outcome |
| **Quality** | Is the product stable enough to ship? | 0 open P0 bugs, >= 99.5% crash-free sessions |

### The "Quotable Testimonials" Gate

The most-skipped gate, and the one that hurts launches most. Set an explicit target (typically 3-5 named customers willing to be quoted). Ask in the week-3 1:1 with a specific draft quote ("If we wrote: '<draft>' -- could we attribute that to you?"). Get written permission before the exit-gate review.

### Anti-Pattern: Vanity Gates

Avoid:

- "Positive feedback overall" -- not measurable.
- "Beta participants are happy" -- happy with what?
- "No critical issues" -- define critical.

Replace with quantified targets, baselines, and review owners.

---

## 5. The Four Exit-Gate Outcomes

Every beta ends in exactly one of these four outcomes. The DACI driver picks one within 5 business days of beta end.

### 5.1 Greenlight GA

**Conditions:** All gates met or all gaps explicitly accepted with mitigation.

**Next steps:** Hand off to `launch-playbook/` with the testimonial bundle, known-issues list, and pricing recommendation.

### 5.2 Extend Beta

**Conditions:** Most gates met, 1-2 specific gaps with a clear plan to close in 2-4 more weeks.

**Required artifacts:**
- Written extension plan with exact gaps, target dates, and gate owners.
- Communication to participants explaining the extension and any new commitments.
- New exit-gate review date on the calendar.

**Anti-pattern:** Extending "to keep learning" without a specific gap or close plan. This is how betas drag 12+ weeks.

### 5.3 Pivot

**Conditions:** Engagement or outcome gates failed, but usage pattern reveals a different job-to-be-done that the team wants to pursue.

**Required artifacts:**
- Rewritten PRD (see `create-prd/`) reflecting the new hypothesis.
- Honest postmortem on why the original hypothesis failed.
- Communication to participants -- some will follow you to the new direction, most will not.

### 5.4 Kill

**Conditions:** Both engagement and outcome gates failed, with no compelling alternative pattern in the usage data.

**Required artifacts:**
- Postmortem covering: original hypothesis, what we learned, why we are killing it, what we will not try again.
- Sunset communication to participants (see `eol-communication/`).
- Engineering effort estimate to remove the code or leave it dormant behind a flag.

Killing a beta is a successful outcome when the data supports it. The cost of killing now is far lower than shipping a feature nobody uses for the next 3 years.

---

## 6. Communication Cadence: What to Send and When

### Monday Digest (PM owns)

- What shipped last week (commits/tickets, plain language)
- Known issues (with workarounds)
- What we want you to try this week (specific task tied to a gate)
- Office hours reminder

### Tuesday Office Hours (PM + Eng Lead)

- 30 minutes, optional, async-friendly thread alternative
- Open agenda; PM posts seed questions if quiet

### Wednesday Internal Review (PM owns)

- Gate metrics snapshot
- Top 3 bugs by occurrence
- Top 3 feature requests by frequency
- Risk register update

### Thursday 1:1s (PM rotates participants)

- 2-3 participants per week
- 30 minutes each
- Standing questions: What is working? What is broken? What is missing? Would you renew/recommend? Can we quote you on X?

### Friday Snapshot (PM owns)

- One screenshot of the gate dashboard
- One sentence on the week's biggest learning
- One thank-you naming individual contributors from the beta cohort

---

## 7. NDA, Pricing, and Commitments

### NDA

A one-page mutual NDA is standard for closed betas. Send it at activation, not at recruitment, so it does not slow the funnel.

### Pricing

Three common patterns:

1. **Free during beta, full price at GA.** Simple. Use when beta is short (<6 weeks).
2. **Free during beta, discounted price for the first 6-12 months post-GA.** Good for design partners; rewards early commitment.
3. **Paid beta at a discounted rate.** Only when participants are getting clear value from day 1; signals seriousness.

Avoid: "We'll figure out pricing later." Participants will assume the lowest possible price.

### Commitments to Honor

If you promise:

- Early access -- give it.
- Pricing lock -- honor it for the stated period.
- Credits for feedback -- track and pay them.
- Reference customer status -- ask before quoting publicly, every time.

Beta participants who feel jerked around become the loudest detractors at GA.

---

## 8. Common Beta Failure Patterns (and Fixes)

| Pattern | Symptom | Fix |
|---------|---------|-----|
| **Recruitment over-reliance on Friends** | 90% of beta is internal or advisors; engagement metrics look great; no Fanatics | Hard-cap Friends at 25% of cohort; require equal Family and Fanatics sizing |
| **Silent participant** | One participant activates and never returns | Personal outreach in week 1 with one specific ask; if no response in 5 days, replace from waitlist |
| **The "beta forever" trap** | Beta runs 6+ months; team forgets why; feature ships by default | Enforce hard 8-week max; any extension is a new beta with new gates |
| **Bug-only beta** | All feedback is bug reports; no outcome signal | Add 1 outcome-focused question to every weekly digest; remove low-priority bugs from the participant Slack to reduce noise |
| **Pricing surprise** | Beta participants churn at GA when invoice arrives | Tell participants the exact GA price in the week-1 digest; offer a written commitment for the first renewal |
| **The "PM-vendor" trap** | Beta participants treat PM as their personal account manager; PM loses 50% of time on ad-hoc requests | Establish a single async channel for asks; batch responses 2x/week; route operational issues to CS |
| **Exit decision made in private** | Decision happens in a hallway conversation; no documented memo | Require a written exit memo using `assets/exit-memo.md`; circulate before any GA commitment |

---

## 9. Beta-to-GA Handoff Checklist

Before handing off to `launch-playbook/`:

- [ ] Exit memo signed by PM, Engineering, and exec sponsor
- [ ] At least 3 quotable testimonials with written permission
- [ ] Known-issues list with status and GA-day plan
- [ ] Pricing decision finalized
- [ ] Beta participant communication scheduled for launch day
- [ ] Sales enablement bundle (case studies, FAQ, objection handling)
- [ ] Support team trained on the feature
- [ ] Marketing has access to all assets at least 2 weeks before launch

---

## 10. References

- Kano, Noriaki. "Attractive Quality and Must-Be Quality." Journal of the Japanese Society for Quality Control, 14(2), 1984.
- Cagan, Marty. *Inspired: How to Create Tech Products Customers Love*. Wiley, 2018. (Chapter on customer discovery programs.)
- Olsen, Dan. *The Lean Product Playbook*. Wiley, 2015. (MVP definition, value proposition testing.)
- Reichheld, Fred. "The One Number You Need to Grow." Harvard Business Review, 2003. (NPS methodology.)

## references/red-flags.md

# Red Flags: Beta Program

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the beta plan, recruitment script, weekly cadence, and exit memo for these patterns before opening recruitment. Each red flag shows the *bad* version next to the *good* version, anchored to the Friends/Family/Fanatics cohort model and Kano scope decisions.

---

## Red Flag 1: Vanity recruit (friends only)

**Symptom.** The recruitment list is 25 internal employees and 5 personal contacts. No Fanatics cohort cold-recruited from the ICP.

**Why it's bad.** Friends-cohort feedback is biased toward "this is great". Without Fanatics — cold-recruited prospects with the actual problem — the beta validates how the team uses the product, not whether the market wants it. The exit memo reads positive; GA flops.

**Bad example:**
> "Beta cohort: 30 employees from the engineering org + 5 advisor friends. Recruitment complete in 2 days."

**Good example:**
> "Beta cohort across 3 rings: 8 Friends (employees + 2 advisors); 15 Family (existing customers who opted in via product update email, screened for active use of the legacy feature); 12 Fanatics (cold-recruited via 2 industry Slack groups + LinkedIn outreach, ICP-screened for active pain in this area). 35 total; sequenced Friends -> Family -> Fanatics with 1-week overlap."

**How to catch it.** Count Fanatics. If under 30% of the cohort, the beta will not test acquisition risk.

---

## Red Flag 2: No exit criteria set before recruitment

**Symptom.** The team opens recruitment with placeholder metrics ("we'll figure out success when we see it"). Exit memo gets backfilled with whatever the data showed.

**Why it's bad.** Without pre-agreed gates, the exit decision becomes a vibe check. The exec sponsor will rationalize ship-it or kill-it based on the loudest signal. The exit memo loses defensibility.

**Bad example:**
> "Beta success: 'users like it'. Exit gate: 'team decides at end of week 6'."

**Good example:**
> "Exit gates, signed by PM + Eng Lead + Exec Sponsor on 2026-04-30, locked in `assets/beta-program-plan.md`: (1) Activation: >= 70% reach first key action in 7 days. (2) Engagement: median >= 3 sessions/week. (3) Outcome: >= 50% achieve the 'reduces close time by 30%' headline. (4) Crash-free: >= 99.5%. (5) P0 bugs: 0 open at exit. (6) Quotable testimonials: >= 3 named participants. Failure on any 2 of the first 4 = Extend or Pivot decision."

**How to catch it.** Look at the exit memo template. If thresholds are blank or vague, recruitment must wait.

---

## Red Flag 3: Beta-as-launch

**Symptom.** The "beta" is announced via a launch press release. 5,000 sign-ups expected. Marketing is treating it as soft GA.

**Why it's bad.** This is not a beta — it is an under-resourced launch with the word "beta" attached. 5,000 users at unknown stability is a support crisis. Feedback signal at that volume becomes noise. The actual purpose of beta (controlled learning before GA) is lost.

**Bad example:**
> "Beta launch: announced on TechCrunch + blog + 50k-subscriber newsletter. 'Sign up for the beta — limited spots' (no actual cap configured). Day 1: 3,200 signups."

**Good example:**
> "Closed beta: 30 invited participants across 3 cohorts. Recruitment via 1:1 outreach, not public announcement. Beta is not press-worthy at this stage. If we want a soft launch with broader audience, that is a separate decision after the closed beta exit; see `launch-playbook/`."

**How to catch it.** Count target participants. > 50 is no longer "closed beta" in most contexts.

---

## Red Flag 4: No Delight features in beta scope

**Symptom.** Beta ships with only Must-be features (Kano basic). Feedback at exit is neutral; no quotable testimonials.

**Why it's bad.** Must-be features generate no positive surprise — users notice their absence but not their presence. Without 1-2 Delight features, beta produces neutral feedback and no quotes for the launch press release.

**Bad example:**
> "Beta scope (v1): login, dashboard, basic CRUD on the main object, settings page. 'Keep it minimal so we don't have to fix bugs.'"

**Good example:**
> "Beta scope: all Must-be features stable (login, dashboard, CRUD). Plus 2 Delight features: (1) auto-summary of the user's last 7 days of activity on first dashboard load, (2) one-click export to the user's preferred BI tool. Delights are where we will get quotable testimonials; we accept the bug-fix cost."

**How to catch it.** Review the scope. Tag each feature Must-be / Performance / Delight. If 0 Delight features, the beta will produce no quotes.

---

## Red Flag 5: Silent cadence

**Symptom.** The team sends 1 welcome email on day 1, then nothing until week 4. Engagement crashes after week 2.

**Why it's bad.** A beta dies of silence. Participants who do not hear from the team within a week assume the program stalled. They disengage; the team gets no signal. The cadence is not optional — it is the program.

**Bad example:**
> "Comms plan: welcome email day 1; 'we'll check in periodically with updates and questions'."

**Good example:**
> "Weekly cadence (locked in `assets/weekly-cadence-template.md`):
> Mon — digest: what shipped, known issues, one specific thing to try this week.
> Tue — 30-min open office hours (Zoom).
> Wed — internal beta health review (PM).
> Thu — 2-3 1:1s with rotating participants.
> Fri — metrics snapshot to the participant Slack.
> Owner: PM. SLA on participant question: 1 business day."

**How to catch it.** Open the participant Slack at week 2. If the team has not posted in 5+ business days, the program is silent.

---

## Red Flag 6: Recruitment leads with features instead of problems

**Symptom.** The outreach email opens "We're launching an exciting new AI assistant — want to try it?" Conversion rate is 4%.

**Why it's bad.** Feature-led recruitment attracts curiosity, not pain. Curious users don't activate; the cohort fills with people who never had the problem the product solves. Outcome metrics fail at exit because the wrong people were in the cohort.

**Bad example:**
> "Subject: Try our new AI assistant before anyone else! Body: 'We're launching a powerful new AI assistant. We'd love your feedback. Sign up here.'"

**Good example:**
> "Subject: Beta — close deals 30% faster with auto-research. Body: 'You mentioned in our last call that pre-meeting research takes 90+ minutes per opportunity. We are testing a tool that compresses that to 10 minutes. We're inviting 15 sales leaders to a closed 6-week beta starting May 28. The ask: 2 hours/week using the product + a 30-min weekly chat. The payoff: you get the tool 4 months before GA and shape v1. Reply if interested.' Targeting: prospects who explicitly named this pain in discovery."

**How to catch it.** Read the recruitment email. If the first paragraph names the product before naming the problem, rewrite.

---

## Red Flag 7: Exit-gate metrics from a 5-person cohort

**Symptom.** Exit memo shows "80% activation" — but n = 5. Sponsor wants to ship.

**Why it's bad.** A 5-person beta is not statistically representative. Eight users out of 10 reaching activation tells you very little about the broader population. Treating that as a green light to GA ignores the variance.

**Bad example:**
> "Exit memo: 8/10 activated (80%). Outcome achieved by 6/10 (60%). Greenlight GA."

**Good example:**
> "Exit memo: cohort size n=30 (Friends 8, Family 14, Fanatics 8). Weighted scoring per the Caveats section: Fanatics weighted 2x. Activation: Friends 7/8 (88%), Family 10/14 (71%), Fanatics 5/8 (63%). Weighted: 71% — above 70% gate. Outcome: 4/8 Fanatics (50%) — meets gate but with low margin and small n. Decision: Extend beta 2 weeks to add 10 more Fanatics before greenlighting."

**How to catch it.** Compute n. If under 20, your gate numbers should be advisory at best.

---

## Red Flag 8: Friends-cohort feedback weighted equally

**Symptom.** Exit memo treats all participant feedback equally. Friends-cohort enthusiasm carries the average.

**Why it's bad.** Friends are biased toward saying "this is great" — they want the project to succeed. Family is moderately biased. Fanatics — cold-recruited with the actual pain — give the cleanest signal. Treating them equally inflates the apparent quality.

**Bad example:**
> "NPS: Friends 65, Family 40, Fanatics 25. Average: 43. Above the 30 gate."

**Good example:**
> "NPS by cohort: Friends 65, Family 40, Fanatics 25. Per the SKILL.md guidance, Fanatics weighted 2x in the exit decision (they represent the acquisition risk). Weighted score: (65 + 40 + 25*2) / 4 = 38.75. Discussion at exit-gate review: Fanatics NPS of 25 is concerning. What did they say about the gap? Do we extend beta to investigate, or is this a fundamental fit problem?"

**How to catch it.** Look for separate Fanatics-cohort metrics in the exit memo. If they're aggregated with Friends, weighting is being skipped.

---

## Red Flag 9: No explicit NDA or beta agreement

**Symptom.** The team assumes participants understand confidentiality. A Fanatics-cohort participant posts a feature screenshot to LinkedIn in week 3.

**Why it's bad.** Implied NDAs are unenforceable and create surprise. The leak forces an awkward correction; the leaker feels accused. Competitors see the feature early.

**Bad example:**
> "Participant onboarding email: 'We'd appreciate you keeping this confidential while we're in beta. Thanks!'"

**Good example:**
> "Activation packet includes: (1) one-page beta agreement signed via DocuSign (confidentiality for 90 days, ownership of feedback, no-warranty disclaimer). (2) Explicit list of what they can/cannot share — internally with their team yes, externally no until launch. (3) An early-public-praise window in the final week to channel enthusiasm legitimately. Reviewed with Legal."

**How to catch it.** Ask: "Show me the signed beta agreement for participant X." If none exists, the NDA is implied.

---

## Red Flag 10: Exit drags past planned window

**Symptom.** Beta planned for 6 weeks. Now in week 11, no exit decision. Team keeps adding features.

**Why it's bad.** Open-ended betas consume budget and morale. The team uses "still in beta" as an excuse to keep iterating instead of committing to GA or kill. Participants disengage; their feedback fatigues.

**Bad example:**
> "Week 11 update: 'still in beta — making good progress. Will revisit timeline next week.'"

**Good example:**
> "Beta was 6 weeks. At week 6 the exit memo went to the DACI driver. Outcome: Extend by 2 weeks to close the Fanatics-cohort activation gap with named action items. At week 8: definitive Greenlight / Extend / Pivot / Kill decision; no further extensions. If extension #2 is needed, the program is restructured as a new closed-beta cohort, not a continuation."

**How to catch it.** Look at the start date and the exit-memo date. If exit is > 8 weeks from start with no decision, the program has slipped from beta to "limbo".

---

## Red Flag 11: One-off enterprise customizations during beta

**Symptom.** The largest beta customer says "we'd buy this if it did X". Engineering builds X for that one customer. Other participants don't get it.

**Why it's bad.** Customization during beta produces a product that ships for one customer and ships poorly for everyone else. It also conflates the beta (learning) with sales (closing). The team optimizes for the loudest paying voice.

**Bad example:**
> "Acme Corp asked for a custom export format; eng built it in week 3 to keep them happy. Week 5: another participant asks for a different custom format."

**Good example:**
> "Acme Corp request logged in the customer-feedback-triage queue. PM responds: 'we hear you; this is going through our triage with the other beta input. We will commit to it in v1.1 if the broader signal supports it.' No mid-beta one-offs. Sales-promised customizations are tracked separately and reported monthly per `customer-feedback-triage/` discipline."

**How to catch it.** Ask the build team: "Have you built anything for one beta participant that the others don't have?" If yes, the program is drifting to bespoke.

---

## Red Flag 12: Decision deferred past the 5-day SLA

**Symptom.** Beta ends. Exit memo not published until 3 weeks later. Decision deferred to the next exec offsite.

**Why it's bad.** Delay erodes momentum. Participants lose context; engineering loses focus. The "GA timeline" becomes mythical. The DACI driver loses authority; the decision becomes consensus mush.

**Bad example:**
> "Beta ended May 12. Exit memo due 'soon'. GA decision: 'we will discuss at the quarterly review on June 28.'"

**Good example:**
> "Beta ended May 12. Per DACI: PM (Sarah K) is the Driver. Exit memo committed for May 17 (5 business days). Review meeting May 18. Documented decision (Greenlight / Extend / Pivot / Kill) by May 19, communicated to participants and exec sponsor. If the decision is Greenlight, kickoff with `launch-playbook/` happens within 7 days."

**How to catch it.** Look at the beta-end date and the exit-memo-publication date. Gap should be <= 5 business days.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Vanity recruit (friends only) | Is the Fanatics cohort >= 30% of total? |
| 2 | No exit criteria pre-recruitment | Are all gate thresholds locked before opening recruitment? |
| 3 | Beta-as-launch | Is target participant count > 50? |
| 4 | No Delight features in scope | Tag each feature Kano-class; is any classed Delight? |
| 5 | Silent cadence | Has the team posted in participant channel in last 5 business days? |
| 6 | Recruitment leads with features | Does the email's first paragraph name the product or the problem? |
| 7 | Exit-gate from < 20 participants | What is n? |
| 8 | Friends-feedback weighted equally | Are Fanatics-cohort metrics reported separately? |
| 9 | No explicit NDA | Show me the signed beta agreement. |
| 10 | Exit drags past window | Has the program run > 8 weeks without a decision? |
| 11 | One-off enterprise customizations | Has the team built anything for only one participant? |
| 12 | Decision deferred past 5-day SLA | Gap between beta-end and exit-memo publication? |

## Related Reading

- SKILL.md Troubleshooting
- references/beta-program-guide.md
- `daci-framework/` (for the exit-decision driver)
- `launch-playbook/` (for GA handoff)
- `customer-feedback-triage/` (for handling participant requests)

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/beta-program -->
