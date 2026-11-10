# summarize-meeting

> **Use these instructions for this whole conversation.** Apply them when: Turns meeting notes or transcripts into a summary of decisions, owned and dated action items, and open questions. Use when writing up a meeting, a recap email or a decision log; for patterns across a series use meeting-analyzer.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Meeting Summary Expert

## Overview

Transform meeting notes, transcripts, or recordings into clear, actionable summaries. Every summary follows a consistent structure that makes it easy for attendees and non-attendees alike to understand what was discussed, what was decided, and who is doing what by when.

**Done looks like:** every decision is numbered with who made it and why; every action item has one owner, a concrete deliverable and a calendar date; open questions have an owner; nothing is invented that the notes do not support (mark gaps as `[owner?]` or `[date?]` and ask).

## When to Use

- **After any meeting** where decisions were made or actions were assigned.
- **Sprint ceremonies** -- planning, retro, backlog refinement, sprint review.
- **Stakeholder meetings** -- steering committees, executive reviews, client calls.
- **Ad-hoc discussions** -- when an impromptu conversation produces commitments that need tracking.

For accountability across a recurring series (who keeps missing commitments, which meetings never decide anything), use `../../meeting-analyzer/` instead.

## Clarify First

Before summarizing, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **The source material and its fidelity:** raw notes, transcript, or recording (summary quality is bounded by input; missing owners/dates for action items cannot be invented).
- **Meeting type:** planning, retro, steering committee, or client call (tailors discussion synthesis and which decisions matter).
- **Distribution scope + confidentiality:** attendees, non-attendees, or execs, and any sensitivity limits (determines whether standard 24-hour distribution applies).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Tools

Once summaries are captured as JSON (one object per meeting under `meetings`), three tools check them. All read `--meetings FILE`, print text or `--format json` (`--json` is the same), and `--example` prints a valid input.

| Tool | Checks |
|------|--------|
| `action_item_tracker.py` | Completion rate, overdue items, owners with the most open work, items with no owner or date. `--as-of YYYY-MM-DD` sets the date for overdue checks; it defaults to the latest meeting date so old notes give a stable result. |
| `decision_log_builder.py` | Numbered decision log (`DEC-YYYYMMDD-NNN`), rationale coverage, high-impact decisions marked reversible. `--search TEXT` filters by keyword. |
| `meeting_effectiveness_scorer.py` | 0-100 per meeting from decisions, owned/dated actions, time per output, agenda coverage and attendee count. |

```bash
python3 scripts/action_item_tracker.py \
  --meetings assets/sample_meetings.json
python3 scripts/decision_log_builder.py \
  --meetings assets/sample_meetings.json --search postgres
python3 scripts/meeting_effectiveness_scorer.py \
  --meetings assets/sample_meetings.json --format json
```

On the sample: 5 actions, 2 done, 1 overdue (Carol, 4 days as of 2026-03-14), 1 with no owner or date; 3 decisions with 67% rationale coverage; the status sync with eight people, no agenda and no decision scores lowest.

**Exit codes:** `0` report produced · `2` missing or unreadable file, invalid JSON, or the wrong shape (top level not an object, `meetings` not a list). The tools report findings; they do not gate.

## Anti-Patterns

### Posting an AI summary without review
**Mistake:** A transcription tool's auto-summary is posted as the official summary, with nobody checking it.
**Why it happens:** The output looks finished, and the 24-hour distribution window pushes people to send it as is.
**Instead:** Treat any machine-generated summary as a draft. Someone who attended checks names, who decided what, and whether each action item was actually agreed, then adds a "reviewed by" line. No "reviewed by" line means it is still a draft.

### Sensitive details sent to a wide list
**Mistake:** A summary that goes beyond the attendees includes personnel feedback, a customer's commercial terms, or in-flight legal language.
**Why it happens:** The summarizer captures everything said in the room, and the distribution list is set by habit.
**Instead:** If anyone outside the meeting is on the distribution list, run a redaction pass before sending. Confirm confidentiality limits up front (see Clarify First). Once the email is sent, you cannot recall it.

