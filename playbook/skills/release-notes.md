# release-notes

> **Use these instructions for this whole conversation.** Apply them when: Turn tickets, changelogs and git logs into user-facing notes grouped by type, breaking changes first. Use when announcing a product release, maintaining a changelog, or rewriting technical entries for customers.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Release Notes Expert

## Overview

Transform raw technical changes -- tickets, changelogs, git logs, PRDs -- into clear, user-benefit-oriented release notes. This skill ensures every release communicates value to the right audience in the right tone, via a 5-step methodology: gather input, classify each change into one of five categories, rewrite for user benefit, adjust tone for the audience, and assemble.

### When to Use

- **Product Releases** -- Announcing new versions to customers, partners, or internal stakeholders.
- **Sprint Demos** -- Summarizing what shipped for sprint review audiences.
- **Changelog Maintenance** -- Keeping a running log of changes across releases.
- **Customer Communication** -- Preparing release announcements for email, in-app, or documentation.

## Core Capabilities

- **5-category classification** — New Features, Improvements, Bug Fixes, Breaking Changes, Deprecations with explicit assignment rules
- **User-benefit rewriting** — lead with the outcome, plain language, 1-3 sentences; detects developer-perspective phrasing
- **Audience tone guidance** — B2B/enterprise, consumer, developer/API, internal
- **Automated generation** — `release_notes_generator.py` groups entries, formats markdown/JSON, and flags technical language for rewrite

## Clarify First

Before generating the release notes, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Audience:** B2B/enterprise, consumer, developer/API, or internal (sets the entire tone matrix and how much detail to include).
- **Source changes:** the tickets/PRs/changelog to translate, classified into the 5 categories (nothing generates without these).
- **Breaking changes & deprecations:** what changed, the required action, and by when (forces the mandatory breaking-change fields that protect user trust).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. **Collect what shipped**: cross-check Done tickets against the release diff; drop anything reverted.
2. **Write each entry for the reader** [RECOMMENDED]: what they can now do, not what the team changed. Breaking changes state what changed, what the user must do, and by which date.
3. **Generate** the grouped notes (categories with no entries are left out):

```bash
python3 scripts/release_notes_generator.py \
  --input assets/sample_release_entries.json \
  --product-name "Acme App" --version "2.5.0" --date 2026-11-08
```

4. **Verify**: rewrite every entry listed under "Rewriting Suggestions" (the tool flags developer jargon such as "refactor", "endpoint", CamelCase or snake_case identifiers) or confirm it is right for the audience, and check customer copy for internal details before sending.

Input: `{"entries": [{title, description, type, ticket_id}]}` with `type` one of feature, improvement, bugfix, breaking, deprecation. Flags: `--input F` or `--demo`, `--product-name`, `--version` (both required), `--date` (default today; pass it for reproducible output), `--format text|json`.

**Exit codes:** 0 notes written; 2 missing file, invalid JSON, wrong shape, invalid entries or a bad `--date`.

## Anti-Patterns

### Notes for features that never shipped
**Mistake:** An item appears because its ticket was marked Done, but the code was reverted before release.
**Why it happens:** The ticket tracker looks like the source of truth, so its Done list goes straight into `changes.json`.
**Instead:** Before running `release_notes_generator.py`, cross-check Done tickets against the shipped commits (for example `git log v4.1..v4.2`). Flag any ticket that is missing from the diff for human review, and remove it if it didn't ship.

### Marketing copy in place of specifics
**Mistake:** "Game-changing AI-powered insights now live across the platform!" with no behavior described.
**Why it happens:** Hype feels like it drives adoption, and describing the exact behavior takes more work.
**Instead:** Search for "revolutionary", "game-changing", "powered by AI" and "next-generation". Replace each with the specific behavior, the plans it is on, and how to turn it off.

