# stakeholder-map

> **Use these instructions for this whole conversation.** Apply them when: Maps stakeholders by power, interest and stance, then plans engagement and blocker conversion so objections surface early. Use for a major initiative, an enterprise deal, a re-org or a contested roadmap change.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Stakeholder Map

The agent builds a power x interest map with each person's stance, then an engagement plan that matches cadence to influence and gives every blocker a conversion plan. The point is to have no surprise vetoes late in the initiative.

**Done looks like:** stakeholders listed broadly (sponsors, decision-makers, veto holders, implementers, users, external parties), each rated power and interest 1-5 with a stance from champion to blocker; quadrant cadences met (manage closely weekly or tighter with an owner, keep satisfied at least monthly); every skeptic and blocker with a conversion plan; `stakeholder_analyzer.py` exits 0.

## When to Use

- Launching a major initiative (re-platform, pricing change, market expansion)
- An enterprise deal with a buying committee, or a re-org
- A roadmap change that hits several teams, or a pre-board decision
- A post-mortem: who did we fail to engage?

## Clarify First

Before mapping, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **The initiative being mapped:** the specific launch/deal/re-org/roadmap change (defines who counts as a stakeholder at all, Step 1).
- **Each stakeholder's power source:** hierarchy vs veto vs budget vs domain expertise (a compliance lead may outrank a VP; drives the Power axis in Step 2).
- **Each stakeholder's stance:** champion → supporter → neutral → skeptic → blocker (drives Step 3 and the conversion plans in Step 6).
- **Decision/launch deadline:** when the verdict lands (sets engagement cadence per quadrant, Step 5).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

```bash
# Six-person billing rollout map with cadences and a skeptic plan: exit 0
python3 scripts/stakeholder_analyzer.py \
  --input assets/sample_stakeholders.json --format markdown
```

```bash
# High-power blocker with no plan, missing owners and cadences: exit 1
python3 scripts/stakeholder_analyzer.py \
  --input assets/sample_stakeholders_flawed.json --format markdown
```

```bash
# Input schema and flags
python3 scripts/stakeholder_analyzer.py --help
```

## Tools Overview

`stakeholder_analyzer.py` is the quality gate for this skill. **What the analyzer checks:** each stakeholder named, with power and interest in 1-5 and a valid stance; manage-closely people with weekly-or-tighter cadence and an owner; keep-satisfied people with at least monthly cadence and an owner; skeptics and blockers with a conversion plan (fail for a blocker with power 4-5); at least one manage-closely stakeholder; a thin list for an initiative labelled "major". It checks only the people listed and cannot find who is missing.

**Exit codes:** `0` no fail findings · `1` at least one fail (an unnamed stakeholder, no stakeholders, a high-power blocker without a plan) · `2` unreadable file, invalid JSON or a top level that is not an object. JSON by default, `--format markdown`, `--output FILE`.

## Workflow

1. **List broadly.** Sponsors, decision-makers, veto holders, influencers, implementers, users, adjacent teams, vendors, regulators. Prune later; the person you skip is usually the one who objects.
2. **Rate power and interest (1-5).** Power is more than hierarchy: budget control, veto (legal, compliance, security), domain expertise, coalition and external legitimacy. A compliance lead with a veto often outranks a VP. Ratings of 4-5 count as high.
3. **Add stance:** champion, supporter, neutral, skeptic, blocker.
4. **Find the people to convert:** high power, high interest, not yet supporters.
5. **Set engagement per quadrant.** Manage closely: weekly 1:1 and co-authoring. Keep satisfied: monthly pre-briefs so they do not tune in late and veto. Keep informed: updates and a visible place for their concerns. Monitor: light touch.
6. **Plan each blocker.** The real objection (often not the stated one), the evidence that might move them, who they listen to, and whether to convert, neutralise or out-vote. Escalate when their authority is structurally needed; never route around legal, security, compliance or finance approvers.
7. **Audit.** Write the map as JSON (schema in `--help`; `assets/sample_stakeholders.json`) and run the analyzer. It must pass with no fail findings; then verify that each warning is fixed. Refresh the map each quarter or project phase.

Engagement patterns for sponsors, powerful skeptics, powerless advocates and absent leaders are in the appendix of `references/stakeholder-mapping-framework.md`.

