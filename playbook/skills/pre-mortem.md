# pre-mortem

> **Use these instructions for this whole conversation.** Apply them when: Runs a pre-mortem that sorts launch risks into evidenced tigers, paper tigers and unspoken elephants, each with an owner. Use when a big launch, build or migration is coming, or the team has a bad feeling it cannot name.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Pre-Mortem Risk Analysis Expert

## Overview

A pre-mortem is a prospective hindsight exercise: imagine that your product has launched and failed, then work backward to identify why. This skill uses the Tiger / Paper Tiger / Elephant classification to categorize risks by type and urgency, ensuring launch-blocking issues are addressed before launch while avoiding wasted effort on unlikely risks.

## Core Capabilities

- **Prospective hindsight framing** — "It is 14 days after launch, and we failed. Why?" surfaces specific, honest risks.
- **Tiger / Paper Tiger / Elephant classification** — separate real evidenced risks (Tigers) from anxiety (Paper Tigers) and unspoken concerns (Elephants).
- **Urgency triage** — tag each Tiger Launch-Blocking, Fast-Follow, or Track with owner and decision date.
- **6-phase facilitation** — scene-setting, silent generation, cluster, classify, mitigate, address elephants in 60-90 minutes.
- **Automated categorization** — `risk_categorizer.py` summarizes distribution and flags elephants needing escalation.

## When to Use

- Before committing significant resources to build (post-ideation, post-validation).
- Before a major launch, migration, or architectural change.
- When the team has "a bad feeling" they cannot articulate.
- When stakeholder confidence is high and you need to stress-test it.

## Clarify First

Before running the pre-mortem, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **The thing being stress-tested:** the specific launch/build/migration that "failed 14 days after launch" (anchors the prospective-hindsight framing).
- **Failure horizon:** the date/milestone you imagine looking back from (a vague horizon produces vague risks).
- **Who's in the room:** the 4-8 participants and whether psychological safety exists (elephants only surface with candor and the right people).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Settle the Clarify First inputs and run the session from `references/methodology-and-tools.md` (scene-setting, silent generation, cluster, classify, mitigate, elephants).
2. Record each risk with `description`, `category` (`tiger`/`paper_tiger`/`elephant`) and `evidence`; tigers also need `urgency` (`launch_blocking`/`fast_follow`/`track`), and launch-blockers an `owner` and `decision_date`.
3. Run `risk_categorizer.py` and fix its findings before the session closes.
4. Done when the tool exits 0, every launch-blocker has an owner and a decision date, and each elephant has a person who will raise it.

```bash
python3 scripts/risk_categorizer.py assets/sample_risks.json          # exit 0
python3 scripts/risk_categorizer.py assets/sample_risks_flawed.json   # exit 1
python3 scripts/risk_categorizer.py --demo --format json
```

The tool groups risks by category and urgency, flags elephants whose text carries escalation signals (no owner, blocked, security, compliance, legal and similar), and reports two findings a rushed session skips: a launch-blocking tiger with no `owner` or `decision_date`, and a tiger whose evidence is speculative ("might", "could", "we think"), which makes it a paper tiger until shown otherwise. Exit codes: 0 no findings, 1 findings, 2 bad input (missing file, invalid JSON, missing fields). Document the session with `assets/pre_mortem_template.md`.

## Anti-Patterns

### Mitigating Paper Tigers
**Mistake:** "AWS regional outage on launch day" is classed as a Tiger and gets weeks of redundancy work, with no evidence that it is likely.
**Why it happens:** A frightening consequence feels like a high probability.
**Instead:** For every Tiger, write the `evidence` that it could actually happen. A described consequence alone does not count. With no evidence, reclassify it as `paper_tiger` and cover it with a standard runbook.

### Risks too vague to act on
**Mistake:** The list holds "stakeholder issues", "scope creep" and "technical risk".
**Why it happens:** Generic labels are safe to say aloud and need no evidence.
**Instead:** Describe each risk as a concrete failure scenario in 1-2 sentences, such as "the CRO blocks launch on Day -7 because the enterprise SKU was cut". Translate worries ("the design feels weak") into a measurable consequence, or drop them.

### Running the pre-mortem too late
**Mistake:** The session happens a week before launch and surfaces a Tiger that needs four weeks of work. The team launches anyway.
**Why it happens:** Pre-mortems get scheduled as a launch-readiness check instead of a planning step.
**Instead:** Run the first pre-mortem at project kickoff and a second one around Day -30. For each risk, confirm it can still be mitigated in the time left.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/methodology-and-tools.md](references/methodology-and-tools.md)** — the thought experiment, full Tiger/Paper Tiger/Elephant classification with examples, urgency table, the 6-phase facilitation script, `risk_categorizer.py` usage and flags, output formats, troubleshooting, success criteria, and bibliography. Read when running or scripting a session.
- **[references/pre-mortem-guide.md](references/pre-mortem-guide.md)** — Gary Klein's origin and why pre-mortems work, when (and when not) to run one, deep classification criteria across domains, the facilitation timeline, and a worked SaaS launch example. Read for the theory and a full example.
- **[references/red-flags.md](references/red-flags.md)** — 12 anti-patterns (mitigation theater, groupthink, vague risks, over-mitigated elephants, late pre-mortems, missing owners) with bad/good examples and one-line checks. Read before sharing pre-mortem output.

