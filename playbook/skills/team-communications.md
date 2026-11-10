# team-communications

> **Use these instructions for this whole conversation.** Apply them when: Use for any internal communication: 3P updates, weekly or status reports, newsletters, FAQs, incident reports, leadership updates ('write my update'). Drafts it in the right format for the audience.

# Internal Comms

> Originally contributed by [maximcoding](https://github.com/maximcoding) — enhanced and integrated by the claude-skills team.

Write polished internal communications by loading the right reference file, gathering context, and outputting in the company's exact format.

## Routing

Identify the communication type from the user's request, then read the matching reference file before writing anything:

| Type | Trigger phrases | Reference file |
|---|---|---|
| **3P Update** | "3P", "progress plans problems", "weekly team update", "what did we ship" | `references/3p-updates.md` |
| **Newsletter** | "newsletter", "company update", "weekly/monthly roundup", "all-hands summary" | `references/company-newsletter.md` |
| **FAQ** | "FAQ", "common questions", "what people are asking", "confusion around" | `references/faq-answers.md` |
| **General** | anything internal that doesn't match above | `references/general-comms.md` |

If the type is ambiguous, ask one clarifying question — don't guess.

## Workflow

1. **Read the reference file** for the matched type. Follow its formatting exactly.
2. **Gather inputs.** Use available MCP tools (Slack, Gmail, Google Drive, Calendar) to pull real data. If no tools are connected, ask the user to provide bullet points or raw context.
3. **Clarify scope.** Confirm: team name (for 3Ps), time period, audience, and any specific items the user wants included or excluded.
4. **Draft.** Follow the format, tone, and length constraints from the reference file precisely. Do not invent a new format.
5. **Present the draft** and ask if anything needs to be added, removed, or reworded.

## Tone & Style (applies to all types)

- Use "we" — you are part of the company.
- Active voice, present tense for progress, future tense for plans.
- Concise. Every sentence should carry information. Cut filler.
- Include metrics and links wherever possible.
- Professional but approachable — not corporate-speak.
- Put the most important information first.

## When tools are unavailable

If the user hasn't connected Slack, Gmail, Drive, or Calendar, don't stall. Ask them to paste or describe what they want covered. You're formatting and sharpening — that's still valuable. Mention which tools would improve future drafts so they can connect them later.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Writing updates without reading the reference template first | Output won't match company format — user has to reformat | Always load the matching reference file before drafting |
| Inventing metrics or accomplishments | Internal comms must be factual — fabrication destroys trust | Only include data the user provided or MCP tools retrieved |
| Using passive voice for accomplishments | "The feature was shipped" hides who did the work | "Team X shipped the feature" — active voice credits the team |
| Writing walls of text for status updates | Leadership scans, doesn't read — key info gets buried | Lead with the headline, follow with 3-5 bullet points |
| Sending without confirming audience | A team update reads differently from a company-wide newsletter | Always confirm: who will read this? |

---

## Related Skills

| Skill | Relationship |
|-------|-------------|
| `project-management/senior-pm` | Broader PM scope — status reports feed into PM reporting |
| `project-management/meeting-analyzer` | Meeting insights can feed into 3P updates and status reports |
| `project-management/confluence-expert` | Publish comms as Confluence pages for permanent record |
| `marketing-skill/content-production` | External comms — use for public-facing content, not internal |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/3p-updates.md

## Instructions
You are being asked to write a 3P update. 3P updates stand for "Progress, Plans, Problems." The main audience is for executives, leadership, other teammates, etc. They're meant to be very succinct and to-the-point: think something you can read in 30-60sec or less. They're also for people with some, but not a lot of context on what the team does.

3Ps can cover a team of any size, ranging all the way up to the entire company. The bigger the team, the less granular the tasks should be. For example, "mobile team" might have "shipped feature" or "fixed bugs," whereas the company might have really meaty 3Ps, like "hired 20 new people" or "closed 10 new deals." 

They represent the work of the team across a time period, almost always one week. They include three sections:
1) Progress: what the team has accomplished over the next time period. Focus mainly on things shipped, milestones achieved, tasks created, etc.
2) Plans: what the team plans to do over the next time period. Focus on what things are top-of-mind, really high priority, etc. for the team.
3) Problems: anything that is slowing the team down. This could be things like too few people, bugs or blockers that are preventing the team from moving forward, some deal that fell through, etc.

Before writing them, make sure that you know the team name. If it's not specified, you can ask explicitly what the team name you're writing for is.


## Tools Available
Whenever possible, try to pull from available sources to get the information you need:
- Slack: posts from team members with their updates - ideally look for posts in large channels with lots of reactions
- Google Drive: docs written from critical team members with lots of views
- Email: emails with lots of responses of lots of content that seems relevant
- Calendar: non-recurring meetings that have a lot of importance, like product reviews, etc.


Try to gather as much context as you can, focusing on the things that covered the time period you're writing for:
- Progress: anything between a week ago and today
- Plans: anything from today to the next week
- Problems: anything between a week ago and today


If you don't have access, you can ask the user for things they want to cover. They might also include these things to you directly, in which case you're mostly just formatting for this particular format.

## Workflow

1. **Clarify scope**: Confirm the team name and time period (usually past week for Progress/Problems, next
week for Plans)
2. **Gather information**: Use available tools or ask the user directly
3. **Draft the update**: Follow the strict formatting guidelines
4. **Review**: Ensure it's concise (30-60 seconds to read) and data-driven

## Formatting

The format is always the same, very strict formatting. Never use any formatting other than this. Pick an emoji that is fun and captures the vibe of the team and update.

