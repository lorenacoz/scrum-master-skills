---
description: "Turn a blocked decision into an async questionnaire a stakeholder can answer without a meeting. Use when you need someone else's input to decide, a meeting would be overkill, or answers from several people must be consolidated."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Decision Questionnaire

Some decisions stall because the knowledge sits with someone else. A meeting costs everyone an hour; "thoughts?" gets a vague reply. A structured questionnaire costs the recipient fifteen minutes and returns comparable, recordable answers.

The agent interviews the sender only about the send (who, what they need back, by when, what happens on silence), never the subject they cannot answer. It writes neutral, one-idea questions with answer formats, gates the draft, and consolidates replies into a decision record.

## When to Use

- A decision is blocked on knowledge that one to five specific people hold
- You would otherwise book a meeting just to ask questions
- Answers came back and must become a recorded decision

## Clarify First

What most shapes the questionnaire is the gap between what the recipient knows and what the sender needs. Settle the inputs below before producing anything. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Recipient and what they know:** role and expertise set tone, how much context to carry, and which questions only they can answer.
- **What you must walk away able to decide:** each question has to unblock one of these outputs, or it gets cut.
- **Deadline and default if silent:** without both, silence blocks the work instead of resolving it.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

```bash
# Gate a draft before sending (exit 1 = not ready)
python3 scripts/questionnaire_linter.py \
  --input assets/sample_questionnaire_flawed.json \
  --today 2026-11-08
```

```bash
# Consolidate replies into a decision-record draft (exit 1 = critical question still blocked)
python3 scripts/answer_consolidator.py \
  --input assets/sample_questionnaire_clean.json \
  --answers assets/sample_answers_conflict.json \
  --today 2026-11-19 --format json
```

## Tools Overview

| Tool | Reads | Reports |
|---|---|---|
| `questionnaire_linter.py` | Questionnaire JSON | Missing header fields, past deadline, leading/vague/compound wording, missing formats, units or choices, options without trade-offs, size over budget |
| `answer_consolidator.py` | Questionnaire + responses | Answers per question, "don't know", conflicts, missing respondents, outcome `ready-to-record` / `needs-follow-up` / `default-applied` |

### Exit code contract

| Code | Linter | Consolidator |
|---|---|---|
| 0 | Ready to send (warnings allowed) | Ready to record, or default applied |
| 1 | At least one error finding | A critical question is unanswered before the deadline or in conflict |
| 2 | Missing file, invalid JSON, bad date | Same |

## Workflow

1. **Interview the send, not the subject.** [PROVEN] Ask who it goes to, what they know that the sender doesn't, and what the sender must be able to decide afterwards. Cut every question the sender could answer by looking it up.
2. **Write the header.** Purpose, the decision riding on it, sender and recipients, how answers will be used, a context paragraph under 150 words for someone in none of the meetings, deadline, effort, and the default action if nobody answers.
3. **Lay out the options.** [RECOMMENDED] Two to four, each with its trade-off; mark at most one as the sender's lean; add "none of these".
4. **Write the questions.** One idea each, neutral, most important first, grouped by theme, each with a format: pick-one, ranked, number with unit, yes-no with condition, or capped free text. "Why this matters" only where misreadable. End with one catch-all.
5. **Validate against the quality gate.** Run `questionnaire_linter.py`; it must pass with zero errors before sending. Then read it once as the recipient and check the hand-review checklist in `references/question-design.md` (hidden premises, loaded descriptors).
6. **Send with a four-line message** (what, why you, time and deadline, default) and one answer channel.
7. **Remind once, then last-call** a day before the deadline, asking only blocking questions.
8. **Consolidate and record.** [RECOMMENDED] Run `answer_consolidator.py`, settle critical conflicts, fill `assets/decision_record_template.md`, and send it to every recipient.

```bash
python3 scripts/answer_consolidator.py \
  --input assets/sample_questionnaire_clean.json \
  --answers assets/sample_answers.json --today 2026-11-19
```

## Anti-Patterns

### The Leading Question
**Mistake:** "Don't you think Frankfurt is the safest choice?"
**Why it happens:** The sender has a lean and wants it confirmed.
**Instead:** State the lean once in the options table, labelled, then ask "Which option would you approve?"

### The Thoughts Dump
**Mistake:** A link to a design doc and "Thoughts?"
**Why it happens:** Writing questions forces the sender to work out what they need.
**Instead:** Turn each unknown into a formatted question; keep one open question, at the end.

### No Default on Silence
**Mistake:** A deadline with no stated consequence, so the decision waits indefinitely.
**Why it happens:** Stating a default feels presumptuous.
**Instead:** Write the action you will take on silence; anyone who dislikes it now has a reason to reply.

