---
description: "Builds, validates and retires reusable Jira issue and Confluence page templates. Use when creating a team or org-wide template, a template is ignored or half-filled, or a template library has sprawled. Space layout is confluence-expert."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Atlassian Template & Files Creator Expert

Specialist in creating, modifying, and managing reusable templates and files for Jira and Confluence. Ensures consistency, accelerates content creation, and maintains org-wide standards through canonical, parameterized templates rather than per-use-case sprawl.

## Core Capabilities

- **Template design** — Confluence page templates with dynamic content, Jira issue templates/descriptions, blueprints for multi-page structures, versioning
- **Content standardization** — org-wide standards, reusable components and macros, template libraries, documentation
- **Automation** — dynamic fields, Jira integration, self-updating structures, template-based workflows
- **Governance** — lifecycle management, version control, deprecation, usage/adoption tracking

## When to Use

- Building org-wide Confluence page templates or Jira issue templates
- Designing blueprints for complex, multi-page content structures
- Establishing content standards and a curated template library
- Migrating teams off ad-hoc, from-scratch pages toward standardized templates
- Diagnosing low template adoption, broken macros, or version confusion

## Clarify First

Before building the template, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Target tool & artifact:** Confluence page template, Jira issue template, or multi-page blueprint (sets which macros/fields are available and the structure).
- **Template type:** meeting notes, PRD, charter, bug report, decision log, etc. (selects the base structure and placeholders).
- **Rollout scope:** one team vs org-wide canonical template (drives parameterization, naming, and governance).
- **Dynamic vs static content:** which fields auto-populate via macros/Jira queries vs fixed placeholders (drives build complexity and adoption).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

1. **Discover** stakeholder needs and review existing content patterns
2. **Design** the structure with clear placeholders + inline guidance
3. **Build** with macros (panels, info/note, tasks, status, dynamic Jira queries)
4. **Test** with sample data, then **publish** to the target space/project
5. **Train** users and **monitor** adoption; iterate quarterly

Grab a ready-made starting point from `references/confluence-templates.md` or `references/jira-templates.md`, then follow the full creation/modification workflow in `references/workflows-and-governance.md`. Step 3 is `template_scaffolder.py`; step 4 is `template_validator.py`; step 5 is `template_usage_analyzer.py`.

## Tools

Each tool reads one JSON file and prints a text report (`--json` for machine output).
`--example` prints the input shape; samples ship in `assets/`. Bad input (missing file,
invalid JSON, wrong shape) exits 2 with a one-line error.

```bash
python3 scripts/template_scaffolder.py --spec assets/sample_template_spec.json --format confluence
python3 scripts/template_validator.py --template assets/sample_template.json         # exit 0
python3 scripts/template_validator.py --template assets/sample_template_flawed.json  # exit 1
python3 scripts/template_usage_analyzer.py --usage assets/sample_template_usage.json
```

| Tool | What it does | Exit |
|------|--------------|------|
| `template_scaffolder.py` | Turns a section spec into Confluence wiki markup or a Jira description (`--format confluence\|jira`) | 0 |
| `template_validator.py` | 10 weighted checks: name, owner, description, 3+ sections, inline instructions, example, dynamic content, version, updated within 12 months of `as_of` (default today), labels | 0 all pass, 1 any fail |
| `template_usage_analyzer.py` | Adoption, quality score and freshness per template; flags zero-use, low-quality and ownerless templates. Freshness is measured from the file's `as_of`, else its latest `last_updated` | 0 |

## Anti-Patterns

### A new template for every variation
**Mistake:** The space fills up with "PRD v1", "PRD v2", "PRD - mobile" and copies of copies.
**Why it happens:** Copying a template and tweaking it is quicker than changing the shared one.
**Instead:** Keep a small set of canonical templates with parameterized sections. More than 15 templates in one top-level space is sprawl. Merge the variants and retire the rest.

### Fields nobody fills in
**Mistake:** The template has 40 fields, and 25 of them end up blank, "TBD" or "N/A".
**Why it happens:** Each field looked useful when someone proposed it, and nobody checks how they get used.
**Instead:** Measure fill rate per field across the last 50 uses. Remove or make optional any field below 50%. Make a section required only if 80% or more of authors will have real content for it.

