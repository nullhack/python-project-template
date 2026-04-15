---
name: tdd
description: Step 3 — write failing tests mapped 1:1 to UUID acceptance criteria with proper markers and docstrings
version: "1.0"
author: developer
audience: developer
workflow: feature-lifecycle
---

# TDD — Test First

Write tests before writing any production code. Every test must fail when first run. Every test maps to exactly one UUID acceptance criterion.

## Test Tool Decision

| Situation | Tool |
|---|---|
| Deterministic input/output, one scenario | Plain pytest |
| Pure function, many input combinations | Hypothesis `@given` |
| Stateful system with sequences of operations | Hypothesis stateful testing |

**Never use Hypothesis for**: I/O operations, side effects, network calls, database writes, or anything where the test environment matters.

## Test File Structure

File naming: `<descriptive-name>_test.py` — never `test_<name>.py`. All test files live directly in `tests/` (flat layout, no subdirectories).

| Source | Test |
|---|---|
| `<package>/module.py` | `tests/module_test.py` |
| `<package>/domain/service.py` | `tests/service_test.py` |
| `<package>/api/routes.py` | `tests/routes_test.py` |

## Test Function Naming

```
test_<short_title>
```

Examples:
- `test_ball_bounces_off_top_wall`
- `test_email_requires_at_symbol`
- `test_empty_cart_returns_zero_total`

## Docstring Format (mandatory)

```python
def test_ball_bounces_off_top_wall():
    """a1b2c3d4-e5f6-7890-abcd-ef1234567890

    Given: A ball moving upward reaches y=0
    When: The physics engine processes the next frame
    Then: The ball velocity y-component becomes positive
    """
    # Given
    ball = Ball(x=5, y=0, vy=-1)
    # When
    result = physics.update(ball)
    # Then
    assert result.vy > 0  # Asserts observable behavior
```

**A test that looks correct but is wrong:**

```python
def test_ball_bounces_off_top_wall():
    """a1b2c3d4-e5f6-7890-abcd-ef1234567890

    Given: A ball moving upward reaches y=0
    When: The physics engine processes the next frame
    Then: The ball velocity y-component becomes positive
    """
    # Given
    ball = Ball(x=5, y=0, vy=-1)
    # When
    physics.update(ball)
    # Then
    assert ball._velocity_y > 0  # WRONG: tests internal attribute, not observable behavior
    # This test would break if you rename _velocity_y, even though behavior is unchanged.
```

The correct test (`result.vy > 0`) would still pass after a complete rewrite that preserves behavior.
The wrong test (`ball._velocity_y > 0`) would break if you rename the internal field.

**Rules**:
- First line: `<uuid>` only — no description
- Mandatory blank line between UUID and Given
- Given/When/Then on separate indented lines
- `# Given`, `# When`, `# Then` comments in the test body mirror the docstring
- UUID must exactly match the UUID on the criterion's first line in the feature doc

## Markers

Every test gets exactly one of:
- `@pytest.mark.unit` — isolated, no external state
- `@pytest.mark.integration` — multiple components, external state

Slow tests additionally get `@pytest.mark.slow` (anything > 50ms: DB, network, Hypothesis, terminal I/O).

```python
@pytest.mark.unit
def test_ball_bounces_off_top_wall():
    ...

@pytest.mark.integration
@pytest.mark.slow
def test_checkout_persists_order_to_database():
    ...
```

### Choosing a Marker

| Marker | Use When |
|---|---|
| `unit` | One function or class in isolation; no external dependencies |
| `integration` | Multiple components working together; external state (DB, filesystem, network) |
| `slow` | Test takes > 50ms — add alongside `unit` or `integration`, never alone |

When in doubt, start with `unit`. Upgrade to `integration` if the implementation requires external state.

## Hypothesis Tests

Use `@given` with `@example` for known edge cases and `assume` for precondition filtering. Configure via `@settings`, not markers.

```python
from hypothesis import given, example, assume, settings
from hypothesis import strategies as st

@pytest.mark.unit
@pytest.mark.slow
@given(x=st.floats(min_value=-100, max_value=100, allow_nan=False))
@example(x=0.0)
@example(x=-100.0)
@settings(max_examples=200)
def test_compute_distance_always_non_negative(x: float) -> None:
    """b2c3d4e5-f6a7-8901-bcde-f12345678901

    Given: Any floating point input value
    When: compute_distance is called
    Then: The result is >= 0
    """
    # Given
    assume(x != 0.0)
    # When
    result = compute_distance(x)
    # Then
    assert result >= 0
```

### Meaningful vs. Tautological Property Tests

A meaningful property test asserts an **invariant** — something that must be true regardless of input, that is NOT derived from the implementation itself:

| Tautological (useless) | Meaningful (tests the contract) |
|---|---|
| `assert Score(x).value == x` | `assert Score(x).value >= 0` |
| `assert sorted(list) == sorted(list)` | `assert sorted(list) == sorted(list, key=...)` |
| `assert EmailAddress(valid).value == valid` | `assert "@" in EmailAddress(valid).value` |

## Writing Failing Tests (Step 3 Checklist)

1. For each UUID in the feature doc, create one test function
2. Write the full test body with real assertions (not `raise NotImplementedError`)
3. The test will fail because the production code does not exist yet — that is correct
4. Run `pytest` — confirm every new test fails with `ImportError` or `AttributeError`, not a logic failure
5. Commit: `test(<feature-name>): add failing tests for all acceptance criteria`

## Integration Test Requirement

For any feature with multiple components or user interaction, at least one `@pytest.mark.integration` test must exercise the public entry point with realistic input. This test must NOT call internal helpers directly — it must go through the same path a real user would.

## Semantic Alignment Rule

The test's Given/When/Then must operate at the **same abstraction level** as the AC's Given/When/Then.

| AC says | Test must do |
|---|---|
| "When the user presses W" | Send `"W"` through the actual input mechanism (stdin, key event, CLI arg) |
| "When `update_player` receives 'W'" | Call `update_player("W")` directly — the boundary is explicit |

If testing through the real entry point is infeasible, the developer must add a new AC via `skill extend-criteria` that explicitly describes the lower-level boundary. **Never silently shift abstraction levels.**

## UUID Uniqueness

One test function per UUID. One UUID per test function. If only `Given` varies across cases, that is a property by definition — use Hypothesis `@given` with `@example` for known edge cases. If `When` or `Then` would differ, that is a new criterion: use `extend-criteria`.

## Property-Based Testing Decision Rule

Use Hypothesis when a function has invariants — things that must always be true regardless of input:

| Code has... | Write a property test for... |
|---|---|
| Ball position clamped to screen | Position always stays within bounds |
| Score accumulator | Score never goes negative |
| Sorted collection | Order is always preserved after insertion |
| Domain value object | Constructor always rejects invalid inputs |

This catches "technically passes but doesn't work" failures that deterministic tests miss.

## Quality Rules

- Write every test as if you cannot see the production code. The test describes what a caller observes, not how the code achieves it. If a complete internal rewrite would not break this test (while preserving behavior), it is correctly written.
- No `isinstance()`, `type()`, or internal attribute (`_x`) checks in assertions
- One assertion concept per test (multiple `assert` statements are ok if they verify the same thing)
- No `pytest.skip` or `pytest.mark.xfail` without written justification in the docstring
- Never use `noqa` — fix the underlying issue instead
- Test data embedded directly in the test, not loaded from external files
