# create-prd

> **Use these instructions for this whole conversation.** Apply them when: Write an 8-section product requirements document, framing the problem before the solution. Use when specifying a new product or a large feature that needs engineering, design and business aligned on one document.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# PRD Scaffolding Expert

## Overview

Structured product requirements document creation using a proven 8-section framework. This skill produces clear, jargon-free PRDs that communicate what to build, why it matters, and how success is measured. Every PRD generated follows a consistent structure that keeps engineering, design, and business stakeholders aligned.

## Core Capabilities

- **Pre-PRD framing** — Problem Framing Canvas (user-perspective narrative) and Working Backwards Press Release sharpen the problem before solutions.
- **8-section PRD framework** — Summary, Contacts, Background, Objective (SMART KRs), Market Segments (JTBD), Value Proposition (Value Curve), Solution (P0/P1/P2), Release.
- **Plain-language discipline** — one idea per sentence, specificity over abstraction, 10-second executive test.
- **Optional scaffolder** — `prd_scaffolder.py` prints the empty skeleton; the framework and problem framing do the work.

## When to Use

- **New Product Initiative** -- Starting a product from scratch and need a comprehensive spec before development begins.
- **Feature Expansion** -- Adding significant functionality to an existing product that requires cross-team alignment.
- **Stakeholder Alignment** -- Need a single document that answers "what are we building and why?" for everyone involved.

## Clarify First

Before generating the PRD, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Core problem:** one sentence in the user's words; who hurts and how (drives Background + Objective).
- **Target reader:** exec, engineering, or mixed (sets altitude and which of the 8 sections matter most).
- **Success metric:** the SMART KR that defines "it worked" (drives Objective).
- **Scope boundary:** what is explicitly NOT in this release (drives Solution P0/P1/P2 + Release).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Gather context: product name, target segment, core problem (Clarify First).
2. Frame the problem before any solution, with the Problem Framing Canvas or a Working Backwards press release (`references/prd-framework.md`). This is where most of the PRD's value comes from.
3. Write the 8 sections from `assets/prd_template.md`. Every KR needs a baseline and a target; every P0 item traces back to a stated pain.
4. **Verify** [RECOMMENDED] against the checklist in `references/prd-writing-guide.md`: an exec gets the Summary in 10 seconds, nothing in Solution lacks a problem above it, and the scope boundary is explicit. Then share for feedback.

Optional: the scaffolder prints the empty 8-section skeleton with your name, objective and segments filled in. Writing straight from the template is equally fine.

```bash
python3 scripts/prd_scaffolder.py --product-name "SearchBoost" \
  --objective "Help shoppers find the right product in under a minute" \
  --segments "Power users, New customers"   # add --output PRD.md to write a file
```

**Exit codes:** 0 skeleton written; 2 missing or empty arguments, or an unwritable `--output` path.

## Prototype-First Path

AI app builders, AI design tools, and AI coding assistants make a clickable or working prototype cheaper than a long spec for some work. Use the prototype to learn; keep the PRD to decide.

**Build a prototype first (or alongside the spec) when:**
- The core risk is usability or desirability ("will they understand / want this?"), not feasibility or policy.
- The interaction is hard to describe in prose (new workflow, dense UI, conversational flow).
- Stakeholders are debating opinions that a 20-minute user session would settle.

**Write the spec first when:** the risk is regulatory, data, security, pricing, or cross-team dependency; or the change is a well-understood extension of an existing flow.

**Testing the prototype with users:**
1. Write the hypothesis and pass threshold before the session (see `discovery/brainstorm-experiments/`).
2. Run 5-8 task-based sessions with the target segment; observe, don't demo.
3. Use realistic but synthetic data — never paste customer PII into third-party prototyping tools without approval.
4. Log what users did (task success, errors, time) separately from what they said.

**The PRD still must contain:** the problem and who has it (Background), success metrics (Objective KRs), constraints (technical, legal, budget, timeline), explicit non-goals, and risks/open questions. Link the prototype and the test findings in Section 7 (Solution) — the prototype illustrates the solution, it does not replace the requirements.

**Handoff to engineering:** label the prototype as throwaway or as a starting point, and say which. Generated prototype code is not production code by default — list what it skips (auth, error states, accessibility, performance, security review, data model) so engineering scopes the real build. Hand over the prototype link, the tested flows, the findings, and the P0/P1/P2 scope together.

## Anti-Patterns

### Writing the solution before the problem
**Mistake:** The PRD opens with features, mockups and a P0 list, while Background and Market Segments get one line each.
**Why it happens:** The team arrives with a solution in mind, and the solution is the part people enjoy writing.
**Instead:** Write Section 3 (Background) and Section 5 (Market Segments) first. Then test Section 7 alone: if a reader can't tell what problem it solves, the problem sections are still too thin.

