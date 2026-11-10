---
description: "Builds 1:1 agendas and kickoff scripts for a PM's manager, EM, designer, reports and cross-functional partners. Use when starting a new 1:1, a 1:1 has turned into status updates, or you need to give a partner hard feedback."
---

# PM 1:1 Expert

## Overview

PMs run more 1:1s than almost any other role: with their manager, their engineering manager partner, their design lead, cross-functional partners (sales, support, data), and -- once they have reports -- with their direct PMs. Each 1:1 type has a different purpose, cadence, and ideal structure.

The value here is the partner-specific agendas, question banks and cadence rules in `assets/` and `references/`; apply the coaching frameworks you already know (Radical Candor, GROW) through them rather than restating them.

### Five core principles

1. **The 1:1 belongs to the other person** — their agenda first.
2. **Status updates do not need a 1:1** — write them async; reserve live time for trust, growth, judgment, feedback.
3. **Care personally, challenge directly** — avoid ruinous empathy and obnoxious aggression.
4. **Cadence matters** — weekly for direct partners, monthly for tier-3; don't skip, reschedule.
5. **Document agreements, not transcripts** — capture decisions and next steps.

### When to Use

- **Starting a new 1:1 relationship** -- use the kickoff template to set expectations.
- **Existing 1:1s feel transactional** -- adopt the structured partner-type template.
- **You manage other PMs** -- use the direct-report template for growth and feedback.
- **You partner with an EM, designer, or cross-functional lead** -- use the partner-type template.

### When NOT to Use

- Ad-hoc problem-solving meetings (treat as project meetings, not 1:1s).
- Performance management conversations (use a separate, manager-led structure).
- Initial intro meetings during onboarding -- use `pm-onboarding/` for those.

## Quick Start

The workflow, start to finish:

1. Settle the Clarify First inputs below.
2. New relationship: run `assets/kickoff_template.md`. Recurring: use the partner-type agenda from `references/one-on-one-templates.md` (`assets/manager_1on1_agenda.md` for your own manager).
3. Fill the agenda with the other person's topics first, then growth, feedback and decisions; move status to async.
4. Verify that the agenda fits the time slot, every item is something only a live conversation can do, and agreements from last time have an owner and a date in `assets/1on1_notes_template.md` before calling it done.

## Clarify First

Before drafting the 1:1 agenda, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Partner type:** your manager, EM partner, designer, direct report, or cross-functional lead (selects the agenda template and question bank).
- **Relationship stage:** brand-new vs steady-state (decides whether you run the kickoff script or the recurring agenda).
- **Purpose this session:** growth/feedback, alignment, or status-clearing (sets which sections matter and whether the Radical Candor frame applies).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Anti-Patterns

### Jumping to the solution
**Mistake:** The other person raises an issue and you answer with "you should..." within the first few minutes.
**Why it happens:** Giving the answer is faster and feels helpful.
**Instead:** Run GROW in order: Goal, Reality, Options, then Will. Ask first whether they want coaching questions or just want to be heard. Offering the fix up front builds dependency.

### No notes, no follow-through
**Mistake:** Nobody writes anything down, so agreed actions vanish and the same topics come back two weeks later.
**Why it happens:** The conversation felt clear at the time, so notes seem unnecessary.
**Instead:** Record agreements and next steps after every 1:1. Skip the transcript. Check: can you show four months of agreed actions for each 1:1 relationship? If not, your follow-through only exists in memory.

### Feedback that only flows down
**Mistake:** Your manager gives you feedback and you never give any back. Or you give feedback to your reports and never ask for theirs.
**Why it happens:** Upward feedback feels risky, and nobody puts it on the agenda.
**Instead:** Put upward feedback on the agenda on purpose. Over your last four 1:1s, aim for at least one piece of upward feedback. Use the Radical Candor frame: care personally, challenge directly.

Nine more, each with a bad and a good example: `references/red-flags.md`.

## References

Load the reference that matches the task; keep this file lean and pull detail on demand.

