---
description: "Writes QA cases from a feature spec across happy, edge, error, empty, concurrent, accessibility and security paths, then audits coverage. Use when planning QA for a feature, or finding coverage gaps after an incident."
---

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Test Scenarios

The agent writes the scenarios from the spec; `test_scenario_generator.py` then audits the list by counting scenarios per category against what the feature type needs. The script generates nothing despite its name.

**Done looks like:** every user goal has a happy path; each input has boundary and weird-but-valid cases; each failure mode has a user-visible outcome; empty states, accessibility and security are covered for every UI feature; concurrency for anything shared or financial; localization when more than one locale ships; at least one P0; the audit exits 0.

## When to Use

- After PRD approval and before implementation, or when sizing test effort in sprint planning
- Reviewing whether a test plan or a PR's tests cover enough
- Bug-bash preparation, or after a production incident to find the missed category

## Categories

Happy path, edge, error, empty state, concurrent, accessibility (`a11y`), security; plus performance, localization and cross-platform when they apply. Examples per category: `references/scenario-categories.md`.

## Clarify First

Before generating scenarios, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Feature type:** form, browse/list, real-time/collab, file upload, payment, or bulk operation (drives the scenario count per category in the coverage rubric).
- **Risk / sensitivity profile:** auth, payment, or PII involved (scales up security and concurrency coverage in the risk-weighted selection).
- **The spec's inputs, outputs, and side effects:** what users provide, expect, and what changes in the system (drives edge cases in Step 3 and error handling in Step 4).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

```bash
# Signup form with full coverage: exit 0
python3 scripts/test_scenario_generator.py \
  --input assets/sample_scenarios.json --format markdown
```

```bash
# Payment step with no error or security scenarios and a mistyped category: exit 1
python3 scripts/test_scenario_generator.py \
  --input assets/sample_scenarios_flawed.json --format markdown
```

```bash
# Input schema and flags
python3 scripts/test_scenario_generator.py --help
```

## Tools Overview

`test_scenario_generator.py` is the quality gate for this skill. **What the audit checks:** scenario counts per category against the feature type's recommended range (fail when happy path, edge, error or security has none; warn when below range; info when above); unknown category names; concurrency for collaborative features; localization when several locales are supported; cross-platform coverage; at least one P0. It counts; it does not judge whether a scenario is any good.

**Exit codes:** `0` no fail findings · `1` at least one fail (a core category with zero scenarios) · `2` unreadable file, invalid JSON or a top level that is not an object. JSON by default, `--format markdown`, `--output FILE`.

## Workflow

1. **Read the spec** for user goals, inputs, outputs and side effects.
2. **Write scenarios per category.** You know the standard techniques (boundaries, wrong types, 4xx/5xx/timeouts, keyboard and screen reader, authorisation and injection); spend the effort on what is specific to this feature: its side effects, its shared state, its money or PII. Payment and collaboration features need concurrency and idempotency cases; uploads need file-abuse cases.
3. **Weight by risk.** Always cover happy paths and empty states; cover edge cases by likelihood x severity; scale security with sensitivity. Mark P0 the scenarios whose failure would stop the release.
4. **Audit.** Write the list as JSON (schema in `--help`; `assets/sample_scenarios.json`) and run the audit. It must pass with no fail findings; then verify that each under-covered category is either filled or consciously out of scope. Recommended counts per feature type are in the appendix of `references/scenario-categories.md`.
5. **Hand to QA** with the automated/manual split from the same appendix.

## Anti-Patterns

### Only happy paths
**Mistake:** The plan tests that the feature works when everything goes right.
**Why it happens:** Happy paths come straight from the spec; failures have to be imagined.
**Instead:** Write at least the recommended error and edge counts for the feature type before anything else is added.

### "QA will figure it out"
**Mistake:** Scenarios are left to QA after the build.
**Why it happens:** Scenario writing feels like QA's job.
**Instead:** Write them before implementation; QA tests what is specified, and engineers build for cases they can see.

### No concurrency for shared or financial state
**Mistake:** A payment or collaborative feature ships with no race or idempotency scenarios.
**Why it happens:** Concurrency bugs do not show up in single-user demos.
**Instead:** Cover double-submit, simultaneous edit and retry-after-timeout explicitly.

More gaps with fixes: `references/coverage-anti-patterns.md`.

## Scope & Limitations