### The Survey Creep
**Mistake:** Twenty-five questions, half of them nice-to-know.
**Why it happens:** Every stakeholder adds "while we're asking…".
**Instead:** Hold to about ten questions and fifteen minutes; defer the rest.

### Merging Conflicts Away
**Mistake:** Two respondents disagree and the record reports only the majority view.
**Why it happens:** A clean record looks more decisive.
**Instead:** Record each conflict and how it was settled; hidden disagreements reopen decisions.

## Files

| File | Purpose |
|---|---|
| `scripts/questionnaire_linter.py` | Pre-send gate |
| `scripts/answer_consolidator.py` | Replies to decision-record draft |
| `assets/questionnaire_template.md`, `assets/decision_record_template.md` | Templates |
| `assets/sample_questionnaire_clean.json` / `_flawed.json` | Linter exits 0 / 1 |
| `assets/sample_answers.json` / `sample_answers_conflict.json` | Consolidator exits 0 / 1 |

## Reference Documentation

- [references/question-design.md](references/question-design.md) — gap analysis, wording, the five answer formats, sizing, linter codes, hand-review checklist. Read while drafting.
- [references/sending-and-consolidating.md](references/sending-and-consolidating.md) — async vs meeting, multi-recipient variants, follow-up cadence, consolidator outcomes, the decision record. Read before sending.

## Scope & Limitations

**In Scope:** async questionnaires for blocked decisions, multi-recipient variants, pre-send linting, consolidating answers into a decision record.

**Out of Scope:**
- Who decides, approves and is consulted (see `project-management/execution/daci-framework/`)
- Live customer discovery interviews (see `project-management/discovery/customer-interview-script/`)
- Large-sample surveys and statistical analysis of responses
- Broad stakeholder engagement planning (see `project-management/execution/stakeholder-map/`)

**Important Caveats:**
- The linter reads JSON, not prose; render the sent version with the template.
- Wording checks are pattern-based and miss loaded adjectives and hidden premises; a human read is still required.
- Effort estimates are a sizing aid. The consolidator matches respondents by exact name and does not judge free text.

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/question-design.md

# Question Design for Async Decision Questionnaires

A decision questionnaire is read once, by someone busy, without you in the room to clarify. Every question has to survive that reading. This reference covers how to find the right questions, how to word them, which answer format to attach, how to order and size the set, and the failure patterns the linter checks for.

## 1. Find the gap before writing a single question

The questions should target exactly one thing: **the gap between what the recipient knows and what the sender needs to decide.** Anything outside that gap is either something the sender can find out alone (and should) or something the recipient cannot answer either.

Work out the gap from two sender-side facts, both of which the sender can always answer:

1. **Who is this going to, and what do they know that I don't?** Role, expertise, relationship, and the specific knowledge they hold — "the Finance Controller knows what infrastructure spend is already committed for Q1", not "Finance has opinions".
2. **What must I walk away able to decide or do?** A short list of concrete outputs — "pick a hosting option", "know the cost ceiling", "know whether backups count for residency".

Then, for each output, ask: *which single fact or judgment from this recipient would unblock it?* That is the question. If an output needs nothing from this recipient, it does not belong in this questionnaire.

### Facts you can look up are not questions

Before sending, strip every question whose answer exists somewhere the sender can reach: a contract repository, a dashboard, a previous decision record, the codebase, the org chart. Asking the recipient to look something up for you spends their goodwill on clerical work and dilutes the questions only they can answer. The test: *could a diligent new hire find this in under 20 minutes?* If yes, find it yourself.

### Do not interview the sender about the subject

The sender is writing the questionnaire precisely because they cannot answer the subject questions. Grilling them on the subject ("what do you think the cost ceiling should be?") either produces guesses that then leak into the questionnaire as leading framing, or reveals that they could have decided alone. Interview the sender only about the send: who, what they need back, by when, what happens if nobody answers.

## 2. One idea per question

A question asks for exactly one fact or judgment. The two common violations:

| Pattern | Example | Problem | Fix |
|---|---|---|---|
| Conjunction | "Should backups stay in the EU and should logs stay there too?" | A "yes" might mean yes to one; a "no" is uninterpretable | Two questions, or one pick-one with four combinations |
| Stacked questions | "What does Legal say? What does the DPO say?" | Respondent answers the easier half | Separate questions, or route to the right person |
| Hidden either/or | "Is cost or speed more important, and by how much?" | Mixes a choice with a magnitude | Ranked question, then a number question |
| Embedded premise | "When we move to Frankfurt, what will break?" | Presumes the decision | "If we chose Frankfurt, what would break?" |