## Anti-Patterns

### Power read off the org chart
**Mistake:** Only VPs and above are rated high power.
**Why it happens:** Hierarchy is visible; vetoes and expertise are not.
**Instead:** Rate budget, veto, expertise and coalition power too. The security reviewer who can block go-live belongs in manage closely or keep satisfied.

### The sleeping authority
**Mistake:** A high-power, low-interest executive hears about the initiative at the final review and vetoes it.
**Why it happens:** Low interest reads as low priority.
**Instead:** Give every keep-satisfied stakeholder an owner and a monthly pre-brief; five-minute readouts are enough.

### A map with no plan
**Mistake:** The 2x2 is drawn and filed.
**Why it happens:** Mapping feels like the work.
**Instead:** Every quadrant gets a cadence and an owner, and every blocker a conversion plan with a date.

More with fixes: `references/stakeholder-anti-patterns.md`.

## Scope & Limitations

**In Scope:**
- A Power x Interest 2x2 with 1-5 ratings and four quadrants: manage closely, keep satisfied, keep informed and monitor
- A support stance per stakeholder from champion to blocker, and the high-power, high-interest, not-yet-supportive group to convert
- Engagement cadence per quadrant and conversion plans for blockers and skeptics
- A map audit for cadence and owners by quadrant, blockers and skeptics without plans, and missing decision-makers (`stakeholder_analyzer.py`)
- Launch, re-org, enterprise buying-committee and failed-launch post-mortem maps

**Out of Scope:**
- Assigning decision rights for a specific decision (see `project-management/execution/daci-framework/`)
- Writing the status updates and communications that the engagement plan calls for (see `project-management/execution/status-update-generator/` and `project-management/team-communications/`)
- Running a sales deal strategy beyond the stakeholder map (see `business-growth/sales-engineer/`)
- Legal and regulatory review of the initiative (see `c-level-advisor/general-counsel-advisor/`)

**Important Caveats:**
- Power, interest and support ratings are judgment calls entered by hand. The tool audits the map it is given and cannot discover missing people.
- The skill recommends building the map with someone politically aware. A solo map often misses lateral resistance.
- Power and stance shift. The map goes stale unless it is refreshed each quarter or project phase.
- The map can hold sensitive opinions about named colleagues. Who sees it is the team's call.

## Files

| File | Purpose |
|------|---------|
| `scripts/stakeholder_analyzer.py` | Stakeholder map audit |
| `assets/sample_stakeholders.json` | Billing rollout map; exits 0 |
| `assets/sample_stakeholders_flawed.json` | Map with an unplanned high-power blocker; exits 1 |
| `assets/stakeholder_map_template.md` | Fill-in template |

## Reference Documentation

- [references/stakeholder-mapping-framework.md](references/stakeholder-mapping-framework.md): Power and interest dimensions, support spectrum, engagement patterns
- [references/stakeholder-anti-patterns.md](references/stakeholder-anti-patterns.md): Common failures and fixes

## Related skills

- `project-management/execution/daci-framework` — decision-rights model
- `project-management/execution/summarize-meeting` — communication artifacts
- `c-level-advisor/ceo-advisor` — executive context
- `c-level-advisor/general-counsel-advisor` — legal stakeholder navigation
- `business-growth/sales-engineer` — buying-committee mapping

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/stakeholder-anti-patterns.md

# Stakeholder Mapping — Anti-Patterns + Fixes

## A1 — No map; trust the org chart
**Symptom:** "We just engage who we're supposed to."

**Fix:** Org chart shows hierarchy. Stakeholder map shows actual power +
interest. Cross-functional initiatives need explicit stakeholder mapping.

## A2 — Map exists; engagement plan doesn't
**Symptom:** Map drawn at kickoff; nobody refers to it again.

**Fix:** Map + engagement plan per quadrant + named cadence. Maintain.

## A3 — Ignoring blockers
**Symptom:** "Just don't tell them" or "They'll come around."

**Fix:** Blockers don't go away. Explicit conversion plan:
- Discover real objection
- Find evidence
- Find messenger
- Time the move

## A4 — Sleeping authority surprise
**Symptom:** HP/LI stakeholder absent during planning; emerges to veto at announcement.

