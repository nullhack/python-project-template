---
domain: software-craft
tags: [testing, pytest, conventions, hypothesis]
last-updated: 2026-04-26
---

# Test Conventions

## Key Takeaways

- Place test files in `tests/features/<feature_slug>/<rule_slug>_test.py`; name functions `test_<feature_slug>_<@id>()`.
- Start new tests as skipped stubs with Gherkin steps in docstrings; remove `@pytest.mark.skip` when implementing.
- Apply `@pytest.mark.slow` to Hypothesis `@given` tests and any test with I/O; apply `@pytest.mark.deprecated` to replaced Examples.
- Test at the same abstraction level as the acceptance criteria (semantic alignment); never test internal implementation details.
- Use Hypothesis for properties that hold across many inputs; use plain pytest for specific behaviours or single edge cases.

## Concepts

**Test File Layout and Naming**: Feature tests go in `tests/features/<feature_slug>/<rule_slug>_test.py`. The feature slug comes from the `.feature` file stem. Function names use `test_<feature_slug>_<@id>()` where `@id` is the Example's ID tag. This enables traceability from test to acceptance criterion.

**Stub Format and Markers**: New tests start as `@pytest.mark.skip(reason="not yet implemented")` stubs with Gherkin steps as docstrings. Remove the skip marker when implementing in the RED phase. `@pytest.mark.slow` is mandatory on every `@given`-decorated Hypothesis test and any test with I/O, network, or DB. `@pytest.mark.deprecated` auto-skips replaced Examples.

**Semantic Alignment Rule**: The test's Given/When/Then must operate at the same abstraction level as the AC's Steps. If the AC says "When the user presses W", the test sends `"W"` through the actual input mechanism. If the AC says "When `update_player` receives 'W'", the test calls `update_player("W")` directly. If testing through the real entry point is infeasible, escalate to PO.

**Quality Rules for Tests**: Write every test as if you cannot see the production code — test what a caller observes. No `isinstance()`, `type()`, or internal attribute checks in assertions. One assertion concept per test. No `pytest.mark.xfail` without written justification. Test data embedded directly in the test, not loaded from external files.

**Test Tool Decision**: Use plain pytest in `tests/features/` for deterministic scenarios from `.feature` `@id` tags. Use Hypothesis `@given` in `tests/unit/` for properties holding across many input values. Use plain pytest in `tests/unit/` for specific behaviours or single edge cases. Use Hypothesis stateful testing in `tests/unit/` for stateful systems with sequences of operations.

## Content

### Test File Layout

```
tests/features/<feature_slug>/<rule_slug>_test.py
```

- `<feature_slug>` = the `.feature` file stem with hyphens replaced by underscores, lowercase
- `<rule_slug>` = the `Rule:` title slugified (lowercase, underscores)

### Function Naming

```python
def test_<feature_slug>_<@id>() -> None:
```

- `feature_slug` = the `.feature` file stem with spaces/hyphens replaced by underscores, lowercase
- `@id` = the `@id` from the `Example:` block

### Docstring Format (mandatory)

New tests start as skipped stubs. Remove `@pytest.mark.skip` when implementing in the RED phase.

```python
@pytest.mark.skip(reason="not yet implemented")
def test_<feature_slug>_<@id>() -> None:
    """
    <@id steps raw text including new lines>
    """
```

Rules:
- Docstring contains Gherkin steps as raw text on separate indented lines
- No extra metadata in docstring — traceability comes from function name `@id` suffix

### Markers

- `@pytest.mark.slow` — takes > 50ms (Hypothesis, DB, network, terminal I/O)
- `@pytest.mark.deprecated` — auto-skipped by pytest-beehive; used for replaced Examples

```python
@pytest.mark.deprecated
def test_wall_bounce_a3f2b1c4() -> None:
    ...

@pytest.mark.slow
def test_checkout_flow_b2c3d4e5() -> None:
    ...
```

### Hypothesis Tests

When using `@given` in `tests/unit/`:

```python
@pytest.mark.slow
@given(x=st.floats(min_value=-100, max_value=100, allow_nan=False))
@example(x=0.0)
def test_wall_bounce_c4d5e6f7(x: float) -> None:
    """
    Given: Any floating point input value
    When: compute_distance is called
    Then: The result is >= 0
    """
    assume(x != 0.0)
    result = compute_distance(x)
    assert result >= 0
```

Rules:
- `@pytest.mark.slow` is mandatory on every `@given`-decorated test
- `@example(...)` is optional but encouraged
- Do not use Hypothesis for: I/O, side effects, network calls, database writes

### Semantic Alignment Rule

The test's Given/When/Then must operate at the same abstraction level as the AC's Steps.

| AC says | Test must do |
|---|---|
| "When the user presses W" | Send `"W"` through the actual input mechanism |
| "When `update_player` receives 'W'" | Call `update_player("W")` directly |

If testing through the real entry point is infeasible, escalate to PO to adjust the AC boundary.

### Quality Rules

- Write every test as if you cannot see the production code — test what a caller observes
- No `isinstance()`, `type()`, or internal attribute (`_x`) checks in assertions
- One assertion concept per test (multiple `assert` ok if they verify the same thing)
- No `pytest.mark.xfail` without written justification
- `pytest.mark.skip(reason="not yet implemented")` is only valid on stubs — remove it when implementing
- Test data embedded directly in the test, not loaded from external files

### Test Tool Decision

| Situation | Location | Tool |
|---|---|---|
| Deterministic scenario from a `.feature` `@id` | `tests/features/` | Plain pytest |
| Property holding across many input values | `tests/unit/` | Hypothesis `@given` |
| Specific behaviour or single edge case | `tests/unit/` | Plain pytest |
| Stateful system with sequences of operations | `tests/unit/` | Hypothesis stateful testing |

## Related

- [[software-craft/tdd]] — TDD cycle governs when tests are written
- [[software-craft/self-declaration]] — item 25 checks semantic alignment
- [[software-craft/code-quality]] — quality gates for test coverage
- [[software-craft/test-design]] — refactor-safe test design, avoiding coupling to implementation