- **[references/one-on-one-templates.md](references/one-on-one-templates.md)** — the five core principles in full, per-partner agenda templates (manager, EM partner, designer, direct report, cross-functional), the kickoff conversation script, the Radical Candor feedback frame, the run-the-system workflow, troubleshooting table, and success criteria. Read this when designing or fixing any specific 1:1.
- **[references/1on1-playbook.md](references/1on1-playbook.md)** — deep dive on cadence by partner type, the three failure modes, and structuring manager / direct-report / EM / design / async 1:1s. Read when you want the underlying theory and quarterly-review discipline.
- **[references/red-flags.md](references/red-flags.md)** — bad-vs-good examples of agendas, notes, and question banks. Scan after drafting a 1:1 agenda or notes, before your next 1:1.
- `assets/kickoff_template.md` — script for kicking off a new 1:1 relationship.
- `assets/1on1_notes_template.md` — recurring 1:1 notes template.
- `assets/manager_1on1_agenda.md` — ready-to-use agenda for your manager 1:1.

External: Scott, K. *Radical Candor* (2017); Whitmore, J. *Coaching for Performance* (GROW); Auzenne & Horstman, *The Effective Manager* (Manager Tools 1:1).

## Scope & Limitations

**In Scope:** 1:1 templates for the 5 common PM partner types; the GROW coaching framework for direct reports; Radical Candor feedback; kickoff conversation script; notes/agenda templates.

**Out of Scope:** Formal performance management (PIP, terminations, reviews — requires HR); compensation conversations; skip-level design from the senior-leader perspective; career conversations beyond growth-plan refresh (use `pm-career-ladder/`).

**Caveats:** 1:1 patterns are culturally inflected — calibrate directness to the room. Templates are starting points that should evolve as the relationship deepens. Re-establish the kickoff conversation when you join a new team.

## Files

| File | Purpose |
|------|---------|
| `assets/kickoff_template.md`, `assets/manager_1on1_agenda.md`, `assets/1on1_notes_template.md` | Kickoff script, manager agenda, running notes |
| `references/one-on-one-templates.md`, `references/1on1-playbook.md`, `references/red-flags.md` | Agendas by partner type, cadence and question banks, failure modes |
| `examples/sr-pm-first-month-with-em-partner.md` | Worked first month with an EM partner |

Related skills: `pm-onboarding` for first-90-day intro meetings, `pm-career-ladder` for growth 1:1s, `senior-pm` (`stakeholder_mapper.py`) to decide who earns a weekly slot.

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/1on1-playbook.md

# 1:1 Playbook for PMs

A deep dive on cadence, structure, and the partner-type specifics that make PM 1:1s work.

---

## 1. Cadence by partner type

| Partner | Default cadence | Length | Format |
|---------|-----------------|--------|--------|
| Manager | Weekly | 30-45 min | Live; written prep |
| Skip-level | Quarterly | 30 min | Live |
| Engineering manager partner | Weekly | 30 min | Live |
| Design lead partner | Weekly to bi-weekly | 30 min | Live |
| Direct report (PM) | Weekly | 45-60 min | Live |
| Adjacent PM peer | Bi-weekly to monthly | 30 min | Live or async |
| Sales / GTM lead | Monthly | 30 min | Live |
| Customer Success lead | Monthly | 30 min | Live |
| Support lead | Monthly | 30 min | Live (or async during quiet periods) |
| Data / analytics partner | Bi-weekly | 30 min | Live |
| Marketing partner | Monthly | 30 min | Live |
| Legal / privacy partner | Quarterly | 30 min | Live (more during compliance events) |

The cadence is the floor, not the ceiling. During launches, incidents, or org changes, double the cadence temporarily.

---

## 2. The three failure modes

Across PM 1:1s, three failure modes dominate:

### Failure mode 1: The status meeting

The 1:1 becomes "what's happening on project X". The PM reads off the status update. The other person nods.

**Why it fails:** Status can be written. The 1:1 wastes scarce live time.

**Fix:** Move status to a written async update. Use the 1:1 for what cannot be written: trust, judgment, feedback, growth.

### Failure mode 2: Ruinous empathy

The PM cares deeply about the relationship but never delivers hard feedback. Issues accumulate. By the time the PM does say something, it lands as a surprise.

**Why it fails:** Feedback delayed is feedback compounded. Late feedback feels disproportionate even when it isn't.

**Fix:** Give the feedback in the next 1:1 after the moment. Use situation-behavior-impact framing.

### Failure mode 3: Solving instead of coaching

The PM (especially with direct reports) jumps to "here's what I'd do". The report's judgment doesn't grow.

**Why it fails:** Coaching is the multiplier; solving is the additive. A PM who coaches well develops 5x their own capacity.

**Fix:** Use GROW. Ask three questions before giving any answer.

---

## 3. Structuring the manager 1:1

The manager 1:1 is the most important 1:1 you run. Treat it with discipline.

### Pre-meeting (15 min, day of)

