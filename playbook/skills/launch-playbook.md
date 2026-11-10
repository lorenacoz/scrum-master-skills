# launch-playbook

> **Use these instructions for this whole conversation.** Apply them when: Coordinate a launch from T-30 to T+30: owners, run-of-show, internal and external comms, rollback and retro. Use when a feature goes GA after beta, a major release ships, or a product is relaunched.

# Launch Playbook (Internal + External Coordination)

## Overview

A complete launch coordination playbook for software products and features. It covers the three windows that matter -- pre-launch (T-30 to T-1), launch day (T-0), and post-launch (T+1 to T+30) -- and produces five concrete artifacts: a run-of-show, an internal comms plan, an external comms checklist, a rollback plan, and a post-launch retro template.

Most failed launches are not failed builds; they are failed coordination. Engineering ships on time, but support has not been trained, sales does not have collateral, the changelog is wrong, the rollback path was never tested, and the executive sponsor hears about a customer complaint before hearing about the launch. This playbook prevents those failures by assigning every owner and every artifact before T-30.

## When to Use

- **GA after closed beta** -- A feature is exiting beta (see `beta-program/`) and needs coordinated launch.
- **Major version release** -- Significant new functionality with cross-functional dependencies (sales enablement, support training, legal review).
- **Re-launch / repositioning** -- An existing feature is being relaunched with new positioning, pricing, or audience.
- **High-blast-radius change** -- Infrastructure migration, pricing change, or breaking API change requiring tightly coordinated comms.

**When NOT to use:** continuous-delivery bug fixes and minor improvements (use `release-notes/` only); internal-only changes with no external comms (use a release runbook); product sunsets and deprecations (use `eol-communication/`).

## Clarify First

Before building the launch plan, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Launch date (T-0):** anchors the entire T-30→T+30 timeline and every artifact deadline.
- **Launch type:** big bang / progressive rollout / dark launch drives the run-of-show and the rollback plan.
- **Cross-functional owners (RACI):** every workstream named across PM/Eng/PMM/Sales/Support/Legal; a missing owner is the #1 cause of failed launches.
- **Exec sponsor:** holds go/no-go authority and receives the T-1/T+1/T+7/T+30 updates.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

The dates below are defaults for a GA launch with external comms [RECOMMENDED]. For a small or progressive launch, compress them (for example T-10 kickoff, sign-off at T-3, go/no-go at T-1) but keep the order: owners, then artifacts, then a tested rollback, then go/no-go.

1. **Kickoff at T-30.** Confirm date, launch type and exec sponsor; open the run-of-show and internal comms plan.
2. **Assign owners** within about 48 hours, every workstream named; unowned work is where launches fail.
3. **Build and sign off the five artifacts before T-7**, and drill the rollback by T-7 so there is time to fix what the drill finds.
4. **Go/no-go at T-3**, run launch day from one run-of-show, stabilise T+1 to T+7, run the 30-day retro.

**Done when** every artifact has a named owner and sign-off, the rollback was drilled, and the go/no-go decision is recorded with who made it.

Full timeline tables, RACI matrix, launch-type rules, and the 10-step workflow are in `references/launch-timeline-and-execution.md`.

## Anti-Patterns

### Launch message that doesn't match the rollout
**Mistake:** The launch post says "available to all customers today" while engineering ramps from 5% to 100% over a week. Most readers click through and hit "not available".
**Why it happens:** PMM and engineering each plan their own track, and nobody reads the two side by side.
**Instead:** At T-7, have PMM and the Eng Lead review the public messaging against the rollout plan together. Any mismatch in scope or timing gets fixed in the copy, for example "rolling out this week".

### Launching on the calendar after a failed beta gate
**Mistake:** The beta exit memo shows the outcome gate missed (38% vs a 50% target), and the team launches anyway because the date was promised.
**Why it happens:** The date is public or committed upward, and "ship and iterate" sounds reasonable.
**Instead:** Re-read the beta exit memo before the go/no-go decision. Any failed gate gets addressed before T-0 or the date moves. Re-baseline the date with the exec sponsor. The criteria are the gate, the calendar is not.

### Support not trained before launch
**Mistake:** Launch day brings a ticket spike, and agents answer "let me check on that" because the runbook is still a draft.
**Why it happens:** Support prep gets scheduled last, after the build and the external comms.
**Instead:** Finish the support runbook by T-14, run mandatory training at T-7, and pre-write macros for the top 10 expected questions. At T-3, ask 2 agents how to handle a likely ticket. If they hesitate, training is missing.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `assets/launch-run-of-show.md` | Hourly launch-day run-of-show |
| `assets/internal-comms-plan.md` | Internal comms before, during and after launch |
| `assets/external-comms-checklist.md` | Press, blog, email, enablement, support and legal checklist |
| `assets/rollback-plan.md` | Rollback decision matrix, drill checklist, runbook |
| `assets/post-launch-retro.md` | 7-day and 30-day retro |
| `examples/shared-dashboards-ga-launch.md` | Worked GA launch |

## References