### Pasting the transcript as the summary
**Mistake:** The "summary" is four pages of who said what.
**Why it happens:** Copying the transcript feels safe because nothing is left out.
**Instead:** Compress it into the template's sections: discussion points, numbered decisions, action items and open questions. If the summary runs past a page of named-speaker dialogue, cut it down.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## Reference Documentation

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/summarization-process.md](references/summarization-process.md)** — the full six-step methodology (metadata → discussion → actions → decisions → open questions → distribute), the output template, focus priorities, troubleshooting table, and success criteria. Read when producing a summary.
- **[references/meeting-facilitation-guide.md](references/meeting-facilitation-guide.md)** — meeting types, note-taking strategies, and anti-patterns. Read to tailor the summary to the meeting type or improve input quality.
- **[references/red-flags.md](references/red-flags.md)** — common ways summaries go wrong with bad/good examples. Read before posting, emailing, or linking a summary.
- **[assets/meeting_summary_template.md](assets/meeting_summary_template.md)** — ready-to-use fill-in template. Use to draft the summary directly.

## Scope & Limitations

**In Scope:** Capturing meeting metadata, extracting key discussion points, documenting decisions with rationale, recording action items with owners and due dates, capturing open questions, distributing summaries, maintaining consistent naming conventions and storage.

**Out of Scope:** Meeting facilitation and agenda design, real-time transcription (use a transcription tool as input), project status tracking (hand off to `../jira-expert/`), strategic decision frameworks (hand off to `../senior-pm/`), recording or video management.

**Limitations:** Summary quality is bounded by the quality of input notes or transcript. Automated transcription tools may introduce errors that the summarizer must catch. The skill does not replace the need for a skilled facilitator -- poorly run meetings produce poor summaries regardless of template quality. Sensitive or confidential meetings may require restricted distribution that the standard workflow does not address.

## Integration Points

| Integration | Direction | What Flows |
|-------------|-----------|------------|
| `wwas/` | Meetings -> WWAS | Decisions and commitments from meetings become WWAS backlog items |
| `job-stories/` | Meetings -> Stories | Discovery discussions surface situations and motivations for job stories |
| `../jira-expert/` | Meetings -> Jira | Action items create Jira tickets; decisions update issue comments |
| `../confluence-expert/` | Meetings -> Confluence | Summaries stored in Confluence using meeting notes template |
| `../senior-pm/` | Meetings -> PM | Steering committee and stakeholder meeting summaries feed portfolio reporting |
| `../delivery-manager/` | Meetings -> DM | Release planning and incident review meeting outcomes feed delivery tracking |

## Files

| File | Purpose |
|------|---------|
| `scripts/action_item_tracker.py` | Action completion, overdue and ownership report |
| `scripts/decision_log_builder.py` | Decision log with rationale coverage |
| `scripts/meeting_effectiveness_scorer.py` | Per-meeting effectiveness score |
| `assets/sample_meetings.json` | Three meetings that exercise all three tools |
| `assets/meeting_summary_template.md` | Fill-in summary template |
| `examples/product-review-may-22.md` | Worked summary |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/meeting-facilitation-guide.md

# Meeting Facilitation Guide

## Meeting Types and Best Practices

### Decision Meetings

**Purpose:** Make a specific decision with the right stakeholders in the room.

**Best practices:**
- State the decision to be made in the meeting invite.
- Share pre-read materials at least 24 hours in advance.
- Timebox discussion. If no decision after the allotted time, explicitly decide to defer and state what additional information is needed.
- End with a clear statement of the decision and who will communicate it.

**Summary focus:** The decision, the rationale, and the communication plan.

### Status / Update Meetings

**Purpose:** Align the team on progress, blockers, and next steps.

**Best practices:**
- Keep to 30 minutes or less.
- Use a standing agenda (same structure each time).
- Focus on exceptions -- what is off track, what needs help.
- Do not use the meeting to share information that could be read asynchronously.

**Summary focus:** Blockers, changes to plan, and escalations.

### Brainstorming / Working Sessions

**Purpose:** Generate ideas or solve a problem collaboratively.

**Best practices:**
- Define the problem statement before the meeting.
- Separate idea generation from idea evaluation.
- Use structured techniques (brainwriting, round-robin, dot voting).
- Capture all ideas, even ones not selected.