## Scope & Limitations

**In Scope:** prospective hindsight using the "14 days after launch failure" framing; Tiger / Paper Tiger / Elephant classification with urgency levels; automated elephant escalation detection; risk registry generation; facilitation methodology for in-person and remote teams.

**Out of Scope:** ongoing risk management and tracking (see `senior-pm/scripts/risk_matrix_analyzer.py`); quantitative probability/impact scoring (`senior-pm/`); product discovery and hypothesis validation (`brainstorm-experiments/`); technical architecture risk assessment (`engineering/` skills).

**Important Caveats:** most effective with 4-8 participants; the elephant escalation keyword check is a heuristic; pre-mortems complement, not replace, assumption mapping (`identify-assumptions/`); psychological safety is a prerequisite.

## Files

| File | Purpose |
|------|---------|
| `scripts/risk_categorizer.py` | Categorizes risks, flags elephants to escalate, gates on unowned launch-blockers and speculative tigers |
| `assets/sample_risks.json`, `assets/sample_risks_flawed.json` | Runnable inputs: sound (exit 0) and flawed (exit 1) |
| `assets/pre_mortem_template.md` | Session template |
| `examples/shared-dashboards-v1-pre-mortem.md` | Worked session |
| `references/*.md` | See References |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/methodology-and-tools.md

# Pre-Mortem Methodology & Tooling

> Read this when running a session end-to-end: the thought experiment, full risk classification with examples, the 6-phase facilitation script, the `risk_categorizer.py` tool, output formats, troubleshooting, and success criteria.

## Core Concept

### The Thought Experiment

> "It is 14 days after launch. The product has failed. What went wrong?"

This framing exploits a cognitive bias: people are better at explaining past events than predicting future ones. By placing the failure in the "past" (even fictitiously), participants generate more specific and honest risk assessments.

## Risk Classification

### Tigers (Real Risks)

Tigers are real, evidence-backed risks that could cause serious harm if not addressed.

**Characteristics:**
- Supported by data, past experience, or observable trends.
- The team can describe a plausible failure scenario in concrete terms.
- Ignoring them would be negligent.

**Examples:**
- "Our authentication service went down 3 times last month. A launch-day outage is plausible."
- "We have zero customers in the enterprise segment. Our sales team has no enterprise relationships."
- "The EU regulation takes effect in 60 days. We have not started compliance work."

### Paper Tigers (Look Scary but Unlikely)

Paper Tigers are risks that sound alarming but, on closer inspection, are unlikely or have minimal real impact.

**Characteristics:**
- Based on hypothetical scenarios without supporting evidence.
- The probability is very low, or the impact would be manageable.
- Often raised because of general anxiety rather than specific knowledge.

**Examples:**
- "A competitor might copy our feature" -- possible, but their execution timeline is 6-12 months.
- "The server might not handle 100x traffic" -- but our realistic projection is 5x, with auto-scaling.
- "Users might hate the new UI" -- but usability testing with 8 users showed high satisfaction.

### Elephants (Unspoken Concerns)

Elephants are the risks everyone knows about but nobody talks about. They are the "elephant in the room."

**Characteristics:**
- The team avoids discussing them due to politics, hierarchy, or discomfort.
- Often involve people, process, or organizational issues rather than technical ones.
- Frequently the actual cause of failure when projects fail.

**Examples:**
- "The tech lead does not believe in this project and has been disengaged for weeks."
- "The CEO's pet feature is driving the roadmap, but customers have not asked for it."
- "We do not have a plan for what happens when the contractor's contract ends next month."

## Tiger Urgency Classification

Once a risk is classified as a Tiger, assign an urgency level:

| Urgency | Definition | Action Required |
|---------|-----------|----------------|
| **Launch-Blocking** | If unresolved, the launch should not proceed. | Concrete mitigation plan, assigned owner, decision date before launch. |
| **Fast-Follow** | Must be addressed within 2 weeks after launch. | Documented plan, assigned owner, scheduled for first post-launch sprint. |
| **Track** | Should be monitored and addressed if it escalates. | Added to risk register, reviewed at regular cadence. |

## Methodology

### Phase 1: Set the Scene (5 minutes)

The facilitator reads this prompt to the group:

