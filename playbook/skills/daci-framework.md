# daci-framework

> **Use these instructions for this whole conversation.** Apply them when: Assign Driver, Approver, Contributor and Informed roles for the decisions that keep stalling, then roll the chart out. Use when decisions thrash, ownership is unclear after a reorg, or a new team needs decision rights.

# DACI Decision Framework

## Overview

Clarify decision ownership and reduce decision thrash using the DACI framework (Driver, Approver, Contributor, Informed). Unlike RACI which focuses on task responsibility, DACI is purpose-built for product decisions -- who drives the decision to closure, who has veto power, who provides input, and who needs to know.

The four roles in brief: **Driver** (exactly one, drives to closure), **Approver** (1-2 max, holds veto), **Contributor** (input without veto), **Informed** (notified, not consulted). Build a chart by mapping current state, finding pain points, designing target state, and rolling out a 30/60/90 transition. See the playbook reference for role rules, the 7-step build sequence, and health metrics.

## When to Use

- **New team formation** -- A new cross-functional group needs clear decision-making roles.
- **Decision thrash** -- Decisions stall because nobody knows who has authority.
- **Scaling teams** -- Growth creates ambiguity about who owns which decisions.
- **Post-incident** -- A failed launch or missed deadline reveals unclear ownership.
- **Reorg transitions** -- Role changes create governance gaps.

### When NOT to Use

- Task assignment or project execution (use RACI instead).
- Individual contributor work allocation (use sprint planning).
- Truly one-person decisions (no governance overhead needed).

## Clarify First

Before building the DACI chart, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **The specific decisions to map:** the 3-5 high-impact decisions, not "everything" (each becomes a chart row; mapping too much at once is the top failure mode).
- **Candidate people and their real authority:** who can actually approve or veto (drives the Driver and Approver assignments; without genuine authority the chart is fiction).
- **Current pain points:** where decisions stall or thrash today (drives the current→target-state gap and the 30/60/90 transition plan).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Pick 3-5 decisions** that stall or recur, not every decision the team makes.
2. **Map the current state** per decision: who actually decides today, who blocks late, where it stalls.
3. **Assign roles** [RECOMMENDED] per decision: exactly one Driver (one person drives to closure), one or two Approvers who hold real authority, at most 3-4 Contributors with expertise to add, everyone else Informed. Anyone who can stop the decision is a Contributor or Approver, never Informed.
4. **Agree the chart** with the Approvers named in it; a chart they have not accepted is fiction.
5. **Roll out** with a 30/60/90 plan and record each decision (option chosen, Approver, rationale, vetoes with reasons).

**Verify** before publishing: every row has one D and one or two A; no row has more than 5 C; every A has the authority in practice; the last few vetoes have written reasons. Build steps, health metrics and troubleshooting: `references/playbook.md`.

## Anti-Patterns

### Informed roles that object late
**Mistake:** Marketing is marked Informed on the launch date, objects three days before launch, and the date slips two weeks.
**Why it happens:** Teams mark a role Informed to keep meetings small, without asking whether that role can block the decision.
**Instead:** Make anyone who can stop the decision a Contributor or Approver from the start. Once the decision locks, a late objection goes to the Approver as an escalation.

### Everyone marked Contributor
**Mistake:** Most cells in the chart are C, so everyone expects to be consulted on everything.
**Why it happens:** Assigning C avoids hard conversations about who is left out.
**Instead:** Per decision, assign one D, one or two A, and at most 3-4 C. Give C only to roles with real expertise to add, and mark the rest I or leave them blank. More than 5 C cells on a row is a flag.

### Vetoes with no written reason
**Mistake:** The Driver proposes option A and the Approver says "No" with no follow-up. Two months later the same debate returns.
**Why it happens:** A veto feels like the end of the matter, so writing it up seems optional.
**Instead:** Ask Approvers to give every veto a written rationale and say what a counter-proposal would need to address. Keep these as decision records, and check the last 5 vetoes for them.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

- **[references/playbook.md](references/playbook.md)** — read this when building or running a DACI chart: role definitions and rules, the 7-step build sequence (working group → roles → decisions → current-state map → pain points → target-state → transition plan), governance health metrics, troubleshooting, and success criteria.
- **[references/red-flags.md](references/red-flags.md)** — read this before publishing a chart or running a decision under it: common ways a DACI chart goes wrong with bad/good examples anchored to the role rules.