### One note for internal and external readers
**Mistake:** The customer email includes "known issue: occasional 502 on Safari, rollback in progress, on-call: @ana".
**Why it happens:** Writing one note is faster, and the internal details feel like useful transparency.
**Instead:** Produce two artifacts from the same source. The internal one carries known issues, on-call and rollback steps. The external one is value-framed with breaking changes first. Check customer copy for "rollback", "on-call" and internal known issues before sending.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/methodology-and-tooling.md](references/methodology-and-tooling.md)** — full 5-step methodology, classification tables, rewriting before/after examples, audience tone matrix, output template, troubleshooting, success criteria, and the `release_notes_generator.py` flag + JSON-schema reference. Read when producing notes or running the tool.
- **[references/release-notes-guide.md](references/release-notes-guide.md)** — best-practices guide on category definitions, audience guidance, and worked examples. Read for the deeper rationale.
- **[references/red-flags.md](references/red-flags.md)** — concrete bad-vs-good entry examples and how to fix them. Read before publishing a draft.

## Files

| File | Purpose |
|---|---|
| `scripts/release_notes_generator.py` | Groups entries, flags jargon, renders markdown or JSON |
| `assets/sample_release_entries.json` | Sample entries incl. a breaking change and a deprecation |
| `assets/release_notes_template.md` | Release notes document template |
| `examples/wayfinder-v2-1-release-notes.md` | Worked release |

## Integration Points

| Integration | Direction | Description |
|------------|-----------|-------------|
| `sprint-retrospective/` | Receives from | Sprint commit data and type distribution inform what changes to include |
| `senior-pm/` | Complements | Stakeholder communication plans guide release note audience and tone |
| `execution/create-prd/` | Receives from | PRD feature descriptions (Section 7) become release note entry drafts |
| `scrum-master/` | Receives from | Sprint review outputs identify what shipped and needs documentation |
| `summarize-meeting/` | Receives from | Release planning meeting summaries capture context for release notes |
| `job-stories/` / `wwas/` | Receives from | User story descriptions inform user-benefit framing of entries |

## Scope & Limitations

**In Scope:**
- Structured release note generation from JSON input with 5 entry categories
- Automatic technical language detection with rewriting suggestions
- Markdown and JSON output formatting with category grouping
- Audience tone guidance (B2B, consumer, developer, internal)
- Classification rules for New Features, Improvements, Bug Fixes, Breaking Changes, and Deprecations

**Out of Scope:**
- Automatic extraction of changes from git history (see `sprint-retrospective/` for git analysis)
- Jira/Linear ticket integration for pulling completed stories (manual JSON input required)
- Changelog maintenance across multiple releases (this tool generates per-release notes)
- Distribution to email, in-app, or documentation channels (output is markdown/JSON for further processing)

**Important Caveats:**
- The rewriting suggestions are pattern-based heuristics. They catch common technical language but cannot assess whether a description truly communicates user benefit.
- Semantic versioning alignment is the user's responsibility. The tool does not validate that version numbers follow semver conventions relative to the change types present.
- Breaking changes require special care. Always include: what changed, what the user must do, and by when. Vague breaking change notes erode user trust.

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/methodology-and-tooling.md

# Release Notes Methodology, Template & Tooling

> Read this when you need the full 5-step methodology (gather, classify, rewrite, tone, assemble), the output template, the `release_notes_generator.py` command/flag reference, troubleshooting, or success criteria.

## Methodology

### Step 1: Gather Raw Input

Collect all changes from the release cycle:

- **Jira/Linear tickets** -- Completed stories, bugs, and tasks
- **Git log** -- Merge commits since last release tag
- **PRD references** -- Feature specs that shipped
- **Hotfix records** -- Emergency fixes deployed between releases

### Step 2: Classify Each Change

Assign every change to exactly one category:

| Category | Definition | Example |
|----------|-----------|---------|
| **New Features** | Net-new capabilities that did not exist before | New export-to-PDF option |
| **Improvements** | Enhancements to existing functionality | Faster dashboard loading |
| **Bug Fixes** | Corrections to broken or incorrect behavior | Fixed login redirect loop |
| **Breaking Changes** | Changes that require user action to adapt | API v2 replaces v1 endpoints |
| **Deprecations** | Features scheduled for future removal | Legacy CSV import will be removed in v4.0 |

**Classification rules:**

