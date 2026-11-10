# eol-communication

> **Use these instructions for this whole conversation.** Apply them when: Plan and write end-of-life announcements with dated milestones, a working migration path and per-segment messages. Use when sunsetting a product, feature, API version or pricing tier.

# EOL Communication Expert

## Overview

Create clear, empathetic End-of-Life (EOL) communications that preserve customer trust and facilitate smooth transitions. Sunsetting a product is a high-stakes communication challenge -- done poorly, it damages brand trust and accelerates churn across your entire portfolio. Done well, it strengthens customer relationships and drives migration to replacement solutions.

The work runs in four phases: **(1) Pre-announcement planning** (what, why, who, when, what support, what risks), **(2) Craft the message** (transition narrative, customer impact, transition solution, timeline, one CTA), **(3) Segment and distribute** (different message and channel per segment), **(4) Support and monitor** (support FAQ, migration tracking, churn watch). See the playbook reference for the full framework, templates, and timeline guidance.

## When to Use

- **Product sunset** -- Discontinuing an entire product or product line.
- **Feature deprecation** -- Removing a significant feature from an existing product.
- **Service migration** -- Moving customers from one platform or infrastructure to another.
- **API retirement** -- Deprecating API versions or endpoints.
- **Pricing model change** -- Major pricing restructure that effectively ends old tiers.

### When NOT to Use

- Minor feature changes that don't require customer notification.
- Internal tooling changes with no customer impact.
- Bug fixes or patches (use release notes instead).

## Clarify First

Before crafting the EOL communication, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **What is being sunset and why:** drives the transition narrative and Phase 1 planning; a vague "why" reads as abandonment.
- **Replacement / migration path:** drives the transition solution and the single CTA; if it is broken or absent, do not announce yet.
- **Timeline and key dates:** drives the timeline section and varies sharply by product type (API vs paid product vs free feature).
- **Customer segments affected:** drives the Phase 3 segment/channel matrix; high-value accounts need different message and outreach than self-serve.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Plan** (phase 1): what ends, why, who is affected, the replacement, the dated milestones, and the support plan.
2. **Prove the migration path** before announcing: real customers have moved on the path you will recommend.
3. **Write the message** (phase 2): transition narrative, customer impact, the migration path, the dated timeline, one call to action.
4. **Segment** (phase 3): a different message and channel for high-value accounts, self-serve users and API consumers.
5. **Brief customer-facing staff first**, then announce, then monitor migration and churn weekly (phase 4).

**Verify** before sending: every milestone has a date; the draft has no "coming months" or "soon"; support, sales and CS have the internal FAQ; the CTA links to a path that works today. Templates and timelines by product type: `references/playbook.md`.

## Anti-Patterns

### Announcing before the migration path works
**Mistake:** The EOL email goes out while the migration tool is still "coming soon". Customers try it at launch, it breaks, and the support queue floods.
**Why it happens:** The shutdown date is set and the announcement feels urgent, so the tooling is assumed to catch up.
**Instead:** Treat a working migration path as a gate. A default [RECOMMENDED]: announce once about 10 real customers have migrated in production on the path you will recommend. Ten is enough to surface the common failure modes; for a product with a handful of enterprise accounts, use most of them instead.

### Vague timeline
**Mistake:** The message says "in the coming months" or "later this year" with no dates.
**Why it happens:** Some dates are not locked yet, and soft wording feels safer than committing.
**Instead:** Search the draft for "coming", "later", "in due course" and "soon", and replace each with a date. Give every milestone a date: announcement, new signups closed, feature freeze, data export deadline, shutdown.

### Customer-facing staff learn from customers
**Mistake:** Internal Slack hears about the EOL a minute after the public post, and a sales rep first hears of it from a customer on a call.
**Why it happens:** Internal comms feel like a formality next to the external message.
**Instead:** Brief sales, CS and support before the external announcement, with the internal FAQ in hand. 7-10 business days is a common default: long enough to rehearse answers and line up key-account calls, short enough not to leak. Before T-0, ask 3 customer-facing employees what the EOL message is. If they hesitate, hold the announcement.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## Files

| File | Purpose |
|---|---|
| `references/playbook.md` | Four-phase framework, message template, segment matrix, internal FAQ, timelines |
| `references/red-flags.md` | Bad/good announcements with fixes |
| `examples/sunsetting-classic-reports.md` | Worked sunset |

## References