- `references/launch-timeline-and-execution.md` — read this when planning/running the launch: three-launches framework, full T-30→T+30 timeline, launch-type selection, RACI matrix, 10-step workflow, troubleshooting, and success criteria.
- `references/launch-coordination-guide.md` — read this for the reasoning behind the playbook: three-launches sequencing, RACI worked examples, big-bang vs progressive decision rules, and anti-patterns.
- `references/red-flags.md` — read this before signing off any launch artifact: common failure modes with bad/good examples and fixes.
- Cagan, Marty. *Inspired: How to Create Tech Products Customers Love*. Wiley, 2018.

## Scope & Limitations

**In Scope:** GA launch coordination across Engineering, Product, PMM, Sales, Support, Legal; run-of-show, rollback plan, comms plans, post-launch retrospective; big bang, progressive rollout, and dark launch patterns; T-30 to T+30 timeline; RACI assignment for cross-functional launches.

**Out of Scope:** Beta program execution (`beta-program/`); release notes content generation (`release-notes/`); end-of-life / sunset communication (`eol-communication/`); incident response runbooks (`delivery-manager/` and engineering on-call); marketing campaign performance analysis beyond the 30-day window (handoff to demand gen).

**Important Caveats:** A launch is not a moment; it is a 60-day window (T-30 to T+30) -- staff accordingly. The single most common cause of failed launches is a missing RACI assignment, not a missing artifact: if you can name the artifact but not the owner, the artifact will not exist. Big-bang launches concentrate risk on one date; default to progressive rollout unless marketing leverage justifies the risk.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `beta-program/` | Receives from | Greenlit beta hands off testimonials, known issues, and pricing decision |
| `create-prd/` | Receives from | PRD provides positioning, segments, and v1 scope |
| `release-notes/` | Feeds into | Launch produces the GA release notes |
| `daci-framework/` | Uses | Major launch decisions (go/no-go, rollback) use DACI |
| `eol-communication/` | Complementary | Launches that replace older features trigger sunset comms |
| `delivery-manager/` | Uses | Deployment, on-call rota, and rollback execution |
| `senior-pm/` | Reports to | Exec sponsor receives T-1, T+1, T+7, T+30 updates |
| `summarize-meeting/` | Feeds into | War-room standups and retro produce structured summaries |
| `status-update-generator/` | Feeds into | Post-launch metrics roll up into weekly status |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/launch-coordination-guide.md

# Launch Coordination Reference Guide

A practical reference for coordinating cross-functional product launches. Expands the patterns in `SKILL.md` with worked examples, common failure modes, and the decision rules behind big-bang vs progressive vs dark launches.

---

## 1. The Three-Launches Model (Cagan)

Marty Cagan's framing splits a single GA launch into three sequenced events. Each tests a different risk; skipping one transfers that risk forward in time and amplifies it.

| Launch | Tests | Failure Mode if Skipped |
|--------|-------|-------------------------|
| **Alpha** | Does it run? Does it crash? | Embarrassing demos; production crashes |
| **Beta** | Does it produce the outcome? Will customers pay? | Launch with no testimonials; high churn at GA |
| **GA** | Can we scale? Does the market care? | Successful technical launch, commercial flop |

The output of each launch feeds the next:

- Alpha -> known-issues list and crash signatures
- Beta -> testimonials, pricing validation, refined positioning
- GA -> adoption curve, press, sales pipeline

This skill (`launch-playbook/`) is the GA event. Alpha is engineering's responsibility. Beta is `beta-program/`.

---

## 2. Launch Type Decision Tree

```
Is the change customer-money-affecting (billing, pricing, payments)?
  YES -> Progressive Rollout (mandatory)
  NO  -> continue

Is there marketing leverage in a single date (keynote, conference, partner co-marketing)?
  YES -> Big Bang (with dark-launch backend prep at T-14)
  NO  -> continue

Is the feature performance-sensitive at scale (search, ML inference, real-time)?
  YES -> Dark Launch + Progressive Rollout
  NO  -> continue

Are external dependencies tightly coupled (mobile app store releases, partner APIs)?
  YES -> Big Bang (forced by external timing)
  NO  -> Progressive Rollout (default)
```

### Big Bang

- One date, all users, full announcement.
- Concentrates risk; rewards rehearsal.
- Use when marketing leverage of the single date is material.

### Progressive Rollout (Ring Deployment)

- Ring 0: internal employees (alpha)
- Ring 1: beta cohort (see `beta-program/`)
- Ring 2: 5% of GA-eligible users
- Ring 3: 25% of GA-eligible users
- Ring 4: 100% of GA-eligible users

Each ring is held for a minimum dwell time (typically 24-72 hours) and gated on:

- Crash-free session rate >= 99.5%
- No new P0 bugs in the ring
- Customer support ticket volume within +20% of baseline

### Dark Launch

- Code is in production, real traffic exercises it, but no UI visible.
- Used for infrastructure validation: database migrations, cache warming, queue capacity, ML model latency.
- Most useful at T-14 through T-7 of a big-bang launch.

---

## 3. RACI Worked Examples

### Example A: Major Feature Launch (SaaS)