**Summary focus:** Ideas generated, criteria used to evaluate, and which ideas move forward.

### Planning Meetings

**Purpose:** Agree on scope, timeline, and assignments for upcoming work.

**Best practices:**
- Come with a draft plan, not a blank slate.
- Walk through dependencies and risks.
- Assign owners to every deliverable.
- Confirm the next checkpoint.

**Summary focus:** Commitments (who, what, when), dependencies, and risks.

### Retrospectives

**Purpose:** Reflect on what worked, what did not, and what to change.

**Best practices:**
- Create psychological safety -- no blame, focus on systems.
- Use a structured format (Start-Stop-Continue, 4Ls, Mad-Sad-Glad).
- Limit to 3 actionable improvements per retro.
- Assign owners to improvement actions.

**Summary focus:** Top improvement actions with owners and due dates.

## Note-Taking Strategies

### The Cornell Method (Adapted for Meetings)

Divide your notes into three sections:

1. **Main notes** (during meeting) -- Capture discussion points as they happen.
2. **Key takeaways** (margin) -- Flag decisions, actions, and questions in real-time.
3. **Summary** (bottom) -- Write a 2-3 sentence summary immediately after the meeting.

### Real-Time Action Tagging

As you take notes, prefix actionable items with tags:

- `[ACTION]` -- Something someone needs to do
- `[DECISION]` -- Something that was decided
- `[QUESTION]` -- Something unresolved
- `[RISK]` -- A risk or concern raised
- `[PARKING]` -- Off-topic item to revisit later

This makes post-meeting processing much faster.

### Collaborative Note-Taking

For important meetings, use a shared document where multiple participants contribute:

- One person captures discussion points.
- Another captures actions and decisions.
- Participants correct or clarify in real-time.
- Reduces single-point-of-failure and improves accuracy.

## Action Item Best Practices (SMART Format)

Every action item should be SMART:

| Criterion | Question | Bad Example | Good Example |
|-----------|----------|-------------|--------------|
| **Specific** | What exactly needs to be done? | "Look into the performance issue" | "Profile the dashboard API endpoint and identify the top 3 bottlenecks" |
| **Measurable** | How will we know it is done? | "Improve onboarding" | "Reduce onboarding flow from 8 steps to 5 steps" |
| **Assignable** | Who is the single owner? | "The team will handle it" | "Maria will handle it" |
| **Realistic** | Can it be done in the timeframe? | "Rewrite the entire backend by Friday" | "Draft the migration plan by Friday" |
| **Time-bound** | What is the deadline? | "Do it soon" | "Complete by March 15" |

## Follow-Up Processes

### Within 24 Hours

1. Finalize and distribute the meeting summary.
2. Create tickets for action items in your tracking system (Jira, Linear, Asana).
3. Update any affected project plans or roadmaps.

### At the Next Meeting

1. Review open actions from the previous meeting.
2. Mark completed items and escalate overdue items.
3. Carry forward unresolved questions.

### Weekly

1. Review all open action items across meetings.
2. Follow up with owners on items approaching their due date.
3. Escalate blocked items.

## Meeting Anti-Patterns

### The Status Meeting That Should Be an Email

**Symptom:** Participants take turns reading updates that could be shared asynchronously.
**Fix:** Use async updates (Slack, email, dashboard) and reserve meeting time for discussion of exceptions and decisions.

### The Meeting Without a Decision

**Symptom:** Lots of discussion, no clear outcome. Same topic appears in the next meeting.
**Fix:** State the decision to be made upfront. If the group cannot decide, explicitly state what information is needed and who will gather it.

### The Meeting With Too Many People

**Symptom:** Most attendees are silent. Side conversations happen. Decisions are deferred because "we need to check with so-and-so."
**Fix:** Invite only decision-makers and direct contributors. Share the summary with everyone else.

### The Meeting Without an Agenda

**Symptom:** Discussion meanders. Important topics get squeezed at the end or skipped entirely.
**Fix:** Every meeting invite must include an agenda with time allocations. No agenda, no meeting.

### The Meeting That Runs Over