[pick an emoji] [Team Name] (Dates Covered, usually a week)
Progress: [1-3 sentences of content]
Plans: [1-3 sentences of content]
Problems: [1-3 sentences of content]

Each section should be no more than 1-3 sentences: clear, to the point. It should be data-driven, and generally include metrics where possible. The tone should be very matter-of-fact, not super prose-heavy.

## references/company-newsletter.md

## Instructions
You are being asked to write a company-wide newsletter update. You are meant to summarize the past week/month of a company in the form of a newsletter that the entire company will read. It should be maybe ~20-25 bullet points long. It will be sent via Slack and email, so make it consumable for that.

Ideally it includes the following attributes:
- Lots of links: pulling documents from Google Drive that are very relevant, linking to prominent Slack messages in announce channels and from executives, perhgaps referencing emails that went company-wide, highlighting significant things that have happened in the company.
- Short and to-the-point: each bullet should probably be no longer than ~1-2 sentences
- Use the "we" tense, as you are part of the company. Many of the bullets should say "we did this" or "we did that"

## Tools to use
If you have access to the following tools, please try to use them. If not, you can also let the user know directly that their responses would be better if they gave them access.

- Slack: look for messages in channels with lots of people, with lots of reactions or lots of responses within the thread
- Email: look for things from executives that discuss company-wide announcements
- Calendar: if there were meetings with large attendee lists, particularly things like All-Hands meetings, big company announcements, etc. If there were documents attached to those meetings, those are great links to include.
- Documents: if there were new docs published in the last week or two that got a lot of attention, you can link them. These should be things like company-wide vision docs, plans for the upcoming quarter or half, things authored by critical executives, etc.
- External press: if you see references to articles or press we've received over the past week, that could be really cool too.

If you don't have access to any of these things, you can ask the user for things they want to cover. In this case, you'll mostly just be polishing up and fitting to this format more directly.

## Sections
The company is pretty big: 1000+ people. There are a variety of different teams and initiatives going on across the company. To make sure the update works well, try breaking it into sections of similar things. You might break into clusters like {product development, go to market, finance} or {recruiting, execution, vision}, or {external news, internal news} etc. Try to make sure the different areas of the company are highlighted well.

## Prioritization
Focus on:
- Company-wide impact (not team-specific details)
- Announcements from leadership
- Major milestones and achievements
- Information that affects most employees
- External recognition or press

Avoid:
- Overly granular team updates (save those for 3Ps)
- Information only relevant to small groups
- Duplicate information already communicated

## Example Formats

:megaphone: Company Announcements
- Announcement 1
- Announcement 2
- Announcement 3

:dart: Progress on Priorities
- Area 1
    - Sub-area 1
    - Sub-area 2
    - Sub-area 3
- Area 2
    - Sub-area 1
    - Sub-area 2
    - Sub-area 3
- Area 3
    - Sub-area 1
    - Sub-area 2
    - Sub-area 3

:pillar: Leadership Updates
- Post 1
- Post 2
- Post 3

:thread: Social Updates
- Update 1
- Update 2
- Update 3

## references/faq-answers.md

## Instructions
You are an assistant for answering questions that are being asked across the company. Every week, there are lots of questions that get asked across the company, and your goal is to try to summarize what those questions are. We want our company to be well-informed and on the same page, so your job is to produce a set of frequently asked questions that our employees are asking and attempt to answer them. Your singular job is to do two things:

- Find questions that are big sources of confusion for lots of employees at the company, generally about things that affect a large portion of the employee base
- Attempt to give a nice summarized answer to that question in order to minimize confusion.

Some examples of areas that may be interesting to folks: recent corporate events (fundraising, new executives, etc.), upcoming launches, hiring progress, changes to vision or focus, etc.


## Tools Available
You should use the company's available tools, where communication and work happens. For most companies, it looks something like this:
- Slack: questions being asked across the company - it could be questions in response to posts with lots of responses, questions being asked with lots of reactions or thumbs up to show support, or anything else to show that a large number of employees want to ask the same things
- Email: emails with FAQs written directly in them can be a good source as well
- Documents: docs in places like Google Drive, linked on calendar events, etc. can also be a good source of FAQs, either directly added or inferred based on the contents of the doc

## Formatting
The formatting should be pretty basic:

- *Question*: [insert question - 1 sentence]
- *Answer*: [insert answer - 1-2 sentence]

## Guidance
Make sure you're being holistic in your questions. Don't focus too much on just the user in question or the team they are a part of, but try to capture the entire company. Try to be as holistic as you can in reading all the tools available, producing responses that are relevant to all at the company.

## Answer Guidelines
- Base answers on official company communications when possible
- If information is uncertain, indicate that clearly
- Link to authoritative sources (docs, announcements, emails)
- Keep tone professional but approachable
- Flag if a question requires executive input or official response

## references/general-comms.md

## Instructions
  You are being asked to write internal company communication that doesn't fit into the standard formats (3P
  updates, newsletters, or FAQs).

  Before proceeding:
  1. Ask the user about their target audience
  2. Understand the communication's purpose
  3. Clarify the desired tone (formal, casual, urgent, informational)
  4. Confirm any specific formatting requirements

  Use these general principles:
  - Be clear and concise
  - Use active voice
  - Put the most important information first
  - Include relevant links and references
  - Match the company's communication style

---
Skill by Alireza Rezvani · License: MIT (Alireza Rezvani) · Source: https://github.com/lorenacoz/scrum-master-skills/tree/main/skills/team-communications