| Workstream | PM | Eng | PMM | Sales | Support | Legal | Exec |
|-----------|:--:|:---:|:---:|:-----:|:-------:|:-----:|:----:|
| Positioning brief | A | C | R | C | I | C | I |
| Pricing decision | R | I | C | C | I | C | A |
| Code deployment | I | A | I | I | I | I | I |
| Sales deck + battle cards | C | I | C | A | I | I | I |
| Support runbook | C | C | I | I | A | I | I |
| Press release | I | I | A | I | I | C | I |
| Customer email | C | I | A | I | I | C | I |
| Launch-day war room | A | C | C | I | C | I | I |
| Rollback authority | C | C | I | I | I | I | A |
| 30-day retro | A | C | C | C | C | I | I |

### Example B: Pricing Change

For pricing changes, Legal moves from C to A on customer-facing comms (regulatory exposure), Exec moves to A on the pricing decision itself, and CS becomes R on customer notification.

| Workstream | PM | Eng | PMM | Sales | CS | Support | Legal | Exec |
|-----------|:--:|:---:|:---:|:-----:|:--:|:-------:|:-----:|:----:|
| Pricing decision | C | I | C | C | C | I | C | A |
| Pricing page copy | C | I | R | C | I | I | A | I |
| Customer notification | C | I | C | C | R | I | A/C | I |
| Renewal communications | I | I | C | A | R | I | C | I |

### Anti-Pattern: "Everyone is Responsible"

If two or more people are listed as A (Accountable) for the same cell, nobody is. There is exactly one Accountable per cell.

---

## 4. The Launch-Readiness Checklist (T-3 Go/No-Go)

Every item must be Yes. Any No requires a documented mitigation or postponement.

### Engineering

- [ ] Code frozen for at least 72 hours
- [ ] Deployment runbook reviewed and signed
- [ ] Rollback drill completed in production with no-op feature
- [ ] On-call rota published for T-0 through T+3
- [ ] Monitoring dashboards updated; alerts validated
- [ ] Database migrations completed and verified (if applicable)
- [ ] Feature flag default state confirmed

### Product

- [ ] PRD final state archived
- [ ] Beta exit memo signed (if applicable)
- [ ] Known-issues list published internally
- [ ] Success metrics dashboard live and accessible

### PMM / Marketing

- [ ] Positioning brief signed off
- [ ] Press release approved by Legal
- [ ] Blog post staged and scheduled
- [ ] Social copy drafted across all channels
- [ ] Customer email campaign tested
- [ ] Press embargo policy documented
- [ ] Analyst pre-briefings completed (if applicable)

### Sales

- [ ] Sales deck delivered to reps at least T-7
- [ ] Battle cards distributed
- [ ] Pricing approved and loaded into CRM/CPQ
- [ ] Demo environment updated
- [ ] Field training session completed
- [ ] Top-account list reviewed for personalized outreach

### Support

- [ ] Runbook published internally
- [ ] FAQ live on help center
- [ ] Tier-1 team training completed
- [ ] Tier-2 escalation path defined
- [ ] Ticket macros updated
- [ ] Status page draft entry ready

### Legal & Compliance

- [ ] Public-facing copy reviewed
- [ ] ToS or DPA changes signed off (if applicable)
- [ ] Pricing page complies with relevant regulations
- [ ] Data residency / privacy claims verified

### Executive Comms

- [ ] Exec sponsor briefed at T-3
- [ ] Board/exec digest scheduled for T+1 and T+7
- [ ] Internal all-hands or company-wide email scheduled

---

## 5. Launch Day Operating Model

### Single Incident Commander

The Incident Commander is the named person empowered to make any operational call on launch day, including a rollback. Default: the PM owns the launch run-of-show; the Engineering Lead is IC for operational/technical decisions. Both are named explicitly in the run-of-show.

### Hourly Cadence

| Hour | Action |
|------|--------|
| T-1h | Final pre-launch standup; all teams confirm ready |
| T-0 | Flag flip / deploy / send launch comms |
| T+1h | First metrics check: traffic, errors, conversion |
| T+2h | Adoption snapshot; first customer reactions |
| T+4h | Second metrics check; press monitoring |
| T+6h | Support volume check; incident review (if any) |
| T+8h | End-of-day summary to exec sponsor |

### War Room

Single shared channel + video bridge. Open T-1h to end of day. Everyone with an A or R role attends.

### Communication Rules During Incident

1. The Incident Commander declares incident scope and severity.
2. PM owns external customer comms; PMM owns press response.
3. Engineering owns technical updates; goes through PM to customer-facing channels.
4. No public update is issued without IC approval.
5. Status page updated within 10 minutes of any user-visible degradation.

---

## 6. Rollback Decision Matrix

| Symptom | Severity | Action |
|---------|----------|--------|
| Error rate > 5x baseline for > 5 min | P0 | Immediate rollback |
| Crash-free session rate < 99% | P0 | Immediate rollback |
| Payment / billing failure | P0 | Immediate rollback |
| Data corruption observed | P0 | Immediate rollback + DB integrity check |
| Support volume > 3x baseline | P1 | Investigate; rollback if no clear root cause in 1 hour |
| One specific cohort failing | P1 | Disable for that cohort; continue rollout for others |
| Negative press coverage only | P2 | Continue; respond per PMM playbook |

Authority to rollback rests with the Incident Commander, with executive sponsor consultation if material business impact (revenue, contracts, public commitments).

---

## 7. Post-Launch Window: What to Measure

### Days 1-3: Stabilization

- Crash-free session rate
- Error rate vs baseline
- Support ticket volume vs baseline
- Top 5 support ticket themes