### Key results without baselines
**Mistake:** "Increase activation by 30%", with no current value, no target value and no date.
**Why it happens:** The baseline needs a data pull, and the PRD is due before anyone runs it.
**Instead:** Write every key result as "[metric] from [baseline] to [target] by [date]". If the baseline is unknown, measuring it is the first task, not a gap to leave in the document.

### Assumptions with no validation plan
**Mistake:** An Assumptions list with four bullets, none with an owner or a test.
**Why it happens:** Writing assumptions down feels like managing the risk.
**Instead:** For each assumption, name who tests it, by when and how. Run the load-bearing ones through `discovery/identify-assumptions` before build starts.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

- `references/prd-framework.md` — read this while writing: the two pre-PRD techniques, full 8-section framework with per-section guidance, writing principles, scaffolder flag reference, troubleshooting, and success criteria.
- `references/prd-writing-guide.md` — read this when polishing a draft: section-by-section writing guide and the review checklist.
- `references/red-flags.md` — read this before sharing the PRD: common ways PRDs go wrong with bad/good examples and fixes.
## Files

| File | Purpose |
|---|---|
| `scripts/prd_scaffolder.py` | Optional skeleton generator |
| `assets/prd_template.md` | Complete PRD template |
| `examples/shared-dashboards-prd.md` | Worked PRD |

## Scope & Limitations

**In Scope:** 8-section PRD skeleton generation with guided placeholders; section-by-section writing guidance (plain-language, specificity); market-segment definition by jobs-to-be-done; value-proposition mapping with Value Curve; release planning with Now/Next/Later and explicit deferral.

**Out of Scope:** Technical architecture or system design docs (`engineering/`); user story writing and backlog creation (`execution/job-stories/`, `execution/wwas/`); detailed UX research or usability testing plans (`product-team/`); financial business-case modeling (`finance/`).

**Important Caveats:** A PRD is a communication tool, not a contract — treat it as a living document. The 8-section framework is proven, but lightweight agile teams may need only sections 1, 3, 4, 7, 8, while regulated contexts may need more. Unclear or missing requirements are a well-documented source of rework, so review the PRD with engineering and design before build starts.

## Integration Points

| Integration | Direction | Description |
|------------|-----------|-------------|
| `discovery/identify-assumptions/` | Receives from | Validated and "Test Now" assumptions populate PRD Section 7 with evidence |
| `discovery/brainstorm-experiments/` | Receives from | Experiment results validate or invalidate PRD assumptions |
| `discovery/pre-mortem/` | Receives from | Tiger mitigations become PRD risk sections |
| `execution/brainstorm-okrs/` | Feeds into | PRD Key Results (Section 4) align with quarterly OKR targets |
| `execution/outcome-roadmap/` | Feeds into | PRD release plan (Section 8) maps to roadmap Now/Next/Later horizons |
| `execution/prioritization-frameworks/` | Receives from | Feature priority (P0/P1/P2) in Section 7 informed by RICE/ICE scoring |
| `senior-pm/` | Feeds into | PRD stakeholder context feeds stakeholder mapper engagement plans |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/prd-framework.md

# PRD Framework & Pre-PRD Techniques

Read this when writing the PRD itself: the two pre-PRD framing techniques, the full 8-section framework with per-section guidance, writing principles, the scaffolder flag reference, troubleshooting, and success criteria.

---

## Pre-PRD Techniques

Before writing the PRD, use one or both of these techniques to sharpen the problem definition and align the team on value.

### Technique A: Problem Framing Canvas

Frame the problem from the user's perspective before jumping to solutions. This canvas produces the narrative that feeds directly into PRD Sections 3 (Background) and 5 (Market Segments).

```markdown
## Problem Framing Canvas

### Problem Framing Narrative

**I am**: [Describe the key persona experiencing the problem]
- [Key characteristic 1]
- [Key characteristic 2]
- [Key characteristic 3]

**Trying to**: [A single sentence listing the desired outcomes]

**But**:
- [Barrier preventing outcomes 1]
- [Barrier 2]
- [Barrier 3]

**Because**: [Root cause explanation in empathetic language]

**Which makes me feel**: [Emotional impact from persona perspective]

### Context & Constraints
- [Geographic, technological, time-based, organizational constraints]

### Final Problem Statement
- [Single concise, empathetic summary for stakeholder alignment]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
```

**Next steps:** Generate testable solution hypotheses, convert into a workshop facilitation guide, or create stakeholder-specific variants (Exec, Eng, Design).

### Technique B: Working Backwards Press Release