## Files

| File | Purpose |
|---|---|
| `references/playbook.md` | Role rules, 7-step build, health metrics |
| `references/red-flags.md` | Bad/good charts with fixes |
| `examples/choosing-payment-processor.md` | Worked DACI for one decision |

## Scope & Limitations

**In Scope:** DACI chart creation, current-state mapping, target-state design, transition planning, governance health metrics, pain point identification, decision ownership clarity.

**Out of Scope:** Task assignment (use RACI), project execution tracking (use sprint planning), individual performance management, organizational design beyond decision governance.

**Important Caveats:** DACI works best when leadership commits to respecting the framework. Without executive buy-in, Drivers may lack the authority to actually drive decisions. Start with 3-5 high-impact decisions rather than trying to map everything at once.

## Integration Points

| Integration | Direction | What Flows |
|---|---|---|
| `create-prd/` | Feeds into | DACI decisions inform PRD Contacts section and decision log |
| `discovery/identify-assumptions/` | Complements | Surfaces assumptions about who has authority |
| `brainstorm-okrs/` | Complements | OKR ownership aligns with DACI decision ownership |
| `summarize-meeting/` | Feeds into | Meeting summaries capture DACI decision outcomes |
| `senior-pm/` | Complements | Portfolio-level DACI for cross-project decisions |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/playbook.md

# DACI Framework Playbook

> Read this when building or running a DACI chart: role definitions and rules, the 7-step build sequence (working group → roles → decisions → current-state → pain points → target-state → transition plan), governance health metrics, troubleshooting, and success criteria.

## DACI Role Definitions

| Role | Symbol | Definition | Rules |
|---|---|---|---|
| **Driver** | D | The person driving the decision to closure. Responsible for process, timeline, and ensuring a decision gets made. | Exactly one per decision. |
| **Approver** | A | The person(s) with authority to approve or veto. Their sign-off is required. | 1-2 maximum per decision. |
| **Contributor** | C | People who provide input, expertise, or implementation effort. Their input shapes the decision but they don't have veto power. | As many as needed. |
| **Informed** | I | People who are notified of the decision outcome. Not part of the decision-making process. | As many as needed. |

### Key DACI Principles

1. **Every decision has exactly one Driver.** If two people are driving, nobody is driving.
2. **Approvers have veto power.** Limit to 1-2 to avoid gridlock.
3. **Contributors influence but don't block.** Their input is valued but the Driver decides how to use it.
4. **Informed means notified, not consulted.** Don't confuse notification with input.
5. **DACI is about decisions, not tasks.** Map decisions, not work items.

## Building a DACI Chart

### Step 1: Identify the Working Group

Define the team, business unit, or cross-functional group this DACI covers.

### Step 2: List Job Titles / Roles

Enumerate all roles involved in product decisions. Common roles:

- Executive Management
- Product Manager
- Product Owner
- Engineering Lead
- UX / Design Lead
- Product Marketing
- Scrum Master
- Sales & Marketing
- Customer Support / Professional Services
- Legal / Compliance

### Step 3: Define Decisions

List the key decisions this group makes. Common product decisions:

| Decision | Description |
|---|---|
| What problem are we solving? | Problem definition and validation |
| Who is the primary user? | Persona and segment selection |
| What is the product vision? | Long-term direction and strategy |
| What is the value proposition? | Differentiation and positioning |
| What are the JTBD? | Jobs-to-be-done identification |
| What goes into the backlog? | Story selection and prioritization |
| What is the release plan? | Timing, scope, and sequencing |
| What experiments to run? | Discovery and validation activities |
| How is the product built? | Architecture and technical decisions |
| How is the product delivered? | Deployment and rollout strategy |
| What data do we collect? | Analytics and instrumentation |
| How do we price the product? | Pricing model and strategy |
| What is the GTM strategy? | Go-to-market planning |

### Step 4: Build Current-State DACI

Map how decisions are made **today** (not how you want them to be made):