> "Imagine it is 14 days after our launch. The product has failed. Users are not adopting it, key metrics are down, and leadership is asking what went wrong. Take 10 minutes to write down every reason you can think of for why we failed. Be specific. Be honest. Nothing is off limits."

**Ground rules:**
- Anonymous contributions (sticky notes or digital equivalent).
- No attribution, no blame, no judgment.
- Quantity over quality in the first round.

### Phase 2: Generate Risks (10 minutes)

Each participant independently writes down failure scenarios. One risk per sticky note. Aim for 5-10 per person.

**Prompts to stimulate thinking:**
- What technical system is most likely to break?
- What customer objection have we not addressed?
- What team dynamic could derail us?
- What external event could change our assumptions?
- What are we pretending is not a problem?
- What decision are we avoiding?

### Phase 3: Share and Cluster (15 minutes)

1. Read each risk aloud (without attribution).
2. Place on the board.
3. Group similar risks together.
4. Merge duplicates.

### Phase 4: Classify (15 minutes)

For each cluster, the group decides:

| Classification | Criteria |
|---------------|----------|
| **Tiger** | Supported by evidence. Plausible failure scenario. |
| **Paper Tiger** | Sounds scary but unlikely or low-impact on inspection. |
| **Elephant** | The room got quiet when this was read. People exchanged glances. |

For each Tiger, assign urgency: Launch-Blocking, Fast-Follow, or Track.

### Phase 5: Mitigation Plans (15 minutes)

For each **Launch-Blocking Tiger**, complete:

| Field | Description |
|-------|-------------|
| **Risk** | Clear description of the risk |
| **Evidence** | What data or experience supports this being a real risk? |
| **Mitigation** | Specific, concrete action to reduce the risk |
| **Owner** | Single person accountable |
| **Decision Date** | Date by which the mitigation must be complete or the launch decision revisited |

### Phase 6: Address Elephants (10 minutes)

Elephants require a different approach than Tigers:

1. **Acknowledge** -- Name the elephant explicitly. "The team is concerned that..."
2. **Assess** -- Is this actually a Tiger in disguise? If so, reclassify.
3. **Decide** -- Either address it (assign an owner) or consciously accept it (document the acceptance and rationale).

## Python Tool: risk_categorizer.py

Categorize and analyze risks using the CLI tool:

```bash
# Run with demo data
python3 scripts/risk_categorizer.py --demo

# Run with custom input
python3 scripts/risk_categorizer.py input.json

# Output as JSON
python3 scripts/risk_categorizer.py input.json --format json
```

### Input Format

```json
{
  "risks": [
    {
      "description": "Authentication service has had 3 outages in the last month",
      "category": "tiger",
      "evidence": "Incident reports from last 30 days",
      "urgency": "launch_blocking"
    }
  ]
}
```

### Output

Risk distribution summary, action plans for launch-blocking tigers, and flags for elephants that may need investigation.

See `scripts/risk_categorizer.py` for full documentation.

## Output Format

### Pre-Mortem Summary

```
Pre-Mortem Analysis: [Product/Feature Name]
Date: YYYY-MM-DD
Participants: [list]
Total risks identified: N
  - Tigers: X (Launch-Blocking: A, Fast-Follow: B, Track: C)
  - Paper Tigers: Y
  - Elephants: Z
```

### Risk Registry

| # | Risk | Category | Urgency | Evidence | Mitigation | Owner | Decision Date |
|---|------|----------|---------|----------|-----------|-------|--------------|
| 1 | ... | Tiger | Launch-Blocking | ... | ... | ... | ... |
| 2 | ... | Tiger | Fast-Follow | ... | ... | ... | ... |
| 3 | ... | Paper Tiger | -- | ... | -- | -- | -- |
| 4 | ... | Elephant | TBD | ... | ... | ... | ... |

Use `assets/pre_mortem_template.md` for the full document template.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Team generates mostly paper tigers | Risk aversion or surface-level thinking; team not fully immersing in the failure scenario | Re-read the thought experiment prompt slowly; extend silent writing time from 10 to 15 minutes; use specific prompts |
| No elephants surfaced | Psychological safety too low, or facilitator is a manager creating power dynamics | Use anonymous contribution (sticky notes or digital tools); consider an external facilitator; separate session from performance reviews |
| All risks classified as tigers | Team lacks calibration on what constitutes real evidence vs. anxiety | Require concrete evidence for each tiger; if evidence is hypothetical, reclassify as paper tiger |
| Elephant escalation check flags too many false positives | ESCALATION_KEYWORDS list is broad, matching common words in non-critical contexts | Review matched keywords in output; refine escalation thresholds; use the recommendation as a prompt, not a verdict |
| Launch-blocking tigers have no owners assigned | Pre-mortem session ended without Phase 5 mitigation planning | Always reserve 15 minutes for mitigation plans; do not skip Phase 5 even if the session runs long |
| Validation errors on input JSON | Missing required fields (`description`, `evidence`, `category`) or invalid urgency for tigers | Check that every tiger has `urgency` set to one of: `launch_blocking`, `fast_follow`, `track` |