Write an Amazon-style "future press release" announcing the product as if it already shipped. This forces you to articulate customer value before implementation.

```markdown
## Working Backwards Press Release

"[Product Name] by [Company] Aims to [Main Purpose/Goal]"

"[City], [Date] --"

"Today, [Company], a [type of organization], announced [product/feature],
a [brief description]. This [product] is set to [main benefit], addressing
[key issue or need]."

"[Product] will [what it does/solves]. [Quote from key person]:
'[customer-outcome-focused quote].' This initiative reflects [Company]'s
commitment to [core value]."

"In addition to [mentioned features], [product] also [additional benefits].
According to [source], [relevant data supporting the news]."

**Media Contact:** [Name, Title, Email]
```

**Writing rules:**
- Focus on customer outcomes, not feature lists.
- Avoid hype; favor credible claims and concrete benefits.
- If you can't write a compelling PR, the product concept needs more work.

**Next steps:** Generate an FAQ, create stakeholder-specific variants, generate objection-handling talking points, or define launch success metrics.

---

## PRD Framework (8 Sections)

### Section 1: Summary

Write 2-3 sentences that a busy executive can read in 10 seconds and understand the full scope. Answer three questions: What is this? Who is it for? Why are we doing it now?

Do not use marketing language. State the product, the user, and the expected outcome plainly.

### Section 2: Contacts

A table of people involved in the decision:

| Name | Role | Responsibility |
|------|------|----------------|
| ... | Product Manager | Final decision on scope |
| ... | Engineering Lead | Technical feasibility |
| ... | Design Lead | UX direction |
| ... | Stakeholder | Business approval |

Keep this short. Only list people who will actively contribute or approve.

### Section 3: Background

Answer three questions:

1. **Context** -- What is the current state? What exists today?
2. **Why now?** -- What changed in the market, technology, or business that makes this urgent?
3. **What recently became possible?** -- New capabilities, partnerships, data, or insights that enable this initiative.

This section sets the stage. A reader who skips every other section should still understand the motivation after reading Background.

### Section 4: Objective

State the business benefit and the customer benefit separately:

- **Business benefit**: How does this move a business metric? (revenue, retention, cost reduction, market share)
- **Customer benefit**: How does this improve the user's life? (time saved, friction removed, new capability)

Then define 2-4 SMART Key Results in OKR format:

- **Objective**: [qualitative, inspirational statement]
- **KR1**: [metric] from [current] to [target] by [date]
- **KR2**: [metric] from [current] to [target] by [date]
- **KR3**: [metric] from [current] to [target] by [date]

### Section 5: Market Segment(s)

Define segments by the problems they face or jobs they need done -- not by demographics. A segment is a group of people who share a common struggle or desired outcome.

Format: "[Segment name]: People who need to [job/problem] because [context]."

Bad: "Millennials aged 25-35 in urban areas"
Good: "Time-constrained professionals who need to coordinate schedules across 3+ tools because their organization lacks a unified calendar system"

### Section 6: Value Proposition(s)

For each market segment, define:

1. **Jobs addressed** -- What tasks or goals does this product help accomplish?
2. **Gains created** -- What positive outcomes does the user experience?
3. **Pains relieved** -- What frustrations, risks, or obstacles are removed?
4. **Competitive advantage** -- Why is our approach better than existing alternatives?

Use the **Value Curve** framework to visualize where you compete, where you exceed, and where you deliberately underinvest relative to alternatives.

### Section 7: Solution

Break into subsections:

- **UX / Prototypes** -- Key screens, flows, or interaction patterns. Link to design files.
- **Key Features** -- Numbered list of features with one-sentence descriptions. Mark each as P0 (must-have), P1 (important), or P2 (nice-to-have).
- **Technology** (optional) -- Architecture decisions, integrations, or infrastructure requirements that constrain the solution.
- **Assumptions** -- Explicit list of things you believe to be true but have not validated. Each assumption should have a plan to validate it.

### Section 8: Release

- **Relative timeline** -- Use T-shirt sizes (S/M/L/XL) or Now/Next/Later rather than specific dates, unless dates are firm.
- **v1 scope** -- What ships in the first version? Draw a clear line.
- **Future versions** -- What is explicitly deferred? List it so stakeholders know it was considered but intentionally excluded.
- **Success criteria** -- When do we know v1 succeeded? Reference the Key Results from Section 4.

## Writing Principles

- **Plain language** -- No jargon, no acronyms without definition, no buzzwords.
- **One idea per sentence** -- If a sentence has "and" connecting two distinct ideas, split it.
- **Specificity over abstraction** -- "Reduce onboarding from 12 steps to 4" beats "Simplify onboarding."
- **Saved as**: `PRD-[product-name].md`