**Fix:** Pre-brief HP/LI before any moment they could derail. Monthly
cadence; 5-min ask. Make engagement low-friction.

## A5 — Power = hierarchy
**Symptom:** Only org-chart hierarchy considered. Compliance, legal, security treated as advisory.

**Fix:** Veto power = power. CISO who blocks contract = HP regardless of org chart.

## A6 — Solo map
**Symptom:** PM builds stakeholder map alone.

**Fix:** Map with someone politically savvy (chief of staff, longtime
engineer, head of CS). Solo maps miss power dynamics.

## A7 — Static map
**Symptom:** Map from kickoff used 6 months later.

**Fix:** Refresh per quarter or major phase. Re-org, exec hire, pivot =
immediate refresh.

## A8 — Treating advocates as automatic supporters
**Symptom:** Champions assumed; never engaged.

**Fix:** Champions still need:
- Information to share
- Talking points
- Ammunition for their advocacy

Without these, champions go silent.

## A9 — Conflating power and influence
**Symptom:** CEO listed as highest power; no engagement plan because "we don't bother CEO".

**Fix:** If CEO has high power AND interest in initiative, engagement
plan needed. Failing to engage CEO when they care = surprise veto.

## A10 — Map without DACI
**Symptom:** Stakeholders listed; decision rights unclear.

**Fix:** Per major decision: who Decides? who Advises? who is Informed?
Map + DACI = complete.

## Worked example — enterprise deal stakeholder map

### Deal context
- Acme is selling $500K SaaS deal to Customer-X
- Customer-X has 12-person buying committee
- 6-month sales cycle expected

### Stakeholder map

| Stakeholder | Role | Power | Interest | Support | Engagement |
|-------------|------|-------|----------|---------|-------------|
| Mary, VP IT | Economic buyer | 5 | 5 | Champion | Weekly 1:1, exec sponsor pairing |
| John, CIO | Final approver | 5 | 3 | Neutral | Monthly brief, pre-brief major moments |
| Lisa, CISO | Veto power (security) | 4 | 4 | Skeptic | Address security concerns explicitly; deliver SOC 2 + pen test reports |
| Mike, IT Director | Technical buyer | 4 | 5 | Champion | Weekly tech review; co-design integration |
| Tom, IT Manager | User community lead | 2 | 5 | Supporter | Provide demo access; collect testimonials |
| Sarah, Procurement | Process owner | 4 | 2 | Neutral | Engage at right phase; have legal-friendly contracts ready |
| Janet, GC | Veto power (legal) | 4 | 2 | Neutral | Standard MSA + DPA; respond to redlines fast |
| Bob, Network Lead | Technical implementer | 2 | 3 | Neutral | Include in technical scoping calls |
| Carol, Helpdesk Lead | User impact | 2 | 4 | Skeptic | Address support model concerns; pilot with willing team |
| Dave, Finance | Budget approver | 3 | 3 | Neutral | ROI model; phased payment terms |
| Eve, Compliance | Veto power | 3 | 3 | Neutral | Compliance docs ready; map to their framework |
| Frank, Operations Lead | Adjacent impact | 1 | 1 | Neutral | Monitor; quarterly inclusion |

### Critical insights from map

1. **Mary is the champion + economic buyer** — invest heavily; don't lose her
2. **Lisa (CISO) is the riskiest skeptic** — her objection could kill deal; address early
3. **John (CIO) is HP/LI** — pre-brief before any major moment to prevent surprise veto
4. **3 veto holders** (Lisa, Janet, Eve) — all need explicit conversion
5. **Carol (skeptic, but LP)** — could rally helpdesk team against; address pilot offer

### Engagement plan

| Stakeholder | Frequency | Owner | Format | Goal |
|-------------|-----------|-------|--------|------|
| Mary | Weekly | AE | 1:1 + sponsor pairing | Maintain Champion |
| John | Monthly | AE + CRO | Pre-brief | Maintain Satisfied; prevent veto |
| Lisa | Bi-weekly | SE + Security partner | Tech + risk review | Convert Skeptic → Neutral+ |
| Mike | Weekly | SE | Tech review | Maintain Champion |
| Lisa, Janet, Eve | Joint kickoff | AE + Legal | Compliance review | Convert all 3 vetoes |

