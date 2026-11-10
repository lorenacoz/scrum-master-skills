# Project Manager AI Playbook

Reusable AI instructions for every phase of a project. Works in Microsoft Copilot, ChatGPT, Gemini, GitHub Copilot or any AI assistant your company allows.

**40 skills** in 7 phases. Each skill is a set of instructions that turns a general AI assistant into a specialist for one project management job.

**Prefer a page with copy buttons?** Download [`pm-playbook.html`](pm-playbook.html) (click *Download raw file* on GitHub) and open it in your browser. It works offline.

## Contents

- [Start the project](#start-the-project) (5 skills)
- [Plan the work](#plan-the-work) (8 skills)
- [Run delivery](#run-delivery) (8 skills)
- [Monitor and report](#monitor-and-report) (5 skills)
- [Communicate and lead](#communicate-and-lead) (3 skills)
- [Launch and close](#launch-and-close) (6 skills)
- [Work tools](#work-tools) (5 skills)
- [How to use a skill at work](#how-to-use-a-skill-at-work)
- [Ground rules](#ground-rules)

## How to use a skill at work

**Microsoft 365 Copilot (Copilot Chat)**

1. Fastest: open a skill's `.md` file, copy everything, paste it as your first message, then ask your question.
2. Too long to paste? Attach the `.md` file to the chat (paperclip) and say: *Follow the instructions in the attached file for this conversation.*
3. Use it often? Create an agent (Copilot Chat → Create agent, or Copilot Studio). Paste the **core instructions** into Instructions and upload the full `.md` file as knowledge.

**ChatGPT**

1. Paste the `.md` file as your first message, or attach it.
2. Use it often? Create a custom GPT or a Project: core instructions in the Instructions box, the full `.md` file as a knowledge file.

**Google Gemini**

1. Paste or attach the `.md` file at the start of the chat.
2. Use it often? Create a Gem: core instructions as the Gem's instructions, the full `.md` file as a knowledge file.

**GitHub Copilot (VS Code, JetBrains)**

1. Save the skill's `.prompt.md` file in your repository at `.github/prompts/`.
2. In Copilot Chat, type `/` and pick the prompt by name.

**Core or full?** Each skill's `.md` file is the full skill: its instructions plus reference material. The core instructions are the first part. Instruction boxes in custom agents and GPTs are often limited to around 7,500 characters, so the tables below show the core size.

## Ground rules

- Follow your company's AI policy. Use only AI tools your company approves, and don't paste confidential data into tools that aren't approved for it.
- Start a new chat for each skill, so instructions from one don't leak into the next.
- Give the AI your real situation: numbers, dates, constraints. The skills ask follow-up questions when something is missing; answer them.
- Check the output before you send it. You own the plan, the status and the decision.

## Start the project

*Get clear on scope, people, decision rights and how the team will work.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **project-manager**<br><sub>core 17,279 chars · too long for most instruction boxes: attach the file</sub> | Set up a project: charter, plan, RAID log (risks, assumptions, issues, dependencies), change control and status. | "Help me set up a new project: migrating our customer portal to a new platform in 5 months, 2 teams, a fixed launch date. Start with the charter and a RAID log." | [Any AI (.md)](skills/project-manager.md) · [Copilot prompt](skills/project-manager.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/project-manager) |
| **stakeholder-map**<br><sub>core 8,512 chars · too long for most instruction boxes: attach the file</sub> | Map who has power and interest, and plan how to engage each group. | "Map stakeholders for a CRM replacement: sponsor (CFO), sales leadership, 40 sales reps, IT security, an outside vendor and the data team." | [Any AI (.md)](skills/stakeholder-map.md) · [Copilot prompt](skills/stakeholder-map.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/stakeholder-map) |
| **daci-framework**<br><sub>core 6,949 chars · fits an instructions box</sub> | Agree who Drives, Approves, Contributes and is Informed for a decision, before it stalls. | "Set up a DACI for choosing between two vendors for our new ticketing tool. Budget sign-off sits with the VP of Operations." | [Any AI (.md)](skills/daci-framework.md) · [Copilot prompt](skills/daci-framework.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/daci-framework) |
| **working-agreements**<br><sub>core 2,997 chars · fits an instructions box</sub> | Charter a new team: purpose, working agreements and a first Definition of Done. | "We just formed a 7-person cross-functional team across two time zones. Facilitate a 90-minute chartering session." | [Any AI (.md)](skills/working-agreements.md) · [Copilot prompt](skills/working-agreements.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/working-agreements) |
| **pm-onboarding**<br><sub>core 7,686 chars · too long for most instruction boxes: attach the file</sub> | Build a 30-60-90 day plan when you join a new project, program or company. | "I'm taking over a delayed program next Monday. Build my 30-60-90 day plan: who to meet, what to ask, and early wins." | [Any AI (.md)](skills/pm-onboarding.md) · [Copilot prompt](skills/pm-onboarding.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/career/pm-onboarding) |

## Plan the work

*Break big work down, sequence it, surface risk early and agree what matters most.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **wayfinder**<br><sub>core 8,101 chars · too long for most instruction boxes: attach the file</sub> | Work is too big or unclear for one sprint: map the open decisions, resolve them in order, then create tickets. | "We need to add single sign-on to three internal apps and nobody knows where to start. Map the decisions we need to make first." | [Any AI (.md)](skills/wayfinder.md) · [Copilot prompt](skills/wayfinder.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/wayfinder) |
| **quarterly-planning**<br><sub>core 9,146 chars · too long for most instruction boxes: attach the file</sub> | Plan a quarter: capacity, commitments versus stretch, cross-team dependencies. | "Plan Q3 for two teams (11 people, one starting parental leave in August). Leadership wants 6 initiatives; help us decide what fits." | [Any AI (.md)](skills/quarterly-planning.md) · [Copilot prompt](skills/quarterly-planning.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/quarterly-planning) |
| **outcome-roadmap**<br><sub>core 8,563 chars · too long for most instruction boxes: attach the file</sub> | Turn a feature list into a Now / Next / Later roadmap of outcomes, each with a measure. | "Turn this into an outcome roadmap: new dashboard, CSV export, SSO, mobile app, faster search, audit log." | [Any AI (.md)](skills/outcome-roadmap.md) · [Copilot prompt](skills/outcome-roadmap.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/outcome-roadmap) |
| **dependency-map**<br><sub>core 9,355 chars · too long for most instruction boxes: attach the file</sub> | Find cross-team dependencies and rank them by risk. | "Map dependencies for a release that needs the payments team's new API, a security review and a vendor contract renewal." | [Any AI (.md)](skills/dependency-map.md) · [Copilot prompt](skills/dependency-map.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/dependency-map) |
| **pre-mortem**<br><sub>core 7,650 chars · too long for most instruction boxes: attach the file</sub> | Imagine the project failed, list why, and give each risk an owner and a mitigation. | "Run a pre-mortem for our ERP go-live on 1 March. 300 users, a two-week cutover window, and the vendor is new to us." | [Any AI (.md)](skills/pre-mortem.md) · [Copilot prompt](skills/pre-mortem.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/discovery/pre-mortem) |
| **plan-grilling**<br><sub>core 8,229 chars · too long for most instruction boxes: attach the file</sub> | Stress-test a plan one round of questions at a time until every decision is settled. | "Grill this plan: we move 4 teams to a new deployment pipeline in 6 weeks, one team at a time, with no change freeze." | [Any AI (.md)](skills/plan-grilling.md) · [Copilot prompt](skills/plan-grilling.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/discovery/plan-grilling) |
| **prioritization-frameworks**<br><sub>core 8,669 chars · too long for most instruction boxes: attach the file</sub> | Choose and apply a prioritization method (RICE, MoSCoW, WSJF, Kano and others). | "Prioritize these 8 requests from three departments using WSJF. Here is what I know about value and effort for each: ..." | [Any AI (.md)](skills/prioritization-frameworks.md) · [Copilot prompt](skills/prioritization-frameworks.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/prioritization-frameworks) |
| **create-prd**<br><sub>core 9,379 chars · too long for most instruction boxes: attach the file</sub> | Write a requirements document that frames the problem before the solution. | "Write a PRD for automating our monthly vendor invoice approval, which today takes 3 days of email back and forth." | [Any AI (.md)](skills/create-prd.md) · [Copilot prompt](skills/create-prd.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/create-prd) |

## Run delivery

*Keep work moving: blockers, scope creep, decisions, meetings and releases.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **delivery-manager**<br><sub>core 8,531 chars · too long for most instruction boxes: attach the file</sub> | Plan releases, run a Go/No-Go, choose a deployment strategy, handle an incident. | "Prepare the Go/No-Go checklist for Friday's release. Two open bugs are rated medium and the on-call engineer is new." | [Any AI (.md)](skills/delivery-manager.md) · [Copilot prompt](skills/delivery-manager.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/delivery-manager) |
| **impediment-log**<br><sub>core 2,189 chars · fits an instructions box</sub> | Log, triage and escalate a blocker, and draft the escalation message. | "We've waited 9 days for firewall access from another department. Help me escalate it without burning the relationship." | [Any AI (.md)](skills/impediment-log.md) · [Copilot prompt](skills/impediment-log.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/impediment-log) |
| **protect-the-sprint**<br><sub>core 2,887 chars · fits an instructions box</sub> | Handle mid-sprint requests and scope creep, and draft the reply to the stakeholder. | "A director asked my team to 'squeeze in' a new report this sprint. We're at full capacity. Draft my reply." | [Any AI (.md)](skills/protect-the-sprint.md) · [Copilot prompt](skills/protect-the-sprint.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/protect-the-sprint) |
| **decision-questionnaire**<br><sub>core 7,904 chars · too long for most instruction boxes: attach the file</sub> | Get a decision from a busy stakeholder in writing, without scheduling a meeting. | "I need the VP to choose between delaying launch two weeks or cutting the reporting feature. Write a questionnaire she can answer in 5 minutes." | [Any AI (.md)](skills/decision-questionnaire.md) · [Copilot prompt](skills/decision-questionnaire.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/decision-questionnaire) |
| **problem-solver**<br><sub>core 15,376 chars · too long for most instruction boxes: attach the file</sub> | Diagnose a recurring problem before fixing it: problem statement and verified root causes. | "Our releases have slipped 4 of the last 6 months. Help me find the real cause before we change the process." | [Any AI (.md)](skills/problem-solver.md) · [Copilot prompt](skills/problem-solver.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/problem-solver) |
| **meeting-analyzer**<br><sub>core 12,997 chars · too long for most instruction boxes: attach the file</sub> | Turn meeting notes into a register of who committed to what; diagnose meetings that decide nothing. | "Here are notes from our last 4 weekly steering meetings. Pull out every commitment and tell me which items keep rolling over." | [Any AI (.md)](skills/meeting-analyzer.md) · [Copilot prompt](skills/meeting-analyzer.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/meeting-analyzer) |
| **summarize-meeting**<br><sub>core 8,603 chars · too long for most instruction boxes: attach the file</sub> | Summarize one meeting into decisions, action items with owners, and open questions. | "Summarize this transcript into decisions, action items with owners and due dates, and open questions." | [Any AI (.md)](skills/summarize-meeting.md) · [Copilot prompt](skills/summarize-meeting.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/summarize-meeting) |
| **test-scenarios**<br><sub>core 7,949 chars · too long for most instruction boxes: attach the file</sub> | Write QA test cases from a spec, including edge, error and security paths. | "Write test scenarios for a new expense-claim form: upload receipt, pick cost center, submit for approval." | [Any AI (.md)](skills/test-scenarios.md) · [Copilot prompt](skills/test-scenarios.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/test-scenarios) |

## Monitor and report

*Know where the project really stands and tell people clearly.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **senior-pm**<br><sub>core 11,337 chars · too long for most instruction boxes: attach the file</sub> | Score portfolio health, risk exposure and resource capacity; frame executive status reports. | "Here are my 5 projects with budget, schedule and risk data. Score their health and draft the portfolio summary for the steering committee." | [Any AI (.md)](skills/senior-pm.md) · [Copilot prompt](skills/senior-pm.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/senior-pm) |
| **status-update-generator**<br><sub>core 9,688 chars · too long for most instruction boxes: attach the file</sub> | Write a weekly status update: RAG status, progress, risks and asks. | "Write this week's status update. We finished data migration testing, the vendor delivery slipped a week, and we need a decision on training dates." | [Any AI (.md)](skills/status-update-generator.md) · [Copilot prompt](skills/status-update-generator.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/status-update-generator) |
| **program-manager**<br><sub>core 8,567 chars · too long for most instruction boxes: attach the file</sub> | Coordinate several related projects: roadmap, dependencies, governance. | "I run a program of 4 projects that all feed a new billing system. Set up the governance and a monthly program review." | [Any AI (.md)](skills/program-manager.md) · [Copilot prompt](skills/program-manager.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/program-manager) |
| **cycle-time-analyzer**<br><sub>core 10,344 chars · too long for most instruction boxes: attach the file</sub> | Analyze cycle time and throughput to find where work gets stuck and forecast delivery. | "Here's an export of 60 tickets with start and done dates. Where does work get stuck, and when will the remaining 25 be done?" | [Any AI (.md)](skills/cycle-time-analyzer.md) · [Copilot prompt](skills/cycle-time-analyzer.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/cycle-time-analyzer) |
| **metrics-conversation**<br><sub>core 2,918 chars · fits an instructions box</sub> | Present delivery metrics to leadership without them being misused. | "My manager wants to compare teams by velocity. Help me explain why that backfires and what to show instead." | [Any AI (.md)](skills/metrics-conversation.md) · [Copilot prompt](skills/metrics-conversation.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/metrics-conversation) |

## Communicate and lead

*The right message to the right audience, and strong working relationships.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **roadmap-communication**<br><sub>core 9,841 chars · too long for most instruction boxes: attach the file</sub> | Produce executive, customer and internal versions of one roadmap. | "Turn our Q2 roadmap into three versions: a one-slide exec summary, a customer-facing note, and an internal team version." | [Any AI (.md)](skills/roadmap-communication.md) · [Copilot prompt](skills/roadmap-communication.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/roadmap-communication) |
| **team-communications**<br><sub>core 3,974 chars · fits an instructions box</sub> | Design how the team communicates: channels, meeting load, status structure, escalation. | "My team has 14 hours of recurring meetings a week. Redesign our communication setup to cut that in half." | [Any AI (.md)](skills/team-communications.md) · [Copilot prompt](skills/team-communications.prompt.md) · [Original](https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/team-communications) |
| **pm-1on1s**<br><sub>core 7,465 chars · fits an instructions box</sub> | Plan 1:1s with your manager, engineering leads and partners. | "Build an agenda for my first 1:1 with the new engineering manager on my project. Things are tense after a missed deadline." | [Any AI (.md)](skills/pm-1on1s.md) · [Copilot prompt](skills/pm-1on1s.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/career/pm-1on1s) |

## Launch and close

*Ship safely, tell people, learn from it.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **launch-playbook**<br><sub>core 8,554 chars · too long for most instruction boxes: attach the file</sub> | Coordinate a launch from 30 days before to 30 days after: owners, run-of-show, comms, rollback, retro. | "Build the launch plan for our new customer self-service portal going live in 4 weeks." | [Any AI (.md)](skills/launch-playbook.md) · [Copilot prompt](skills/launch-playbook.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/launch-playbook) |
| **beta-program**<br><sub>core 9,187 chars · too long for most instruction boxes: attach the file</sub> | Run a pilot or closed beta with exit criteria agreed before it starts. | "Plan a 6-week pilot of our new scheduling tool with 3 regional offices before company-wide rollout." | [Any AI (.md)](skills/beta-program.md) · [Copilot prompt](skills/beta-program.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/beta-program) |
| **feature-flag-strategy**<br><sub>core 9,642 chars · too long for most instruction boxes: attach the file</sub> | Plan a phased rollout with a kill switch. | "Plan a phased rollout of the new checkout flow: 5%, 25%, 100%, with clear rollback triggers." | [Any AI (.md)](skills/feature-flag-strategy.md) · [Copilot prompt](skills/feature-flag-strategy.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/feature-flag-strategy) |
| **release-notes**<br><sub>core 8,528 chars · too long for most instruction boxes: attach the file</sub> | Turn tickets and changelogs into release notes people will read. | "Turn this list of 18 closed tickets into release notes for business users. Put anything that changes their daily work first." | [Any AI (.md)](skills/release-notes.md) · [Copilot prompt](skills/release-notes.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/release-notes) |
| **eol-communication**<br><sub>core 7,468 chars · fits an instructions box</sub> | Retire a system or feature: dated milestones, migration path, messages per audience. | "We retire the old reporting tool on 30 September. Plan the announcements for power users, occasional users and managers." | [Any AI (.md)](skills/eol-communication.md) · [Copilot prompt](skills/eol-communication.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/eol-communication) |
| **post-mortem**<br><sub>core 10,228 chars · too long for most instruction boxes: attach the file</sub> | Run a blameless review after a missed launch, incident or failed project. | "Run a blameless post-mortem on our go-live that was rolled back after 6 hours." | [Any AI (.md)](skills/post-mortem.md) · [Copilot prompt](skills/post-mortem.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/post-mortem) |

## Work tools

*Get more out of Jira, Confluence and other work tools.*

| Skill | Use it when | Try this | Get it |
|---|---|---|---|
| **jira-expert**<br><sub>core 11,019 chars · too long for most instruction boxes: attach the file</sub> | Jira workflows, JQL queries, boards, dashboards and automation. | "Write JQL for all open bugs in projects PORTAL and API that have been in 'In Review' for more than 5 days." | [Any AI (.md)](skills/jira-expert.md) · [Copilot prompt](skills/jira-expert.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/jira-expert) |
| **confluence-expert**<br><sub>core 8,862 chars · too long for most instruction boxes: attach the file</sub> | Set up or clean up Confluence spaces, page trees, permissions and stale pages. | "Design a Confluence space structure for a program with 4 projects, a steering committee and a vendor." | [Any AI (.md)](skills/confluence-expert.md) · [Copilot prompt](skills/confluence-expert.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/confluence-expert) |
| **atlassian-templates**<br><sub>core 8,440 chars · too long for most instruction boxes: attach the file</sub> | Build reusable Jira issue and Confluence page templates people actually fill in. | "Create a Confluence template for a weekly project status page and a Jira template for a change request." | [Any AI (.md)](skills/atlassian-templates.md) · [Copilot prompt](skills/atlassian-templates.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/atlassian-templates) |
| **notion-pm**<br><sub>core 10,155 chars · too long for most instruction boxes: attach the file</sub> | Design Notion databases and views for projects, decisions and roadmaps. | "Design a Notion setup for tracking 10 projects with status, owner, RAG, risks and decisions." | [Any AI (.md)](skills/notion-pm.md) · [Copilot prompt](skills/notion-pm.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/notion-pm) |
| **linear-expert**<br><sub>core 11,255 chars · too long for most instruction boxes: attach the file</sub> | Set up Linear teams, cycles, projects and triage. | "Set up Linear for 3 teams that share one product, with a shared triage queue." | [Any AI (.md)](skills/linear-expert.md) · [Copilot prompt](skills/linear-expert.prompt.md) · [Original](https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/linear-expert) |

---

Skills are by their authors and keep their own licenses: see [LICENSES.md](LICENSES.md). Rebuild with `python3 tools/build_playbook.py` after editing `playbook/pm-playbook.json`.
