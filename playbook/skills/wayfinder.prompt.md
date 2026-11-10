---
description: "Chart work too big for one sprint as a map of decision tickets, resolve them in dependency order, then turn answers into tracer-bullet tickets. Use when the route is unclear, open questions block each other, or estimates swing wildly."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Wayfinder

Some work is too large for one session and too foggy to estimate: the build steps depend on choices nobody has made, and those choices block each other. The agent instead charts a **map of decision tickets**, works them one per session in dependency order, and converts each answer into **thin end-to-end tracer-bullet tickets** only once it is made.

The map is an index: destination, notes, decisions so far, fog (in-scope questions not yet sharp enough to ticket) and out of scope.

## When to Use

- An initiative spans several sprints and its estimates range across an order of magnitude
- Planning keeps reopening the same questions, or code is being written "until we decide"
- Several owners (finance, legal, platform) must each make a call before work can start
- Parts of a large effort go to coding agents, who must not guess the design

## Clarify First

The destination fixes the scope of the whole map, so settle it before any ticket. When an input is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Destination:** an observable end state, not an activity; it decides what is fog and what is out of scope.
- **Decision owners:** who can make each kind of call; a ticket without an owner never leaves the frontier.
- **Fixed constraints:** dates, budgets and platform choices that are not up for decision, so they do not become tickets.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

```bash
# Validate a map: cycles, dangling ids, ownerless decisions, premature builds; prints order + frontier
python3 scripts/decision_map_validator.py \
  --input assets/sample_decision_map_clean.json --today 2026-11-08
```

```bash
# Check implementation tickets are vertical slices (and expand-migrate-contract is ordered)
python3 scripts/tracer_slice_checker.py \
  --input assets/sample_decision_map_flawed.json --format json
```

## Tools Overview

| Tool | Reads | Reports |
|------|-------|---------|
| `decision_map_validator.py` | Map JSON (`destination`, `fog`, `out_of_scope`, `tickets`) | Errors/warnings, stable topological order, frontier |
| `tracer_slice_checker.py` | Same file (implementation tickets only) | Horizontal slices, missing demo/criteria, vague criteria, refactor ordering |

### Exit code contract

`0` no error findings (warnings allowed) · `1` at least one error (the quality gate) · `2` unreadable input or bad arguments. Both tools exit 1 on the flawed sample by design and 0 on the clean one:

```bash
python3 scripts/decision_map_validator.py   --input assets/sample_decision_map_flawed.json; echo "exit $?"  # exit 1
```

## Workflow

Tags on the headings below: **[PROVEN]** means the rule is well established in practice and the validators check for it; **[RECOMMENDED]** means a sensible default practice to tune to your team.

1. **Name the destination** [PROVEN]. One or two sentences describing a checkable end state. If stakeholders disagree, that disagreement is the first decision; chart nothing else.
2. **Fan out breadth-first** [RECOMMENDED]. List unknown facts, forks, outside owners, irreversible choices. Sharp question → ticket; vague → fog; past the destination → out of scope.
3. **Write decision tickets.** Question ending in "?", type (research, prototype, discussion, enabling-task), at least two options for discussion and prototype, owner, decide-by date. Use `assets/ticket_templates.md`.
4. **Wire blocking links in a second pass** [RECOMMENDED]. Keep a link only if the blocker's least likely answer would change this ticket's options.
5. **Validate** — quality gate. Run `decision_map_validator.py`; fix every error before taking work.
6. **Take one frontier ticket per session** [PROVEN]. Claim it, resolve it, record chosen / why / rejected / consequences, close it, add one line to Decisions so far.
7. **Update the map.** Graduate fog that is now sharp, open new tickets, rule out anything past the destination.
8. **Convert resolved decisions into tracer bullets** [PROVEN]. Each slice names a behaviour, lists `derived_from`, crosses two or more layers, has a demo, testable criteria and an estimate of three days or less. Wide mechanical refactors become expand → migrate batches → contract.
9. **Check the slices.** Run `tracer_slice_checker.py`, then walk the review checklist in `references/decisions-to-tracer-bullets.md` with the people who will build them.
10. **Close the map** when frontier and fog are empty and each decision is converted or `no_build`.

## Anti-Patterns

### The Map That Became a Backlog
**Mistake:** Charting every task you can imagine, so the map holds forty tickets and no questions.
**Why it happens:** Listing work feels like progress; listing unknowns feels like ignorance.
**Instead:** Tickets resolve decisions or put resolved decisions into effect. Everything else leaves the map.