### Days 4-14: Adoption

- % of eligible users who used the feature at least once
- % who used it more than once (repeat use)
- Median time-to-first-use
- Top user paths through the feature

### Days 15-30: Outcome

- Headline outcome metric vs forecast
- Revenue impact (new MRR, expansion, retention)
- Sales pipeline created
- Press coverage tone and reach

The 30-day window produces one decision: invest more, sustain, iterate, or sunset.

---

## 8. Common Launch Failure Patterns

| Pattern | Symptom | Fix |
|---------|---------|-----|
| **"It worked in beta"** | Performance collapses at GA volume | Add dark-launch and progressive rollout to absorb scale risk |
| **Sales surprise** | Sales reps see the announcement on the same day as customers | Mandatory enablement at T-7 with attendance tracking |
| **Support drowning** | Tier-1 buried in tickets; escalations stack | Pre-launch volume forecast; surge staffing for first 72h |
| **Press misalignment** | Coverage contradicts internal messaging | Single positioning brief; PMM-only press contact |
| **Rollback paralysis** | Symptoms unclear; team debates instead of rolling back | Rollback decision matrix pre-signed by IC and Exec Sponsor |
| **Exec surprise** | Sponsor learns about a customer complaint from a customer | Internal comms plan with named touchpoints at T-1, T-0, T+1 |
| **No-one owns the retro** | Team disbands at T+1; 30-day decision never made | Calendar-block the retro at kickoff; named owner in RACI |
| **Comms-only launch** | Marketing fires on schedule, product never ships the feature flag | Single integrated checklist with engineering deploy as a gating item |

---

## 9. Internal Comms Touchpoints

| Time | Audience | Channel | Owner |
|------|----------|---------|-------|
| T-30 | Executive sponsor | 1:1 brief | PM |
| T-21 | Cross-functional leads | Kickoff doc + meeting | PM |
| T-14 | Sales leadership | Pre-enablement preview | PMM |
| T-7 | All sales reps | Enablement session | PMM + Sales Lead |
| T-7 | All support agents | Training session | Support Lead |
| T-3 | Exec sponsor | Go/no-go memo | PM |
| T-2 | Whole company | Pre-launch teaser email | PMM |
| T-0 | Whole company | Launch announcement | PMM + Exec Sponsor |
| T+1 | Exec sponsor | First-24h metrics | PM |
| T+7 | Exec sponsor | Week-1 retro summary | PM |
| T+30 | Exec sponsor + leadership | 30-day decision memo | PM |

---

## 10. References

- Cagan, Marty. *Inspired: How to Create Tech Products Customers Love*. Wiley, 2018.
- Cagan, Marty. *Empowered: Ordinary People, Extraordinary Products*. Wiley, 2020.
- Humble, Jez and Farley, David. *Continuous Delivery*. Addison-Wesley, 2010. (Dark launches, ring deployments.)
- Beyer, Betsy et al. *Site Reliability Engineering*. O'Reilly, 2016. (Incident command, rollback patterns.)

## references/launch-timeline-and-execution.md

# Launch Timeline & Execution

Read this when planning and running the launch: the three-launches framework, the full T-30 to T+30 timeline tables, launch-type selection, the RACI matrix, the 10-step workflow, troubleshooting, and success criteria.

---

## The Three Launches Framework

Marty Cagan's "three launches" model (popularized in *Inspired*, 2008/2018) sequences a launch into three windows that test different risks.

| Launch | Audience | Primary Risk Tested | Typical Duration |
|--------|----------|--------------------|-----------------|
| **Alpha** | Internal employees, dogfooding | Does it work at all? | 1-2 weeks |
| **Beta** | 10-30 closed external participants | Does it produce the outcome? Is it stable? | 4-8 weeks (see `beta-program/`) |
| **GA (Launch)** | All target users | Does the market care? Can we scale? | The launch event + 30-day stabilization |

This skill focuses on the GA launch. Alpha lives with engineering; Beta lives in `beta-program/`. By the time you open this playbook, both should be complete or in their final week.

## The Launch Timeline (T-30 to T+30)

### Pre-Launch (T-30 to T-1)

| Day | Workstream | Action |
|----:|-----------|--------|
| T-30 | All | Kickoff: confirm date, owner per workstream, exec sponsor |
| T-30 | PM + PMM | Positioning brief signed off |
| T-21 | Eng | Code freeze decision; rollout strategy (big bang vs progressive) confirmed |
| T-21 | Support | Runbook drafted; FAQ in progress |
| T-21 | Sales | Enablement deck drafted; pricing finalized |
| T-14 | Legal | Final review of public-facing copy, ToS changes, pricing pages |
| T-14 | Marketing | Press release, blog post, social copy, email campaign drafted |
| T-10 | Eng | Dark launch / feature flag toggled for internal verification |
| T-7 | All | Dry-run of the launch-day run-of-show; rollback drill |
| T-7 | Support | Team training completed; runbook published |
| T-7 | Sales | Reps trained; battle cards distributed |
| T-3 | All | Final go/no-go check against launch readiness checklist |
| T-2 | Marketing | Embargoed press outreach |
| T-1 | All | Final confirmation; on-call rota for launch day published |