**Symptom:** Meetings consistently exceed their scheduled time, causing cascading delays.
**Fix:** Appoint a timekeeper. When time is up, decide to either extend (with consent) or schedule a follow-up. Do not silently run over.

### Missing Follow-Through

**Symptom:** Action items are captured but never tracked. The same issues resurface weeks later.
**Fix:** Review previous action items at the start of every recurring meeting. Use a tracking system, not just meeting notes.

## references/red-flags.md

# Red Flags: Summarize Meeting

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every meeting summary before posting / emailing / linking it in Jira / Confluence. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Minutes Without Owners

**Symptom.** "Action items: follow up with vendor, refine the spec, schedule next session."
**Why it's bad.** An action without an owner has no owner. It defaults to the meeting organizer or it dies. Either way, the team is not aligned and the next meeting starts with re-litigation of the same items.
**Bad example:**
> "Action items:
> - Follow up with vendor on SDK breaking change.
> - Refine spec for integration.
> - Schedule next sync."
**Good example:**
> "Action items:
> 1. Follow up with vendor on SDK breaking change. **Owner**: <name>. **Due**: Tue Jun 4.
> 2. Refine spec for integration. **Owner**: <name>. **Due**: Fri Jun 7.
> 3. Schedule next sync. **Owner**: <name>. **Due**: end of day."
**How to catch it.** Action items with no owner column = re-draft before sending.

---

## Red Flag 2: Decisions Buried in Narrative

**Symptom.** "We had a long discussion about the vendor situation, and after weighing options the team felt that switching might be wise."
**Why it's bad.** Decisions are the highest-value output of any meeting. Burying them in prose means people scan the summary, miss the decision, and proceed as if it had not been made. Worse, the wording is ambiguous -- did the team decide to switch, or to consider switching?
**Bad example:**
> "Discussion: the team weighed pros and cons of switching vendors. There were concerns about timeline. Ultimately the leaning was towards switching, though some open questions remain."
**Good example:**
> "**Decision**: switch from Vendor A to Vendor B by July 15.
> **Owner**: <name>.
> **Rationale**: Vendor A's SDK breaking change adds 4 weeks; Vendor B has a confirmed integration path.
> **Open questions**: contractual termination clause with Vendor A (legal owns; due Tue)."
**How to catch it.** Every decision must appear in its own labeled block (Decision / Owner / Rationale / Open Questions). Prose summaries hide decisions; surface them.

---

## Red Flag 3: No Distinction Between Decisions, Discussions, and Action Items

**Symptom.** Summary is one bulleted list mixing decisions, talking points, and to-dos.
**Why it's bad.** Each type of artifact has different downstream consumers. Decisions need to be archived as part of the decision log. Action items need to be tracked in Jira / Linear. Discussion items are just context. Mixing them means nothing is tracked properly.
**Bad example:**
> "- Vendor A is having issues.
> - Switch to Vendor B.
> - <name> will contact Vendor B.
> - Cost concern raised.
> - PM thinks we should defer."
**Good example:**
> "**Decisions** (logged in `decision-log.md`):
> - DEC-117: switch from Vendor A to Vendor B by July 15.
>
> **Action items** (logged in Jira):
> - <name>: contact Vendor B by Tue. Tracked: PROJ-422.
>
> **Discussion notes** (for context, not actionable):
> - Vendor A's SDK breaking change adds 4 weeks.
> - Cost differential is ~5%."
**How to catch it.** Single mixed list = restructure into three sections.

---

## Red Flag 4: Verbatim Transcript Pasted as Summary

**Symptom.** The summary is a 4-page transcript of who said what.
**Why it's bad.** A transcript is raw data, not a summary. It buries the signal in noise. People will not read it. Action items get lost. The whole point of the summary -- to compress -- is defeated.
**Bad example:**
> "Sarah: 'I think we should switch.'
> Tom: 'I disagree, switching costs are too high.'
> Sarah: 'But the breaking change blocks us.'
> [3 more pages of dialog]"
**Good example:**
> "Topic: vendor switch.
> Positions: Sarah advocated switching (citing 4-week delay if we stay); Tom raised switching costs (~$80k, 1-month transition).
> Decision: see DEC-117 (switch by July 15)."
**How to catch it.** Summary > 1 page of dialog with named speakers = compress.