The linter flags more than one question mark and the patterns "and/or + auxiliary verb" ("and should", "or would"). It cannot see a hidden premise — review for that by hand.

## 3. Neutral wording

A leading question tells the recipient which answer you want. Async makes this worse, not better: the recipient cannot see your face, so they read the wording as the signal, and agreeable people supply the answer it implies.

Leading families the linter catches:

- **Tag questions and negative interrogatives:** "Don't you think…", "Wouldn't it be…", "Isn't it better…", "Shouldn't we…", "…, right?"
- **Certainty markers:** "obviously", "clearly", "surely".
- **Agreement prompts:** "Do you agree that…".

Leading patterns it does not catch, which need a human pass:

- **Loaded descriptors:** "the risky US option", "the proven Frankfurt setup".
- **Asymmetric detail:** three sentences of upside on option A, one line on B.
- **Order bias:** the recommended option always listed first in every question. List options in a fixed, stated order (A, B, C) and mark the recommendation explicitly instead of signalling it by position.

### Recommending without leading

A sender often has a lean, and hiding it is unhelpful — the recipient may want to react to it. The honest pattern is to **state the lean once, in the options table, labelled as such** ("A — our current lean"), and then ask neutral questions. "Which option would you approve?" with a labelled recommendation is fair. "Don't you think A is safest?" is not.

## 4. Attach an answer format to every question

Free-form answers are slow to write and impossible to compare across respondents. Every question declares one of five formats:

| Format | Use when | Rules |
|---|---|---|
| **pick-one** | A choice among known alternatives | At least two choices; always include "none of these" and "don't know" so nobody is forced into a false answer |
| **ranked** | Relative priority matters more than absolute | Three to five items; more than five and the middle of the ranking is noise |
| **number** | A threshold, budget, date offset, volume | Always state the unit ("EUR per month", "requests per second", "weeks"); ask for a single number or an explicit range, not "roughly" |
| **yes-no** | A binary constraint | Always invite the condition: "yes / no / yes-if…". Bare yes-no hides the most useful part of the answer |
| **free-text** | Facts you cannot enumerate (which contracts, which customers) | Cap the length (30-80 words) and say so; uncapped text produces essays from some respondents and one word from others |

Rules of thumb:

- If you catch yourself writing a free-text question for a judgment call, convert it into a pick-one with the realistic options and an escape.
- A number question is the best defence against vague agreement: "is the cost acceptable?" gets "yes"; "what is the most you would approve?" gets 3,500.
- Ranking is the right tool for "what matters most" — never ask people to rate five things on a 1-5 scale; everything comes back as 4.

## 5. "Why this matters" — only when needed

A one-line rationale under a question helps in two cases:

1. The question could be misread ("Must backups stay in the EU?" — the respondent may not realise backups are a separate decision from primary storage).
2. The question invites a throwaway answer ("Which contracts name a region?" — without the rationale, "none that I know of" looks like a fine answer).

Adding a rationale to every question doubles reading time and buries the ones that need it. The linter does not require it; the review checklist asks you to justify each one.

## 6. Order, grouping and size

**Most important first.** Async means you may get one pass, possibly partial. Put the questions that decide the outcome at the top and mark them critical. If the respondent stops after three questions, you should still be able to decide.

**Group by theme once you have more than four questions.** Themes are recipient-facing ("Approval", "Compliance", "Gaps"), not sender-facing ("Stuff for the infra ticket"). Within a theme, still most-important-first.

**Size budget: about ten questions and fifteen minutes.** Past that, completion rates drop and late questions get skimmed. The linter estimates effort from answer formats:

| Format | Approx. minutes |
|---|---|
| yes-no | 0.75 |
| pick-one | 1.0 |
| number | 1.5 |
| ranked | 2.0 |
| free-text | 3.0 |

If you are over budget: cut questions you can answer yourself; merge two pick-ones into one with combined choices; move "nice to know" questions to a second round after the decision.

## 7. The closing catch-all

End with one open question: "Is there anything we did not ask that would change this decision?" It is the only deliberately open question in the set, and it is the one that catches the constraint the sender did not know existed. Keep it last and keep it single.

## 8. Context paragraph

One paragraph, under about 150 words, written for someone who was in none of the meetings:

- What exists today.
- What changed that forces a decision now.
- What is already decided and **not** up for discussion (so the recipient does not spend their answer relitigating it).

"See the thread from last week" is not context. The recipient will not read the thread, and if they do, they will answer the thread rather than your questions.

## 9. The default if nobody answers