- Review your running 1:1 notes doc
- List 3 things you want from this 1:1
- Identify 1 piece of feedback you have for your manager (if relevant)
- Identify 1 growth question
- Send the agenda to your manager 30+ min before

### During the meeting

| Block | Content |
|-------|---------|
| Opening | "What's top of mind for you?" (Let them go first) |
| Your topics | The 3 things from prep |
| Feedback | One specific moment, situation-behavior-impact |
| Growth | One question that opens a longer conversation |
| Close | Confirm 2-3 action items, owner of each |

### After the meeting (5 min)

- Update the running notes doc
- Add action items to your task system
- If feedback was shared, send a written follow-up summarizing what you heard

---

## 4. Structuring the direct-report 1:1

If you manage PMs, this is the highest-leverage 1:1 you run.

### Default rules

1. **Their agenda first.** Even if you have a hot topic, ask "What's on your mind?" before your topic.
2. **Coach, don't solve.** Use GROW unless the question is purely factual.
3. **Make space for feedback both ways.** Always end with "What feedback do you have for me?"
4. **Track growth across cycles.** Bring up their growth plan monthly.

### Monthly growth conversation (replaces one weekly 1:1)

A deeper 60-minute conversation, with the growth plan as the agenda:

| Block | Time | Content |
|-------|------|---------|
| Check-in on the cycle theme | 5 min | "What's your read on how this month went against your cycle theme?" |
| Evidence and behaviors | 15 min | Walk through each focus area; capture new evidence |
| Calibration sense-check | 10 min | "Where do you think you'd be scored today? Where do I see you?" |
| Manager observation | 15 min | Manager-driven feedback on what's working and what's not |
| Adjustments | 10 min | Update experiments, evidence targets |
| Close | 5 min | Confirm next month's experiments |

### Quarterly rubric calibration

Use `pm-career-ladder/assets/gap_analysis.md` to score together.

### Annual career conversation

Use a separate planning session, not a 1:1 block. 60-90 minutes, calendar-blocked weeks in advance.

---

## 5. Structuring the EM partner 1:1

This is the relationship that most determines team velocity. Invest in it.

### Five questions to ask the EM partner monthly

1. "What am I doing that makes your team's life harder?"
2. "Where are we mis-aligned on priorities right now?"
3. "What's an opinion you have about the roadmap you haven't shared yet?"
4. "Where are you over-extended?"
5. "What's a piece of feedback for me you've been sitting on?"

### Partnership health quarterly review (60 min)

Once a quarter, run a longer 60-minute reset:

- What's working in our partnership?
- What's not working?
- Where are our decision rights ambiguous?
- What process should we change?
- What's our shared bar for the next quarter?

---

## 6. Structuring the design partner 1:1

Design 1:1s often slip toward project review. Resist.

### Three categories to rotate weekly

1. **Craft conversation** -- A design pattern, a competitor's UX, a quality bar discussion
2. **User research** -- What we've learned, what we should run next
3. **Project review** -- Current designs in flight (default fallback)

The strongest design partnerships spend 60%+ of 1:1 time on categories 1 and 2.

---

## 7. Async 1:1s

Sometimes a live 1:1 isn't possible. Async 1:1s can work for partner-of-partner relationships (adjacent PM peers, monthly cross-functional partners).

### Async 1:1 structure

Each person writes (in a shared doc) before a deadline:

- Top 2-3 things on my mind
- Anything I need from you
- Anything I want you to know

The other person responds inline within 24 hours. If a response sparks a longer thread, schedule a live 1:1.

### When async 1:1s fail

- Trust-building (impossible async)
- Coaching conversations (GROW needs live back-and-forth)
- Feedback delivery (always live, never async)
- High-stakes alignment (always live)

---

## 8. The "what to do when nothing's wrong" problem

Sometimes the 1:1 has no urgent topics. Three good defaults:

1. **Reflection question.** "What's one thing you've changed your mind about this quarter?"
2. **Trust-building.** Share something about your week that's not work.
3. **Strategic conversation.** "If we had no constraints, what would we build in this area?"

A 1:1 with no urgent agenda is an opportunity for the long-term work that gets crowded out otherwise.

---

## 9. Ending the 1:1

Strong closes have three elements:

1. **Recap the 2-3 action items.** Owner of each. Don't leave action items implicit.
2. **Confirm the next 1:1.** "Same time next week? Anything different we should plan for?"
3. **Closing exchange.** "Anything I can do for you in the next two weeks?"