- **[references/playbook.md](references/playbook.md)** — read this when crafting a sunset announcement: the 4-phase EOL framework, the messaging template and writing rules, the segment/channel matrix, the internal support FAQ, the monitoring checklist, timeline best practices by product type, troubleshooting, and success criteria.
- **[references/red-flags.md](references/red-flags.md)** — read this before sending the message to Legal and Support for review: common ways an EOL message, timeline, or migration plan goes wrong with bad/good examples anchored to the 4-phase framework.

## Scope & Limitations

**In Scope:** EOL message creation, timeline planning, segment-specific messaging, internal FAQ preparation, migration monitoring framework, customer objection handling, support team preparation.

**Out of Scope:** Replacement product development, data migration tooling implementation, legal contract review, refund processing, technical infrastructure decommissioning.

**Important Caveats:** EOL communication is only as good as the transition path behind it. If the replacement product isn't ready or the migration path is broken, the best-written message won't prevent customer frustration. Ensure migration tooling is tested before announcing.

## Integration Points

| Integration | Direction | What Flows |
|---|---|---|
| `create-prd/` | Complements | Replacement product PRD informs EOL transition narrative |
| `release-notes/` | Feeds into | Final product updates communicated alongside EOL timeline |
| `summarize-meeting/` | Receives from | EOL decision meeting notes inform communication content |
| `senior-pm/` | Receives from | Stakeholder map identifies high-risk accounts for personal outreach |
| `daci-framework/` | Complements | DACI chart clarifies who Drives the EOL decision and communication |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/playbook.md

# EOL Communication Playbook

> Read this when crafting a sunset announcement: the 4-phase EOL framework (planning → message → segment & distribute → support & monitor), the messaging template and writing rules, segment/channel matrix, internal support FAQ, monitoring checklist, timeline best practices, troubleshooting, and success criteria.

## EOL Communication Framework

### Phase 1: Pre-Announcement Planning

Before writing any communication, answer these questions:

| Question | Answer Required |
|---|---|
| What is being discontinued? | Specific product, feature, or service name |
| What is the replacement path? | Alternative product, migration path, or "none" |
| Why is this happening? | Honest reason framed around customer benefit |
| Who is affected? | Customer segments and estimated count |
| What is the timeline? | Key dates (announcement, deprecation, final shutdown) |
| What support is available? | Migration tools, documentation, customer success resources |
| What are the risks? | High-value accounts, contractual obligations, regulatory requirements |

### Phase 2: Craft the EOL Message

#### EOL Messaging Template

```markdown
## Product Transition Narrative

**We are**: [Company and relationship to the product being phased out]
- [Commitment to customers]
- [Product evolution context]
- [Future vision]

**Announcing**: [Single clear sentence stating EOL and introducing replacement]

**Because**:
- [Reason focused on customer benefit 1]
- [Reason focused on customer benefit 2]
- [Reason focused on customer benefit 3]

**Which means for you**: [Customer-centered impact and benefit summary]

## Current Product Context

**[Product name]**
- is a [brief description and primary function]
- that has served [target customer] for [timeframe]
- by providing [key benefits]

## Customer Impact

**We understand this may affect you by:**
- [Impact 1 -- be honest about inconvenience]
- [Impact 2 -- acknowledge disruption]
- [Impact 3 -- recognize switching costs]

## Transition Solution

**For** [affected customers]
- that currently use [discontinued product],
- [replacement product]
- is a [product category]
- that [benefit statement focused on continuity and improvements].

## Differentiation and Continuity

- Like [discontinued product], [replacement] provides [continuity of key benefits]
- While also offering [new benefits that justify the transition]

## Support and Next Steps

**To ensure a smooth transition, we will:**
- [Support measure 1 -- e.g., free migration tool]
- [Support measure 2 -- e.g., dedicated migration support team]
- [Support measure 3 -- e.g., extended parallel operation period]

## Timeline

| Date | Milestone |
|---|---|
| [Date 1] | Announcement and migration tools available |
| [Date 2] | New sign-ups disabled; existing users continue |
| [Date 3] | Feature freeze on old product |
| [Date 4] | Final data export deadline |
| [Date 5] | Product shutdown |

## Call to Action

- [Clear next step for customers]
- [Contact information for questions]
- [Link to migration guide]
```

### Writing Rules