## Success Criteria

- Pre-mortem conducted before every major launch, migration, or significant resource commitment
- At least 5-10 risks generated per person during the silent writing phase
- Risk distribution includes all three categories (not all tigers, not all paper tigers)
- Every launch-blocking tiger has an assigned owner, concrete mitigation plan, and decision date
- Elephants are explicitly named and either addressed or consciously accepted with documented rationale
- Pre-mortem findings are reviewed against actual outcomes post-launch to calibrate future sessions
- Session duration stays within 60-90 minutes total across all 6 phases

## Tool Reference

### risk_categorizer.py

Categorizes pre-mortem risks as Tigers, Paper Tigers, or Elephants. Generates action plans for launch-blocking tigers and flags elephants with escalation signals.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `input_file` | positional | (optional) | Path to JSON file with risks array |
| `--demo` | flag | off | Run with built-in sample data (7 risks across all categories) |
| `--format` | choice | `text` | Output format: `text` or `json` |

**Input fields per risk:**
- `description` (required): Clear description of the risk scenario
- `category` (required): One of `tiger`, `paper_tiger`, `elephant`
- `evidence` (required): Supporting data or observations
- `urgency` (required for tigers): One of `launch_blocking`, `fast_follow`, `track`

## Bibliography

- Gary Klein, "Performing a Project Pre-Mortem," *Harvard Business Review* (2007)
- Daniel Kahneman, *Thinking, Fast and Slow* (2011) -- prospective hindsight
- Chip Heath & Dan Heath, *Decisive* (2013) -- decision-making under uncertainty
- Amy Edmondson, *The Fearless Organization* (2018) -- psychological safety for surfacing elephants

## references/pre-mortem-guide.md

# Pre-Mortem Guide

## Origin: Gary Klein's Prospective Hindsight

The pre-mortem technique was developed by psychologist Gary Klein and published in the *Harvard Business Review* in 2007. It is based on research into "prospective hindsight" -- the finding that imagining an event has already occurred increases the ability to identify reasons for that event by 30%.

### Why Pre-Mortems Work

Traditional risk assessment asks: "What could go wrong?" This question triggers optimism bias -- people tend to minimize risks because they are invested in the plan's success.

A pre-mortem flips the frame: "The project has failed. Why?" This framing:
1. **Legitimizes dissent.** Team members have permission to voice concerns.
2. **Activates different cognitive processes.** Explaining a "past" event is easier than predicting a future one.
3. **Reduces groupthink.** The exercise explicitly asks for failure scenarios, breaking the social pressure to be positive.
4. **Surfaces elephants.** Anonymous contributions lower the barrier to raising sensitive issues.

### When to Run a Pre-Mortem

- **Before major commits.** Before allocating a full team to a multi-month effort.
- **Before launches.** 2-4 weeks before go-live, when there is still time to act on findings.
- **Before migrations or architectural changes.** High-risk, low-reversibility decisions.
- **Periodically during long projects.** Every 6-8 weeks for projects lasting more than a quarter.

### When NOT to Run a Pre-Mortem

- When the decision is already made and irreversible. A pre-mortem on a shipped feature wastes energy; run a retrospective instead.
- When the team lacks psychological safety. If people cannot speak honestly, the exercise will produce sanitized results.

---

## Tiger / Paper Tiger / Elephant Classification

### Tigers: Real Risks

**Definition:** Risks supported by evidence that could credibly cause the project to fail.

**How to identify:**
- Can the person describe a specific, plausible failure scenario?
- Is there data, past experience, or observable signals supporting this risk?
- Would a reasonable outside observer agree this is a real concern?

**Examples across domains:**

| Domain | Tiger Example |
|--------|--------------|
| Technical | "Our database query P99 latency is already 800ms. Adding the new feature will push it over SLA." |
| Market | "Three of our five pilot customers have gone silent after the demo. No follow-up despite outreach." |
| Operational | "The only person who knows the deployment process is on parental leave starting next week." |
| Financial | "Our burn rate at current headcount gives us 4 months of runway. The feature needs 5 months." |

### Paper Tigers: Perceived but Unlikely Risks

**Definition:** Risks that sound alarming but are unlikely to materialize or would have manageable impact.

**How to identify:**
- Is the scenario based on speculation rather than evidence?
- Is the probability very low (< 5%)?
- If it happened, could we recover quickly?
- Is this a general anxiety rather than a specific concern?

**Examples:**

| Perceived Risk | Why It Is a Paper Tiger |
|---------------|------------------------|
| "AWS might have a global outage on launch day" | Probability < 0.1%. Multi-AZ setup provides resilience. |
| "A major competitor might launch the same feature" | Their last release was 8 months ago. Even if they started now, we would have a 6-month head start. |
| "Users might abuse the API" | Rate limiting is in place. Abuse is detectable and reversible. |