### Building on Hope
**Mistake:** Starting implementation tickets that depend on decisions still open.
**Why it happens:** Pressure to show progress.
**Instead:** The validator errors on it. Record the decision if it is made, or treat the code as a disposable prototype.

### Corridor Decisions
**Mistake:** Closing a decision ticket with no resolution text.
**Why it happens:** The call was made in a meeting and felt settled.
**Instead:** Write the chosen option, reason and rejected options first.

### Horizontal Implementation Tickets
**Mistake:** Converting good decisions into "schema", "API" and "UI" tickets.
**Why it happens:** Habit and org charts.
**Instead:** Slice by behaviour across every layer; the checker errors on single-layer slices.

## Files

| File | Purpose |
|------|---------|
| `scripts/decision_map_validator.py` | Map gate, order and frontier |
| `scripts/tracer_slice_checker.py` | Slice gate |
| `assets/sample_decision_map_clean.json` | Usage-based billing map mid-flight; both tools exit 0 |
| `assets/sample_decision_map_flawed.json` | Offline-mode map seeded with every failure; both tools exit 1 |
| `assets/decision_map_template.md` | Map page template |
| `assets/ticket_templates.md` | Decision, tracer-bullet and refactor-phase tickets |

## Reference Documentation

- [references/charting-the-map.md](references/charting-the-map.md) — destination, finding decisions, ticket vs fog, types, links, cycles, sessions, worked example. Read when charting or resuming.
- [references/decisions-to-tracer-bullets.md](references/decisions-to-tracer-bullets.md) — converting answers into slices, testable criteria, expand-migrate-contract, review checklist. Read before writing implementation tickets.
- [references/map-health-and-failure-modes.md](references/map-health-and-failure-modes.md) — health signals, each finding with its repair, cadence. Read when the map stalls.

## Scope & Limitations

**In Scope:** destination framing, decision tickets, fog and out-of-scope management, one-decision-per-session cadence, conversion into tracer-bullet and refactor tickets, validation and ordering.

**Out of Scope:**
- Tracking cross-team dependencies and the critical path of already-committed work (`project-management/execution/dependency-map/`).
- Slicing a user journey into releases (`project-management/execution/story-mapping/`).
- Splitting one oversized story (`project-management/execution/story-splitting/`).

**Important Caveats:**
- The tools read a hand-maintained JSON export; they do not call Jira, Linear or GitHub.
- Owners, options and statuses are self-reported. The validator checks that they exist, not that they are right.
- Layer names are free text; read the demo statement too.

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/charting-the-map.md

# Charting and Working a Decision Map

This reference covers the first two thirds of wayfinding: turning a large, foggy
piece of work into a map of decision tickets, and then working that map one
decision at a time. Converting resolved decisions into implementation tickets is
covered in `decisions-to-tracer-bullets.md`.

## 1. When a map is the right tool

A decision map earns its overhead when three things are true at once:

1. **The work is bigger than one sitting.** It will span several working sessions,
   several people, or several sprints. If one focused session could plan and finish
   it, a map is ceremony.
2. **The route is not visible.** You can describe where you want to end up, but you
   cannot yet list the build steps because they depend on choices nobody has made.
3. **Those choices block each other.** Some answers cannot be given until other
   answers exist. If every open question is independent, a simple checklist does the
   job.

Signals that you need one:

