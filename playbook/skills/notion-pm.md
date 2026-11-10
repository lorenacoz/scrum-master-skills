# notion-pm

> **Use these instructions for this whole conversation.** Apply them when: Designs Notion databases, views and page structure for PRDs, OKRs, roadmaps and decisions, and writes REST API calls. Use when asked to "design a PRD database", sync Notion with Jira or Linear, or script the Notion API.

# Notion for Product Management

Master-level expertise in using Notion as the documentation and operational backbone for a product team: PRDs, OKRs, roadmaps, decision logs, sprint reviews, 1:1 notes, customer research, and sync patterns with Jira, Linear, and GitHub. Covers Notion's database model, view design, formula and rollup patterns, page architecture, and REST API.

## Overview

Notion's PM value comes from its database model: every meaningful PM artifact (a PRD, an OKR, a roadmap row, a decision) becomes a row in a typed database, with relations to other databases. This unlocks linked views (one source of truth, many surface presentations), rollups (aggregate child progress into a parent), and a queryable API. The job of a Notion PM expert is to design these databases up front, restrain ad-hoc page creation, and tie the workspace into Jira/Linear/GitHub so the artifacts stay current without manual maintenance.

## Core Capabilities

- **Database design** — typed schemas for PRDs, OKRs, Roadmap, Decisions, and Sprint/Cycle Reviews, with the right property types (relation, rollup, formula, status, unique_id).
- **View design** — Table, Board, Timeline, Calendar, Gallery, and List views with filters, sorts, and groups tuned per artifact.
- **Page & workspace architecture** — Teamspace setup, curated home dashboards, linking strategy (relations vs mentions vs sub-pages), governance and review cadence.
- **REST API authoring** — query/create/update/append calls, compound filters, pagination, and rate-limit handling.
- **Sync patterns** — one-way, two-way, roll-up, and embed integrations with Jira, Linear, and GitHub.

## When to Use

- Standing up a new product team's documentation workspace
- Designing a PRD, OKR, Roadmap, or Decisions database from scratch
- Refactoring an existing Notion workspace that has grown into a sprawl of unrelated pages
- Building roadmap or status views aggregated from underlying issue trackers
- Authoring Notion REST API calls (page creation, database queries, block updates)
- Setting up two-way sync between Notion and Jira/Linear/GitHub
- Establishing governance: ownership, review cadence, archive strategy

## Clarify First

Notion advice depends most on whether the user is designing a workspace or scripting against the API, and on what already exists. Settle the inputs below before producing anything. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **New workspace or existing sprawl:** A new workspace can start from the canonical schemas in `references/notion-database-design-for-pm.md`. A refactor needs an inventory first: which PRDs live outside the database, which cross-database references are plain text instead of Relations, and who owns each Teamspace.
- **Read-only, write or sync:** Querying a database is low risk but has to loop on `has_more`. Creating pages, updating properties or running a two-way sync with Jira, Linear or GitHub writes to shared content, and the limit of about 3 requests per second decides whether a sync needs batching and a queue.
- **Plan tier and API version:** Lower plan tiers cannot create Status options through the API, so those must be created by hand first. The API references target `Notion-Version: 2025-09-03`, where databases are queried as data sources; an integration pinned to an older version uses different endpoints and cannot chain rollups.
- **Access level:** Teamspace setup, database design and views are in scope for a Teamspace owner. SCIM, SAML and billing are workspace-admin tasks outside this skill, and Teamspace-level changes can override page permissions, so know who can change what before proposing a permission model.

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Anti-Patterns

### Ignoring API pagination
**Mistake:** A script queries a database through `POST /v1/data_sources/{data_source_id}/query`, gets 100 results back and treats them as all results.
**Why it happens:** The first page looks complete, and small test databases never go past 100 rows.
**Instead:** Loop until `has_more` is false, passing `next_cursor` as `start_cursor` on each call. Any Notion API call that doesn't loop on `has_more` is broken, and decisions made on its output rest on a partial sample.

### Cross-database links stored as text
**Mistake:** The PRDs, OKRs and Roadmap databases exist, but each PRD names its OKR in plain text instead of linking to it.
**Why it happens:** Typing a name is quicker than setting up a Relation property, and it reads fine on the page.
**Instead:** Convert every cross-database reference to a Relation. Text references go stale when the OKR's wording changes, and they make basic queries like "all PRDs supporting this OKR" impossible.

### PRDs as free-form pages
**Mistake:** Each PRD is a hand-made page in a folder, some with a status and some without.
**Why it happens:** A new page is Notion's default, and a database feels like overhead for a few documents.
**Instead:** Make every PRD a row in the PRDs database with consistent properties (see `references/notion-database-design-for-pm.md`). Then you can query which PRDs are blocked or waiting on design review. Migrate PRD pages that live outside the database.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## Reference Documentation

Pull the reference that matches the task; keep this file lean and load detail on demand.

- **[references/notion-pm-playbook.md](references/notion-pm-playbook.md)** — the full operational playbook: core concepts (hierarchy, property types, views, block types), the seven core workflows (workspace setup, PRD/OKR/Roadmap/Decisions/Review DB design, linking, sync), inline API/query examples, best practices, troubleshooting, and success criteria. Read when building or refactoring a workspace.
- **[references/notion-api-patterns.md](references/notion-api-patterns.md)** — full REST API call catalog with request/response examples, targeting `Notion-Version: 2025-09-03` (databases → data sources; as of September 2026). Read when authoring API integrations.
- **[references/notion-database-design-for-pm.md](references/notion-database-design-for-pm.md)** — canonical schemas for PRDs, OKRs, Roadmap, Decisions, Reviews. Read when designing the database relations.
- **[references/red-flags.md](references/red-flags.md)** — concrete examples of how Notion PM setups go wrong and how to fix them. Read when reviewing a workspace for quality.
- **assets/notion-prd-template.md** — PRD page template using Notion-native blocks.
- **assets/notion-roadmap-template.md** — Roadmap database schema and view definitions.
- **assets/notion-okr-template.md** — OKR database schema with Wodtke confidence model.
- Notion API docs: https://developers.notion.com/ — reference: https://developers.notion.com/reference/intro — changelog: https://developers.notion.com/page/changelog

## Scope & Limitations

**In Scope:** Notion workspace and Teamspace setup, database design for PRDs/OKRs/Roadmap/Decisions/Reviews/1:1s, view design, property and relation modeling, page architecture, Notion REST API authoring, sync pattern design with Jira/Linear/GitHub, governance and review cadences.

**Out of Scope:** Notion administration (SCIM, SAML, billing) at the workspace level beyond Teamspace setup. Jira space and project configuration (hand off to `jira-expert/` and `confluence-expert/`). Linear configuration (hand off to `linear-expert/`). Strategic OKR setting (hand off to `execution/brainstorm-okrs/`). Story splitting and backlog refinement (hand off to `execution/backlog-refinement/`, `execution/story-splitting/`).

**Limitations:** Notion's API rate limits (~3 req/s) make it unsuitable for very high-throughput sync; batch and queue. Status properties cannot have options created via the API in lower plan tiers; pre-create options manually. Rollups cannot reference rollups in older API versions; chain via formulas where needed. Page-level permissions can be overridden in unexpected ways by Teamspace-level changes. Notion is not a real-time collaboration substitute for chat; do not try to replace Slack with comments.

## Integration Points