**Caution:** Sometimes a Paper Tiger is actually a Tiger that the team is underestimating. If there is disagreement, investigate further before dismissing.

### Elephants: Unspoken Concerns

**Definition:** Risks that the team is aware of but avoids discussing, typically because they involve interpersonal dynamics, organizational politics, or uncomfortable truths.

**How to identify:**
- The room goes quiet when the topic is raised.
- People speak in euphemisms or generalities.
- The risk involves a person, a relationship, or a power dynamic.
- Multiple people have mentioned it privately but not in group settings.

**Examples:**

| Elephant | Why It Is Unspoken |
|----------|--------------------|
| "The project sponsor does not actually use the product and is making requirements based on assumptions" | Challenging the sponsor feels politically risky |
| "Two key engineers have been interviewing elsewhere" | Retention concerns feel disloyal to raise publicly |
| "The deadline was set by a sales commitment, not engineering estimation" | Nobody wants to push back on the VP of Sales |
| "We are building this because the CEO saw a competitor demo, not because of customer demand" | Questioning the CEO's judgment feels career-limiting |

**How to surface elephants:**
1. Anonymous contributions (sticky notes, digital forms).
2. Direct prompts: "What are we pretending is not a problem?"
3. One-on-one conversations before the session to prime participation.
4. Explicit psychological safety: "There will be no consequences for anything raised in this exercise."

---

## Urgency Classification Guide

Once a risk is classified as a Tiger, assign one of three urgency levels:

### Launch-Blocking

**Definition:** If this risk is not mitigated before launch, the launch should not proceed.

**Criteria (any one is sufficient):**
- The risk could cause data loss, security breach, or legal liability.
- The risk could cause >50% of target users to have a broken experience.
- The risk would make the core value proposition non-functional.
- The risk would cause immediate, public reputational damage.

**Required action:**
- Concrete mitigation plan with specific steps.
- Single accountable owner.
- Decision date: a specific date by which the mitigation is complete or the launch is postponed.

### Fast-Follow

**Definition:** This risk is real but manageable at launch. It must be addressed within 2 weeks post-launch.

**Criteria:**
- The risk affects a subset of users or a secondary flow.
- A temporary workaround exists (manual process, reduced functionality).
- The risk grows over time but is acceptable for a short window.

**Required action:**
- Documented plan.
- Assigned owner.
- Scheduled in the first post-launch sprint.

### Track

**Definition:** This risk should be monitored but does not require immediate action.

**Criteria:**
- The risk is real but low probability in the near term.
- The impact is manageable if it materializes.
- Early warning signals exist that would give time to respond.

**Required action:**
- Added to risk register.
- Monitoring metric or tripwire defined.
- Reviewed at regular cadence (weekly or bi-weekly).

---

## Facilitation Guide for Pre-Mortem Sessions

### Before the Session

1. **Invite the right people.** Include PM, Design, Engineering, QA, and at least one person outside the core team (fresh perspective).
2. **Set expectations.** Send a pre-read explaining the exercise and ground rules.
3. **Prepare materials.** Sticky notes (physical or digital), timer, board for clustering.
4. **Create safety.** Ensure anonymous contribution is possible.

### During the Session (60 minutes total)

| Phase | Duration | Facilitator Action |
|-------|----------|--------------------|
| Set the scene | 5 min | Read the failure prompt. Establish ground rules. |
| Silent generation | 10 min | Everyone writes risks independently. No talking. |
| Share and cluster | 15 min | Read aloud, group on board, merge duplicates. |
| Classify | 15 min | Vote or discuss: Tiger, Paper Tiger, or Elephant for each cluster. |
| Mitigation planning | 15 min | Assign owner, mitigation, and decision date for Launch-Blocking Tigers. |

### Facilitator Tips

- **Protect anonymity.** If reading sticky notes aloud, shuffle them first. Do not ask "whose is this?"
- **Probe Paper Tigers.** "What evidence would change this from a Paper Tiger to a Tiger?" This prevents premature dismissal.
- **Name Elephants explicitly.** "I notice the room got quiet. Let us talk about this one."
- **Keep the energy up.** This exercise can feel heavy. Remind participants that identifying risks is empowering, not demoralizing.
- **Time-box strictly.** The mitigation phase tends to expand. Keep it focused on Launch-Blocking items only.

### After the Session

1. Document all risks in the pre-mortem template.
2. Distribute to all participants and stakeholders.
3. Track Launch-Blocking mitigations in your project management tool.
4. Schedule a follow-up review 1 week before the decision date.

---

## Example Pre-Mortem: SaaS Feature Launch

**Product:** Analytics dashboard for a B2B SaaS product
**Launch date:** 3 weeks from pre-mortem
**Participants:** PM, 2 Engineers, Designer, QA Lead

