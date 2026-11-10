# outcome-roadmap

> **Use these instructions for this whole conversation.** Apply them when: Turn a feature-list roadmap into outcome statements placed in Now/Next/Later, and check each has a measure. Use when converting a feature-list roadmap, reviewing a roadmap before it goes to leadership, or quarterly planning.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Outcome Roadmap Expert

The agent transforms output-based roadmaps ("build feature X") into outcome-driven roadmaps ("enable customers to achieve Y") using the "so what?" technique and Now/Next/Later framing. It produces roadmaps that communicate strategy and measurable impact, not just feature lists and dates.

## Core Capabilities

- **Output → outcome transformation** — applies the formula "Enable [segment] to [outcome] so that [impact]" via a "so what?" chain that drills from feature to business metric.
- **Now/Next/Later classification** — sorts initiatives into horizons whose detail and commitment level match certainty.
- **Metric definition** — primary, secondary, and counter-metrics for Now/Next items.
- **Dependency capture** — technical, organizational, and market prerequisites per item.
- **Stakeholder-ready output** — text, JSON, and markdown reports grouped by horizon for alignment review.

## When to Use

- Converting a feature-list / date-driven roadmap into outcome-driven format.
- Communicating product strategy to executives or customers.
- Running quarterly planning and aligning teams around impact rather than deliverables.
- Anchoring roadmap items to customer value and OKRs.

## Clarify First

Before transforming the roadmap, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Customer segment + business impact per item:** the raw material for "Enable [segment] to [outcome] so that [impact]"; without it the outcome is a guess.
- **Target quarter per initiative and the current quarter:** drive Now/Next/Later placement and the commitment level.
- **Success metric with a baseline per Now/Next item:** an outcome nobody can measure is still an output.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Write the outcomes yourself.** For each initiative, run the "so what?" chain (feature → what changes for the user → which number moves → what the business gets) until you reach a named segment, a job and a number. State it as "Enable [segment] to [outcome] so that [impact]". The tool cannot write these; it checks them.
2. **Add the measures**: a metric with baseline and target for Now and Next items, a counter-metric for Now items. Later items stay metric-light on purpose; false precision there hurts credibility.
3. **Check the roadmap:**

```bash
python3 scripts/roadmap_transformer.py \
  --input assets/sample_roadmap_clean.json --as-of "Q3 2026"
```

4. **Fix every error and re-run.** Done when the tool exits 0 and three outcome statements read aloud could not be swapped between items.

**What the tool checks:** horizon from quarter vs `--as-of` (default: earliest quarter in the file, so samples read the same on any day; pass the current quarter for a live roadmap); more than 3 Now items; Now/Next items with no outcome, an outcome that starts with an output verb (build, launch, migrate...), no "so that", no metric, or a metric without baseline or target; Now items with no counter-metric; quarters already past. Items without an outcome get the "so what?" prompts for their type.

Input per initiative: `title`, `description`, `quarter` ("Q3 2026"), `type` (feature, improvement, infrastructure), and the fields you write: `outcome`, `metric {name, baseline, target}`, `counter_metric`. Flags: `--input F` or `--demo`, `--as-of`, `--format text|json|markdown`, `--output`.

**Exit codes:** 0 no errors, 1 at least one error (`assets/sample_roadmap.json` and `--demo` exit 1 by design: a feature list with 4 Now items), 2 missing file, invalid JSON, wrong shape or bad `--as-of`.

## Anti-Patterns

### Outcome statements on top of a dated feature list
**Mistake:** Each item opens with "Enable [X] to [Y] so that [Z]", but underneath sits a feature list with ship dates, and standups only discuss the dates.
**Why it happens:** Teams used to date-driven roadmaps add the outcome wording without changing how they work.
**Instead:** Under each Now item, list the success metric with baseline and target, and frame the features as a working hypothesis the team will change if the metric doesn't move. Check standup notes: if they name only features, the roadmap is still output-driven.

### Too many Now items
**Mistake:** The Now column lists 8 initiatives.
**Why it happens:** Everything feels urgent, and moving an item to Next feels like saying no to a stakeholder.
**Instead:** [RECOMMENDED] Cap Now at 2-3 items, sized to what the team can ship in 6-8 weeks. Move the rest to Next. More than 3 Now items means the commitment level on the roadmap is false.

### Interchangeable outcome statements
**Mistake:** "Enable users to be more productive, so we grow revenue." "Enable customers to succeed, so they retain better." The template is filled in mechanically.
**Why it happens:** The "Enable ... so that ..." formula is easy to fill with generic words, and a structural check passes them.
**Instead:** Each outcome names a specific segment, a specific job and a number. Read three statements aloud. If they could be swapped between items without anyone noticing, push the "so what?" chain 2-3 levels deeper.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

