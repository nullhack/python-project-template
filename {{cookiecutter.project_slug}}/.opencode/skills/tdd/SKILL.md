---
name: tdd
description: Implement Test-Driven Development with descriptive naming conventions and pytest best practices
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---

## What I do
Guide the creation of tests using TDD methodology with descriptive naming conventions, using pytest, coverage, and hypothesis for robust testing.

## When to use me
Use this after prototype validation to create comprehensive tests before implementing the actual feature code.

## Test Data from Prototypes

After running prototypes:
1. Copy output values directly into test file as fixtures/constants
2. Delete prototype directory: `rm -rf prototypes/<name>/`
3. Tests read from test file fixtures, NOT from prototype files

## TDD Patterns

For complete test patterns and guidelines, see:
[Reference: Test Patterns](../reference/test-patterns.md)

## Test Workflow

1. **Write failing test** (RED phase)
   - Use descriptive naming: `test_when_[condition]_should_[outcome]`
   - Embed test data directly in test file

2. **Implement minimal code** (GREEN phase)
   - Just enough to pass the test

3. **Refactor** (REFACTOR phase)
   - Improve code while keeping tests green

## CRITICAL: Handle Lint Warnings Properly

When writing tests, ruff may report issues like RUF069 (float-equality-comparison). 

**NEVER use noqa to silence warnings.** Instead:
1. Check the rule at https://docs.astral.sh/ruff/rules/<RULE_CODE>/
2. Apply the proper fix from the "How to fix" section

Example for RUF069 (float-equality):
```python
# WRONG - silencing
assert bond.amount_usdt == 10.0  # noqa: RUF069

# RIGHT - using math.isclose()
import math
assert math.isclose(bond.amount_usdt, 10.0, abs_tol=1e-9)
```

## Running Tests

```bash
# Run all tests
task test

# Run with coverage
task test --cov

# Run specific marker
pytest -m unit
```