---

## Red Flag 5: No Date or Attendees

**Symptom.** Summary headline: "Vendor discussion." No date, no attendee list.
**Why it's bad.** Six weeks later, when someone references "the vendor decision", nobody can tell which meeting. Decisions cannot be traced. Attendees who were quoted cannot be checked. The summary is unciteable.
**Bad example:**
> "# Vendor discussion
> Decisions: switch to Vendor B.
> ..."
**Good example:**
> "# Vendor discussion -- 2026-05-21 14:00 UTC
> **Attendees**: <name (chair)>, <name>, <name>. **Apologies**: <name>.
> **Linked context**: PROJ-419 (vendor evaluation), DEC-117 (this decision).
> ..."
**How to catch it.** Top of summary must have date + attendees + linked context. No exceptions.

---

## Red Flag 6: Sensitive Information Not Redacted

**Symptom.** Summary shared widely contains personnel feedback, customer-specific commercial terms, or in-flight legal language.
**Why it's bad.** Meeting summaries are circulated broadly. Including sensitive content leaks confidential information, harms trust, and may breach contracts. Once the email is sent, you cannot recall it.
**Bad example:**
> "Notes mention: 'Customer X is willing to pay 30% above list; we should not surface this'."
**Good example:**
> "Two summaries from the same meeting:
> - **Public** (shared with the project channel): topics, decisions, action items, redacted of commercials and personnel matters.
> - **Confidential** (shared only with attendees): full notes including commercial terms.
> Generator has a `--sensitivity public|confidential` flag."
**How to catch it.** Distribution list includes anyone outside the meeting = run a redaction pass.

---

## Red Flag 7: Summary Does Not Link Back to Source Artifacts

**Symptom.** "Decided to update the PRD" -- but no link to the PRD, no version reference.
**Why it's bad.** Decisions reference artifacts that change over time. Without a link, the reader has to hunt; with a stale link, the reader sees the wrong version. Either way, the decision is unmoored from the context it was made in.
**Bad example:**
> "Decision: update the PRD to reflect the new scope."
**Good example:**
> "Decision: update the PRD to reflect the new scope.
> **Source PRD**: `confluence://PROJ/prd-bulk-edit` (version as of meeting: `v1.4`, May 18 2026).
> **Owner**: <name>. **Due**: Fri Jun 4. New version expected: `v2.0`."
**How to catch it.** Decision references an artifact without a link + version = re-edit.

---

## Red Flag 8: Action Items With No Due Date

**Symptom.** "Follow up with marketing on launch copy. (No due date.)"
**Why it's bad.** Without a due date, the action item is open-ended and immediately becomes the lowest-priority thing on the owner's plate. By the next meeting, it has not been done, and the team re-discusses the same item.
**Bad example:**
> "Action: <name> follows up with marketing on launch copy."
**Good example:**
> "Action: <name> follows up with marketing on launch copy. **Due**: Fri Jun 7. **Definition of done**: a draft of the launch headline + 3 supporting paras committed to `confluence://LAUNCH/copy`."
**How to catch it.** No due date = unbounded = will not happen.

---

## Red Flag 9: Summary Generated From Audio Without Human Review

**Symptom.** AI-generated meeting transcript posted directly as summary, without anyone correcting hallucinations or mis-attributions.
**Why it's bad.** Auto-generated summaries hallucinate names, mis-attribute decisions, and sometimes invent action items that were never discussed. Posting them unreviewed propagates the errors as if they were authoritative.
**Bad example:**
> "AI-generated summary auto-posted to Slack. Includes a 'decision' that was actually a hypothetical. Two action items attributed to wrong owners."
**Good example:**
> "AI-generated draft summary is the *starting point*. The meeting chair reviews within 24h, corrects mis-attributions, removes hypotheticals, and validates owner / due-date for each action. Final summary marked `reviewed by <name>`."
**How to catch it.** No 'reviewed by' line = treat as draft, not summary.

---

## Red Flag 10: No Next-Steps or Next-Meeting Trigger