**In Scope:**
- Test scenarios across seven categories: happy path, edge, error, empty state, concurrent, accessibility and security, plus performance, localization and cross-platform where they apply
- Scenario counts per category by feature type: form, browse, real-time, upload, payment and bulk (table in the reference appendix, matching the script)
- Risk-weighted selection and a default split between manual and automated testing per scenario type
- A coverage audit that flags under-covered categories for the feature type (`test_scenario_generator.py`)
- Test-plan audits and post-incident scenario gap analysis

**Out of Scope:**
- Writing the PRD or acceptance criteria the scenarios come from (see `project-management/execution/create-prd/` and `project-management/execution/wwas/`)
- Implementing automated tests (see `engineering/senior-qa/` and `engineering/playwright-pro/`)
- A full WCAG accessibility audit (see `engineering/a11y-audit/`)
- Security testing and penetration work (see `engineering/security-audit/`)

**Important Caveats:**
- Despite its name, `test_scenario_generator.py` does not write scenarios. It audits a hand-written JSON list and counts scenarios per category.
- The tool checks coverage by count, not scenario quality. A category can pass with weak scenarios.
- The per-category counts are starting defaults. The team adjusts them for the risk profile of the feature.
- The team decides which scenarios to automate and which edge cases matter enough to test.

## Files

| File | Purpose |
|------|---------|
| `scripts/test_scenario_generator.py` | Coverage audit by category (it does not generate scenarios) |
| `assets/sample_scenarios.json` | Signup form, 19 scenarios; exits 0 |
| `assets/sample_scenarios_flawed.json` | Under-covered payment step; exits 1 |
| `assets/scenario_template.md` | Scenario template |

## Reference Documentation

- [references/scenario-categories.md](references/scenario-categories.md): Categories with examples; appendix with recommended counts and manual vs automated
- [references/coverage-anti-patterns.md](references/coverage-anti-patterns.md): Common gaps and fixes

## Related skills

- `project-management/execution/create-prd` — upstream spec
- `project-management/execution/wwas` — acceptance criteria
- `engineering/senior-qa` — implementation
- `engineering/code-reviewer` — review coverage
- `product-team/spec-to-repo` — translating spec to tickets

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/coverage-anti-patterns.md

# Coverage Anti-Patterns + Fixes

## A1 — Only happy paths
**Symptom:** Test plan = "user signs up, user logs in, user does X."

**Fix:** For each happy path, generate 4-8 edge cases, 3-5 errors,
empty state. Most production bugs come from non-happy paths.

## A2 — No empty / first-use state
**Symptom:** Dashboard tested with 50 demo projects; empty state never tested.

**Fix:** Always test the first-use experience. It's the first impression.

## A3 — Errors tested in isolation
**Symptom:** "5xx returns error message" — but never tested what user does after.

**Fix:** Each error scenario must include:
- Message displayed
- Suggested action
- Recovery path (retry / cancel / report)
- No corrupt state

## A4 — Concurrent skipped for collab features
**Symptom:** Real-time editing tested only single-user.

**Fix:** Test 2-user scenarios as table stakes for any collaborative
feature. Race conditions ship otherwise.

## A5 — Accessibility tested last (or never)
**Symptom:** "We'll add a11y in v2."

**Fix:** Baseline a11y on every feature:
- Keyboard navigation
- Screen reader pass
- Color contrast
- Touch targets

Automated tools (axe-core) cover 30%; manual covers the rest.

## A6 — Security tested only at end
**Symptom:** "Pen test before launch."

**Fix:** Security scenarios per feature:
- Auth
- Permissions
- Injection
- Sensitive data handling

Tested incrementally; pen test confirms at end.

## A7 — Performance tested only with synthetic data
**Symptom:** Load test with 100 records; production has 10M.

**Fix:** Test with production-like data volumes (or close).

## A8 — Cross-platform: only Chrome
**Symptom:** Tested only in Chrome dev machine.

**Fix:** Per supported browser + OS + device tier matrix.

## A9 — Localization: only English tested
**Symptom:** English looks fine; German breaks UI; Arabic backwards.

**Fix:** Pseudo-localization in CI (long-string, RTL); manual spot-check on shipped locales.

## A10 — "QA will catch it"
**Symptom:** Engineer / PM doesn't generate scenarios; relies on QA.

**Fix:** Scenarios are designed before code, not after. QA implements
tests; PM defines what to test.

## A11 — Same scenarios per feature regardless of risk
**Symptom:** Login feature gets same 5 scenarios as a help-text update.

**Fix:** Risk-weight scenario count:
- Auth / payment / data-integrity: heavy scenarios
- UI text: light scenarios

## A12 — Scenarios written; never reviewed
**Symptom:** Scenario list created; sits in a doc; not used.