| Decision | Exec Mgmt | PM | PO | Eng Lead | Design | Marketing | Support | Legal |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Problem definition | A | D | C | C | C | I | C | |
| User/segment selection | I | D | C | | C | A | C | |
| Product vision | A | D | C | C | C | I | | |
| Value proposition | I | D | | | C | A | | |
| Backlog priorities | I | A | D | C | C | | | |
| Release plan | I | A | D | C | | I | I | |
| Experiments | | D | C | C | C | | | |
| Architecture | I | C | | D | | | | A |
| Pricing | A | C | | | | D | | C |
| GTM strategy | A | C | | | | D | C | I |

**Rules:**
- Each row has exactly one `D`.
- Each row has 1-2 `A` maximum.
- Use `D`, `A`, `C`, `I`, or blank only.
- Add Notes column for non-obvious assignments.

### Step 5: Identify Pain Points

From the current-state chart, identify common failure patterns:

| Failure Pattern | Symptom | Business Impact |
|---|---|---|
| **No Driver** | Decision stalls for weeks | Missed market windows |
| **Too many Approvers** | Endless review cycles | Slow time-to-market |
| **Driver lacks authority** | Decision made but not respected | Rework and confusion |
| **Informed treated as Approver** | Late objections derail decisions | Scope creep and delays |
| **Missing Contributors** | Decisions made without key input | Poor outcomes, rework |

### Step 6: Design Target-State DACI

Based on pain points, redesign decision ownership:

- Ensure every row has exactly one D.
- Reduce Approvers to 1-2 per decision.
- Move chronic blockers from A to C or I.
- Add missing Contributors.
- Document changes in Notes column.

### Step 7: Create Transition Plan

| Timeframe | Action |
|---|---|
| **First 30 days** | Align on first 3 high-impact decision changes; communicate new roles |
| **60 days** | Expand to all decisions; run first decision under new DACI |
| **90 days** | Full adoption; retrospective on decision speed and quality |

## DACI Health Metrics

Track these metrics to monitor governance effectiveness:

| Metric | Target | How to Measure |
|---|---|---|
| Decision cycle time | <5 business days for P0 decisions | Time from decision identified to resolved |
| Decision reversal rate | <10% | Decisions overturned within 30 days |
| Stakeholder satisfaction | >80% | Survey: "Do you know who makes decision X?" |
| Escalation rate | <15% | Decisions escalated past intended Approver |
| Decision coverage | 100% | All recurring decisions have a DACI row |

## Integration with Other Skills

- Use `create-prd/` to document decisions made via DACI in PRD Section 2 (Contacts).
- Use `identify-assumptions/` to surface assumptions about decision authority.
- Use `brainstorm-okrs/` to align DACI decisions with quarterly objectives.
- Use `summarize-meeting/` to capture decision outcomes in meeting notes.

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---|---|---|
| Decisions still stall after DACI rollout | Driver lacks confidence or authority in practice | Coach Drivers on decision-making process; ensure Approvers respect the framework |
| Everyone is marked as Contributor | Team avoids accountability by defaulting to C | Force each person to commit to D, A, C, or I -- no "everyone contributes" |
| DACI chart exists but nobody references it | Document not integrated into workflows | Post DACI in team Confluence/Notion; reference it in kickoff meetings |
| Approvers overrule without explanation | Authority without accountability | Require Approvers to document veto rationale; review in retrospectives |
| New decisions not added to chart | DACI treated as one-time exercise | Review and update DACI quarterly; add new decisions as they emerge |

## Success Criteria

- 100% of recurring product decisions have a DACI row with exactly one Driver
- Decision cycle time reduced by 30%+ after DACI implementation
- <10% of decisions reversed within 30 days of being made
- >80% of team members can identify the Driver for any given decision
- DACI chart reviewed and updated at least quarterly

## references/red-flags.md

# Red Flags: DACI Framework

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the DACI chart before publishing or running a decision under it. Each red flag shows the *bad* version next to the *good* version, anchored to the Driver / Approver / Contributor / Informed role rules.

---

## Red Flag 1: Too many Approvers (gridlock by design)

**Symptom.** A decision row lists 4 Approvers. Decision sits for 6 weeks waiting for sign-off.

**Why it's bad.** Approvers have veto power. Each additional Approver multiplies the chance of stall. The DACI rule is 1-2 Approvers max — beyond that, the decision becomes consensus-by-veto, which is the opposite of clarity.

