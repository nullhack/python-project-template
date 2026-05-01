---
domain: requirements
tags: [gherkin, acceptance-criteria, specification, examples, bdd]
last-updated: 2026-04-29
---

# Gherkin Specification Format

## Key Takeaways

- Write declarative Examples that describe behaviour, not UI steps; use `Example:` not `Scenario:` (BDD — North, 2006).
- Each Example must have an `@id` tag (format `@id:<unique-id>`) for traceability from test to acceptance criterion.
- `Then` must be a single, observable, measurable outcome; no "and" combining multiple behaviours in one `Then`.
- Bug Examples use `@bug` and require both a specific feature test and a Hypothesis property test.
- After criteria commit, Examples are frozen; changes require `@deprecated` on the old Example and a new Example with a new `@id`.

## Concepts

**Declarative vs Imperative Gherkin**: Declarative Examples describe behaviour, not UI steps (BDD — North, 2006). "Given a registered user Bob / When Bob logs in / Then Bob sees a personalized welcome" is correct. "Given I type 'bob' in the username field / When I click the Login button / Then I see 'Welcome, Bob'" is imperative and wrong. Declarative Examples express what the user observes, not how the system implements it.

**Example Format and @id Tags**: Each Example uses the `Example:` keyword (not `Scenario:`), includes `Given/When/Then` in plain English, and must have an `@id` tag for traceability. The format is `@id:<unique-id>` where the unique ID is assigned when the feature is baselined. Each Example must be observably distinct from every other Example in the same Rule.

**Single Observable Outcome per Then**: `Then` must be a single, observable, measurable outcome. No "and" combining multiple behaviours in one `Then` — split into separate Examples instead. Observable means observable by the end user, not by a test harness.

**Frozen Examples**: After criteria commit, Examples are frozen. Changes require `@deprecated` on the old Example and a new Example with a new `@id`. No editing or deleting committed Examples. This prevents scope creep and maintains traceability from test to acceptance criterion.

**Bug Examples**: When a defect is reported, add an `@bug` Example. Implement both a specific `@id` test and a Hypothesis property test covering the whole class of inputs. Both are required.

## Content

### Declarative vs Imperative

| Imperative (wrong) | Declarative (correct) |
|---|---|
| Given I type "bob" in the username field | Given a registered user Bob |
| When I click the Login button | When Bob logs in |
| Then I see "Welcome, Bob" on the dashboard | Then Bob sees a personalized welcome |

### Example Format Rules

- `Example:` keyword (not `Scenario:`)
- `Given/When/Then` in plain English
- `Then` must be a single, observable, measurable outcome — no "and"
- Observable means observable by the end user, not by a test harness
- Declarative, not imperative — describe behaviour, not UI steps
- Each Example must be observably distinct from every other

### @id Tag Format

- Format: `@id:<unique-id>`
- Assigned when the feature is baselined
- Globally unique across all feature files
- Enables traceability from test to acceptance criterion

### Frozen Examples Rule

After criteria commit, Examples are frozen. This rule is stated explicitly in the feature template and enforced by the `bdd-features` conditions in the planning flow:

- `all_examples_have_ids: ==true`
- `all_examples_have_gherkin: ==true`
- `premortem_done: ==true`

Any change to committed Examples requires:
1. `@deprecated` on the old Example
2. A new Example with a new `@id`

No editing or deleting committed Examples.

### Bug Example Format

When a defect is reported:

```gherkin
@bug
Example: <what the bug is>
  Given <conditions that trigger the bug>
  When <action>
  Then <correct behaviour>
```

Implement both:
1. The specific `@id` test in `tests/features/<feature_slug>/`
2. A Hypothesis property test covering the whole class of inputs

### Common Mistakes

- "Then: It works correctly" — not measurable
- "Then: The system updates the database and sends an email" — split into two Examples
- Multiple behaviours in one Example — split them
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behaviour descriptions

### Feature File Path Convention

Feature files are located at `features/<file>.feature`. The flow works on one feature at a time, so `<file>.feature` refers to a single feature file, not a glob pattern.

### Test Path Convention

Tests follow the pattern `tests/features/<feature_slug>/<rule_slug>_test.py` with function names `test_<feature_stem>_<id>`.

### Feature Test vs Unit Test Boundary

`tests/features/` contains only BDD scenario tests with `@id` traceability to the feature file. Coverage-boosting tests that exercise implementation branches not covered by any `@id` example are unit contract tests and belong in `tests/unit/`, not `tests/features/`. Adding a test to `tests/features/` without a corresponding `@id` tag violates the traceability contract.

### Two-Dimensional Traceability

Traceability is two-dimensional: **structural** (every @id has a test function) and **semantic** (every @id test exercises the entry point the AC describes). Structural traceability without semantic depth creates a false sense of coverage — tests exist for every example but don't verify the actual user-facing behavior. If the AC describes a command-line invocation with flags, the test must invoke the command handler with those flags; calling domain methods directly satisfies structural traceability but fails semantic depth.

## Related

- [[requirements/invest]] — story quality criteria applied before writing Examples
- [[requirements/moscow]] — prioritizing Examples as Must/Should/Could
- [[requirements/decomposition]] — splitting Rules with too many Examples
- [[requirements/pre-mortem]] — finding hidden failure modes before writing Examples