The closing exchange signals partnership and reciprocity. It is the single most under-used 1:1 ritual.

---

## 10. Reviewing your 1:1s quarterly

Once a quarter, audit:

| Question | Action if "no" |
|----------|----------------|
| Are my 1:1s producing decisions and growth, or just status? | Adopt the partner-type templates |
| Am I giving regular hard feedback? | Schedule one feedback conversation per Tier-1 partner this month |
| Are my cancellation rates <10%? | Re-cadence; if you cancel 30%, the cadence is wrong |
| Do my direct reports leave 1:1s with a clearer next step (not a solved problem)? | Shift from solving to coaching with GROW |
| Do I get feedback from my reports / partners in 1:1s? | Ask explicitly; demonstrate non-defensiveness when they share once |

The 1:1 system that works for a PM at year 3 of the job will not work at year 6. Re-audit annually.

## references/one-on-one-templates.md

# PM 1:1 Templates, Feedback & Workflow

Read this when you need the full per-partner agenda templates, the Radical Candor feedback frame, the kickoff conversation script, the run-the-system workflow, or the troubleshooting/success-criteria detail. The SKILL.md keeps only the lean map; everything operational lives here.

---

## Core principles for PM 1:1s

Five principles that apply across all 1:1 types:

### 1. The 1:1 belongs to the other person

The default for a 1:1 with your manager: their agenda first. The default for a 1:1 with your report: their agenda first. PMs often invert this and turn 1:1s into status meetings; resist that.

### 2. Status updates do not need a 1:1

If the conversation is "here's what's happening on project X", that's a written update. The 1:1 is for what cannot be written: trust-building, growth, judgment calls, feedback.

### 3. Care personally, challenge directly (Radical Candor)

The strongest 1:1 relationships combine personal care with direct challenge. Avoid the two failure modes: "ruinous empathy" (care without challenge -- you never give hard feedback) and "obnoxious aggression" (challenge without care -- feedback feels brutal).

### 4. Cadence matters

Weekly is the default for direct working relationships. Bi-weekly for partner-of-partner. Monthly for tier-3 stakeholders. Cancelled 1:1s are an anti-pattern; reschedule, don't skip.

### 5. Document agreements, not transcripts

Capture what was decided and what the next step is. Don't transcribe the whole conversation -- it kills psychological safety.

## 1:1 type templates

### Type A: With your manager

**Cadence:** Weekly, 30-45 minutes.

**Default agenda:**

| Time | Section | Owner |
|------|---------|-------|
| 5 min | What's top of mind for you (your manager) | Manager |
| 15-20 min | What's top of mind for me | You |
| 5-10 min | Growth / longer-term discussion | Both |
| 5 min | Action items + next 1:1 | You |

**Your default questions for them:**

- "What feedback do you have for me from the past week?"
- "What's worrying you that you haven't shared?"
- "What's on your plate I could take off?"
- "How is leadership feeling about [project / area]?"

**Your default agenda items to raise:**

- One judgment call you're working through
- One piece of feedback you have for your manager (if relevant)
- One growth-related question
- One people-related update (team dynamic, hire, etc.)
- One escalation if needed

**What NOT to do:**

- Read off your status update
- Use the 1:1 to negotiate scope changes (do that async with a written proposal)
- Bring 8 topics (3-4 is the sweet spot)

### Type B: With your engineering manager partner

**Cadence:** Weekly, 30 minutes.

**Purpose:** Operational coordination, partnership health, escalations.

**Default agenda:**

| Time | Section |
|------|---------|
| 5 min | Personal check-in |
| 10 min | What's happening on shared projects |
| 10 min | What's worrying me / what's worrying you |
| 5 min | Actions for the week |

**Key questions:**

- "Is there anything I'm doing that's making your team's job harder?"
- "Where are you over-extended right now?"
- "What's an opinion you have about the roadmap you haven't shared yet?"
- "Where are we mis-aligned on priorities?"

**Topics to rotate weekly:**

- Roadmap and priorities
- Team health and capacity
- Technical debt and platform investments
- Quality (incidents, on-call, regression)
- Process changes
- Hiring

### Type C: With your design lead

**Cadence:** Weekly to bi-weekly, 30 minutes.

**Purpose:** Product quality, user research, craft conversations.

**Default agenda:**

| Time | Section |
|------|---------|
| 5 min | Personal check-in |
| 10 min | Current designs in flight |
| 10 min | User research / craft conversation |
| 5 min | Actions |

**Key questions:**