### Macros that render empty
**Mistake:** The template ships a Jira-issues macro with a hardcoded JQL filter, or a page-properties report on a label nobody uses.
**Why it happens:** The macro worked in the space where the template was built.
**Instead:** Render the template into a sample page before you publish it. Every macro must show real content or a clear "configure me" prompt. It must never show a silent blank.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/confluence-templates.md](references/confluence-templates.md)** — full Confluence template library (Meeting Notes, Project Charter, Sprint Retrospective, PRD, Decision Log). Read when you need a ready-to-paste Confluence page template.
- **[references/jira-templates.md](references/jira-templates.md)** — full Jira issue template library (User Story, Bug Report, Epic). Read when you need a ready-to-paste Jira description.
- **[references/workflows-and-governance.md](references/workflows-and-governance.md)** — step-by-step creation/modification/blueprint workflows, best practices, role handoff protocols, governance, and Atlassian MCP operations. Read when building, modifying, or operationalizing templates.
- **[references/troubleshooting.md](references/troubleshooting.md)** — troubleshooting table (adoption, macro breakage, versioning, stale data) and measurable success criteria. Read when a deployed template misbehaves or to define done.
- **[references/red-flags.md](references/red-flags.md)** — common ways template output goes wrong with bad/good examples (template sprawl and more). Read before publishing a template for org-wide use.

## Scope & Limitations

**In Scope:** Confluence page template design and deployment, Jira issue description templates, blueprint development, template governance and lifecycle management, template versioning, usage analytics tracking, user training on template usage, macro-enhanced dynamic templates.

**Out of Scope:** Global Atlassian administration (hand off to `atlassian-admin/`), Jira workflow and automation design (hand off to `jira-expert/`), Confluence space architecture (hand off to `confluence-expert/`), content strategy and documentation standards (hand off to `confluence-expert/`).

**Limitations:** Confluence Cloud templates cannot include all macro types (some advanced macros require manual insertion after page creation). Jira issue templates are limited to description field content -- they cannot pre-set custom field values without automation rules. Template analytics require Confluence Premium or a marketplace analytics app for detailed usage metrics.

## Files

| File | Purpose |
|------|---------|
| `scripts/template_scaffolder.py`, `scripts/template_validator.py`, `scripts/template_usage_analyzer.py` | See Tools |
| `assets/sample_template_spec.json`, `assets/sample_template.json`, `assets/sample_template_flawed.json`, `assets/sample_template_usage.json` | Runnable inputs; the flawed template shows a failing gate |
| `references/*.md` | See References |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/confluence-templates.md

# Confluence Templates Library

Read this when you need a ready-to-use Confluence page template. Copy the block, replace the bracketed placeholders, and adjust macros for your space.

### 1. Meeting Notes Template
```markdown
---
**Meeting Title**: [Meeting Name]
**Date**: {date:format=dd MMM yyyy}
**Time**: [Time]
**Attendees**: @user1, @user2, @user3
**Facilitator**: @facilitator
**Note Taker**: @notetaker
---

{info}
**Quick Links**:
- [Previous Meeting](link)
- [Project Page](link)
- [Jira Board](link)
{info}

## Agenda
1. [Topic 1] - [Duration] - [Owner]
2. [Topic 2] - [Duration] - [Owner]
3. [Topic 3] - [Duration] - [Owner]

## Discussion & Notes

### [Topic 1]
**Presenter**: @owner
**Discussion**:
- Key point 1
- Key point 2

**Decisions Made**:
{panel:title=Decision|borderColor=#00875a}
[Decision description]
**Decided by**: @decisionmaker
{panel}

### [Topic 2]
[Continue pattern]

## Action Items
{tasks}
- [ ] [Action item 1] - @owner - Due: [Date]
- [ ] [Action item 2] - @owner - Due: [Date]
- [ ] [Action item 3] - @owner - Due: [Date]
{tasks}

## Parking Lot
{note}
Topics to discuss in future meetings:
- [Deferred topic 1]
- [Deferred topic 2]
{note}

## Next Meeting
**Date**: [Next meeting date]
**Focus**: [Next meeting focus areas]
```

### 2. Project Charter Template
```markdown
{panel:title=Project Overview|borderColor=#0052cc}
**Project Name**: [Project Name]
**Project Code**: [PROJ]
**Status**: {status:colour=Blue|title=Planning}
**Owner**: @projectowner
**Sponsor**: @sponsor
**Start Date**: [DD/MM/YYYY]
**Target End Date**: [DD/MM/YYYY]
{panel}

## Executive Summary
[2-3 paragraphs summarizing the project purpose, scope, and expected outcomes]

## Business Case

### Problem Statement
[Describe the problem or opportunity]

### Objectives
1. [SMART Objective 1]
2. [SMART Objective 2]
3. [SMART Objective 3]

### Success Criteria
{info}
**Definition of Success**:
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]
{info}

## Scope

### In Scope
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

### Out of Scope
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

## Stakeholders

| Name | Role | Responsibility | Influence |
|------|------|----------------|-----------|
| @user1 | Sponsor | Funding & approval | High |
| @user2 | PM | Day-to-day management | High |
| @user3 | Tech Lead | Technical direction | Medium |

**RACI Matrix**: [Link to detailed RACI]

## Timeline & Milestones

{timeline}
| Phase | Start | End | Deliverables |
|-------|-------|-----|--------------|
| Discovery | DD/MM | DD/MM | Requirements doc |
| Design | DD/MM | DD/MM | Design specs |
| Development | DD/MM | DD/MM | MVP |
| Testing | DD/MM | DD/MM | Test report |
| Launch | DD/MM | DD/MM | Production release |
{timeline}

## Budget
**Total Budget**: $XXX,XXX

| Category | Estimated Cost | Notes |
|----------|----------------|-------|
| Personnel | $XX,XXX | FTE allocation |
| Software/Tools | $XX,XXX | Licenses & subscriptions |
| External Services | $XX,XXX | Contractors, vendors |
| Contingency (10%) | $X,XXX | Risk buffer |

## Risks & Assumptions

### Top Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| [Risk 1] | Medium | High | [Mitigation strategy] |
| [Risk 2] | Low | High | [Mitigation strategy] |

### Assumptions
- [Critical assumption 1]
- [Critical assumption 2]

## Resources & Links
- [Jira Project](#)
- [Confluence Space](#)
- [Design Files](#)
- [Technical Docs](#)
```