### Blocker conversion plan: Lisa (CISO)

- **Stated objection:** "We need SOC 2 Type 2 + pen test + DPA + data residency"
- **Actual concern (probed):** Bad experience with prior vendor's breach
- **Evidence to address:**
  - SOC 2 Type 2 report (provide)
  - Recent pen test summary (provide)
  - Incident response runbook (provide)
  - 3 reference customers who completed her security review
- **Messenger:** Acme CISO calls Lisa direct (peer-to-peer)
- **Timing:** Before any pricing discussion; security clears the path

Initiative likely to succeed = explicit map + engagement + blocker plan
+ regular refresh.

## Checklist

Before declaring a stakeholder map workable:

- [ ] All stakeholders listed (20+ for major initiative)
- [ ] Power + Interest + Support rated per stakeholder
- [ ] Power dimensions beyond hierarchy considered
- [ ] Blockers have conversion plans
- [ ] HP/LI stakeholders have light-engagement plan
- [ ] Champions have ammunition + tasks
- [ ] DACI applied to major decisions
- [ ] Engagement cadence + owner per quadrant
- [ ] Refresh date scheduled
- [ ] Map built with someone politically savvy (not solo)

## references/stakeholder-mapping-framework.md

# Stakeholder Mapping — Framework Reference

## 1. Power dimensions

Power comes in many forms beyond hierarchy:

### Hierarchical
- Org chart position
- Reporting relationships
- Direct authority over budget / headcount

### Veto power
- Legal: can block on contractual or regulatory grounds
- Security / CISO: can block on risk grounds
- Privacy / DPO: can block on data grounds
- Compliance: can block on policy grounds
- Finance: can block on budget grounds

These often have *less* hierarchy but *more* veto. Don't underestimate.

### Domain expertise power
- The one person who actually understands the system
- The technical lead who'll implement
- The customer-success rep who knows the customers
- They can't fire you but they can sandbag

### Coalition power
- Influences a faction (their direct reports + cross-functional allies)
- Often middle management with strong informal authority

### External legitimacy power
- Analyst relations (Gartner, Forrester contact)
- Customer reference
- Partner relationship
- Regulator contact

### Information power
- Owns the data others need
- Controls the narrative (PR, comms, IR)
- Has the relationship history (CSM)

## 2. Interest dimensions

Interest = how much the stakeholder cares:

### Outcome impact
- Does it move their team's KPIs?
- Does it affect their P&L?

### Personal stake
- Career risk / reward
- Compensation impact
- Ego / reputation

### Resource impact
- Does it touch their headcount / budget?

### Public visibility
- Will their name be associated?
- Reputational risk?

## 3. Support spectrum

Beyond power × interest, position on:

- **Champion** — actively advocates; rallies others
- **Supporter** — positive; passive support
- **Neutral** — undecided; convertible
- **Skeptic** — has concerns; needs evidence
- **Blocker** — actively opposes; will fight

Champion + Supporter = need to nurture
Neutral = convertible
Skeptic + Blocker = need conversion strategy

## 4. The 2x2 in action

### Quadrant A — Manage closely (HP/HI)
**Profile:** key decision-makers + engaged advocates and skeptics

**Engagement:**
- Weekly 1:1 (you bring updates + asks)
- Co-author key documents
- Veto power respected; used carefully
- They're the "first call" before big moves

**Risks:**
- Over-engaging blockers can paralyze you
- Under-engaging champions wastes leverage

### Quadrant B — Keep satisfied (HP/LI)
**Profile:** powerful but not engaged

**Engagement:**
- Monthly executive briefing
- Pre-brief before major decisions
- Make engagement low-friction (5-min asks)
- Don't surprise

**Risks:**
- Sleeping authority wakes up late and vetoes
- "I would have flagged that if anyone asked" is a common failure

### Quadrant C — Keep informed (LP/HI)
**Profile:** advocates, detractors, implementers, users

**Engagement:**
- Email updates + newsletters
- Open forums (AMA, Slack channel)
- Surface their concerns publicly to show responsiveness

**Risks:**
- Detractors here can build coalitions
- Advocates here can be undervalued