Every questionnaire states what happens if no answer arrives by the deadline, as an action: "we proceed with option A and record that the choice was made without Finance input." This does three things:

- It converts silence into a decision instead of a blocker.
- It gives the recipient a reason to answer — if they dislike the default, they now have to say so.
- It makes the sender commit to a lean, which often exposes that the questionnaire is really asking for a veto check, not open input. That is fine; say so.

A default must be something the sender is actually willing to do. A default of "we wait" is not a default.

## 10. Linter finding reference

| Code | Severity | Meaning |
|---|---|---|
| missing-purpose / missing-decision / missing-context | error | Header fields the recipient needs to orient |
| missing-deadline / deadline-past | error | No deadline, or it has already passed relative to `--today` |
| missing-default-if-no-answer | error | Silence would block the work |
| missing-recipient | error | Nobody named |
| single-option / multiple-recommended / missing-tradeoffs | error | The options table cannot support a choice |
| leading / vague / compound | error | Wording problems that corrupt answers |
| missing-format / too-few-choices / missing-unit | error | Answers would not be comparable |
| too-many-questions / effort-over-budget | error | Over the size budget |
| missing-use / missing-catch-all / no-escape-option / no-escape-choice | warn | Weaker but sendable |
| uncapped-free-text / yes-no-no-condition / missing-theme | warn | Answer quality will vary |
| deadline-tight / context-long / estimate-over-budget / missing-effort | warn | Likely to be answered late or skimmed |

Warnings do not fail the gate. Fix them when the decision is high-stakes or the recipient is senior; ship with them for a quick internal check.

## 11. Hand-review checklist

The linter cannot read intent. Before sending, read the questionnaire once as the recipient and confirm each line:

- [ ] Every question targets something only this recipient knows; nothing is a lookup the sender could do.
- [ ] No question presumes the decision ("when we move to…" instead of "if we chose…").
- [ ] Options are described with comparable detail and no loaded adjectives.
- [ ] The recommendation, if any, appears once, labelled, in the options table.
- [ ] The critical questions are first and would let you decide even if the rest are skipped.
- [ ] Each "why this matters" line earns its place by preventing a misreading or a throwaway answer.
- [ ] The default on silence is an action you are genuinely willing to take.
- [ ] Context mentions what is already decided and off the table.
- [ ] One answer channel is named.

## references/sending-and-consolidating.md

# Sending, Following Up and Consolidating Answers

Writing the questionnaire is half the work. This reference covers the send itself, variants for more than one recipient, the follow-up cadence, turning answers into a decision record, and when to abandon async and meet.

## 1. Choosing async over a meeting

Use a questionnaire when all of these hold:

- The decision needs **specific knowledge** from one to five people, not a negotiation among them.
- The questions can be **stated precisely now**. If you cannot yet word the question, you need a conversation to find it, not a form.
- Respondents can answer **independently** — one person's answer does not depend on hearing another's first.
- A delay of several working days is acceptable.

Prefer a live conversation when:

| Signal | Why async fails |
|---|---|
| The recipients disagree with each other and know it | Independent answers just document the conflict; someone has to broker it |
| The decision is emotionally loaded (reorgs, cuts, people) | Written questions read as cold; answers get guarded |
| You cannot write the options table | You are still in discovery; a questionnaire would fix the frame too early |
| The answer is needed today | Async realistically needs two working days minimum |

A useful hybrid: send the questionnaire anyway and use it as the agenda for a short meeting. Respondents who fill it in beforehand make the meeting fifteen minutes instead of an hour.

## 2. The send message

The questionnaire travels inside a short message (email, chat, ticket comment). That message has four lines and nothing else:

1. What you need: "I need your input on where the analytics add-on is hosted for EU customers."
2. Why them: "You know what spend is committed for Q1, which I don't."
3. Cost and deadline: "About 12 minutes, by Thursday 20 November."
4. The default: "If I hear nothing, I'll go ahead with Frankfurt."

Do not paste the questions into the message body *and* attach the document — respondents answer whichever they see first, and you end up merging two partial answer sets.

### Where answers go

Decide one place for answers before sending: the document itself (inline under each question), a form, or a reply. Mixed channels are the most common source of lost answers. If respondents will see each other's answers, say so in "how your answers will be used" — it changes what people write.

## 3. Multiple recipients

| Situation | Variant | Notes |
|---|---|---|
| Same knowledge, need a cross-check | **Same questionnaire to each**, answered independently | Do not let respondents see each other's answers before submitting; anchoring makes agreement meaningless |
| Different knowledge per person | **One core plus per-recipient sections** | Keep the critical decision question identical for all; add role-specific questions only to the person who can answer them |
| One decider, several advisers | **Advisers first, decider second** | Send advisers the questionnaire, consolidate, then send the decider a two-question follow-up with the consolidated view |
| Large group (6+) | **Not a questionnaire** — use a survey or a decision meeting | Above about five, consolidation becomes polling and the "decision" becomes a vote nobody owns |