- Estimates for the work range across an order of magnitude ("two weeks or three
  months, depending").
- Every planning conversation re-opens the same three questions.
- Engineers are writing code that may be thrown away because "we'll decide later".
- A ticket titled "Investigate X" has been open for a month.

Signals that you do not:

- The open questions can all be answered in one meeting.
- The work is already decided and only needs sequencing across teams (a dependency
  map of committed work is the right tool for that).
- The work is a user journey that needs release slicing (a story map fits better).

## 2. Writing the destination

The destination is the single most important line on the map. It fixes scope, so it
decides what counts as fog (in scope, not yet sharp) and what counts as out of scope
(beyond the destination). Write it before any ticket.

A good destination is:

| Property | Test | Example |
|----------|------|---------|
| Observable | Could a stranger check whether it is true? | "Every invoice reconciles to the ledger within 0.5%" |
| End state, not activity | Does it describe a world, not work? | "is billed per seat-hour", not "build metering" |
| Bounded | Does it exclude something tempting? | "new self-serve workspaces" (legacy excluded) |
| One sentence or two | Can it be read at the start of every session? | — |

The destination can also be a decision or a spec rather than a shipped change:
"A signed-off data-retention policy that legal and engineering both accept" is a
valid destination. A map whose destination is a decision ends when that decision is
made and recorded; there are no implementation tickets.

Common destination failures:

- **Activity framing.** "Explore offline mode." There is no point at which exploring
  is done, so the map never closes.
- **Solution baked in.** "Ship the Kafka-based sync pipeline." The choice of Kafka was
  one of the decisions the map should have contained.
- **Unbounded.** "Modernise billing." Everything is in scope, so nothing is out of
  scope, and the fog list grows forever.

When stakeholders disagree on the destination, stop. Do not chart tickets. Resolve
the destination as its own decision first, usually as a short written proposal with
two or three candidate destinations and the trade-offs between them.

## 3. Finding the decisions

Fan out breadth-first across the whole problem before going deep on any thread. The
aim of the first charting session is coverage, not answers. Useful prompts:

- **Unknown facts.** What do we not know that would change what we build? (limits,
  volumes, costs, vendor capabilities, legal constraints)
- **Forks.** Where are there two or more plausible approaches with different costs?
- **Ownership.** Which choices belong to someone outside the team (finance, legal,
  security, a platform team)?
- **Irreversibility.** Which choices are expensive to undo (data model, public API,
  pricing, contracts)? These deserve tickets even when the answer seems obvious.
- **Presentation.** Where will people need to see something before they can choose?
- **Prerequisites.** What access, data or environment must exist before anyone can
  even evaluate the options?

Each answer that survives becomes either a ticket, a fog item, or an out-of-scope
line. Use the sharpness test below to decide which.

## 4. Ticket, fog, or out of scope

| You can... | And it is... | It becomes |
|------------|--------------|------------|
| State the question precisely now | Inside the destination | A decision ticket (even if blocked) |
| Sense the question but not phrase it | Inside the destination | A fog line, noting what it hangs on |
| Phrase it or not | Beyond the destination | An out-of-scope line with a reason |

The test for ticket versus fog is **whether you can state the question sharply, not
whether you can answer it**. A sharp but blocked question is still a ticket; the
blocking link is what keeps it off the frontier.

Do not slice fog into ticket-sized pieces in advance. Fog is coarser than tickets: a
single fog line may later become three tickets, or none, once the answers ahead of it
are known. Pre-slicing produces tickets built on guesses, which then have to be
rewritten.

Marking something out of scope narrows the work; it does not add a ticket to the map. Nothing in that list is ever promoted to a build ticket.
If one comes back, the destination has changed, and that is a new effort or an
explicit redraw of the map, not a quiet addition.

## 5. Ticket types

Every decision ticket has exactly one type. The type tells whoever picks it up how
it gets resolved.

| Type | Resolved by | Needs a human in the loop? | Typical length |
|------|-------------|---------------------------|----------------|
| research | Reading docs, data, code, vendor APIs; reporting a fact | No, can be delegated | Hours |
| prototype | Making a rough concrete artefact people react to | Yes, the reaction is the point | Half a day |
| discussion | A person with authority choosing between options | Yes, always | One session |
| enabling-task | Doing prerequisite work so another decision becomes possible | Sometimes | Hours to a day |

Rules that keep types honest:

- A **research** ticket returns a fact, not a choice. If the researcher ends up
  choosing, split the ticket: research for the fact, discussion for the choice.
- A **discussion** ticket needs at least two real options, including "do nothing" when
  that is genuine. A discussion with one option is a decree; record it as resolved.
- A **prototype** ticket also needs options: the prototype exists to compare them.
- An **enabling-task** must name the decision it unblocks. Work that unblocks nothing
  on the map is implementation work wearing the wrong label.
- Nobody may answer their own discussion ticket on behalf of the owner. An agent or
  analyst can prepare the options and a recommendation; the owner makes the call.

## 6. Owners and decide-by dates

The owner is the person who makes the call, not the person who does the research.
For a pricing decision the researcher might be an analyst and the owner the head of
product. A ticket with no owner will sit on the frontier until someone notices it has
been there for weeks.

Decide-by dates exist to expose the cost of delay. Write next to the date what slips
if it is missed ("T1 cannot start; launch moves a week"). A decide-by date that has
passed is a warning in `decision_map_validator.py` when run with `--today`; treat a
run of overdue tickets as a signal that the owners are wrong or overloaded, not that
the dates were optimistic.

## 7. Blocking links

Draw a blocking link only when one question genuinely cannot be answered without the
other's answer. Over-linking collapses the frontier: everything waits on everything
and nothing is takeable. Under-linking causes rework: a decision made before its
prerequisite gets reopened.

Test each link by asking: "If the blocker came back with its *least* likely answer,
would this ticket's options change?" If not, remove the link.

Create tickets first and wire links in a second pass. Trackers need ids before
tickets can reference each other, and writing placeholder references produces links
to unrelated issues.

Cycles mean two questions have been drawn as each other's prerequisite. They are
almost always one of three things:

1. **Two halves of one decision.** Merge them into a single ticket.
2. **A missing fact both depend on.** Extract a research ticket that both are blocked by.
3. **A wrong link.** Apply the least-likely-answer test and drop the weaker edge.

The validator reports every cycle as a closed path so you can see which edge to cut.

## 8. Working the map

Each working session:

1. **Load the map page**, not every ticket. The decisions-so-far index gives the
   low-resolution view; open individual tickets only as needed.
2. **Run the validator.** Fix any error before taking work. An error means the map is
   lying about what is takeable.
3. **Take one frontier ticket.** The frontier is every open, unclaimed ticket whose
   blockers are all closed. Decisions come before implementation in the tool output
   because an unmade decision ripples further than an unbuilt slice.
4. **Claim it** before doing anything else, so a parallel session does not take it too.
5. **Resolve it** according to its type.
6. **Record the resolution on the ticket**: chosen option, reason, rejected options,
   consequences, and what would make you revisit it. Close the ticket.
7. **Add one line to Decisions so far**: title, link, one-clause gist.
8. **Update the map**: graduate fog that is now sharp into tickets (and delete it from
   the fog list), open newly surfaced tickets, rule anything now beyond the destination
   out of scope, and convert the resolution into implementation tickets where it is ready.

Resolve one decision per session. A session that tries to settle several decisions
usually settles the first and quietly assumes the rest. Research tickets are the
exception: several can run in parallel because none of them chooses anything.

## 9. Parallel sessions

When several people or agents work the same map:

- The claim (assignee plus `claimed` status) is the lock. An open, unassigned ticket
  is free; anything else is taken.
- Expect the map to change under you. Reload it before recording a resolution.
- Never edit another session's claimed ticket. Comment on it instead.
- Keep the decisions-so-far index append-only; reordering it causes merge pain and
  destroys the record of the route actually walked.

## 10. Worked example (abridged)

**Destination:** "New self-serve workspaces are billed per active seat-hour through
the new metering pipeline, and every invoice reconciles to the ledger within 0.5%
before month-end close."

First charting session produced:

| Id | Type | Question | Blocked by |
|----|------|----------|-----------|
| D1 | discussion | What unit do we meter and bill on? | — |
| D2 | research | Do we rate usage ourselves or send it to the provider to rate? | D1 |
| D3 | discussion | Which identifier keys usage records, given account_id is overloaded? | — |
| D4 | prototype | How should seat-hour usage appear on the invoice? | D2 |
| D5 | discussion | What happens when a usage invoice fails to collect? | D2 |
| D6 | enabling-task | Can we get a provider sandbox with metered prices? | D2 |

Fog: proration on mid-cycle plan changes (hangs on D2 and D5); who receives usage
alerts. Out of scope: migrating legacy flat-rate customers; multi-currency invoicing.

After three sessions D1, D2 and D3 were resolved, the D3 answer became a four-ticket
expand-migrate-contract refactor, and D1+D2 became the first tracer bullet. The full
JSON is in `assets/sample_decision_map_clean.json`.

## 11. Closing the map

The map is finished when:

- the destination is reached (or, for a decision-destination, the decision is made);
- the frontier is empty and no fog remains;
- every resolved decision either has implementation tickets or is marked as needing
  none (`no_build: true`);
- the decisions-so-far index reads as a coherent account of how the route was found.

Archive the map rather than deleting it. Six months later, the index is the fastest
way for someone to learn why the system is shaped the way it is.

## references/decisions-to-tracer-bullets.md

# From Resolved Decisions to Tracer-Bullet Tickets

A decision map produces answers. Answers do not ship. This reference covers the
conversion step: turning each resolved decision into thin, end-to-end implementation
tickets that can be built, demoed and verified one at a time.

## 1. What a tracer bullet is

A tracer-bullet ticket delivers a narrow path through **every layer the behaviour
needs**, all the way to something a person can observe. It is thin in breadth and
complete in depth.

| | Tracer bullet (vertical) | Layer ticket (horizontal) |
|--|--------------------------|---------------------------|
| Shape | One behaviour, every layer | One layer, many behaviours |
| Done means | Someone can demo it | Code exists in one layer |
| Integration risk | Paid on day one | Deferred to the end |
| Feedback | Immediate, from real use | None until all layers meet |
| Can be reprioritised | Yes, each slice stands alone | No, layers depend on each other |

The reason to slice vertically is not tidiness. It is that integration is where the
surprises live, and a vertical slice forces integration on the first ticket instead
of the last. When the first slice works, the architecture has been proven end to end
at small scale.

## 2. When a decision is ready to convert

Convert a resolved decision when:

- the resolution names a choice concrete enough to build against;
- every other decision the build depends on is also resolved;
- the result would be demoable on its own.

Some resolutions convert immediately ("meter on seat-hours" plus "provider rates
usage" together give the first slice). Others never produce code ("we will not
support offline edits on shared devices") and are marked `no_build: true`. Others
must wait for a sibling decision; leave them resolved and unconverted, and the
validator will keep a gentle warning on them until you act.

Never convert a decision that is still open. An implementation ticket that depends on
an open decision is a bet that the decision goes a particular way. The validator
treats this as an error because it is the most common source of thrown-away work.

## 3. Writing the slice

For each slice, write:

1. **A title that names a behaviour.** "One workspace's seat-hours appear at the
   provider", not "Build metering API".
2. **Derived from.** The decision ids it puts into effect. This is the traceability
   that lets someone ask "why does this exist?" and get an answer.
3. **Layers crossed.** List them explicitly. A list with one entry is the signal that
   the slice is horizontal.
4. **Demo.** What someone will run or look at. If you cannot write it, the slice does
   not end anywhere observable.
5. **Acceptance criteria.** Observable statements with numbers or concrete examples.
   Cover the happy path, one failure path, and any idempotency or retry behaviour.
6. **Blocked by.** Only the tickets that genuinely gate it.
7. **Estimate.** Three days or fewer. Larger slices hide a second behaviour.
8. **Out of scope for this slice.** The adjacent work that will be tempting mid-build.

### Testable criteria

| Untestable | Testable |
|-----------|----------|
| "Metering works correctly" | "An hour with 2 active seats reports exactly 2 seat-hours" |
| "Handles errors properly" | "A failed provider call is retried 3 times then logged with workspace_id" |
| "Fast enough" | "Hourly aggregation for 10k workspaces completes in under 5 minutes" |
| "Report looks good" | "Rows with variance above 0.5% are highlighted" |

The slice checker flags vague wording (works, properly, correctly, as expected, etc.)
as warnings. They are warnings rather than errors because sometimes the word is
used precisely; read each one.

### Describe behaviour, not files

Implementation tickets often sit for days or weeks before someone picks them up. File
paths, line numbers and function names drift in that time. Describe interfaces,
contracts and observable behaviour; let the implementer find the code. The one
exception is a schema or type shape that a prototype already settled, which can be
quoted because it *is* the decision.

## 4. Choosing the first slice

The first slice should be the one that proves the riskiest integration with the least
scope. Ask:

- Which layer has never talked to which other layer before?
- Which external system have we not yet called in anger?
- Which assumption, if wrong, would invalidate the most later slices?

The first slice through the billing example touched event capture, the aggregation
job, the provider client and an integration test, for one workspace and one hour.
Nothing about invoices, dunning or reporting: those are later slices that reuse the
path the first one proved.

## 5. Slicing patterns

When a slice is too big, cut along one of these lines:

| Cut by | Example |
|--------|---------|
| One entity first | One workspace, then all workspaces |
| One happy path first | Successful collection, then failed collection |
| Manual before automated | Finance runs the report by hand, then it is scheduled |
| Read before write | Show usage, then let users change their plan |
| Simple rule first | Flat seat-hour price, then tiers |
| One channel first | Email notification, then in-app |

Each cut must still cross every layer. "One workspace" is a valid cut; "database
only" is not.

## 6. The exception: wide mechanical refactors

Some changes cannot be sliced vertically because they are one mechanical edit that
fans out across hundreds of call sites: renaming a widely used field, changing the
type of a shared identifier, moving a module. Making the edit in one go breaks every
caller at once, and no vertical slice can land with the build green.

Sequence these as **expand, migrate, contract**:

1. **Expand.** Add the new form beside the old. Both work. Nothing breaks. One ticket.
2. **Migrate.** Move callers to the new form in batches sized so each batch lands with
   the suite passing (per package, per directory, per service). One ticket per batch,
   each blocked by the expand ticket. Batches can run in parallel.
3. **Contract.** Remove the old form once nothing uses it. One ticket, blocked by
   every migrate batch.

The slice checker enforces exactly this: one expand per refactor group, every migrate
blocked by the expand, the contract blocked by every migrate. A contract that can run
before a migrate batch would delete the old form under live callers.

If even individual migrate batches cannot stay green alone (because callers are
tightly coupled), keep the same sequence on a shared integration branch and add a
final integrate-and-verify ticket blocked by every batch. Only that final ticket
promises a green build.

Place the refactor before the slices that need the new form: in the billing sample,
the first tracer bullet is blocked by the contract ticket so that new metering code is
written only against `workspace_id`.

## 7. Ordering the implementation tickets

Run `decision_map_validator.py`. Its dependency order covers decisions and
implementation together, using Kahn's algorithm with ties broken by id so the order is
stable from run to run. The frontier shows what can be picked up now.

For implementation work, prefer:

1. Refactor expand tickets (they unblock everything that follows).
2. The first tracer bullet (it proves the path).
3. Slices that reuse the proven path, in order of risk retired per day of effort.
4. Contract tickets as soon as their migrate batches are done, so the old form does
   not linger.

## 8. Review before handing out

Before tickets go to a team or a coding agent, check:

- [ ] Every implementation ticket has `derived_from` pointing at resolved decisions.
- [ ] No ticket is blocked by, or built on, an open decision.
- [ ] Every slice lists two or more layers, a demo and testable criteria.
- [ ] No slice is over three days.
- [ ] Every refactor group has one expand, at least one migrate, one contract, with the
      blocking links in the right direction.
- [ ] Both tools exit 0.

Ask the people who will build the slices whether the granularity feels right and
whether each blocking edge is real. Adjust and re-run the tools. A breakdown nobody
on the building side has read is a plan only on paper.

## references/map-health-and-failure-modes.md

# Map Health and Failure Modes

A decision map decays like any other plan. This reference gives the signals that a map
is healthy or stuck, the validator findings that map to each failure mode, and the
repair for each.

## 1. Health signals to track each session

| Signal | Healthy | Worry | How to read it |
|--------|---------|-------|----------------|
| Frontier width | 2-5 tickets | 0, or more than 10 | Zero means stalled; too many means links are missing or the map is a backlog in disguise |
| Decision latency (open to resolved) | Days | Weeks | Long latency points at the wrong owner or a missing prerequisite |
| Overdue decide-by dates | 0-1 | 3+ | A cluster means owners are overloaded or dates were invented |
| Fog list size | Shrinking over time | Growing every session | Growing fog means the destination is too broad |
| Decisions resolved per week | Steady | Zero for two weeks | The map has stopped being worked; ask why before adding more tickets |
| Resolved but unconverted decisions | Few, recent | Many, old | Planning is outrunning building, or decisions are vaguer than they look |
| Reopened decisions | Rare | Frequent | Decisions are being made before their prerequisites |

Run `decision_map_validator.py --today <date>` at the start of each session and paste
the counts into the map's health section. The trend matters more than any single
reading.

## 2. Validator findings and what they mean

| Finding | Severity | What it usually means | Repair |
|---------|----------|-----------------------|--------|
| no destination | error | The effort was charted before anyone agreed on the end state | Stop; resolve the destination first |
| blocking cycle | error | Two halves of one decision, a shared missing fact, or a wrong link | Merge, extract a research ticket, or drop the weaker edge |
| unknown blocker id | error | A ticket was deleted or mistyped; the dependent looks blocked forever | Fix the id or remove the link |
| decision has no owner | error | Nobody can make the call | Name the person with authority, not the researcher |
| fewer than 2 options | error | A discussion with one option is a decree, not a decision | Add the real alternatives (including "do nothing") or mark it resolved |
| resolved without resolution | error | The answer lived in a meeting and was not written down | Write chosen / why / rejected / consequences before anything else |
| built on / blocked by unresolved decision | error | Someone started building on a guess | Pause the implementation ticket or resolve the decision now |
| in progress while blocker open | error | Work started out of order | Either the link is wrong or the work is premature |
| orphan implementation ticket | error | Work that traces to no decision on the map | Link it, or move it off the map if it serves another effort |
| question not phrased as a question | warn | The ticket names a topic, not a decision | Rewrite as one sentence ending in "?" |
| isolated decision | warn | No links in or out; may not serve the destination | Confirm it belongs, link it, or rule it out of scope |
| resolved, not converted | warn | Planning ahead of building | Convert, or mark `no_build: true` |
| decide-by passed | warn | The decision is late | Escalate to the owner with what is slipping |
| claimed without claimant | warn | A lock nobody holds | Set `claimed_by` or return the ticket to open |
| frontier empty, work remains | warn | Everything open is blocked or the map is stuck | Look for cycles, unknown ids, or a missing enabling task |

## 3. Failure modes in practice

### The map that became a backlog

Symptoms: forty tickets, most of them implementation work, frontier of fifteen, no
fog. Cause: the planner charted every task they could imagine instead of only the
questions blocking the route. Repair: close or move every ticket that does not resolve
a decision or put a resolved decision into effect. A map holds questions and the
slices that follow from answered ones, not every chore.

### Fog that never clears

Symptoms: the fog list grows every session and nothing graduates. Cause: the
destination is too broad, so every resolution reveals more in-scope territory.
Repair: redraw the destination tighter and move the excess to out of scope with a
reason. If stakeholders resist, that disagreement is itself the first decision.

### The decision made in the corridor

Symptoms: a ticket closed as resolved with no resolution text, or a resolution like
"agreed in sync". Cause: the decision happened in conversation and nobody wrote it
down. Repair: the validator blocks this as an error. Write the chosen option, the
reason, and the rejected options before taking the next ticket. A decision nobody can
read later will be reopened.

### Building on hope

Symptoms: implementation tickets in progress that derive from open decisions.
Cause: pressure to show progress. Repair: either the decision is actually made (record
it) or the code is a prototype (move it to a prototype decision ticket and treat the
code as disposable). Do not let it become the default answer by inertia.

### The ownerless frontier

Symptoms: frontier tickets sit for weeks; nobody claims them. Cause: owners are
missing, or are people outside the team who do not know they own anything. Repair:
name owners at charting time and send each owner their tickets with the decide-by date
and the consequence of delay. A short structured questionnaire to an external owner
often resolves a ticket faster than a meeting.

### Too many links

Symptoms: frontier of zero or one even though most tickets are open; long chains in the
dependency order. Cause: every vague relationship drawn as a blocking link. Repair:
apply the least-likely-answer test to each link and remove the ones that do not change
options.

### The cycle hidden by a long chain

Symptoms: the validator reports a cycle of four or more tickets. Cause: each link
looked reasonable on its own. Repair: find the edge where the dependency is weakest
(often a "nice to know" research result) and cut it, or extract the shared missing fact
into its own research ticket that every member of the cycle depends on.

### Horizontal tickets after a good map

Symptoms: the decisions were made well, then the implementation tickets came out as
"database schema", "API endpoints", "UI screens". Cause: the conversion step was rushed
or done by habit. Repair: run `tracer_slice_checker.py`; every single-layer ticket is
an error. Re-slice around behaviours using the patterns in
`decisions-to-tracer-bullets.md`.

## 4. Cadence

| Effort size | Session cadence | Map review |
|-------------|-----------------|-----------|
| 2-4 weeks | One decision per day | End of each week |
| 1-3 months | Two to three decisions per week | Every two weeks with owners |
| Quarter+ | Weekly decision session per workstream | Monthly with sponsor; redraw destination if fog grows |

A map review is not a status meeting. Its agenda is: frontier, overdue decisions,
fog that is ready to graduate, anything that should move out of scope, and whether the
destination still holds.

## 5. When to abandon a map

Abandon or restart when:

- the destination has changed materially (start a new map, link the old one);
- two consecutive reviews show no resolved decisions and no clear reason;
- the remaining questions are all answerable in one meeting (hold the meeting, close
  the map, and convert what is left directly into implementation tickets).

Archive the abandoned map with a one-paragraph note on why. The decisions it did reach
are still valid input to whatever replaces it.

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/wayfinder -->
