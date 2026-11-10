---
description: "Administers Linear teams, cycles, projects and triage, and writes GraphQL API calls. Use when setting up or fixing a Linear workspace, scripting bulk changes, or migrating from Jira to Linear."
---

# Linear Expert

Master-level expertise in Linear configuration, workflow design, GraphQL API mastery, Cycle and Project management, Initiative-level roadmaps, triage automation, GitHub integration, and migration from Jira. Covers everything from workspace setup to programmatic bulk operations against the Linear API.

## Overview

Linear is an opinionated, keyboard-driven issue tracker built around a strict data model (Team → Project → Issue → Sub-issue) and a GraphQL-only public API. Unlike Jira, Linear's strength is its lack of configurability: there is one workflow shape (Backlog → Unstarted → Started → Completed → Canceled), one priority scale (0-4), and a tight set of first-class concepts (Cycles, Projects, Initiatives, Labels, Milestones). The job of a Linear expert is to operate fluently inside those rails while extending the system through the API, automations, and integrations.

## Core Capabilities

- **Workspace & team configuration** — URL keys, SSO, team keys, cycle cadence, estimation scales, workflow states, label taxonomy
- **Planning hierarchy** — Cycles (sprints), Projects + Milestones, Initiatives, and Roadmap views
- **Triage automation** — inbound routing from Slack, support, GitHub Issues; daily triage SOP
- **GraphQL API mastery** — query/mutation authoring, pagination, batch mutations, webhooks, rate-limit hygiene
- **GitHub integration** — magic-word auto-link/auto-close, branch auto-linking, PR-state syncing
- **Bulk operations & migration** — API-driven bulk edits and Jira → Linear migration planning

## When to Use

- Setting up a new Linear workspace, team, or project from scratch
- Designing Cycle cadence, triage rules, and SLA workflows
- Writing GraphQL queries and mutations against the Linear API
- Configuring GitHub PR auto-link/auto-close and Slack notifications
- Building Initiative / Project / Milestone hierarchies for executive roadmaps
- Running bulk operations (relabel, retarget, reassign) across hundreds of issues
- Migrating an existing Jira instance to Linear without losing history
- Diagnosing why automations, sub-issues, or triage rules are not firing as expected

## Clarify First

Linear advice depends most on the user's plan, whether the work reads data or changes it, and where the workspace is starting from. Settle the inputs below before producing anything. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Plan:** The Free plan caps at 250 issues and 2 teams. Sub-initiatives and SAML/SCIM are Enterprise-only, and team initiatives need Business or Enterprise. A planning hierarchy or SSO setup that relies on these fails on a lower plan.
- **Read-only or writing through the API:** A GraphQL query changes nothing. Bulk mutations across hundreds of issues, webhook handlers and migration imports change shared data and are hard to undo, so they deserve a dry run on a small sample. API keys get 2,500 requests per hour per user and OAuth apps 5,000, which sets how a bulk job has to be batched.
- **Starting point:** A new workspace can follow `assets/linear-team-template.md`. An existing workspace needs its current teams, workflow states, labels and cycle cadence before you change them. A Jira migration needs a map from every Jira status to one of Linear's five workflow categories, and a decision on where each Jira custom field goes, since Linear has none.
- **Team count and size:** Cycle cadence, estimation scale, triage rotation and whether Initiatives are worth using all scale with the number of teams and people. A single team of five needs far less structure than ten teams reporting to an executive roadmap.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

Linear's API is GraphQL-only at `https://api.linear.app/graphql`; auth via personal API key (`Authorization: <key>`) or OAuth2.

```bash
# $1 = GraphQL document, $2 = variables as JSON (optional). jq builds the body, so quotes
# and newlines in the query are escaped correctly; pass values as variables, not by string splicing.
linear_query() {
  local vars="${2:-}"
  [ -z "$vars" ] && vars='{}'
  jq -n --arg q "$1" --argjson v "$vars" '{query: $q, variables: $v}' |
    curl -s -X POST https://api.linear.app/graphql \
      -H "Authorization: $LINEAR_API_KEY" \
      -H "Content-Type: application/json" \
      --data @-
}

linear_query 'query { viewer { id name } }'
linear_query 'query($id: String!) { issue(id: $id) { title state { name } } }' '{"id": "ENG-123"}'
```

Cache team/label/state UUIDs locally, use nested selection to avoid N+1 calls, and prefer webhooks over polling. See the references below for the full query catalog and operating workflows.

## Anti-Patterns

### Trusting unsigned webhooks
**Mistake:** A Linear webhook posts to an internal service that acts on the payload without checking where it came from.
**Why it happens:** The integration works in testing, and verification looks like optional hardening.
**Instead:** Validate the `Linear-Signature` header in every webhook handler before acting. Without it, anyone can forge or replay events that trigger deletions, status changes or notifications. Any handler that skips the check needs a security review now.

### Migrating from Jira without a status map
**Mistake:** Thousands of Jira issues are bulk-imported and every status lands in Backlog.
**Why it happens:** The importer runs without one, and mapping many Jira states onto Linear's five workflow categories takes work.
**Instead:** Write a table that maps each Jira status to a Linear state before you import (see `references/linear-vs-jira.md`). A migration plan with no status-mapping table is not ready to run.

### Letting Triage pile up
**Mistake:** The Triage queue holds hundreds of issues going back months.
**Why it happens:** Nobody owns Triage, so it only gets done when someone has spare time.
**Instead:** Staff Triage with a rotation and a daily routine (`assets/linear-triage-workflow.md`). If the queue passes 30 issues or the oldest is over 14 days old, add triage capacity.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## Reference Documentation

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/linear-concepts-and-workflows.md](references/linear-concepts-and-workflows.md)** — Linear data model, the 7 core workflows (setup, cycle/project planning, initiatives, triage, GitHub, bulk ops, Jira migration), best practices, and success criteria. Read when configuring a workspace or running any of the core operating workflows.
- **[references/linear-graphql-patterns.md](references/linear-graphql-patterns.md)** — canonical query and mutation catalog with variables, plus inline quick examples and CLI patterns. Read when authoring any GraphQL query/mutation or scripting against the API.
- **[references/linear-vs-jira.md](references/linear-vs-jira.md)** — concept-by-concept translation guide for teams migrating from Jira. Read before planning a Jira → Linear migration.
- **[references/red-flags.md](references/red-flags.md)** — common anti-patterns (cycle-as-sprint, project bloat, N+1, untriaged inbox, unsigned webhooks) plus the troubleshooting table. Read before applying config/queries to a team or when diagnosing failures.
- **[assets/linear-team-template.md](assets/linear-team-template.md)** — recommended new-team configuration. Read when standing up a new team.
- **[assets/linear-triage-workflow.md](assets/linear-triage-workflow.md)** — daily triage SOP and rotation template. Read when staffing or designing triage.
- Linear API docs: https://developers.linear.app/docs
- Linear GraphQL schema explorer: https://studio.apollographql.com/public/Linear-API/
- Linear method (workspace conventions): https://linear.app/method

