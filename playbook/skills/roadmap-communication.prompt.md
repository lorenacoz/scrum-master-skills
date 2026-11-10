---
description: "Produce executive, customer and internal versions of one roadmap with consistent framing and the right detail and risk language for each. Use when publishing the quarterly roadmap, a board packet or a customer or sales roadmap."
---

# Roadmap Communication Expert

## Overview

A single roadmap cannot serve every audience. Executives need confidence and strategic framing. Customers need plausible promises with credible timelines. Internal teams need detail, dependency awareness, and honest risk. When PMs publish one roadmap to all three, one audience is always wrong -- either the executives are bored, customers feel misled, or engineers feel managed.

This skill produces three variants of the same underlying roadmap, each tailored to its audience. The underlying source of truth -- the roadmap data -- stays single; the framing, level of detail, risk language, and visualization all change. The variants share names and identifiers so a customer reference can be traced back through the internal variant to the actual ticket. The structural backbone is **Now / Next / Later** (Janna Bastow, ProdPad), which Marty Cagan calls "right-sizing the roadmap" -- forecast confidence decreases with time horizon, so commit explicitly to "Now," name "Next" by theme, and keep "Later" deliberately fuzzy.

## Core Capabilities

- **Three audience variants** — executive (outcome-led, confidence-rated, 1 page), customer (theme-led, benefit-framed, no firm dates), and internal (feature-led with owners, dependencies, and explicit risk).
- **Now / Next / Later right-sizing** — encode the confidence gradient and calibrate it per audience.
- **Outcome-vs-feature framing** — translate features into customer outcomes for the executive and customer variants.
- **Triangulation check** — trace one Now item across all three variants to guarantee consistent identity and framing.

## When to Use

- **Quarterly roadmap publication** -- the regular cadence where you communicate to multiple audiences.
- **Pre-board meeting** -- the executive variant feeds the board packet.
- **Annual customer conference** -- the customer variant becomes the conference roadmap session.
- **Engineering kickoff** -- the internal variant grounds sprint planning across multiple teams.
- **Sales enablement** -- the customer variant feeds sales reps' "what's coming" pitch.

### When NOT to Use

- For a single-team backlog with one stakeholder (one roadmap suffices).
- For tactical sprint planning (use `../scrum-master/` outputs).
- For incident communication or in-flight project status (use `status-update-generator/`).

## Clarify First

Before generating the variants, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Target audience(s):** executive, customer, internal, or all three (each is a distinct variant with different detail, framing, and risk language).
- **The roadmap source of truth:** Now/Next/Later items with owners and dates (the internal variant is authored first; exec/customer derive from it).
- **Date-commitment policy:** what you can promise customers publicly (the customer variant strips firm dates; the exec variant gets confidence ratings instead).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Author the internal variant first** — it is the source of truth (owners, dates, dependencies, risks). Use `assets/internal_roadmap_template.md`.
2. **Derive the executive variant** — promote each Now item to its parent outcome, add confidence ratings, cap at 1 page. Use `assets/executive_roadmap_template.md`.
3. **Derive the customer variant** — translate features to benefits, strip dates beyond the current quarter, use "exploring / in development / shipping soon." Use `assets/customer_roadmap_template.md`.
4. **Run the triangulation check** [RECOMMENDED] — trace one Now item across all three; the framings must be consistent. Re-publish on a fixed cadence.

**Done when** the same item reads consistently in all three, the customer variant carries no dates past the current quarter and no internal risks, and the internal variant shows the bad news the other two soften.

## Anti-Patterns

### Now / Next / Later with no themes
**Mistake:** Each column is a flat list of features with no organizing theme.
**Why it happens:** Features are what teams track day to day, and themes take a strategy decision to name.
**Instead:** Group every item under a theme, such as Activation or Enterprise readiness, in all three variants. If you can't name the themes, settle the strategy before publishing the roadmap.

### A wishlist presented as a roadmap
**Mistake:** Sales and Success add every customer request, and the roadmap grows past 60 items.
**Why it happens:** Adding a request to the roadmap is an easy way to say yes to a customer.
**Instead:** Put only prioritized, validated bets on the roadmap. Keep requests in a separate insights inbox that feeds discovery, and let only the PM move items onto the roadmap. More than 20 items per quarter means the roadmap has become a wishlist.