- **[references/outcome-roadmap-workflow.md](references/outcome-roadmap-workflow.md)** — read this when transforming a roadmap: the 6-step workflow with validation checkpoints, the "so what?" technique, Now/Next/Later detail levels, a full worked example, why output roadmaps fail, output structure, tool flags, troubleshooting, and success criteria.
- **[references/outcome-roadmap-guide.md](references/outcome-roadmap-guide.md)** — read this for the deeper guide: output-vs-outcome comparison, outcome formulas, and stakeholder communication strategies.
- **[references/red-flags.md](references/red-flags.md)** — read this to spot the common ways outcome roadmaps go wrong (false precision, mechanical templates, too many Now items) before sharing.

## Files

| File | Purpose |
|---|---|
| `scripts/roadmap_transformer.py` | Horizon placement and outcome-readiness check |
| `assets/sample_roadmap_clean.json` | Outcome roadmap that passes (exit 0) |
| `assets/sample_roadmap.json` | Output-style feature list (exit 1) |
| `assets/outcome_roadmap_template.md` | Roadmap document template |
| `examples/output-to-outcome-transformation.md` | Worked transformation |

## Scope & Limitations

**In Scope:** turning output-based feature lists into outcome-driven items, Now/Next/Later placement by quarter, "so what?" prompts by initiative type, and a structural check of outcomes and measures.