### Launch Day (T-0)

Run from a single shared document (the run-of-show). Hourly cadence. Single incident commander. See `assets/launch-run-of-show.md`.

### Post-Launch (T+1 to T+30)

| Day | Workstream | Action |
|----:|-----------|--------|
| T+1 | PM + Eng | War-room standup: metrics, incidents, customer sentiment |
| T+1 | PMM | Launch-day metrics report to exec sponsor |
| T+3 | Support | First-3-days ticket triage; identify themes |
| T+7 | PM | Week-1 retrospective using `assets/post-launch-retro.md` |
| T+14 | PMM | Press coverage roundup; first-2-weeks adoption report |
| T+30 | All | 30-day retrospective; long-term metrics vs forecast |
| T+30 | PM | Decision: invest more / sustain / sunset / iterate |

## Launch Type Selection

### Big Bang

Single date, all users, full announcement. Use when:

- The product is stable, tested, and beta gates were met cleanly.
- Marketing leverage of a single date is critical (e.g., conference keynote).
- No technical risk that benefits from gradual exposure.

### Progressive Rollout

Stage exposure by feature flag, geography, account tier, or random percentage. Use when:

- Performance or scale risk that cannot be tested in beta volume.
- New billing flow, payment system, or anything that could lose customer money on failure.
- Migration that needs a clear rollback path per cohort.

### Dark Launch

Code is in production behind a flag, exercising real traffic and infrastructure, but not visible to users. Use when:

- You need to validate infrastructure under real load before any user-visible change.
- The feature has expensive backend dependencies (database migrations, indexing, queue capacity).

The three are not mutually exclusive: dark-launch the backend, then progressive-rollout the UI, then big-bang the announcement.

## RACI Matrix for Launches

| Workstream | PM | Eng | PMM | Sales | Support | Legal | Exec |
|-----------|:--:|:---:|:---:|:-----:|:-------:|:-----:|:----:|
| Positioning & messaging | A | C | R | C | I | C | I |
| Code freeze & deployment | I | R/A | I | I | I | I | I |
| Sales enablement | C | I | R | A | I | I | I |
| Support runbook & training | C | C | I | I | R/A | I | I |
| Legal & compliance review | C | I | C | I | I | R/A | I |
| External comms (PR, blog, social) | I | I | R/A | I | I | C | I |
| Internal comms (all-hands, FAQ) | R/A | I | C | I | C | I | I |
| Launch day run-of-show | R/A | C | C | I | C | I | I |
| Rollback decision | C | C | I | I | I | I | A |
| 30-day retrospective | R/A | C | C | C | C | I | I |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

## Workflow

1. **Kickoff at T-30.** Confirm launch date, type (big bang / progressive / dark), and exec sponsor. Open `assets/launch-run-of-show.md` and `assets/internal-comms-plan.md`.
2. **Assign the RACI.** Every cell above is named within 48 hours of kickoff.
3. **Lock the positioning.** PMM owns; PM + Eng + Legal review. Signed off by T-21.
4. **Build the comms artifacts.** Internal comms plan (T-14), external comms checklist (T-10), customer email and press release (T-7).
5. **Test the rollback.** Engineering runs a rollback drill in staging by T-7. The result is documented in `assets/rollback-plan.md`.
6. **Run the dry-run.** At T-7, walk through the launch-day run-of-show with all owners present. Identify any unowned action.
7. **Go/no-go at T-3.** Use the launch-readiness checklist in `assets/external-comms-checklist.md`. Any "No" requires a documented mitigation or a launch postponement.
8. **Run launch day.** Single incident commander; hourly cadence; war room (physical or virtual) open from T-0 to end-of-day.
9. **Stabilize T+1 to T+7.** Daily war-room standup; rapid hotfix lane open; sales and support triage themes.
10. **Run the 30-day retro.** Use `assets/post-launch-retro.md`. Decide: invest more, sustain, iterate, or sunset.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Launch date slips repeatedly | Beta gates were not actually met; team launching on the calendar instead of the criteria | Reopen the beta exit memo from `beta-program/`; re-baseline date based on actual gate status |
| Sales has no idea the feature exists on launch day | Enablement workstream not assigned an owner; PMM assumed Sales would self-serve from the blog post | Add a named Sales Enablement Lead in the RACI by T-21; mandatory training session in week T-1 |
| Support overwhelmed in first 48 hours | Runbook published too late, no T-7 training, no on-call rota | Make Support runbook + training a T-7 launch gate; require named on-call schedule in the run-of-show |
| Press coverage misrepresents the feature | Embargoed materials skipped or PMM and PM had different messaging | Single shared positioning brief signed off by T-21; PMM-led press briefings only; one PR contact for all journalists |
| Rollback "tested" but fails in production | Drill was performed in staging with synthetic data; production differences not exercised | Run a production rollback drill (with a no-op feature) at T-14; document the result in `assets/rollback-plan.md` |
| Exec sponsor hears about a customer issue before hearing about the launch | No internal comms plan; #launches Slack channel never existed | Internal comms plan with exec briefing at T-1 and T+1; dedicated launch channel from T-30 |
| Post-launch metrics never reviewed | Team disbanded at T+1; nobody owns 30-day decision | Calendar-block the 30-day retro at kickoff; assign accountable PM in the RACI |