### Quadrant D — Monitor (LP/LI)
**Profile:** tangential parties

**Engagement:**
- Quarterly newsletter; no proactive
- Inclusion in broad announcements

**Risks:**
- Letting position shift unnoticed (LP → HP)

## 5. Engagement cadence templates

| Cadence | Forum | Output |
|---------|-------|--------|
| Daily | Slack channel updates | Status |
| Weekly | 1:1 (HP/HI), team standup, Slack digest | Decisions, blockers |
| Bi-weekly | Steering committee | Decisions, escalations |
| Monthly | Exec brief (HP/LI) | Strategic update |
| Quarterly | Board / all-hands | High-level recap, asks |

## 6. The blocker conversion playbook

For each blocker:

### Step 1 — Understand the actual objection
Stated objections often hide real ones:
- "It's too expensive" → actually "I lose budget control"
- "We tried that before" → actually "I championed the old way; new way embarrasses me"
- "The data doesn't support it" → actually "I don't trust your team"

Probe carefully (often via someone neutral).

### Step 2 — Find evidence that addresses it
- Customer references
- Pilot data
- Industry analyst reports
- Peer company examples

### Step 3 — Find the right messenger
- Their peer (lateral influence)
- Their superior (vertical influence)
- An external authority (analyst, board member)
- A customer they trust

### Step 4 — Time the move
- Pre-brief in 1:1 before public
- Address objection at the right forum (not in front of their boss; not via email)
- Give them a graceful path to support

### Step 5 — Lock in support visibly
- Get explicit verbal agreement
- Note in writing (meeting notes; never quote without permission)
- Surface their support to others

## 7. DACI / RACI cross-cut

After stakeholder mapping, apply decision-rights:

| Role | Definition |
|------|------------|
| **D**river | Owns getting the decision made (often you) |
| **A**pprover | Has authority to approve (1-2 max) |
| **C**ontributor | Provides input; doesn't decide |
| **I**nformed | Notified after decision |

A clean DACI prevents:
- 7 approvers (paralysis)
- 0 approvers (drift)
- Surprised informed parties

See `project-management/execution/daci-framework`.

## 8. Stakeholder map by initiative type

### Product launch
- Eng (build), Design (UX), PM (drive), Marketing (launch), Sales (sell),
  CS (onboard), Support (help), Legal (review), Security (review), Exec
  (approve), Customers (use)

### Pricing change
- Sales (executes), Marketing (positioning), Finance (modeling), Legal
  (contracts), CS (customer comms), Exec (approval), Existing customers
  (impact), Prospects (perception)

### Re-organization
- Affected employees (every one), People Ops (process), Legal, Finance,
  Exec, Department heads, Adjacent teams, External (customers,
  partners), Communications

### Enterprise deal
- Economic buyer, Technical buyer, End users, Executive sponsor, IT,
  Security, Procurement, Legal, Champion (internal advocate)

## 9. Refresh cadence

Stakeholder maps go stale fast:
- Per-initiative: refresh at each phase
- Per-org: review quarterly
- Per major event: re-org, exec hire, pivot — refresh immediately

## 10. Stakeholder map artifacts

For each initiative:

- **Map (2x2 with names)**
- **Engagement plan (per stakeholder; cadence + owner)**
- **Blocker conversion plan (per blocker)**
- **Decision log (DACI per decision)**
- **Communications schedule (what / when / to whom)**

These artifacts live as long as the initiative.

## Appendix: engagement patterns by stakeholder type

_Moved from SKILL.md._

**For executive sponsor (HP/HI):**
- Weekly 1:1 (you bring updates + asks)
- Co-author the strategic narrative
- Defend at board level
- Veto power to be used selectively

**For powerful skeptic (HP/HI, low support):**
- Discover the actual objection (often different than stated)
- Find evidence that addresses it
- Pre-brief before big decisions
- Make their support visible to their peers

**For powerless advocate (LP/HI, high support):**
- Use them to influence others
- Amplify their voice publicly
- Don't burn them with surprise asks

**For powerful absent leader (HP/LI):**
- Don't let them tune in late and veto
- Pre-brief before key decisions
- Make engagement low-friction (5-min readouts)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/stakeholder-map
