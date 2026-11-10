# confluence-expert

> **Use these instructions for this whole conversation.** Apply them when: Designs and audits Confluence spaces: page trees, labels, permissions, page ownership and stale content. Use when setting up or restructuring a space, a wiki has gone stale or duplicated, or labels are a mess.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Atlassian Confluence Expert

Master-level expertise in Confluence space management, documentation architecture, content creation, macros, templates, and collaborative knowledge management.

## Core Capabilities

- **Space architecture** — design space hierarchies, organize knowledge by team/project/topic, implement taxonomies, configure permissions and visibility
- **Content creation** — structured pages with layouts, dynamic macros, reusable templates, version control and change tracking
- **Collaboration & governance** — documentation practices, review/approval workflows, content lifecycle management, documentation standards
- **Integration & automation** — link Confluence with Jira, embed dynamic Jira reports, configure watchers/notifications, content automation

## When to Use

- Standing up or restructuring a space and its page hierarchy
- Designing templates (meeting notes, project overview, decision log, retro)
- Setting content governance: review cycles, archiving, quality standards
- Embedding Jira issues, charts, or reports inside Confluence pages
- Defining or auditing space permission schemes
- Driving documentation strategy and knowledge-base health

## Clarify First

Confluence advice depends most on which Confluence the user runs and how much of it they can change. Settle the inputs below before producing anything. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Cloud or Data Center, and plan tier:** Cloud plan tiers set storage limits that matter for attachment-heavy spaces, and page-view and contributor analytics need Premium or a marketplace app. Data Center reaches end of life on 28 Mar 2029, so a restructure there should be planned around the Cloud migration.
- **Permission level:** A space admin can change the page tree, space templates and space permissions. Org-wide templates, blueprints, global automation and cross-space permissions belong to `atlassian-admin/`, and space settings cannot override stricter org-wide security policies. The user's rights decide whether you deliver a change they can make or a request for their admin.
- **New space or existing one:** A new space can get the right page tree from the start. An existing space needs its current tree or a page export first, because moving pages between spaces can break internal links, and `space_structure_analyzer.py`, `content_health_auditor.py` and `label_taxonomy_analyzer.py` all work from such an export.
- **What the space is for:** A team workspace, an operational space of runbooks and a published knowledge base need different hierarchies, permissions and review cadences. Operational pages need a named owner and a review date; a scratch team space can be looser.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Workflow

1. Settle the Clarify First inputs and get a page export of the space (or the planned tree for a new one).
2. Run the three tools below on the export to measure structure, content health and labels before proposing changes.
3. Design the target tree, ownership and review cadence from `references/confluence-playbook.md`; check it against `references/red-flags.md`.
4. Done when the re-run on the restructured export shows no root sprawl, every operational page has an owner, and no top topic has duplicate pages.

## Tools

Each tool reads one JSON export and prints a text report (`--json` for machine output).
`--example` prints the input shape; samples ship in `assets/`. Exit 0 on success, 2 on bad
input (missing file, invalid JSON, wrong shape) with a one-line error.

```bash
python3 scripts/space_structure_analyzer.py --space assets/sample_space.json
python3 scripts/content_health_auditor.py --pages assets/sample_pages.json
python3 scripts/label_taxonomy_analyzer.py --labels assets/sample_labels.json
```

| Tool | What it does |
|------|--------------|
| `space_structure_analyzer.py` | Depth distribution, root-page count, short and duplicate titles; structure score |
| `content_health_auditor.py` | Per-page score for stale (>12 months) or aging (>6 months), orphaned, ownerless and unlabelled pages. Age is measured from the export's `as_of`, else its newest `last_updated` |
| `label_taxonomy_analyzer.py` | Label coverage, top and single-use labels, case conflicts (`Engineering` vs `engineering`), labels with spaces or underscores |

Template design and template governance belong to `atlassian-templates`; this skill decides where pages and templates live in a space.

## Anti-Patterns

### Flat space with no hierarchy
**Mistake:** Hundreds of pages sit at the root of one space, and nobody knows where new content goes.
**Why it happens:** Creating a page at the top level is the default, and nobody owns the structure.
**Instead:** Design the page tree before content piles up. If the space root has more than about 15 pages, regroup them under parent pages by team, project or topic.

### Pages with no owner or review date
**Mistake:** Pages carry no owner and no "last reviewed" date, so stale content stays live.
**Why it happens:** Writing the page feels like the end of the job.
**Instead:** Give every page in an operational space a named owner and a review date, and set a review cadence. A runbook that pages someone who left two years ago is an outage waiting to happen.

### "Source of truth" with four versions
**Mistake:** The team calls Confluence its source of truth, but one topic has four pages that disagree.
**Why it happens:** Writing a new page is easier than finding and fixing the old one.
**Instead:** For your top 10 most-searched topics, keep exactly one canonical page. Merge or archive the duplicates and link them to the canonical page.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/confluence-playbook.md](references/confluence-playbook.md)** — full detail behind this map: competencies, workflows (space creation, page architecture, documentation strategy, KB management), macro syntax, page layouts, inline template examples, permission schemes, content governance, decision/handoff protocols, analytics, troubleshooting table, and success criteria. Read when executing any Confluence task.
- **[references/templates.md](references/templates.md)** — ready-to-paste Confluence page templates (meeting notes, and more) with full markdown structure. Read when you need a complete template to drop into a space.
- **[references/red-flags.md](references/red-flags.md)** — common ways a space design, IA proposal, page template, or governance policy goes wrong, with bad/good examples. Read before shipping any Confluence artifact.

## Scope & Limitations

**In Scope:** Space creation and architecture, page hierarchy design, template creation and management, content governance (review cycles, archiving, quality standards), macro usage and dynamic content, documentation strategy, knowledge base management, Jira-Confluence integration, content analytics.

**Out of Scope:** Global Atlassian administration (hand off to `atlassian-admin/`), Jira project configuration (hand off to `jira-expert/`), template design and governance (hand off to `atlassian-templates/`), sprint execution artifacts (hand off to `scrum-master/`).