When the same question goes to several people, the consolidator compares answers:

- **pick-one / yes-no:** any difference is a conflict (yes-no compares the verdict, ignoring the stated condition).
- **ranked:** a conflict only when first choices differ; differences lower in the ranking are reported but not blocking.
- **number:** a conflict when the spread exceeds half the median (e.g. 1,500 vs 4,000).

## 4. Follow-up cadence

| When | Action |
|---|---|
| Send day | Send; put the deadline in your own calendar |
| Midpoint | One reminder to non-respondents only, restating time needed and the default |
| Deadline −1 working day | Direct message: "Tomorrow I'll go ahead with the default unless you'd like to weigh in." |
| Deadline | Run the consolidator. Record the decision, or follow up on blocking questions only |
| After deadline | Apply the default if critical questions are unanswered; tell non-respondents what was decided |

One reminder and one last-call is the ceiling. More than that trains people that your deadlines are soft.

### Follow-up on a partial answer

Do not resend the whole questionnaire. Send only the unanswered critical questions, or the conflicting ones, with what you already know: "Security picked A, you picked C — what would need to be true for A to work for you?" That is a different, sharper question than the original, and it often resolves the conflict in one reply.

## 5. Reading the consolidator outcome

| Outcome | Meaning | Next step |
|---|---|---|
| `ready-to-record` | Every critical question has a usable, consistent answer | Write the decision record; resolve non-critical conflicts at leisure |
| `needs-follow-up` | A critical question is unanswered before the deadline, or answered with a conflict | Targeted follow-up on the listed questions only (exit code 1) |
| `default-applied` | Deadline passed with critical questions unanswered and no conflict blocking | Record the decision as "decided by default" and notify recipients |

A conflict on a critical question blocks even after the deadline: the default exists to replace silence, not to overrule an explicit objection. When a respondent has said "not A", proceeding with A by default is a decision someone must own, so the tool keeps it in follow-up.

"Don't know" answers are recorded separately, never treated as votes. Three "don't know" responses to a critical question with no real answer is functionally unanswered — and a signal you asked the wrong people.

## 6. Writing the decision record

Use `assets/decision_record_template.md`. The record exists so that, six months later, someone can see what was decided, on what evidence, and what would reopen it. Fill it in this order:

1. **Outcome first**, stated as an action. If the default applied, say so in the first line.
2. **What the answers established** — one row per question that influenced the outcome, with the answer per respondent and how it was used. Questions that turned out not to matter can be omitted; note that they were asked.
3. **Disagreements** — every conflict, how it was settled, by whom, and why. A record that hides a disagreement invites the losing side to reopen the decision later.
4. **Open items** — useful "don't know" answers and catch-all points that need their own decision, each with an owner.
5. **Revisit if** — the concrete condition that would reopen the decision.

Then close the loop: send the record to every recipient, including those who did not answer. People who answered see their input used; people who did not learn what was decided without them, which is the strongest incentive to answer the next one.

## 7. When the questionnaire itself was wrong

Signs the questionnaire asked the wrong thing:

- Most answers land in "none of these" or the catch-all.
- Respondents answer a different question from the one asked.
- A respondent replies "I'm not the right person for this".
- The answers are consistent but do not let you decide.

Do not patch the questionnaire and resend to the same people. Go back to the gap analysis: either the recipient does not hold the knowledge you thought, or the decision is not yet framed well enough for questions. A short conversation is usually the faster repair.

## 8. Worked example (from the sample files)

The sample questionnaire asks a Security Lead and a Finance Controller to help choose the EU hosting region for an analytics add-on.

- **Clean run, day before the deadline** (`sample_answers.json`, `--today 2026-11-19`): both pick A, cost ceilings 4,000 and 3,500 (spread under half the median, so no conflict). They disagree on whether backups must stay in the EU — but that question is not critical. Outcome `ready-to-record`; the backup question goes into "Disagreements" with a follow-up owner.
- **Conflict run** (`sample_answers_conflict.json`): Security picks A, Finance picks C. Q1 is critical, so the outcome is `needs-follow-up` (exit 1). The follow-up is one question to Finance: what would make A acceptable?
- **Silence after the deadline** (an empty response list, `--today 2026-11-21`): outcome `default-applied`; the record states that Frankfurt was chosen without Security and Finance input.

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/decision-questionnaire -->