### 3. Sprint Retrospective Template
```markdown
{panel:title=Sprint Retrospective|borderColor=#00875a}
**Sprint**: Sprint [Number]
**Sprint Dates**: [Start Date] - [End Date]
**Team**: [Team Name]
**Facilitator**: @facilitator
**Date**: {date}
{panel}

## Sprint Overview
**Sprint Goal**: [Sprint goal]
**Completed Stories**: [X/Y]
**Velocity**: [XX points]
**Carry Over**: [X stories]

## Ceremony: What Went Well? 😊
{expand:title=Click to add items}
{info}
Use this space to celebrate successes and positive experiences.
{info}

- [Positive item 1]
- [Positive item 2]
- [Positive item 3]
{expand}

## Ceremony: What Didn't Go Well? 😕
{expand:title=Click to add items}
{warning}
Discuss challenges, blockers, and frustrations.
{warning}

- [Challenge 1]
- [Challenge 2]
- [Challenge 3]
{expand}

## Ceremony: Ideas & Actions 💡
{expand:title=Click to add items}
{note}
Brainstorm improvements and define actionable next steps.
{note}

| Idea | Votes | Action Owner | Target Sprint |
|------|-------|--------------|---------------|
| [Improvement idea 1] | ⭐⭐⭐ | @owner | Sprint X+1 |
| [Improvement idea 2] | ⭐⭐ | @owner | Sprint X+2 |
{expand}

## Action Items (Committed)
{tasks}
- [ ] [Action 1 - High Priority] - @owner - Due: [Date]
- [ ] [Action 2 - Medium Priority] - @owner - Due: [Date]
- [ ] [Action 3 - Low Priority] - @owner - Due: [Date]
{tasks}

## Action Items from Previous Retro - Status Check
{panel:title=Previous Action Items}
| Action | Owner | Status | Notes |
|--------|-------|--------|-------|
| [Previous action 1] | @owner | {status:colour=Green|title=Done} | [Completion notes] |
| [Previous action 2] | @owner | {status:colour=Yellow|title=In Progress} | [Progress notes] |
{panel}

## Team Mood
{info}
Use emojis or numeric scale (1-10) to capture team sentiment.
{info}

**Overall Sprint Mood**: [😊 😐 😕]
**Team Energy**: [X/10]

## Next Retro
**Date**: [Next retro date]
**Focus**: [Special focus if any]
```

### 4. Product Requirements Document (PRD) Template
```markdown
{panel:title=PRD Overview|borderColor=#0052cc}
**Feature Name**: [Feature Name]
**PRD ID**: PRD-XXX
**Author**: @author
**Status**: {status:colour=Blue|title=Draft}
**Last Updated**: {date}
**Epic Link**: {jira:Epic Key}
{panel}

## Problem Statement
[Describe the user problem or business need. Answer: What problem are we solving and for whom?]

## Goals & Success Metrics

### Goals
1. [Primary goal]
2. [Secondary goal]

### Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| [Metric 1] | [Target value] | [How to measure] |
| [Metric 2] | [Target value] | [How to measure] |

## User Stories & Use Cases

### Primary User Story
**As a** [user type]
**I want** [capability]
**So that** [benefit]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Use Cases
1. **Use Case 1**: [Scenario name]
   - **Actor**: [User role]
   - **Preconditions**: [What must be true]
   - **Flow**: [Step-by-step]
   - **Postconditions**: [End state]

## Requirements

### Functional Requirements
| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-1 | [Requirement description] | Must Have | |
| FR-2 | [Requirement description] | Should Have | |
| FR-3 | [Requirement description] | Nice to Have | |

### Non-Functional Requirements
| ID | Requirement | Target | Notes |
|----|-------------|--------|-------|
| NFR-1 | Performance | <2s load time | |
| NFR-2 | Scalability | 10K concurrent users | |
| NFR-3 | Availability | 99.9% uptime | |

## Design & User Experience

### User Flow
[Insert diagram or link to design files]

### Wireframes/Mockups
[Embed images or link to Figma]

### UI Specifications
- [Key UI element 1]
- [Key UI element 2]

## Technical Considerations

### Architecture
[High-level architecture overview or diagram]

### Dependencies
- [System dependency 1]
- [Service dependency 2]
- [Third-party integration]

### Technical Constraints
- [Constraint 1]
- [Constraint 2]

## Release Plan

### Phases
| Phase | Features | Target Date | Status |
|-------|----------|-------------|--------|
| MVP (v1.0) | [Core features] | [Date] | {status:colour=Blue|title=Planned} |
| v1.1 | [Additional features] | [Date] | {status:colour=Gray|title=Future} |

### Rollout Strategy
[Describe rollout approach: beta, phased, full launch]

## Open Questions
{warning}
- [ ] [Question 1 requiring resolution]
- [ ] [Question 2 requiring resolution]
{warning}

## Appendix
- [Related Documents](#)
- [Research & Data](#)
- [Competitive Analysis](#)
```