### An internal variant that hides bad news
**Mistake:** The internal roadmap shows every initiative as on track, while standups know two are weeks behind.
**Why it happens:** Red status feels like a career risk, and the PM hopes to recover before anyone looks.
**Instead:** Give the internal variant a red/yellow/green status column that initiative leads update weekly, with a mitigation plan for each red item. More than 95% green for more than 2 weeks means the status column is not being used honestly.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/roadmap-variants-playbook.md](references/roadmap-variants-playbook.md)** — the variant comparison tables, the "right-size the roadmap" principle, outcome-vs-feature framing, the detailed structure for each of the three variants, the authoring workflow, troubleshooting, and success criteria. Read when building or reviewing the variants.
- **[references/roadmap-communication-guide.md](references/roadmap-communication-guide.md)** — the origin of Now/Next/Later (Bastow), Cagan's right-size principle, the outcome-vs-feature debate (Cagan, Torres), and worked examples of all three variants for the same project. Read for theory and full examples.
- **[references/red-flags.md](references/red-flags.md)** — common ways roadmap artifacts go wrong, each with bad/good examples. Read before publishing any variant.

## Files

| File | Purpose |
|---|---|
| `assets/internal_roadmap_template.md` | Internal variant, the source of truth |
| `assets/executive_roadmap_template.md` | Executive variant |
| `assets/customer_roadmap_template.md` | Customer variant |
| `examples/pylon-roadmap-three-ways.md` | One roadmap in all three variants |

## Scope & Limitations

**In Scope:**
- Three roadmap variants (executive, customer, internal) from a shared underlying spec
- Now / Next / Later horizon structure with audience-appropriate detail
- Outcome-based framing for executive and customer variants
- Detailed feature/dependency/risk framing for internal variant
- Triangulation check ensuring consistency across variants
- Templates for each variant

**Out of Scope:**
- Backlog prioritization (use `prioritization-frameworks/`)
- OKR drafting (use `brainstorm-okrs/`)
- NSM definition (use `north-star-metric/`)
- Outcome-roadmap transformation (use `outcome-roadmap/`)
- Sprint planning (use `../scrum-master/`)
- Marketing launch copy (handoff to marketing skills)
- Detailed dependency graphs (use `dependency-map/`)

**Important Caveats:**
- Three variants triple the maintenance load. Teams without the discipline to keep them aligned will be better off publishing only the internal variant and disclaiming everything else. The three-variant pattern is for teams that can sustain quarterly re-publication.
- The customer variant is a public commitment. Treat updates as carefully as you treat a launch. Surprise changes erode trust.
- The internal variant must remain non-public. Sales reps must be trained to quote the customer variant only.
- Outcome-based roadmaps require an NSM and OKRs to function. Without those, "outcomes" are unmeasurable aspirations.

## Integration Points

| Integration | Direction | Description |
|-------------|-----------|-------------|
| `execution/outcome-roadmap/` | Receives from | Outcome decomposition feeds the executive variant |
| `execution/north-star-metric/` | Receives from | NSM and inputs are the executive variant's metrics |
| `execution/brainstorm-okrs/` | Receives from | KRs map to internal roadmap items |
| `execution/create-prd/` | Receives from | Each Now-quarter feature in the internal variant links to its PRD |
| `execution/prfaq/` | Receives from | PR/FAQ summaries become the seed of customer variant theme descriptions |
| `execution/prioritization-frameworks/` | Receives from | Prioritization scores determine which items make Now / Next / Later |
| `execution/dependency-map/` | Pairs with | Internal-variant dependencies are sourced from the dependency map |
| `execution/status-update-generator/` | Feeds into | Weekly status updates reference roadmap variant deltas |
| `../senior-pm/` | Feeds into | Portfolio roll-ups aggregate executive variants across teams |
| `marketing/` (skills domain) | Hands off to | Customer variant feeds product marketing content calendars and launch comms |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/red-flags.md

# Red Flags: Roadmap Communication

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every roadmap artifact (exec deck, customer-facing roadmap, internal Confluence page) before publishing. Each red flag has bad and good quoted examples.

---

## Red Flag 1: One Roadmap for All Audiences

**Symptom.** The same Gantt chart is shown to the board, to customers, and to engineering.
**Why it's bad.** Each audience has different stakes. The board wants outcomes and confidence levels. Customers want themes and approximate sequencing. Engineering wants dependencies and acceptance criteria. A single artifact fails all three -- it is too detailed for the board and too vague for engineering.
**Bad example:**
> "Q2 Roadmap (single Confluence page, shown to board on Monday, customer advisory on Tuesday, engineering all-hands on Wednesday): 47 line items with dates, owners, and ticket links."
**Good example:**
> "Three views derived from the same source roadmap:
> - **Board view**: 5 strategic bets, each with a confidence level and an outcome metric.
> - **Customer view**: 4 themes with quarterly buckets (Now / Next / Later), no dates.
> - **Engineering view**: 47 initiatives with dependencies, owners, target sprints."
**How to catch it.** Reusing the exact same artifact for two different audiences = generate audience-specific views from one source.

---

## Red Flag 2: Dates Promised as Commitments