- If a change adds something entirely new, it is a **New Feature**.
- If it makes something existing better (faster, easier, more reliable), it is an **Improvement**.
- If it fixes something that was wrong, it is a **Bug Fix**.
- If users must change their behavior, configuration, or integration, it is a **Breaking Change**.
- If a feature still works but will be removed later, it is a **Deprecation**.

### Step 3: Rewrite for User Benefit

The most critical step. Every entry must lead with the benefit to the user, not the technical change.

**Rewriting principles:**

1. **Lead with the outcome.** What can the user do now that they could not before, or what is better for them?
2. **Use plain language.** Avoid internal jargon, code references, or implementation details.
3. **Keep it to 1-3 sentences.** One sentence for minor items, up to three for significant features.
4. **Include context when needed.** If users need to take action, tell them exactly what to do.

**Before and after examples:**

| Technical (Bad) | User-Benefit (Good) |
|----------------|-------------------|
| Implemented Redis caching layer for dashboard queries | Dashboards now load up to 3x faster |
| Refactored authentication module to use OAuth 2.0 PKCE flow | Sign-in is now more secure and works reliably across all browsers |
| Fixed null pointer exception in report export handler | Report exports no longer fail when date ranges include empty days |
| Migrated user preferences API from v1 to v2 schema | **Action required:** Update your API calls to use the new `/v2/preferences` endpoint by April 30. See migration guide. |
| Added feature flag for beta dashboard | You can now opt into the redesigned dashboard from Settings > Beta Features |

**Red flags that an entry needs rewriting:**

- Mentions a class name, function, or library
- Starts with "Refactored," "Migrated," or "Updated" without stating impact
- Uses acronyms the target audience would not know
- Describes what the team did instead of what the user gains

### Step 4: Adjust Tone for Audience

| Audience | Tone | Style Notes |
|----------|------|-------------|
| **B2B / Enterprise** | Professional, precise | Emphasize reliability, security, compliance. Avoid casual language. |
| **Consumer** | Friendly, conversational | Use "you" and "your." Celebrate new features. Keep it light. |
| **Developer / API** | Technical, direct | Include endpoint names, SDK versions, code snippets. Be specific. |
| **Internal** | Detailed, context-rich | Include ticket IDs, team names, technical details as needed. |

### Step 5: Assemble the Release Notes

Use the output template below. Include only categories that have entries -- do not show empty sections.

## Output Template

```markdown
# [Product Name] v[X.Y.Z] Release Notes

**Release Date:** [YYYY-MM-DD]

---

## New Features

- **[Feature Name]** -- [1-3 sentence description of user benefit]. ([TICKET-ID])

## Improvements

- **[Improvement Name]** -- [1-2 sentence description of what is better]. ([TICKET-ID])

## Bug Fixes

- **[Bug Fix Name]** -- [1 sentence describing what was broken and that it is now fixed]. ([TICKET-ID])

## Breaking Changes

> **Action Required:** The following changes require updates on your end.

- **[Change Name]** -- [Description of what changed and exactly what the user must do]. ([TICKET-ID])

## Deprecations

> **Planned Removal:** The following features will be removed in a future release.

- **[Feature Name]** -- [What is being deprecated and when it will be removed. Recommend alternative if available]. ([TICKET-ID])

---

**Full changelog:** [link]
**Questions?** [support link or contact]
```

## Python Tool

Use `scripts/release_notes_generator.py` to generate formatted release notes from structured input.

```bash
# Generate from JSON input
python scripts/release_notes_generator.py --input changes.json --product-name "Acme App" --version "2.5.0"

# Run with demo data
python scripts/release_notes_generator.py --demo --product-name "Acme App" --version "1.0.0"

# Output as JSON instead of markdown
python scripts/release_notes_generator.py --input changes.json --format json --product-name "Acme App" --version "2.5.0"
```