1. **Lead with empathy, not defensiveness.** Acknowledge the disruption honestly.
2. **Focus on customer continuity.** Explain what stays the same, then what improves.
3. **Be specific about dates.** Vague timelines ("coming months") create anxiety.
4. **Provide concrete support.** Tools, documentation, and human help.
5. **Avoid corporate euphemisms.** "Sunsetting" and "streamlining" feel dishonest. Say "discontinuing" or "replacing."
6. **One clear call to action.** Don't overwhelm with options.

### Phase 3: Segment and Distribute

Different customer segments need different messages:

| Segment | Message Emphasis | Channel |
|---|---|---|
| Enterprise / High-value | Personal outreach, dedicated migration support, contract review | Direct email from account manager, followed by call |
| SMB / Mid-market | Self-serve migration tools, clear documentation | Email + in-app notification |
| Free / Low-tier | Simple transition guide, automated migration | Email + blog post |
| Developers / API users | Technical migration guide, deprecation timeline, SDK updates | Developer email list + docs site + changelog |

### Phase 4: Support and Monitor

#### Internal FAQ for Support Teams

Prepare your support team with answers to likely objections:

| Customer Objection | Recommended Response |
|---|---|
| "I don't want to switch" | Acknowledge frustration; emphasize what stays the same; offer migration help |
| "I need more time" | Explain timeline flexibility if any; offer extended access if possible |
| "The replacement doesn't have feature X" | Document the gap; provide workaround or roadmap commitment |
| "I want a refund" | Follow refund policy; escalate if needed; preserve relationship |
| "Why wasn't I consulted?" | Explain decision process; invite feedback on replacement |

#### Monitoring Checklist

- [ ] Track migration rate weekly (target: 80%+ by shutdown date)
- [ ] Monitor support ticket volume related to EOL
- [ ] Track churn across entire portfolio (not just EOL product)
- [ ] Monitor social media and community forums for sentiment
- [ ] Escalation path for high-risk accounts clear and documented

## EOL Timeline Best Practices

| Product Type | Minimum Notice Period | Recommended |
|---|---|---|
| Free product / feature | 30 days | 60 days |
| Paid product (monthly) | 60 days | 90 days |
| Paid product (annual) | End of contract term | 6+ months |
| Enterprise / API | 12 months | 18 months |
| Regulated industry | Per regulatory requirement | 12+ months |

## Integration with Other Skills

- Use `create-prd/` to document the replacement product requirements.
- Use `release-notes/` to communicate the final updates to the old product.
- Use `summarize-meeting/` to document EOL decision meetings.
- Use `senior-pm/` stakeholder mapping for high-risk account identification.

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---|---|---|
| Customer backlash on social media | Message too corporate; lacked empathy | Rewrite with customer-first language; acknowledge impact honestly |
| Low migration rate | Migration path too complex or unclear | Simplify migration tools; offer hands-on support; extend timeline |
| Support team overwhelmed | FAQ not prepared; team not trained on responses | Conduct support team briefing before announcement; provide response scripts |
| Enterprise customers threaten legal action | Contractual obligations not reviewed | Involve Legal before announcement; honor contract terms |
| Replacement product not ready | EOL announced before replacement was production-ready | Delay EOL timeline; run products in parallel until replacement is stable |
| Internal teams learn about EOL from customers | Communication leaked before internal alignment | Brief internal teams 1-2 weeks before external announcement |

## Success Criteria

- EOL message reviewed by Legal, Support, and Customer Success before publication
- 80%+ of affected customers migrated before shutdown date
- Support ticket volume related to EOL decreases week-over-week after announcement
- No increase in churn for non-EOL products (brand trust preserved)
- Zero contractual violations during EOL process
- Post-EOL retrospective conducted within 30 days of shutdown

## references/red-flags.md

# Red Flags: EOL Communication

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan the EOL message, timeline, and migration plan before sending to Legal and Support for review. Each red flag shows the *bad* version next to the *good* version, anchored to the 4-phase EOL framework.

---

## Red Flag 1: Cold sunset (no migration path)

**Symptom.** Email lands: "Product X will be discontinued on July 1. Thanks for being a customer."

**Why it's bad.** A sunset with no migration path treats the customer as disposable. Their workflow breaks; they had a contract with the team; the team broke it without offering anywhere to land. Brand trust collapses across the *entire* portfolio, not just the EOL product.

**Bad example:**
> "Subject: Product X Discontinuation. Body: 'We are discontinuing Product X effective July 1. Please plan accordingly. Thank you for being a customer.'"