### Tigers Identified

| # | Risk | Urgency | Evidence |
|---|------|---------|----------|
| T1 | Dashboard query timeout on accounts with >100K events | Launch-Blocking | Load testing showed P95 latency of 12s on large accounts (SLA is 3s) |
| T2 | Export-to-CSV does not handle special characters in data | Fast-Follow | Bug found in QA but not yet fixed. Affects ~15% of accounts. |
| T3 | No monitoring alerts for the new data pipeline | Track | Pipeline is new. We have logs but no automated alerting. |

### Paper Tigers Identified

| # | Risk | Why Paper Tiger |
|---|------|----------------|
| P1 | Competitor X might launch similar feature | Their last release was 9 months ago. We have a 6-month head start. |
| P2 | Users might not find the new dashboard | It is the default landing page. Discovery is not a concern. |

### Elephants Identified

| # | Risk | Resolution |
|---|------|-----------|
| E1 | The PM who requested this feature left the company. Nobody has validated the requirements with current customers. | Reclassified as Tiger (Fast-Follow). PM will run 5 customer interviews this week. |
| E2 | The team is burned out from the previous sprint. Quality may suffer. | Acknowledged. Reduced scope for launch: defer 2 non-critical features to Fast-Follow. |

### Action Plan (Launch-Blocking)

| Tiger | Mitigation | Owner | Decision Date |
|-------|-----------|-------|--------------|
| T1: Query timeout | Add query optimization + caching layer for large accounts. If not resolved by decision date, launch with a feature flag limiting to accounts <50K events. | Senior Engineer | 10 days before launch |

## references/red-flags.md

# Red Flags: Pre-Mortem

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them. Pair with the SKILL.md and Troubleshooting table.

## How to use this document

When you have just facilitated a pre-mortem or classified risks, scan the red flags below before sharing the output. Each red flag shows the *bad* and *good* version, anchored in Klein's prospective hindsight method and the Tiger/Paper Tiger/Elephant classification.

---

## Red Flag 1: Treating Paper Tigers as Tigers (Mitigation Theater)

**Symptom.** Risk list classifies "AWS could go down on launch day" as a Tiger and assigns 3 engineers to build redundancy. AWS has 99.99% SLA; the probability is negligible.

**Why it's bad.** Klein's framework explicitly separates Tigers (real, evidenced, plausible failure scenarios) from Paper Tigers (sound scary, lack evidence). Mitigating Paper Tigers burns capacity that should go to Tigers and Elephants. The result is "we mitigated everything" — but the actual launch fails on an unmitigated Tiger.

**Bad example:**
> "Tigers: (1) AWS regional outage on launch day. Mitigation: build multi-region redundancy ($50K, 2 engineers, 6 weeks)."

**Good example:**
> "Paper Tiger: AWS regional outage. Evidence: 99.99% SLA, no recent incidents in our region. Probability x impact below threshold for mitigation. Action: standard runbook, no extra investment."

**How to catch it.** For each "Tiger", what is the *evidence* of plausibility? If only the consequence is described (without evidence of likelihood), it may be a Paper Tiger.

---

## Red Flag 2: Groupthink on Risks (Everyone Names the Same Three)

**Symptom.** 8 people in pre-mortem; output lists 4 risks, all of which the senior person mentioned first. Real risks held by the team go unspoken.

**Why it's bad.** Klein's whole insight is that prospective hindsight surfaces risks that ordinary planning misses. Groupthink defeats this — risks become a recitation of the senior's worries instead of a genuine surfacing exercise. The fix is silent individual generation before any group discussion.

**Bad example:**
> Pre-mortem opens with the VP saying "I'm worried about scalability." 90% of subsequent risks named are scalability-related.

**Good example:**
> Pre-mortem opens with 10 minutes of silent individual writing: 'Imagine it's 14 days post-launch and the product failed. Write 5 things that went wrong, in detail.' Then round-robin sharing. Output: 22 distinct risks across 5 categories — only one of which is scalability."

**How to catch it.** Was there silent individual generation before group discussion? If discussion started open, groupthink corrupted output.

---

## Red Flag 3: Vague Risks ("Things Could Go Wrong")

**Symptom.** Risk list has items like "stakeholder issues", "scope creep", "technical risk." No specifics.

**Why it's bad.** Vague risks cannot be mitigated. "Stakeholder issues" could mean a hundred different scenarios, each with a different mitigation. Klein insists on *specific, concrete failure scenarios* — "the CRO will block the launch because we did not include the enterprise SKU."

**Bad example:**
> "Risk: Stakeholder alignment problems."

**Good example:**
> "Risk (Tiger): The CRO will block launch on Day -7 because the enterprise SKU was de-prioritized in scope. Evidence: CRO said in Q3 review 'enterprise must be in launch.' Mitigation: meet with CRO Day -21 to align scope; if not aligned by Day -14, escalate to CEO. Owner: PM."