### 5. Decision Log Template
```markdown
{panel:title=Decision Record|borderColor=#ff5630}
**Decision ID**: [PROJ]-DEC-[XXX]
**Date**: {date}
**Status**: {status:colour=Green|title=Approved}
**Decision Maker**: @decisionmaker
**Stakeholders**: @stakeholder1, @stakeholder2
{panel}

## Context & Background
[Provide background on what led to this decision. Include relevant history, constraints, and why a decision is needed now.]

## Problem Statement
[Clearly articulate the problem or question that requires a decision]

## Options Considered

### Option 1: [Option Name]
**Description**: [Detailed description]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Cost/Effort**: [Estimate]

### Option 2: [Option Name]
**Description**: [Detailed description]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Cost/Effort**: [Estimate]

### Option 3: [Option Name]
[Continue pattern]

## Decision Matrix
| Criteria | Weight | Option 1 | Option 2 | Option 3 |
|----------|--------|----------|----------|----------|
| Cost | 30% | 7/10 | 5/10 | 8/10 |
| Time to Implement | 25% | 6/10 | 9/10 | 5/10 |
| Scalability | 25% | 8/10 | 6/10 | 9/10 |
| Risk | 20% | 7/10 | 8/10 | 5/10 |
| **Total Score** | | **X.X** | **Y.Y** | **Z.Z** |

## Decision
{info}
**Chosen Option**: [Option X]

**Rationale**: [Explain why this option was selected. Reference the decision matrix and key factors.]
{info}

## Consequences & Trade-offs
**Positive Consequences**:
- [Expected benefit 1]
- [Expected benefit 2]

**Negative Consequences/Trade-offs**:
- [Known limitation 1]
- [Known limitation 2]

**Mitigation Plans**:
- [How to address limitation 1]

## Implementation Plan
{tasks}
- [ ] [Implementation step 1] - @owner - [Date]
- [ ] [Implementation step 2] - @owner - [Date]
- [ ] [Implementation step 3] - @owner - [Date]
{tasks}

## Success Criteria
[How will we know if this decision was the right one?]
- [Metric/outcome 1]
- [Metric/outcome 2]

## Review Date
**Scheduled Review**: [Date to revisit this decision]

## Related Decisions
- [Link to related decision 1]
- [Link to related decision 2]

## References
- [Supporting document 1]
- [Research/data source]
```

## references/jira-templates.md

# Jira Templates Library

Read this when you need a ready-to-use Jira issue description template (User Story, Bug Report, or Epic). Paste into the issue description field and fill the bracketed placeholders.

### 1. User Story Template
```
**As a** [type of user]
**I want** [capability or goal]
**So that** [benefit or value]

## Acceptance Criteria
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

## Design
[Link to design files, wireframes, or mockups]

## Technical Notes
[Any technical considerations, dependencies, or constraints]

## Definition of Done
- [ ] Code reviewed and approved
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] QA approved
- [ ] Deployed to production

## Related Stories
[Links to related issues, epics, or dependencies]
```

### 2. Bug Report Template
```
## Summary
[Brief, clear summary of the bug]

## Environment
- **Browser/Device**: [e.g., Chrome 118, iOS 17, Android 13]
- **OS**: [e.g., Windows 11, macOS 14]
- **App Version**: [e.g., v2.3.1]
- **User Type**: [e.g., Admin, End User]

## Steps to Reproduce
1. [First step]
2. [Second step]
3. [Third step]
4. [Observe issue]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Screenshots/Videos
[Attach or link to visual evidence]

## Impact
- **Severity**: [Critical / High / Medium / Low]
- **Affected Users**: [Percentage or user count]
- **Workaround**: [If available]

## Additional Context
[Any other relevant information, logs, error messages]

## Related Issues
[Links to similar bugs or related features]
```