**Good example:**
> "Subject: Product X is moving to Product Y on October 1 — here's the migration. Body: 'Product X has served our [target customer] for [3 years]. We're consolidating onto Product Y because [honest customer-benefit reason]. Migration plan: (1) Auto-migration tool ships May 30; (2) Free migration office hours every Tuesday until October 1; (3) Your existing data and configurations transfer automatically; (4) Pricing parity for first 12 months. Documentation: [link]. Migration team contact: [name + email].'"

**How to catch it.** Read the message. Is there a named alternative product or service? Is there a concrete migration mechanism with dates? If no, the sunset is cold.

---

## Red Flag 2: Vague timeline ("coming months")

**Symptom.** Message uses phrases like "in the coming months", "later this year", "in due course". No specific dates.

**Why it's bad.** Vague timelines create anxiety. Customers cannot plan. Some churn preemptively to avoid uncertainty; others wait too long and are blindsided. Either way, the team loses control of the narrative.

**Bad example:**
> "We will be sunsetting Product X in the coming months. We will provide more details as they become available."

**Good example:**
> "Product X timeline (locked, signed off by leadership):
> • May 22, 2026: Announcement (today).
> • June 30: New signups closed; existing users continue.
> • August 31: Feature freeze on Product X.
> • November 30: Final data export deadline (one-click tool available now).
> • December 31, 2026: Product X shutdown.
> All dates are firm. We will communicate at each milestone."

**How to catch it.** Search the message for "coming", "later", "in due course", "soon". Replace each with a specific date.

---

## Red Flag 3: Corporate euphemisms

**Symptom.** Message says "We are streamlining our portfolio" or "evolving our offerings" or "investing in next-generation experiences".

**Why it's bad.** Customers translate corporate euphemism in real time. They know "streamlining" means "killing your product"; they resent being addressed in code. Honesty performs better than spin every time.

**Bad example:**
> "We are streamlining our portfolio to invest in next-generation experiences. As part of this evolution, Product X will be sunset."

**Good example:**
> "We are discontinuing Product X on December 31, 2026. The honest reason: usage has declined to a level that no longer justifies the engineering investment, and we believe Product Y better serves the jobs you originally hired Product X to do."

**How to catch it.** Search for: streamlining, sunsetting, evolving, optimizing, next-generation, transitioning, consolidating. Replace each with "discontinuing", "replacing", "ending".

---

## Red Flag 4: Replacement product not actually ready

**Symptom.** EOL announced. Migration tool is described as "coming soon". Customers try it; it's broken; support is flooded.

**Why it's bad.** EOL communication is only as good as the transition behind it. Announcing before the migration path is production-ready means customers experience the worst of both worlds — anxiety about the EOL, and frustration with broken migration tooling.

**Bad example:**
> "Announcement on May 1: 'Migration tool ships May 15'. May 15 tool ships with critical bugs; support queue: 400 tickets in 48 hours."

**Good example:**
> "Internal gate: announce EOL only after the migration path is validated in production with at least 10 real customer migrations. Discovered + fixed bugs before announcement. Day-1 announcement included a video of a real customer migrating successfully."

**How to catch it.** Has 10+ real customers successfully migrated using the path? If no, the announcement is premature.

---

## Red Flag 5: Internal team learns from customers

**Symptom.** Salesperson on a customer call: "Oh no, I didn't know that was being discontinued." Customer screenshots. Twitter sees it.

**Why it's bad.** Internal misalignment becomes external embarrassment. The customer loses confidence ("they don't even know their own roadmap"). Sales and Support have no answers; the team handles a crisis instead of a launch.

**Bad example:**
> "External announcement Wednesday 9am. Internal Slack #all-hands announcement: Wednesday 9:01am. Sales rep on call at 9:05: customer asks about Product X EOL; rep: 'wait, what?'"

**Good example:**
> "Internal communication 7-10 business days before external. Sequence: T-10 sales + CS leads briefed; T-7 sales + support team training; T-5 internal FAQ distributed; T-3 sales-ready materials in Highspot; T-1 final readiness check; T-0 external announcement at 10am after internal stand-up confirmation. No external announcement until every customer-facing employee has been briefed."

**How to catch it.** Ask 3 customer-facing employees: "what's the EOL message?" If they hesitate, internal comms is behind external.

---

## Red Flag 6: No segment-specific messaging

**Symptom.** Same email goes to enterprise customers, SMBs, free-tier users, and API consumers. Enterprise customer (ARR $400k) receives the same generic email as a free-tier user.