| Integration | Direction | What Flows |
|---|---|---|
| `jira-expert/` | Notion ↔ Jira | PRD-to-Epic creation; Jira issue embeds in PRD pages |
| `confluence-expert/` | Migration | When moving from Confluence to Notion, structure and content mapping |
| `linear-expert/` | Notion ↔ Linear | PRD-to-Project creation; Linear progress rollups into Notion |
| `execution/create-prd/` | PRD → Notion | PRD scaffolder output rendered as Notion blocks via `--format notion` |
| `execution/brainstorm-okrs/` | OKR → Notion | OKR validator output written to the OKR DB |
| `execution/outcome-roadmap/` | Roadmap → Notion | Roadmap rows materialized in the Roadmap DB |
| `execution/daci-framework/` | Decision → Notion | DACI decisions logged in the Decisions DB |
| `execution/status-update-generator/` | Notion → Status | Weekly status pulls aggregates from PRDs/OKRs DBs |
| `execution/release-notes/` | Notion → Release | Shipped PRDs feed release notes input |
| `senior-pm/` | Notion → Portfolio | OKR and Roadmap DBs feed portfolio reports |
| `discovery/interview-synthesis/` | Research → Notion | Customer research database populated from interview synth output |

## Files

Reference files are described under Reference Documentation above. Templates:

| File | Purpose |
|------|---------|
| `assets/notion-okr-template.md` | Database template |
| `assets/notion-prd-template.md` | Database template |
| `assets/notion-roadmap-template.md` | Database template |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/notion-api-patterns.md

# Notion REST API Patterns

Canonical Notion API calls for PM workflows. Endpoint base: `https://api.notion.com/v1/`. Auth: `Authorization: Bearer secret_...` (internal integration token) or OAuth2. Every request must include a `Notion-Version` header. These recipes target **`2025-09-03`**, the version that introduced **data sources** (as of September 2026; a newer version, `2026-03-11`, also exists — see the version note below).

All examples use `curl` for clarity; the same JSON bodies apply to any HTTP client.

---

## 1. Authentication & Connection

```bash
export NOTION_TOKEN="secret_..."
export NOTION_VERSION="2025-09-03"

NOTION_HEADERS=(
  -H "Authorization: Bearer $NOTION_TOKEN"
  -H "Notion-Version: $NOTION_VERSION"
  -H "Content-Type: application/json"
)
```

An integration only sees pages and databases that have been **explicitly shared** with it (open the database → "..." → Add connections). 404s are almost always a missing share.

### Version note — databases vs. data sources (as of September 2026)

From `Notion-Version: 2025-09-03`, a **database** is a container that holds one or more **data sources**; the rows, the property schema and queries live on the data source. What changed versus `2022-06-28`:

| Task | `2022-06-28` | `2025-09-03` |
|---|---|---|
| Query rows | `POST /v1/databases/{database_id}/query` | `POST /v1/data_sources/{data_source_id}/query` |
| Read property schema | `GET /v1/databases/{database_id}` | `GET /v1/data_sources/{data_source_id}` |
| Change property schema | `PATCH /v1/databases/{database_id}` | `PATCH /v1/data_sources/{data_source_id}` |
| Create a row (page) | `"parent": { "database_id": ... }` | `"parent": { "type": "data_source_id", "data_source_id": ... }` |
| Search filter for DBs | `"value": "database"` | `"value": "data_source"` |
| Create a database | `properties` at top level | `properties` nested under `initial_data_source` |
| Webhook events | `database.content_updated`, `database.schema_updated` | `data_source.content_updated`, `data_source.schema_updated` |

`PATCH /v1/databases/{database_id}` still exists but now only covers database-level fields (`parent`, `title`, `is_inline`, `icon`, `cover`, `in_trash`). Relation properties must reference a `data_source_id`; `database_id` is no longer accepted in requests. Always send the version header explicitly — do not mix versions within one integration.

`2026-03-11` is the latest version as of September 2026. Its breaking changes: `archived` replaced by `in_trash`, the append-children `after` parameter replaced by a `position` object, and the `transcription` block type renamed to `meeting_notes`. The recipes below do not use any of those fields. Notion states it has no current plans to stop supporting older versions.

Sources: https://developers.notion.com/docs/upgrade-guide-2025-09-03 · https://developers.notion.com/docs/upgrade-guide-2026-03-11 · https://developers.notion.com/reference/versioning

---

## 2. Discovery — IDs You Need First

Notion IDs are 32-char hex (sometimes hyphenated). The API accepts both forms.

**Resolve a database to its data source ID** (required before querying or creating rows):
```bash
curl -X GET "https://api.notion.com/v1/databases/<db_id>" "${NOTION_HEADERS[@]}"
```
The response lists the database's data sources:
```json
"data_sources": [
  { "id": "<data_source_id>", "name": "PRDs" }
]
```
Most PM databases have exactly one data source; cache its `id`. If a database has several, pick by `name` — never assume index 0.

**Retrieve the property schema** (lives on the data source):
```bash
curl -X GET "https://api.notion.com/v1/data_sources/<data_source_id>" "${NOTION_HEADERS[@]}"
```
Use the `properties` in the response to inspect property names, types, and the exact option strings for `select` / `status` / `multi_select` properties. Selectable options are **case-sensitive** when set via the API.

**Search for a database by title** (returns data source objects on `2025-09-03`):
```bash
curl -X POST "https://api.notion.com/v1/search" "${NOTION_HEADERS[@]}" \
  -d '{
    "query": "PRDs",
    "filter": { "value": "data_source", "property": "object" }
  }'
```

**Get a user (for the People property)**:
```bash
curl -X GET "https://api.notion.com/v1/users" "${NOTION_HEADERS[@]}"
```
Cache user IDs; they are stable.

---

## 3. Querying Databases (via their data source)

**Basic query**:
```bash
curl -X POST "https://api.notion.com/v1/data_sources/<data_source_id>/query" "${NOTION_HEADERS[@]}" \
  -d '{
    "filter": { "property": "Status", "status": { "equals": "In Review" } },
    "sorts":  [{ "property": "Target Date", "direction": "ascending" }],
    "page_size": 100
  }'
```

**Compound filter (AND)**:
```json
{
  "filter": {
    "and": [
      { "property": "Owner",  "people": { "contains": "<user_id>" } },
      { "property": "Status", "status": { "does_not_equal": "Killed" } },
      { "property": "Target Date", "date": { "next_quarter": {} } }
    ]
  }
}
```

**Compound filter (OR)**:
```json
{
  "filter": {
    "or": [
      { "property": "Status", "status": { "equals": "At Risk" } },
      { "property": "Status", "status": { "equals": "Off Track" } }
    ]
  }
}
```

**Filter by relation**:
```json
{ "filter": { "property": "OKR", "relation": { "contains": "<okr_page_id>" } } }
```

**Pagination**:
```json
{ "page_size": 100, "start_cursor": "<cursor_from_previous_response>" }
```
Loop while `has_more` is true, passing `next_cursor` as the next `start_cursor`.

---

## 4. Creating a Page in a Database

**Minimal PRD page**:
```bash
curl -X POST "https://api.notion.com/v1/pages" "${NOTION_HEADERS[@]}" \
  -d '{
    "parent": { "type": "data_source_id", "data_source_id": "<prd_data_source_id>" },
    "properties": {
      "Title":   { "title":  [{ "text": { "content": "PRD: Self-Serve Signup" } }] },
      "Status":  { "status": { "name": "Draft" } },
      "Owner":   { "people": [{ "id": "<user_id>" }] },
      "Target Date": { "date": { "start": "2026-09-30" } },
      "Priority":    { "select": { "name": "P1" } }
    },
    "children": [
      { "object": "block", "type": "heading_2",
        "heading_2": { "rich_text": [{ "text": { "content": "Problem" } }] } },
      { "object": "block", "type": "paragraph",
        "paragraph": { "rich_text": [{ "text": { "content": "Today, new users must..." } }] } },
      { "object": "block", "type": "callout",
        "callout": {
          "icon":     { "type": "emoji", "emoji": "ℹ" },
          "rich_text": [{ "text": { "content": "Reviewed by Eng + Design on 2026-05-19." } }]
        }
      }
    ]
  }'
```