## Success Criteria

- All five launch artifacts (run-of-show, internal comms plan, external comms checklist, rollback plan, retro) are populated and signed off before T-7.
- Launch RACI has every cell assigned to a named individual by T-21.
- Rollback drill was successfully performed and documented by T-7.
- Go/no-go at T-3 has explicit approval from PM, Engineering, PMM, Support, Legal, and Exec Sponsor.
- Launch day runs from a single shared run-of-show with hourly cadence and single incident commander.
- Post-launch retrospective produces a 30-day decision (invest more / sustain / iterate / sunset) documented and shared with the exec sponsor.
- Zero unplanned customer-visible incidents in the first 24 hours, or any incidents have a documented timeline from detection to resolution.

## references/red-flags.md

# Red Flags: Launch Playbook

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the run-of-show, RACI, comms plans, and rollback plan before T-7. Each red flag shows the *bad* version next to the *good* version, anchored to Marty Cagan's three-launches model (alpha/beta/GA) and the launch RACI.

---

## Red Flag 1: No rollback rehearsal

**Symptom.** Rollback plan is documented. Nobody has actually executed a rollback in staging. Launch day discovers the runbook has stale commands.

**Why it's bad.** A documented-but-untested rollback is a fiction. Production rollback drills surface stale credentials, missing access, runbook gaps, and decision-authority confusion — all of which become amplified in a real incident.

**Bad example:**
> "Rollback plan: 8-page doc, last updated 6 weeks ago. Drill: 'we'll do that in the future when we have time.' Launch day: rollback attempted; command in runbook fails because the service was renamed."

**Good example:**
> "Rollback rehearsal at T-14 and T-7:
> • Run in staging first; then in production with a no-op feature flag.
> • Time it; document the actual elapsed time.
> • Confirm: kill-switch flips < 60 sec; full rollback < 10 min.
> • Test each runbook step; every command works.
> • Test escalation paths; on-call rota current.
> Result documented in `assets/rollback-plan.md` with timestamps and the names of the people who ran it."

**How to catch it.** Ask: "show me the timestamps from the last rollback drill." If no answer, the drill didn't happen.

---

## Red Flag 2: Comms not aligned with engineering

**Symptom.** PMM publishes a launch post saying "shipping today, 100% available globally". Engineering's actual ramp is 5% → 25% → 100% over a week. Customers in Europe try the feature, hit "not available in your region", post on Twitter.

**Why it's bad.** Marketing message and engineering reality must match. When they don't, customers' expectations are set wrong, support is overwhelmed, and the launch narrative is hijacked by "broken promise" stories.

**Bad example:**
> "PMM blog: 'Available to all customers today.' Engineering rollout: 5% canary all week; 100% on Friday. Day 1: 95% of customers see a 'not available' message after clicking the blog post."

**Good example:**
> "T-7 alignment check: PMM and Eng Lead jointly review the rollout plan and the public messaging. Public message updated to match: 'Rolling out this week — most customers will see it by Friday. If you don't see it yet, click here to request access.' Engineering's ramp schedule documented in the in-app message users see. PMM, Eng, and Support agree on the language."

**How to catch it.** At T-7, read the PMM materials and the engineering rollout plan side by side. Any mismatch in scope or timing = misalignment.

---

## Red Flag 3: RACI cells unowned

**Symptom.** Launch RACI is published. Several cells are blank. Assumption: "someone will figure it out".

**Why it's bad.** Unowned launch workstreams *will not happen*. The single most common cause of failed launches is a missing RACI assignment, not a missing artifact. If you can name the artifact but not the owner, the artifact will not exist.

**Bad example:**
> "Launch RACI: 10 workstreams x 7 roles = 70 cells. 12 cells blank. Sales enablement row: A and R both blank. (Launch day: sales has no battle card; reps freelance their pitch; messaging fragments across the team.)"

**Good example:**
> "Launch RACI at T-21: every cell assigned to a named individual (not 'the team' or 'TBD'). Sales enablement row: R Jorge M (PMM); A Sarah K (Sales Director); C David T (PM), Eng Lead; I All sales reps. Battle card committed by T-14; mandatory training session T-7."

**How to catch it.** Read the RACI. Every R and A cell should have a person's name. Any "TBD", "the team", or blank = unowned.

---

## Red Flag 4: Beta gates not actually met

**Symptom.** Launch date is fixed for August 31 (committed to investors). Beta exit memo says outcome gate failed (38% achieved headline outcome vs 50% target). Team launches anyway.

**Why it's bad.** Beta gates exist precisely to prevent calendar-driven launches of products that aren't ready. Launching on the calendar instead of on the criteria means GA will be the first time customers experience the gaps. Trust erodes; support is overwhelmed; competitors notice.

**Bad example:**
> "Beta exit memo: 38% outcome (vs 50% target). PM: 'we have a hard launch date; we'll ship and iterate.'"

**Good example:**
> "Beta exit memo: 38% outcome (vs 50% target). DACI Driver convenes the gate review: launch postponed 4 weeks. Internal comms: 'we discovered a friction point in beta; pushing GA to Sep 28 so we ship the right thing.' Re-baseline the launch date with the exec sponsor; the calendar is not the gate, the criteria are."