- "Is there a design direction we should debate that we haven't?"
- "Where am I over- or under-specifying in PRDs?"
- "What user research should we be running that we're not?"
- "What's a customer pain that's nagging you?"

### Type D: With a direct report (PM)

**Cadence:** Weekly, 45-60 minutes.

**Purpose:** Growth, judgment-building, feedback, blockers.

**Default agenda:**

| Time | Section |
|------|---------|
| 5 min | Personal check-in |
| 20-25 min | Their topics: work, judgment calls, blockers |
| 10-15 min | Growth and feedback |
| 5 min | Actions + next 1:1 |

**Coaching with GROW (Whitmore):**

When a report brings a problem, resist the urge to solve it. Use GROW:

- **G**oal -- What outcome are you trying to reach?
- **R**eality -- What's the current state? What have you tried?
- **O**ptions -- What options have you considered?
- **W**ay forward -- What will you do next?

GROW develops judgment. Solving problems for reports stunts their development.

**Default questions for them:**

- "What's gone well this week?"
- "What's the hardest decision you're facing?"
- "What do you need from me?"
- "What feedback do you have for me?"

**Growth conversation cadence:**

- Monthly: deeper growth conversation tied to their growth plan
- Quarterly: rubric calibration against the next level
- Annually: career planning (12-24 month horizon)

### Type E: With cross-functional partners (sales, support, data, marketing, legal)

**Cadence:** Monthly, 30 minutes (more often during launches).

**Purpose:** Alignment, mutual context, early-warning signal.

**Default agenda:**

| Time | Section |
|------|---------|
| 5 min | What's happening on your side |
| 10 min | What's happening on my side |
| 10 min | Mutual blockers / requests |
| 5 min | Actions |

**Key questions (rotate):**

- "What's a customer signal you're seeing that I should know about?"
- "What's a question you've been getting that we should answer?"
- "Where is our messaging mis-aligned with what customers experience?"
- "What's coming up that you need from product?"

## The 1:1 kickoff conversation

When starting any new 1:1 relationship, have a kickoff conversation explicitly:

1. **What this 1:1 is for** -- Status? Growth? Coordination? Trust-building?
2. **Cadence and format** -- Weekly? Bi-weekly? In-person? Async sometimes?
3. **Who owns the agenda** -- Default = the other person, but clarify
4. **How we'll give each other feedback** -- Frequency, format, examples
5. **What "good" looks like in 6 months** -- Define success for the partnership

See `assets/kickoff_template.md` for a full script.

## Feedback in 1:1s (Radical Candor)

The hardest part of any 1:1 is giving direct feedback. Kim Scott's Radical Candor framework provides a 2x2:

|  | Care Personally HIGH | Care Personally LOW |
|--|--|--|
| **Challenge Directly HIGH** | Radical Candor (target) | Obnoxious Aggression (avoid) |
| **Challenge Directly LOW** | Ruinous Empathy (avoid) | Manipulative Insincerity (avoid) |

Strong 1:1 feedback:

- Is specific to a behavior or moment, not a generalization
- Is timely (same week beats next month)
- Frames the impact: "When you did X, the impact on the team was Y"
- Invites response: "How did you experience that moment?"
- Closes with a desired change: "Next time, what would you try differently?"

Weak feedback patterns to avoid:

- The "feedback sandwich" (positive-negative-positive) -- it dilutes the message
- Generalizations ("You always...")
- Feedback delivered as humor or via someone else
- Sitting on feedback for weeks (compound interest works against you)

## Workflow