### 3. Epic Template
```
## Vision
[High-level description of what this epic aims to achieve and why it matters]

## Goals
1. [Primary goal]
2. [Secondary goal]
3. [Tertiary goal]

## Success Metrics
| Metric | Target | How to Measure |
|--------|--------|----------------|
| [Metric 1] | [Value] | [Method] |
| [Metric 2] | [Value] | [Method] |

## User Stories (Breakdown)
- [ ] [User story 1] - [PROJ-XXX]
- [ ] [User story 2] - [PROJ-XXX]
- [ ] [User story 3] - [PROJ-XXX]

## Dependencies
- [Dependency 1]
- [Dependency 2]

## Timeline
**Target Start**: [Date]
**Target Completion**: [Date]

## Risks
- [Risk 1]
- [Risk 2]

## Related Epics
[Links to related epics]

## Resources
- [PRD Link]
- [Design Files]
- [Technical Specs]
```

## references/red-flags.md

# Red Flags: Atlassian Templates

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them. Pair with the SKILL.md and Troubleshooting table.

## How to use this document

When you have just designed a Confluence page template, Jira issue template, or blueprint for org-wide use, scan the red flags below before publishing it. Each red flag shows a *bad* and *good* version of the same artifact.

---

## Red Flag 1: Template Sprawl (a Template per Use Case)

**Symptom.** The org has 60+ Confluence templates, including "PRD v1", "PRD v2", "PRD - mobile", "PRD - copy of PRD v2 for that one project", and so on.

**Why it's bad.** Template sprawl is the documentation equivalent of permission scheme bloat. Authors cannot find the right template; the wrong template gets used; outdated templates remain in circulation forever. The fix is a small set of canonical templates with parameterized sections, not a template per variation.

**Bad example:**
> "Templates in space: 64 templates including 7 PRD variants, 5 RFC variants, 4 release-notes formats, and 12 retrospective templates."

**Good example:**
> "8 canonical templates, each with parameterized sections. PRD template includes optional sections (mobile, enterprise, AI). Template owners listed. Quarterly review removes unused templates."

**How to catch it.** Count templates per space. More than 15 per top-level space is sprawl.

---

## Red Flag 2: Fields Nobody Fills In

**Symptom.** The template has 40 fields. In practice, 25 of them are left blank or filled in with "TBD" or "N/A".

**Why it's bad.** Required fields nobody fills in train users to ignore the template. Optional fields nobody fills in are dead weight that clutters the page. The signal-to-noise ratio drops; future authors copy the bad pattern.

**Bad example:**
> "Bug report template: 18 fields including 'Browser', 'OS', 'Carrier', 'Time of day', 'Mood when bug occurred'. 70% of fields blank in the last 200 reports."

**Good example:**
> "Bug report template: 6 required fields (summary, steps to reproduce, expected, actual, environment, version). Optional 'attachments' field. Quarterly review of fill-rate; fields under 40% fill-rate are deprecated."

**How to catch it.** Measure fill rate per field across the last 50 uses. Any field below 50% fill is a candidate for removal or making it optional.

---

## Red Flag 3: Template with No Owner

**Symptom.** The template was created by someone who left the company. No one knows what it is for or whether it should still be used.

**Why it's bad.** Unowned templates rot. Examples become stale, instructions reference removed features, and there is no one to update them when frameworks change. The library erodes one orphaned template at a time.

**Bad example:**
> "Confluence template 'Quarterly Planning Doc' last edited 2022. Author: ex-employee. 47 pages created from it in 2025."

**Good example:**
> "Every template has a named owner (single-threaded). Owner reviews quarterly: still in use? still accurate? Updated 2026-02. If owner unidentified for 60 days, template archived."

**How to catch it.** Audit template metadata. Any template without a current employee as owner is a red flag.

---

## Red Flag 4: Instructions Buried Inside the Template

**Symptom.** The template body has the instructions ("Replace this section with your goals", "Delete this if not applicable") and authors forget to remove them. Final published pages contain the scaffolding text.

**Why it's bad.** Instructional text in the template becomes published content, which is embarrassing and signals lack of care. Worse, readers cannot distinguish guidance from content.

**Bad example:**
> Published PRD says: "**Goals:** [Replace this with 3-5 SMART goals for the feature. See PM guide for SMART criteria.] We want to improve onboarding."

**Good example:**
> Template uses Confluence info-panel macro for instructions, set to "hide on view." Author guidance is in a separate page (`/templates/prd-author-guide`) linked from the template description. Final published page contains only content.

**How to catch it.** Spot-check the last 20 pages created from the template. If any contain template instruction text, the template is broken.

---

## Red Flag 5: Linked Issues / Smart Macros That Break Silently

**Symptom.** Template includes a Jira-issues macro tied to a hardcoded JQL filter, or a page-properties report referencing a label that no one uses. Pages render with empty results.

**Why it's bad.** Authors copy the template and get a blank macro. They do not know whether it is broken or whether there is just no data. The macro becomes invisible noise.