**Bad example:**
> "Decision: Backlog priorities. Approvers: VP Product, VP Eng, VP Marketing, CFO. (Decision pending since Q1; quarter ending; no movement.)"

**Good example:**
> "Decision: Backlog priorities. Driver: PM (Sarah K). Approver: VP Product (David T) — sole approval. Contributors: VP Eng (capacity input), VP Marketing (GTM input), CFO (budget input). Informed: exec team. Decision SLA: 5 business days from Driver proposal."

**How to catch it.** Count `A` cells per row. > 2 = the row is built to stall.

---

## Red Flag 2: Driver-by-committee

**Symptom.** A row shows D in two cells: PM and PMM both "drive" the launch decision.

**Why it's bad.** "Every decision has exactly one Driver" is the central DACI principle. Two Drivers means nobody is driving — each waits for the other; both blame the other when nothing moves. The decision becomes unowned.

**Bad example:**
> "Decision: GTM strategy. PM: D. PMM: D. Approver: VP Product. (Decision unresolved 8 weeks; PM thinks PMM is leading; PMM thinks PM is leading.)"

**Good example:**
> "Decision: GTM strategy. Driver: PMM (Jorge M) — accountable for process + timeline. Contributor: PM (Sarah K) — provides product context and launch dependency. Approver: VP Product. Single named owner; PMM runs the meeting and writes the memo."

**How to catch it.** Count `D` cells per row. > 1 = no Driver.

---

## Red Flag 3: Driver lacks authority

**Symptom.** Driver is a Junior PM. Approver is the CEO. Driver runs the meeting; CEO ignores Driver's framing and decides unilaterally.

**Why it's bad.** Authority follows the role's title. A Driver junior to the decision's stakes will be steamrolled. The DACI chart looks valid on paper; in practice, decisions skip the Driver entirely. Other teams learn the chart is decoration.

**Bad example:**
> "Decision: Architecture. Driver: Sr Eng (3y tenure). Approver: CTO. (Meeting reality: CTO walks in, restates the question, picks an answer; Driver thanks the team and goes home.)"

**Good example:**
> "Decision: Architecture. Driver: Eng Manager (peer of CTO's direct reports). Approver: CTO. Driver has the standing to push back on the Approver in the room. If the role's natural Driver is too junior for the stakes, escalate the Driver role (not the decision)."

**How to catch it.** Ask the Driver: "could you tell the Approver 'no, here is why' and have it land?" If not, the Driver lacks authority.

---

## Red Flag 4: Informed treated as Approver

**Symptom.** Marketing was marked I (Informed) on the launch-date decision. Three days before launch, Marketing objects and the date slips.

**Why it's bad.** Late objections destroy DACI. Informed means notified, not consulted. If Marketing has objection rights, they should have been Contributor or Approver from the start. The chart promised one thing; behavior delivered another.

**Bad example:**
> "Launch decision: Driver PM, Approver VP Product, Marketing as I. (T-3: 'wait, Marketing can't support this date'. Slip 2 weeks.)"

**Good example:**
> "Launch decision: Driver PM, Approver VP Product, Contributor PMM (input on GTM readiness), Contributor Marketing (input on demand-gen capacity), Informed: rest of team. PMM and Marketing get to weigh in at T-30 and T-21; their concerns shape the date. After date-lock at T-21, they cannot reopen at T-3 without escalating to the Approver."

**How to catch it.** When a role objects late, ask: "what was their DACI role?" Marketing-as-I objecting at T-3 is a chart violation.

---

## Red Flag 5: Everyone is a Contributor

**Symptom.** Most cells in the chart are C. Team uses "everyone contributes" as a default to avoid hard accountability conversations.

**Why it's bad.** Defaulting to C is a polite refusal to assign accountability. The chart loses information; nothing is signal because everything is signal. Decisions slow because everyone expects to be consulted.

**Bad example:**
> "DACI chart: 10 decisions × 8 roles. 70% of cells are C. (Everyone feels included; no one feels accountable.)"

**Good example:**
> "DACI chart: 10 decisions × 8 roles. Per decision: 1 D, 1 A, 3-4 C maximum, rest I (or blank). C is reserved for roles with substantive expertise to add. If a role has nothing to contribute, leave the cell blank or mark I — do not default to C to 'be polite'."