**How to catch it.** For each risk, can you describe the *specific scenario* in 1-2 sentences? If not, the risk is vague.

---

## Red Flag 4: Elephants Treated as Tigers (Over-Mitigating Large Acceptable Risks)

**Symptom.** Risk "we may need to add a second sales engineer to support enterprise customers" is classified as a Tiger and triggers urgent staffing action.

**Why it's bad.** Elephants are large, expected risks that the business has chosen to accept. Treating them as Tigers wastes pre-launch focus. The right response to an Elephant is acknowledge, plan for, and continue — not mitigate as if it were a launch-blocker.

**Bad example:**
> "Tiger: 'We may need another sales engineer next quarter.' Mitigation: emergency hire."

**Good example:**
> "Elephant: Enterprise traction will require 1-2 additional sales engineers in Q3. This is large but expected; we have budget. Plan: open req now, hire by Q3 start. Not a launch-blocker."

**How to catch it.** Is the risk *unexpected* and *plausible*, or *large and expected*? If the latter, it is an Elephant.

---

## Red Flag 5: Pre-Mortem Held Too Late to Matter

**Symptom.** Pre-mortem held 1 week before launch. Surfaces a Tiger that requires 4 weeks of work to mitigate. The team launches anyway.

**Why it's bad.** Pre-mortems are valuable when there is still time to act. Held too late, they become theater — risks surfaced cannot be mitigated, and the team launches into known failure. Klein recommends pre-mortems *at the planning stage*, not the launch stage.

**Bad example:**
> Pre-mortem on Day -7. Tiger surfaces: 'Onboarding flow has not been usability-tested with non-technical users.' Cannot fix in 7 days. Launch proceeds.

**Good example:**
> Pre-mortem at project kickoff (Day -90). Tigers surface; mitigations planned. Second pre-mortem at Day -30 to re-check. Final launch checklist at Day -7 confirms Tigers have been addressed."

**How to catch it.** Can the surfaced risks actually be mitigated in the time remaining? If not, the pre-mortem was too late.

---

## Red Flag 6: No Owner per Risk (Diffuse Accountability)

**Symptom.** Risk list has 12 items. Mitigations are sketched. No name attached. "The team will handle it."

**Why it's bad.** Diffuse ownership = no ownership. The risks that are not assigned drift; week 4 of the project, they are still listed as "the team will handle" with no progress. Klein's framework requires explicit ownership of each Tiger.

**Bad example:**
> "Risk 1: Stakeholder alignment. Mitigation: hold meetings. Owner: team."

**Good example:**
> "Risk 1 (Tiger): CRO will block launch over enterprise scope. Owner: Sarah (PM). Mitigation: 1:1 with CRO by Day -21. Check-in: Day -14. Escalation path: if unresolved, escalate to CEO by Day -10."

**How to catch it.** Does every Tiger have a single named owner with a deadline? If multiple owners or no owner, the risk will drift.

---

## Red Flag 7: Failing to Update the Risk List

**Symptom.** Pre-mortem produces a risk list. The list lives in a doc, never updated. By Day -14, the team has discovered new risks not in the doc, and several listed risks are no longer relevant.

**Why it's bad.** Risk lists decay. A snapshot from Day -90 does not reflect Day -30 reality. Klein's prospective hindsight is most useful when run iteratively, with the list as a living tracker.

**Bad example:**
> Risk doc from Day -90. Not opened since.

**Good example:**
> Risk tracker updated weekly. Closed risks marked. New risks added as discovered. Status report each Friday: top 3 unmitigated Tigers + owners + ETAs. Visible to leadership."

**How to catch it.** When was the risk list last updated? Over 2 weeks = stale.

---

## Red Flag 8: Mitigation That Costs More Than the Risk

**Symptom.** Tiger with $50K expected impact. Mitigation costs $200K and 3 engineering months. Net result is negative.

**Why it's bad.** Mitigation must be proportionate. Spending more on mitigation than the risk's expected cost (impact x probability) is risk-aversion overcorrection. Klein's framework implicitly requires cost-benefit reasoning.

**Bad example:**
> Tiger: 'API rate limit could spike at launch.' Expected cost if it happens: 4 hours customer impact (~$2K). Mitigation: rebuild infrastructure with full elastic scaling ($150K, 2 engineering months)."

**Good example:**
> Tiger: 'API rate limit could spike at launch.' Expected cost: ~$2K. Mitigation: pre-launch load test + automated alerting + scale-up playbook on-call ($5K, 1 engineering week). Proportionate."

**How to catch it.** For each mitigation, is the cost less than (impact x probability)? If not, you are over-mitigating.

---

## Red Flag 9: Pre-Mortem as Solo PM Exercise