**Symptom.** Customer roadmap lists "Feature X: April 2026". Customer reads this as a contract and procurement schedules around it.
**Why it's bad.** A roadmap is an artifact of intent, not a contract. Dates communicated as commitments destroy the team's ability to learn and re-prioritize. The PM either becomes a slave to the date (shipping a worse version) or burns customer trust by missing it.
**Bad example:**
> "Customer roadmap:
> - Bulk-edit: March 15, 2026
> - SCIM: April 30, 2026
> - SOC 2 audit report: May 31, 2026"
**Good example:**
> "Customer roadmap (Now / Next / Later):
> - **Now** (Q2 2026, high confidence): bulk-edit, SOC 2 audit report.
> - **Next** (Q3 2026, medium confidence): SCIM provisioning.
> - **Later** (H2 2026, low confidence): SAML SP-initiated flows.
> Dates above are planning approximations and may shift as we learn. Contractual commitments live in your MSA, not here."
**How to catch it.** Any customer-facing roadmap with calendar dates = replace with Now / Next / Later buckets.

---

## Red Flag 3: Now / Next / Later With No Themes

**Symptom.** Roadmap is a flat list of features in Now / Next / Later, no organizing theme.
**Why it's bad.** Without themes, customers cannot extrapolate where the product is heading. They see features but not direction. Sales cannot pitch the strategic story. Internal teams optimize for feature delivery, not the larger outcome.
**Bad example:**
> "Now: bulk-edit, dark mode, SOC 2.
> Next: SCIM, audit log, OAuth.
> Later: SAML, FedRAMP, advanced roles."
**Good example:**
> "Now -- *Activation*: bulk-edit, dark mode, onboarding redesign.
> Now -- *Enterprise readiness*: SOC 2, audit log.
> Next -- *Activation*: in-product templates.
> Next -- *Enterprise readiness*: SCIM, OAuth.
> Later -- *Enterprise readiness*: SAML, FedRAMP."
**How to catch it.** Roadmap items not bucketed under a theme = add themes; if no themes exist, you do not have a strategy.

---

## Red Flag 4: Roadmap = Feature List (Outputs, Not Outcomes)

**Symptom.** Every item is a feature name; nothing describes the customer outcome.
**Why it's bad.** Output roadmaps lock the team into specific solutions before validation. When a feature does not move the metric, the team ships it anyway because it is on the roadmap. The roadmap becomes an obstacle to learning.
**Bad example:**
> "Q2 roadmap: bulk-edit, dark mode, SCIM."
**Good example:**
> "Q2 roadmap (outcome -> bets):
> - *Outcome*: reduce time-to-second-action from 7 min to 3 min. *Bets*: bulk-edit, in-product templates.
> - *Outcome*: unblock 4 enterprise deals stuck on compliance. *Bets*: SOC 2, audit log, SCIM.
> Bets are revisable as we learn."
**How to catch it.** Outcome column absent = use `outcome-roadmap` skill to transform.

---

## Red Flag 5: Confidence Levels Missing

**Symptom.** Roadmap items appear with equal visual weight, regardless of whether they are a researched bet or a wild guess.
**Why it's bad.** All bets are not equal. Stakeholders need to know which items have high evidence behind them and which are speculative. Without confidence levels, the board treats Later-bucket guesses as plans, and the PM gets pinned to ideas that should still be exploratory.
**Bad example:**
> "Q3 roadmap: SCIM, marketplace, AI agent. (All listed identically.)"
**Good example:**
> "Q3 roadmap:
> - SCIM (Confidence: HIGH; 4 design partners committed)
> - Marketplace (Confidence: MEDIUM; opportunity solution tree validates demand; build approach unvalidated)
> - AI agent (Confidence: LOW; hypothesis only; 2-week spike in Q2 to assess)"
**How to catch it.** No confidence column = add one. Anything without evidence = LOW.

---

## Red Flag 6: Roadmap Updated Annually

**Symptom.** Roadmap published in January, never revised, presented at year-end with most items either shipped late or never shipped.
**Why it's bad.** A roadmap that does not revise loses signal value -- everyone learns to ignore it. Worse, customers anchor on the original version and feel betrayed when reality diverges.
**Bad example:**
> "Roadmap v1, January 2026. (Last edit: January 2026.)"
**Good example:**
> "Roadmap reviewed monthly in the leadership sync, revised quarterly with explicit changelog. Customers subscribed via Productboard get a monthly digest of changes ('Moved SAML from Q3 -> Q4 because the design partner pulled; added in-app templates to Q2 based on Q1 NSM data')."
**How to catch it.** Last-edit timestamp older than 6 weeks on a customer-facing roadmap = update or pull down.

---

## Red Flag 7: Wishlist Items Treated as Roadmap

