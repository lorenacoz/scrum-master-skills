# jira-expert

> **Use these instructions for this whole conversation.** Apply them when: Configures Jira projects, workflows, boards, JQL, automation and dashboards, and audits board, issue and workflow exports. Use when setting up or fixing Jira, writing or debugging JQL, or designing automation rules.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Atlassian Jira Expert

Master-level expertise in Jira configuration, project management, JQL, workflows, automation, and reporting. Handles all technical and operational aspects of Jira.

> **Terminology (Jira Cloud, as of September 2026):** Jira "projects" are now called **spaces** and "issues" **work items** in the UI -- a naming change only ([announcement](https://jirareleases.atlassian.com/announcements/jira-spaces-a-new-name-that-matches-how-you-really-work)). Existing JQL keeps working, and if a new term is not yet accepted in JQL, use the old one (`project`, `issuetype`) ([JQL fields](https://support.atlassian.com/jira-software-cloud/docs/jql-fields/)); REST paths are unchanged (`/rest/api/3/project`). Advanced Roadmaps is now **Plans** (Jira Premium and Enterprise, [docs](https://support.atlassian.com/jira-software-cloud/docs/what-is-advanced-roadmaps/)). This skill uses "project" and "space" interchangeably.

## Core Capabilities

- **Project configuration** — create Scrum/Kanban/custom projects, design custom workflows, configure issue types/fields/screens, set permission and security schemes
- **JQL mastery** — author advanced queries, build complex filters, optimize query performance, create saved filters for teams
- **Automation & integration** — design automation rules, configure webhooks and notifications, integrate Confluence/Slack/external tools
- **Reporting & dashboards** — custom dashboards with gadgets, sprint/velocity/burndown reports, portfolio-level and executive reporting

## When to Use

- Setting up a new project and its workflow, fields, and board
- Writing or debugging JQL for filters, reports, or dashboards
- Designing automation rules and avoiding trigger loops
- Building dashboards and configuring gadgets for a team or exec
- Managing custom fields, issue links, security levels, or bulk operations

## Clarify First

Jira advice depends most on which Jira the user runs, what they are allowed to change, and whether the work only reads data or changes it. Settle the inputs below before producing anything. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Cloud or Data Center, and plan:** Plans (formerly Advanced Roadmaps) needs Premium or Enterprise. Cloud automation is metered in usage-based steps pooled across the organization, which limits how many rules a design can afford. Data Center reaches end of life on 28 Mar 2029, so long-lived configuration work there should assume a Cloud move.
- **Querying or configuring:** JQL, saved filters and dashboards need little more than browse access and affect nobody else. Workflow schemes, permission schemes, custom fields and org-wide automation need project or Jira admin rights, and some go to `atlassian-admin/`. A workflow change on an active project needs a migration plan, because in-flight issues are not changed retroactively.
- **Read-only or writing through the API or MCP:** A JQL search is safe to run. Creating, editing, transitioning or bulk-changing work items alters shared data and notifies people, so confirm the scope before any write. Workflow schemes, automation rules, permission schemes and custom-field configuration are not exposed as MCP tools and have to be done in Jira admin or the REST API.
- **Instance size and current setup:** JQL on instances above about 100K issues can hit performance ceilings, and more than five active workflows across the org is a signal to consolidate rather than add another. `workflow_analyzer.py`, `board_optimizer.py` and `issue_quality_checker.py` need an export of issues or the board config to say anything specific.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Tools

Three offline audits of Jira exports (they never call Jira). Each prints text or `--format json` (`--json` is the same); `--example` prints a valid input, and the files in `assets/` are those examples.

| Tool | Input | Reports |
|------|-------|---------|
| `board_optimizer.py --board FILE` | Board config: `name`, `type`, `team_size`, `filter_jql`, `columns[]` (`name`, `wip_limit`, `statuses`), card fields | 0-100 score, active columns without WIP limits, missing card fields, suggested WIP (about 1.5x team size) |
| `issue_quality_checker.py --issues FILE` | `issues[]` with `key`, `type`, `summary`, `description`, `assignee`, `priority`, `story_points`, `labels`, `epic_link`, `sprint` | Per-issue score against summary, description, acceptance-criteria, assignee and estimate checks; most common gaps |
| `workflow_analyzer.py --issues FILE` | `issues[]` each with `transitions[]` (`from_status`, `to_status`, `entered`, `exited`) | Time in status (avg/median/P90), bottleneck status, rework rate (backward moves) |

```bash
python3 scripts/board_optimizer.py --board assets/sample_board.json
python3 scripts/issue_quality_checker.py --issues assets/sample_issues.json --format json
python3 scripts/workflow_analyzer.py --issues assets/sample_transitions.json
```

On the samples: the board scores 80 with "In Review" missing a WIP limit; PROJ-102 scores 11% (no description, no criteria, unassigned); the workflow shows a 12.5% rework rate from one review bounce.

**Exit codes:** `0` report produced · `2` missing or unreadable file, invalid JSON, or the wrong shape. They report; none of them gates.

## Anti-Patterns

### A custom workflow for every project
**Mistake:** Each project gets its own workflow with 12+ states, until the org runs dozens of distinct workflows.
**Why it happens:** Every team asks for statuses that match its own process exactly, and saying yes is easy.
**Instead:** Start new projects from a shared workflow and push back on per-project states. Count the active workflows across the org: more than 5 means consolidate. Cross-project reporting and reusable automation depend on shared statuses.

### Unreadable JQL
**Mistake:** Filters and dashboards run on 200-character JQL with nested AND / OR / NOT chains nobody can read.
**Why it happens:** Each new condition gets bolted onto a query that already works, and nobody goes back to restructure it.
**Instead:** Break any JQL longer than 120 characters or deeper than 2 levels of parentheses into named saved filters with comments. A misplaced OR or missing parenthesis silently drops tickets, and small named filters are easier to check.

### Story points per person
**Mistake:** A dashboard or filter groups completed story points by assignee, and the numbers end up in performance reviews.
**Why it happens:** The data is already in Jira, and it looks like an objective productivity measure.
**Instead:** Report story points at team level only, and remove any filter or gadget that groups them by assignee. Points are a team's relative sizing tool. Judging people by them leads to inflated estimates and avoided hard work.

Eight more, each with a bad and a good example: `references/red-flags.md`.

## Reference Documentation

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/jira-playbook.md](references/jira-playbook.md)** — full detail behind this map: competencies, workflows (project creation, workflow design, dashboards, automation), JQL operators/functions, advanced features (custom fields, linking, security, bulk ops), reporting templates, decision/handoff protocols, best practices, troubleshooting table, and success criteria. Read when executing any Jira task.
- **[references/jql-examples.md](references/jql-examples.md)** — extended library of ready-to-run JQL queries grouped by use case (sprints, and more). Read when you need a specific query pattern fast.
- **[references/automation-examples.md](references/automation-examples.md)** — concrete Jira automation rule recipes (auto-assignment, and more) with triggers/conditions/actions. Read when building or troubleshooting automation rules.
- **[references/red-flags.md](references/red-flags.md)** — common ways a Jira configuration, JQL query, automation rule, or dashboard goes wrong, with bad/good examples. Read before shipping any change to a team.

## Scope & Limitations

**In Scope:** Jira project creation and configuration, workflow design and implementation, JQL query authoring and optimization, automation rule design, dashboard and reporting setup, custom field management, board configuration, bulk operations, issue linking strategies.

**Out of Scope:** Org-wide Atlassian administration (hand off to `atlassian-admin/`), Confluence space management (hand off to `confluence-expert/`), sprint execution and team coaching (hand off to `scrum-master/`), strategic project prioritization (hand off to `senior-pm/`).

**Limitations:** Jira Cloud automation is metered as usage-based automation steps, with per-plan allowances pooled at the organization level ([usage](https://support.atlassian.com/cloud-automation/docs/how-is-my-usage-calculated/), as of September 2026). Jira Data Center reaches end of life on 28 Mar 2029 (no new/expanded DC licenses after 30 Mar 2028) -- see `atlassian-admin/` and Atlassian's [DC end-of-life page](https://www.atlassian.com/licensing/data-center-end-of-life). Complex JQL on large instances (>100K issues) may hit performance ceilings. Workflow changes to active projects require careful migration planning -- retroactive changes do not apply to in-flight issues.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `atlassian-admin/` | Admin -> Jira | Global schemes, permission templates, user provisioning |
| `scrum-master/` | SM -> Jira | Sprint board configuration requests, velocity report needs |
| `senior-pm/` | PM -> Jira | Portfolio-level reporting requirements, cross-project dashboards |
| `confluence-expert/` | Bidirectional | Jira macros embedded in Confluence pages; documentation links in issue descriptions |
| `atlassian-templates/` | Templates -> Jira | Issue description templates, workflow documentation |
| `delivery-manager/` | DM -> Jira | Release version management, deployment tracking fields |

## Files

| File | Purpose |
|------|---------|
| `scripts/board_optimizer.py` | Board configuration audit |
| `scripts/issue_quality_checker.py` | Issue description and field quality |
| `scripts/workflow_analyzer.py` | Time in status, bottleneck, rework |
| `assets/sample_board.json`, `assets/sample_issues.json`, `assets/sample_transitions.json` | Inputs for the three tools |
| `examples/acme-50-person-eng-setup.md` | Worked Jira setup for a 50-person org |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/automation-examples.md

# Jira Automation Examples

## Auto-Assignment Rules

### Auto-assign by component
**Trigger:** Issue created
**Conditions:**
- Component is not EMPTY
**Actions:**
- Assign issue to component lead

### Auto-assign to reporter for feedback
**Trigger:** Issue transitioned to "Waiting for Feedback"
**Actions:**
- Assign issue to reporter
- Add comment: "Please provide additional information"

### Round-robin assignment
**Trigger:** Issue created
**Conditions:**
- Project = ABC
- Assignee is EMPTY
**Actions:**
- Assign to next team member in rotation (use smart value)

---

## Status Sync Rules

### Sync subtask status to parent
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Sub-task
- Transition is to "Done"
- Parent issue exists
- All subtasks are Done
**Actions:**
- Transition parent issue to "Done"

### Sync parent to subtasks
**Trigger:** Issue transitioned
**Conditions:**
- Issue type has subtasks
- Transition is to "Cancelled"
**Actions:**
- For each: Sub-tasks
  - Transition issue to "Cancelled"

### Epic progress tracking
**Trigger:** Issue transitioned
**Conditions:**
- Epic link is not EMPTY
- Transition is to "Done"
**Actions:**
- Add comment to epic: "{{issue.key}} completed"
- Update epic custom field "Progress"

---

## Notification Rules

### Slack notification for high-priority bugs
**Trigger:** Issue created
**Conditions:**
- Issue type = Bug
- Priority IN (Highest, High)
**Actions:**
- Send Slack message to #engineering:
  ```
  🚨 High Priority Bug Created
  {{issue.key}}: {{issue.summary}}
  Reporter: {{issue.reporter.displayName}}
  Priority: {{issue.priority.name}}
  {{issue.url}}
  ```

### Email assignee when mentioned
**Trigger:** Issue commented
**Conditions:**
- Comment contains @mention of assignee
**Actions:**
- Send email to {{issue.assignee.emailAddress}}:
  ```
  Subject: You were mentioned in {{issue.key}}
  Body: {{comment.author.displayName}} mentioned you:
  {{comment.body}}
  ```

### SLA breach warning
**Trigger:** Scheduled - Every hour
**Conditions:**
- Status != Done
- SLA time remaining < 2 hours
**Actions:**
- Send email to {{issue.assignee}}
- Add comment: "⚠️ SLA expires in <2 hours"
- Set priority to Highest

---

## Field Automation Rules

### Auto-set due date
**Trigger:** Issue created
**Conditions:**
- Issue type = Bug
- Priority = Highest
**Actions:**
- Set due date to {{now.plusDays(1)}}

### Clear assignee when in backlog
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "Backlog"
- Assignee is not EMPTY
**Actions:**
- Assign issue to Unassigned
- Add comment: "Returned to backlog, assignee cleared"

### Auto-populate sprint field
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "In Progress"
- Sprint is EMPTY
**Actions:**
- Add issue to current sprint

### Set fix version based on component
**Trigger:** Issue created
**Conditions:**
- Component = "Mobile App"
**Actions:**
- Set fix version to "Mobile v2.0"

---

## Escalation Rules

### Auto-escalate stale issues
**Trigger:** Scheduled - Daily at 9:00 AM
**Conditions:**
- Status = "Waiting for Response"
- Updated < -7 days
**Actions:**
- Add comment: "@{{issue.reporter}} This issue needs attention"
- Send email to project lead
- Add label: "needs-attention"

### Escalate overdue critical issues
**Trigger:** Scheduled - Every hour
**Conditions:**
- Priority IN (Highest, High)
- Due date < now()
- Status != Done
**Actions:**
- Transition to "Escalated"
- Assign to project manager
- Send Slack notification

### Auto-close inactive issues
**Trigger:** Scheduled - Daily at 10:00 AM
**Conditions:**
- Status = "Waiting for Customer"
- Updated < -30 days
**Actions:**
- Transition to "Closed"
- Add comment: "Auto-closed due to inactivity"
- Send email to reporter

---

## Sprint Automation Rules

### Move incomplete work to next sprint
**Trigger:** Sprint closed
**Conditions:**
- Issue status != Done
**Actions:**
- Add issue to next sprint
- Add comment: "Moved from {{sprint.name}}"

### Auto-remove completed items from active sprint
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "Done"
- Sprint IN openSprints()
**Actions:**
- Remove issue from sprint
- Add comment: "Removed from active sprint (completed)"

### Sprint start notification
**Trigger:** Sprint started
**Actions:**
- Send Slack message to #team:
  ```
  🚀 Sprint {{sprint.name}} Started!
  Goal: {{sprint.goal}}
  Committed: {{sprint.issuesCount}} issues
  ```

---

## Approval Workflow Rules

### Request approval for large stories
**Trigger:** Issue created
**Conditions:**
- Issue type = Story
- Story points >= 13
**Actions:**
- Transition to "Pending Approval"
- Assign to product owner
- Send email notification

### Auto-approve small bugs
**Trigger:** Issue created
**Conditions:**
- Issue type = Bug
- Priority IN (Low, Lowest)
**Actions:**
- Transition to "Approved"
- Add comment: "Auto-approved (low-priority bug)"

### Require security review
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "Ready for Release"
- Labels contains "security"
**Actions:**
- Transition to "Security Review"
- Assign to security-team
- Send email to security@company.com

---

## Integration Rules

### Create GitHub issue
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "In Progress"
- Labels contains "needs-tracking"
**Actions:**
- Send webhook to GitHub API:
  ```json
  {
    "title": "{{issue.key}}: {{issue.summary}}",
    "body": "{{issue.description}}",
    "assignee": "{{issue.assignee.name}}"
  }
  ```

### Update Confluence page
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Epic
- Transition is to "Done"
**Actions:**
- Send webhook to Confluence:
  - Update epic status page
  - Add completion date

---

## Quality & Testing Rules

### Require test cases for features
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Story
- Transition is to "Ready for QA"
- Custom field "Test Cases" is EMPTY
**Actions:**
- Transition back to "In Progress"
- Add comment: "❌ Test cases required before QA"

### Auto-create test issue
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Story
- Transition is to "Ready for QA"
**Actions:**
- Create linked issue:
  - Type: Test
  - Summary: "Test: {{issue.summary}}"
  - Link type: "tested by"
  - Assignee: QA team

### Flag regression bugs
**Trigger:** Issue created
**Conditions:**
- Issue type = Bug
- Affects version is in released versions
**Actions:**
- Add label: "regression"
- Set priority to High
- Add comment: "🚨 Regression in released version"

---

## Documentation Rules

### Require documentation for features
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Story
- Labels contains "customer-facing"
- Transition is to "Done"
- Custom field "Documentation Link" is EMPTY
**Actions:**
- Reopen issue
- Add comment: "📝 Documentation required for customer-facing feature"

### Auto-create doc task
**Trigger:** Issue transitioned
**Conditions:**
- Issue type = Epic
- Transition is to "In Progress"
**Actions:**
- Create subtask:
  - Type: Task
  - Summary: "Documentation for {{issue.summary}}"
  - Assignee: {{issue.assignee}}

---

## Time Tracking Rules

### Log work reminder
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "Done"
- Time spent is EMPTY
**Actions:**
- Add comment: "⏱️ Reminder: Please log your time"

### Warn on high time spent
**Trigger:** Work logged
**Conditions:**
- Time spent > original estimate * 1.5
**Actions:**
- Add comment: "⚠️ Time spent exceeds estimate by 50%"
- Send notification to assignee and project manager

---

## Advanced Conditional Rules

### Conditional assignee based on priority
**Trigger:** Issue created
**Conditions:**
- Issue type = Bug
**Actions:**
- If: Priority = Highest
  - Assign to on-call engineer
- Else if: Priority = High
  - Assign to team lead
- Else:
  - Assign to next available team member

### Multi-step approval flow
**Trigger:** Issue transitioned
**Conditions:**
- Transition is to "Request Approval"
- Budget estimate > $10,000
**Actions:**
- If: Budget > $50,000
  - Assign to CFO
  - Send email to executive team
- Else if: Budget > $10,000
  - Assign to Director
  - Add comment: "Director approval required"
- Add label: "pending-approval"

---

## Smart Value Examples

### Dynamic assignee based on component
```
{{issue.components.first.lead.accountId}}
```

### Days since created
```
{{issue.created.diff(now).days}}
```

### Conditional message
```
{{#if(issue.priority.name == "Highest")}}
  🚨 CRITICAL
{{else}}
  ℹ️ Normal priority
{{/}}
```

### List all subtasks
```
{{#issue.subtasks}}
  - {{key}}: {{summary}} ({{status.name}})
{{/}}
```

### Calculate completion percentage
```
{{issue.subtasks.filter(item => item.status.statusCategory.key == "done").size.divide(issue.subtasks.size).multiply(100).round()}}%
```

---

## Best Practices

1. **Test in sandbox** - Always test rules on test project first
2. **Start simple** - Begin with basic rules, add complexity incrementally
3. **Use conditions wisely** - Narrow scope to reduce unintended triggers
4. **Monitor audit log** - Check automation execution history regularly
5. **Limit actions** - Keep rules focused, don't chain too many actions
6. **Name clearly** - Use descriptive names: "Auto-assign bugs to component lead"
7. **Document rules** - Add description explaining purpose and owner
8. **Review regularly** - Audit rules quarterly, disable unused ones
9. **Handle errors** - Add error handling for webhooks and integrations
10. **Performance** - Avoid scheduled rules that query large datasets hourly

## references/jira-playbook.md

# Jira Expert Playbook

> Read this when you need the full detail behind the SKILL.md map — competencies, workflows, JQL operators/functions, inline JQL examples, advanced features, reporting templates, decision/handoff protocols, best practices, troubleshooting, and success criteria.

## Core Competencies (detail)

**Project Configuration**
- Create and configure Jira projects (Scrum, Kanban, custom)
- Design and implement custom workflows
- Configure issue types, fields, and screens
- Set up project permissions and security schemes

**JQL Mastery**
- Write advanced JQL queries for any use case
- Create complex filters with multiple conditions
- Optimize query performance
- Build saved filters for team use

**Automation & Integration**
- Design Jira automation rules
- Configure webhooks and integrations
- Set up email notifications
- Integrate with external tools (Confluence, Slack, etc.)

**Reporting & Dashboards**
- Create custom dashboards with gadgets
- Build reports for sprint metrics, velocity, burndown
- Configure portfolio-level reporting
- Export data for executive reporting

## Workflows

### Project Creation
1. Determine project type (Scrum, Kanban, Bug Tracking, etc.)
2. Create project with appropriate template
3. Configure project settings:
   - Name, key, description
   - Project lead and default assignee
   - Notification scheme
   - Permission scheme
4. Set up issue types and workflows
5. Configure custom fields if needed
6. Create initial board/backlog view
7. **HANDOFF TO**: Scrum Master for team onboarding

### Workflow Design
1. Map out process states (To Do → In Progress → Done)
2. Define transitions and conditions
3. Add validators, post-functions, and conditions
4. Configure workflow scheme
5. Associate workflow with project
6. Test workflow with sample issues
7. **USE**: References for complex workflow patterns

### JQL Query Building
**Basic Structure**: `field operator value`

**Common Operators**:
- `=, !=` : equals, not equals
- `~, !~` : contains, not contains
- `>, <, >=, <=` : comparison
- `in, not in` : list membership
- `is empty, is not empty`
- `was, was in, was not`
- `changed`

**Powerful JQL Examples**:

Find overdue issues:
```jql
dueDate < now() AND status != Done
```

Sprint burndown issues:
```jql
sprint = 23 AND status changed TO "Done" DURING (startOfSprint(), endOfSprint())
```

Find stale issues:
```jql
updated < -30d AND status != Done
```

Cross-project epic tracking:
```jql
"Epic Link" = PROJ-123 ORDER BY rank
```

Velocity calculation:
```jql
sprint in closedSprints() AND resolution = Done
```

Team capacity:
```jql
assignee in (user1, user2) AND sprint in openSprints()
```

### Dashboard Creation
1. Create new dashboard (personal or shared)
2. Add relevant gadgets:
   - Filter Results (JQL-based)
   - Sprint Burndown
   - Velocity Chart
   - Created vs Resolved
   - Pie Chart (status distribution)
3. Arrange layout for readability
4. Configure automatic refresh
5. Share with appropriate teams
6. **HANDOFF TO**: Senior PM or Scrum Master for use

### Automation Rules
1. Define trigger (issue created, field changed, scheduled)
2. Add conditions (if applicable)
3. Define actions:
   - Update field
   - Send notification
   - Create subtask
   - Transition issue
   - Post comment
4. Test automation with sample data
5. Enable and monitor
6. **USE**: References for complex automation patterns

## Advanced Features

### Custom Fields
**When to Create**:
- Track data not in standard fields
- Capture process-specific information
- Enable advanced reporting

**Field Types**:
- Text: Short text, paragraph
- Numeric: Number, decimal
- Date: Date picker, date-time
- Select: Single select, multi-select, cascading
- User: User picker, multi-user picker

**Configuration**:
1. Create custom field
2. Configure field context (which projects/issue types)
3. Add to appropriate screens
4. Update search templates if needed

### Issue Linking
**Link Types**:
- Blocks / Is blocked by
- Relates to
- Duplicates / Is duplicated by
- Clones / Is cloned by
- Epic-Story relationship

**Best Practices**:
- Use Epic linking for feature grouping
- Use blocking links to show dependencies
- Document link reasons in comments

### Permissions & Security

**Permission Schemes**:
- Browse Projects
- Create/Edit/Delete Issues
- Administer Projects
- Manage Sprints

**Security Levels**:
- Define confidential issue visibility
- Control access to sensitive data
- Audit security changes

### Bulk Operations
**Bulk Change**:
1. Use JQL to find target issues
2. Select bulk change operation
3. Choose fields to update
4. Preview changes
5. Execute and confirm
6. Monitor background task

**Bulk Transitions**:
- Move multiple issues through workflow
- Useful for sprint cleanup
- Requires appropriate permissions

## JQL Functions Reference

**Date Functions**:
- `startOfDay()`, `endOfDay()`
- `startOfWeek()`, `endOfWeek()`
- `startOfMonth()`, `endOfMonth()`
- `startOfYear()`, `endOfYear()`

**Sprint Functions**:
- `openSprints()`
- `closedSprints()`
- `futureSprints()`

**User Functions**:
- `currentUser()`
- `membersOf("group")`

**Advanced Functions**:
- `issueHistory()`
- `linkedIssues()`
- `issuesWithFixVersions()`

## Reporting Templates

**Sprint Report**:
```jql
project = PROJ AND sprint = 23
```

**Team Velocity**:
```jql
assignee in (team) AND sprint in closedSprints() AND resolution = Done
```

**Bug Trend**:
```jql
type = Bug AND created >= -30d
```

**Blocker Analysis**:
```jql
priority = Blocker AND status != Done
```

## Decision Framework

**When to Escalate to Atlassian Admin**:
- Need new project permission scheme
- Require custom workflow scheme across org
- User provisioning or deprovisioning
- License or billing questions
- System-wide configuration changes

**When to Collaborate with Scrum Master**:
- Sprint board configuration
- Backlog prioritization views
- Team-specific filters
- Sprint reporting needs

**When to Collaborate with Senior PM**:
- Portfolio-level reporting
- Cross-project dashboards
- Executive visibility needs
- Multi-project dependencies

## Handoff Protocols

**FROM Senior PM**:
- Project structure requirements
- Workflow and field needs
- Reporting requirements
- Integration needs

**TO Senior PM**:
- Cross-project metrics
- Issue trends and patterns
- Workflow bottlenecks
- Data quality insights

**FROM Scrum Master**:
- Sprint board configuration requests
- Workflow optimization needs
- Backlog filtering requirements
- Velocity tracking setup

**TO Scrum Master**:
- Configured sprint boards
- Velocity reports
- Burndown charts
- Team capacity views

## Best Practices

**Data Quality**:
- Enforce required fields
- Use field validation
- Regular cleanup of stale issues
- Consistent naming conventions

**Performance**:
- Optimize JQL queries
- Limit dashboard gadgets
- Use saved filters
- Archive old projects

**Governance**:
- Document workflow rationale
- Version control for schemes
- Change management for major updates
- Regular permission audits

## Atlassian MCP Integration

**Primary Tool**: Atlassian Rovo MCP Server (Atlassian's official remote MCP server for Cloud; endpoint `https://mcp.atlassian.com/v2/mcp`, OAuth 2.1 or API token). Tool names below are from Atlassian's [supported tools](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/) list as of September 2026 -- re-check it, the list changes.

**Key Operations** (Jira tools):
- Execute JQL queries for data extraction -- `searchJiraIssuesUsingJql`
- Create and update issues -- `createJiraIssue`, `editJiraIssue`, `addOrEditJiraIssueComment`
- Move issues through the workflow -- `listJiraIssueTransitions`, `transitionJiraIssue`
- Create and manage sprints and boards -- `manageJiraSprint`, `listJiraBoardSprints`, `getJiraBoardSprintData`, `createJiraBoard`
- Create or update spaces (formerly "projects") -- `createJiraProject`, `updateJiraProject`
- Pull history for flow metrics -- `listJiraIssueChangelogs`
- Read filters and dashboards -- `listJiraFilters`, `listJiraDashboards`

Workflow schemes, automation rules, permission schemes and custom-field configuration are **not** exposed as MCP tools -- configure those in Jira admin (or via the REST API) and document the change.

**Integration Points**:
- Pull metrics for Senior PM reporting
- Configure sprint boards for Scrum Master
- Create documentation pages for Confluence Expert
- Support template creation for Template Creator

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| JQL queries return unexpected results or time out | Overly broad filters, missing indexes, or incorrect field references | Add specificity with project/date constraints; use `ORDER BY` sparingly on large datasets; verify field names with autocomplete |
| Automation rules fire multiple times for a single event | Cascading triggers where one rule's action triggers another rule | Add conditions to prevent loops (e.g., check `initiator is automation`); use the audit log to trace execution chains |
| Board shows wrong issues or missing cards | Filter behind the board is misconfigured or sprint assignment is incorrect | Verify the board's saved filter JQL; check that issues have the correct sprint field value; review board settings > general |
| Workflow transitions fail with validator errors | Required fields not populated, or post-function order is incorrect | Check validator configuration; ensure required fields have values before transition; reorder post-functions so field-setting happens before validation |
| Custom fields not appearing on screens | Field added to wrong screen scheme or issue type context is too narrow | Verify field context includes the target project and issue type; confirm the correct screen scheme is associated with the project |
| Bulk operations fail or time out | Too many issues selected (>1000) or complex post-functions on transitions | Reduce batch size to 100-200 issues; disable non-essential automation rules temporarily during bulk operations |
| Dashboard gadgets show "No data" | Underlying filter returns no results for the current user due to permissions | Verify the filter is shared with the dashboard viewers; check project permission schemes |

## Success Criteria

- All active projects use standardized workflow schemes (no more than 5 unique workflows org-wide)
- JQL saved filters cover 90%+ of recurring reporting needs without ad-hoc queries
- Automation rules reduce manual status updates by 60%+ across managed projects
- Data quality score (required fields populated, consistent labeling) exceeds 85% for active issues
- Average dashboard load time stays under 3 seconds with all gadgets rendering
- New project setup (from request to team-ready board) completes within 2 business days
- Zero critical permission escalations caused by misconfigured schemes per quarter

## references/jql-examples.md

# JQL Query Examples

## Sprint Queries

**Current sprint issues:**
```jql
sprint IN openSprints() ORDER BY rank
```

**Issues in specific sprint:**
```jql
sprint = "Sprint 23" ORDER BY priority DESC
```

**All sprint work (current and backlog):**
```jql
project = ABC AND issuetype IN (Story, Bug, Task) 
ORDER BY sprint DESC, rank
```

**Unscheduled stories:**
```jql
project = ABC AND issuetype = Story AND sprint IS EMPTY 
AND status != Done ORDER BY priority DESC
```

**Spillover from last sprint:**
```jql
sprint IN closedSprints() AND sprint NOT IN (latestReleasedVersion()) 
AND status != Done ORDER BY created DESC
```

**Sprint completion rate:**
```jql
sprint = "Sprint 23" AND status = Done
```

## User & Team Queries

**My open issues:**
```jql
assignee = currentUser() AND status != Done 
ORDER BY priority DESC, created ASC
```

**Unassigned in my project:**
```jql
project = ABC AND assignee IS EMPTY AND status != Done
ORDER BY priority DESC
```

**Issues I'm watching:**
```jql
watcher = currentUser() AND status != Done
```

**Team workload:**
```jql
assignee IN membersOf("engineering") AND status IN ("In Progress", "In Review")
ORDER BY assignee, priority DESC
```

**Issues I reported that are still open:**
```jql
reporter = currentUser() AND status != Done ORDER BY created DESC
```

**Issues commented on by me:**
```jql
comment ~ currentUser() AND status != Done
```

## Date Range Queries

**Created today:**
```jql
created >= startOfDay() ORDER BY created DESC
```

**Updated in last 7 days:**
```jql
updated >= -7d ORDER BY updated DESC
```

**Created this week:**
```jql
created >= startOfWeek() AND created <= endOfWeek()
```

**Created this month:**
```jql
created >= startOfMonth() AND created <= endOfMonth()
```

**Not updated in 30 days:**
```jql
status != Done AND updated <= -30d ORDER BY updated ASC
```

**Resolved yesterday:**
```jql
resolved >= startOfDay(-1d) AND resolved < startOfDay()
```

**Due this week:**
```jql
duedate >= startOfWeek() AND duedate <= endOfWeek() AND status != Done
```

**Overdue:**
```jql
duedate < now() AND status != Done ORDER BY duedate ASC
```

## Status & Workflow Queries

**In Progress issues:**
```jql
project = ABC AND status = "In Progress" ORDER BY assignee
```

**Blocked issues:**
```jql
project = ABC AND labels = blocked AND status != Done
```

**Issues in review:**
```jql
project = ABC AND status IN ("Code Review", "QA Review", "Pending Approval")
ORDER BY updated ASC
```

**Ready for development:**
```jql
project = ABC AND status = "Ready" AND sprint IS EMPTY
ORDER BY priority DESC
```

**Recently done:**
```jql
project = ABC AND status = Done AND resolved >= -7d
ORDER BY resolved DESC
```

**Status changed today:**
```jql
status CHANGED AFTER startOfDay() ORDER BY updated DESC
```

**Long-running in progress:**
```jql
status = "In Progress" AND status CHANGED BEFORE -14d
ORDER BY status CHANGED ASC
```

## Priority & Type Queries

**High priority bugs:**
```jql
issuetype = Bug AND priority IN (Highest, High) AND status != Done
ORDER BY priority DESC, created ASC
```

**Critical blockers:**
```jql
priority = Highest AND status != Done ORDER BY created ASC
```

**All epics:**
```jql
issuetype = Epic ORDER BY status, priority DESC
```

**Stories without acceptance criteria:**
```jql
issuetype = Story AND "Acceptance Criteria" IS EMPTY AND status = Backlog
```

**Technical debt:**
```jql
labels = tech-debt AND status != Done ORDER BY priority DESC
```

## Complex Multi-Condition Queries

**My team's sprint work:**
```jql
sprint IN openSprints() 
AND assignee IN membersOf("engineering") 
AND status != Done
ORDER BY assignee, priority DESC
```

**Bugs created this month, not in sprint:**
```jql
issuetype = Bug 
AND created >= startOfMonth() 
AND sprint IS EMPTY 
AND status != Done
ORDER BY priority DESC, created DESC
```

**High-priority work needing attention:**
```jql
project = ABC 
AND priority IN (Highest, High) 
AND status IN ("In Progress", "In Review") 
AND updated <= -3d
ORDER BY priority DESC, updated ASC
```

**Stale issues:**
```jql
project = ABC 
AND status NOT IN (Done, Cancelled) 
AND (assignee IS EMPTY OR updated <= -30d)
ORDER BY created ASC
```

**Epic progress:**
```jql
"Epic Link" = ABC-123 ORDER BY status, rank
```

## Component & Version Queries

**Issues in component:**
```jql
project = ABC AND component = "Frontend" AND status != Done
```

**Issues without component:**
```jql
project = ABC AND component IS EMPTY AND status != Done
```

**Target version:**
```jql
fixVersion = "v2.0" ORDER BY status, priority DESC
```

**Released versions:**
```jql
fixVersion IN releasedVersions() ORDER BY fixVersion DESC
```

## Label & Text Search Queries

**Issues with label:**
```jql
labels = urgent AND status != Done
```

**Multiple labels (AND):**
```jql
labels IN (frontend, bug) AND status != Done
```

**Search in summary:**
```jql
summary ~ "authentication" ORDER BY created DESC
```

**Search in summary and description:**
```jql
text ~ "API integration" ORDER BY created DESC
```

**Issues with empty description:**
```jql
description IS EMPTY AND issuetype = Story
```

## Performance-Optimized Queries

**Good - Specific project first:**
```jql
project = ABC AND status = "In Progress" AND assignee = currentUser()
```

**Bad - User filter first:**
```jql
assignee = currentUser() AND status = "In Progress" AND project = ABC
```

**Good - Use functions:**
```jql
sprint IN openSprints() AND status != Done
```

**Bad - Hardcoded sprint:**
```jql
sprint = "Sprint 23" AND status != Done
```

**Good - Specific date:**
```jql
created >= 2024-01-01 AND created <= 2024-01-31
```

**Bad - Relative with high cost:**
```jql
created >= -365d AND created <= -335d
```

## Reporting Queries

**Velocity calculation:**
```jql
sprint = "Sprint 23" AND status = Done
```
*Then sum story points*

**Bug rate:**
```jql
project = ABC AND issuetype = Bug AND created >= startOfMonth()
```

**Average cycle time:**
```jql
project = ABC AND resolved >= startOfMonth() 
AND resolved <= endOfMonth()
```
*Calculate time from In Progress to Done*

**Stories delivered this quarter:**
```jql
project = ABC AND issuetype = Story 
AND resolved >= startOfYear() AND resolved <= endOfQuarter()
```

**Team capacity:**
```jql
assignee IN membersOf("engineering") 
AND sprint IN openSprints()
```
*Sum original estimates*

## Notification & Watching Queries

**Issues I need to review:**
```jql
status = "Pending Review" AND assignee = currentUser()
```

**Issues assigned to me, high priority:**
```jql
assignee = currentUser() AND priority IN (Highest, High) 
AND status != Done
```

**Issues created by me, not resolved:**
```jql
reporter = currentUser() AND status != Done 
ORDER BY created DESC
```

## Advanced Functions

**Issues changed from status:**
```jql
status WAS "In Progress" AND status = "Done" 
AND status CHANGED AFTER startOfWeek()
```

**Assignee changed:**
```jql
assignee CHANGED BY currentUser() AFTER -7d
```

**Issues re-opened:**
```jql
status WAS Done AND status != Done ORDER BY updated DESC
```

**Linked issues:**
```jql
issue IN linkedIssues("ABC-123") ORDER BY issuetype
```

**Parent epic:**
```jql
parent = ABC-123 ORDER BY rank
```

## Saved Filter Examples

**Daily Standup Filter:**
```jql
assignee = currentUser() AND sprint IN openSprints() 
AND status != Done ORDER BY priority DESC
```

**Team Sprint Board Filter:**
```jql
project = ABC AND sprint IN openSprints() ORDER BY rank
```

**Bugs Dashboard Filter:**
```jql
project = ABC AND issuetype = Bug AND status != Done
ORDER BY priority DESC, created ASC
```

**Tech Debt Backlog:**
```jql
project = ABC AND labels = tech-debt AND status = Backlog
ORDER BY priority DESC
```

**Needs Triage:**
```jql
project = ABC AND status = "To Triage" 
AND created >= -7d ORDER BY created ASC
```

## references/red-flags.md

# Red Flags: Jira Expert

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every Jira configuration change, JQL query, automation rule, or dashboard before publishing to a team. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Workflow Proliferation

**Symptom.** Each project has its own custom workflow with 12+ states; the org has 47 distinct workflows across 30 projects.
**Why it's bad.** Workflow proliferation makes cross-project reporting impossible (no shared statuses), trains every new joiner from scratch, and means automation rules cannot be reused. The Jira admin spends most of their week mapping workflow A's "In Review" to workflow B's "Code Review In Progress".
**Bad example:**
> "Project A workflow: Open -> In Triage -> Ready -> In Progress -> In Code Review -> In QA -> Ready for UAT -> In UAT -> Done -> Closed -> Archived.
> Project B workflow: To Do -> Doing -> Reviewing -> Validated -> Released.
> (Cross-project velocity report breaks.)"
**Good example:**
> "Org-wide shared workflow: Open -> In Progress -> In Review -> Done. Custom states *only* in projects with a defended exception (e.g., regulated team needs an explicit 'Awaiting QA Signoff' state). Exceptions logged in the Jira-admin charter."
**How to catch it.** Count distinct active workflows. > 5 across the org = proliferation; consolidate.

---

## Red Flag 2: JQL Spaghetti

**Symptom.** Filters and dashboards use 200-character JQL queries with nested AND / OR / NOT chains nobody can read.
**Why it's bad.** Spaghetti JQL is unmaintainable. The original author leaves; the query becomes load-bearing infrastructure nobody dares touch. Subtle bugs (an OR scoping wrong, a missing parenthesis) silently exclude tickets.
**Bad example:**
> "project in (PROJ, OPS, INFRA) AND ((status not in (Done, Closed) AND assignee in membersOf('eng-team')) OR (labels in (urgent, blocker) AND status != Done)) AND created >= -90d AND (component != 'legacy' OR resolution = Unresolved)"
**Good example:**
> "Saved filter `Eng Active Work` (definition stored in `jira-filters.md` with comments):
> ```
> project in (PROJ, OPS, INFRA)
> AND status != Done
> AND (assignee in membersOf('eng-team') OR labels in (urgent, blocker))
> AND created >= -90d
> ```
> Then a dashboard widget references the named filter, not raw JQL."
**How to catch it.** Any inline JQL > 120 chars or > 2 levels of parens = refactor into named saved filters with comments.

---

## Red Flag 3: Dashboards Nobody Opens

**Symptom.** The team has 14 Jira dashboards, all created during onboarding, used by 0 people in the last 30 days.
**Why it's bad.** Dashboards are infrastructure. Unused ones drift, embed stale assumptions, and mislead new joiners who *do* find them. The right number of dashboards is the number people actually use.
**Bad example:**
> "Dashboards in the team's space: Sprint Health, Quarterly Velocity, Bug Bash 2024, Q1 Retrospective Data, Hiring Pipeline, Old Atlas Project, ..."
**Good example:**
> "Quarterly Jira-hygiene review: open dashboard audit log; any dashboard with 0 views in 30 days is archived. Standing dashboards: 3 (Sprint Health, Quarter-View, Incident Tracker). New dashboards require an owner + a use case stated in the description."
**How to catch it.** Run `Dashboard activity report` (Jira admin); any dashboard with 0 views in 30 days = archive.

---

## Red Flag 4: Custom Fields Sprawl

**Symptom.** The Jira instance has 340 custom fields, half referencing departed team configurations.
**Why it's bad.** Custom-field sprawl slows Jira queries, clutters issue-creation forms, and increases the chance of inconsistent data ('Story Points' vs 'Story Pts' vs 'Estimate' all in use). It also exhausts Jira's custom-field index limits.
**Bad example:**
> "Issue creation form has 47 fields, half pre-filled with default values nobody understands, 6 abandoned fields from a 2022 process. Search performance degraded by ~30%."
**Good example:**
> "Custom fields: 28, each with a documented owner and a use case. Quarterly audit removes orphaned fields. Issue creation forms use field configuration schemes to hide non-essential fields per issue type (Bug: 6 fields; Story: 8 fields; Spike: 5 fields)."
**How to catch it.** Custom field count > 80 = audit. Any field with 0 issues touched in 90 days = candidate for removal.

---

## Red Flag 5: Automation Rules That Conflict

**Symptom.** Two automation rules fire on the same transition: one moves the ticket to "Done", the other transitions it back to "In Review". Tickets oscillate.
**Why it's bad.** Conflicting rules produce non-deterministic Jira behavior. Engineers cannot trust the board state. Worse, the bug is hard to diagnose because each rule looks correct in isolation.
**Bad example:**
> "Rule 1: 'On commit message [DONE-XYZ], transition to Done.'
> Rule 2: 'On status change to Done without a QA sign-off, transition back to In Review.'
> (Tickets bounce.)"
**Good example:**
> "Automation rules are catalogued in `jira-automation.md` with each rule's trigger, condition, action, and known interactions. Quarterly review tests all rules together in a staging Jira project before promoting to production."
**How to catch it.** Any ticket that has changed status > 4 times in a day = inspect for rule conflict.

---

## Red Flag 6: Story Points as a Performance Metric

**Symptom.** Manager pulls "story points completed per engineer per sprint" and uses it in performance reviews.
**Why it's bad.** Story points are a *team* relative-sizing tool, not an individual productivity metric. Treating them as performance data trains engineers to inflate estimates, decline complex work, and avoid pair programming. Velocity collapses as a planning signal.
**Bad example:**
> "Performance review: 'Sarah completed 38 SP last sprint; Tom completed 18. Tom needs a PIP.' (Ignoring that Tom's work included on-call + a complex migration.)"
**Good example:**
> "Story points are used only at the team-level (sprint capacity + velocity forecasting). Performance is reviewed via the career-ladder rubric (`pm-career-ladder` skill), not Jira numbers. Engineering managers have explicit org-wide guidance: 'no individual story-point reports'."
**How to catch it.** Any Jira filter / dashboard grouping story points by assignee = remove. See `scrum-master/references/red-flags.md` Red Flag 1.

---

## Red Flag 7: Sprints That Never End

**Symptom.** "Sprint 47" has been "active" for 8 weeks because tickets keep getting carried over.
**Why it's bad.** A sprint is a time-boxed iteration. Letting it run past its end-date corrupts velocity, makes retrospectives meaningless, and erodes the "complete what you commit" discipline. Worse, it hides scope creep -- the sprint just expands.
**Bad example:**
> "Sprint 47: started March 1, originally 2 weeks. Today is May 20. 22 tickets still open. Sprint 48 cannot start because 47 has not closed."
**Good example:**
> "Sprint discipline: sprints close on their scheduled end-date, regardless of completion. Incomplete tickets are explicitly moved (either back to the backlog with a retrospective lesson, or into the next sprint with a documented reason). Closing a sprint is the scrum master's responsibility on the scheduled day."
**How to catch it.** Sprint open longer than 1.5x its planned duration = close it; write a retro lesson.

---

## Red Flag 8: Epic / Story / Subtask Hierarchy Inversion

**Symptom.** Stories with 12 subtasks; subtasks larger than the parent story; epics containing one story.
**Why it's bad.** The hierarchy exists to keep work coherent. Inversions signal under-thought structure -- subtasks-as-stories is a misuse of the type (subtasks are within-sprint slices). Reports break: epic-level burndown shows tiny epics; subtask totals dwarf parent stories.
**Bad example:**
> "Epic 'Bulk Edit' contains 1 story 'Implement Bulk Edit', which contains 22 subtasks ranging from UI to backend to DB migration."
**Good example:**
> "Epic 'Bulk Edit' contains 6 stories (one per vertical slice from `story-splitting`). Each story has 2-5 subtasks for within-sprint coordination only (e.g. 'write tests', 'cut release'). Stories are the unit of value; subtasks are the unit of within-sprint work."
**How to catch it.** Any story with > 6 subtasks, or any subtask > 5 SP = restructure.

---

## Red Flag 9: Inconsistent Issue Types Across Projects

**Symptom.** Project A uses 'Bug, Story, Task, Epic'. Project B uses 'Defect, Feature, Improvement, Initiative'.
**Why it's bad.** Inconsistent types break org-wide reporting and make every cross-project ritual (release notes, security audit, executive reporting) require manual translation. It is also confusing to people who work across projects.
**Bad example:**
> "Org-wide bug report: cannot be generated because 'Bug' and 'Defect' are distinct issue types in different projects."
**Good example:**
> "Issue-type scheme is org-standardized: Story, Task, Bug, Epic, Spike, Subtask. New projects inherit the scheme. Exceptions for regulated teams approved via the Jira-admin charter."
**How to catch it.** Cross-project issue-type count > 8 distinct = consolidate.

---

## Red Flag 10: Permissions Configured Per-Project By Hand

**Symptom.** Each project has a hand-edited permission scheme; the QA team has read access in 11 of 14 projects and nobody knows why the 3 are different.
**Why it's bad.** Per-project hand-editing is unscalable, error-prone, and creates security risk (forgotten access). Reconciling who-has-what-where takes hours per incident.
**Bad example:**
> "47 distinct permission schemes across 30 projects. Half were copies of another scheme with one tweak."
**Good example:**
> "3 org-wide permission schemes: 'Open' (read-all, write-team), 'Restricted' (read-team, write-team), 'Confidential' (read-named-roles). Projects pick one. Role memberships drive access. Documented in `jira-permissions.md`."
**How to catch it.** Permission schemes > 5 = consolidate.

---

## Red Flag 11: JQL in Documentation Without an As-of Date

**Symptom.** "To see open bugs: `project = PROJ AND issuetype = Bug AND status != Done`." Documentation written 2 years ago.
**Why it's bad.** JQL semantics shift as projects evolve (issue types renamed, statuses added). Old JQL silently returns wrong results. The reader trusts the documentation; the documentation is wrong.
**Bad example:**
> "[Old runbook]: 'Open bugs: `project = PROJ AND issuetype = Bug AND status != Done`. (No date, no verification.)'"
**Good example:**
> "[Runbook, 2026-05-21]: 'Open bugs: saved filter `OPEN-BUGS-PROJ` (definition link). Verified against current schema; renewed on the quarterly runbook review.' (Filter ownership: <name>; expires if not renewed.)"
**How to catch it.** Any JQL in a runbook with no date / no saved-filter wrapper = re-validate.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Workflow proliferation | > 5 distinct workflows = consolidate |
| 2 | JQL spaghetti | Inline JQL > 120 chars = saved filter |
| 3 | Dashboards nobody opens | 0 views in 30 days = archive |
| 4 | Custom field sprawl | > 80 custom fields = audit |
| 5 | Automation rules conflict | Tickets oscillating between states |
| 6 | SP as performance metric | No SP-by-assignee filters |
| 7 | Sprints that never end | Open > 1.5x planned duration = close |
| 8 | Hierarchy inversion | Story with > 6 subtasks = restructure |
| 9 | Inconsistent issue types | > 8 cross-project types = consolidate |
| 10 | Per-project permissions | Permission schemes > 5 = consolidate |
| 11 | JQL in docs without date | All runbook JQL via saved filters |

## Related Reading

- `SKILL.md` -- Jira administration patterns
- `references/jql-patterns.md` -- canonical JQL recipes
- `references/automation-recipes.md` -- standard automation rules
- Sibling skill: `linear-expert/` -- Linear's equivalent patterns
- Sibling skill: `atlassian-admin/` -- broader Atlassian-suite admin
- Sibling skill: `scrum-master/` -- the data Jira-expert serves
- Sibling skill: `confluence-expert/` -- the documentation paired with Jira

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/jira-expert
