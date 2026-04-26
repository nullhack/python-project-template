---
domain: requirements
tags: [gherkin, acceptance-criteria, specification, examples]
last-updated: 2026-04-26
---

# Gherkin Specification Format

## Key Takeaways

- Write declarative Examples that describe behaviour, not UI steps; use `Example:` not `Scenario:`.
- Each Example must have an `@id` tag (8-char hex, assigned by `uv run task assign-ids`) and be observably distinct from every other Example.
- `Then` must be a single, observable, measurable outcome; no "and" combining multiple behaviours in one `Then`.
- Bug Examples use `@bug` and require both a specific feature test and a Hypothesis property test.
- After criteria commit, Examples are frozen; changes require `@deprecated` on the old Example and a new Example with a new `@id`.

## Concepts

**Declarative vs Imperative Gherkin**: Declarative Examples describe behaviour, not UI steps. "Given a registered user Bob / When Bob logs in / Then Bob sees a personalized welcome" is correct. "Given I type 'bob' in the username field / When I click the Login button / Then I see 'Welcome, Bob'" is imperative and wrong.

**Example Format and @id Tags**: Each Example uses the `Example:` keyword (not `Scenario:`), includes `Given/When/Then` in plain English, and must have an `@id` tag (8-character hex, assigned by `uv run task assign-ids`). Each Example must be observably distinct from every other Example in the same Rule.

**Single Observable Outcome per Then**: `Then` must be a single, observable, measurable outcome. No "and" combining multiple behaviours in one `Then` — split into separate Examples instead.

**Bug Examples**: When a defect is reported, the PO adds an `@bug` Example. The SE implements both a specific `@id` test in `tests/features/` and a Hypothesis `@given` property test in `tests/unit/`. Both are required.

**Frozen Examples**: After criteria commit, Examples are frozen. Changes require `@deprecated` on the old Example and a new Example with a new `@id`. No editing or deleting committed Examples.

## Content

### Declarative vs Imperative Gherkin

| Imperative (wrong) | Declarative (correct) |
|---|---|
| Given I type "bob" in the username field | Given a registered user Bob |
| When I click the Login button | When Bob logs in |
| Then I see "Welcome, Bob" on the dashboard | Then Bob sees a personalized welcome |

Declarative Examples describe behaviour, not UI steps. They express what the user observes, not how the system implements it.

### Example Format Rules

- `Example:` keyword (not `Scenario:`)
- `Given/When/Then` in plain English
- `Then` must be a single, observable, measurable outcome — no "and"
- **Observable means observable by the end user**, not by a test harness
- **Declarative, not imperative** — describe behaviour, not UI steps
- Each Example must be observably distinct from every other

### Feature File Format Overview

Each feature is a single `.feature` file containing:

1. **Description block** — narrative description and Status
2. **Rules (Business)** — business rules that hold across multiple Examples
3. **Constraints** — non-functional requirements
4. **Rule blocks** — each with a user story header and Example blocks

```gherkin
Rule: Wall bounce
  As a game engine
  I want balls to bounce off walls
  So that gameplay feels physical

  @id:a3f2b1c4
  Example: Ball bounces off top wall
    Given a ball moving upward reaches y=0
    When the physics engine processes the next frame
    Then the ball velocity y-component becomes positive
```

### @id Tag Format and Purpose

- Format: `@id:XXXXXXXX` (8-character hex)
- Assigned by running `uv run task assign-ids`
- Globally unique across all `.feature` files
- Enables traceability from test to acceptance criterion
- After criteria commit, Examples are frozen — changes require `@deprecated` on the old Example and a new Example with a new `@id`

### Bug Handling Example Format

When a defect is reported, the PO adds a `@bug` Example:

```gherkin
@bug
Example: <what the bug is>
  Given <conditions that trigger the bug>
  When <action>
  Then <correct behaviour>
```

The SE implements both:
1. The specific `@id` test in `tests/features/<feature_slug>/`
2. A `@given` Hypothesis property test in `tests/unit/` covering the whole class of inputs

### Common Mistakes

- "Then: It works correctly" — not measurable
- "Then: The system updates the database and sends an email" — split into two Examples
- Multiple behaviours in one Example — split them
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behaviour descriptions

## Related

- [[requirements/invest-moscow]] — story quality and prioritization criteria
- [[requirements/discovery-techniques]] — surfacing requirements before writing Gherkin
- [[architecture/domain-stubs]] — translating Gherkin into domain stubs