**Bad example:**
> "Status page template embeds Jira filter `project = OLDPROJ AND status = 'In Progress'`. Project OLDPROJ archived 8 months ago. All status pages show empty issue list."

**Good example:**
> "Status page template uses a parameter (page-property) for project key. Macro guides author with placeholder text 'Set page-property `jira-project` to your project key'. Quarterly broken-macro audit via Confluence REST API."

**How to catch it.** Render the template into a sample page. Every macro should display real content or a clear "configure me" prompt — never silently empty.

---

## Red Flag 6: Version Drift across Templates

**Symptom.** PRD template was updated in March, but the RFC, post-mortem, and quarterly-planning templates still reference the old PRD section names. Documents stop cross-linking cleanly.

**Why it's bad.** Templates are an ecosystem. A change in one ripples to others; if updates are not coordinated, the library decays. Authors learn that "the templates do not match each other" and lose trust.

**Bad example:**
> "PRD template renamed 'Success Metrics' to 'Outcomes'. Retro template still asks 'did we hit the PRD's Success Metrics?'. Authors confused; some answer the old, some the new."

**Good example:**
> "Templates ship with a `template-version` page property. Cross-references use the property, not hard-coded names. Quarterly cross-template audit confirms consistency. Major changes communicated via template-release notes."

**How to catch it.** Search the template library for shared terms. Any term that means different things in different templates is drift.

---

## Red Flag 7: Template That Replicates Tribal Knowledge Instead of Encoding It

**Symptom.** The template has empty sections ("Strategy", "Risks", "Resourcing") with no prompts, no examples, no rubrics. Authors who do not already know how to fill it out produce poor pages.

**Why it's bad.** A good template is a thinking tool. It encodes the framework the author should use. Empty section headers are just paperwork.

**Bad example:**
> Template section: "**Risks:** [Add risks here.]"

**Good example:**
> Template section: "**Risks:** Use the Pre-Mortem framework — Tigers (real risks with evidence), Paper Tigers (sound risky but unlikely), Elephants (large but acceptable). For each Tiger, name owner and mitigation. See `/templates/risks-author-guide`. Example below.\n\n[Example: 'Tiger: payment provider has 99.5% SLA; launch-day traffic spike likely. Owner: platform. Mitigation: pre-warm capacity, fall-back provider configured.']"

**How to catch it.** For each section, ask: would a new joiner know how to fill this out? If not, add a prompt and an example.

---

## Red Flag 8: Templates That Lock Authors into a Single Workflow

**Symptom.** PRD template assumes a Scrum delivery model with story points; Kanban teams cannot use it. Or the post-mortem template assumes a blameful "root cause" model.

**Why it's bad.** A template that hard-codes one methodology forces all teams onto that methodology, or forces them to deviate from the template (defeating standardization). Templates should encode *outputs*, not *methodologies*.

**Bad example:**
> PRD template includes "Story points for each user story (Fibonacci 1, 2, 3, 5, 8, 13)". Kanban team using cycle-time cannot complete the section.

**Good example:**
> PRD template asks for "estimated size and timeline" with examples for story points, t-shirt sizing, or cycle-time forecasts. Methodology-neutral, output-focused.

**How to catch it.** List the templates' assumptions. Any assumption about delivery model, estimation method, or team structure should be optional or parameterized.

---

## Red Flag 9: No Template Adoption Metrics

**Symptom.** The team has spent weeks designing a new template. After launch, no one measures whether it is being used or whether quality improved.

**Why it's bad.** Template design is product work. Templates that are not measured may not be used; templates that are used may not be helping. Without metrics, you cannot iterate.

**Bad example:**
> "We rolled out the new PRD template last quarter. Hope teams are using it."

**Good example:**
> "PRD template adoption: 78% of new PRDs (target 90% by Q3). Quality leading indicators: % with measurable success metric (62% -> 84%), % with named risks (40% -> 71%). Author feedback survey quarterly."

**How to catch it.** Every template launch should declare a target adoption rate and at least one quality indicator measurable from page content.

---

## Red Flag 10: Templates Coupled to Specific People or Tools that Change

**Symptom.** Template includes hardcoded references to a specific tool ("Paste your Mixpanel dashboard URL here"), specific person ("Submit for review to Jane Doe"), or specific Slack channel that has since been renamed.

**Why it's bad.** Templates outlive specific tools and individuals. Hardcoded references rot. Authors copy stale instructions and produce broken pages.

**Bad example:**
> "PRD template: 'Get review approval from Jane Doe in #product-reviews Slack channel.'"

**Good example:**
> "PRD template: 'Get review approval from the PM Director (see /org-chart). Post in the product-reviews channel.' Org-chart and channel referenced by directory entry, not name."

**How to catch it.** Search templates for proper nouns (people, tools, channels). Each is a future failure point.

---

## Red Flag 11: Required Fields That Should Be Optional