1. **Audit your current 1:1s.** List every 1:1 you run weekly. For each, name the type (A-E above) and whether it has a working structure.
2. **Pick the highest-leverage one to fix first.** Usually the manager 1:1 or your weakest direct-report 1:1.
3. **Have a kickoff conversation.** Use `assets/kickoff_template.md` to reset expectations explicitly.
4. **Adopt the template.** Use the partner-type agenda for 4 weeks consistently.
5. **Capture decisions and actions.** Use `assets/1on1_notes_template.md`. Keep the running doc.
6. **Review quarterly.** Are the 1:1s producing trust, growth, and unblocking? If not, change the format.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| 1:1s turn into status updates | No structured agenda; default behavior takes over | Adopt the partner-type template; move status to a written async update; reclaim the 1:1 for what cannot be written |
| Your direct report leaves 1:1s frustrated | You are solving instead of coaching | Adopt GROW; resist the urge to answer until you've asked 3 questions; when stuck, ask "What do you think?" before "Here's what I think" |
| Your manager cancels your 1:1s frequently | Lower priority on their side, or you've not made them valuable | Make them tighter (30 min, 3 topics); pre-send the agenda; make sure they leave with one thing they didn't have before |
| You haven't given hard feedback in 6+ months | Ruinous empathy mode (Scott) | Pick the one piece of feedback you've been sitting on; deliver it in the next 1:1 using the situation-behavior-impact format |
| The 1:1 with your EM partner is tense | Misaligned priorities or accumulated unspoken issues | Schedule a 60-minute "operating model reset" 1:1; bring the partnership-health questions; ask each other explicitly "what's not working?" |
| You don't have time for monthly 1:1s with all cross-functional partners | Over-scheduled OR too many partners on your map | Tier the list -- weekly for 5 people, monthly for 8, quarterly for the rest; replace monthly meetings with bi-monthly written updates where possible |
| Your direct reports don't bring you their hardest problems | Trust gap; they expect to be judged rather than coached | Ask explicitly: "What's something you're avoiding telling me?"; demonstrate non-reactivity when they share something hard once; trust builds from there |

## Success Criteria

- Every 1:1 has a clear type (manager / EM partner / designer / report / cross-functional)
- Every 1:1 has a working agenda template the participants both know
- You have given at least one piece of direct feedback per month to each Tier 1 partner
- Your direct reports (if any) leave 1:1s with a clearer next step, not a solved problem
- Quarterly, you and your manager have a growth-focused 1:1 (not just operational)
- You document decisions and actions in every 1:1; you do not transcribe the conversation
- Your cancellation rate of 1:1s is <10% (if higher, the cadence is wrong)

## references/red-flags.md

# Red Flags: PM 1:1s

> Common ways this skill's output goes wrong — concrete examples, why they're bad, and how to fix them. Pair with the SKILL.md and Troubleshooting table.

## How to use this document

When you have just drafted a 1:1 agenda, written notes, or designed a question bank, scan the red flags below before your next 1:1. Each red flag shows a *bad* and *good* version of the same artifact or interaction.

---

## Red Flag 1: Status Update Theater

**Symptom.** The 1:1 with your manager is 25 minutes of "here is what I worked on this week" with no questions, no asks, no growth conversation.

**Why it's bad.** Status updates belong in async writeups (Slack, weekly digest, project tracker). The 1:1 is your highest-bandwidth conversation with your manager; spending it on read-aloud status burns the slot. Manager Tools' framework explicitly puts status at the *bottom* of the agenda.

**Bad example:**
> Agenda: "1. Project A update. 2. Project B update. 3. Project C update. 4. Any questions?"

**Good example:**
> "Async sent Monday: 5-bullet status. 1:1 agenda: (a) 1 ask for help (Project B stakeholder blocked), (b) 1 growth topic (preparing for next-level promo discussion), (c) feedback I owe — both directions, (d) what is on your mind that I should know about."

**How to catch it.** If 60%+ of the 1:1 is updating your manager on things they could read async, you have status theater.

---

## Red Flag 2: No Trust-Building or Personal Connection

**Symptom.** Every 1:1 starts with "okay, first item..." and ends on a status note. No check-in on the human at the other end of the table.

**Why it's bad.** Kim Scott's Radical Candor frame requires *caring personally* before *challenging directly*. A 1:1 with no human dimension cannot deliver hard feedback; the trust account is empty when you need to make a withdrawal.

**Bad example:**
> "Hi. Item 1: roadmap. The sprint is at risk because..."

**Good example:**
> "Hi, before we get into it — how's your week been? You mentioned your kid's exam last time, how did that go?" (2-3 minutes, sincere.)

**How to catch it.** Do you know one non-work fact about the person at the other end of each recurring 1:1? If not, your 1:1s are transactional.

---

## Red Flag 3: One-Directional Feedback Flow (Only Down)

**Symptom.** Your manager gives you feedback; you never give feedback to your manager. Or you give feedback to your reports but never invite it back.

**Why it's bad.** Feedback that only flows downhill is performance management, not coaching. Manager Tools and Radical Candor both require *upward* feedback explicitly. Skipping it leaves your manager unable to improve and signals that feedback is a sword, not a tool.

**Bad example:**
> Manager: "Here's what you could improve." You: "Thanks, I'll work on that."

**Good example:**
> Manager: "Here's what you could improve." You: "Thanks, I'll work on that. One piece of feedback for you: when we discussed the roadmap last week, I felt the priorities shifted faster than I could communicate to the team. Could we agree on a 'no changes within sprint' rule?"