**How to catch it.** Re-read the beta exit memo before launch decision. Any failed gate = address before T-0, not after.

---

## Red Flag 5: Support not trained before launch

**Symptom.** Launch day. Support inbox: 400 tickets in 4 hours. Agents respond "let me check on that" because the runbook is still draft.

**Why it's bad.** Support is the customer's only human touchpoint when something goes wrong. Untrained support means the customer's first experience of "something wrong" is also "the company can't help me" — a double failure.

**Bad example:**
> "Support runbook drafted at T-3. Training session: never scheduled. Launch day: agents see new feature tickets for first time. Macro responses absent. Escalation queue overflows."

**Good example:**
> "Support runbook completed at T-14; training T-7 (mandatory for all customer-facing agents). Top-10 anticipated questions: macro responses pre-written. Escalation rota: T-1 confirmation. Launch day: ticket volume spike of 3.2x baseline absorbed within SLA; macro responses cover 78% of tickets; escalations are real issues, not training gaps."

**How to catch it.** At T-3: ask 2 support agents "what's launching this week and how do I handle ticket X?" If they hesitate, training is missing.

---

## Red Flag 6: Sales has no idea the feature exists

**Symptom.** Launch day. Sales rep on a customer call: "We're launching what? Today?"

**Why it's bad.** Sales enablement is a workstream that requires deliberate effort, not osmosis. Without battle cards, training, and a defined SDR/AE handoff, sales freelances responses. Some reps oversell; others undersell; messaging fragments.

**Bad example:**
> "PMM published the launch blog on Wednesday at 9am. Sales-team Slack channel: '#products' was supposed to receive the heads-up. The heads-up never went. Reps learn from the customer."

**Good example:**
> "Sales enablement workstream owned by PMM:
> • T-21: battle card drafted (PMM + PM jointly).
> • T-14: battle card reviewed with VP Sales.
> • T-7: mandatory enablement session (all AEs, SDRs, CSMs). Recording in Highspot.
> • T-3: quiz to confirm rep readiness (90% pass before launch).
> • T-1: final talking points and FAQ in CRM playbook.
> Launch day: every rep can name the feature, target customer, and 3 differentiators."

**How to catch it.** At T-3: ask 3 random reps "what are we launching this week and to whom?" If 2 can't answer, sales enablement failed.

---

## Red Flag 7: Single incident commander missing

**Symptom.** Launch day. An issue surfaces. PMM tries one mitigation; Eng tries another; both miss each other's actions in the war-room thread.

**Why it's bad.** Multi-headed incident response produces conflicting actions, missed signals, and slower recovery. Cagan's framing and standard incident-management practice: one named incident commander with authority to make and reverse decisions.

**Bad example:**
> "War-room Slack: 12 active people; PMM posting 'I'm reaching out to TechCrunch'; Eng Manager posting 'I'm pausing the rollout'; PM trying to triage; nobody has the floor."

**Good example:**
> "Launch-day run-of-show: single incident commander named for the day (Eng Manager Tomas R). Authority: make any go/no-go decision for the next 4 hours without escalation. War room: he runs hourly check-in (top of every hour); everyone reports to him; he posts the consolidated update. Other roles post into a side thread, not into the main."

**How to catch it.** Read the run-of-show. Does it name a single incident commander with explicit authority? If not, the chain is unclear.

---

## Red Flag 8: Exec sponsor surprised by customer issue

**Symptom.** A customer escalates an issue on Twitter at 11am. VP Product first hears about it from a different customer on the 2pm board call.

**Why it's bad.** Exec sponsors are the company's senior face for the launch. Being surprised by a customer issue in a high-stakes meeting destroys credibility and gives the sponsor no time to prepare a response. Worse, it signals to the sponsor that the team doesn't have control.

**Bad example:**
> "Internal comms plan: 'we'll update the exec channel as needed'. (Reality: T+1 customer Twitter post; T+3 VP hears about it; T+4 VP messages PM 'why am I learning this from a customer?')"

**Good example:**
> "Exec briefing cadence:
> • T-1 17:00: pre-launch briefing memo to exec sponsor (current readiness, expected risks).
> • T+0 12:00: launch-day status (metrics + any issues).
> • T+0 17:00: end-of-day summary.
> • T+1 09:00: 24h retro.
> • Any P0/P1 incident: exec sponsor pinged within 15 min of declaration.
> No exec hears about a customer issue from outside the team before hearing about it from the team."

**How to catch it.** Look at the exec comms plan. Are scheduled briefings on the calendar? If no, surprise is likely.

---

## Red Flag 9: 30-day retro never happens

**Symptom.** Launch was September 1. It is now October 15. No retrospective scheduled. Team has moved to the next initiative.

**Why it's bad.** Without a 30-day retro, the team cannot learn what worked and what didn't. The next launch repeats the same mistakes. The 30-day window also captures the lagging metrics (cohort retention, customer-feedback themes) that day-1 metrics miss.

**Bad example:**
> "Launch: Sep 1. PM on next project Oct 5. No retro held. Director: 'we'll discuss at the next QBR.'"