**Symptom.** Summary ends with action items but no plan for follow-up.
**Why it's bad.** Meetings often spawn next meetings or check-in points. Without explicit next-step triggers, the work stalls between meetings, and the decision-to-action gap grows.
**Bad example:**
> "Action items: <list>. End of summary."
**Good example:**
> "**Next steps**:
> - Action items tracked in Jira; updated weekly in #proj-status.
> - Mid-point check-in: Wed Jun 12, 14:00 UTC (calendar invite sent).
> - Final review: end of June, at the next vendor steering committee."
**How to catch it.** No next meeting / check-in trigger = add one before sending.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Minutes without owners | Every action item has Owner + Due Date |
| 2 | Decisions buried in narrative | Each decision in its own labeled block |
| 3 | Mixed lists | Decisions / Actions / Discussion separated |
| 4 | Verbatim transcript | Summary > 1 page of dialog = compress |
| 5 | No date / attendees | Top of summary has both |
| 6 | Sensitive info not redacted | `--sensitivity` flag used appropriately |
| 7 | No links back | Each artifact reference includes link + version |
| 8 | Actions without due dates | Every action has a date + definition of done |
| 9 | AI-generated unreviewed | 'Reviewed by' line present |
| 10 | No next-steps trigger | Explicit next meeting / check-in point |

## Related Reading

- `SKILL.md` -- structured meeting summary template
- `references/decision-log-format.md` -- how decisions get archived
- Sibling skill: `execution/daci-framework/` -- decision rights for high-stakes meetings
- Sibling skill: `execution/status-update-generator/` -- weekly status reuses meeting decisions
- Sibling skill: `senior-pm/` (stakeholder mapping) -- audience considerations for distribution
- Sibling skill: `sprint-retrospective/` -- retro outputs follow the same pattern

## references/summarization-process.md

# Summarization Process — Methodology, Template, Troubleshooting

> Read this when producing a meeting summary: the six-step methodology, the output template, focus priorities, troubleshooting table, and success criteria. Pair with `meeting-facilitation-guide.md` and `red-flags.md`.

## Methodology

### Step 1: Capture Meeting Metadata

Record the essential context:

| Field | Description |
|-------|-------------|
| **Date** | Meeting date (YYYY-MM-DD) |
| **Time** | Start and end time with timezone |
| **Participants** | Names and roles (e.g., "Sarah Chen, Product Lead") |
| **Topic** | One-line meeting purpose |
| **Location** | Room name, video link, or "async" |

### Step 2: Extract Key Discussion Points

From the raw notes or transcript, identify the substantive topics discussed. Guidelines:

- **Summarize, do not transcribe.** Capture the essence of each topic in 1-3 bullet points.
- **Use plain language.** Avoid jargon. Anyone reading the summary should understand the points without having attended.
- **Focus on what matters.** Skip small talk, repeated points, and tangential discussions.
- **Note disagreements.** If there was significant debate, capture the key positions and how they were resolved (or not).

### Step 3: Extract Action Items

Every action item must answer three questions:

1. **Who** is responsible? (Single owner, not a team)
2. **What** specifically must they do? (Concrete, observable deliverable)
3. **By when?** (Specific date, not "soon" or "next sprint")

Format as a table:

| Due Date | Owner | Action |
|----------|-------|--------|
| 2026-03-10 | Sarah Chen | Share revised wireframes with the design team |
| 2026-03-07 | James Park | Schedule load test for the staging environment |

**Action item quality checks:**

- Each action has exactly one owner (not "Sarah and James")
- The deliverable is specific enough to verify completion
- The due date is a calendar date, not a relative timeframe
- Actions use active verbs: "share," "schedule," "draft," "review," "decide"

### Step 4: Record Decisions

List each decision made during the meeting as a numbered item. Include enough context that someone who was not present understands the decision and its rationale.

**Format:**

1. **[Decision]** -- [Brief rationale or context]. Decided by [who].
2. **[Decision]** -- [Brief rationale or context]. Decided by [who].

**Examples:**

1. **Launch date set for April 15** -- Allows two full sprints for QA after feature freeze on March 28. Decided by steering committee.
2. **Use PostgreSQL instead of MongoDB for the analytics service** -- Team consensus based on query pattern analysis showing 80% relational queries. Decided by engineering leads.