**How to catch it.** In your last 4 1:1s, have you delivered at least 1 piece of upward feedback? If zero, the feedback channel is one-way.

---

## Red Flag 4: GROW Model Skipped — Jumping to Will (Solutions)

**Symptom.** Report or partner brings up an issue; you immediately offer a solution. Goal/Reality/Options are skipped.

**Why it's bad.** GROW (Whitmore) is in this skill because the *value* of a coaching conversation is helping the other person think, not solving their problem. Skipping to Will is faster but produces dependency and underdeveloped reports.

**Bad example:**
> Report: "I'm struggling with the engineering team's velocity." You: "You should set a clearer DoD and run a velocity retro."

**Good example:**
> Report: "I'm struggling with the engineering team's velocity." You: "What does 'good' look like for you here? [Goal] What's actually happening today? [Reality] What options have you considered? [Options] Which of those will you try first? [Will]"

**How to catch it.** If you find yourself saying "you should..." in the first 5 minutes of a topic, you skipped GROW.

---

## Red Flag 5: Skip-Level Information Leakage

**Symptom.** You repeat to your skip-level (or to your manager's manager) something a report told you in confidence in a 1:1.

**Why it's bad.** 1:1 confidentiality is the foundation of psychological safety. One breach kills the channel — the report stops sharing real concerns, retreats to status theater, and looks for a new manager or a new job.

**Bad example:**
> In skip-level: "Jamie mentioned in our 1:1 that she's frustrated with the EM."

**Good example:**
> In skip-level: "A common theme in my 1:1s is that PMs feel unclear on engineering priorities. I'm working with my reports to surface specifics; would you support a cross-functional alignment session?"

**How to catch it.** Before mentioning anything from a 1:1 in any other meeting, ask: "did this person give me permission to share this?" If not, abstract or omit.

---

## Red Flag 6: No Notes, No Follow-Through

**Symptom.** You take no notes. Two weeks later, you cannot remember what you agreed. The same topics resurface; commitments evaporate.

**Why it's bad.** A 1:1 without notes is improv. The Manager Tools framework requires written follow-ups precisely because human memory is unreliable and trust is built by following through. Reports notice when their issues vanish into the ether.

**Bad example:**
> No shared document. Both parties go to next 1:1 trying to remember what they agreed.

**Good example:**
> Shared rolling doc. Each 1:1 has dated agenda, decisions, and action items with owner. Items not closed last time are carried forward. 15-minute pre-read before each 1:1.

**How to catch it.** Can you produce a 4-month history of agreed actions per 1:1 relationship? If not, your follow-through is fictional.

---

## Red Flag 7: Skipping or Constantly Rescheduling 1:1s

**Symptom.** "Crazy week, let's skip the 1:1." Or 1:1s get moved 3 times then dropped.

**Why it's bad.** Cadence is the point. The 1:1 is the *only* guaranteed conversation between two people in the week. Skipping it during high-stress weeks is exactly when it would have caught problems early. A skipped 1:1 signals "you are not important enough" — even when meant otherwise.

**Bad example:**
> Slack: "Crazy launch week, let's skip our 1:1 and catch up next week."

**Good example:**
> Slack: "Crazy launch week. Shrinking 1:1 to 15 min and tightening agenda to just blockers and one ask. Still meeting at 2pm."

**How to catch it.** Over the last 8 scheduled 1:1s, what % actually happened? If under 75%, cadence is broken.

---

## Red Flag 8: Coaching Without Permission (Unsolicited)

**Symptom.** Partner brings up a problem; you launch into coaching mode without asking if they want coaching or just to vent.

**Why it's bad.** Unsolicited coaching feels patronizing. Sometimes people need to be heard, not coached. Asking permission — "would it be more helpful for me to listen or to ask coaching questions?" — preserves agency.

**Bad example:**
> Partner: "The launch is a disaster, I'm furious." You: "What does great look like here? What have you tried?"

**Good example:**
> Partner: "The launch is a disaster, I'm furious." You: "Sounds rough. Do you want to vent for a few, want me to help think it through, or want a recommendation?"

**How to catch it.** In your last 5 coaching attempts, did you ask permission first? If never, you are imposing the frame.

---

## Red Flag 9: Treating Direct Reports' 1:1s as Performance Reviews

**Symptom.** Every 1:1 with a report becomes a mini-review: "here's what I noticed you doing wrong this week."

**Why it's bad.** 1:1s are *their* time, not yours. Performance feedback belongs in a separate, regular feedback cadence (Radical Candor's "in the moment" or scheduled performance check-ins). A 1:1 that is a feedback-delivery slot is dreaded and skipped.