**Symptom.** Every PRD must fill out "Competitive Analysis" — even internal tools with no competitive landscape. Authors fabricate content or leave it as "N/A".

**Why it's bad.** Mandatory-everywhere fields train authors to fill in junk. The signal value of "Competitive Analysis" drops to zero when half the answers are "N/A".

**Bad example:**
> PRD template requires Competitive Analysis. Internal-tool PRD says: "Competitors: N/A, we are the only internal tool."

**Good example:**
> PRD template has Competitive Analysis as a conditional section: "Required for customer-facing features. Omit for internal tools." Template guidance explains when to include.

**How to catch it.** For each required section, ask: would 80%+ of users have meaningful content here? If not, make it conditional.

---

## Red Flag 12: Template Library with No Discovery Surface

**Symptom.** Templates exist in a Confluence space, but nobody knows they exist. New PMs ask in Slack "what's the PRD template?" and get pointed to a personal page.

**Why it's bad.** Templates only work if authors can find them. A library without discovery is just a backup. Adoption is bounded by surface area.

**Bad example:**
> "Templates are in the 'Templates' Confluence space." (Space has no landing page, no index, not pinned, not linked from team handbooks.)

**Good example:**
> "Template catalog page: indexed by use case (PRDs, RFCs, retros, status, incident, planning). Each template has a 1-line description, owner, last-updated date. Linked from team handbook, onboarding pages, and Jira issue-create panels."

**How to catch it.** Ask 3 people in different teams: "where do you find the [X] template?" If you get 3 different answers, the discovery surface is broken.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Template Sprawl | Fewer than ~15 templates per space? |
| 2 | Fields Nobody Fills In | Each field above 50% fill rate? |
| 3 | Template with No Owner | Every template owned by a current employee? |
| 4 | Instructions Buried Inline | Instructions hidden on view, not part of content? |
| 5 | Broken Smart Macros | Macros parameterized, never silently empty? |
| 6 | Version Drift | Cross-references use page properties, not names? |
| 7 | Empty Section Headers | Every section has prompt + example? |
| 8 | Single Methodology Locked In | Outputs parameterized, not methodology? |
| 9 | No Adoption Metrics | Target adoption + quality indicator measured? |
| 10 | Hardcoded People/Tools | No proper nouns; use directory entries? |
| 11 | Required Should Be Optional | 80%+ of authors have real content for required sections? |
| 12 | No Discovery Surface | 3 random people find the template the same way? |

## Related Reading

- SKILL.md Troubleshooting section (for symptom -> root cause -> resolution)
- references/template-library-governance.md (if present)
- atlassian-admin/references/red-flags.md (for org-wide governance patterns)

## references/troubleshooting.md

# Troubleshooting & Success Criteria

Read this when a deployed template is misbehaving (low adoption, broken macros, version confusion, stale data) or when you need the measurable bar for "this skill did its job."

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| Users create pages from scratch instead of using templates | Templates not discoverable, or template names are unclear | Pin templates to space sidebar; use descriptive names (e.g., "Sprint Retro - Team Template"); send periodic reminders with usage links |
| Template produces inconsistent output across teams | Template has too many free-text sections without guidance; teams interpret placeholders differently | Add inline instructions within placeholders; provide a completed example alongside the blank template; standardize section headings |
| Confluence macros in templates break after product updates | Atlassian deprecated or renamed macros in a platform update | Subscribe to Atlassian release notes; test templates in sandbox after major updates; maintain a macro compatibility checklist |
| Template versioning creates confusion about which version to use | Multiple versions coexist without clear deprecation; naming does not indicate version | Use version suffix in template name (e.g., "PRD Template v2.1"); archive old versions immediately after migration; add deprecation banner to old templates |
| Jira issue templates do not apply consistently | Template applied at wrong level (project vs. issue type), or default values overridden by workflow post-functions | Verify template scope matches intended issue type and project; check for conflicting automation rules or post-functions |
| Template adoption rate is low despite training | Templates add friction rather than reducing it; too many required fields | Simplify templates to the minimum viable structure; make optional sections collapsible; gather user feedback and iterate quarterly |
| Dynamic macros (Jira queries, charts) show stale data | JQL filter references incorrect project, or cache settings are too aggressive | Verify JQL in each dynamic macro; adjust cache refresh intervals; test macros after any project key or filter changes |

## Success Criteria

- Template adoption rate exceeds 70% for targeted content types (measured by pages created from templates vs. blank pages)
- New template requests are evaluated and deployed within 10 business days
- All active templates have documented usage instructions and at least one completed example
- Template satisfaction score (from quarterly user survey) averages 4+/5
- Zero active templates older than 12 months without a documented review
- Template-created content passes quality checklist at 85%+ rate on first use
- Deprecated templates are archived within 30 days of replacement deployment

## references/workflows-and-governance.md

# Workflows, Governance & MCP Integration