**Symptom.** PM lists risks alone in a doc. Workshop is not held; cross-functional input not gathered.

**Why it's bad.** Risks live in different parts of the org. Engineers know feasibility risks; designers know usability risks; support knows operational risks; sales knows market risks. A solo PM pre-mortem captures only PM-visible risks — typically the smallest set.

**Bad example:**
> PM solo doc: 8 risks listed.

**Good example:**
> Pre-mortem workshop with PM, design, engineering, support, sales, security. 22 risks surfaced from 8 different angles. Engineer caught a feasibility Tiger that PM had marked as a non-issue. Security caught an Ethical risk not previously considered."

**How to catch it.** Who was in the pre-mortem? If PM solo, the risk surface is incomplete.

---

## Red Flag 10: Pre-Mortem Without "What Would We Do?" (Mitigation Plans Missing)

**Symptom.** Risks identified, classified, ranked. No mitigation plans written. Team congratulates itself on a good pre-mortem and moves on.

**Why it's bad.** Identifying risks without planning responses is half the job. The mitigation plan is what turns awareness into reduced risk. Klein's process explicitly requires action commitments for each Tiger.

**Bad example:**
> "Tigers: 1. CRO blocking. 2. Enterprise SKU incomplete. 3. Onboarding untested. End of doc."

**Good example:**
> "Tiger 1: CRO blocking. Mitigation: scope alignment meeting Day -21, owner PM, escalation path CEO. Tiger 2: Enterprise SKU. Mitigation: split into MVP enterprise feature (in scope) + advanced (Q+1), owner EM. Tiger 3: Onboarding untested. Mitigation: 5-user usability test by Day -45, owner UX."

**How to catch it.** Every Tiger has a written mitigation plan? If not, awareness without action.

---

## Red Flag 11: Confusing Risk with Worry (Emotional, Not Evidence-Based)

**Symptom.** Risk list contains items the team feels worried about ("the design feels weak") but no concrete failure scenario.

**Why it's bad.** Worries are not risks. Worries are emotional signals worth investigating but cannot be assessed without translation into a concrete failure scenario. A pre-mortem of worries produces emotional alignment, not risk reduction.

**Bad example:**
> "Risk: The design feels weak."

**Good example:**
> "Worry: The design feels weak. Translated to risk: 'Users may not understand the value proposition from the landing page; signup conversion below 3% threshold.' Test: 5-user moderated test before launch. If conversion concern persists, classify as Tiger."

**How to catch it.** For each "risk", is there a concrete failure scenario with measurable consequence? If only feelings, translate or drop.

---

## Red Flag 12: No Post-Launch Verification (Did the Tigers Actually Bite?)

**Symptom.** Launched 6 weeks ago. No retrospective on which risks materialized vs which did not.

**Why it's bad.** Pre-mortem skill compounds with practice. Without post-launch verification, the team never learns which of their risks were real (Tigers) vs imagined (Paper Tigers). Next pre-mortem repeats the same misclassifications.

**Bad example:**
> Pre-mortem done. Launch done. No follow-up.

**Good example:**
> Post-launch retro at Day +30 includes a 'risk verification' section. Of the 7 classified Tigers, 4 materialized as predicted (mitigations worked or didn't); 3 did not materialize (re-classify as Paper Tigers for future). Of the 5 Paper Tigers, 1 actually materialized (we missed it). Learning: pattern X risks deserve more weight."

**How to catch it.** Was there a risk verification step in the launch retro? If not, the pre-mortem skill is not compounding.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Paper Tigers Mitigated | Each Tiger has evidence of plausibility? |
| 2 | Groupthink | Silent individual generation before discussion? |
| 3 | Vague Risks | Concrete scenario in 1-2 sentences per risk? |
| 4 | Elephants Over-Mitigated | Distinguished from Tigers (expected vs unexpected)? |
| 5 | Pre-Mortem Too Late | Risks mitigatable in time remaining? |
| 6 | No Owner per Risk | Each Tiger has named owner + deadline? |
| 7 | List Not Updated | Last update under 2 weeks? |
| 8 | Mitigation Costs More Than Risk | Mitigation cost < (impact x probability)? |
| 9 | Solo PM Pre-Mortem | Cross-functional workshop, not solo? |
| 10 | No Mitigation Plans | Every Tiger has written mitigation? |
| 11 | Worries Mistaken for Risks | Each risk has concrete failure scenario? |
| 12 | No Post-Launch Verification | Did Tigers actually bite? Reviewed in retro? |

## Related Reading

- SKILL.md Troubleshooting section (for symptom -> root cause -> resolution)
- references/klein-prospective-hindsight.md (if present)
- identify-assumptions/references/red-flags.md (for upstream assumption mapping)
- delivery-manager/references/red-flags.md (for adjacent incident/risk patterns)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/discovery/pre-mortem