**Symptom.** Sales team adds features to the roadmap whenever a customer asks. The roadmap balloons to 60+ items.
**Why it's bad.** Roadmaps need to be selective to be useful. Adding everything anyone has requested produces an unfilterable list that customers cannot act on and engineering cannot deliver. The roadmap becomes a wishlist.
**Bad example:**
> "Q2 / Q3 / Q4 roadmap (60+ items added by sales, success, and product over the year): every feature a customer has ever asked for."
**Good example:**
> "Roadmap shows only validated bets that survived prioritization (RICE-scored, top quartile). Unvalidated requests live in Productboard's insights inbox and feed into discovery, not the roadmap. Sales / Success can see the inbox; only the PM moves items onto the roadmap."
**How to catch it.** Roadmap item count > 20 per quarter = the roadmap is a wishlist; separate it from the inbox.

---

## Red Flag 8: No Visualization for the Customer View

**Symptom.** Customer-facing roadmap is a wall of bullet points.
**Why it's bad.** Customers and executives are visual. A wall of bullets is harder to scan, retain, and reference than a swimlane / Kanban / GO product roadmap visual. Adoption (the audience actually opening the roadmap) drops.
**Bad example:**
> "[5 pages of nested bullets]"
**Good example:**
> "Customer roadmap: a single-page Now / Next / Later board with theme swimlanes and color-coded confidence levels, drawn as a Mermaid diagram. Bullet detail lives in the appendix for those who want it."
**How to catch it.** Customer-facing roadmap with no visual = generate one.

---

## Red Flag 9: Promising Roadmap Items in Contracts

**Symptom.** A sales contract MSA lists 3 roadmap features as "to be delivered by Q3 2026".
**Why it's bad.** Roadmap items are intent, not commitments. Embedding them in contracts creates legal liability for things that should remain revisable. The PM loses agency to learn and re-prioritize.
**Bad example:**
> "MSA Schedule A: 'Vendor will deliver SCIM, audit log, and SAML by Q3 2026.'"
**Good example:**
> "MSA Schedule A names a *delivery commitment* (SOC 2 audit report by June 30 -- a deliverable, not a feature) and a *roadmap notification* clause ('Vendor will give 60 days' notice of material changes to the roadmap shared in CRM/Productboard'). Features are not promised in MSAs."
**How to catch it.** Pull sales contracts; search for roadmap feature names. Any presence = escalate to legal + sales-ops.

---

## Red Flag 10: Internal Roadmap That Hides Bad News

**Symptom.** Internal roadmap is "all green", but everyone in the team knows two initiatives are deeply in trouble.
**Why it's bad.** Hidden bad news compounds. By the time leadership finds out (usually from a missed launch), it is too late to redirect. Teams learn that the roadmap is a marketing document, not a coordination tool, and stop trusting it.
**Bad example:**
> "Internal roadmap shows all 7 initiatives 'on track'. In team standups, two are 4 weeks behind."
**Good example:**
> "Internal roadmap has a red/yellow/green status column updated weekly by initiative lead. Two initiatives currently red, with a documented mitigation plan (descope to MVP for one; pull in engineer from another initiative for the second). Leadership reviews changes weekly."
**How to catch it.** Internal roadmap shows > 95% green for > 2 weeks = the status column is theater. See `status-update-generator/references/red-flags.md` Red Flag 1.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | One roadmap for all audiences | Are there audience-specific views? |
| 2 | Dates promised as commitments | Customer view uses Now / Next / Later? |
| 3 | No themes | Items bucketed under strategic themes? |
| 4 | Outputs, not outcomes | Outcome column present? |
| 5 | No confidence levels | Each item has H / M / L confidence? |
| 6 | Annual updates | Last edit < 6 weeks ago? |
| 7 | Wishlist treated as roadmap | Item count per quarter < 20? |
| 8 | No visual for customer view | Customer roadmap has a visualization? |
| 9 | Roadmap items in contracts | MSAs reference deliverables, not features? |
| 10 | Internal roadmap hides bad news | > 95% green for weeks = theater |

## Related Reading

- `SKILL.md` -- the 3-audience pattern
- `references/audience-patterns.md` -- exec / customer / internal variants
- Sibling skill: `execution/outcome-roadmap/` -- output -> outcome transformation
- Sibling skill: `execution/status-update-generator/` -- the weekly status that feeds the internal roadmap
- Sibling skill: `productboard-expert/` -- the insights inbox that feeds discovery
- Sibling skill: `execution/quarterly-planning/` -- the planning cycle the roadmap reflects

## references/roadmap-communication-guide.md

# Roadmap Communication Guide

A reference on roadmap framing across audiences. Covers the origin of Now/Next/Later, Marty Cagan's "right-size the roadmap" principle, the outcome-vs-feature debate (Cagan, Torres), and worked examples of all three variants for the same project.

---

## Part 1: The Now / Next / Later structure

Janna Bastow (co-founder of ProdPad) introduced the **Now / Next / Later** framework in 2014 as an antidote to Gantt-style roadmaps that promised features 12 months out and then disappointed. The structure is simple:

- **Now (in flight or starting imminently)** -- specific commitments, dates, high confidence
- **Next (next 1-2 quarters)** -- themes, not features; medium confidence
- **Later (beyond)** -- directions and bets; low confidence by design

It worked because it made the **confidence gradient explicit**. A team can commit to "Now" with conviction; "Next" is a working hypothesis; "Later" is a north star. Audiences understand the gradient because the structure encodes it.

### Why the alternatives fail

| Format | Why it fails |
|--------|--------------|
| Gantt by feature | Implies commitments at every date the bar crosses; teams cannot honor 9-month feature commitments |
| Quarter columns ("Q1 / Q2 / Q3 / Q4 features") | Same problem; teams over-promise far quarters to look complete |
| Backlog as roadmap | Backlog is prioritization, not commitment; cannot be shared upstream |
| One-pager "we will do these 30 things this year" | Confidence-blind; treats year-out items as equivalent to next-week items |

---

## Part 2: Cagan's "right-size the roadmap"

Marty Cagan argues that the right format for a roadmap depends on **how confident the team can be** at each horizon. His rule of thumb:

| Horizon | Confidence | Right level of commitment |
|---------|------------|---------------------------|
| 2-4 weeks | High (>80%) | Specific feature with date |
| 1 quarter | Medium-high (~70%) | Specific feature with target sprint |
| 2 quarters | Medium (~50%) | Theme, not feature |
| 1 year | Low (<30%) | Direction or bet |
| Multi-year | Very low | Vision statement only |

Roadmap formats that ignore this gradient (committing to specific features 12 months out) trade short-term clarity for long-term credibility loss. Customers learn that roadmap items at the right end of the timeline are decorative.

---

## Part 3: Outcome vs feature roadmaps

A second axis: what is the unit of work on the roadmap -- a customer outcome (something the user achieves) or a feature (something the team builds)?

### The outcome case (Cagan, Torres)

Marty Cagan and Teresa Torres (Continuous Discovery Habits) argue that outcomes are the only durable roadmap unit:

- An outcome ("reduce onboarding from 14 days to 3 days") survives scope changes
- A feature ("ship guided onboarding wizard") binds you to a specific solution
- If the wizard solution fails, the outcome is still the goal
- Outcomes can be measured; features can only be delivered

### The feature case (pragmatic)

Outcomes work well at the executive and customer variant level, but engineering execution requires features. A team cannot estimate "reduce onboarding from 14 days to 3 days" -- they can estimate "build the wizard" or "build verification step bypass." The internal roadmap therefore tracks features, with each feature mapped to its parent outcome.

### The reconciliation

| Variant | Default orientation |
|---------|---------------------|
| Executive | Outcomes |
| Customer | Themes (outcomes), with Now items occasionally named as features |
| Internal | Features, each mapped to an outcome and a KR |

This matches the audience: executives plan for outcomes, customers buy outcomes, engineers ship features.

---

## Part 4: Confidence ratings on roadmaps

The executive variant should include confidence ratings per Now-quarter item. The standard scale:

| Rating | Definition | When to use |
|--------|------------|-------------|
| **High** | >=80% chance to deliver on time, on scope | In flight, on schedule, no major risks |
| **Medium** | 50-80% chance | One or two known risks with credible mitigations |
| **Low** | <50% chance | Material risks; dependency on external party; or recent slip |

Ratings are honest, not optimistic. A Medium rating tells the executive "watch this." A Low rating tells the executive "ask me about it." A team that publishes 5 of 5 High ratings every quarter is either coasting or lying.

---

## Part 5: The triangulation check

Before publishing, perform a triangulation check on one item per variant:

1. Pick an item from the Now bucket
2. Find its representation in the internal variant (e.g., "Feature: SAML SSO with Okta + Azure AD")
3. Find its representation in the executive variant (e.g., "Outcome: Enterprise customers can log in via their identity provider; supports $2M expansion target")
4. Find its representation in the customer variant (e.g., "Theme: Single sign-on for enterprise. Available this quarter.")

If all three are recognizably the same thing, the variants are aligned. If a customer reading variant 3 could not predict the internal feature in variant 1, the customer variant is misleading or the internal is incomplete. Adjust.

---

## Part 6: Worked example -- same roadmap, three variants

### Source of truth: internal variant (excerpt)

| Feature | PM | EM | Status | Target | KR mapped | Dependencies | Risks |
|---------|----|----|--------|--------|-----------|--------------|-------|
| SAML SSO with Okta and Azure AD | Jane Doe | Sara Lee | In flight | Sprint 24 (2026-06-12) | KR2 (Enterprise activation rate) | Identity provider documentation | Vendor cert renewal in window |
| SCIM user provisioning | Jane Doe | Sara Lee | Sprint 25 | 2026-06-26 | KR2 | SSO must ship first | Spec ambiguity |
| Audit log export (CSV) | Jane Doe | Tom Kim | In flight | Sprint 24 | KR3 (Enterprise retention) | None | Storage cost spike |
| Search latency optimization | Liam Wu | Tom Kim | Sprint 24 | 2026-06-12 | KR1 (latency p95 <250ms) | Index rebuild | Rollout window contention |