**Setting a relation**:
```json
{
  "properties": {
    "OKR": { "relation": [{ "id": "<okr_page_id_1>" }, { "id": "<okr_page_id_2>" }] }
  }
}
```

**Setting multi_select**:
```json
{ "properties": { "Areas": { "multi_select": [{ "name": "API" }, { "name": "Web" }] } } }
```

---

## 5. Updating a Page

**Update properties only** (does not touch the page body):
```bash
curl -X PATCH "https://api.notion.com/v1/pages/<page_id>" "${NOTION_HEADERS[@]}" \
  -d '{
    "properties": {
      "Status":      { "status": { "name": "Approved" } },
      "Approved On": { "date":   { "start": "2026-05-21" } }
    }
  }'
```

**Move a page to trash** (Notion's "delete"):
```bash
curl -X PATCH "https://api.notion.com/v1/pages/<page_id>" "${NOTION_HEADERS[@]}" \
  -d '{ "in_trash": true }'
```

**Restore from trash**:
```json
{ "in_trash": false }
```
Use `in_trash` rather than the older `archived` field — `2026-03-11` removes `archived`.

---

## 6. Working with Blocks (Page Body)

**Append children to a page**:
```bash
curl -X PATCH "https://api.notion.com/v1/blocks/<page_id>/children" "${NOTION_HEADERS[@]}" \
  -d '{
    "children": [
      { "object": "block", "type": "heading_3",
        "heading_3": { "rich_text": [{ "text": { "content": "Open questions" } }] } },
      { "object": "block", "type": "toggle",
        "toggle": {
          "rich_text": [{ "text": { "content": "Should we A/B test the new flow?" } }],
          "children": [
            { "object": "block", "type": "paragraph",
              "paragraph": { "rich_text": [{ "text": { "content": "Pro: data. Con: 2 weeks." } }] } }
          ]
        }
      }
    ]
  }'
```

**Common block types for PM artifacts**:

| Block | JSON `type` value | Use |
|---|---|---|
| Heading | `heading_1`, `heading_2`, `heading_3` | Sections |
| Paragraph | `paragraph` | Body text |
| Bulleted list | `bulleted_list_item` | Lists |
| Numbered list | `numbered_list_item` | Ordered lists |
| To-do | `to_do` (`checked: true/false`) | Action items |
| Callout | `callout` (with `icon`) | Notes, warnings, decisions |
| Toggle | `toggle` (with `children`) | Collapsible details |
| Code | `code` (`language: "javascript"`) | Code snippets |
| Quote | `quote` | Customer voice, pull-quotes |
| Divider | `divider` | Section separator |
| Bookmark | `bookmark` (`url: "..."`) | Rich link preview |
| Embed | `embed` (`url: "..."`) | Figma, Loom, etc. |
| Table | `table` + child `table_row` blocks | Tables |
| Synced block | `synced_block` | Reusable content |

**Read a block** (for fetching the page body):
```bash
curl -X GET "https://api.notion.com/v1/blocks/<block_id>" "${NOTION_HEADERS[@]}"
```

**List a page's children**:
```bash
curl -X GET "https://api.notion.com/v1/blocks/<page_id>/children?page_size=100" "${NOTION_HEADERS[@]}"
```

**Update a block**:
```bash
curl -X PATCH "https://api.notion.com/v1/blocks/<block_id>" "${NOTION_HEADERS[@]}" \
  -d '{ "to_do": { "checked": true } }'
```

**Delete (archive) a block**:
```bash
curl -X DELETE "https://api.notion.com/v1/blocks/<block_id>" "${NOTION_HEADERS[@]}"
```

---

## 7. Creating a Database

Databases can be created as children of an existing page. Use this sparingly; most workspaces should design DBs in the UI and then drive them programmatically.

```bash
curl -X POST "https://api.notion.com/v1/databases" "${NOTION_HEADERS[@]}" \
  -d '{
    "parent": { "type": "page_id", "page_id": "<parent_page_id>" },
    "title":  [{ "type": "text", "text": { "content": "Decisions" } }],
    "initial_data_source": {
      "properties": {
        "Title":   { "title": {} },
        "Status":  { "select": { "options": [
          { "name": "Proposed",   "color": "yellow" },
          { "name": "Approved",   "color": "green"  },
          { "name": "Superseded", "color": "gray"   }
        ]}},
        "Date":    { "date": {} },
        "Owner":   { "people": {} },
        "ID":      { "unique_id": { "prefix": "DEC" } }
      }
    }
  }'
```
On `2025-09-03` the schema goes under `initial_data_source.properties`. The response includes the new database's `data_sources[]` — store that `id` for later queries and page creation.

---

## 8. Rich Text Structure

Every text-bearing block uses a `rich_text` array. The minimal form:

```json
{ "text": { "content": "Hello" } }
```

With link:
```json
{ "text": { "content": "Linear", "link": { "url": "https://linear.app/..." } } }
```

With formatting:
```json
{
  "text": { "content": "important" },
  "annotations": {
    "bold": true, "italic": false, "code": false, "strikethrough": false, "underline": false,
    "color": "red"
  }
}
```

Mentions (a person):
```json
{ "mention": { "type": "user", "user": { "id": "<user_id>" } } }
```

Mentions (a page):
```json
{ "mention": { "type": "page", "page": { "id": "<page_id>" } } }
```

Mentions (a date):
```json
{ "mention": { "type": "date", "date": { "start": "2026-05-21" } } }
```

---

## 9. Sync Pattern Recipes

### Notion → Linear (create Project on PRD approval)

1. Webhook source: PRD status changes to Approved (handled by Zapier/Make/custom poller).
2. Read PRD properties via Notion API.
3. Look up Linear team ID and label IDs from cache.
4. Call Linear's `projectCreate` mutation (see `linear-expert/references/linear-graphql-patterns.md`).
5. Store the returned Linear Project URL in the PRD's `Linear Project` property via Notion PATCH.

### Linear → Notion (roll up project progress)

1. Scheduled job (nightly).
2. For each PRD with a non-null `Linear Project` URL: extract project ID; query Linear for project progress.
3. PATCH the PRD's `Linear Progress` number property and `Linear State` select property.

### GitHub → Notion (log ADR as a Decision)

1. GitHub Action on push to `main` matching `docs/adr/*.md`.
2. Parse the ADR front matter (title, status, date, drivers).
3. POST to Notion's pages endpoint with `parent: { "type": "data_source_id", "data_source_id": "<decisions_data_source_id>" }`.

---

## 10. Rate Limits and Resilience

- ~3 requests/second per integration, with short bursts permitted.
- On `429`, response includes `Retry-After` header (seconds). Honor it.
- For bulk writes, batch and sleep 300-500ms between calls.
- Wrap mutating calls in idempotency checks where possible (search by title before create).
- Cache data source IDs and schemas; refresh only when a 400 indicates a property mismatch.

## 11. Quick Reference

| Operation | Method | Endpoint |
|---|---|---|
| Get DB (→ `data_sources[].id`) | GET | `/v1/databases/{database_id}` |
| Query rows | POST | `/v1/data_sources/{data_source_id}/query` |
| Get property schema | GET | `/v1/data_sources/{data_source_id}` |
| Update property schema | PATCH | `/v1/data_sources/{data_source_id}` |
| Create DB | POST | `/v1/databases` (schema in `initial_data_source`) |
| Update DB title/icon/parent | PATCH | `/v1/databases/{database_id}` |
| Get page | GET | `/v1/pages/{id}` |
| Create page | POST | `/v1/pages` |
| Update page props | PATCH | `/v1/pages/{id}` |
| Get block | GET | `/v1/blocks/{id}` |
| List children | GET | `/v1/blocks/{id}/children` |
| Append children | PATCH | `/v1/blocks/{id}/children` |
| Update block | PATCH | `/v1/blocks/{id}` |
| Delete (archive) block | DELETE | `/v1/blocks/{id}` |
| List users | GET | `/v1/users` |
| Search | POST | `/v1/search` |

Endpoints above are for `Notion-Version: 2025-09-03` (as of September 2026). Full reference: https://developers.notion.com/reference/intro

## references/notion-database-design-for-pm.md

# Notion Database Design for PM

Canonical database schemas for a product team's Notion workspace. Each section gives:

- Properties (with types and purpose)
- Recommended views
- Key relations to other databases
- Optional formulas/rollups

Conventions:

- `title` is the page's name; every database has exactly one.
- Property names are Title Case.
- `unique_id` properties use a 3-letter prefix (PRD, OKR, DEC, etc.).
- All databases include system properties `Created time`, `Last edited time`, `Created by`, `Last edited by` (implicit).

---

## 1. PRDs Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "PRD: Self-Serve Signup" |
| ID | unique_id (prefix `PRD`) | PRD-001 |
| Status | status | Draft / In Review / Approved / In Build / Shipped / Killed |
| Owner | people | Driving PM (one) |
| Author | people | Original drafter |
| Reviewers | people | Engineering lead, Design lead, others |
| Priority | select | P0 / P1 / P2 / P3 |
| Target Date | date | Aspirational launch |
| Approved On | date | Set when status → Approved |
| Shipped On | date | Set when status → Shipped |
| Areas | multi_select | API / Web / Mobile / Infra / Data |
| Customer Segments | multi_select | SMB / Mid-Market / Enterprise |
| OKR | relation → OKRs | Which OKR(s) this serves |
| Roadmap Item | relation → Roadmap | Roadmap row this delivers |
| Decisions | relation → Decisions | Decision log entries spawned by this PRD |
| Linear Project | url | Live link |
| Jira Epic | url | If using Jira |
| Confidence | select | High / Medium / Low |
| Tech Lead | people | |
| Design Lead | people | |
| Last Reviewed | date | Updated on any quarterly review |
| Days Since Review | formula | `dateBetween(now(), prop("Last Reviewed"), "days")` |

**Recommended views**:
- **My PRDs** — filter: Owner is me; group by Status.
- **In Review** — filter: Status = In Review; sort by Target Date asc.
- **Approved / In Build** — filter: Status in (Approved, In Build); group by Owner.
- **Shipping This Quarter** — filter: Target Date in next 90 days, Status != Killed.
- **Stale (>90 days since review)** — filter: Days Since Review > 90.

---

## 2. OKRs Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "Increase activation rate" |
| ID | unique_id (prefix `OKR`) | OKR-014 |
| Type | select | Objective / Key Result |
| Parent Objective | relation (self) | KRs link to their Objective |
| Quarter | select | Q1 2026, Q2 2026, ... |
| Owner | people | Single accountable |
| Status | status | Not started / On track / At risk / Off track / Hit / Missed |
| Confidence | select | 10 / 7 / 5 / 3 (Wodtke) |
| Target | rich_text | "30% → 45%" |
| Current | rich_text | Updated weekly |
| Progress | number (percent) | Manual or formula from Current/Target if numeric |
| PRDs | relation → PRDs | Contributing PRDs |
| Initiatives | relation → Roadmap | Aggregated initiatives |
| Update Cadence | select | Weekly / Biweekly |
| Last Updated | date | Reflects the latest check-in |

**Rollup ideas**:
- PRDs Count: rollup PRDs relation, count.
- PRDs Shipped: rollup PRDs Status, count where = Shipped.

**Views**:
- **This Quarter by Objective** — group by Parent Objective, filter Quarter = current.
- **My OKRs** — filter: Owner is me.
- **At Risk / Off Track** — filter: Status in (At Risk, Off Track).
- **Confidence Distribution** — Board grouped by Confidence.

---

## 3. Roadmap Database

| Property | Type | Notes |
|---|---|---|
| Title | title | Initiative name |
| ID | unique_id (prefix `ROAD`) | ROAD-007 |
| Horizon | select | Now / Next / Later (or quarters) |
| Status | status | Discovery / Defining / Building / Shipped / Killed |
| Owner | people | Driving PM |
| Customer Outcome | rich_text | Outcome statement |
| OKR | relation → OKRs | What it rolls up to |
| PRDs | relation → PRDs | Underlying PRDs |
| Start | date | Range start |
| End | date | Range end |
| Confidence | select | High / Medium / Low |
| Audience | multi_select | Internal / Customer / Exec |
| Teams Involved | multi_select | Eng / Design / Data / Marketing / Sales |
| Dependencies | relation (self) | Other roadmap items this depends on |

**Rollups**:
- PRDs Count: rollup PRDs relation, count.
- All PRDs Shipped?: rollup PRDs Status, "show original" or "percent per group" to compute health.

**Views**:
- **Timeline (This Year)** — Timeline view; group by Horizon; date source Start/End.
- **Now/Next/Later Board** — Board grouped by Horizon.
- **Customer-Facing** — filter: Audience contains Customer.
- **Exec Read-Out** — filter: Status != Killed, sort by Horizon; show only Title, Customer Outcome, Status, Confidence, End.

---

## 4. Decisions (ADR) Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "Adopt Postgres over MySQL for analytics" |
| ID | unique_id (prefix `DEC`) | DEC-042 |
| Status | select | Proposed / Approved / Superseded / Reversed |
| Date | date | Decision date |
| DACI Driver | people | The Driver (per `daci-framework/`) |
| Approver | people | The Approver |
| Contributors | people | |
| Informed | people | |
| Context | rich_text | What forced the decision |
| Decision | rich_text | Chosen path (the headline) |
| Trade-offs | rich_text | What we accepted/rejected |
| Supersedes | relation (self) | If this overrides a prior decision |
| Superseded By | relation (self, reverse) | Auto via relation |
| Related PRDs | relation → PRDs | |
| Tags | multi_select | architecture / process / hiring / vendor / pricing |

**Page body template** (each row's content):
- Context
- Options Considered (toggle per option, with pros and cons)
- Decision
- Consequences
- Action Items (to-do blocks)
- Review Date (`@date`)

**Views**:
- **Recent** — sort by Date desc.
- **By Tag** — group by Tags.
- **Open Action Items** — filter: pages with unchecked to-do blocks (use Notion's filter on "Has content").

---

## 5. Sprint / Cycle Reviews Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "Sprint 23 Review" or "Cycle 47 Review" |
| Cycle Number | number | For sorting |
| Team | select | Engineering, Design, Data |
| Date | date | Review date |
| Velocity | number | Story points or issue count |
| Throughput | number | Issues completed |
| Cycle Time P50 | number | Days |
| Cycle Time P95 | number | Days |
| Health | select | Green / Yellow / Red |
| Demos | rich_text | What was shown |
| Outcomes | rich_text | What changed for users |
| Carryover | rich_text | What slipped |
| Retro Summary | rich_text | Liked / Learned / Lacked / Longed-for |
| Linked PRDs | relation → PRDs | PRDs touched this cycle |

**Views**:
- **Latest** — sort by Cycle Number desc; limit 1 per Team.
- **Health Over Time** — filter: Team = X; sort by Cycle Number; show Health.

---

## 6. Customer Research Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "Interview: Acme Inc CTO 2026-05-15" |
| ID | unique_id (prefix `RSCH`) | RSCH-128 |
| Type | select | Interview / Survey / Usability / Diary Study |
| Date | date | When |
| Segment | select | SMB / Mid-Market / Enterprise |
| Industry | multi_select | Fintech / Healthtech / E-commerce / SaaS / Other |
| Company | rich_text | |
| Role | rich_text | |
| Interviewer | people | |
| Recording | url | Loom / Zoom |
| Transcript | files | |
| Key Quotes | rich_text | |
| Pains | multi_select | Pre-categorized (cost / time / quality / learning curve) |
| Gains Sought | multi_select | Pre-categorized |
| Linked Opportunities | relation → Opportunities (if using `discovery/interview-synthesis/`) | |
| Linked PRDs | relation → PRDs | If informed a PRD |

**Views**:
- **By Segment** — group by Segment.
- **Recent** — sort by Date desc, limit 25.
- **By Pain** — group by Pains.

---

## 7. 1:1s Database

| Property | Type | Notes |
|---|---|---|
| Title | title | "Alice ↔ Bob — 2026-05-21" |
| Date | date | |
| Partners | people | Both attendees |
| Cadence | select | Weekly / Biweekly / Monthly |
| Agenda Items | rich_text | |
| Action Items | rich_text | |
| Health Check | select | Green / Yellow / Red |
| Topics | multi_select | Career / Project / Feedback / Personal |

**Views**:
- **My 1:1s This Week** — filter: Partners contains me, Date in this week.
- **By Partner** — group by Partners.

---

## 8. Relations Diagram (Conceptual)

```
OKRs ──┬── PRDs ── Decisions
       └── Roadmap ── PRDs
                     ├── Customer Research (informs)
                     └── Sprint Reviews (closes)
```

- OKRs ← PRDs (many-to-many): a PRD can serve multiple KRs; a KR can have multiple PRDs.
- Roadmap ← PRDs (many-to-many): one roadmap item often spans multiple PRDs.
- Decisions ↔ PRDs (many-to-many): decisions emerge from PRDs and shape future ones.
- Customer Research → PRDs (one-to-many): research entries inform specific PRDs.
- Sprint Reviews ← PRDs (many-to-many): a sprint touches multiple PRDs.

---

## 9. Permissions Model

| Database | Read | Comment | Edit |
|---|---|---|---|
| PRDs | All workspace | Product, Eng, Design | Owners and Reviewers |
| OKRs | All workspace | Product, Leadership | Owners |
| Roadmap | All workspace | Product, Leadership | Product team |
| Decisions | All workspace | All workspace | DACI Drivers |
| Sprint Reviews | All workspace | Team members | Team members |
| Customer Research | Product, Eng, Design | Product, Eng, Design | Research team + PMs |
| 1:1s | Participants only | Participants only | Participants only |

Set permissions at the database level; avoid per-row overrides.

---

## 10. Database Hygiene

- **Property audit**: quarterly, remove unused properties (zero non-empty rows in 90 days).
- **Option audit**: quarterly, merge underused select options.
- **Relation audit**: monthly, search for relations pointing to archived rows.
- **Ownership audit**: monthly, flag any row whose Owner has left the team.
- **Stale row audit**: quarterly, archive rows untouched in 180+ days unless explicitly kept.

## references/notion-pm-playbook.md

# Notion PM Playbook

> Read this when standing up or refactoring a Notion PM workspace: core concepts (hierarchy, property types, views, blocks), the seven core workflows (workspace setup, PRD/OKR/Roadmap/Decisions/Review DB design, linking, sync), inline API/query patterns, best practices, troubleshooting, and success criteria.

## Concepts

### Workspace Hierarchy

| Level | Purpose | Example |
|---|---|---|
| **Workspace** | Top-level account, billing scope, SCIM/SAML | "Acme Inc" |
| **Teamspace** | Permission boundary for a team or function | "Product", "Engineering" |
| **Page** | A document or container | "Onboarding wiki" |
| **Database** | Typed collection of pages (rows = pages with properties) | "PRDs DB", "OKRs DB" |
| **Database row** | A page whose parent is a database | "PRD: Self-Serve Signup" |
| **Linked Database** | A view of another database, embedded in a page | A "This Quarter" view of the PRDs DB |
| **Block** | A unit of content inside a page (paragraph, heading, callout, toggle, image, embed) | "Heading 2", "Callout", "Synced Block" |

### Property Types (the heart of database design)

| Type | Use | Notes |
|---|---|---|
| `title` | The row's name; every database has exactly one | Renders as the page title |
| `rich_text` | Long-form text | Supports markdown formatting |
| `select` | Single-value tag from a closed list | E.g. PRD status: Draft / Review / Approved / Shipped |
| `multi_select` | Multi-value tags | E.g. PRD area: API, Web, Mobile |
| `status` | Special select with three groups: To-do, In progress, Complete | First-class in views |
| `date` | Date or date range | Supports reminders |
| `people` | Reference to workspace member(s) | Owner, reviewer |
| `files` | Attached files or URLs | Specs, mocks |
| `checkbox` | Boolean | Approved? |
| `url`, `email`, `phone` | Typed contact data | Customer DB |
| `number` | Numeric with optional format (percent, currency) | Confidence, RICE score |
| `formula` | Computed from other properties | E.g. RICE = (R*I*C)/E |
| `relation` | Link to row(s) in another database | PRD → OKR, PRD → Roadmap Item |
| `rollup` | Aggregate property of related rows | "Sum of estimates from linked Linear issues" |
| `created_time`, `last_edited_time` | System | Always present |
| `created_by`, `last_edited_by` | System | Always present |
| `unique_id` | Auto-incremented short ID with prefix | E.g. PRD-001, DEC-042 |

### Views

Every database can present multiple views, each with its own filter, sort, group, and property visibility:

- **Table** — spreadsheet-like; default editing view
- **Board** — Kanban grouped by a select/status property; great for PRD status, OKR confidence
- **Timeline** — Gantt-like; great for Roadmaps when there is a date-range property
- **Calendar** — month view; great for launches, reviews, sprint ceremonies
- **Gallery** — card view with the cover image; great for customer research notes or design reviews
- **List** — minimal, dense; great for backlog-style browsing

### Notion-Compatible Markdown / Block Types

Notion is not strictly Markdown, but Markdown extensions are recognized in many contexts. Key blocks used in PM artifacts:

- Headings: `#`, `##`, `###`
- Callouts: `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]` (in Markdown imports; native block in UI)
- Toggle blocks: collapse-expand sections (great for "Open questions", "Out of scope")
- Synced blocks: a single block reused across pages (Definition of Done, glossary)
- Code blocks: fenced with language for syntax highlighting
- Linked databases: a view of another DB embedded inline
- Mentions: `@person`, `@page`, `@date`
- Bookmarks: a URL becomes a rich preview card
- Embeds: Figma, Loom, GitHub Gist, YouTube
- Math: `$equation$` inline; `$$equation$$` block

## Core Workflows

### 1. Workspace Setup for a Product Team

1. Create a Teamspace named `Product`.
2. Create the foundational databases as direct children of the Teamspace:
   - PRDs
   - OKRs (with quarter as a property)
   - Roadmap
   - Decisions
   - Customer Research
   - Sprint Reviews (or Cycle Reviews if on Linear)
   - 1:1s
3. Define the relations between them (see `references/notion-database-design-for-pm.md`).
4. Create a Teamspace home page with a curated set of linked database views.
5. Establish naming conventions; pin them in a "Team conventions" page.
6. Set permissions: full access for product team, edit for engineering, view for everyone else.
7. **HANDOFF TO**: PMs to start populating PRDs and OKRs.

### 2. PRD Database Design

A PRD is a row in the PRDs database. Properties:

| Property | Type | Purpose |
|---|---|---|
| `Title` | title | PRD name |
| `Status` | status | Draft / In Review / Approved / In Build / Shipped / Killed |
| `Owner` | people | Driving PM |
| `Author` | people | Original drafter |
| `Reviewers` | people | DRI, Eng lead, Design lead |
| `Target Date` | date | Aspirational launch |
| `Priority` | select | P0 / P1 / P2 / P3 |
| `OKR` | relation → OKRs | Which OKR(s) this serves |
| `Roadmap Item` | relation → Roadmap | Which roadmap item this delivers |
| `Linear Project` | url | Link to the Linear Project tracking the work |
| `Jira Epic` | url | If using Jira |
| `Tech Lead` | people | Engineering DRI |
| `Design Lead` | people | Design DRI |
| `Approved On` | date | Set when status → Approved |
| `Shipped On` | date | Set when status → Shipped |
| `Document` | (page body) | The PRD itself, with the template from `assets/notion-prd-template.md` |

Build views:
- **My PRDs** (filter: Owner is me)
- **In Review** (filter: Status = In Review; sort by Target Date)
- **This Quarter** (filter: Target Date in this quarter, group by Status)
- **All by Owner** (group by Owner, hide killed)

### 3. OKR Database Design

| Property | Type | Purpose |
|---|---|---|
| `Title` | title | KR or Objective name |
| `Type` | select | Objective / Key Result |
| `Parent Objective` | relation (self) | For KRs, link to parent Objective |
| `Quarter` | select | Q1 2026, Q2 2026, ... |
| `Owner` | people | Single accountable owner |
| `Status` | status | Not started / On track / At risk / Off track / Hit / Missed |
| `Confidence` | select | 10 / 7 / 5 / 3 (Wodtke scale) |
| `Target` | rich_text | The measurable target |
| `Current` | rich_text | Current value (updated weekly) |
| `Progress` | number (percent) | Manual or formula |
| `PRDs` | relation → PRDs | PRDs that contribute to this KR |
| `Notes` | rich_text | Context, blockers |

Views:
- **This Quarter by Objective** (group by Parent Objective)
- **My OKRs** (filter: Owner is me)
- **At Risk / Off Track** (filter on Status)

### 4. Roadmap Database Design

| Property | Type | Purpose |
|---|---|---|
| `Title` | title | Initiative name |
| `Horizon` | select | Now / Next / Later (or Q1 / Q2 / Q3 / Q4) |
| `Status` | status | Discovery / Defining / Building / Shipped / Killed |
| `Owner` | people | Driving PM |
| `Customer Outcome` | rich_text | Outcome statement |
| `OKR` | relation → OKRs | What this rolls up to |
| `PRDs` | relation → PRDs | Underlying PRDs |
| `Start` | date | Range start |
| `End` | date | Range end |
| `Confidence` | select | High / Medium / Low |
| `Audience` | multi_select | Internal / Customer / Exec |

Views:
- **Timeline** (grouped by Horizon, dates from Start/End)
- **Now/Next/Later Board** (grouped by Horizon)
- **Customer-Facing** (filter: Audience contains Customer)

### 5. Decisions (ADR-style) Database

| Property | Type | Purpose |
|---|---|---|
| `Title` | title | Decision name |
| `ID` | unique_id (prefix DEC) | Auto-numbered |
| `Status` | select | Proposed / Approved / Superseded / Reversed |
| `Date` | date | Decision date |
| `DACI Driver` | people | The Driver |
| `Approver` | people | The Approver |
| `Contributors` | people | Contributors |
| `Informed` | people | Informed parties |
| `Context` | rich_text | What forced the decision |
| `Options` | (page body) | Options considered with pros/cons |
| `Decision` | rich_text | Chosen path |
| `Supersedes` | relation (self) | If this overrides a prior decision |

### 6. Sprint / Cycle Review Database

| Property | Type | Purpose |
|---|---|---|
| `Title` | title | "Sprint 23 Review" or "Cycle 47 Review" |
| `Cycle Number` | number | For sorting |
| `Date` | date | Review date |
| `Team` | select | Engineering, Design, Data, ... |
| `Velocity` | number | Story points or issue count |
| `Health` | select | Green / Yellow / Red |
| `Demos` | rich_text | What was shown |
| `Outcomes` | rich_text | What changed for users |
| `Retro` | (page body) | Liked / Learned / Lacked / Longed-for |

### 7. Linking Strategy

Three layers of linking:

1. **Relations** for many-to-many DB joins (PRD ↔ OKR, PRD ↔ Roadmap).
2. **Mentions** for one-off references inside page bodies (`@PRD: Self-Serve Signup`).
3. **Sub-pages** only for hierarchical content that does not warrant a database (e.g. PRD has a child page "Open Questions").

Avoid: linking with raw markdown links to other Notion pages (loses bidirectionality and search relevance).

### 8. Sync Patterns

**Notion ↔ Jira**
- One-way: build a Zapier/Make/n8n job that, on PRD status change, creates the linked Jira Epic.
- Two-way (advanced): periodically diff PRD status and Jira Epic status; reconcile.
- Embed: paste a Jira issue URL; Notion renders a rich preview (read-only).

**Notion ↔ Linear**
- One-way: on PRD approval, create a Linear Project; store its URL in `Linear Project` property.
- Roll-up: a scheduled job queries Linear's GraphQL API for project progress and writes back to a Notion number property.
- Embed: paste a Linear issue/project URL for a rich preview.

**Notion ↔ GitHub**
- Embed: PR and Issue URLs render as rich previews.
- Custom: a webhook handler creates Decisions DB rows when an ADR is added to a repo.

See `references/notion-api-patterns.md` for the API calls these patterns use.

## API / Query Patterns

The Notion API is REST, served at `https://api.notion.com/v1/`. Auth is via integration tokens (`Authorization: Bearer secret_...`). Every request must include a `Notion-Version` header; these examples use `2025-09-03`, which splits each database into one or more **data sources** (as of September 2026; `2026-03-11` is the newest version). Rows are queried and created against the data source, so first resolve it: `GET /v1/databases/<db_id>` returns `data_sources[].id`. See `references/notion-api-patterns.md` for the full library and the version-change table.

**Query a database** (find all PRDs in review — via its data source):
```bash
curl -X POST https://api.notion.com/v1/data_sources/<data_source_id>/query \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
  -d '{
    "filter": {
      "property": "Status",
      "status": { "equals": "In Review" }
    },
    "sorts": [{ "property": "Target Date", "direction": "ascending" }]
  }'
```

**Create a page in a database** (new PRD):
```bash
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
  -d '{
    "parent": { "type": "data_source_id", "data_source_id": "<prd_data_source_id>" },
    "properties": {
      "Title":   { "title":  [{ "text": { "content": "PRD: Self-Serve Signup" } }] },
      "Status":  { "status": { "name": "Draft" } },
      "Owner":   { "people": [{ "id": "<user_id>" }] },
      "Target Date": { "date": { "start": "2026-09-30" } }
    },
    "children": [
      { "object": "block", "type": "heading_2",
        "heading_2": { "rich_text": [{ "text": { "content": "Problem" } }] } },
      { "object": "block", "type": "paragraph",
        "paragraph": { "rich_text": [{ "text": { "content": "..." } }] } }
    ]
  }'
```

**Update a page property** (mark PRD approved):
```bash
curl -X PATCH https://api.notion.com/v1/pages/<page_id> \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
  -d '{
    "properties": {
      "Status":      { "status": { "name": "Approved" } },
      "Approved On": { "date":   { "start": "2026-05-21" } }
    }
  }'
```

**Append blocks to a page** (add a section):
```bash
curl -X PATCH https://api.notion.com/v1/blocks/<page_id>/children \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
  -d '{
    "children": [
      { "object": "block", "type": "callout",
        "callout": {
          "icon":     { "type": "emoji", "emoji": "ℹ" },
          "rich_text": [{ "text": { "content": "Approved by Product Council on 2026-05-21." } }]
        }
      }
    ]
  }'
```

**Paginate through a large database** (handle `has_more`):
```bash
# Pass `start_cursor` from the previous response on each subsequent call
curl -X POST https://api.notion.com/v1/data_sources/<data_source_id>/query \
  -d '{ "page_size": 100, "start_cursor": "<cursor>" }'
```

**Compound filter** (PRDs owned by me and in review):
```json
{
  "filter": {
    "and": [
      { "property": "Owner",  "people": { "contains": "<user_id>" } },
      { "property": "Status", "status": { "equals": "In Review" } }
    ]
  }
}
```

### Rate Limits

Notion rate-limits at ~3 requests/second per integration with bursts permitted. On `429`, honor the `Retry-After` header. For bulk operations, batch and add 300-500ms sleep between writes.

## Best Practices

**Database design**
- Decide property types up front; changing a property type later can be lossy.
- Prefer `select` and `status` over free-text where values are constrained; this enables filters and Boards.
- Use `relation` for any many-to-many link between artifact types; do not paste page URLs into rich_text.
- Use `unique_id` for any artifact you want to reference externally (PRD-042, DEC-017).

**Views over duplication**
- Never copy a database row to display it elsewhere; embed a Linked Database View instead.
- Each page should have at most one source-of-truth database; everything else is a view.

**Page architecture**
- Teamspace home page = a curated dashboard of linked views; not a content dumping ground.
- Use synced blocks for content reused across many pages (e.g. Definition of Done).
- Cap page nesting at 3 levels for navigability.

**Governance**
- Every active page in a database must have an Owner and a `Last Reviewed` date.
- Quarterly review: archive Shipped/Killed PRDs older than 12 months.
- Permissions at the Teamspace level whenever possible; avoid per-page overrides.

**API hygiene**
- Cache database IDs, data source IDs, property IDs, and user IDs.
- Always set `Notion-Version` header explicitly to avoid silent breaks.
- Use webhooks (via Notion's official webhooks where available, or Zapier/Make as fallback) instead of polling.

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---|---|---|
| API returns 404 for a database the integration "should" see | Integration has not been explicitly shared on the database (or its parent page) | Open the database in Notion, click "..." → "Add connections" → select the integration |
| Rollup property shows nothing | The relation property is empty, or the rolled-up property is filtered out | Confirm the relation has linked rows; check the rollup's source property; rebuild the rollup if added recently |
| Status property cannot be set via API | The status name does not exactly match an existing option (case-sensitive) | Read the database schema first; use the exact option name; status options cannot be created via the API in some plan tiers |
| Linked database view loses its filter after edit | The view was edited in a destination page rather than at the source | Edit views at the database's source location; saved views from the source propagate everywhere |
| Page becomes very slow to load | Too many embedded videos, too many rollup calculations, or a deeply nested toggle structure | Move heavy content to a child page; replace rollups with formula caches where possible; flatten toggles |
| Workspace search returns irrelevant results | Pages share generic titles ("Notes"), or are missing tags | Use descriptive titles with a prefix (PRD:, DEC:, OKR:); add multi_select tags |
| Bulk import of Markdown loses callouts and toggles | Notion's Markdown import does not preserve all custom block types | Use the API to create blocks programmatically (block-by-block) for high-fidelity migration |

## Success Criteria

- Every PM artifact (PRD, OKR, Decision, Roadmap item) lives in a database, not as an ad-hoc page
- 90%+ of database rows have an Owner and a Last Reviewed date within the past 6 months
- The Teamspace home page is the single launching point for the team's daily work
- New team members can find an active PRD in under 3 clicks from the home page
- API integrations (Linear sync, Jira sync, GitHub webhooks) run nightly with zero manual reconciliation
- No more than 5% of database rows reference deleted or archived counterparts (relation hygiene)
- Quarterly OKR check-ins are recorded in the OKR database with updated Confidence and Progress
- Decision log captures 100% of architecture-level decisions across the team

## references/red-flags.md

# Red Flags: Notion PM

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every Notion database design, relation, or API integration before adopting it for PM workflows. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Page Sprawl

**Symptom.** PM workspace has 2,400 top-level pages, no consistent hierarchy. New PMs create pages in their personal space; nobody can find anything.
**Why it's bad.** Page sprawl makes Notion functionally a graveyard. Search returns 20 versions of the same PRD. The "shared knowledge" promise of Notion is broken because there is no shared structure.
**Bad example:**
> "Top-level workspace: 2400 pages, no folder structure. PRD-2026-Q1, PRD-2026-Q1-v2, PRD-2026-Q1-final, PRD-2026-Q1-final-v2 all exist."
**Good example:**
> "Workspace hierarchy:
> - PRDs database (one entry per PRD; versions tracked as a property + history)
> - OKRs database
> - Roadmap database
> - Decisions database
> - Meeting notes database
> Pages outside databases require a documented exception. Personal pages live in `/personal`."
**How to catch it.** Workspace has > 100 top-level pages without database membership = enforce DB-driven structure.

---

## Red Flag 2: Missing Relations

**Symptom.** PRDs database, OKRs database, and Roadmap database all exist -- but no relations between them. Each PRD lists its OKR as plain text.
**Why it's bad.** Plain-text references break. A PRD references "Q2 OKR: Activation" but the OKR's wording shifted; the PRD is now misleading. Worse, you cannot generate "all PRDs supporting this OKR" -- a basic PM query.
**Bad example:**
> "PRD page property `OKR`: text = 'Q2 Activation OKR'. (No link.)"
**Good example:**
> "PRD database has a Relation property `OKR` -> OKRs database. Two-way relation: each OKR shows its supporting PRDs. Rollup: OKR shows count of in-progress vs done PRDs."
**How to catch it.** Any cross-database reference stored as text = convert to a Relation.

---

## Red Flag 3: Rollup-of-Rollup Performance Collapse

**Symptom.** OKR DB has a rollup of Project DB (which has a rollup of Task DB). Page load > 10 seconds.
**Why it's bad.** Notion rollups across multiple databases recompute on every page render. Deep rollup chains (3+ levels) make the page sluggish; teams stop using the dashboards because they hang.
**Bad example:**
> "OKRs DB rollup: 'completed task count' = rollup of Projects.rollup of Tasks.is-done. Page takes 12s to render."
**Good example:**
> "Rollups are 1-deep. For aggregations needing more depth, a scheduled script (running daily via cron) updates an explicit 'aggregate-stats' property using the Notion API. Page renders in < 1s."
**How to catch it.** Notion page > 3s render time + uses rollups = re-architect to flat aggregations or scripted updates.

---

## Red Flag 4: Inline Databases Everywhere

**Symptom.** Every PM has their own inline database in their meeting notes, all duplicating fields with slight variations.
**Why it's bad.** Inline databases are isolated copies. Search does not aggregate them. Reporting is impossible. Renaming a property in one does not propagate. It is the worst of both worlds: database overhead with none of the benefits.
**Bad example:**
> "Each PM's weekly meeting notes contain an inline 'Action Items' DB. The org cannot generate 'all action items assigned to <name> across teams'."
**Good example:**
> "Single workspace-wide 'Action Items' DB. PM meeting notes embed a *filtered view* of this DB (filter: 'meeting = this page'). All action items live in one place; cross-team queries work."
**How to catch it.** Count databases named the same thing (e.g. 'Action Items' x 14) = consolidate.

---

## Red Flag 5: Notion Used as a Wiki Without Owners

**Symptom.** Pages exist with no owner, no last-reviewed date, no expiry. Half are 18 months stale.
**Why it's bad.** Stale pages mislead. New joiners trust the page; the team has long since changed practice. Documentation drift is a real cost; the right antidote is page-level ownership + review cadence.
**Bad example:**
> "Onboarding page 'How to deploy to staging': last edited 2024-08. Says to use AWS CodeBuild; team migrated to GitHub Actions in 2025."
**Good example:**
> "Every long-lived page has: `Owner` property (user), `Last Reviewed` (date), `Review Cadence` (every N months), `Expires` (date). A weekly script lists pages overdue for review; owners review or archive."
**How to catch it.** Workspace has pages with no Last Reviewed property or with Last Reviewed > 1 year ago = run the review script.

---

## Red Flag 6: API Tokens in Pages

**Symptom.** A page titled 'Notion API credentials' contains `secret_xxxxxxxx`.
**Why it's bad.** Notion pages are not secret stores. Anyone with workspace access (often a wide group) can read the secret. Worse, Notion's audit log of page views is limited, so leaks may go undetected.
**Bad example:**
> "Page 'Engineering / Tools / Notion API' contains the workspace integration secret in plain text."
**Good example:**
> "Secrets live in a secrets manager (1Password, AWS Secrets Manager, Vault). The Notion page references *how to retrieve* the secret (with the right permissions) but never contains the secret itself."
**How to catch it.** Search Notion for strings starting with `secret_`, `sk_`, `xoxb-`, `ghp_`, `xoxp-` = remove and rotate.

---

## Red Flag 7: Notion API Pagination Ignored

**Symptom.** Script fetches database entries via `POST /v1/data_sources/{data_source_id}/query` (or the pre-`2025-09-03` `POST /v1/databases/{id}/query`); returns 100 results; treats it as 'all results'.
**Why it's bad.** Notion API paginates at 100 items by default. Without honoring `has_more` + `next_cursor`, scripts silently miss data. The org thinks it has 100 PRDs; in reality there are 340 -- and decisions get made on a 30% sample.
**Bad example:**
> "response = requests.post(url, json={...}).json()
> all_results = response['results']  # treats 100 as all"
**Good example:**
> "all_results = []
> next_cursor = None
> while True:
>     body = {'page_size': 100}
>     if next_cursor:
>         body['start_cursor'] = next_cursor
>     r = requests.post(url, json=body).json()
>     all_results.extend(r['results'])
>     if not r.get('has_more'):
>         break
>     next_cursor = r['next_cursor']"
**How to catch it.** Any Notion API call that does not loop on `has_more` = broken.

---

## Red Flag 8: Synced Blocks Used as a Sharing Mechanism

**Symptom.** A team uses Synced Blocks to share a "current OKR" across 14 team-pages; updating the OKR requires editing the block in 14 places.
**Why it's bad.** Synced Blocks are tracking blocks across pages, but they do not survive page restructuring well and break in unpredictable ways. They are a workaround for missing database views, not a sharing mechanism.
**Bad example:**
> "Synced block 'Q2 OKRs' embedded in 14 team-pages. Editing the OKR requires opening each page to confirm sync."
**Good example:**
> "Q2 OKRs live in the OKRs database. Each team page embeds a *filtered view* of the OKRs DB (filter: 'team = this team'). Editing the OKR updates everywhere automatically."
**How to catch it.** > 3 instances of the same Synced Block = replace with a DB view.

---

## Red Flag 9: Permissions Set Per-Page Manually

**Symptom.** Each PRD page has hand-edited permissions. The CTO has access to 12 of 18 PRDs; nobody knows why the other 6 are different.
**Why it's bad.** Per-page permission editing does not scale and creates security drift. Someone leaves; their access is forgotten. New joiners get inconsistent visibility.
**Bad example:**
> "PRD pages with hand-edited permissions. Engineering Director has visibility into ~70% of PRDs; the rest 'must have been missed at setup'."
**Good example:**
> "Permissions inherit from the PRDs database. Database access groups are defined per role (PM full edit; Engineering read; Sales-Leadership read-only on customer-facing PRDs only). New pages inherit; per-page overrides require a documented exception."
**How to catch it.** Any page with permissions different from its parent DB = audit; standardize via inheritance.

---

## Red Flag 10: PRDs as Free-Form Pages, Not DB Entries

**Symptom.** Each PRD is a Notion page in a hand-crafted folder; some have status; some do not; no consistent properties.
**Why it's bad.** Without DB structure, you cannot query "which PRDs are blocked", "which are awaiting design review", "average days from draft to approved". The PRDs database is the org's pipeline; free-form pages destroy it.
**Bad example:**
> "PRD folder contains 47 pages, each with its own ad-hoc top section. Some have Status, some have Owner, some neither."
**Good example:**
> "PRDs database with required properties: Status (Draft / In Review / Approved / Shipped / Archived), Owner (user), Squad (relation), Target Quarter (select), OKR (relation), Last Updated (auto), Pre-mortem complete (checkbox). Page body uses a Template with the 8-section PRD structure. New PRDs must use the Template; the body sections cannot be skipped."
**How to catch it.** PRD pages outside the PRDs DB = migrate.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Page sprawl | > 100 top-level pages outside DBs = restructure |
| 2 | Missing relations | Cross-DB references stored as text = convert |
| 3 | Rollup-of-rollup performance | Render time > 3s = re-architect |
| 4 | Inline databases everywhere | Duplicate-named DBs > 5 = consolidate |
| 5 | No page owners / cadence | Pages without Last Reviewed = run audit |
| 6 | API tokens in pages | Search for `secret_*` = remove & rotate |
| 7 | Pagination ignored | API calls loop on `has_more`? |
| 8 | Synced Blocks as sharing | > 3 copies of same block = replace with DB view |
| 9 | Per-page permissions | Page perms differ from parent DB = audit |
| 10 | PRDs as free-form pages | PRDs outside PRDs DB = migrate |

## Related Reading

- `SKILL.md` -- Notion DB-driven PM patterns
- `references/notion-api-patterns.md` -- the API recipes
- `references/db-schemas.md` -- canonical PRD / OKR / Roadmap / Decision schemas
- Sibling skill: `confluence-expert/` -- the Atlassian-side equivalent
- Sibling skill: `jira-expert/` -- ticket data that feeds Notion dashboards
- Sibling skill: `execution/create-prd/` -- the PRD content that lives in the DB
- Sibling skill: `senior-pm/` -- portfolio + stakeholder dashboards in Notion

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/notion-pm