See `scripts/release_notes_generator.py --help` for full usage.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Tool flags too many entries as "technical language" | TECHNICAL_PATTERNS is a keyword heuristic (jargon verbs like "refactor", acronyms such as API or SSO, code identifiers) | Review the flagged entries; the tool provides suggestions, not mandates -- ignore false positives for user-facing descriptions |
| All entries classified as same type | Input JSON uses wrong type values or inconsistent casing | Use exact lowercase types: `feature`, `improvement`, `bugfix`, `breaking`, `deprecation` |
| Empty sections appear in output | No entries of that type exist but template still renders the section | The tool only renders sections with entries; empty sections indicate a data issue in input |
| Breaking changes not highlighted prominently | Entries marked as `improvement` instead of `breaking` | Review classification rules: if users must change behavior, config, or integration, it is `breaking`, not `improvement` |
| Release notes sound like commit messages | Descriptions written from developer perspective, not user perspective | Apply the rewriting principles: lead with outcome, use plain language, 1-3 sentences per entry |
| `--demo` flag requires `--product-name` and `--version` | These are required arguments regardless of input source | Always provide both: `--demo --product-name "App" --version "1.0.0"` |
| JSON output missing rewriting suggestions | No entries triggered technical language detection patterns | This is expected behavior; suggestions only appear when TECHNICAL_PATTERNS match entry descriptions |

## Success Criteria

- Every release has structured notes published within 24 hours of deployment
- All entries lead with user benefit, not technical implementation details
- Breaking changes include explicit migration instructions with deadlines
- Deprecations include removal timeline and recommended alternatives
- Technical language flags reviewed and addressed before publication
- Release notes tone matches the target audience (B2B/consumer/developer/internal)
- Entries traceable to tickets via ticket_id for audit and context

## Tool Reference

### release_notes_generator.py