**Good example:**
> "Calendar-blocked at kickoff:
> • T+7 retrospective: week-1 metrics, top issues, hotfix list.
> • T+30 retrospective: 30-day metrics vs forecast, cohort retention, customer-feedback themes, decision: invest-more / sustain / iterate / sunset.
> Owner: PM. Attendees: full launch team + exec sponsor. Output: 1-page memo to all-hands + actions for next launch."

**How to catch it.** Check the calendar at launch+30 days. Is the retro on the calendar? If not, it won't happen.

---

## Red Flag 10: Big bang when progressive would be safer

**Symptom.** First-of-its-kind feature; high blast radius (touches billing); team chooses big-bang launch because "marketing wants a moment".

**Why it's bad.** Big bang concentrates risk on one date. For high-blast features, progressive rollout reduces customer impact at the cost of marketing optics. Choosing big-bang because of optics is choosing optics over customers.

**Bad example:**
> "Launch plan: 'Big bang on Aug 31 to coincide with the conference keynote.' Touches billing. No prior testing at scale. Day 1: 12% transaction failure rate; revenue loss in 4 hours exceeds the conference's marketing budget."

**Good example:**
> "Launch plan: progressive rollout for the billing change (5% / 25% / 50% / 100% over 14 days). Conference keynote announces the launch with 'now rolling out — most customers will see it by mid-September'. Marketing optics preserved; risk distributed; the team can pause at any stage."

**How to catch it.** For each launch, ask: "what is the smallest blast radius we could start with?" If the answer is "all users on day 1" for a non-trivial feature, big-bang is over-confident.

---

## Red Flag 11: Press materials misrepresent the feature

**Symptom.** Press release says "AI-powered fully autonomous workflow assistant". Reality: scripted workflows with one AI-summary feature. Press writes stories matching the headline; customers expect autonomous AI; product underdelivers.

**Why it's bad.** Press exaggeration produces customer disappointment and erodes brand trust. The team handed the press the wrong headline; the press wrote what they were given. Recovery is hard because the framing is now public.

**Bad example:**
> "Press release headline: 'CompanyX launches fully autonomous AI workflow agent'. Reality: rule-based workflows with optional AI summarization."

**Good example:**
> "Single source of truth for messaging: PMM-owned positioning brief signed by PM, Eng Lead, Legal at T-21. Press release written from the brief. Press briefings only led by PMM; reps cite the brief verbatim. Anti-claims documented: 'we do not claim autonomous; we claim AI-assisted scripted workflows'. Legal reviews any 'AI' claim against substantiation."

**How to catch it.** Compare the press release to the PRD's customer-benefit statements. Any escalation in claims = misalignment.

---

## Red Flag 12: T-3 go/no-go check skipped

**Symptom.** T-3. Team is busy. The launch-readiness review never happens. Launch happens with several unaddressed risks.

**Why it's bad.** The T-3 check is the last formal gate. Skipping it means risks identified earlier (ambiguous owner, unresolved bug, missing translation) ride into launch unaddressed. The cost is paid by customers and by the team on launch day.

**Bad example:**
> "T-3: PM intended to run the readiness review; busy with stakeholder fires; skipped. T-0: rolling launch; 3 of the 8 risks flagged in week-2 review are unresolved; surprises ensue."

**Good example:**
> "T-3 go/no-go review (60 min, blocked on calendar at kickoff):
> Attendees: PM, Eng Lead, PMM, Sales Lead, Support Lead, Legal, Exec Sponsor.
> Agenda: walk the readiness checklist; each row is Green / Yellow / Red. Any Red blocks launch until resolution; any Yellow has a documented mitigation. Decision: Go / No-Go (or Postpone). Documented in `assets/external-comms-checklist.md`.
> Sample T-3 decisions: Green 18/20, Yellow 2 (mitigations documented), Red 0 → Go. If any Red, postpone to T+5; restart at T-3 from the new date."

**How to catch it.** Is the T-3 review on the calendar with the right attendees? If not, the gate is missing.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | No rollback rehearsal | Show me timestamps from the last drill |
| 2 | Comms not aligned with engineering | Side-by-side PMM message vs engineering ramp |
| 3 | RACI cells unowned | Every R/A cell has a person's name? |
| 4 | Beta gates not actually met | Re-read beta exit memo before launch decision |
| 5 | Support not trained before launch | Can support agents name top-10 questions at T-3? |
| 6 | Sales has no idea | Ask 3 reps at T-3 to name what's launching |
| 7 | Single incident commander missing | Run-of-show: does it name one person with authority? |
| 8 | Exec sponsor surprised | Are scheduled briefings on the calendar? |
| 9 | 30-day retro never happens | Is the retro on the calendar at T+30? |
| 10 | Big bang when progressive is safer | What is the smallest blast radius option? |
| 11 | Press materials misrepresent | Compare release to PRD's customer-benefit claims |
| 12 | T-3 go/no-go skipped | Is the T-3 review on the calendar with right attendees? |

## Related Reading

- SKILL.md Troubleshooting
- references/launch-coordination-guide.md
- `beta-program/` (beta exit feeds launch readiness)
- `feature-flag-strategy/` (progressive rollout mechanics)
- `prfaq/` (positioning brief is the single source of truth)
- `daci-framework/` (go/no-go decision authority)
- `post-mortem/` (if the launch becomes an incident)
- Marty Cagan, *Inspired* (2018) — three launches model

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/launch-playbook