**Fix:** Scenarios reviewed at:
- Sprint planning (sizing)
- Code review (verify coverage)
- QA planning (test pass)
- Production incidents (gap analysis)

## Worked example — signup feature

### Weak coverage

- User signs up successfully
- Form shows error on invalid email

### Strong coverage

**Happy path (3):**
1. User signs up with email + password → account created
2. User signs up with Google SSO → account created
3. User signs up via invite link → joins existing org

**Edge cases (8):**
1. Empty email → "Email required"
2. Email = "a" (invalid format) → "Invalid email format"
3. Email 257+ chars → "Email too long"
4. Password 7 chars (below min 8) → "Password too short"
5. Password 501+ chars (above max) → "Password too long"
6. Password no uppercase / digit / special → "Password must include..."
7. Email with emoji → handled (accept) or rejected (consistent)
8. Email matches existing → "Already registered. Sign in?"

**Error handling (5):**
1. Submit offline → "Connection lost"; form preserves input
2. Server 500 → "Something went wrong" (not stack trace)
3. Rate limited (10+ attempts) → "Too many attempts"; cool-down
4. SSO failure → fallback to email; partial state cleaned
5. Verification email fails to send → user sees "Resend"

**Empty / first-use (2):**
1. After signup → land on onboarding (not blank dashboard)
2. After email verification → land in product (not stuck on verification page)

**Concurrent (2):**
1. Same email signs up twice in parallel → only one account created
2. User submits twice quickly → idempotent (no duplicate)

**Accessibility (4):**
1. Tab through form → focus visible; logical order
2. Screen reader → labels read correctly
3. Submit with keyboard (Enter) → works
4. Error messages → associated with field via aria-describedby

**Security (5):**
1. Password not in URL / logs
2. Password hashed before storage (verify in DB)
3. SQL injection in email → sanitized
4. XSS in email field → escaped on display
5. Rate limit prevents brute force

**Performance (1):**
1. Signup endpoint < 500ms P95 under 1000 concurrent

**Cross-platform (3):**
1. iOS Safari → autofill works
2. Android Chrome → password manager integration
3. Older browsers (Safari 14) → graceful degradation

**Total: 33 scenarios vs original 2.**

The original missed:
- All edge cases
- Most errors
- Empty state
- Concurrent
- A11y entirely
- Security entirely
- Cross-platform

## Coverage gap analysis

For an existing feature's scenario list:

| Category | Recommended | Actual | Gap |
|----------|-------------|--------|-----|
| Happy | 1-3 | | |
| Edge | 4-8 | | |
| Error | 4-6 | | |
| Empty | 1-2 | | |
| Concurrent | varies | | |
| A11y | 3-4 baseline | | |
| Security | 3+ | | |

Highlight rows with gaps. Score by importance.

## Coverage discipline checklist

For each feature before code:

- [ ] PRD / spec reviewed
- [ ] User goals identified
- [ ] Inputs + outputs enumerated
- [ ] Happy paths defined (1-3)
- [ ] Edge cases per input (5+)
- [ ] Error handling for each failure mode
- [ ] Empty / first-use state covered
- [ ] Concurrent considered (if collab)
- [ ] Accessibility baseline covered
- [ ] Security considered (per feature sensitivity)
- [ ] Performance considered (per feature sensitivity)
- [ ] Localization considered (if i18n)
- [ ] Cross-platform considered (per supported)
- [ ] Priorities assigned (P0/P1/P2)
- [ ] Coverage reviewed at sprint planning

## references/scenario-categories.md

# Test Scenario Categories — Deep Reference

## 1. Happy paths

The primary user flow, no errors, no surprises.

### Patterns
- User completes the main task successfully
- All required fields filled correctly
- Default settings used
- Standard network conditions

### Examples (signup form)
- User enters valid email + password, clicks signup → account created, verification email sent
- User clicks Google SSO → authenticated, account created
- User signs up via invite link → joins existing org

### How many
- 1-3 per feature, covering the most common user paths

### What to verify
- Final state correct
- User sees confirmation
- System state updated
- Side effects (emails, webhooks) triggered

## 2. Edge cases

Boundary conditions and unusual inputs.

### Patterns
- Empty input where optional allowed
- Minimum value
- Maximum value
- Just below min / just above max
- Wrong data type
- Very long string
- Special characters / Unicode / emoji
- Whitespace-only
- SQL-injection-like input (verify sanitization)
- Combining edge cases (long + special)