### Executive variant (1 page)

```markdown
# Acme Platform -- Q2 2026 Roadmap

**Strategy:** Win enterprise mid-market by removing top-3 procurement objections.
**Sponsor:** VP Product

## Now (Q2 2026)

| Outcome | Metric | Confidence | Lead PM |
|---------|--------|------------|---------|
| Enterprise customers can log in via their identity provider | KR2: Enterprise activation rate 38% -> 55% | High | Jane Doe |
| Admins can pull audit data for compliance | KR3: Enterprise retention 91% -> 94% | High | Jane Doe |
| Search performance no longer cited as objection | KR1: p95 latency 480ms -> 250ms | High | Liam Wu |

## Next (Q3 2026)

- Automated user provisioning for enterprise admins (Medium confidence)
- Self-serve enterprise contract upgrade (Medium)
- Multi-region data residency (Medium)

## Later (H2 2026)

- AI-assisted search relevance ranking
- Cross-product data unification

## Not this period

- Mobile app parity work (sequenced for 2027)
- Workflow automation themes (in discovery, not committed)
```

### Customer variant (themed cards)

```markdown
# What's Coming in 2026

> This roadmap is directional and may change as we learn from customers.
> Items in "Exploring" are not commitments. Dates may shift.

## Shipping this quarter

**Single sign-on for enterprise**
Log in with your company identity provider. Supports SAML 2.0 with major providers.

**Audit log export**
Export account audit data for compliance reviews.

**Faster search**
Search responses significantly faster for large workspaces.

## In development -- later this year

**Automated team provisioning**
Sync user accounts from your identity provider so admins do not manage them manually.

**Self-serve enterprise upgrades**
Upgrade to enterprise tier directly in product, without sales involvement for standard plans.

**Multi-region data residency**
Choose where your data is stored to meet regional requirements.

## Exploring

**AI-assisted search**
We are exploring how AI can improve search result quality for large knowledge bases.

**Cross-product data unification**
Working on bringing your data across products into one view.
```

### Internal variant (operational table)

See above. The internal variant is the full source-of-truth table with all columns: PM, EM, status, target sprint, KR mapping, dependencies, risks. Updated weekly.

### Triangulation

Pick **SAML SSO** as the test item:

- **Internal:** "Feature: SAML SSO with Okta and Azure AD. Sprint 24."
- **Executive:** "Enterprise customers can log in via their identity provider." (Outcome framing)
- **Customer:** "Single sign-on for enterprise. Shipping this quarter." (Benefit framing)

All three are the same item, appropriately framed. Pass.

---

## Part 7: Common failure modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| One roadmap for all audiences | Sales quotes internal dates; execs see feature lists; customers feel misled | Publish three variants; segment distribution |
| Customer variant has dates beyond current quarter | "Q3: ship X, Q4: ship Y" | Replace with "later this year" and "exploring" |
| Executive variant has features instead of outcomes | "We will ship the wizard, the API, and the export" | Replace each with the customer outcome the feature delivers |
| Internal variant lacks risks | Pretty table, no real visibility | Make risks and dependencies mandatory fields |
| Variants drift over the quarter | Updates happen only when there's news | Set a fixed quarterly republication date |
| Customer variant is identical to internal | Lazy export | Spend the translation time; the customer variant is a public-trust asset |

---

## Part 8: When you cannot publish three variants

Three variants are work. If the team cannot sustain quarterly republication of all three, publish only:

- **Internal** (always required; this is the source of truth)
- **Customer** (when prospects or partners need forward visibility)

Skip the executive variant and instead present the customer variant + an exec-only verbal walkthrough that adds risks and confidence ratings. This is honest -- you are admitting the team does not have the bandwidth for a fully separate executive artifact.

---

## Further reading