**How to catch it.** Count C cells per row. > 5 C's = the row is consensus theater.

---

## Red Flag 6: DACI built but never referenced

**Symptom.** Chart published in Confluence. Six months later, no team meeting has referenced it. New joiners do not know it exists.

**Why it's bad.** A DACI chart that nobody references provides no clarity. Decision velocity is whatever it was before; the document is a fossil. The exercise of building it produced alignment in the room; the artifact produces nothing afterward.

**Bad example:**
> "DACI built March 1; last referenced March 5 (in the meeting that built it). Decision X stalled in May with three people debating ownership; nobody opened the chart."

**Good example:**
> "DACI is referenced at: (1) every kickoff meeting for new initiatives ('per the DACI, the Driver here is …'); (2) onboarding for new joiners (1-hour walkthrough); (3) escalations ('we are in conflict; per the chart, the Approver is …'). Chart link pinned in the team channel. Quarterly review and refresh."

**How to catch it.** Open the chart. When was it last referenced? Last-modified date alone is not enough — was it actually used?

---

## Red Flag 7: Approvers overrule without explanation

**Symptom.** Driver proposes; Approver vetoes with "I don't think so". No written rationale. Two months later, the decision recurs because the team doesn't understand why option A was killed.

**Why it's bad.** Veto without explanation undermines authority. The team cannot learn the Approver's pattern; the same debate recurs. Worse, junior team members generalize ("Approver hates option A") and self-censor on adjacent decisions.

**Bad example:**
> "Driver: 'I propose option A.' Approver: 'No.' [End of meeting. No written follow-up.]"

**Good example:**
> "Driver proposes option A in a 1-page memo. Approver responds in writing: 'Vetoing. Three reasons: (1) data privacy concern around X; (2) conflict with our enterprise positioning; (3) prefer option B because of Y. Open to a counter-proposal that addresses 1 and 2.' Rationale becomes a decision record."

**How to catch it.** Look at the last 5 vetoes. Did each have a written rationale? If no, the Approver is exercising veto without accountability.

---

## Red Flag 8: New decisions never added to chart

**Symptom.** DACI built at team formation. Six new decision categories have emerged. None are on the chart.

**Why it's bad.** A static DACI ages out. Teams take on new responsibilities — pricing changes, AI feature decisions, partnership reviews — and the chart silently becomes incomplete. New decisions get assigned ad-hoc; ad-hoc assignment is what DACI was supposed to replace.

**Bad example:**
> "DACI v1 covers 12 decisions. Team has added AI feature scope, pricing experiments, and customer-data partnerships since. None on the chart."

**Good example:**
> "DACI v3 (current). Quarterly refresh adds new decision categories: 'AI feature scope (Driver: PM, Approver: VP Product + Safety lead)', 'Pricing experiments (Driver: PM, Approver: VP Product, Contributors: Finance, Legal)'. Refresh date logged; outdated rows removed."

**How to catch it.** Look at the chart's last refresh date. If > 6 months old, new decision types have probably emerged but not been added.

---

## Red Flag 9: Treating DACI as RACI for tasks

**Symptom.** Chart lists "Build the feature", "Test the feature", "Deploy the feature" with D/A/C/I assignments.

**Why it's bad.** DACI is for *decisions*, not *tasks*. Task assignment is RACI (Responsible/Accountable/Consulted/Informed). Mixing them produces confusion — the chart looks comprehensive but is doing two different jobs poorly.

**Bad example:**
> "DACI row: 'Build the new dashboard'. Driver: PM. Approver: Eng Lead. (This is a task. The decision was 'do we build it?'; the task is 'build it once approved'.)"

**Good example:**
> "DACI rows are decisions: 'Whether to build the new dashboard' (D: PM, A: VP Product). 'Architecture for the dashboard' (D: Eng Lead, A: Eng Manager). Task execution lives in the sprint backlog / RACI / ticket assignment, not in the DACI."

**How to catch it.** Read each row's title. Does it start with "Whether to…" or imply a decision? If it starts with "Build/Test/Deploy", it is a task.

---

## Red Flag 10: Chart doesn't match how decisions actually happen