### Examples (signup form)
- Empty email
- Email = "a@b" (technically valid?)
- Email 256 chars long
- Password = 1 char (below min)
- Password = 500 chars (above max)
- Password with no special character (if required)
- Email with emoji ("test💎@example.com")
- Email with Unicode ("test@例え.テスト")
- Email matching existing account
- Password = email (security check)

### How many
- 4-8 per input field; cluster related cases

## 3. Error handling

What the user experiences when things fail.

### Failure modes
- Network failure (offline, slow)
- Server error (500, 502, 504)
- Validation error (400, 422)
- Rate limited (429)
- Auth expired (401)
- Permission denied (403)
- Resource not found (404)
- Conflict (409 — concurrent modification)
- Timeout (request, response, idle)

### What to verify per error
- User sees clear message
- Specific suggested action (retry, contact support)
- No corrupt state left behind
- Logged for debugging
- Doesn't leak sensitive info in error
- Recoverable: user can try again
- Errors don't loop infinitely

### Examples (signup form)
- Submit while offline → "Connection lost. Try again."
- Submit during 500 → "Something went wrong. We've been notified." (not "500 Internal Server Error")
- Submit with duplicate email → "Email already in use. Sign in?"
- Slow network → loading state visible; cancellable

## 4. Empty / first-use / after-action states

Often the worst-tested category. Important because:
- First-use is the first impression
- Empty state is when user is most confused

### Patterns
- First use (no data)
- After deleting last item
- After error left partial state
- After cancel
- After signing out
- After timeout
- Filtered to no results

### What to verify
- Friendly message (not "no data")
- Primary action affordance
- Visual hierarchy guides next step
- Doesn't look broken

### Examples
- Empty dashboard (no projects yet) → "Create your first project" with prominent CTA
- After deleting last item → return to friendly empty state, not error
- Filter returns 0 results → "No matches. Clear filters?"

## 5. Concurrent / race scenarios

Critical for collaborative or data-integrity-sensitive features.

### Patterns
- Two users editing same record
- Two users triggering same action
- Race on resource (last seat in cart, etc.)
- Stale data submitted
- Optimistic locking
- Two API calls in flight; results out of order

### What to verify
- Consistent end state
- Clear conflict resolution UX
- No data loss
- No double-effect (idempotency)

### Examples (collaborative doc editing)
- Two users typing in same paragraph
- One user edits while another deletes the section
- User A saves stale version after User B's edit

### Testing approach
Often hard to automate; combination of:
- Targeted integration tests
- Manual scenarios
- Chaos / fuzz testing
- Production canary observation

## 6. Accessibility

Not optional. Compliance + ethics + actual users.

### Patterns
- Keyboard-only navigation (no mouse)
- Screen reader (VoiceOver / NVDA / JAWS)
- High contrast mode
- Reduced motion preference
- Text resize to 200%+
- Voice control
- Switch control

### What to verify
- All interactive elements keyboard-reachable
- Logical tab order
- Visible focus indicators
- Screen reader reads meaningful labels
- Color isn't the only signal (icon + text)
- Touch targets ≥ 44x44pt (mobile)
- Forms label associations correct
- ARIA roles used appropriately (not over-applied)

### Common gaps
- Modal traps focus → keyboard users stuck
- Carousel auto-advances → screen reader stuck
- Color-only validation states → invisible to color-blind
- Custom checkboxes without ARIA → broken for screen reader

## 7. Security + privacy

Scale with sensitivity of data + actions.

### Auth scenarios
- Logged out user accesses (should redirect / reject)
- Logged in but wrong permission
- Session expired during action
- CSRF (form not from your origin)
- Re-auth required for sensitive action

### Permission scenarios
- Role downgrade mid-session
- Permission denied at API but allowed by UI (or vice versa)
- Multi-tenant isolation (data leak across orgs)