**Why it's bad.** Enterprise customers need personal outreach, contract review, and dedicated migration support. SMBs need self-serve tooling. Developers need a technical guide and deprecation timeline. One message for all = none receive what they need.

**Bad example:**
> "Single email blast to 12,000 customers. Generic 'Product X is going away, here's a link to docs'. Enterprise account manager: 'I didn't know this was happening — my customer is furious.'"

**Good example:**
> "Segment-tailored comms:
> • Enterprise (>$50k ARR): personal call from account manager 7 days before public announcement; contract review; named migration manager; bespoke timeline if contract permits.
> • SMB (<$50k ARR): email + in-app notification; self-serve migration tool; weekly office hours.
> • Free tier: email + blog post + automated migration on opt-in.
> • Developers/API: technical migration guide; deprecation header on old API; SDK update notes."

**How to catch it.** Look at the comms plan. If it lists one channel + one message for all customers, segmentation is missing.

---

## Red Flag 7: No regulatory/contractual review

**Symptom.** EOL message goes out. Legal calls 24 hours later: "we're violating 12 enterprise contracts that have a 12-month termination notice."

**Why it's bad.** Pricing changes, sunsets, and EOLs are contractual events. Skipping Legal review exposes the company to suit, refunds, and reputational damage. In regulated industries (healthcare, finance), it can mean compliance violations.

**Bad example:**
> "EOL announced May 22, effective August 31. (Contracts review: skipped. 14 enterprise customers have contracts requiring 12-month notice. Lawsuits filed; settlements: $1.4M.)"

**Good example:**
> "Pre-announcement gate: Legal reviews all enterprise contracts for termination-notice clauses. Of 28 enterprise contracts: 14 require 12-month notice. EOL timeline adjusted: enterprise EOL extended to May 22 the following year; other tiers stay on original timeline. Communication tailored per contract. Reviewed by external counsel for regulated-industry customers (healthcare, fintech)."

**How to catch it.** Has Legal signed off on the timeline against existing contracts? If no, the announcement is unprotected.

---

## Red Flag 8: Migration rate not monitored

**Symptom.** EOL announced. 90 days later, shutdown approaches. PM checks: only 32% of customers have migrated. Panic.

**Why it's bad.** Late discovery of low migration rates leaves no time to react. Either the team extends the EOL (eroding the original messaging) or pulls the trigger and abandons customers (extreme reputational damage).

**Bad example:**
> "Day 90/120: migration rate check. 32% migrated. PM: 'we have 30 days and 68% of customers still on the old product. We need to extend.'"

**Good example:**
> "Weekly migration rate tracking, with thresholds:
> • Week 4: 20% migrated (target 15%). Green.
> • Week 8: 45% migrated (target 35%). Green.
> • Week 12: 65% migrated (target 60%). Green.
> • If at any check the rate is < 80% of target, escalate: increase comms, add personal outreach to lagging segments, consider timeline extension. Decision authority: DACI Driver."

**How to catch it.** Is there a weekly migration-rate dashboard? If not, the team is flying blind.

---

## Red Flag 9: Quiet escape window for enthusiast complaints

**Symptom.** Power-user community discovers the EOL via Reddit. Team has no plan; replies are defensive; community sentiment turns toxic.

**Why it's bad.** Power users and developer communities are over-indexed in influence. They are the early-adopter signal for your other customers. Their public anger amplifies. A defensive response makes it worse.

**Bad example:**
> "Reddit thread r/ProductX: 200 angry comments. Team comments once defensively. Twitter picks it up. TechCrunch writes a story. Other (non-EOL) products lose trust."

**Good example:**
> "Power-user comms plan: (1) Notify community moderators 48h before public announcement; (2) Provide an AMA the day of announcement with PM + Engineering Lead; (3) Acknowledge frustration in public replies, do not get defensive; (4) Offer 2-3 community-only concessions (extended migration window, free credits on new product, early access to features the community asked for). (5) Designated community manager monitors and responds for 30 days."

**How to catch it.** Is there a power-user / community-specific plan? If not, you are one Reddit post from a crisis.

---

## Red Flag 10: Refund and credit policy improvised

**Symptom.** Customer asks for a refund. Support says "let me check". 5 days later, no answer. Customer's email tone has shifted from disappointed to legal-threatening.

**Why it's bad.** Refunds are predictable; not preparing for them is incompetence. Improvisation produces inconsistent treatment — Customer A gets a 50% credit, Customer B gets nothing, they compare notes, both feel betrayed.