### Step 5: Capture Open Questions

List unresolved questions that need follow-up. For each question, note who is expected to provide an answer and by when, if known.

1. Do we need a separate staging environment for the new analytics service? (James to investigate by March 10)
2. What is the budget ceiling for the Q2 marketing campaign? (Pending finance review)

### Step 6: Save and Distribute

**File naming convention:** `Meeting-Summary-[YYYY-MM-DD]-[topic-slug].md`

Examples:
- `Meeting-Summary-2026-03-04-sprint-planning.md`
- `Meeting-Summary-2026-03-04-q2-roadmap-review.md`

**Distribution:**
- Share the summary within 24 hours of the meeting.
- Send to all participants and relevant stakeholders who were not present.
- Store in the team's shared documentation space (Confluence, Notion, shared drive).

## Output Template

```markdown
# Meeting Summary

## Metadata

| Field | Value |
|-------|-------|
| **Date** | [YYYY-MM-DD] |
| **Time** | [HH:MM] - [HH:MM] [TZ] |
| **Participants** | [Name, Role]; [Name, Role]; ... |
| **Topic** | [One-line meeting purpose] |

## Summary

- [Key discussion point 1]
- [Key discussion point 2]
- [Key discussion point 3]

## Action Items

| Due Date | Owner | Action |
|----------|-------|--------|
| [YYYY-MM-DD] | [Name] | [Specific, verifiable action] |

## Decisions Made

1. **[Decision]** -- [Rationale]. Decided by [who].

## Open Questions

1. [Question]? ([Who is expected to answer, by when])
```

## What to Focus On

When summarizing, prioritize:

- **Decisions that affect roadmap or strategy** -- These have the broadest impact and are most likely to be referenced later.
- **Who does what by when** -- Accountability is the primary value of a meeting summary.
- **Blockers and risks surfaced** -- These need visibility beyond the meeting room.
- **Changes to previously agreed plans** -- These create confusion if not documented.

When summarizing, deprioritize:

- Status updates that are available elsewhere (Jira, dashboards)
- Repetition of information already documented
- Social conversation and small talk
- Detailed technical discussions better captured in design docs

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| Action items are assigned to teams instead of individuals | Culture avoids individual accountability; facilitator does not press for a single owner | Enforce the "one owner" rule during the meeting; if a team is named, ask "Who on that team is the single point of contact?" |
| Summaries are too long and nobody reads them | Summarizer includes too much detail; tries to capture everything | Apply the "would someone who missed the meeting need this?" filter to every bullet point; target 1 page maximum for 1-hour meetings |
| Decisions are not documented, leading to re-litigation in future meetings | Meeting moved quickly; facilitator focused on discussion, not decisions | Pause after each decision and state it aloud: "Let me confirm: we decided X because Y"; add decision capture as a facilitator checklist item |
| Action items have vague due dates ("soon", "next sprint") | Facilitator does not push for specificity; team uncomfortable committing to dates | Require a calendar date for every action; if the team cannot commit, set a date to decide the date |
| Summaries are distributed days after the meeting | Summarizer is overburdened or perfectionist | Set a 24-hour distribution rule; use a structured template to reduce writing effort; assign summary responsibility before the meeting |
| Open questions from previous meetings are never resolved | No follow-up mechanism; questions captured but not tracked | Add "Previous Open Questions" as a standing agenda item; assign each question an owner and a resolution date |
| Attendees disagree with the summary after distribution | Summary reflects summarizer's interpretation, not group consensus | Share key decisions and action items verbally at the meeting close; invite corrections within 24 hours of distribution |

## Success Criteria

- 100% of meetings with decisions or action items produce a written summary within 24 hours
- Every action item has a single named owner and a specific calendar due date
- Action item completion rate exceeds 80% by the stated due date
- Summaries are 1 page or less for meetings under 1 hour
- Decisions are documented with enough context that a non-attendee can understand the rationale
- Open questions from previous meetings are tracked and resolved within 2 meeting cycles
- Meeting summary satisfaction (from periodic team survey) averages 4+/5

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/summarize-meeting