Generates formatted release notes from structured JSON input. Groups entries by category, formats into markdown or JSON, and flags entries that may need user-benefit rewriting.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input` | string | (optional) | Path to JSON file containing release entries |
| `--demo` | flag | off | Run with built-in demo data (8 entries across all types) |
| `--product-name` | string | (required) | Product name for the release notes header |
| `--version` | string | (required) | Version string (e.g., `2.5.0`) |
| `--format` | choice | `text` | Output format: `text` (markdown) or `json` |
| `--date` | string | today | Release date in YYYY-MM-DD format |

**Input JSON schema:**
```json
{
  "entries": [
    {
      "title": "Feature Name",
      "description": "User-benefit description (1-3 sentences)",
      "type": "feature|improvement|bugfix|breaking|deprecation",
      "ticket_id": "PROJ-123 (optional)"
    }
  ]
}
```

## references/red-flags.md

# Red Flags: Release Notes

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every release-note draft before it ships to customers, in-app, or via email. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Changelog Disguised as Release Notes

**Symptom.** The release note is a list of ticket titles copied from Jira / Linear, with the engineering vocabulary intact.
**Why it's bad.** A changelog is for developers; release notes are for users. Pasting tickets verbatim makes customers parse internal language ("Fixed: SEG-2241"), lowers read-through, and hides genuine value behind noise.
**Bad example:**
> "v3.4 release notes:
> - SEG-2241 Refactor of the user-event ingestion pipeline
> - SEG-2310 Added retry logic to webhook dispatcher
> - SEG-2342 Migrated from Redis 6 to Redis 7"
**Good example:**
> "v3.4 release notes:
> **Events arrive faster.** Webhook events now retry automatically when receivers are slow, reducing the 'missing event' tickets you have been raising by ~80%. No setup needed.
> *(Internal: SEG-2241, 2310, 2342)*"
**How to catch it.** Search the draft for ticket IDs in customer-facing text. Any visible ID = rewrite the line.

---

## Red Flag 2: No Value Framing

**Symptom.** Each item describes what was *built* but never *why a customer should care*.
**Why it's bad.** Customers skim release notes for 8 seconds and look for "what does this do for me?". Bare feature descriptions force them to translate, and they bounce. Adoption lags because no one knows what to try.
**Bad example:**
> "Added: keyboard shortcut Cmd+Shift+E to export."
**Good example:**
> "Export 10x faster from anywhere. New `Cmd+Shift+E` shortcut opens the export dialog from any view -- no more clicking through the menu. Useful for analysts who export several times a day."
**How to catch it.** Each item should answer "what can the customer now do that they could not do before, and why does it matter?". If absent, rewrite.

---

## Red Flag 3: Mixing Internal Refactors with Customer Wins

**Symptom.** Release notes list "migrated to Postgres 16" alongside "added dark mode" with equal weight.
**Why it's bad.** Internal infrastructure changes -- even ones engineers are proud of -- mean nothing to most customers and dilute the high-signal items. Customers learn to skim past your release notes because most lines do not concern them.
**Bad example:**
> "v4.2:
> - Dark mode is here.
> - Migrated from Postgres 14 to 16.
> - Added new pricing page.
> - Refactored the WebSocket reconnection logic."
**Good example:**
> "v4.2 (customer-facing):
> - Dark mode is here.
> - New pricing page lets you compare plans at a glance.
> ---
> v4.2 (under the hood, for our developer customers):
> - Postgres 16 upgrade: queries are 15% faster on average; expect snappier dashboards.
> - WebSocket reconnection is more aggressive: fewer 'disconnected' banners during flaky networks."
**How to catch it.** Items that mention only internal systems and have no observable customer impact = move to a separate "under the hood" section, or drop.

---

## Red Flag 4: No Segmentation by Audience

**Symptom.** One release note goes to all customers regardless of plan, segment, or feature usage.
**Why it's bad.** Enterprise admins want compliance / SSO / audit changes. End-users want UI changes. API customers want SDK / webhook changes. A blast email mixing them gets archived by everyone.
**Bad example:**
> "Hi everyone: SCIM provisioning is now generally available, dark mode is here, the Python SDK is bumped to v3, and our soc 2 audit completed."
**Good example:**
> "Three release notes generated from the same release:
> - For *Admins on Enterprise*: SCIM GA + SOC 2 audit report (link).
> - For *all users*: Dark mode is here.
> - For *API users*: Python SDK v3 with type hints and async support."
**How to catch it.** One draft, one audience. If you have multiple personas, generate multiple notes.

---

## Red Flag 5: Buried Breaking Changes

**Symptom.** A breaking API change is the 11th item in a bulleted list of 14, formatted identically to the rest.
**Why it's bad.** Breaking changes need attention or customers' production systems break. Burying them is a support and trust disaster. They must be at the top, visually distinct, with migration steps.
**Bad example:**
> "v5.0 release notes:
> - Faster searches.
> - New billing portal.
> - ...
> - [item 11] Deprecated /v1/users endpoint."
**Good example:**
> "**v5.0 -- ACTION REQUIRED before June 30**
> The `/v1/users` endpoint is deprecated and will be removed on June 30. Migrate to `/v2/users` (docs: link). Affected: every customer using the legacy SDK < 2.4.
> ---
> Other changes in this release: ..."
**How to catch it.** Search for "deprecated", "removed", "no longer supported". Any such item not in the first 100 words of the note = move to the top.

---

## Red Flag 6: Marketing Copy Replacing Specifics

**Symptom.** "Revolutionary new collaboration experience powered by AI." -- no concrete behavior described.
**Why it's bad.** Customers cannot try a "revolutionary experience". They try features. Vague hype copy in release notes signals the team is hiding either the feature is small or it does not actually solve a problem.
**Bad example:**
> "Game-changing AI-powered insights now live across the platform!"
**Good example:**
> "AI summaries on dashboards. When a dashboard has >= 6 charts, a 3-sentence summary appears at the top describing the most notable change since last week. Available on Pro and Enterprise plans. Disable in Settings -> AI."
**How to catch it.** Search for "revolutionary", "game-changing", "powered by AI", "next-generation". Each one needs a specific behavior + plan + opt-out.

---

## Red Flag 7: No Visual

**Symptom.** A UI change described in words only, no screenshot or short GIF.
**Why it's bad.** Visual changes are 3-5x more likely to drive adoption when shown vs described. Customers skim, see the screenshot, and immediately try the feature. Without a visual, the line is invisible.
**Bad example:**
> "We redesigned the dashboard navigation."
**Good example:**
> "We redesigned the dashboard navigation. [Annotated screenshot showing before / after, 30 KB, alt text describing the change]. The most-used 5 destinations are now in a left rail; everything else is in a 'More' menu. No action needed on your part."
**How to catch it.** Any line describing a UI change without an attached image = add or rewrite.

---

## Red Flag 8: No Version Number or Date

**Symptom.** Release note headline is "What's new!" with no version or date.
**Why it's bad.** Customers cite release notes in support tickets, internal change-management, and procurement reviews. Without a version + date, they cannot reference the note unambiguously, and support cannot disambiguate ("which 'what's new' are you on?").
**Bad example:**
> "# What's new!
> Dark mode and faster searches!"
**Good example:**
> "# v4.2 -- released June 14, 2026
> ## Highlights
> Dark mode and faster searches. Full notes below."
**How to catch it.** Top of the note must have a version and a date. No exceptions.

---

## Red Flag 9: Generated from Tickets That Were Never Closed Correctly

**Symptom.** Items appear in the release notes that were not actually shipped, because the underlying tickets were marked Done in Jira but the feature was reverted in code.
**Why it's bad.** Promising features that did not ship is a credibility disaster. Customers report bugs against features that do not exist, support has no answer, and trust drops.
**Bad example:**
> "v4.2: 'Granular permissions for projects' (ticket SEG-2400 marked Done in Jira)."
> ... but the feature was reverted in PR #4220 due to a security review.
**Good example:**
> "Before building `changes.json`, the PM runs `git log v4.1..v4.2` and checks each Jira Done ticket against the shipped commits. Tickets with no commit in the range go to human review. SEG-2400 caught; left out of the input, so it never reaches the notes."
**How to catch it.** `scripts/release_notes_generator.py` formats whatever entries it is given and does not look at git. Cross-check the Jira / Linear "Done" list against `git log <previous-tag>..<release-tag>` before you write the input file.

---

## Red Flag 10: Same Release Note Used Internally and Externally

**Symptom.** The internal Slack announcement and the customer-facing post are identical.
**Why it's bad.** Internal notes need known issues, on-call instructions, rollback procedures, and the rationale for sequencing. External notes need value framing and migration steps. Mashing them confuses both audiences.
**Bad example:**
> "Customer email contains: 'Known issue: occasional 502 on Safari, rollback in progress, on-call: @ana'."
**Good example:**
> "Two artifacts from the same release:
> - Internal: changelog + known issues + on-call + rollback steps + post-release-check checklist.
> - External: value-framed, audience-segmented, breaking-changes-first, with visuals.
> Both built from the same ticket list: run `scripts/release_notes_generator.py` once per audience, each time with its own input file (internal entries keep known issues and rollback notes; external entries keep value framing and migration steps)."
**How to catch it.** Audit any release note for the words 'rollback', 'known issue: internal', 'on-call'. If present in customer-facing copy, split.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Changelog disguised as notes | Are ticket IDs visible in customer copy? |
| 2 | No value framing | Does each item answer "why care"? |
| 3 | Internal refactors mixed in | Are infra changes in a separate section? |
| 4 | No segmentation | One audience per draft? |
| 5 | Buried breaking changes | Are deprecations in the first 100 words? |
| 6 | Marketing copy replacing specifics | Does every "AI-powered" line have a concrete behavior? |
| 7 | No visual | UI changes have images? |
| 8 | No version + date | Top of note has both? |
| 9 | Generated from stale Jira | Was the Done list checked against `git log` before generating? |
| 10 | Internal = external | Are 'rollback' / 'on-call' in customer copy? |

## Related Reading

- `SKILL.md` -- release-note structure
- `scripts/release_notes_generator.py --help` -- the generator (formats JSON entries as text or JSON; it does not read git)
- Sibling skill: `execution/launch-playbook/` -- coordinated launch sequence
- Sibling skill: `execution/feature-flag-strategy/` -- handle gradual rollouts that span releases
- Sibling skill: `execution/roadmap-communication/` -- audience-segmented messaging patterns

## references/release-notes-guide.md

# Release Notes Best Practices Guide

## Purpose

Release notes are the bridge between what your team built and what your users understand. They serve three functions: inform users of what changed, build trust through transparency, and drive adoption of new capabilities.

## Category Definitions

### New Features

Something that did not exist before. The user gains a capability they previously lacked.

**Test:** Could the user do this yesterday? If no, it is a new feature.

### Improvements

An existing capability that is now better -- faster, easier, more reliable, more accessible.

**Test:** Could the user already do this, but now it is better? If yes, it is an improvement.

### Bug Fixes

Something was broken and is now fixed. The software was not behaving as intended or documented.

**Test:** Was this a defect report or unexpected behavior? If yes, it is a bug fix.

### Breaking Changes

A change that requires the user to take action. Their existing workflow, integration, or configuration will stop working or behave differently without intervention.

**Test:** Will anything break for the user if they do nothing? If yes, it is a breaking change.

### Deprecations

A feature that still works today but will be removed in a future release. This gives users time to migrate.

**Test:** Does it still work but is scheduled for removal? If yes, it is a deprecation.

## Writing for Different Audiences

### B2B / Enterprise

- **Tone:** Professional, precise, confident
- **Emphasize:** Reliability, security, compliance, productivity gains
- **Avoid:** Casual language, exclamation marks, emojis
- **Include:** Impact on workflows, admin actions required, compliance implications
- **Example:** "Role-based access controls now support custom permission sets, enabling administrators to define granular access policies aligned with organizational security requirements."

### Consumer

- **Tone:** Friendly, conversational, enthusiastic (measured)
- **Emphasize:** Ease of use, delight, time saved, new possibilities
- **Avoid:** Technical jargon, implementation details
- **Include:** Visual descriptions, tips for getting started
- **Example:** "You can now organize your photos into custom albums. Tap the new Albums tab to get started."

### Developer / API

- **Tone:** Technical, direct, specific
- **Emphasize:** Endpoints, parameters, SDK versions, migration steps
- **Avoid:** Marketing language, vague descriptions
- **Include:** Code snippets, request/response examples, version numbers
- **Example:** "The `GET /v2/users` endpoint now accepts an optional `fields` query parameter for sparse fieldsets. See the API reference for supported field names."

### Internal Stakeholders

- **Tone:** Detailed, context-rich
- **Emphasize:** Business impact, metrics, team contributions
- **Avoid:** Over-simplification
- **Include:** Ticket IDs, team names, technical context as needed

## Distribution Channels

| Channel | Best For | Format |
|---------|----------|--------|
| **In-app notification** | All users, high visibility | Short summary with link to full notes |
| **Email** | Active users, subscription-based | Full notes or curated highlights |
| **Blog post** | Major releases, marketing value | Narrative format with screenshots |
| **Changelog page** | Developer audience, reference | Chronological, all versions |
| **Documentation** | API changes, migration guides | Technical, step-by-step |
| **Social media** | Brand awareness, feature highlights | Single feature spotlight |
| **Slack / Teams** | Internal stakeholders | Summary with links |

## Good vs Bad Examples

### Bad: Technical and self-centered

> - Updated React from v17 to v18
> - Refactored UserService to use repository pattern
> - Fixed NPE in ReportExportHandler.java line 234
> - Migrated auth to PKCE flow

### Good: User-benefit-oriented

> - **Smoother interactions** -- Page transitions and form updates are now noticeably faster and more responsive.
> - **Faster report exports** -- Reports that previously timed out now complete reliably, even for large date ranges.
> - **More secure sign-in** -- Your account is now protected by an upgraded authentication standard that works consistently across all browsers.

### Bad: Vague and unhelpful

> - Various bug fixes and improvements
> - Performance enhancements
> - Updated dependencies

### Good: Specific and actionable

> - **Fixed:** CSV exports now include all columns when custom fields are enabled. (BUG-3421)
> - **Faster:** Dashboard widgets load 40% faster on pages with more than 20 widgets.
> - **Updated:** The Python SDK now requires Python 3.9 or later. See the migration guide for upgrade instructions.

## Checklist Before Publishing

- [ ] Every entry leads with user benefit, not technical change
- [ ] No internal jargon, class names, or function references
- [ ] Breaking changes clearly state what the user must do
- [ ] Deprecations include a timeline and recommended alternative
- [ ] Tone matches the target audience
- [ ] Ticket IDs are included for traceability (if appropriate for audience)
- [ ] Empty categories are removed
- [ ] Release date and version number are correct
- [ ] Links to full changelog, support, and migration guides are included

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/release-notes