**Out of Scope:** feature prioritization or scoring (`execution/prioritization-frameworks/`), sprint-level planning or capacity allocation (`scrum-master/`), product strategy or vision definition (roadmaps communicate strategy, they don't create it), cross-team dependency management (`program-manager/`).

**Important Caveats:** outcome roadmaps require a cultural shift — teams used to date-driven lists need coaching on commitment levels; the tool checks outcome statements, it does not write them; Later items intentionally lack detailed metrics, and adding false precision undermines credibility.

## Integration Points

| Integration | Direction | Description |
|------------|-----------|-------------|
| `execution/brainstorm-okrs/` | Receives from | OKR key results become success metrics for Now/Next roadmap items |
| `execution/prioritization-frameworks/` | Receives from | RICE/ICE scores inform which initiatives move to Now vs. Next vs. Later |
| `execution/create-prd/` | Feeds into | Now items with validated outcomes become PRD candidates |
| `discovery/brainstorm-experiments/` | Receives from | Experiment results validate demand for Next/Later items, promoting them to Now |
| `senior-pm/` | Receives from | Portfolio strategic priorities influence roadmap horizon placement |
| `scrum-master/` | Receives from | Sprint capacity data determines how many Now items the team can support |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/outcome-roadmap-guide.md

# Outcome Roadmap Guide

A detailed reference for building outcome-driven roadmaps that communicate strategy, not just feature lists.

---

## Output vs Outcome Roadmap

### Side-by-Side Comparison

| Aspect | Output Roadmap | Outcome Roadmap |
|--------|---------------|-----------------|
| **Format** | Feature list with dates | Outcome statements with horizons |
| **Time horizon** | Q1, Q2, Q3, Q4 (fixed dates) | Now, Next, Later (commitment levels) |
| **Success measure** | "Did we ship it?" | "Did it produce the expected result?" |
| **Stakeholder question** | "When will feature X be done?" | "How are we progressing toward outcome Y?" |
| **Risk** | Dates slip, trust erodes | Outcomes are flexible; learning is valued |
| **Team alignment** | Aligned on deliverables | Aligned on impact |
| **Adaptability** | Change requires re-planning | Pivot the solution, keep the outcome |

### Why Outcomes Win

When a roadmap says "Build advanced search in Q2," the team ships advanced search in Q2. Success. But if customers do not use it, or it does not improve conversion, was it actually a success?

When a roadmap says "Enable customers to find products 50% faster," the team might build advanced search. Or they might improve navigation. Or they might add better categorization. The outcome is fixed; the solution is flexible. If advanced search does not work, the team can pivot without declaring failure.

---

## Outcome Statement Formula

```
Enable [customer segment] to [desired customer outcome] so that [business impact]
```

### Breaking It Down

**[Customer segment]:** Who specifically benefits? Be precise. "Users" is too broad. "New users in their first week" or "Enterprise admins managing 50+ seats" is specific enough to design for.

**[Desired customer outcome]:** What changes in the customer's experience? This should be something the customer would recognize and value. "Find products in under 5 seconds" -- a customer understands this. "Improved search indexing" -- a customer does not care about this.

**[Business impact]:** Why does the business care? Connect to a metric: revenue, retention, cost, market share, competitive position.

### Examples

| Output | Outcome |
|--------|---------|
| Build advanced search | Enable power users to find relevant products in under 5 seconds so that browse-to-purchase conversion increases by 20% |
| Launch mobile app | Enable field teams to access critical data on-site so that deal cycle time decreases by 30% |
| Add SSO integration | Enable enterprise IT admins to onboard teams in minutes instead of days so that enterprise deal close rate improves by 25% |
| Redesign dashboard | Enable managers to identify at-risk accounts in one glance so that proactive retention outreach increases by 40% |
| Migrate to new database | Enable the platform to handle 10x current load without degradation so that we can support enterprise-tier SLAs |

---

## The "So What?" Technique

The most powerful tool for finding outcomes. Start with the feature and keep asking "so what?" until you reach something a customer or executive would care about.

### Example 1

```
"Add CSV export"
  -> So what?
"Users can get their data out of the system"
  -> So what?
"They can share reports with stakeholders who don't have accounts"
  -> So what?
"Decision-makers see the data, which accelerates deal approvals"

Outcome: "Enable users to share insights with external stakeholders
          so that deal approval cycles shorten by 2 weeks"
```

### Example 2

```
"Implement caching layer"
  -> So what?
"Pages load faster"
  -> So what?
"Users experience less friction during peak hours"
  -> So what?
"Abandonment rate during high-traffic periods decreases"

Outcome: "Enable users to complete transactions without slowdowns during
          peak traffic so that peak-hour abandonment drops below 5%"
```

### When to Stop

Stop when you reach a statement that satisfies both:
1. A customer would nod and say "yes, that matters to me"
2. A business leader would say "yes, that moves a metric I care about"

If only one is satisfied, keep asking.

---

## Time Horizon Recommendations

### Now / Next / Later

This framework replaces calendar quarters with commitment levels.

**Now (0-6 weeks)**
- Team is actively working on this or will start within 2 weeks.
- Scope is defined. Solution is chosen. Dependencies are identified.
- Detail level: Full outcome statement, specific metrics, assigned team.
- Commitment: "We are doing this."

**Next (6 weeks - 3 months)**
- Direction is clear. Solution may still be flexible.
- The problem is validated, but the approach may change based on learnings from "Now" items.
- Detail level: Outcome statement with draft metrics. Team identified but not fully assigned.
- Commitment: "We intend to do this, subject to learning."

**Later (3-6 months)**
- Strategic opportunity or problem area identified.
- No solution chosen. May be reframed based on what we learn.
- Detail level: Problem statement or opportunity description. No solution details.
- Commitment: "We are thinking about this."

### Why Not Quarters?

Calendar quarters create two problems:

1. **False precision:** "Q3" implies a specific 3-month window. But 6 months out, you cannot predict scope, dependencies, or team availability with any reliability. The date becomes a promise you cannot keep.

2. **Rigidity:** When a Q2 item slips to Q3, the entire roadmap shifts. With Now/Next/Later, items move between horizons based on strategic priority, not calendar math.

---

## Success Metrics for Outcome Roadmaps

Every outcome needs 2-3 metrics that tell you whether the outcome was achieved.

### Metric Types

**Leading indicators:** Predict future success. Measurable quickly. Examples: sign-up rate, feature adoption in first week, NPS after onboarding.

**Lagging indicators:** Confirm actual impact. Take longer to materialize. Examples: revenue change, churn rate, market share.

**Counter-metrics:** Ensure you are not achieving the outcome at the expense of something else. Examples: if you increase sign-ups, track activation rate to make sure quality is not dropping.

### Metric Selection Checklist

- [ ] Is this metric directly influenced by the initiative?
- [ ] Can we measure it within the quarter?
- [ ] Do we have a reliable baseline (current value)?
- [ ] Would improving this metric genuinely indicate success?
- [ ] Is there a counter-metric to catch unintended consequences?

---

## Stakeholder Communication Strategies

### For Executives

Executives want to know: "Are we making progress toward our strategic goals?"

- Lead with outcomes, not features.
- Show metrics: baseline, target, current progress.
- Use Now/Next/Later to show strategic sequencing.
- Highlight dependencies and risks, not task-level status.

### For Sales Teams

Sales wants to know: "What can I tell customers is coming?"

- Share "Now" items as commitments. Be specific about what customers will experience.
- Share "Next" items as direction. Use language like "We are investing in [outcome area]."
- Do not share "Later" items. They change too frequently.

### For Engineering Teams

Engineers want to know: "What problem am I solving and how will I know I succeeded?"

- Lead with the outcome statement and success metrics.
- Share the "so what?" chain so engineers understand the full context.
- Let engineers propose solutions. The outcome is fixed; the approach is theirs.

### For Customers

Customers want to know: "Will this product keep solving my problems?"

- Share themes, not features. "We are investing in making collaboration faster" is better than "We are building real-time editing."
- Use outcome language: "You will be able to [desired outcome]."
- Never share dates unless you are confident. Missed dates destroy trust faster than vague timelines.

---

## Roadmap Review Cadence

| Activity | Frequency | Participants | Purpose |
|----------|-----------|-------------|---------|
| Outcome check-in | Weekly | Product + Engineering leads | Are "Now" items progressing toward metrics? |
| Horizon review | Monthly | Product team + stakeholders | Should anything move between Now/Next/Later? |
| Strategic review | Quarterly | Leadership + Product | Are our outcomes still aligned to company strategy? |
| Customer validation | Ongoing | Product + Customer-facing teams | Are our outcome assumptions correct? |

## references/outcome-roadmap-workflow.md

# Outcome Roadmap Workflow

> Read this when you are actually transforming a roadmap: the 6-step workflow with validation checkpoints, the "so what?" technique, the Now/Next/Later detail levels, a full worked example, why output roadmaps fail, the output structure, the tool flags, troubleshooting, and success criteria.

## Workflow

### 1. Gather Current Roadmap Items

The agent collects the existing roadmap -- features, projects, or initiatives -- in any format (list, spreadsheet, JSON, or prose).

**Validation checkpoint:** Each item must have at least a name and a brief description. If items are just feature names with no context, the agent asks for the problem each feature is meant to solve.

### 2. Transform Each Item

The agent applies the transformation formula:

```
"Enable [customer segment] to [desired customer outcome] so that [business impact]"
```

For each feature, the agent uses the "so what?" chain to find the real outcome:

```
"Build advanced search"
  -> So what? "Users can find products faster"
  -> So what? "They spend less time browsing and more time buying"
  -> So what? "Conversion rate increases, reducing acquisition cost per sale"
```

The last answer is the outcome. The agent works backward to write the outcome statement:

**Output:** "Enable power users to find relevant products in under 5 seconds so that conversion rates increase by 20%"

**Validation checkpoint:** Every transformed item must answer Who benefits, What changes for them, and Why it matters to the business.

### 3. Categorize into Now / Next / Later

| Horizon | Meaning | Commitment | Detail Level |
|---------|---------|-----------|--------------|
| **Now** | In progress or starting within 2 weeks | High -- team assigned, scope defined | Full outcome statements, success metrics, dependencies |
| **Next** | Planned for 1-3 months | Medium -- direction set, scope flexible | Outcome statements with draft metrics |
| **Later** | On the radar, 3-6 months | Low -- strategic intent only | Problem statements or opportunity areas |

**Validation checkpoint:** "Later" items should NOT have detailed metrics or specific solutions. Forcing detail on uncertain items creates false precision.

### 4. Add Success Metrics

For each Now and Next item, the agent defines 2-3 measurable indicators:

- **Primary metric:** Directly measures the desired outcome
- **Secondary metric:** Captures a different dimension of success
- **Counter-metric:** Prevents perverse optimization (optional for Next items)

### 5. Identify Dependencies

For each item, the agent documents:
- Technical prerequisites (APIs, infrastructure, data)
- Organizational prerequisites (team capacity, stakeholder buy-in)
- Market prerequisites (customer demand signal, competitive timing)

### 6. Review with Stakeholders

The agent produces a stakeholder-ready roadmap document for alignment review.

**Validation checkpoint:** Walk stakeholders through the outcome roadmap. If anyone asks "but when exactly will this ship?", redirect to commitment levels -- Now items have dates, Later items do not.

## Example: Roadmap Transformation

**Input (output-based roadmap):** "Build advanced search" (Q2), "Launch mobile app" (Q3),
"Add Slack integration" (Q3), "Redesign dashboard" (Q4).

**After the "so what?" pass (written by the PM; `roadmap_transformer.py` then checks it):**

```text

NOW (In Progress):
  Original: "Build advanced search"
  Outcome: "Enable power users to find relevant products in under 5 seconds
            so that conversion rates increase by 20%"
  Metrics:
    - Search-to-purchase conversion: 12% -> 15%
    - Avg search time: 18s -> 5s
    - Counter: Maintain search result relevance score above 0.8
  Dependencies: Elasticsearch cluster upgrade, product taxonomy cleanup

NEXT (1-3 Months):
  Original: "Launch mobile app"
  Outcome: "Enable field sales reps to close deals on-site so that
            average deal cycle shortens by 30%"
  Metrics:
    - Mobile-originated deals: 0% -> 15% of total
    - Avg deal close time: 14 days -> 10 days
  Dependencies: API v2 completion, mobile auth infrastructure

  Original: "Add Slack integration"
  Outcome: "Enable teams to act on alerts without context-switching
            so that mean response time drops by 40%"
  Metrics:
    - Alert-to-action time: 25min -> 15min
    - Alerts resolved in Slack: 0% -> 60%
  Dependencies: Webhook infrastructure, Slack app approval

LATER (3-6 Months):
  Original: "Redesign dashboard"
  Problem area: Users report dashboard is overwhelming and they
                can't find the metrics that matter to their role.
  Strategic intent: Role-based views that surface relevant data,
                    reducing time-to-insight.
  Dependencies: User research (not yet started)
```

## Why Output Roadmaps Fail

Output roadmaps create three problems:

1. **False precision** -- Dates promise certainty that does not exist. When dates slip, trust erodes.
2. **Misaligned teams** -- Engineers optimize for shipping features. Product optimizes for impact. An output roadmap makes these goals invisible to each other.
3. **Lost context** -- Six months later, nobody remembers why "advanced search" was important. The feature ships, but the problem it solved may have changed.

The outcome roadmap solves these by anchoring every item to customer value and business impact, with commitment levels that match certainty.

## Output Structure

For each initiative, the transformed roadmap includes:

1. **Original Initiative** -- What was on the old roadmap
2. **Outcome Statement** -- "Enable [segment] to [outcome] so that [impact]"
3. **Success Metrics** -- 2-3 measurable indicators
4. **Dependencies** -- Technical, organizational, or market prerequisites
5. **Strategic Context** -- Connection to company objectives or OKRs

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| All initiatives classified as "Later" | Quarter strings do not match expected format (e.g., "Q2 2026") or dates are far future | Verify `quarter` field uses "Q[1-4] YYYY" format; the tool uses current date to compute Now/Next/Later horizons |
| "So what?" chain produces vague outcomes | Team stopped the chain too early or did not reach business impact | Push through at least 3 "So what?" levels; the last answer should reference a business metric (revenue, retention, cost) |
| Stakeholders keep asking "when exactly will this ship?" | Commitment levels not communicated clearly, or stakeholders trained to expect dates | Redirect to Now/Next/Later commitment framework; Now items have dates, Next has direction, Later has intent only |
| Outcome statements all sound the same | Using the template formula mechanically without domain-specific context | Customize the "[customer segment]", "[desired outcome]", and "[business impact]" placeholders with real data |
| Roadmap has too many "Now" items | Team not making hard prioritization choices, or everything feels urgent | Enforce a cap: maximum 2-3 Now items at any time; use `prioritization-frameworks/` to rank competing priorities |
| Demo mode works but custom input fails | JSON schema mismatch: missing `initiatives` key or missing required fields per item | Each initiative needs `title`, `description`, `quarter`, and `type` (feature/improvement/infrastructure) |

## Success Criteria

- Every roadmap initiative has an outcome statement answering Who benefits, What changes, and Why it matters
- Now items have full outcome statements with 2-3 measurable success metrics and dependencies documented
- Next items have outcome statements with draft metrics (no counter-metrics required)
- Later items have problem statements and strategic intent only (no false-precision metrics or solutions)
- Stakeholders understand and accept the commitment level framework (Now = high, Next = medium, Later = low)
- Roadmap is reviewed quarterly with stakeholders to validate horizon placement
- Output-to-outcome transformation reduces "when will it ship?" questions by 50%+

## Tool Reference

### roadmap_transformer.py

Places initiatives in Now/Next/Later and checks each is outcome-ready. It does not write outcomes.

| Flag | Default | Description |
|------|---------|-------------|
| `--input` / `--demo` | one required | JSON file with `initiatives`, or the built-in output-style roadmap (exits 1) |
| `--as-of` | earliest quarter in the file | Current quarter, e.g. `Q4 2026`; pass it for a live roadmap |
| `--format` | `text` | `text`, `json` or `markdown` |
| `--output` | stdout | Write to a file |

Per initiative: `title`, `description`, `quarter` ("Q3 2026"), `type` (`feature`, `improvement`, `infrastructure`), plus `outcome`, `metric {name, baseline, target}` and `counter_metric`.

Errors: more than 3 Now items; Now/Next item with no outcome, an outcome that starts with an output verb, no metric, or a metric missing baseline or target; unparseable quarter. Warnings: no "so that", Now item without counter-metric, quarter before `--as-of`.

Exit codes: 0 no errors, 1 errors found, 2 bad input.

## references/red-flags.md

# Red Flags: Outcome Roadmap

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the transformed roadmap before sharing with stakeholders. Each red flag shows the *bad* version next to the *good* version, anchored to the Now/Next/Later commitment-level framework and the "so what?" technique.

---

## Red Flag 1: Outcome-themed but output-driven

**Symptom.** Each roadmap item has the "Enable [X] to [Y] so that [Z]" template at the top. Underneath is a feature list with dates. The team operates against the feature list; the outcome statement is decorative.

**Why it's bad.** The roadmap looks outcome-driven to executives but engineering treats it as a feature backlog with extra prose. The outcome statements add overhead without changing decisions. Worst, stakeholders think the team is outcome-driven when it isn't.

**Bad example:**
> "Now: 'Enable users to find products faster, so conversion improves.' Underneath: 'Ship advanced search by July 15. Ship filter dropdown by July 22. Ship saved searches by July 29.' Team meetings focus on the dates; conversion is never measured."

**Good example:**
> "Now: 'Enable power users to find relevant products in under 5 seconds, so conversion rate increases by 20%.'
> Success metrics: Search-to-purchase conversion 12% → 15%; avg search time 18s → 5s.
> Working hypothesis: ship Elasticsearch upgrade + relevance tuning (NOT a fixed feature list); measure conversion after 2 weeks; if not moving, change tactic.
> Standup question: 'are we moving conversion or just shipping features?'"

**How to catch it.** Read the team's standup notes. Do they reference the outcome metric or the feature names? If only the feature names, it's output dressed as outcome.

---

## Red Flag 2: Missing measurement

**Symptom.** Now items have outcome statements but no success metric ("Enable users to be productive" — measured how?).

**Why it's bad.** Without measurement, the outcome cannot be validated. The team ships the work and declares success based on what they did, not on what changed. The team learns nothing about whether the work actually delivered value.

**Bad example:**
> "Now: 'Enable customers to make better decisions, so they can grow their business.' (No measurable indicators.)"

**Good example:**
> "Now: 'Enable mid-market retailers to choose merchandise mixes that match their store traffic patterns, so they reduce overstock by 25%.'
> Primary metric: overstock value per store per month, from $42k to $32k.
> Secondary: % of stores using the new merchandising tool weekly, from 0% to 60%.
> Counter: stockout rate stays below 4% (don't trade overstock for stockout).
> Owner of the metric pull: BI team; reporting cadence: weekly."

**How to catch it.** For each Now item, does the success metric have a baseline and a target with a date? If no, measurement is missing.

---

## Red Flag 3: Now items > 3

**Symptom.** Now column lists 8 active initiatives.

**Why it's bad.** A team that has 8 "Now" items has 0 priorities. Now is supposed to be high-commitment, fully-scoped work — capped at what the team can ship in 6-8 weeks. 8 items means most are not real; they will not all ship; the column lies about commitment.

**Bad example:**
> "Now (Q3): 8 initiatives, each with team assignment. (Reality: 4 are starting; 3 are aspirational; 1 was bumped down from last quarter.)"

**Good example:**
> "Now (Q3, capped at 2-3): 'Improve mid-market activation' (active) and 'Reduce enterprise onboarding friction' (starting Aug 1). Others are Next. Cap enforced because activation experiments take 6-8 weeks each; more Now items means we're not really running any of them seriously."

**How to catch it.** Count Now items. > 3 = the commitment level is false.

---

## Red Flag 4: Later items with detailed scope

**Symptom.** Later column has full feature lists, mockups, P0/P1/P2 designations, dates.

**Why it's bad.** "Later" is strategic intent only. Adding precision to uncertain items creates false confidence. Stakeholders read the detail and commit emotionally to it; when reality forces a different choice, trust erodes ("you promised this!").

**Bad example:**
> "Later (Q1 2027): 'Mobile app redesign — 14 P0 features, mockups linked, ship date Mar 15, success metric DAU +25%, owner Sarah K, eng estimate 8 weeks.'"

**Good example:**
> "Later (3-6 months out, intentionally vague):
> 'Mobile experience deserves a refresh — current mobile NPS is 22 vs web 45, suggesting a gap. We are tracking 'mobile abandonment' as a leading indicator. In Q4 we'll decide whether to invest in mobile-app redesign or mobile-web optimization or both, based on the experiment in Q3.'
> (No mockups. No P0/P1. No dates. No success metric beyond directional intent.)"

**How to catch it.** Read Later items. Search for: dates, mockup links, P0/P1, specific feature counts. Each is false precision.

---

## Red Flag 5: "So what?" chain stopped too early

**Symptom.** Original initiative was "Build advanced search". After 1 "so what?", the team wrote: "users can find products faster". They wrote that as the outcome and moved on.

**Why it's bad.** "Find products faster" is still an activity-level outcome ("user does X faster"). The business outcome — what changes for the company — is 2-3 "so whats" further: conversion rate, revenue, retention. Stopping early produces user-experience-level outcomes that may not connect to business impact.

**Bad example:**
> "Original: 'Build advanced search.'
> So what? → 'Users find products faster.'
> Outcome: 'Enable users to find products faster.'"

**Good example:**
> "Original: 'Build advanced search.'
> So what? → 'Users find relevant products faster.'
> So what? → 'They spend less time browsing without buying.'
> So what? → 'Conversion rate increases, reducing acquisition cost per sale.'
> Outcome: 'Enable shoppers to find relevant products in <5 sec, so conversion rate increases from 12% to 15%.'"

**How to catch it.** Count "so what" iterations. If only 1, push 2-3 deeper to reach a business metric.

---

## Red Flag 6: All outcome statements sound the same

**Symptom.** "Enable users to be productive so the business grows." "Enable customers to use the product so revenue increases." "Enable teams to collaborate so they have better outcomes." Each item has the template applied mechanically.

**Why it's bad.** Generic outcome statements are worse than honest feature lists. They imply outcome thinking without doing the work. The team can't differentiate priorities; stakeholders can't tell what's important.

**Bad example:**
> "Now 1: 'Enable users to be more productive, so we grow revenue.'
> Now 2: 'Enable customers to succeed, so they retain better.'
> Now 3: 'Enable teams to collaborate, so they have better outcomes.'"

**Good example:**
> "Now 1: 'Enable mid-market sales leaders to cut pre-call research from 90 minutes to 10 minutes, so their reps spend 80% of their day in customer conversations instead of preparing for them.'
> Now 2: 'Enable enterprise admins to provision new users in under 2 minutes (currently 18 minutes), so their average time-to-first-team-value drops below 24 hours.'
> Now 3: 'Enable hybrid teams to see who is working on what without joining a sync meeting, so async teams stay aligned with 30% fewer meetings.'
> (Each outcome names specific segment, specific job, specific number.)"

**How to catch it.** Read 3 outcome statements aloud. If they could be swapped between items without anyone noticing, they are too generic.

---

## Red Flag 7: Stakeholders keep asking "when exactly?"

**Symptom.** Every roadmap review, the same question: "but when will [X] actually ship?" Team explains commitment levels; stakeholder is unsatisfied.

**Why it's bad.** Repeated date questions signal the commitment-level framework hasn't been internalized. Stakeholders may have been trained by years of date-driven roadmaps; switching to Now/Next/Later requires re-education they have not received.

**Bad example:**
> "Review meeting #4. Sales VP: 'I know it's "Next" but when will the API actually ship?' PM: 'commitment level is medium; we don't have a date.' Sales VP: 'I need a date for the customer.' [Repeat every quarter.]"

**Good example:**
> "Quarterly roadmap kickoff: 30-min education for stakeholders on the commitment-level framework. Slides cover: 'Now = high commitment, dates available'; 'Next = direction set, dates approximate'; 'Later = strategic intent, no dates'. Followed by Q&A. Sales VP receives a separate 'sales-ready commitments' artifact showing only Now items with firm dates plus Next items with date *windows* (e.g. 'Aug-Oct'). The wide-window dates are firm enough to commit to customers conservatively."

**How to catch it.** If the same date question recurs 3 reviews in a row, the framework hasn't been taught.

---

## Red Flag 8: Roadmap re-shuffled mid-quarter

**Symptom.** Now column on July 15 looks completely different from Now column on June 15. Items appear and disappear; no one tracks why.

**Why it's bad.** A roadmap that re-shuffles mid-quarter has no commitment level — Now is just "whatever we're working on this week". Teams cannot plan against it. Stakeholders cannot rely on it. The artifact becomes a vanity board.

**Bad example:**
> "June 1 Now: A, B, C. July 1 Now: A, D, E. (B and C silently moved; D and E appeared with no note.)"

**Good example:**
> "Now items locked for the quarter at kickoff. Mid-quarter changes require a documented decision: 'Removed item C on July 5 because user research invalidated the assumption; replaced with item D approved by VP Product.' Changelog at the bottom of the roadmap doc; reviewed at the monthly roadmap-review meeting."

**How to catch it.** Compare Now column at quarter start to mid-quarter. Each addition/removal should have a documented reason. Silent swaps = no commitment level.

---

## Red Flag 9: Roadmap as project plan

**Symptom.** Roadmap is a Gantt chart with engineer names, hours, weekly milestones. 27 dependencies marked.

**Why it's bad.** This is a project plan, not a roadmap. Roadmaps communicate strategy and outcomes to a broad audience. Project plans communicate scheduling to the working team. Conflating them produces a document too detailed for executives and too high-level for engineers.

**Bad example:**
> "'Outcome roadmap': 32-row Gantt chart with engineer assignments, hourly estimates, dependency arrows, daily milestones. Shown to the board."

**Good example:**
> "Outcome roadmap (strategic, for execs/customers/cross-functional): 3 Now / 4 Next / 5 Later items with outcomes and success metrics. No dates beyond month-level on Now items. No engineer names. No hourly estimates. The project plan / Gantt lives separately in the team's planning tool; it is the execution detail. The roadmap is the strategic abstraction."

**How to catch it.** Open the roadmap. Does it have engineer names? Hourly estimates? Daily milestones? Each is project-plan content polluting the roadmap.

---

## Red Flag 10: No connection to the NSM or OKRs

**Symptom.** Roadmap items have outcomes. NSM and OKRs exist separately. No mapping between them.

**Why it's bad.** Outcomes that don't ladder to the company's NSM and the team's OKRs are local optimizations. The team can hit every roadmap outcome and still not move the strategic levers. Roadmap-OKR alignment is what makes the work add up.

**Bad example:**
> "Roadmap Now item: 'Enable users to find products faster, so conversion rate improves.' Q3 OKR: 'Reduce churn from 4% to 2.5%.' (No connection. Conversion-rate improvement doesn't move churn.)"

**Good example:**
> "Roadmap Now item: 'Enable repeat shoppers to find products faster, so weekly repeat-visit conversion rate improves from 8% to 12%.'
> Strategic linkage: NSM is 'weekly active engaged accounts'; this initiative moves the 'repeat visit conversion' input which combines with WAU to produce WAEA. Q3 OKR KR2 is 'WAEA from 28k to 40k' — this initiative is expected to contribute ~30% of that lift."

**How to catch it.** For each Now item, ask: "which OKR KR does this serve?" If the team can't answer, the roadmap is locally optimized.

---

## Red Flag 11: Dependencies hidden

**Symptom.** Now item "Enable [X]" lists no dependencies. Engineering reveals at week 4 that it depends on a Platform team migration that hasn't been planned.

**Why it's bad.** Hidden dependencies are roadmap timebombs. They surface late, cause slips, and embarrass the team in stakeholder reviews. The roadmap promised an outcome but cannot deliver because the team did not surface the prerequisites.

**Bad example:**
> "Now: 'Enable customers to share dashboards externally.' (Dependencies field: blank.) (Week 4: PM realizes this requires the auth team's external-sharing infrastructure, which is not on Platform's roadmap.)"

**Good example:**
> "Now: 'Enable customers to share dashboards externally.'
> Dependencies:
> • Technical: external-auth service from Platform team (DEP-014, needed by Aug 1, expected Jul 28).
> • Organizational: Legal review of GDPR data-sharing implications.
> • Market: SOC 2 certification of the sharing surface (current; verified May).
> Each dependency tracked in `dependency-map/` and visible in the cross-team weekly sync."

**How to catch it.** For each Now/Next item, are technical + organizational + market dependencies documented? If blank, surface them.

---

## Red Flag 12: Roadmap reviewed only at quarter boundaries

**Symptom.** Roadmap published April 1. Next review June 28. In between, the team works against it but never updates it.

**Why it's bad.** Roadmaps drift in 90 days. Items complete (or fail); new information emerges; assumptions get validated or invalidated. A roadmap reviewed only at quarter boundaries is an autopsy, not a steering instrument.

**Bad example:**
> "Q3 roadmap published Jul 1. Next review: Sep 28. Mid-quarter: 2 Now items completed (not removed); 1 invalidated by user research (still listed); 3 new opportunities surfaced (not added)."

**Good example:**
> "Roadmap reviewed monthly (3 times per quarter):
> Month 1: focus on Now item progress; mid-flight decisions.
> Month 2: confirm Next items as Q3 progresses; promote/demote based on data.
> Month 3: shape next quarter's Now; confirm strategic Later items still relevant.
> Quarterly: full re-baseline with stakeholders."

**How to catch it.** Compare the published roadmap to actual team work. If the roadmap shows items the team isn't working on, or omits items they are working on, the artifact is stale.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Outcome-themed but output-driven | Do standups reference outcome metric or feature names? |
| 2 | Missing measurement | Does each Now item have baseline + target + date? |
| 3 | Now items > 3 | Count Now items |
| 4 | Later items with detailed scope | Are dates/mockups/P0 lists on Later items? |
| 5 | "So what?" stopped too early | Count "so what" iterations: < 2? |
| 6 | All outcomes sound the same | Could you swap two outcomes without anyone noticing? |
| 7 | Stakeholders keep asking "when?" | Has the commitment-level framework been taught? |
| 8 | Roadmap reshuffled mid-quarter | Is there a changelog for additions/removals? |
| 9 | Roadmap as project plan | Engineer names? Hourly estimates? Daily milestones? |
| 10 | No NSM/OKR linkage | Which KR does this item serve? |
| 11 | Dependencies hidden | Are technical + organizational deps documented? |
| 12 | Reviewed only at quarter boundaries | When was the roadmap last updated? |

## Related Reading

- SKILL.md Troubleshooting
- references/outcome-roadmap-guide.md
- `brainstorm-okrs/` (OKRs anchor Now items)
- `north-star-metric/` (initiatives target input metrics)
- `prioritization-frameworks/` (RICE/ICE inform Now vs Next vs Later)
- `dependency-map/` (cross-team dependencies on roadmap items)
- `create-prd/` (Now items become PRD candidates)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/outcome-roadmap