## Tool Reference: prd_scaffolder.py

Generates a complete 8-section PRD markdown skeleton with guided placeholders, market segment sections, and value proposition templates.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--product-name` | string | (required) | Name of the product (used in title and headers) |
| `--objective` | string | (required) | Short description of the product objective (1-2 sentences) |
| `--segments` | string | (required) | Comma-separated list of market segments |
| `--output` | string | stdout | Output file path; if omitted, prints to stdout |

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| PRD scaffolder output is too generic | Only product name provided; objective and segments need specificity | Write a 1-2 sentence objective that states the outcome, not just the product category; define segments by jobs-to-be-done, not demographics |
| Stakeholders skip reading the PRD | Document too long, too jargon-heavy, or lacks a clear Summary section | Ensure Section 1 (Summary) answers What/Who/Why in 3 sentences; cut any section beyond 1 page that is not Section 7 |
| Engineering team builds the wrong thing | PRD focuses on solution before establishing problem context | Strengthen Section 3 (Background) and Section 5 (Market Segments); ensure problem definition precedes solution |
| PRD assumptions never validated | Assumptions listed in Section 7 but no validation plan assigned | Add a validation plan column to the Assumptions table; link each assumption to `identify-assumptions/` or `brainstorm-experiments/` |
| Scope creep after PRD approval | Section 8 (Release) does not clearly separate v1 from future versions | Be explicit about "Explicitly Deferred" items; ensure every stakeholder has seen and acknowledged the deferred list |
| PRD becomes stale during development | Treated as a static document rather than a living reference | Update after implementation decisions change; archive final state and link to retrospective notes |
| `--segments` flag parsing fails | Segments not properly comma-separated or contain special characters | Wrap the segments argument in quotes: `--segments "Segment A, Segment B"` |

## Success Criteria

- PRD passes the "10-second executive test" -- a busy executive understands scope from Section 1 alone
- All 8 sections are complete before development begins (no placeholder sections remain)
- Market segments defined by jobs-to-be-done, not demographics
- Key Results in Section 4 are measurable with baselines, targets, and deadlines
- Every assumption in Section 7 has a validation plan and owner
- PRD reviewed by PM, Engineering Lead, Design Lead, and at least one stakeholder before commitment
- v1 scope in Section 8 draws a clear line between what ships and what is explicitly deferred

## references/prd-writing-guide.md

# PRD Writing Guide

A section-by-section guide for writing effective product requirements documents.

---

## Section 1: Summary

### What Makes a Good Summary

- **Length:** 2-3 sentences maximum. If it takes longer, the scope is too large or you do not understand it yet.
- **Structure:** What it is + who it is for + why now.
- **Test:** Can someone who knows nothing about your company read this and understand what you are building?

### Good Example

"TaskFlow is a task management tool for distributed engineering teams that need async collaboration across time zones. It replaces manual standup updates with automated progress tracking. We are building this now because remote-first work has made synchronous updates impractical for 70% of our customer base."

### Bad Example

"TaskFlow is a next-generation, AI-powered productivity platform that leverages cutting-edge technology to synergize cross-functional workflows and empower teams to achieve unprecedented efficiency gains."

The bad example uses jargon, makes vague claims, and does not tell you what the product actually does.

---

## Section 2: Contacts

### Tips

- Only list people who will actively contribute decisions or approvals.
- Include their specific responsibility, not just their job title.
- Keep it under 6 people. If more are involved, the project may be too large for one PRD.

---

## Section 3: Background

### Three Questions to Answer

1. **Context:** Describe the current state as if explaining to a new team member. What exists? What do users do today?
2. **Why now?** Something changed. Name it specifically: competitor launched X, customer churn increased Y%, new API became available, board set a new strategic direction.
3. **What recently became possible?** This is the most overlooked question. It separates "we should do this eventually" from "we can and should do this now."

### Anti-Patterns

- Restating the objective as background ("We need to build this because it is important")
- Including solution details in the background section
- Writing more than one page

---

## Section 4: Objective

### Good Objectives vs Bad Objectives

| Good | Bad |
|------|-----|
| Reduce customer onboarding time from 3 days to 4 hours | Improve onboarding |
| Increase monthly active users from 10K to 25K | Grow our user base |
| Reduce support tickets per user from 2.1/month to 0.8/month | Improve product quality |

**Pattern:** Good objectives include a specific metric, current value, target value, and timeframe.

### Writing Key Results

- Each KR must have a number attached to it.
- KRs measure outcomes, not outputs. "Launch feature X" is an output. "Reduce time-to-task from 5 min to 2 min" is an outcome.
- Aim for 60-70% confidence that you can hit the target. If you are 100% confident, the target is too easy.

---

## Section 5: Market Segments

### Definition Tips

Define segments by shared problems or jobs-to-be-done, not demographics.

**Why:** Demographics describe who people are. Jobs describe what people need. Two people with identical demographics may have completely different needs. Two people with different demographics may share the exact same problem.

### Format

"[Segment name]: People who need to [job/problem] because [context]."

### Examples

- "Overwhelmed managers: People who need to track progress across 5+ direct reports because their organization lacks standardized reporting."
- "Solo founders: People who need to validate product-market fit quickly because they have limited runway and no dedicated research team."

---

## Section 6: Value Proposition

### Frameworks

**Jobs-Gains-Pains:**
- **Jobs:** Functional tasks, social goals, or emotional needs the user is trying to satisfy.
- **Gains:** Outcomes the user wants. Benefits they expect, desire, or would be surprised by.
- **Pains:** Risks, obstacles, and negative outcomes the user wants to avoid.

**Value Curve:**
Plot your product against alternatives on key factors. Identify where you invest heavily (differentiation), where you match (table stakes), and where you deliberately underinvest (strategic tradeoff).

The value curve prevents "me too" products by forcing explicit tradeoff decisions.

---

## Section 7: Solution

### Feature Prioritization

- **P0 (Must-have):** Product does not ship without this. Users cannot accomplish the core job.
- **P1 (Important):** Significantly improves the experience. Ship in v1 if possible, v1.1 at latest.
- **P2 (Nice-to-have):** Adds polish or secondary value. Defer without guilt.

### Assumptions

Every PRD contains assumptions. The dangerous ones are the ones you do not write down. List them explicitly with a plan to validate each one.

Common assumption categories:
- User behavior assumptions ("Users will adopt this workflow")
- Technical assumptions ("The API can handle this load")
- Market assumptions ("Competitors will not ship this first")
- Business assumptions ("This will reduce churn")

---

## Section 8: Release

### Timeline Tips

- Use relative sizing (S/M/L/XL) or Now/Next/Later unless you have firm dates.
- Specific dates create false precision. Stakeholders treat "Q2 2026" as a promise.
- Be explicit about what is NOT in v1. Deferred items show stakeholders their request was heard but intentionally sequenced.

---

## PRD Review Checklist

Use this before sharing the PRD with stakeholders:

### Clarity
- [ ] Can someone outside the team understand the Summary in 10 seconds?
- [ ] Is every acronym defined on first use?
- [ ] Are there zero instances of jargon ("leverage," "synergy," "paradigm")?

### Completeness
- [ ] All 8 sections are filled in (not just placeholder text)?
- [ ] At least 2 Key Results with metrics, baselines, and targets?
- [ ] At least 1 market segment defined by problem, not demographics?
- [ ] At least 3 assumptions listed with validation plans?

### Specificity
- [ ] Objective includes a measurable metric?
- [ ] Features have priority labels (P0/P1/P2)?
- [ ] v1 scope has a clear boundary (what is in and what is out)?
- [ ] Success criteria reference specific Key Results?

### Consistency
- [ ] Summary aligns with Objective aligns with Key Results?
- [ ] Market segments match the value propositions?
- [ ] Features map to at least one value proposition?
- [ ] Deferred items do not contradict v1 scope?

---

## Common PRD Anti-Patterns

1. **The Novel** -- PRD is 20+ pages. Nobody reads it. Solution: If it is longer than 6 pages, split into multiple PRDs.
2. **The Wishlist** -- Everything is P0. Solution: Force-rank. Only 3-5 features can be P0.
3. **The Solution Looking for a Problem** -- Starts with the feature, not the customer need. Solution: Write Sections 3-5 before Section 7.
4. **The Vague Objective** -- "Improve the user experience." Solution: Attach a number.
5. **The Missing Audience** -- Written for engineers but shared with executives (or vice versa). Solution: Summary for execs, Details for engineers, same document.
6. **The Immortal PRD** -- Never updated after initial writing. Solution: Set a review cadence (biweekly during active development).
7. **The Assumption-Free Zone** -- No assumptions listed, as if the team knows everything. Solution: List at least 3 things you believe but have not proven.

## references/red-flags.md

# Red Flags: Create PRD

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan a draft PRD before sending to stakeholders. Each red flag shows the *bad* version next to the *good* version, anchored to the 8-section structure (Summary / Contacts / Background / Objective / Market Segments / Value Prop / Solution / Release).

---

## Red Flag 1: Solution before problem

**Symptom.** The PRD opens with Section 7 (Solution) energy — feature lists, mockups, P0/P1/P2 — before the problem in Sections 3 (Background) and 5 (Market Segments) is established.

**Why it's bad.** A reader who lands on Solution first has no way to evaluate it. They cannot tell whether the features address the actual problem or whether the team has fallen in love with an implementation. Engineering builds the wrong thing.

**Bad example:**
> "Section 1 Summary: 'We will ship an AI-powered chatbot, a new dashboard, push notifications, and a Slack integration.' (Sections 3 and 5 left thin: 'Background: many customers complain about onboarding.' 'Segments: SMB and enterprise.')"

**Good example:**
> "Section 1: 'Time-constrained sales leaders lose 90 minutes per opportunity researching prospects before calls. We are reducing that to 10 minutes with auto-research.' Section 3: 'Until now this was solved by SDRs spending their day on research. New LLM capabilities make context-window-sized research feasible in seconds. Customer interviews (n=22) show this is the #2 reason quota is missed.' Section 5: 'B2B sales leaders at companies with 50-500 reps who run multiple weekly opportunity-review calls.' Section 7: 'The auto-research panel surfaces top 3 talking points from a 15-source aggregation.'"

**How to catch it.** Read Section 7 alone. Could a reader tell what problem it solves? If no, Sections 3 and 5 are too thin.

---

## Red Flag 2: Section 7 (Solution) bloat

**Symptom.** Section 7 is 8 pages long. P0 list has 24 items. Mockup references multiply.

**Why it's bad.** A PRD is not a spec. Bloated Solution sections crowd out the Why; reviewers skim; v1 scope becomes "all of it"; the release plan in Section 8 becomes incoherent because there is nothing left to cut.

**Bad example:**
> "Section 7 Solution: 8 pages, 24 P0 features, 18 P1 features, 12 P2 features, 6 nested UX subsections, references to 14 Figma files."

**Good example:**
> "Section 7 Solution: 1.5 pages. 'UX: 3 key screens (link to single Figma). Key Features: 4 P0 (numbered list, one sentence each), 2 P1, 1 P2 deferred. Tech: 2 architecture notes. Assumptions: 3 numbered with validation plan.' Section 8: 'v1 ships the 4 P0; everything else explicitly deferred to v1.1 or later.'"

**How to catch it.** Count pages in Section 7. > 3 pages on a feature-sized PRD is a flag.

---

## Red Flag 3: Market segments by demographics

**Symptom.** Section 5 says "Millennials aged 25-35 in urban areas" or "Mid-market companies in tech".

**Why it's bad.** Demographic segments are not actionable. Two 30-year-olds in San Francisco can have completely different jobs-to-be-done. Designing for demographics produces feature ambiguity. JTBD-based segments produce specific design choices.

**Bad example:**
> "Section 5 Market Segments: Segment 1: Millennials aged 25-35 in urban areas. Segment 2: Mid-market companies in tech."

**Good example:**
> "Section 5 Market Segments: Segment 1: 'Sales leaders who run 5+ pipeline-review calls per week and prepare for them between meetings, because their team's win rate depends on the quality of pre-meeting talking points.' Segment 2: 'New sales reps in their first 90 days who do not yet know the buyer journey deeply, because they need a research scaffolding to compensate for missing domain knowledge.'"

**How to catch it.** Read Section 5. If a segment includes age, geography, or industry without a "because" clause naming the job, rewrite.

---

## Red Flag 4: Section 4 KRs without baselines

**Symptom.** Key Results read "Increase activation by 30%" — no current value, no target value, no date.

**Why it's bad.** Without a baseline, "30%" is meaningless. The team will measure 30% of *something* and call it done. With no target value and date, success is a moving target.

**Bad example:**
> "KR1: Increase activation significantly.
> KR2: Drive enterprise growth.
> KR3: Improve customer satisfaction."

**Good example:**
> "KR1: D7 activation rate from 32% (Apr 2026 baseline) to 52% by Q3 end.
> KR2: Enterprise MRR from $1.2M to $2.4M by Q3 end.
> KR3 (counter): NPS stays above 42 (current 45)."

**How to catch it.** Each KR should follow the pattern "[metric] from [baseline] to [target] by [date]". Anything else is incomplete.

---

## Red Flag 5: Assumptions listed without validation plans

**Symptom.** Section 7 has an Assumptions sub-list with 4 bullets. None has an owner or a validation method.

**Why it's bad.** Listing assumptions without validating them is theater. The team writes them down and then ignores them. Production reveals that the load-bearing assumption was wrong; the project is 80% built; everyone is surprised.

**Bad example:**
> "Assumptions:
> 1. Users will accept research summaries from LLM
> 2. CRM API supports the data we need
> 3. Sales managers have time to review research before calls"

**Good example:**
> "Assumptions (each with owner + validation plan):
> 1. 'Users will accept LLM-summarized research' — owner: PM. Test: 5-user concept test by 2026-05-30. See `discovery/identify-assumptions/`.
> 2. 'CRM API supports the fields we need' — owner: Eng Lead. Test: API smoke test by 2026-05-25.
> 3. 'Sales managers have 5 min before calls to review' — owner: PM. Test: time-diary study (n=10) by 2026-06-05."

**How to catch it.** For each assumption, ask "who is testing this, by when, how?" Missing answer = unvalidated assumption.

---

## Red Flag 6: PRD reads like marketing copy

**Symptom.** Words like "seamless", "revolutionary", "transformative", "world-class" appear in Sections 1, 3, or 6.

**Why it's bad.** Marketing language hides specificity. A reviewer reading "seamless onboarding" cannot evaluate whether the team has thought through edge cases. A reviewer reading "reduces onboarding from 12 steps to 4 steps" can.

**Bad example:**
> "Section 1 Summary: 'A revolutionary, AI-powered, seamless onboarding experience that transforms how new users discover our world-class product.'"

**Good example:**
> "Section 1 Summary: 'New users currently complete 12 onboarding steps in a median of 9 minutes; 41% bail before step 7. We are cutting the flow to 4 steps targeting < 3 minutes median, by deferring 8 setup decisions to in-app contextual prompts after first value.'"

**How to catch it.** Search the PRD for: seamless, revolutionary, transformative, world-class, cutting-edge, next-generation. Replace each with specific facts.

---

## Red Flag 7: Section 8 (Release) without explicit deferral list

**Symptom.** Section 8 says "v1 ships in Q3" but does not list what is *not* in v1.

**Why it's bad.** Scope creep is the default outcome. Without an explicit deferral list, every stakeholder assumes their favorite feature is in v1. The team commits to a too-large scope; ship slips; trust erodes.

**Bad example:**
> "Section 8 Release: 'v1 targets Q3 launch. Future versions will add additional capabilities.'"

**Good example:**
> "Section 8 Release: 'v1 (Now, ships Aug 2026): 4 P0 features [list]. Explicitly deferred to v1.1 (Next, Q4 2026): mobile push, Slack integration, custom dashboards [list with rationale]. Explicitly deferred to v2 (Later, Q1 2027 or later): white-label, API marketplace [list]. Success criteria: D7 activation hits 52% (KR1) on a 30-day rolling cohort.'"

**How to catch it.** Search Section 8 for "deferred" or "explicitly not". If missing, scope is undefined.

---

## Red Flag 8: Contacts section padded

**Symptom.** Section 2 lists 14 names — exec sponsor, 3 PMs, 2 designers, 4 engineers, 2 marketing, legal, finance, "miscellaneous stakeholders".

**Why it's bad.** A 14-person contact table dilutes accountability. Nobody is sure who decides. The PRD becomes consensus-by-committee. Decisions drag.

**Bad example:**
> "Section 2: PM, Sr PM, Group PM, Eng Manager, Eng Lead, Sr Eng (2), Designer, Sr Designer, PMM, Marketing Manager, Legal Counsel, Finance Partner, Exec Sponsor."

**Good example:**
> "Section 2 (5 people): PM (Sarah K) — final decision on scope. Eng Lead (Tomas R) — technical feasibility. Design Lead (Amy L) — UX direction. PMM (Jorge M) — positioning + GTM. Exec Sponsor (VP Product, David T) — business approval. Other reviewers are listed in the project Slack but do not appear here."

**How to catch it.** Count names in Section 2. > 6 is a flag.

---

## Red Flag 9: Stale PRD treated as authoritative

**Symptom.** PRD was written Feb 2026. Engineering started building in March. It's now May. The PRD has not been updated; assumptions in Section 7 have all been validated/invalidated, but the doc still reads as if they're open.

**Why it's bad.** A PRD is a communication tool, not a contract. Stale PRDs misinform new joiners and stakeholders. They become reference artifacts that nobody trusts but everybody cites.

**Bad example:**
> "PRD last updated Feb 14. (Reality: 60% of assumptions have been validated; the architecture pivoted from monolith to event-driven; v1 scope changed.) PRD remains the doc people reference."

**Good example:**
> "PRD has a 'Changelog' at the top: 'v1.4 (May 18): assumption 1 validated via concept test; assumption 2 invalidated, scope reduced. v1.3 (Apr 5): architecture pivot — see ADR-014. v1.2 (Mar 12): KR3 target adjusted from NPS 50 to NPS 45 after baseline correction.' Each milestone review updates the doc."

**How to catch it.** Check the last-modified date. If the PRD has not been touched in > 30 days and the project is mid-build, it is stale.

---

## Red Flag 10: Value Proposition reads like internal wishlist

**Symptom.** Section 6 lists "gains" like "users will love the new interface" or "more revenue".

**Why it's bad.** Vague gains do not test against customer reality. Real value propositions name a specific job, a measurable gain, and a specific pain relieved. Without specificity, the team has no way to know if v1 delivered the value prop.

**Bad example:**
> "Section 6 Value Proposition: 'Jobs addressed: better workflow. Gains: time saved. Pains relieved: frustration. Competitive advantage: better UX.'"

**Good example:**
> "Section 6 Value Proposition for Segment 1 (sales leaders):
> Jobs: prepare for pipeline review in <10 min; coach SDR talking points using the same research.
> Gains: 80 minutes/week saved per leader; shared research artifact for the team.
> Pains relieved: skipping prep when calendar is back-to-back; reps showing up unprepared.
> Competitive advantage: integrated into existing CRM with no second tool to open; alternatives (manual + Gong + Notion) require 3 tabs."

**How to catch it.** Could the team measure each gain in 90 days? If no, the value prop is too vague.

---

## Red Flag 11: Background dodges "why now"

**Symptom.** Section 3 lists context ("customers complain about X") but never says what changed to make this feature feasible or urgent *now*.

**Why it's bad.** "Why now" is the question every exec sponsor asks. Without it, the PRD looks opportunistic — a feature the team wanted to build, dressed in a customer story. Sponsors withhold funding because they cannot tell strategic urgency from desk-driven enthusiasm.

**Bad example:**
> "Section 3 Background: 'For years, customers have asked for better search. The current search is slow and limited. We should improve it.'"

**Good example:**
> "Section 3 Background: (Context) Search is the #2 in-app event by volume; current p95 latency is 4.2s. (Why now) Three things changed in 2026: (1) Elasticsearch 9 reduces our latency floor to 800ms at our scale. (2) Two competitor releases have raised buyer expectations — our last 3 lost deals cited search. (3) Internal data pull (Apr 2026) shows search-abandon correlates 0.61 with churn. (What recently became possible) The new ES cluster lands in May; engineering capacity opens after the migration."

**How to catch it.** Read Section 3. Find the phrase "Why now". If absent, the urgency is unstated.

---

## Red Flag 12: "10-second executive test" fails

**Symptom.** Sponsor reads Section 1 (Summary) and cannot answer: "What is this? Who is it for? Why now?"

**Why it's bad.** Section 1 is the entire PRD compressed. If a busy exec cannot leave that section knowing the answer, the rest of the document will not save them. Funding decisions are made on Section 1.

**Bad example:**
> "Section 1 Summary: 'This PRD describes our plans for the upcoming quarter, focused on improvements to our product. We will be building several features across multiple workstreams, with the goal of increasing customer satisfaction and growth.'"

**Good example:**
> "Section 1 Summary: 'Auto-research panel for B2B sales leaders. Cuts pre-call research from 90 to 10 minutes per opportunity. Targeting sales leaders at 50-500-rep companies; ships Aug 2026. Built now because LLM context-window pricing dropped 4x in Q1 and our top-3 lost deals all named research time as a coaching gap.'"

**How to catch it.** Time a stakeholder reading Section 1. Ask them the three questions. If they hesitate, rewrite.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Solution before problem | Could a reader of Section 7 alone tell what problem it solves? |
| 2 | Section 7 bloat | Is Section 7 > 3 pages? |
| 3 | Segments by demographics | Does each segment include a "because [job]" clause? |
| 4 | KRs without baselines | Does each KR follow "[metric] from X to Y by date"? |
| 5 | Assumptions without validation plans | For each assumption: who, by when, how? |
| 6 | Marketing-copy adjectives | Search for: seamless, revolutionary, world-class. |
| 7 | Section 8 without deferral list | Does it list what is explicitly NOT in v1? |
| 8 | Padded Contacts section | > 6 names? |
| 9 | Stale PRD | Last updated > 30 days ago and project mid-build? |
| 10 | Value Prop reads as wishlist | Can each gain be measured in 90 days? |
| 11 | Background dodges "why now" | Does Section 3 explicitly say "why now"? |
| 12 | 10-second executive test fails | Can a reader answer What / Who / Why now from Section 1? |

## Related Reading

- SKILL.md Troubleshooting
- references/prd-writing-guide.md
- `prfaq/` (Working Backwards PR as a pre-PRD discipline)
- `discovery/identify-assumptions/` (for the validation plans in Section 7)
- `brainstorm-okrs/` (KRs in Section 4)
- `outcome-roadmap/` (Section 8 Now/Next/Later horizons)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/create-prd