## Scope & Limitations

**In Scope:** Linear workspace, team, and project configuration; cycle and project planning; Initiative and Roadmap hierarchy; triage workflow design; GitHub PR integration; GraphQL query and mutation authoring; bulk operations via API; webhook configuration; Jira → Linear migration planning and execution.

**Out of Scope:** Jira-side configuration and migration freeze (hand off to `jira-expert/`); Notion documentation pages for Linear roadmaps (hand off to `notion-pm/`); strategic prioritization and OKR setting (hand off to `senior-pm/`, `execution/brainstorm-okrs/`); sprint coaching and team health (hand off to `scrum-master/`); release notes generation from Linear issues (hand off to `execution/release-notes/`).

**Limitations:** Linear has no custom fields; all extension happens through labels, descriptions, or external systems. As of September 2026 the Free plan caps at 250 issues and 2 teams; Initiatives are on every plan, but sub-initiatives and SAML/SCIM are Enterprise-only and team initiatives need Business or Enterprise (verify on linear.app/pricing). API rate limits depend on auth type, not plan: API keys get 2,500 requests/hour per user, OAuth apps 5,000/hour, each with an hourly complexity budget; heavy automation may require coordination. Importers preserve most history but cannot recreate Jira's custom workflow states; mapping is many-to-five. GraphQL schema evolves continuously; pin client code to the deprecation calendar.

## Integration Points

| Integration | Direction | What Flows |
|---|---|---|
| `jira-expert/` | Jira → Linear | Migration mappings, custom-field translation, freeze coordination |
| `notion-pm/` | Linear → Notion | Roadmap embeds, Initiative pages, project status rollups |
| `execution/create-prd/` | PRD → Linear | PRD page becomes the Linear Project description; PRD sections become Milestones |
| `execution/brainstorm-okrs/` | OKR → Linear | Initiatives mapped to Objectives; Projects tagged with KR identifiers |
| `execution/outcome-roadmap/` | Roadmap → Linear | Outcome roadmap rows mapped to Linear Initiatives; outputs become Projects |
| `execution/release-notes/` | Linear → Release Notes | Closed issues in a cycle/project become release note line items |
| `execution/prioritization-frameworks/` | Scoring → Linear | RICE/WSJF scores written back to labels or description fields |
| `scrum-master/` | Linear → Analytics | Cycle data feeds velocity_analyzer.py and sprint_health_scorer.py |
| `senior-pm/` | Linear → Portfolio | Initiative-level rollups feed project_health_dashboard.py |
| `delivery-manager/` | Linear → Release | Project completion state and milestone dates feed release coordination |

## Files

Reference files are described under Reference Documentation above. Templates:

| File | Purpose |
|------|---------|
| `assets/linear-team-template.md` | Team setup template |
| `assets/linear-triage-workflow.md` | Triage workflow template |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/linear-concepts-and-workflows.md

# Linear Concepts & Workflows

> Read this when you need the Linear data model, the seven core operating workflows (setup, cycle/project planning, initiatives, triage, GitHub, bulk ops, Jira migration), best practices, or the success criteria for a healthy Linear workspace.

## Concepts

### Data Model