- Janna Bastow -- originator of the Now-Next-Later roadmap format
- Marty Cagan, "Empowered" (Wiley, 2020) -- Chapter on right-sized roadmaps
- Teresa Torres, "Continuous Discovery Habits" (2021) -- Opportunity Solution Trees as outcome inputs
- C. Todd Lombardo et al., "Product Roadmaps Relaunched" (O'Reilly, 2017)

---

**Last Updated:** 2026-05-21

## references/roadmap-variants-playbook.md

# Roadmap Variants Playbook

> Read this when building the three roadmap variants: the variant comparison tables, the "right-size the roadmap" principle, outcome-vs-feature framing, the detailed structure for each of the executive / customer / internal variants, the authoring workflow, troubleshooting, and success criteria. (For the origin of Now/Next/Later and full worked examples, see `roadmap-communication-guide.md`.)

## The three variants

| Variant | Audience | Time horizon detail | Risk framing | Format |
|---------|----------|---------------------|--------------|--------|
| **Executive** | Board, exec team, investors | Outcome-led; quarterly | Confidence levels (high/med/low) | 1-page narrative + simple visual |
| **Customer** | Customers, partners, sales prospects | Theme-led; "this year / later this year / next year" | No risk language; "exploring", "in development", "shipping soon" | Themes + benefit statements, no dates beyond current quarter |
| **Internal** | Engineering, design, support, account teams | Feature-led with dependencies | Explicit risks with mitigations | Detailed table with owners, dependencies, links to PRDs |

### What changes across variants

| Element | Executive | Customer | Internal |
|---------|-----------|----------|----------|
| **Granularity** | Outcomes (3-7 items) | Themes (5-10 items) | Features (15-50 items) |
| **Time horizon** | This quarter / next quarter / H2 | Now / Next / Later (themes only) | Sprint-by-sprint for "Now"; quarter for "Next" |
| **Dates** | Quarter only | Quarter only for "Now"; "later this year" for "Next" | Specific sprint and release dates for "Now" |
| **Risk** | Confidence per outcome | None (use language like "exploring" / "shipping soon") | Explicit: tigers, mitigations, dependencies |
| **Owner** | Exec sponsor per outcome | None | PM, EM, design lead per feature |
| **Metric** | Outcome metric + target | Benefit statement | KR + leading indicator |
| **What's NOT here** | Implementation detail, risk discussion | Risk, dependencies, internal team names | Marketing language, exec framing |
| **Visual** | Now/Next/Later 3-column or Gantt-summary | Themed cards or simple Now/Next/Later | Detailed table or Gantt |

## The "right-size the roadmap" principle

Marty Cagan's observation: **forecast confidence drops sharply with time horizon**. A 2-week commitment can be 90% confident. A 1-quarter commitment is maybe 70%. A 1-year commitment is 30% at best. Pretending otherwise (by promising features 9 months out) trains customers to disbelieve every roadmap you publish.

The Now / Next / Later structure encodes this honesty:

- **Now (this quarter):** Specific features with committed dates. Build is in flight or starting imminently. High confidence.
- **Next (next 1-2 quarters):** Themes with named outcomes, but specific features are not committed. Medium confidence.
- **Later (beyond):** Directions, hypotheses, big bets. Deliberately fuzzy. Low confidence by design.

Each audience needs this honesty calibrated:

- **Executives** want confidence ratings on each item (so they can plan).
- **Customers** want forward visibility without firm dates (so they can buy with confidence in the direction).
- **Internal teams** want explicit dependencies and risks (so they can execute).

## Outcome-based vs feature-based roadmaps

A second axis: **outcomes vs features**. Cagan and Torres both argue for outcome-based roadmaps -- the roadmap promises a customer outcome ("reduce onboarding from 14 days to 3 days"), not a feature ("ship guided onboarding wizard"). Outcomes survive scope changes; features become commitments that bind you to wrong solutions.

| Variant | Default orientation |
|---------|---------------------|
| Executive | Outcome-based always |
| Customer | Mix: themes (outcomes) for Next/Later; specific features for Now (when they are committed) |
| Internal | Feature-based for execution, but each feature must trace to an outcome |

The translation from feature to outcome is the highest-leverage move a PM can make in roadmap communication. "We are shipping X" is a feature. "Customers can now achieve Y" is an outcome.

## Variant 1: Executive Roadmap

**Purpose:** Build confidence that the team is solving the right problems and is on track.

**Length:** 1 page (slide or memo).

**Structure:**

1. **Header:** Quarter, sponsor, the one-sentence strategy this roadmap serves.
2. **Now (this quarter) -- 3-5 outcomes:** Each outcome named, with metric target, confidence rating (High/Med/Low), and lead PM.
3. **Next (next quarter) -- 3-5 outcomes:** Theme-level. No specific features. Confidence is implicit (Medium).
4. **Later (H2 directions) -- 2-3 big bets:** One line each. Deliberately fuzzy.
5. **What we are explicitly NOT doing this period:** 2-3 items. Builds credibility by showing tradeoffs.

**Voice:** Direct, plain, confident-but-honest. No marketing adjectives. No "leveraging" or "synergizing." Bezos memo style.

**Visualization:** Now/Next/Later 3-column or a slim Gantt of the 3-5 Now-quarter outcomes. Avoid swim-lane explosions.

## Variant 2: Customer Roadmap

**Purpose:** Help customers and prospects make confident purchase or expansion decisions; help sales sell direction without overcommitting.

**Length:** 2-5 themed cards (web page or 1-2 slides).

**Structure:**

1. **Header:** "What's coming in [year]" -- positions roadmap as a window, not a contract.
2. **Now (this quarter) -- 3-5 themes with named features:** "Workflow automation: Connect tasks to your CRM with built-in triggers. Available this quarter."
3. **Next -- 3-5 themes, features unnamed:** "Reporting: deeper drill-down across teams and saved-view collaboration. Coming later this year."
4. **Exploring (Later) -- 2-3 directions:** "Exploring: AI-assisted task creation from meeting notes. Early experiments underway."

**Voice:** Benefits-led, customer-perspective. No internal team names. No release versions. No risk language. Use directional language ("exploring", "in development", "shipping soon") instead of dates beyond the current quarter.

**Visualization:** Themed cards (Notion / Productboard / Cards format). Avoid Gantt -- it reads as a commitment.

**Important caveats to repeat on the page:**

- "This roadmap is directional and may change as we learn from customers."
- "Items in 'Exploring' are not commitments."
- "Dates are based on current planning and may shift."

## Variant 3: Internal Roadmap

**Purpose:** Coordinate execution across teams; surface risks, dependencies, and capacity issues; enable detailed sprint planning.

**Length:** Detailed table or multi-tab spreadsheet/wiki. No length limit.

**Structure:**

1. **Header:** Quarter, sponsor, strategy reference, link to NSM and OKRs.
2. **Now (this quarter) -- features by team:**
   - Feature name, PM, EM, design lead, status, target sprint/release, KR mapped, dependencies, risks
3. **Next (next 1-2 quarters) -- themes with candidate features:**
   - Theme, PM, EM, target quarter, dependencies expected, open questions
4. **Later (H2) -- directions and hypotheses:**
   - Direction, sponsor, what we'd need to be true to commit
5. **Cross-cutting dependencies:** Platform changes, infra work, external vendor work
6. **Capacity view:** Team commitment vs available capacity per quarter

**Voice:** Direct, candid, complete. Risks named explicitly. Mitigations specified. Dependencies traced. This document trains trust internally and is the source of truth for the other two variants.

**Visualization:** Detailed table (sortable by team, quarter, status). Cross-link to PRDs (`create-prd/`), OKRs (`brainstorm-okrs/`), NSM (`north-star-metric/`), and PR/FAQs (`prfaq/`).

## Workflow

1. **Author the internal variant first.** This is the source of truth. All fields, all risks, all dependencies. Use the template in `assets/internal_roadmap_template.md`.
2. **Derive the executive variant.** Strip implementation; promote each Now item to its parent outcome; assign confidence ratings; remove dependencies; cap at 1 page.
3. **Derive the customer variant.** Translate features into customer benefits; strip dates beyond current quarter; remove risk language; use "exploring / in development / shipping soon."
4. **Run a triangulation check.** Pick one item in the Now bucket. Trace it from the internal feature to the executive outcome to the customer benefit. The three should be consistent -- different framings of the same thing.
5. **Distribute with named recipients.** Each variant has a distribution list. The internal variant is wiki-published; executive is in the board packet; customer goes on the public site or in sales decks.
6. **Re-publish on a fixed cadence.** Quarterly is standard; monthly for fast-moving startups.
7. **Update the customer variant LAST.** Customer-facing language outlives the items; surprise changes erode trust more than slow updates would.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Sales reps quote internal roadmap dates to prospects | One roadmap is being used by all audiences | Publish three variants; restrict internal-variant access; train sales on the customer variant |
| Executives say "I do not understand what's changing" between roadmap updates | Executive variant is feature-level instead of outcome-level | Rewrite Now items as outcomes; cap at 5 items per quarter |
| Customers feel misled when a "Later" item never ships | Customer variant uses commitment language for Later items | Use exploratory language ("exploring", "early experiments"); add the standard caveats line |
| Engineers feel managed by the customer variant | Customer variant lacks risk and the team feels accountable for the marketing version | Make the internal variant the operational source of truth; route engineering planning off internal only |
| The three variants drift apart over the quarter | No re-publication cadence; only updated when there's "news" | Publish on a fixed quarterly cadence; force the triangulation check at each update |
| Customer variant has 30 items | Mistaking comprehensiveness for transparency | Cap at 5-10 themes. More items dilute the signal and increase the surface area for "we never shipped X" |
| Internal variant lacks owners/dates | Created as a marketing asset, not as an execution tool | Make ownership and dates mandatory fields; reject roadmap entries without them |

## Success Criteria

- Every Now-quarter item exists in all three variants with consistent identity (same ID, different framing)
- The executive variant fits on one page and has 3-5 outcome items per Now-quarter
- The customer variant uses no internal team names, no dates beyond current quarter, and includes the directional caveats
- The internal variant has owner, dependencies, risks, and KR mapping for every Now item
- The triangulation check passes for every published roadmap (each item traces consistently across variants)
- Roadmaps are republished on a predictable cadence (quarterly minimum)
- A customer reading the customer variant 6 months later does not feel misled

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/roadmap-communication -->
