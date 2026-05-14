---
domain: requirements
tags: [gherkin, acceptance-criteria, specification, examples, bdd]
last-updated: 2026-05-14
---

# Gherkin Specification Format

## Key Takeaways

- Write declarative Examples that describe behaviour, not UI steps; use `Example:` not `Scenario:` (BDD, North, 2006).
- Example titles must be unique within the feature file — pytest-beehave uses title-based mapping (title → `test_<slug>` function name) for traceability.
- `Then` must be a single, observable, measurable outcome; no "and" combining multiple behaviours in one `Then`.
- Bug Examples use `@bug` and require both a specific feature test and a Hypothesis property test.
- After criteria commit, Examples are frozen; changes require `@deprecated` on the old Example and a new Example with a new unique title.
- Two Examples with the same `Then` outcome but different input values test the same behaviour; partition by behaviour outcome, not by input value (Wynne, 2015; Adzic, 2011).

## Concepts

**Declarative vs Imperative Gherkin**: Declarative Examples describe behaviour, not UI steps (BDD, North, 2006). "Given a registered user Bob / When Bob logs in / Then Bob sees a personalized welcome" is correct. "Given I type 'bob' in the username field / When I click the Login button / Then I see 'Welcome, Bob'" is imperative and wrong. Declarative Examples express what the user observes, not how the system implements it.

**Example Format and Title-Based Mapping**: Each Example uses the `Example:` keyword (not `Scenario:`), includes `Given/When/Then` in plain English. pytest-beehave maps Examples to test functions by title: the function name is `test_<scenario_title_slug>`. Titles must be unique within the feature file. Descriptive titles serve as the traceability link between feature specification and test code — no `@id` tags are needed.

**Single Observable Outcome per Then**: `Then` must be a single, observable, measurable outcome. No "and" combining multiple behaviours in one `Then`. Split into separate Examples instead. Observable means observable by the end user, not by a test harness.

**Frozen Examples**: After criteria commit, Examples are frozen. Changes require `@deprecated` on the old Example and a new Example with a new unique title. No editing or deleting committed Examples. This prevents scope creep and maintains traceability from test to acceptance criterion.

**Bug Examples**: When a defect is reported, add an `@bug` Example. Implement both a specific test and a Hypothesis property test covering the whole class of inputs. Both are required.

**Behavioral Distinctness**: Two Examples are behavior-distinct only when they produce different `Then` outcomes (Wynne, 2015; Adzic, 2011). Partitioning by behaviour outcome rather than by input value avoids the combinatorial explosion of value-distinct testing. Two Examples with the same `Then` but different input values test the same behaviour — keep one, discard the duplicates. For action and behavioural rules, each distinct outcome gets one representative Example. For structural (invariant) rules, one representative Example suffices because the invariant holds across all inputs; full coverage is deferred to a Hypothesis property test per [[software-craft/test-design#concepts]].

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
- `Then` must be a single, observable, measurable outcome: no "and"
- Observable means observable by the end user, not by a test harness
- Declarative, not imperative: describe behaviour, not UI steps
- Each Example must be observably distinct from every other
- Title must be unique within the feature file

### Title Conventions for pytest-beehave

- Title becomes the test function name: `test_<scenario_title_slug>`
- Titles must be unique within the feature file
- Titles should be descriptive enough to serve as the test identifier
- No `@id` tags — the title is the traceability link
- After criteria commit, changing a title breaks the traceability chain — deprecate and create a new Example instead

### Feature Title and Filename Convention

pytest-beehave derives the test directory name from the Feature title (slugified). The feature filename stem MUST match the Feature title slug. For example: Feature title "CLI Entrypoint" → slug `cli_entrypoint` → filename `cli_entrypoint.feature` → test directory `tests/features/cli_entrypoint/`. A mismatch between title slug and filename stem causes `misplaced-test` errors.

### Frozen Examples Rule

After criteria commit, Examples are frozen. Any change to committed Examples requires:
1. `@deprecated` on the old Example
2. A new Example with a new unique title

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
1. The specific test in `tests/features/<feature_slug>/`
2. A Hypothesis property test covering the whole class of inputs

### Common Mistakes

- "Then: It works correctly": not measurable
- "Then: The system updates the database and sends an email": split into two Examples
- Multiple behaviours in one Example: split them
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behaviour descriptions
- Two examples with the same `Then` but different input values: duplicate behaviour coverage per [[requirements/gherkin#concepts]]
- Duplicate Example titles within a feature file: breaks pytest-beehave mapping

### Feature File Path Convention

Feature files are located at `docs/features/<file>.feature`. The flow works on one feature at a time, so `<file>.feature` refers to a single feature file, not a glob pattern.

### Test Path and Traceability Conventions

Test path conventions (`tests/features/<feature_slug>/`), the feature-test vs unit-test boundary, and two-dimensional traceability (structural + semantic) are defined in [[software-craft/test-design]].

## Related

- [[requirements/invest]]: story quality criteria for rules
- [[requirements/moscow]]: prioritizing Examples as Must/Should/Could
- [[requirements/decomposition]]: splitting Rules with too many Examples
- [[requirements/pre-mortem]]: finding hidden failure modes in rules
- [[software-craft/test-design]]: property-based testing for invariant rules