| Entity | Purpose | Key Fields |
|---|---|---|
| **Workspace** (Organization) | Top-level account, billing scope | `urlKey`, `name`, `samlEnabled` |
| **Team** | Permissions boundary, workflow owner, issue identifier prefix (e.g. `ENG`, `DESIGN`) | `key`, `cyclesEnabled`, `triageEnabled`, `defaultIssueState` |
| **Cycle** | Time-boxed iteration owned by one team (Linear's "sprint") | `number`, `startsAt`, `endsAt`, `progress`, `scopeHistory` |
| **Project** | Cross-functional body of work with a target date; spans one or more teams | `state` (planned/started/paused/completed/canceled), `targetDate`, `lead`, `teamIds` |
| **Initiative** | Strategic theme that groups Projects under a top-line outcome | `status`, `targetDate`, `owner`, `projects` |
| **Roadmap** | Saved view of Projects/Initiatives ordered by time | (UI construct, queried as filtered Project list) |
| **Issue** | The atomic unit of work | `identifier` (e.g. `ENG-123`), `state`, `priority`, `estimate`, `cycle`, `project`, `parent` |
| **Sub-issue** | Issue with `parent` set, rolls progress up | inherits team from parent |
| **Label** | Free-form tag; can be grouped into mutually-exclusive label groups | `color`, `parent` (for groups) |
| **Milestone** | Project-scoped checkpoint with a target date | `name`, `targetDate`, `sortOrder` |
| **Workflow State** | Per-team status; lives in one of 5 types | `type` (backlog/unstarted/started/completed/canceled/triage) |
| **Triage** | Special inbox state for unassigned/unscored incoming issues | enabled per-team via `triageEnabled` |

### Issue Identifier & Linear-Flavored Markdown

- Issues are referenced as `TEAMKEY-NUMBER` (e.g. `ENG-123`, `DSGN-47`). The number is workspace-unique within the team. Pasting an identifier in any Linear text field auto-resolves to a link with the issue title.
- **Mentions**: `@username` resolves against workspace members. `@team-name` mentions an entire team.
- **Priorities** map to numeric values: `0` No priority, `1` Urgent, `2` High, `3` Medium, `4` Low. Most UIs and the API accept the numeric value.
- **Markdown extensions**: standard CommonMark plus issue refs, mentions, task lists (`- [ ]`), and inline emoji shortcodes (`:rocket:`).
- **Code blocks** support fenced language tags; Linear renders syntax highlighting for ~30 languages.

## Core Workflows

### 1. Workspace and Team Setup

1. Create workspace; set URL key (immutable, used in all issue URLs).
2. Configure SSO/SAML if available on the plan tier.
3. Create the first Team with a meaningful 2-4 letter key (it appears in every issue ID forever).
4. Decide per-team:
   - **Cycles enabled?** Yes for shipping teams, no for triage-only/support teams.
   - **Cycle cadence**: typically 1-2 weeks, set the day-of-week start.
   - **Triage enabled?** Yes if external sources (Slack, support, GitHub Issues) create issues that need human routing.
   - **Estimation scale**: Exponential (0, 1, 2, 4, 8), Fibonacci, Linear (1-5), or T-shirt.
5. Customize workflow states (within the 5 allowed types). Common pattern: `Backlog → Todo → In Progress → In Review → Done → Canceled`.
6. Define core labels and label groups (e.g. group `area/*` with values `area/api`, `area/web`, `area/infra`).
7. **HANDOFF TO**: team leads for issue templates, automations, and GitHub install.

### 2. Cycle and Project Planning

**Cycle planning checklist** (run 1-2 days before cycle start):
1. Review the Cycle view: any issues without estimates, owners, or projects?
2. Pull issues from Backlog into Todo for the upcoming cycle.
3. Confirm cycle scope against the team's recent velocity (Linear shows median cycle velocity in Insights).
4. Set the cycle's auto-archive cadence (default: 6 completed cycles).

**Project planning**:
1. Create Project; assign Lead, target date, and member teams.
2. Add Milestones inside the project; order them.
3. Pull or create issues, assigning each to a milestone where useful.
4. Set Project status updates cadence (weekly is the default expectation).

### 3. Initiative and Roadmap Management

Initiatives are the top of Linear's hierarchy (Initiative → Project → Milestone → Issue).
1. Create an Initiative per strategic theme (e.g. "Self-Serve Onboarding Q3").
2. Attach 3-7 Projects per Initiative; more than 10 signals the Initiative is too broad.
3. Use the Roadmap view to visualize Initiatives and Projects on a quarterly timeline.
4. Owner posts an Initiative update at minimum monthly; the update appears in the Initiative feed and in any subscribed Slack channel.

### 4. Triage Workflow

Triage is Linear's inbox for issues that arrive without a workflow state. It's the right destination for Slack-created issues, customer support escalations, and inbound GitHub Issues.
1. Enable Triage on the receiving team.
2. Configure intake sources: GitHub Issues mirroring, Slack-to-Linear, customer request form, or API.
3. Establish a daily triage cadence (one person, ~15 minutes). For each triage item:
   - Confirm or reassign team.
   - Assign priority (Urgent/High/Medium/Low).
   - Assign owner or leave in `Todo` for cycle planning.
   - Attach project/milestone if it belongs to existing work.
   - Apply labels (`area/*`, `type/bug|feature|chore`).
4. **HANDOFF TO**: cycle planning for any items not closed during triage.

### 5. GitHub Integration

Linear's GitHub integration is bidirectional and the highest-leverage automation in the product.
1. Install the Linear GitHub app on the org; grant access to the relevant repos.
2. **Magic words in PR titles or descriptions** auto-link and auto-close:
   - `Fixes ENG-123`, `Closes ENG-123`, `Resolves ENG-123` move the issue to Done on PR merge.
   - `Part of ENG-123` or just `ENG-123` link without auto-close.
3. **Branch name auto-linking**: branches matching `<username>/eng-123-short-description` are auto-detected.
4. PR status changes update the issue state (Linear → In Review when PR opens; → Done when merged).
5. Configure per-team "GitHub repos" so only the relevant repos appear in the issue sidebar.

### 6. Bulk Operations

Bulk edits go through the API for anything beyond ~50 issues. Strategy:
1. Build a GraphQL query to fetch the issue IDs matching the criteria.
2. Loop in batches of 50; call `issueUpdate` mutation for each.
3. Rate limit (as of September 2026, per [Linear's rate-limiting docs](https://linear.app/developers/rate-limiting)): API keys get 2,500 requests / hour and 3,000,000 complexity points / hour per user; OAuth apps get 5,000 requests / hour and 2,000,000 complexity points / hour per user or app user; a single query may not exceed 10,000 complexity points. Limits are set by auth type, not by plan.
4. Always include an `--dry-run` mode in scripts; print the full list of issues that will change before mutating.
5. Use `issueBatchUpdate` mutation (where available) to update up to 100 issues per call.

### 7. Migration from Jira

Linear ships a first-party Jira importer that covers ~80% of cases. For the remaining 20%, plan a custom GraphQL-backed migration.
1. **Inventory Jira**: project count, custom fields, workflows, user count, issue count, attachment volume.
2. **Map concepts**:
   - Jira Project → Linear Team (often) or Linear Project (sometimes)
   - Jira Epic → Linear Project
   - Jira Initiative → Linear Initiative
   - Jira Sprint → Linear Cycle
   - Jira Subtask → Linear Sub-issue
   - Jira Components → Linear Labels (often in an `area/*` group)
3. **Decide on history**: Linear's importer preserves comments, attachments, status history, and assignees, but not custom field values verbatim (they map to labels or description text).
4. **Pilot with one Jira project** before mass migration. Validate identifiers, link integrity, and attachment downloads.
5. **Cut over**: freeze Jira writes, run final import, redirect all integrations (Slack, GitHub, CI) to Linear, archive Jira.
6. **HANDOFF TO**: `jira-expert/` for the Jira freeze and decommission plan.

## Best Practices

**Data quality**
- Enforce labels via team conventions (e.g. every issue must carry one `area/*` and one `type/*` label).
- Estimate every issue before it enters a cycle. Cycle velocity is meaningless if half the issues have null estimates.
- Use sub-issues for genuine parent-child decomposition; do not use them as a substitute for projects.

**Workflow discipline**
- Resist the urge to add a 7th or 8th workflow state. Linear's strength is the constrained model. If a team feels squeezed, the right move is usually a label, not a new state.
- Use the `Triage` state aggressively for any source that creates issues automatically; do not let bots write directly into `Todo`.

**Cycles and projects**
- Cycle scope set at planning time should drift no more than ~20% during the cycle; bigger drift is a signal of unclear acceptance criteria upstream.
- Projects without a target date are red flags; every project should have one even if approximate.

**API hygiene**
- Cache the team and label UUIDs your scripts use; never look them up by name on every call.
- Use webhooks instead of polling. Linear's webhook system covers nearly every entity.
- Respect rate limits; a rate-limited request returns HTTP 400 with a `RATELIMITED` error code in `errors[].extensions`. Back off until the time in `X-RateLimit-Requests-Reset` / `X-RateLimit-Complexity-Reset`.

**Governance**
- Restrict who can create teams (admins only on larger workspaces).
- Audit Initiatives quarterly; merge or close stale ones.
- Document the workspace's label taxonomy in a pinned issue or Notion page.

## Success Criteria

- All active teams have triage enabled (where applicable), a defined cycle cadence, and a standard label taxonomy
- 95%+ of issues entering a cycle carry an estimate, an owner, and a state-appropriate label
- Cycle velocity variance stays within 25% of the trailing 6-cycle median
- Every active Project has a Lead, a target date, and a status update within the last 14 days
- Initiatives have a clear owner and a monthly update; no Initiative carries more than 10 Projects
- GitHub PRs auto-close their linked Linear issues in 95%+ of merges
- API/automation scripts respect rate limits; no script triggers more than 5 `RATELIMITED` responses per day
- Jira-to-Linear migrations cut over with zero loss of comment history and 100% of identifiers redirected

## references/linear-graphql-patterns.md

# Linear GraphQL Patterns

Canonical GraphQL queries and mutations for the Linear API. Endpoint: `https://api.linear.app/graphql`. Auth: `Authorization: <personal-api-key>` or OAuth2 bearer token.

All queries below assume an HTTP POST with a JSON body of the shape:
```json
{ "query": "<graphql-string>", "variables": { ... } }
```

---

## 1. Discovery — IDs You Need First

Most mutations require UUIDs (teamId, stateId, labelId, projectId). Cache these locally; do not look them up by name on every call.

**Get team IDs and state IDs**:
```graphql
query Teams {
  teams(first: 50) {
    nodes {
      id
      key
      name
      states { nodes { id name type } }
      labels { nodes { id name parent { name } } }
    }
  }
}
```

**Get current user (whoami)**:
```graphql
query Me {
  viewer { id name email }
}
```

**Get workspace projects and initiatives**:
```graphql
query Portfolio {
  projects(first: 100, filter: { state: { in: ["started", "planned"] } }) {
    nodes { id name state targetDate lead { name } }
  }
  initiatives(first: 50) {
    nodes { id name status targetDate owner { name } projects { nodes { id name } } }
  }
}
```

---

## 2. Reading Issues

**Single issue by identifier**:
```graphql
query IssueByIdentifier($id: String!) {
  issue(id: $id) {
    identifier title description priority estimate
    state { name type }
    assignee { name }
    creator { name }
    project { name }
    cycle { number }
    labels { nodes { name } }
    children { nodes { identifier title state { name } } }
    comments { nodes { user { name } body createdAt } }
  }
}
```
Variables: `{ "id": "ENG-123" }` (Linear's `issue(id:)` accepts both UUID and the public identifier).

**List issues with a complex filter**:
```graphql
query OpenBugsInArea {
  issues(
    first: 100
    filter: {
      labels: { name: { in: ["type/bug", "area/auth"] } }
      state: { type: { in: [backlog, unstarted, started] } }
      priority: { lte: 2 }
    }
    orderBy: updatedAt
  ) {
    nodes { identifier title priority state { name } assignee { name } updatedAt }
  }
}
```

**Active cycle issues for a team**:
```graphql
query ActiveCycle($teamId: String!) {
  team(id: $teamId) {
    activeCycle {
      number startsAt endsAt
      issues(first: 250) {
        nodes { identifier title state { type } estimate assignee { name } }
      }
    }
  }
}
```

**Pagination loop**:
```graphql
query AllOpenIssues($after: String) {
  issues(
    first: 250
    after: $after
    filter: { state: { type: { neq: completed } } }
  ) {
    pageInfo { hasNextPage endCursor }
    nodes { id identifier title }
  }
}
```
Client loop: call repeatedly, passing `endCursor` as the next `after`, until `hasNextPage` is false.

---

## 3. Creating Issues

**Minimal issue create**:
```graphql
mutation CreateIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { id identifier url title }
  }
}
```
Variables:
```json
{
  "input": {
    "teamId": "<team-uuid>",
    "title": "Add SAML support",
    "description": "Customers on Enterprise need SAML 2.0.",
    "priority": 2,
    "estimate": 3,
    "labelIds": ["<label-uuid-area-auth>", "<label-uuid-type-feature>"],
    "projectId": "<project-uuid>",
    "assigneeId": "<user-uuid>"
  }
}
```

**Create a sub-issue**:
```graphql
mutation CreateSubIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { identifier parent { identifier } }
  }
}
```
Variables: add `"parentId": "<parent-issue-uuid>"` (the sub-issue inherits the parent's team).

**Create from triage** (issue lands in the Triage inbox; do not set `stateId`):
```graphql
mutation CreateTriageIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { identifier state { type } }
  }
}
```
Variables:
```json
{
  "input": {
    "teamId": "<team-with-triage-enabled>",
    "title": "Customer report: login loop on Safari",
    "description": "Repro: ... Customer: acme.com"
  }
}
```

---

## 4. Updating Issues

**Transition state**:
```graphql
mutation Transition($id: String!, $stateId: String!) {
  issueUpdate(id: $id, input: { stateId: $stateId }) {
    success
    issue { identifier state { name type } }
  }
}
```

**Reassign**:
```graphql
mutation Reassign($id: String!, $assigneeId: String!) {
  issueUpdate(id: $id, input: { assigneeId: $assigneeId }) {
    success
    issue { identifier assignee { name } }
  }
}
```

**Add a label** (Linear replaces the full label set; merge in client first):
```graphql
mutation Relabel($id: String!, $labelIds: [String!]!) {
  issueUpdate(id: $id, input: { labelIds: $labelIds }) {
    success
    issue { identifier labels { nodes { name } } }
  }
}
```

**Move to cycle**:
```graphql
mutation MoveToCycle($id: String!, $cycleId: String!) {
  issueUpdate(id: $id, input: { cycleId: $cycleId }) {
    success
    issue { identifier cycle { number } }
  }
}
```

**Attach to project + milestone**:
```graphql
mutation AttachProject($id: String!, $projectId: String!, $milestoneId: String!) {
  issueUpdate(id: $id, input: { projectId: $projectId, projectMilestoneId: $milestoneId }) {
    success
    issue { identifier project { name } projectMilestone { name } }
  }
}
```

---

## 5. Bulk Operations

**Batch update up to 100 issues per call**:
```graphql
mutation BatchPriority($ids: [String!]!, $priority: Int!) {
  issueBatchUpdate(ids: $ids, input: { priority: $priority }) {
    success
    issues { identifier priority }
  }
}
```

**Pattern for bulk relabel**:
1. Query the target issues, collect their `id` (UUID, not identifier) values.
2. Chunk into batches of 100.
3. Call `issueBatchUpdate` per batch.
4. Sleep 200ms between batches to stay well under rate limits.

---

## 6. Comments and Attachments

**Post a comment**:
```graphql
mutation Comment($input: CommentCreateInput!) {
  commentCreate(input: $input) {
    success
    comment { id body user { name } }
  }
}
```
Variables: `{ "input": { "issueId": "<uuid>", "body": "Repro confirmed on Safari 17." } }`.

**Attach a URL (e.g. GitHub PR, Figma frame, Notion page)**:
```graphql
mutation Attach($input: AttachmentCreateInput!) {
  attachmentCreate(input: $input) {
    success
    attachment { id title url }
  }
}
```
Variables:
```json
{
  "input": {
    "issueId": "<uuid>",
    "title": "PR #482",
    "url": "https://github.com/acme/web/pull/482",
    "iconUrl": "https://github.com/favicon.ico"
  }
}
```

---

## 7. Projects and Initiatives

**Create a project**:
```graphql
mutation CreateProject($input: ProjectCreateInput!) {
  projectCreate(input: $input) {
    success
    project { id name url }
  }
}
```
Variables:
```json
{
  "input": {
    "name": "Self-Serve Onboarding",
    "teamIds": ["<team-uuid>"],
    "leadId": "<user-uuid>",
    "targetDate": "2026-09-30",
    "state": "planned"
  }
}
```

**Post a project status update**:
```graphql
mutation ProjectUpdate($input: ProjectUpdateCreateInput!) {
  projectUpdateCreate(input: $input) {
    success
    projectUpdate { id body health }
  }
}
```
Variables:
```json
{
  "input": {
    "projectId": "<uuid>",
    "body": "Week 3: API spec signed off; web build starting.",
    "health": "onTrack"
  }
}
```

**Create an initiative and link projects**:
```graphql
mutation CreateInitiative($input: InitiativeCreateInput!) {
  initiativeCreate(input: $input) {
    success
    initiative { id name }
  }
}
```
Then attach projects via `initiativeToProjectCreate` for each project.

---

## 8. Webhooks

Webhook bodies arrive as JSON; validate `Linear-Signature` (HMAC-SHA256 of the raw body with your webhook secret).

Common event types:
- `Issue` — `create`, `update`, `remove`
- `Comment` — `create`, `update`, `remove`
- `Project`, `ProjectUpdate`, `Cycle`, `Reaction`, `IssueLabel`

Payload skeleton:
```json
{
  "action": "update",
  "type": "Issue",
  "data": { "id": "...", "identifier": "ENG-123", "title": "...", "state": { "name": "In Progress" } },
  "updatedFrom": { "stateId": "<previous-state-uuid>" },
  "url": "https://linear.app/acme/issue/ENG-123",
  "createdAt": "2026-05-21T12:00:00.000Z",
  "webhookId": "...",
  "webhookTimestamp": 1716292800000
}
```

Best practice: respond 2xx within 5 seconds; queue the work asynchronously.

---

## 9. Rate Limits

Limits depend on the authentication type, not the plan (as of September 2026; source: [linear.app/developers/rate-limiting](https://linear.app/developers/rate-limiting)):

| Auth type | Requests / hour | Complexity points / hour | Scope |
|---|---|---|---|
| API key | 2,500 | 3,000,000 | Per user |
| OAuth app | 5,000 | 2,000,000 | Per user or app user |
| Unauthenticated | 600 | 100,000 | Per IP address |

- A single query may not exceed 10,000 complexity points.
- Limits use a leaky bucket: tokens refill at a constant rate (limit / period), so a steady pace beats bursts.
- A rate-limited request returns HTTP 400 with the `RATELIMITED` error code in `errors[].extensions` (not a `429`). Read `X-RateLimit-Requests-Remaining` / `X-RateLimit-Requests-Reset` and `X-RateLimit-Complexity-Remaining` / `X-RateLimit-Complexity-Reset` (the cost of each query comes back in `X-Complexity`), and back off exponentially until the reset time.

For long-running scripts, prefer:
- Batched mutations (`issueBatchUpdate`) over per-issue loops.
- Webhooks over polling.
- Caching of IDs, label names, and state names.

---

## 10. Reference Mutations Cheatsheet

| Operation | Mutation |
|---|---|
| Create issue | `issueCreate(input: IssueCreateInput!)` |
| Update issue | `issueUpdate(id: String!, input: IssueUpdateInput!)` |
| Batch update | `issueBatchUpdate(ids: [String!]!, input: IssueUpdateInput!)` |
| Archive issue | `issueArchive(id: String!)` |
| Delete issue | `issueDelete(id: String!)` |
| Create comment | `commentCreate(input: CommentCreateInput!)` |
| Attach URL | `attachmentCreate(input: AttachmentCreateInput!)` |
| Create project | `projectCreate(input: ProjectCreateInput!)` |
| Project update | `projectUpdateCreate(input: ProjectUpdateCreateInput!)` |
| Create label | `issueLabelCreate(input: IssueLabelCreateInput!)` |
| Create cycle | `cycleCreate(input: CycleCreateInput!)` |
| Create initiative | `initiativeCreate(input: InitiativeCreateInput!)` |

Full schema: https://studio.apollographql.com/public/Linear-API/

---

## 11. Quick Inline Examples (from SKILL.md)

Linear's API is GraphQL-only, served at `https://api.linear.app/graphql`. Auth is via personal API key (`Authorization: <key>`) or OAuth2.

**List issues for a team in the active cycle**:
```graphql
query ActiveCycleIssues($teamKey: String!) {
  team(id: $teamKey) {
    activeCycle {
      issues(first: 100) {
        nodes {
          identifier
          title
          state { name type }
          assignee { name }
          priority
          estimate
        }
      }
    }
  }
}
```

**Create an issue**:
```graphql
mutation CreateIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { id identifier url }
  }
}
```
Variables:
```json
{
  "input": {
    "teamId": "team-uuid-here",
    "title": "Support TOTP for SSO logins",
    "description": "Customers on Enterprise plan want TOTP as a second factor.",
    "priority": 2,
    "labelIds": ["label-uuid-area-auth"],
    "projectId": "project-uuid-self-serve-q3"
  }
}
```

**Transition an issue to a new state**:
```graphql
mutation MoveIssue($id: String!, $stateId: String!) {
  issueUpdate(id: $id, input: { stateId: $stateId }) {
    success
    issue { identifier state { name } }
  }
}
```

**Find all open Urgent issues across the workspace**:
```graphql
query UrgentOpen {
  issues(
    filter: {
      priority: { eq: 1 }
      state: { type: { in: [backlog, unstarted, started] } }
    }
    first: 50
  ) {
    nodes { identifier title team { key } assignee { name } }
  }
}
```

**Paginate through a large result set**:
```graphql
query AllOpenIssues($after: String) {
  issues(first: 250, after: $after, filter: { state: { type: { neq: completed } } }) {
    pageInfo { hasNextPage endCursor }
    nodes { identifier title }
  }
}
```
Loop until `pageInfo.hasNextPage` is false, passing `endCursor` as the next `after`.

**Bulk update via batch mutation**:
```graphql
mutation BatchLabel($ids: [String!]!, $labelId: String!) {
  issueBatchUpdate(ids: $ids, input: { labelIds: [$labelId] }) {
    success
    issues { identifier }
  }
}
```

**Webhook payload shape** (for `Issue` events):
```json
{
  "action": "create",
  "type": "Issue",
  "data": { "id": "...", "identifier": "ENG-123", "title": "..." },
  "url": "https://linear.app/acme/issue/ENG-123",
  "createdAt": "2026-05-21T12:00:00.000Z",
  "webhookId": "...",
  "webhookTimestamp": 1716292800000
}
```
Always validate the `Linear-Signature` header against your webhook secret.

### CLI Patterns

Linear does not ship a first-party CLI, but several community CLIs exist; alternatively, a thin shell wrapper around `curl` plus GraphQL queries is the most portable pattern.

```bash
# Minimal curl-based query helper
linear_query() {
  curl -s -X POST https://api.linear.app/graphql \
    -H "Authorization: $LINEAR_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"query\": \"$1\"}"
}
```

## references/linear-vs-jira.md

# Linear vs Jira: Translation Guide for Migrating Teams

This guide is for teams moving an existing Jira instance to Linear. It maps Jira concepts to Linear concepts, calls out where the mapping is lossy, and recommends a migration sequence.

---

## Concept Map

| Jira | Linear | Notes |
|---|---|---|
| Site / Cloud Instance | Workspace (Organization) | One Linear workspace usually maps to one Jira site |
| Project | **Team** (most often) | A Jira Project's permission boundary and issue prefix are closest to Linear's Team |
| Project (when it's really a feature) | **Project** (Linear) | If a Jira project is one feature, map it to a Linear Project under an existing Team |
| Issue Type (Story, Bug, Task) | **Label** in a `type/*` group | Linear has no issue types; convention is `type/feature`, `type/bug`, `type/chore`, `type/spike` |
| Epic | **Project** | Linear Projects are the right "container of related issues with a target date" |
| Initiative (Premium/Enterprise Plans, formerly Advanced Roadmaps) | **Initiative** | Direct map |
| Sprint | **Cycle** | Direct map; cycles are per-team in Linear |
| Subtask | **Sub-issue** | Direct map |
| Component | **Label** in an `area/*` group | E.g. `area/api`, `area/web` |
| Fix Version / Release | **Project Milestone** or **Project target date** | Lossy: Jira releases span multiple projects; Linear milestones live inside one project |
| Custom Field (single-select) | **Label** in a custom label group | Use a label group per single-select field |
| Custom Field (free text) | Description text or a comment | No first-class home; structure as `Key: value` lines in description |
| Custom Field (number) | Description text | No first-class home; consider rounding into priority/estimate |
| Workflow (custom states) | **Workflow State** (constrained to 5 types) | Lossy: Jira workflows with 10+ states collapse to Linear's 5 type buckets (backlog/unstarted/started/completed/canceled) |
| Workflow Transition rules | Automations + GraphQL | Most rules become Linear automations or external webhook handlers |
| Resolution | Workflow state in `completed` or `canceled` type | Linear conveys resolution through the state's type |
| Priority (Highest/High/Medium/Low/Lowest) | Priority (Urgent/High/Medium/Low/No priority) | Map Highest+High → Urgent or High; Lowest → No priority or Low |
| Story Points | **Estimate** | Pick the team's estimation scale to match: Fibonacci (1, 2, 3, 5, 8) is closest |
| Labels | **Label** (no group) | Direct map |
| Watchers | **Subscribers** | Direct map |
| Comment | Comment | Direct map; Markdown is preserved by the importer |
| Attachment | Attachment | Direct map; importer downloads from Jira and re-uploads |
| Issue Link (blocks/is blocked by) | **Issue Relation** (blocks/blocked by/related to/duplicate of) | Direct map for the standard link types |
| Filter (JQL saved filter) | **View** (saved filter) | JQL → Linear's filter UI; the syntax differs |
| Dashboard / Gadget | **Views** + Insights | Linear has no gadget concept; Insights covers velocity, throughput, scope; custom dashboards live in Notion or BI tools |
| Permission Scheme | Team membership + workspace role | Linear has 3 workspace roles (Admin, Member, Guest) and team membership; no per-issue permissions |
| Service Desk / Jira Service Management | Not in Linear; use Triage + external helpdesk | Linear is not a helpdesk; integrate with Front, Intercom, Plain |
| Confluence link | Notion page link or attachment | If migrating docs too, see `notion-pm/` |

---

## Workflow State Mapping

Jira workflows are highly variable. Linear constrains every state to one of 5 types. Default mapping:

| Jira state (typical) | Linear type | Linear state name (typical) |
|---|---|---|
| Backlog, Open | `backlog` | Backlog |
| To Do, Selected for Development, Ready | `unstarted` | Todo |
| In Progress, In Development | `started` | In Progress |
| In Code Review, In QA, In Staging | `started` | In Review |
| Done, Closed, Resolved | `completed` | Done |
| Won't Do, Rejected, Duplicate | `canceled` | Canceled |
| Triage, Needs Triage | `triage` | Triage (enable on team) |

When a Jira project has unusual states like "Awaiting Customer Response," create a label (`status/awaiting-customer`) and keep the issue in `started`.

---

## Filter / JQL Translation Examples

| JQL | Linear filter equivalent |
|---|---|
| `project = ENG AND status = "In Progress"` | Team filter = ENG + State type = Started |
| `assignee = currentUser() AND sprint in openSprints()` | Assigned to me + Cycle = Current cycle |
| `priority in (Highest, High) AND status != Done` | Priority in (Urgent, High) + State type not in (Completed, Canceled) |
| `labels = "tech-debt"` | Label = tech-debt |
| `updated < -30d AND status != Done` | Updated date < 30 days ago + State type not in (Completed, Canceled) |
| `"Epic Link" = ENG-100` | Project = <linked Linear Project for that Jira Epic> |
| `type = Bug AND created >= -7d` | Label = type/bug + Created date < 7 days ago |

---

## Migration Plan (Recommended Sequence)

### Phase 0 — Inventory (1-2 days)
- Count: projects, issues per project, custom fields, workflows, users.
- Identify integrations: Slack, GitHub, CI, BI exports, scripts hitting the Jira REST API.
- Decide cutover strategy: big bang (one weekend) or phased (one Jira project per week).

### Phase 1 — Pilot (1 week)
- Pick the smallest, most active Jira project.
- Create the destination Linear team; configure labels, states, cycles.
- Run Linear's first-party Jira importer in dry-run mode.
- Validate: identifiers, comments, attachments, status mappings, custom fields → labels.
- Tweak the team configuration based on what broke.

### Phase 2 — Communication and Training (1 week, in parallel)
- Announce timeline to all users.
- Run 2-3 live demos showing the daily workflow in Linear.
- Publish a cheat sheet: keyboard shortcuts, magic words, triage SOP.
- Set the Jira instance to read-only on the cutover date.

### Phase 3 — Cutover (1 weekend per batch)
- Freeze writes on the source Jira projects.
- Run the importer for real.
- Spot-check 5% of issues for fidelity.
- Switch integrations: GitHub app, Slack, CI, scripts.
- Set up a 301-redirect or maintenance page on the Jira URL.

### Phase 4 — Decommission (after 30 days)
- Confirm no team is still writing to Jira.
- Export Jira as XML/JSON for compliance archive.
- Cancel the Jira subscription.

---

## What You Lose Going Jira → Linear

- **Per-issue permissions and security levels.** Linear permissions are at the team level.
- **Highly customized workflows.** Linear's 5 state types are a hard ceiling.
- **Custom field rigor.** Labels and structured description sections are the only extension points.
- **Service desk / SLA features.** Linear is not a helpdesk; pair with Front/Intercom/Plain for support workflows.
- **JQL.** Linear's filter UI is more visual but less expressive; very complex JQL becomes multiple saved views.
- **Time tracking.** Linear has no native time tracking; use an integration (Toggl, Harvest) if required.
- **Gadgets and pixel-perfect dashboards.** Use Linear Insights for velocity/throughput; push exported data to Notion or a BI tool for executive dashboards.

## What You Gain Going Jira → Linear

- A keyboard-first UI most engineers will adopt voluntarily.
- A GraphQL API that is consistent, documented, and pleasant to script against.
- GitHub integration that actually closes issues on merge without configuration ceremony.
- An opinionated Cycle / Project / Initiative hierarchy that resists the sprawl Jira invites.
- Triage as a first-class concept, not a workaround.
- Performance: Linear is fast even on workspaces with hundreds of thousands of issues.

---

## Common Pitfalls

1. **Mapping every Jira project to a Linear team.** Often the right move is many small Jira "feature projects" → one Linear team with multiple Linear Projects.
2. **Recreating Jira's 12-state workflow.** Resist; collapse to 5-6 states and use labels for nuance.
3. **Preserving every custom field.** Most are read by nobody; audit before mapping.
4. **Doing a big-bang migration on a large instance.** Phase by team or business unit; pilot first.
5. **Forgetting BI exports and ETL pipelines.** They will break the moment Jira goes read-only.
6. **Not training on keyboard shortcuts.** Linear's velocity advantage evaporates if users navigate by mouse.

## references/red-flags.md

# Red Flags: Linear Expert

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every Linear configuration, GraphQL query, automation, or migration artifact before applying to a team. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Cycle-as-Sprint Misuse

**Symptom.** Team treats Linear cycles as 2-week scrum sprints: cycle planning meeting, cycle goal, cycle review, velocity tracking.
**Why it's bad.** Linear cycles are designed for continuous flow, not commit-and-deliver ceremonies. Cycles auto-roll, do not enforce commitments, and have soft boundaries. Forcing scrum semantics on top creates friction -- the team works around Linear's defaults instead of leveraging them.
**Bad example:**
> "Cycle 23 (Apr 1 - Apr 14): team committed to 18 issues; carried 9 over to Cycle 24; treated this as a failed sprint and started over."
**Good example:**
> "Cycles 23 + 24 used as flow windows: team aims for ~12 issues per cycle but does not 'commit' in the scrum sense. Carry-over is expected and tracked as a flow metric (cycle-time, throughput) rather than as a failure mode. Sprint-style ceremonies (commit + review) replaced by continuous review per Linear's design."
**How to catch it.** Team is doing 'cycle planning' meetings with explicit commitments and carrying over = either re-adopt Linear's flow defaults or switch to Jira for scrum semantics.

---

## Red Flag 2: Project Bloat

**Symptom.** 200+ active Linear Projects, half with 1-3 issues; new initiatives spawn a Project by default.
**Why it's bad.** Projects are heavy-weight in Linear -- they have their own update cadence, members, lead, and visibility. Bloat dilutes the signal; nobody knows which Projects are truly active, and the org-wide Projects view becomes useless.
**Bad example:**
> "Active Projects: 247. Of those, 132 have < 5 issues, 78 have not been updated in 90 days. Project list is 14 screens long."
**Good example:**
> "Project hygiene: Projects are reserved for *initiatives that need a status update + a sponsor + a target date*. Smaller themed work uses Labels + Cycles instead. Quarterly review archives stale Projects. Today: 38 active Projects, all with a documented update cadence."
**How to catch it.** Project count > 50 = audit. Any Project with no Update in 30 days = candidate for archive.

---

## Red Flag 3: GraphQL N+1

**Symptom.** Script fetches 200 issues, then for each issue makes a separate query for its assignee and labels.
**Why it's bad.** Linear's GraphQL API supports nested selection; making N+1 queries hits rate limits fast (as of September 2026 Linear allows 2,500 requests/hour per user for API keys and 5,000 for OAuth apps, plus an hourly complexity budget), is 100x slower, and is the most common anti-pattern in Linear integrations.
**Bad example:**
> "for issue in issues:
>   assignee = client.query('{ user(id: ...) { name } }')
>   labels = client.query('{ issueLabels(filter: { issueId: ... }) { ... } }')"
**Good example:**
> "Single query with nested selection:
> ```graphql
> query {
>   issues(first: 200, filter: { ... }) {
>     nodes {
>       id identifier title state { name }
>       assignee { id name email }
>       labels { nodes { id name color } }
>     }
>   }
> }
> ```"
**How to catch it.** Any script that loops over issues making per-issue queries = rewrite with nested selection. Watch for `RATELIMITED` errors (returned with HTTP 400) in logs.

---

## Red Flag 4: Initiatives Used as Folders

**Symptom.** Linear Initiatives are created to group Projects by team or department, not by strategic outcome.
**Why it's bad.** Initiatives in Linear are designed for cross-team strategic bets. Misusing them as folders breaks Linear's outcome-tracking features and clutters the strategic view.
**Bad example:**
> "Initiative 'Engineering Q2 Work' contains 47 Projects. (It is a folder, not a strategy.)"
**Good example:**
> "Initiatives align with strategic outcomes (e.g. 'Activation: time-to-second-action < 3 min by Q4'). Each Initiative contains 3-8 Projects, each contributing to the outcome. Organizational grouping uses Teams + Labels, not Initiatives."
**How to catch it.** Initiative name contains a team / department / quarter / 'work' / 'engineering' = reclassify.

---

## Red Flag 5: Workflow States Modified Per-Team Without Org Alignment

**Symptom.** Team A's workflow: Backlog -> Triage -> Todo -> In Progress -> In Review -> Done. Team B added 4 custom states.
**Why it's bad.** Custom states break Linear's cross-team views (no shared mapping), confuse engineers who work across teams, and inflate the org-wide complexity. Linear's defaults are battle-tested; custom states should be rare and justified.
**Bad example:**
> "Team B added: 'Spec Review', 'Awaiting Design', 'In QA', 'Blocked External'. None match Team A's; cross-team reports broken."
**Good example:**
> "Org-wide default workflow used by all teams. Any custom state requires a documented exception in `linear-conventions.md` and an explicit mapping back to org-wide types (started / completed / canceled)."
**How to catch it.** Count distinct workflow states across all teams. > 8 in any team = audit; > 12 across the org = consolidate.

---

## Red Flag 6: Sub-Issue Hierarchy Inversion

**Symptom.** Issues with 15 sub-issues, sub-issues that are larger than the parent, deeply nested sub-issue trees (4+ levels).
**Why it's bad.** Linear's sub-issue model is intended for shallow within-task decomposition, not as a substitute for the Project layer. Deep nesting breaks burn-down, makes the issue view a tree of clutter, and slows the UI noticeably.
**Bad example:**
> "Issue 'Build Bulk Edit' has 4 sub-issues, each with 6-8 sub-sub-issues, totaling 31 nested issues."
**Good example:**
> "Issue 'Build Bulk Edit' is a Project (not an issue) -- because it spans > 2 weeks and crosses multiple components. The Project contains 6-8 top-level issues, each with 0-3 sub-issues for within-sprint tasks only. Max depth: 2."
**How to catch it.** Any issue with > 5 sub-issues or > 2 levels of nesting = re-model as a Project.

---

## Red Flag 7: Triage Inbox Untriaged

**Symptom.** Linear's Triage queue has 380 issues, going back 6 months.
**Why it's bad.** Triage is the gate between intake and the team's commitment. An overflowing Triage means new bugs / feature requests are not being acknowledged, customers wait, and the team loses visibility into what is incoming.
**Bad example:**
> "Triage queue: 380 issues, oldest 184 days. Nobody owns Triage."
**Good example:**
> "Triage SLA: each issue routed to a team within 2 business days. Rotating Triage owner per team (1-week rotation). Weekly Triage cleanup ritual: any issue > 14 days in Triage is either accepted, declined with reason, or escalated."
**How to catch it.** Triage queue > 30 issues or oldest > 14 days = staff Triage.

---

## Red Flag 8: API Webhooks With No Signature Verification

**Symptom.** Linear webhook posts to an internal service; service trusts the payload and acts on it.
**Why it's bad.** Without signature verification, attackers can replay or forge webhook events, triggering automation (deletions, status changes, notifications). This is a real security risk, not theoretical.
**Bad example:**
> "@app.route('/linear-webhook', methods=['POST'])
> def handle():
>     data = request.json
>     do_thing(data)  # no verification"
**Good example:**
> "Every webhook handler verifies the `Linear-Signature` header against the configured webhook secret using constant-time HMAC comparison. Failed verifications return 401 and log to the security channel. Documented in `references/webhook-security.md`."
**How to catch it.** Any webhook handler that does not validate `Linear-Signature` = security review now.

---

## Red Flag 9: Jira -> Linear Migration Without Workflow Mapping

**Symptom.** Bulk import 8000 Jira issues into Linear; statuses default to 'Backlog'.
**Why it's bad.** A statuses-collapsed migration loses the team's most valuable signal (which work is in flight, which is blocked, which is done). The team has to manually re-classify thousands of issues or the new Linear instance is unusable.
**Bad example:**
> "Bulk migrate: all 8000 Jira issues created in Linear; all set to Backlog. Sprint history dropped."
**Good example:**
> "Migration plan with explicit mappings:
> - Jira `In Progress`, `In Review`, `In QA` -> Linear `In Progress` (with a label preserving the precise Jira state)
> - Jira `Done` -> Linear `Done`
> - Closed-resolved Jira issues map to canceled state
> Sprint history is preserved in a custom field `legacy_sprint`. Migration script in `references/jira-to-linear-migration.md`."
**How to catch it.** Any migration plan that does not have a status-mapping table = stop and write one.

---

## Red Flag 10: Cycle Goals That Are Output Lists

**Symptom.** Cycle goal: "Ship features A, B, C." (Not an outcome.)
**Why it's bad.** A cycle goal that lists outputs collapses to a status checklist, not a coordination signal. The team ships and feels successful even if nothing improved. Linear's update cadence is built on outcomes, not output lists.
**Bad example:**
> "Cycle 23 goal: 'Ship bulk-edit, dark mode, and SCIM v1.'"
**Good example:**
> "Cycle 23 goal: 'Enterprise admins spend < 2 min on candidate edits' (measured via the candidate-edit-event log). Bets in flight this cycle: bulk-edit (primary), in-product templates (secondary). Reviewing the goal at cycle close means looking at the metric, not the ship-list."
**How to catch it.** Cycle goal is a list of features = rewrite as an outcome with bets underneath.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Cycle-as-sprint | Team commits + carries over? Wrong tool. |
| 2 | Project bloat | > 50 active Projects = audit |
| 3 | GraphQL N+1 | Loops doing per-issue queries = nested selection |
| 4 | Initiatives as folders | Initiative named after a team / department |
| 5 | Custom workflow states | > 8 states per team = consolidate |
| 6 | Sub-issue hierarchy inversion | > 5 sub-issues or > 2 levels = use a Project |
| 7 | Triage untriaged | Queue > 30 or oldest > 14 days = staff |
| 8 | Webhooks unsigned | All handlers verify HMAC |
| 9 | Migration without mapping | Explicit status-mapping table |
| 10 | Output-list cycle goals | Cycle goal is an outcome, not a ship-list |

## Related Reading

- `SKILL.md` -- Linear admin + GraphQL patterns
- `references/linear-graphql-patterns.md` -- canonical queries
- `references/jira-to-linear-migration.md` -- migration playbook
- `references/webhook-security.md` -- signature verification
- Sibling skill: `jira-expert/` -- Jira's equivalent patterns
- Sibling skill: `scrum-master/` -- ceremony patterns that fit Linear cycles
- Sibling skill: `execution/cycle-time-analyzer/` -- flow metrics that Linear emphasizes

---

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---|---|---|
| Issue did not auto-close on PR merge | PR description used wrong magic word, repo not connected to the team, or PR was merged via squash without the magic word in the commit message | Verify the GitHub integration is enabled for the team; ensure the magic word (`Fixes`, `Closes`, `Resolves`) appears in PR title or description; if squash-merging, include the magic word in the commit message |
| GraphQL query returns null for a field that should exist | Field is gated behind a permission your API key lacks, or the field is on a different type (e.g. `Issue.project` vs `Issue.projectMilestone`) | Re-check the schema via Linear's GraphQL Playground; ensure the API key belongs to a workspace member with access to the relevant team |
| Triage rules not firing for inbound items | Team does not have triage enabled, or the source integration is configured to write directly to a workflow state | Enable triage in team settings; reconfigure the source (e.g. Slack-to-Linear) to create issues without a state so they land in triage |
| Bulk update script gets `RATELIMITED` errors | Exceeded the request or complexity budget for its auth type (API key: 2,500 req/hr and 3M points/hr per user; OAuth app: 5,000 req/hr and 2M points/hr; as of September 2026) | Add exponential backoff until the `X-RateLimit-*-Reset` time; use `issueBatchUpdate` instead of per-issue calls; trim nested selections to cut complexity; spread work over time or move the integration to an OAuth app |
| Cycle issues show the wrong velocity | Issues without estimates are excluded from velocity; canceled work is excluded; scope changes during cycle distort the chart | Require estimates at planning time; review the cycle's scope history in Insights to spot mid-cycle additions |
| Custom field values from Jira are missing after import | Linear has no custom fields; the Jira importer maps them to labels or appends to description, which can lose semantics | Pre-map critical Jira custom fields to label groups before import; for fields that cannot be expressed as labels, append structured key:value lines to the description |
| Webhook deliveries are missing or duplicated | Receiver is too slow (>10s response), or the webhook secret is rotated and signatures fail validation | Respond with 2xx within 5 seconds; queue work asynchronously; verify the signature on every payload using the current secret |

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/linear-expert -->