### Data scenarios
- PII in error messages (shouldn't be)
- PII in logs (shouldn't be)
- PII in URLs (should be in POST body)
- Sensitive data displayed when not needed

### Injection scenarios
- SQL injection
- XSS (script in input rendered as HTML)
- Command injection
- Path traversal
- LDAP / NoSQL injection where applicable

### Rate limiting
- Brute-force on auth
- Spam on creation endpoints
- Throttle on expensive operations

## 8. Performance scenarios

For performance-sensitive features.

### Patterns
- Cold load (first time, no cache)
- Warm load (cached)
- Large data volume (1000+ items, 1M+ items)
- Slow network (3G simulation)
- Slow device (mid-tier mobile)
- Concurrent users (10, 100, 1000)
- Long-running operations

### What to verify
- P50, P95, P99 latency
- Memory usage doesn't explode
- UI remains responsive during background work
- Errors don't cascade
- Recovery from degradation

## 9. Localization scenarios

For internationalized products.

### Patterns
- Long-string languages (German, Finnish)
- RTL languages (Arabic, Hebrew)
- Multi-byte characters (CJK)
- Different date / number / currency formats
- Pluralization rules vary by language
- Time zones

### What to verify
- Text fits / wraps; doesn't truncate critical info
- RTL layout flips correctly
- Dates render in user's locale
- Currency formats match locale
- Pluralization rules respected
- DST transitions don't break

## 10. Cross-platform scenarios

For multi-platform products.

### Patterns
- Browsers (Chrome, Safari, Firefox, Edge)
- Mobile browsers
- iOS Safari quirks
- Old browser versions (if supported)
- Desktop OS (macOS, Windows, Linux)
- Mobile OS (iOS, Android — multiple versions)
- Screen sizes (320px → 4K)

### What to verify
- Visual consistency
- Functional consistency
- Performance acceptable on lowest-tier
- Touch + click both work where applicable

## 11. Scenario priorities

Risk-weighted prioritization:

```
P0: Will block ship if broken
P1: Will harm user trust if broken
P2: Will inconvenience user
P3: Edge case; nice to cover
```

Map scenarios to priorities:
- Happy paths: usually P0
- Common edge cases: P1
- Empty state: P1
- Error handling for common errors: P1
- Concurrent (for collab): P0-P1
- Accessibility baseline: P1
- Security (auth, payment): P0
- Rare edge cases: P2-P3

## 12. Per-feature templates

### Form submission
- 1 happy / 5 edge / 5 error / 1 empty / 2 a11y / 3 security

### Browse / list
- 2 happy / 3 edge / 2 error / 2 empty / 3 a11y / 2 security

### Real-time / collaborative
- 3 happy / 4 edge / 4 error / 1 empty / 5 concurrent / 3 a11y / 3 security

### File upload
- 2 happy / 8 edge / 4 error / 1 empty / 1 concurrent / 2 a11y / 6 security

### Payment / financial
- 3 happy / 8 edge / 8 error / 1 empty / 4 concurrent / 3 a11y / 10 security

Adjust for your risk profile.

## Appendix: recommended counts, risk weighting, manual vs automated

### Recommended scenario counts (what `test_scenario_generator.py` checks)

Generated from the script's `RECOMMENDED` table; localization and cross-platform are situational. Starting defaults, adjusted for the feature's risk.

| Feature type | happy_path | edge | error | empty | concurrent | a11y | security | performance |
|---|---|---|---|---|---|---|---|---|
| form | 1-3 | 4-8 | 4-6 | 1-2 | 0-2 | 3-5 | 3-5 | 0-2 |
| browse | 2-3 | 3-5 | 2-3 | 2-3 | 0-1 | 3-4 | 2-3 | 1-3 |
| realtime | 2-4 | 4-6 | 4-6 | 1-2 | 4-6 | 3-4 | 3-5 | 1-3 |
| upload | 1-2 | 6-10 | 4-6 | 1-1 | 1-2 | 2-3 | 5-10 | 1-3 |
| payment | 2-3 | 6-10 | 8-12 | 1-2 | 4-6 | 3-4 | 8-12 | 1-3 |
| bulk | 1-2 | 4-6 | 4-6 | 1-1 | 2-4 | 2-3 | 3-5 | 2-4 |
| generic | 1-3 | 3-5 | 3-5 | 1-2 | 0-2 | 3-4 | 2-4 | 0-2 |

### Risk-weighted scenario selection

Not all scenarios need full QA coverage. Apply:
- **Happy path:** always test
- **Edge cases:** test those that matter (likelihood × severity)
- **Error handling:** test all paths that user can recover from
- **Empty state:** always test (first impression!)
- **Concurrent:** test for data-integrity-critical features
- **Accessibility:** baseline coverage on all UI; full coverage on user-facing
- **Security:** scale with sensitivity (full coverage on auth/payment)

### Manual vs automated

| Scenario type | Default |
|----------------|---------|
| Happy path | Automated (E2E or integration) |
| Edge cases (input validation) | Unit tests |
| Error handling | Mix (mocked errors in unit; real in integration) |
| Empty state | Visual regression + manual |
| Concurrent | Hard — usually manual + targeted integration |
| Accessibility | Automated (axe-core) + manual screen-reader |
| Security | SAST + DAST + manual review for critical paths |
| Performance | Automated load tests |
| Localization | Pseudo-localization + manual spot-check |

<!-- Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/execution/test-scenarios -->