**Limitations:** Confluence Cloud has storage limits per plan tier that affect attachment-heavy spaces. Advanced analytics (page view trends, contributor activity) require Confluence Premium or marketplace apps. Space-level permissions cannot override more restrictive org-wide security policies set by `atlassian-admin/`. Content migration between spaces can break internal links and require manual fixup. Confluence Data Center reaches end of life on 28 Mar 2029 (read-only; no new/expanded DC licenses after 30 Mar 2028) -- plan space restructuring around a Cloud migration rather than on DC ([timeline](https://www.atlassian.com/licensing/data-center-end-of-life); see `atlassian-admin/`).

## Files

| File | Purpose |
|------|---------|
| `scripts/space_structure_analyzer.py`, `scripts/content_health_auditor.py`, `scripts/label_taxonomy_analyzer.py` | See Tools |
| `assets/sample_space.json`, `assets/sample_pages.json`, `assets/sample_labels.json` | Runnable inputs for each tool |
| `references/*.md` | See References |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/confluence-playbook.md

# Confluence Expert Playbook

> Read this when you need the full detail behind the SKILL.md map — competencies, workflows, macro syntax, page layouts, inline template examples, permissions, governance, decision/handoff protocols, analytics, troubleshooting, and success criteria.

## Core Competencies (detail)

**Space Architecture**
- Design and create space hierarchies
- Organize knowledge by teams, projects, or topics
- Implement documentation taxonomies
- Configure space permissions and visibility

**Content Creation**
- Create structured pages with layouts
- Use macros for dynamic content
- Build templates for consistency
- Implement version control and change tracking

**Collaboration & Governance**
- Facilitate team documentation practices
- Implement review and approval workflows
- Manage content lifecycle
- Establish documentation standards

**Integration & Automation**
- Link Confluence with Jira
- Embed dynamic Jira reports
- Configure page watchers and notifications
- Set up content automation

## Workflows

### Space Creation
1. Determine space type (Team, Project, Knowledge Base, Personal)
2. Create space with clear name and description
3. Set space homepage with overview
4. Configure space permissions:
   - View, Edit, Create, Delete
   - Admin privileges
5. Create initial page tree structure
6. Add space shortcuts for navigation
7. **HANDOFF TO**: Teams for content population

### Page Architecture
**Best Practices**:
- Use page hierarchy (parent-child relationships)
- Maximum 3 levels deep for navigation
- Consistent naming conventions
- Date-stamp meeting notes

**Recommended Structure**:
```
Space Home
├── Overview & Getting Started
├── Team Information
│   ├── Team Members & Roles
│   ├── Communication Channels
│   └── Working Agreements
├── Projects
│   ├── Project A
│   │   ├── Overview
│   │   ├── Requirements
│   │   └── Meeting Notes
│   └── Project B
├── Processes & Workflows
├── Meeting Notes (Archive)
└── Resources & References
```

### Template Creation
1. Identify repeatable content pattern
2. Create page with structure and placeholders
3. Add instructions in placeholders
4. Format with appropriate macros
5. Save as template
6. Share with space or make global
7. **USE**: References for advanced template patterns

### Documentation Strategy
1. **Assess** current documentation state
2. **Define** documentation goals and audience
3. **Organize** content taxonomy and structure
4. **Create** templates and guidelines
5. **Migrate** existing documentation
6. **Train** teams on best practices
7. **Monitor** usage and adoption
8. **REPORT TO**: Senior PM on documentation health

### Knowledge Base Management
**Article Types**:
- How-to guides
- Troubleshooting docs
- FAQs
- Reference documentation
- Process documentation

**Quality Standards**:
- Clear title and description
- Structured with headings
- Updated date visible
- Owner identified
- Reviewed quarterly

## Essential Macros

### Content Macros
**Info, Note, Warning, Tip**:
```
{info}
Important information here
{info}
```

**Expand**:
```
{expand:title=Click to expand}
Hidden content here
{expand}
```

**Table of Contents**:
```
{toc:maxLevel=3}
```

**Excerpt & Excerpt Include**:
```
{excerpt}
Reusable content
{excerpt}

{excerpt-include:Page Name}
```

### Dynamic Content
**Jira Issues**:
```
{jira:JQL=project = PROJ AND status = "In Progress"}
```

**Jira Chart**:
```
{jirachart:type=pie|jql=project = PROJ|statType=statuses}
```

**Recently Updated**:
```
{recently-updated:spaces=@all|max=10}
```

**Content by Label**:
```
{contentbylabel:label=meeting-notes|maxResults=20}
```

### Collaboration Macros
**Status**:
```
{status:colour=Green|title=Approved}
```

**Task List**:
```
{tasks}
- [ ] Task 1
- [x] Task 2 completed
{tasks}
```

**User Mention**:
```
@username
```

**Date**:
```
{date:format=dd MMM yyyy}
```

## Page Layouts & Formatting

**Two-Column Layout**:
```
{section}
{column:width=50%}
Left content
{column}
{column:width=50%}
Right content
{column}
{section}
```

**Panel**:
```
{panel:title=Panel Title|borderColor=#ccc}
Panel content
{panel}
```

**Code Block**:
```
{code:javascript}
const example = "code here";
{code}
```

## Templates Library

### Meeting Notes Template
```
**Date**: {date}
**Attendees**: @user1, @user2
**Facilitator**: @facilitator

## Agenda
1. Topic 1
2. Topic 2

## Discussion
- Key point 1
- Key point 2

## Decisions
{info}Decision 1{info}

## Action Items
{tasks}
- [ ] Action item 1 (@owner, due date)
- [ ] Action item 2 (@owner, due date)
{tasks}

## Next Steps
- Next meeting date
```

### Project Overview Template
```
{panel:title=Project Quick Facts}
**Status**: {status:colour=Green|title=Active}
**Owner**: @owner
**Start Date**: DD/MM/YYYY
**End Date**: DD/MM/YYYY
**Budget**: $XXX,XXX
{panel}

## Executive Summary
Brief project description

## Objectives
1. Objective 1
2. Objective 2

## Key Stakeholders
| Name | Role | Responsibility |
|------|------|----------------|
| @user | PM | Overall delivery |

## Milestones
{jira:project=PROJ AND type=Epic}

## Risks & Issues
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Risk 1 | High | Action plan |

## Resources
- [Design Docs](#)
- [Technical Specs](#)
```

### Decision Log Template
```
**Decision ID**: PROJ-DEC-001
**Date**: {date}
**Status**: {status:colour=Green|title=Approved}
**Decision Maker**: @decisionmaker

## Context
Background and problem statement

## Options Considered
1. Option A
   - Pros:
   - Cons:
2. Option B
   - Pros:
   - Cons:

## Decision
Chosen option and rationale

## Consequences
Expected outcomes and impacts

## Next Steps
- [ ] Action 1
- [ ] Action 2
```

### Sprint Retrospective Template
```
**Sprint**: Sprint XX
**Date**: {date}
**Team**: Team Name

## What Went Well
{info}
- Positive item 1
- Positive item 2
{info}

## What Didn't Go Well
{warning}
- Challenge 1
- Challenge 2
{warning}

## Action Items
{tasks}
- [ ] Improvement 1 (@owner)
- [ ] Improvement 2 (@owner)
{tasks}

## Metrics
**Velocity**: XX points
**Completed Stories**: X/X
**Bugs Found**: X
```

## Space Permissions

### Permission Levels
- **View**: Read-only access
- **Edit**: Modify existing pages
- **Create**: Add new pages
- **Delete**: Remove pages
- **Admin**: Full space control

### Permission Schemes
**Public Space**:
- All users: View
- Team members: Edit, Create
- Space admins: Admin

**Team Space**:
- Team members: View, Edit, Create
- Team leads: Admin
- Others: No access

**Project Space**:
- Stakeholders: View
- Project team: Edit, Create
- PM: Admin

## Content Governance

**Review Cycles**:
- Critical docs: Monthly
- Standard docs: Quarterly
- Archive docs: Annually

**Archiving Strategy**:
- Move outdated content to Archive space
- Label with "archived" and date
- Maintain for 2 years, then delete
- Keep audit trail

**Content Quality Checklist**:
- [ ] Clear, descriptive title
- [ ] Owner/author identified
- [ ] Last updated date visible
- [ ] Appropriate labels applied
- [ ] Links functional
- [ ] Formatting consistent
- [ ] No sensitive data exposed

## Decision Framework

**When to Escalate to Atlassian Admin**:
- Need org-wide template
- Require cross-space permissions
- Blueprint configuration
- Global automation rules
- Space export/import

**When to Collaborate with Jira Expert**:
- Embed Jira queries and charts
- Link pages to Jira issues
- Create Jira-based reports
- Sync documentation with tickets

**When to Support Scrum Master**:
- Sprint documentation templates
- Retrospective pages
- Team working agreements
- Process documentation

**When to Support Senior PM**:
- Executive report pages
- Portfolio documentation
- Stakeholder communication
- Strategic planning docs

## Handoff Protocols

**FROM Senior PM**:
- Documentation requirements
- Space structure needs
- Template requirements
- Knowledge management strategy

**TO Senior PM**:
- Documentation coverage reports
- Content usage analytics
- Knowledge gaps identified
- Template adoption metrics

**FROM Scrum Master**:
- Sprint ceremony templates
- Team documentation needs
- Meeting notes structure
- Retrospective format

**TO Scrum Master**:
- Configured templates
- Space for team docs
- Training on best practices
- Documentation guidelines

**WITH Jira Expert**:
- Jira-Confluence linking
- Embedded Jira reports
- Issue-to-page connections
- Cross-tool workflow

## Best Practices

**Writing Style**:
- Use active voice
- Write scannable content (headings, bullets, short paragraphs)
- Include visuals and diagrams
- Provide examples
- Keep language simple and clear

**Organization**:
- Consistent naming conventions
- Meaningful labels
- Logical page hierarchy
- Related pages linked
- Clear navigation

**Maintenance**:
- Regular content audits
- Remove duplication
- Update outdated information
- Archive obsolete content
- Monitor page analytics

## Analytics & Metrics

**Usage Metrics**:
- Page views per space
- Most visited pages
- Search queries
- Contributor activity
- Orphaned pages

**Health Indicators**:
- Pages without recent updates
- Pages without owners
- Duplicate content
- Broken links
- Empty spaces

## Atlassian MCP Integration

**Primary Tool**: Atlassian Rovo MCP Server (Atlassian's official remote MCP server for Cloud; endpoint `https://mcp.atlassian.com/v2/mcp`). Tool names below are from Atlassian's [supported tools](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/) list as of September 2026 -- re-check it, the list changes.

**Key Operations** (Confluence tools):
- Create and manage spaces -- `createConfluenceSpace`, `listConfluenceSpaces`, `getConfluenceSpace`
- Create and update pages (and other content types) -- `createConfluenceContent`, `updateConfluenceContent`
- Manage page hierarchies -- `moveConfluenceContent`, `copyConfluenceContent`, `archiveConfluenceContent`
- Read templates -- `listConfluenceTemplates`, `getConfluenceTemplate`
- Configure page permissions and restrictions -- `addConfluenceContentPermissions`, `setConfluenceContentRestrictionState`
- Search content with CQL -- `searchConfluence`
- Extract documentation for analysis -- `getConfluenceContent`, `exportConfluenceContent`, `getContentFormatGuide` (body format rules)

**Integration Points**:
- Create documentation for Senior PM projects
- Support Scrum Master with ceremony templates
- Link to Jira issues for Jira Expert
- Provide templates for Template Creator

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| Users cannot find existing documentation | Poor space/page hierarchy, missing labels, or unclear page titles | Restructure to max 3 levels deep; enforce descriptive naming conventions; add labels to all pages and use `contentbylabel` macro for discovery |
| Confluence search returns irrelevant results | Page titles are generic, content lacks keywords, or spaces have too many orphaned pages | Use specific, descriptive titles; add excerpt macros for search snippets; audit and remove orphaned pages quarterly |
| Pages become stale with outdated information | No content ownership model, no review cadence, or no visible "last updated" date | Assign a page owner to every active page; set quarterly review reminders; add `{date}` macro to show last update prominently |
| Space permissions are too permissive or too restrictive | Ad-hoc permission changes without a governance model; individual permissions used instead of groups | Reset to group-based permissions; define 3-4 standard permission schemes; audit permissions quarterly |
| Jira macros embedded in pages show errors or no data | JQL references deleted projects, or the viewer lacks Jira permissions for the referenced project | Verify JQL validity; ensure Confluence viewers also have Jira browse permissions for referenced projects |
| Content duplication across multiple spaces | No single source of truth policy; teams copy content instead of linking | Implement excerpt-include pattern for shared content; establish content ownership map; use cross-space linking instead of copying |
| Page tree becomes too deep (>5 levels) creating navigation fatigue | Organic growth without architectural review; no archiving strategy | Flatten hierarchy to max 3 levels; archive completed project pages; use labels and search instead of deep nesting |

## Success Criteria

- 90%+ of active pages have a designated owner and a review date within the past 6 months
- Orphaned pages (no parent, no links, no views in 90 days) represent less than 5% of total content
- New team members can find onboarding documentation within 3 clicks from the space homepage
- Content duplication rate stays below 10% (measured by duplicate title or excerpt analysis)
- All spaces follow the standardized page architecture template (overview, team info, projects, processes, resources)
- Confluence adoption measured by monthly active editors exceeds 60% of licensed users
- Knowledge base articles resolve 40%+ of common questions without escalation to a person

## references/red-flags.md

# Red Flags: Confluence Expert

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them. Pair with the SKILL.md and Troubleshooting table.

## How to use this document

When you have just produced a Confluence space design, IA proposal, page template, or governance policy, scan the red flags below. Each red flag shows a *bad* and *good* version of the same artifact.

---

## Red Flag 1: Information-Architecture Chaos (Flat Spaces with 800+ Pages)

**Symptom.** A single space has 800 top-level pages and no hierarchy. Search returns 40 results for any common term. Nobody knows where to put new content.

**Why it's bad.** Confluence is a hierarchical wiki by design. A flat space defeats the navigation tree, breaks page-tree macros, and turns every search into a needle-in-haystack exercise. Users start writing in personal spaces because the main space is unusable.

**Bad example:**
> Engineering space: 1,200 pages, 947 at root level. Mixed: meeting notes, RFCs, runbooks, onboarding, OKRs, retros.

**Good example:**
> Engineering space, 5-section IA: (1) /Strategy (OKRs, roadmap), (2) /Practices (runbooks, on-call), (3) /Projects (one branch per project), (4) /People (onboarding, growth), (5) /Archive. Each section has an owner, a page-tree macro on the landing page, and a retention policy."

**How to catch it.** Open the space tree. If the root has more than ~15 pages, you have IA chaos.

---

## Red Flag 2: Orphan Pages (No Inbound Links, No Parent)

**Symptom.** 30% of pages in a space have zero inbound links and are not children of any indexed page. They exist but are not findable except by URL.

**Why it's bad.** Orphan pages cannot be discovered, so their content is invisible. Worse, they often contain critical info (a forgotten policy, a half-finished design doc) that someone reinvented later because they could not find the original.

**Bad example:**
> Space audit: 2,400 pages total. 720 (30%) orphan — no inbound links, no parent. Half are "draft" pages from 2-3 years ago.

**Good example:**
> Quarterly orphan-page audit run via REST API. Orphans either (a) re-parented and linked, (b) archived to /Archive with date label, or (c) deleted with stakeholder confirmation. Current orphan rate <5%."

**How to catch it.** Use the Confluence REST API or a community macro to list orphans. Anything above 10% is unhealthy.

---

## Red Flag 3: Documentation Treated as Storage, Not Communication

**Symptom.** Pages exist but are wall-of-text dumps with no structure, no summary, no audience identification. Readers cannot find the answer in 30 seconds.

**Why it's bad.** Confluence content competes with Slack threads and human memory. A page that takes 10 minutes to skim loses to a 1-minute Slack search. Pages must be skimmable: TL;DR, headings, structured tables.

**Bad example:**
> Page "Deployment Process": 2,400 words, single block of text, no headings, no TL;DR. Last updated 2023.

**Good example:**
> Page "Deployment Process": 1-paragraph TL;DR, audience banner ("for: on-call engineers"), table of common scenarios, expandable sections for edge cases. Last reviewed banner: 2026-04. Owner named."

**How to catch it.** Open any page. Can a reader find the key info in 30 seconds? If not, the page is storage, not communication.

---

## Red Flag 4: No Page Ownership or Review Cadence

**Symptom.** Pages have no owner field, no "last reviewed" date, no review cadence. Stale info accumulates indefinitely.

**Why it's bad.** Documentation rots. Without a named owner and review cadence, pages drift from reality and become liabilities — readers act on stale info and cause incidents. The runbook that says "page Jane on-call" when Jane left two years ago is a real outage waiting to happen.

**Bad example:**
> Runbook page last edited 2022. No owner. References old infrastructure (no longer in production).

**Good example:**
> Every page in /Practices has page properties: `owner`, `last-reviewed`, `review-cadence` (quarterly/annual). Page-properties report on space landing page surfaces stale pages. Pages overdue for review get a banner."

**How to catch it.** Does every page in your operational spaces have owner + review date? If not, content rot is invisible.

---

## Red Flag 5: Permissions Tangled at the Page Level

**Symptom.** Space has space-level permissions, but 100+ pages have individual page-level restrictions on top. New users cannot see what they should; some users see things they shouldn't.

**Why it's bad.** Page-level permissions are a maintenance nightmare. They are not visible in space-permission audits, so access drift is silent. New employees inherit a permission patchwork that no one can fully explain.

**Bad example:**
> "We restrict sensitive pages individually. Currently 187 page-level restrictions across the space."

**Good example:**
> "Sensitive content lives in a separate Restricted space with appropriate space-level permissions. Main space uses inheritance only. Page-level restrictions reserved for genuinely exceptional cases (<5 across the org), all logged."

**How to catch it.** Count page-level permission overrides. Above 20 in a space is excessive complexity.

---

## Red Flag 6: Jira-Confluence Drift (Macros Pointing to Dead Projects)

**Symptom.** Pages embed Jira-issues macros, status reports, and Jira filters. Many filter results render empty because projects were renamed or archived.

**Why it's bad.** Broken macros render as blank panels. Readers cannot tell if there is no work or if the macro is broken. Status pages stop being trustworthy.

**Bad example:**
> Quarterly status page: 6 embedded Jira filter macros. 3 return zero results because referenced projects archived. Page still says "Q1 Status: On Track."

**Good example:**
> Status page macros parameterized via page properties (jira-project-key). Annual macro-health audit via REST API. Empty results trigger a warning banner ('configure page property: jira-project-key')."

**How to catch it.** Open status/dashboard pages. Are macros displaying real content or silently empty? Silent empties are bugs.

---

## Red Flag 7: Confluence as a Single Source of Truth without Defining "Truth"

**Symptom.** "Confluence is our source of truth" — but the same topic has 4 pages with conflicting info and no canonical pointer.

**Why it's bad.** Single source of truth (SSoT) is a discipline, not a slogan. If a topic has multiple pages, you do not have SSoT — you have redundancy and ambiguity. Readers find different pages and get different answers.

**Bad example:**
> Search "deployment process" returns 5 pages, all from different teams, all slightly contradicting. Each team thinks theirs is "the" page.

**Good example:**
> One canonical page per topic, with `canonical: true` page property. Other pages on the topic include a "Canonical reference: [link]" callout at the top, and exist only to extend, not duplicate. Cross-team review for new canonical pages."

**How to catch it.** For your top 10 most-searched topics, is there exactly one canonical page? If multiple, SSoT is fiction.

---

## Red Flag 8: Meeting Notes as Permanent Pages

**Symptom.** /Meeting Notes branch has 2,000+ pages. Search returns meeting notes for any product term, drowning out canonical content.

**Why it's bad.** Meeting notes are ephemeral. They should live in a dedicated subspace with retention policies, not pollute the main searchable corpus. The result of search becoming meeting-notes-noise is that nobody trusts search.

**Bad example:**
> /Engineering/Meeting Notes: 2,400 pages going back 4 years. Searching "rate limiter" returns 18 meeting notes mentioning it in passing.

**Good example:**
> /Engineering/Meeting Notes: separate space (excluded from default site search). Retention policy: archive after 90 days. Decisions extracted into canonical decision-log pages on the main space. Meeting notes link out to those decisions."

**How to catch it.** Search a common term. If meeting notes outnumber canonical content in results, your search is polluted.

---

## Red Flag 9: Templates Exist but Are Not Discoverable

**Symptom.** Space has 12 well-designed templates. New page creators click "Blank Page" because they do not know templates exist.

**Why it's bad.** Templates only help if they are used. A library nobody finds produces no quality lift. The template space needs landing pages, prompts at page-create time, and onboarding inclusion.

**Bad example:**
> Templates space exists. Adoption: 8% of new pages use a template.

**Good example:**
> Templates surfaced in the "Create Page" dialog by default. Template catalog page indexed by use case. Featured in onboarding. Adoption: 71% of new pages use a template. Quarterly review of template fit."

**How to catch it.** What percent of new pages in the last 30 days came from a template? Below 50% means templates are invisible.

---

## Red Flag 10: Mixing Personal Notes into Team Spaces

**Symptom.** Individuals create personal scratch pages in team spaces. Half-finished thoughts, draft questions, personal lists — all visible to the team and indexed in search.

**Why it's bad.** Personal notes in team spaces pollute the corpus. They lower the signal-to-noise of search and confuse readers ("is this a real plan or someone's brainstorm?"). Confluence has personal spaces for this; the team space should be clean.

**Bad example:**
> Engineering space contains pages like "Sarah's notes from her Monday review" and "Random ideas for retros."

**Good example:**
> Personal scratchwork lives in each user's personal Confluence space. Team space contains only canonical, owned content. Onboarding includes 'use your personal space for notes' guidance."

**How to catch it.** Sample 50 recent pages in a team space. Any that are explicitly personal-titled? If yes, the discipline is missing.

---

## Red Flag 11: No Archival Lifecycle

**Symptom.** Pages from 2018 still live in the active hierarchy alongside current pages. Nothing is archived; everything stays "live forever."

**Why it's bad.** Without archival, the space accumulates indefinitely. Search performance degrades; orphan rates climb; readers see stale content alongside current content. Confluence's `archive` feature exists for this reason but goes unused.

**Bad example:**
> Roadmap space: contains roadmap pages from 2018-2026, all in /Roadmaps, all in search results. Newest mixed with oldest.

**Good example:**
> Annual archival pass each January: anything older than 18 months and superseded gets `archive` flag. Archived pages remain searchable when filter applied but not in default search. Retention policy documented per space."

**How to catch it.** How many pages older than 24 months are in active hierarchy? If many, the lifecycle is broken.

---

## Red Flag 12: Page Titles That Do Not Describe Content

**Symptom.** Page titles like "Draft", "Working Doc", "Notes", "Untitled (1)". Search returns useless title matches.

**Why it's bad.** Search relevance depends on titles. Vague titles destroy findability. Confluence does not auto-rename when content evolves, so the placeholder title persists.

**Bad example:**
> Pages titled: "Draft", "Working", "Notes", "Brainstorm v3", "Untitled".

**Good example:**
> Style guide: page titles are noun phrases describing content. "Q3 Activation Strategy" not "Working". Onboarding includes title-style review. Bad titles flagged in monthly content audit."

**How to catch it.** Search "draft", "working", "notes", "untitled" in your space. Each hit is a title to rename.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | IA Chaos | Space root has ~15 or fewer pages? |
| 2 | Orphan Pages | Orphan rate under 10%? |
| 3 | Storage Not Communication | Key info findable in 30 seconds? |
| 4 | No Owner / Review Cadence | Operational pages have owner + review date? |
| 5 | Tangled Page Permissions | Page-level overrides under 20 per space? |
| 6 | Broken Jira Macros | Macros show content or clear "configure me" prompt? |
| 7 | Multiple "Sources of Truth" | One canonical page per top-10 topic? |
| 8 | Meeting Notes Polluting Search | Meeting notes in separate subspace, retention 90d? |
| 9 | Templates Not Discoverable | Template-based page creation above 50%? |
| 10 | Personal Notes in Team Space | Recent pages all canonical, none personal? |
| 11 | No Archival Lifecycle | Annual archive pass; old content not in active hierarchy? |
| 12 | Vague Page Titles | Search "draft/working/untitled" returns zero hits? |

## Related Reading

- SKILL.md Troubleshooting section (for symptom -> root cause -> resolution)
- references/space-architecture.md (for IA patterns, if present)
- atlassian-admin/references/red-flags.md (for org-wide governance)
- atlassian-templates/references/red-flags.md (for template library health)

## references/templates.md

# Confluence Page Templates

## Meeting Notes Template

```markdown
# [Meeting Title] - [Date]

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM - HH:MM]
**Location:** [Room/Video link]
**Attendees:** @[Name1], @[Name2], @[Name3]
**Note Taker:** @[Name]

## Agenda
1. [Topic 1]
2. [Topic 2]
3. [Topic 3]

## Discussion

### [Topic 1]
**Summary:**
[Key points discussed]

**Decisions:**
- [Decision 1]
- [Decision 2]

**Action Items:**
- [ ] [Action] - @[Owner] - [Due Date]
- [ ] [Action] - @[Owner] - [Due Date]

### [Topic 2]
**Summary:**
[Key points discussed]

**Decisions:**
- [Decision 1]

**Action Items:**
- [ ] [Action] - @[Owner] - [Due Date]

## Parking Lot
- [Item to discuss later]
- [Future topic]

## Next Meeting
**Date:** [YYYY-MM-DD]
**Agenda Topics:**
- [Topic 1]
- [Topic 2]
```

---

## Decision Log Template

```markdown
# [Decision Title]

| Field | Value |
|-------|-------|
| **Status** | 🟢 Accepted / 🟡 Proposed / 🔴 Deprecated |
| **Date** | [YYYY-MM-DD] |
| **Deciders** | @[Name1], @[Name2] |
| **Stakeholders** | @[Name3], @[Name4] |
| **Related Decisions** | [Link to related decisions] |

## Context and Problem Statement
[Describe the context and problem that requires a decision. 2-3 paragraphs explaining:
- What situation led to this decision?
- What problem are we trying to solve?
- What constraints exist?]

## Decision
[Clearly state the decision made in 1-2 sentences]

### Details
[Provide additional details about the decision:
- What exactly will we do?
- How will it be implemented?
- What timeline?]

## Rationale
[Explain why this decision was made:
- What were the key factors?
- What evidence supports this?
- Why is this the best choice?]

## Consequences

### Positive Consequences
- ✅ [Benefit 1]
- ✅ [Benefit 2]
- ✅ [Benefit 3]

### Negative Consequences / Trade-offs
- ⚠️ [Trade-off 1]
- ⚠️ [Trade-off 2]

### Risks
- 🔴 [Risk 1] - Mitigation: [How we'll handle it]
- 🟡 [Risk 2] - Mitigation: [How we'll handle it]

## Alternatives Considered

### Alternative 1: [Name]
**Description:** [What is this alternative?]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why Not Chosen:** [Reason]

### Alternative 2: [Name]
[Same structure as above]

## Implementation Plan
1. [Step 1] - @[Owner] - [Date]
2. [Step 2] - @[Owner] - [Date]
3. [Step 3] - @[Owner] - [Date]

## Success Metrics
- [Metric 1]: [Target]
- [Metric 2]: [Target]

## Review Date
**Next Review:** [YYYY-MM-DD]
**Review Notes:** [Link to review page]

## References
- [Link 1]
- [Link 2]
- [Link 3]

---
*Updated: [Date] by @[Name]*
```

---

## Technical Specification Template

```markdown
# [Feature/Component Name] Technical Specification

| Field | Value |
|-------|-------|
| **Status** | 🟡 Draft / 🟢 Approved / 🔴 Archived |
| **Author** | @[Name] |
| **Reviewers** | @[Name1], @[Name2] |
| **Date Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **JIRA Epic** | [ABC-123](link) |

## Overview
[1-2 paragraph summary of what this spec covers and why it matters]

## Goals and Non-Goals

### Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

### Non-Goals (Out of Scope)
- [Non-goal 1]
- [Non-goal 2]

## Background
[Context needed to understand this spec:
- What problem are we solving?
- What's the current state?
- Why now?]

## High-Level Design

### Architecture Diagram
[Insert diagram here]

### System Components
1. **[Component 1 Name]**
   - Purpose: [What it does]
   - Technology: [What it uses]
   - Interfaces: [How it connects]

2. **[Component 2 Name]**
   - Purpose: [What it does]
   - Technology: [What it uses]
   - Interfaces: [How it connects]

### Data Flow
[Describe how data flows through the system]

## Detailed Design

### Component 1: [Name]
**Purpose:** [Detailed purpose]

**Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

**API/Interface:**
```
[API spec or interface definition]
```

**Data Model:**
```
[Schema or data structure]
```

**Key Algorithms/Logic:**
[Describe any complex logic]

### Component 2: [Name]
[Same structure as Component 1]

## Database Schema

### Table: [table_name]
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| name | VARCHAR(255) | NOT NULL | Entity name |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |

### Indexes
- `idx_name` on `name` - For fast lookups
- `idx_created` on `created_at` - For temporal queries

## API Specification

### Endpoint: [Method] /api/path
**Purpose:** [What this endpoint does]

**Request:**
```json
{
  "param1": "value",
  "param2": 123
}
```

**Response:**
```json
{
  "result": "success",
  "data": {}
}
```

**Error Handling:**
- 400: [Reason]
- 404: [Reason]
- 500: [Reason]

## Security Considerations
- [Security consideration 1]
- [Security consideration 2]
- [Authentication/Authorization approach]
- [Data encryption requirements]

## Performance Considerations
- [Expected load/throughput]
- [Scalability approach]
- [Caching strategy]
- [Performance targets]

## Testing Strategy

### Unit Tests
- [Test area 1]
- [Test area 2]

### Integration Tests
- [Test scenario 1]
- [Test scenario 2]

### Performance Tests
- [Load test plan]
- [Performance benchmarks]

## Deployment Plan
1. [Deployment step 1]
2. [Deployment step 2]
3. [Deployment step 3]

### Rollback Plan
[How to revert if issues occur]

## Monitoring and Alerting
- [Metric 1] - Alert threshold: [Value]
- [Metric 2] - Alert threshold: [Value]
- [Log tracking]

## Migration Plan (if applicable)
[How to migrate from current system]

## Dependencies
- [Dependency 1] - Why needed
- [Dependency 2] - Why needed

## Open Questions
- [ ] [Question 1] - @[Owner]
- [ ] [Question 2] - @[Owner]

## Future Considerations
- [Future enhancement 1]
- [Future enhancement 2]

## References
- [Link to related specs]
- [Link to design docs]
- [Link to JIRA epics]

---
*For questions, contact @[Author]*
```

---

## How-To Guide Template

```markdown
# How to [Task Name]

## Overview
[1-2 sentences explaining what this guide covers and who it's for]

**Estimated Time:** [X minutes]
**Difficulty:** [Beginner/Intermediate/Advanced]

## Prerequisites
Before you begin, ensure you have:
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]
- [ ] [Prerequisite 3]

## Quick Summary (TL;DR)
[One paragraph with the essence of the guide for those who just need a reminder]

## Step-by-Step Instructions

### Step 1: [Action]
[Detailed description of what to do]

**Commands/Code:**
```bash
command here
```

**Expected Result:**
[What you should see if it worked]

**Screenshot:**
[Add screenshot if helpful]

### Step 2: [Action]
[Detailed description]

**Tips:**
- 💡 [Helpful tip]
- ⚠️ [Warning about common mistake]

### Step 3: [Action]
[Continue pattern...]

## Verification
To verify everything worked:
1. [Check 1]
2. [Check 2]

## Troubleshooting

### Problem: [Common issue]
**Symptoms:** [What you see]
**Cause:** [Why it happens]
**Solution:**
1. [Fix step 1]
2. [Fix step 2]

### Problem: [Another issue]
[Same structure as above]

## Best Practices
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

## Related Guides
- [Link to related guide 1]
- [Link to related guide 2]

## Need Help?
- Questions? Ask in #[channel]
- Issues? Create ticket in [JIRA project]
- Contact: @[Expert name]

---
*Last updated: [Date] by @[Name]*
```

---

## Requirements Document Template

```markdown
# [Feature/Project Name] Requirements

| Field | Value |
|-------|-------|
| **Status** | 🟡 Draft / 🟢 Approved / 🔵 In Progress / ✅ Complete |
| **Product Owner** | @[Name] |
| **Stakeholders** | @[Name1], @[Name2] |
| **Target Release** | [Release version] |
| **JIRA Epic** | [ABC-123](link) |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |

## Executive Summary
[2-3 sentences describing the feature and its business value]

## Business Goals
- [Goal 1]: [Metric]
- [Goal 2]: [Metric]
- [Goal 3]: [Metric]

## User Stories

### Story 1: [Title]
**As a** [user type]
**I want** [goal]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Priority:** [High/Medium/Low]
**Effort:** [Story points]

### Story 2: [Title]
[Same structure as Story 1]

## Functional Requirements

### FR-001: [Requirement Title]
**Description:** [What the system must do]

**Rationale:** [Why this is needed]

**Acceptance Criteria:**
- [Criterion 1]
- [Criterion 2]

**Priority:** [Must Have / Should Have / Could Have / Won't Have]

### FR-002: [Requirement Title]
[Same structure as FR-001]

## Non-Functional Requirements

### Performance
- [Requirement 1]
- [Requirement 2]

### Security
- [Requirement 1]
- [Requirement 2]

### Scalability
- [Requirement 1]
- [Requirement 2]

### Accessibility
- [Requirement 1]
- [Requirement 2]

## User Experience

### Wireframes
[Insert wireframes or link to Figma]

### User Flow
[Diagram showing user journey]

### UI Requirements
- [UI requirement 1]
- [UI requirement 2]

## Technical Constraints
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Dependencies
| Dependency | Owner | Status | Impact if Blocked |
|------------|-------|--------|-------------------|
| [Dep 1] | @[Name] | 🟢 Ready | [Impact] |
| [Dep 2] | @[Name] | 🟡 In Progress | [Impact] |

## Success Metrics
| Metric | Baseline | Target | How Measured |
|--------|----------|--------|--------------|
| [Metric 1] | [Current] | [Goal] | [Method] |
| [Metric 2] | [Current] | [Goal] | [Method] |

## Risks and Mitigations
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [Risk 1] | High | Medium | [Strategy] |
| [Risk 2] | Medium | Low | [Strategy] |

## Out of Scope
- [Explicitly excluded 1]
- [Explicitly excluded 2]

## Open Questions
- [ ] [Question 1] - @[Owner] - [Due date]
- [ ] [Question 2] - @[Owner] - [Due date]

## Timeline
| Phase | Start Date | End Date | Deliverables |
|-------|-----------|----------|--------------|
| Design | [Date] | [Date] | [Deliverable] |
| Development | [Date] | [Date] | [Deliverable] |
| Testing | [Date] | [Date] | [Deliverable] |
| Launch | [Date] | [Date] | [Deliverable] |

## Approval

### Reviewers
- [ ] Product Owner: @[Name]
- [ ] Engineering Lead: @[Name]
- [ ] Design Lead: @[Name]
- [ ] Stakeholder: @[Name]

**Approved Date:** [YYYY-MM-DD]

## References
- [Market research]
- [User feedback]
- [Technical specs]
- [Related features]

---
*For questions, contact @[Product Owner]*
```

---

## Retrospective Template

```markdown
# Sprint [N] Retrospective - [Team Name]

**Date:** [YYYY-MM-DD]
**Sprint:** [Sprint N]
**Sprint Dates:** [Start Date] - [End Date]
**Facilitator:** @[Name]
**Participants:** @[Name1], @[Name2], @[Name3]

## Sprint Metrics
- **Velocity:** [X points] (Average: [Y points])
- **Committed:** [X points / N issues]
- **Completed:** [Y points / M issues]
- **Sprint Goal Met:** ✅ Yes / ❌ No

## What Went Well 😊
- [Positive 1]
- [Positive 2]
- [Positive 3]

## What Didn't Go Well 😞
- [Challenge 1]
- [Challenge 2]
- [Challenge 3]

## Action Items from Last Retro
- [✅ / ❌] [Action item 1] - @[Owner]
  - Status: [Done / In Progress / Not Done]
  - Notes: [Update]
- [✅ / ❌] [Action item 2] - @[Owner]
  - Status: [Done / In Progress / Not Done]
  - Notes: [Update]

## Discussion Themes

### Theme 1: [Topic]
**What we discussed:**
[Summary of discussion]

**Root cause:**
[What's really causing this issue?]

**Ideas for improvement:**
- [Idea 1]
- [Idea 2]

### Theme 2: [Topic]
[Same structure as Theme 1]

## Action Items for Next Sprint
| Action | Owner | Due Date | Success Criteria |
|--------|-------|----------|------------------|
| [Action 1] | @[Name] | [Date] | [How we know it's done] |
| [Action 2] | @[Name] | [Date] | [How we know it's done] |
| [Action 3] | @[Name] | [Date] | [How we know it's done] |

## Shout-Outs 🎉
- @[Name] for [what they did]
- @[Name] for [what they did]

## Notes
[Any additional notes or observations]

---
*Next Retrospective: [Date]*
```

---

## Status Report Template

```markdown
# [Project Name] Status Report - [Week of Date]

**Report Date:** [YYYY-MM-DD]
**Reporting Period:** [Start Date] - [End Date]
**Project Manager:** @[Name]
**Overall Status:** 🟢 On Track / 🟡 At Risk / 🔴 Off Track

## Executive Summary
[2-3 sentences: What's the current state? What are the key achievements? What needs attention?]

## Project Health

| Metric | Status | Details |
|--------|--------|---------|
| **Scope** | 🟢 / 🟡 / 🔴 | [Comment] |
| **Schedule** | 🟢 / 🟡 / 🔴 | [Comment] |
| **Budget** | 🟢 / 🟡 / 🔴 | [Comment] |
| **Quality** | 🟢 / 🟡 / 🔴 | [Comment] |
| **Team Morale** | 🟢 / 🟡 / 🔴 | [Comment] |

## Key Accomplishments
- ✅ [Accomplishment 1]
- ✅ [Accomplishment 2]
- ✅ [Accomplishment 3]

## Milestones Status

| Milestone | Target Date | Status | Actual/Forecast | Notes |
|-----------|-------------|--------|-----------------|-------|
| [Milestone 1] | [Date] | ✅ Complete | [Date] | [Notes] |
| [Milestone 2] | [Date] | 🔄 In Progress | On track | [Notes] |
| [Milestone 3] | [Date] | ⏳ Not Started | [Forecast] | [Notes] |

## Active Risks

### 🔴 Critical Risks
| Risk | Impact | Mitigation | Owner | Status |
|------|--------|------------|-------|--------|
| [Risk 1] | High | [Strategy] | @[Name] | [Update] |

### 🟡 Medium Risks
| Risk | Impact | Mitigation | Owner | Status |
|------|--------|------------|-------|--------|
| [Risk 2] | Medium | [Strategy] | @[Name] | [Update] |

## Issues & Blockers

### 🚨 Blockers
- [Blocker 1] - @[Owner] - **Escalated to:** [Person]
  - Impact: [What's blocked]
  - ETA to resolve: [Date]

### ⚠️ Issues
- [Issue 1] - @[Owner]
  - Status: [Update]

## Upcoming in Next Period
- [Activity 1]
- [Activity 2]
- [Activity 3]

## Budget Update (if applicable)
- **Total Budget:** [Amount]
- **Spent to Date:** [Amount] ([%])
- **Forecast to Complete:** [Amount]
- **Variance:** [Amount] ([%])

## Decisions Needed
| Decision | Why Needed | Deadline | Stakeholder |
|----------|-----------|----------|-------------|
| [Decision 1] | [Reason] | [Date] | @[Name] |

## Team Update
- **Current Team Size:** [N people]
- **Open Positions:** [N] ([Roles])
- **Recent Additions:** @[Name] - [Role]
- **Upcoming Departures:** [Names/Dates]

## Metrics (if applicable)
| Metric | This Period | Last Period | Trend | Target |
|--------|-------------|-------------|-------|--------|
| [Metric 1] | [Value] | [Value] | ↗️ / ↘️ / → | [Target] |
| [Metric 2] | [Value] | [Value] | ↗️ / ↘️ / → | [Target] |

## Links
- [Jira Project](link)
- [Roadmap](link)
- [Technical Docs](link)

---
*Next Status Report: [Date]*
```

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/confluence-expert