Read this when you need the full step-by-step processes for creating, modifying, or governing templates — plus handoff protocols, best practices, and Atlassian MCP operations.

## Workflows

### Template Creation Process
1. **Discover**: Interview stakeholders to understand needs
2. **Analyze**: Review existing content patterns
3. **Design**: Create template structure and placeholders
4. **Implement**: Build template with macros and formatting
5. **Test**: Validate with sample data
6. **Document**: Create usage instructions
7. **Publish**: Deploy to appropriate space/project
8. **Train**: Educate users on template usage
9. **Monitor**: Track adoption and gather feedback
10. **Iterate**: Refine based on usage

### Template Modification Process
1. **Assess**: Review change request and impact
2. **Version**: Create new version, keep old available
3. **Modify**: Update template structure/content
4. **Test**: Validate changes don't break existing usage
5. **Migrate**: Provide migration path for existing content
6. **Communicate**: Announce changes to users
7. **Support**: Assist users with migration
8. **Archive**: Deprecate old version after transition

### Blueprint Development
1. Define blueprint scope and purpose
2. Design multi-page structure
3. Create page templates for each section
4. Configure page creation rules
5. Add dynamic content (Jira queries, user data)
6. Test blueprint creation flow
7. **HANDOFF TO**: Atlassian Admin for global deployment

## Best Practices

### Template Design Principles
**Clarity**: Use clear section headers and instructions
**Consistency**: Maintain visual and structural consistency
**Completeness**: Include all necessary sections
**Flexibility**: Allow customization where appropriate
**Guidance**: Provide inline instructions and examples

### Macro Usage Guidelines
**Dynamic Content**: Use macros for auto-updating content (dates, user mentions, Jira queries)
**Visual Hierarchy**: Use panels, infos, and notes to create visual distinction
**Interactivity**: Use expand macros for collapsible sections
**Integration**: Embed Jira charts and tables for live data

### Template Maintenance
**Version Control**: Track template versions and changes
**Deprecation**: Clearly mark outdated templates
**Documentation**: Maintain usage guides for each template
**Feedback Loop**: Regularly gather user feedback and iterate

## Handoff Protocols

**FROM Senior PM**:
- Template requirements for projects
- Reporting template needs
- Executive summary formats
- Portfolio tracking templates

**TO Senior PM**:
- Completed templates ready for use
- Template usage analytics
- Suggestions for new templates
- Template optimization opportunities

**FROM Scrum Master**:
- Sprint ceremony template needs
- Team-specific template requests
- Retrospective format preferences
- Sprint planning layouts

**TO Scrum Master**:
- Sprint-ready templates
- Team documentation templates
- Agile ceremony structures
- Velocity tracking templates

**FROM Jira Expert**:
- Issue template requirements
- Custom field display needs
- Workflow-specific templates
- Reporting template requests

**TO Jira Expert**:
- Issue description templates
- Field configuration templates
- Workflow documentation
- JQL query templates

**FROM Confluence Expert**:
- Space-specific template needs
- Global template requests
- Blueprint requirements
- Macro-based templates

**TO Confluence Expert**:
- Configured page templates
- Blueprint structures
- Template deployment plans
- Usage guidelines

**FROM Atlassian Admin**:
- Org-wide template standards
- Global template deployment
- Template governance requirements
- Compliance templates

**TO Atlassian Admin**:
- Global templates for approval
- Template usage reports
- Template compliance status
- Recommendations for standards

## Template Governance

**Creation Process**:
1. Request and justification
2. Design and review
3. Testing with pilot users
4. Documentation
5. Approval
6. Deployment
7. Training
8. Monitoring

**Review Cycle**:
- Templates reviewed quarterly
- Usage metrics analyzed
- Feedback incorporated
- Updates deployed
- Deprecated templates archived

**Quality Standards**:
- All templates documented
- Clear usage instructions
- Example content provided
- Tested before deployment
- Version controlled
- Feedback mechanism in place

## Atlassian MCP Integration

**Primary Tools**: Atlassian Rovo MCP Server (Atlassian's official remote MCP server for Cloud; endpoint `https://mcp.atlassian.com/v2/mcp`). See Atlassian's [supported tools](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/) list (as of September 2026).

**Template Operations**:
- Read existing Confluence templates -- `listConfluenceTemplates`, `getConfluenceTemplate`
- Create pages from template content -- `createConfluenceContent` (check `getContentFormatGuide` for body format)
- Pre-fill Jira issue descriptions from templates -- `createJiraIssue`, `editJiraIssue`
- Build automated template deployment scripts (Confluence/Jira REST API -- creating or editing templates themselves is not an MCP tool)
- Version control template content

**Integration Points**:
- Support all roles with standardized templates
- Enable Confluence Expert with deployable templates
- Provide Jira Expert with issue templates
- Supply Senior PM with reporting templates
- Give Scrum Master sprint ceremony templates

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/atlassian-templates -->