**Symptom.** Chart says "Driver: PM". In practice, every decision is made in a Slack thread between the Eng Manager and the VP Eng; PM is informed afterward.

**Why it's bad.** Chart-vs-reality mismatch is worse than no chart. New joiners learn the chart, then experience the actual workflow, and lose trust in both the chart and the leaders who published it.

**Bad example:**
> "Chart (published, signed-off): Driver = PM. Reality: every decision in a 2-person Slack thread between EM and VPE; PM informed in #product-updates."

**Good example:**
> "Step 1 in building the chart: map the *current-state* DACI — how decisions actually happen, not how leadership wishes they happened. Then design *target-state*. If current shows EM/VPE making decisions, that is the baseline. Either change behavior (PM becomes Driver, EM moves to C) or update the chart to match reality (PM is C, EM is D). Do not publish a fiction."

**How to catch it.** Ask 3 team members independently: "for the last 3 decisions, who actually drove them?" Compare to chart.

---

## Red Flag 11: Decision cycle time not tracked

**Symptom.** Team has DACI. Cannot answer "how long does a P0 decision take?" No data.

**Why it's bad.** The point of DACI is faster, cleaner decisions. Without tracking decision cycle time, you cannot tell if it's working. The team is doing the ritual without the metric.

**Bad example:**
> "DACI rollout summary: 'chart published, all decisions assigned'. No metric on cycle time, escalation rate, or reversal rate."

**Good example:**
> "DACI health metrics (tracked monthly): (1) Decision cycle time for P0 decisions: target < 5 business days. Current: 6.2d, trending down from 11d pre-DACI. (2) Decision reversal rate: target < 10%. Current: 8%. (3) Escalation rate (decisions escalated past Approver): target < 15%. Current: 12%. (4) Stakeholder confidence ('do you know who decides X?'): quarterly survey; current 78%."

**How to catch it.** Ask the DACI owner for the cycle-time number. No answer = the framework is theater.

---

## Red Flag 12: DACI imposed without team buy-in

**Symptom.** VP brings a pre-built DACI to the team meeting. "Here is how decisions work now." Team nods. Six weeks later, nothing has changed.

**Why it's bad.** DACI requires cultural buy-in. A chart imposed from above without the team's input lacks legitimacy. The team interprets it as a control move, not a clarity tool. They comply nominally and route around it.

**Bad example:**
> "VP's announcement: 'I have drafted a DACI for our team. Effective Monday.' Team meeting: 5 minutes of Q&A, no substantive discussion. Outcome: chart published, behavior unchanged."

**Good example:**
> "DACI workshop (2 hours, all team members): (1) Each person lists 3 decisions they have felt unclear on in the last quarter. (2) Group clusters into ~10 decision categories. (3) Per category, the group debates Driver and Approver assignments. (4) Disagreements escalate to the team's manager in real-time. (5) Chart is committed at end of workshop with everyone in the room. Re-reviewed at 30, 60, 90 days."

**How to catch it.** Ask team members: "did you help build this DACI?" If most say no, ownership is missing.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Too many Approvers | Any row with > 2 A's? |
| 2 | Driver-by-committee | Any row with > 1 D? |
| 3 | Driver lacks authority | Can Driver push back on Approver and have it land? |
| 4 | Informed treated as Approver | Has any I role objected late and caused a slip? |
| 5 | Everyone is Contributor | Any row with > 5 C's? |
| 6 | Built but never referenced | When was the chart last cited in a meeting? |
| 7 | Veto without explanation | Last 5 vetoes — written rationale present? |
| 8 | New decisions not added | Chart's last refresh date? |
| 9 | DACI as task list | Do rows start with "Build/Test" instead of "Whether to"? |
| 10 | Chart doesn't match reality | Ask 3 team members independently: who actually decides? |
| 11 | Cycle time not tracked | Current decision cycle time number? |
| 12 | Imposed without buy-in | Did team help build the chart? |

## Related Reading

- SKILL.md Troubleshooting
- `create-prd/` (Contacts section often maps to DACI roles)
- `post-mortem/` (action items frequently need DACI to assign owners)
- `dependency-map/` (cross-team decisions where DACI assigns the seam owner)
- Productside DACI guidance for product teams

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/daci-framework