**Bad example:**
> Manager-to-report 1:1: 80% manager speaking, 20% report. Most of manager talk is corrective feedback.

**Good example:**
> Manager-to-report 1:1: 70% report speaking on their topics, 20% growth/career, 10% feedback (both directions). Corrective feedback delivered in-the-moment, not stockpiled.

**How to catch it.** In the last 1:1, what % of speaking time was theirs vs yours? Under 50% theirs is a manager-speech red flag.

---

## Red Flag 10: No Growth or Career Conversation Ever

**Symptom.** 1:1s cover only current work. Growth, promotion, skill development, and longer-arc career topics never come up.

**Why it's bad.** The PM career ladder is steep and signals are noisy. Reports who never discuss growth assume they are not on track for promotion; partners who never discuss skills stagnate. Manager Tools recommends a *quarterly* growth-focused 1:1 minimum.

**Bad example:**
> 26 weeks of 1:1s. Zero mentions of promotion, skill gaps, or career arc.

**Good example:**
> Standing quarterly agenda: "Where do you want to be in 12 months? What's the next-level rubric saying? What experiments are you running this quarter? How can I sponsor your growth?"

**How to catch it.** Search your 1:1 notes for "growth", "career", "promotion", "next level" over the last 90 days. If zero hits, growth is invisible.

---

## Red Flag 11: Using 1:1s for Tactical Decisions That Should Be Group Meetings

**Symptom.** Strategic or cross-functional decisions get made in 1:1s, then the team is informed after the fact.

**Why it's bad.** Decisions made in 1:1s exclude the people who should have weighed in. The decision is fragile (no group buy-in) and the people who should have heard the reasoning hear only the outcome.

**Bad example:**
> Manager and PM decide in 1:1 to change the roadmap priorities. Team finds out via revised Jira board.

**Good example:**
> In 1:1: "I think we should re-prioritize, here's why. Can we put this on the next product trio meeting agenda so design and engineering weigh in?"

**How to catch it.** If a decision in a 1:1 affects 3+ people who were not in the 1:1, the decision should move to a group forum.

---

## Red Flag 12: Cross-Functional 1:1 Becomes a Sales Pitch

**Symptom.** 1:1 with the EM, design partner, or cross-functional lead turns into you trying to sell them on your roadmap.

**Why it's bad.** Partners notice when a 1:1 is one-sided. The relationship is a deposit account; selling without asking burns the deposit. The partner-type-specific templates in this skill exist to balance the conversation across both sides' interests.

**Bad example:**
> 1:1 with EM: PM spends 40 minutes pitching why mobile work should be prioritized. EM nods, leaves drained.

**Good example:**
> 1:1 with EM: 5 min context-sharing, 15 min listening (what are EM's pressures, team capacity reality), 10 min joint priorities discussion, 10 min process improvements both can make.

**How to catch it.** In your last cross-functional 1:1, did you ask 5+ questions about *their* world? If not, it was a pitch.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Status Update Theater | Status moved to async; 1:1 is growth/asks/feedback? |
| 2 | No Trust-Building | Do you know one non-work fact about them? |
| 3 | One-Directional Feedback | Have you given upward feedback in last 4 1:1s? |
| 4 | Skipping to Solutions | Did you ask Goal/Reality/Options before Will? |
| 5 | Skip-Level Information Leakage | Permission to share before mentioning elsewhere? |
| 6 | No Notes / No Follow-Through | Can you produce 4 months of dated actions? |
| 7 | Skipping or Rescheduling | Last 8 1:1s, % actually happened above 75%? |
| 8 | Coaching Without Permission | Did you ask listen/coach/recommend? |
| 9 | 1:1 as Performance Review | Report speaks 50%+ of the time? |
| 10 | No Growth Conversation | Growth topic in last 90 days of 1:1 notes? |
| 11 | Group Decisions in 1:1 | Decisions affecting 3+ moved to a group? |
| 12 | Cross-Functional 1:1 as Pitch | 5+ questions about their world? |

## Related Reading

- SKILL.md Troubleshooting section (for symptom -> root cause -> resolution)
- references/templates/ (for partner-type-specific 1:1 templates, if present)
- pm-onboarding/references/red-flags.md (for new-relationship 1:1 patterns)

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/career/pm-1on1s -->