**Bad example:**
> "Support team's response on day 1: 'we don't have a refund policy for EOL yet; checking with leadership.' Day 5: still checking. Customer escalates to LinkedIn."

**Good example:**
> "Refund and credit policy approved 1 week before announcement and shared with support:
> • Annual subscribers: prorated refund for unused months OR equivalent credit on Product Y at 1.5x value.
> • Monthly subscribers: cancel anytime, no penalty.
> • Enterprise: per-contract; account manager owns.
> Support has macro responses for the top 5 refund scenarios. Customer requests resolved within 2 business days."

**How to catch it.** Read the support FAQ. Does it have a refund policy section with specifics? If no, support will improvise.

---

## Red Flag 11: API deprecation without versioning discipline

**Symptom.** API endpoints are deprecated. No deprecation headers, no client warnings, no SDK version updates. Customers' integrations break overnight at shutdown.

**Why it's bad.** Developer customers have automated systems depending on APIs. They expect industry-standard deprecation discipline (announce, header, sunset, remove). Skipping that breaks trust with the most technical buyers — who are the most vocal influencers.

**Bad example:**
> "API v1 deprecated; v2 ships May 1. Day of shutdown (Aug 31): v1 returns 410 Gone. 600 customer integrations break. Twitter: 'never trust [company] APIs again.'"

**Good example:**
> "API deprecation discipline:
> • Announcement T-12 months in API changelog + developer email list.
> • Deprecation header (`Sunset: 2026-08-31`) added at T-6 months.
> • Client warning in SDK at T-3 months.
> • Webhook to /v1 returns 200 with deprecation warning at T-1 month.
> • Final shutdown: T-0; 410 Gone with migration link in error body.
> • Migration guide published with code samples for every v1 endpoint."

**How to catch it.** Is there a `Sunset` header on the deprecated endpoints? Is there a published migration guide with code samples? If no, the discipline is missing.

---

## Red Flag 12: Post-EOL retrospective skipped

**Symptom.** Shutdown happens. Team moves on. No retrospective. The next EOL is run with the same mistakes.

**Why it's bad.** EOLs are organizational learning events. Each one teaches what worked and what didn't (comm timing, migration friction, refund handling, segment-specific issues). Skipping the retro means the next team relearns the same lessons painfully.

**Bad example:**
> "Shutdown Dec 31. Jan 5: PM moves to next project. No retro. Next EOL (six months later) repeats: vague timeline, late internal comms, broken migration tool."

**Good example:**
> "Post-EOL retrospective scheduled within 30 days of shutdown. Agenda:
> 1. Migration rate vs target (final).
> 2. Customer churn across portfolio (was brand trust preserved on non-EOL products?).
> 3. Support ticket volume profile.
> 4. Top 5 customer complaints, categorized.
> 5. What worked.
> 6. What we would do differently.
> 7. Updates to the EOL playbook for the next team.
> Output: revised EOL playbook + lessons-learned doc filed in the team wiki."

**How to catch it.** 30 days after shutdown, ask: "did we hold the retro?" If no, learning is lost.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Cold sunset (no migration path) | Is there a named alternative + concrete migration? |
| 2 | Vague timeline | Search message for "coming", "soon", "later" |
| 3 | Corporate euphemisms | Search for "streamlining", "evolving", "transitioning" |
| 4 | Replacement not ready | Have 10+ real customers migrated successfully? |
| 5 | Internal learns from customers | Ask 3 customer-facing employees the EOL message |
| 6 | No segment-specific messaging | One message for all = none receive what they need |
| 7 | No regulatory/contractual review | Has Legal signed off against existing contracts? |
| 8 | Migration rate not monitored | Is there a weekly migration-rate dashboard? |
| 9 | No power-user / community plan | Is there a community-specific comm plan? |
| 10 | Refund policy improvised | Read support FAQ — refund policy specific? |
| 11 | API deprecation without discipline | Is there a Sunset header + migration guide? |
| 12 | Post-EOL retro skipped | Within 30 days of shutdown, was a retro held? |

## Related Reading

- SKILL.md Troubleshooting
- `create-prd/` (replacement product PRD)
- `feature-flag-strategy/` (reverse-ramp Shape F)
- `daci-framework/` (assigning EOL decision Driver)
- `release-notes/` (final product updates)
- `senior-pm/` (stakeholder map for high-risk account outreach)

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/eol-communication
