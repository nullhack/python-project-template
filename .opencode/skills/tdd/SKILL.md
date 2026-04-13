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

## Test Tool Decision Guide

Choosing the right test tool matters. Applying the wrong one wastes effort.

### Use plain TDD (example-based) when:
- Testing **side effects**: DB connections, file handles, network sockets, state changes
- Testing **behavioral contracts**: "given connection, when closed, it ceases to exist"
- Testing **error paths** with specific messages
- Testing **integration** between components
- The assertion is about a specific, known outcome

```python
# RIGHT: plain TDD for side-effectful behavior
def test_connection_closed_should_no_longer_be_active(db_connection):
    db_connection.close()
    assert not db_connection.is_active
```

### Use Hypothesis (property-based) when:
- Testing **pure functions** with well-defined input/output relationships
- Testing **algorithms**: parsers, serializers, transformers, validators
- Testing **invariants** that must hold for *all* valid inputs, not just examples
- Testing **round-trip** properties (encode → decode == original)
- You would otherwise write 5+ similar parametrize tests varying only input values

```python
# RIGHT: Hypothesis for pure-function invariants
@given(st.text(min_size=1, max_size=100))
def test_any_valid_name_provided_slugify_should_be_idempotent(name):
    slug = slugify(name)
    assert slug == slugify(slugify(name))  # idempotent
```

### Use Hypothesis stateful testing when:
- Testing **state machines** with many possible operation sequences
- You want to find **unexpected state transitions** from interleaved operations

### NEVER use Hypothesis for:
- Side effects (DB writes, HTTP calls, file I/O) — it's inefficient and flaky
- Tests that require specific fixture data from prototype output
- Behavioral contracts where the outcome depends on external state

## TDD Patterns

For complete test patterns and guidelines, see:
[Reference: Test Patterns](../reference/test-patterns.md)

## Acceptance Criteria Test Docstrings

All test functions must include acceptance criteria docstrings with UUID traceability. Each test maps to an acceptance criteria UUID from the feature specification.

### Required Format: UUID with Acceptance Criteria Steps

The docstring format uses UUID from acceptance criteria followed by Given/When/Then steps with **mandatory newlines**:

```python
def test_user_login_with_valid_credentials_should_grant_access():
    """123e4567-e89b-12d3-a456-426614174000: Successful user authentication.

    Given: A registered user with valid credentials exists in the system
    When: The user submits correct username and password
    Then: Access should be granted to the application
    """
```

**CRITICAL**: Newlines are required:
- Docstrings must start with newline: `"""\n`
- Docstrings must end with newline: `\n"""`

### UUID Source

The UUID comes from the acceptance criteria in `docs/features/business/backlog/<feature>.md` or `docs/features/architecture/backlog/<feature>.md`. Generate UUIDs using:
```bash
python -c "import uuid; print(uuid.uuid4())"
```

Each acceptance criteria gets a unique UUID, and tests reference that UUID for traceability.

### Why Acceptance Criteria Docstrings?

1. **pytest-html**: The HTML report displays docstrings as test names, making it easy to understand what each test verifies
2. **Documentation**: Docstrings serve as living documentation of test intent
3. **Debugging**: When a test fails, the docstring immediately shows what scenario was being tested

### CRITICAL: Newline Requirements

**STRICT**: Docstrings MUST start and end with newlines:

```python
# ✅ CORRECT
def test_valid_case():
    """123e4567-e89b-12d3-a456-426614174000: Valid scenario.

    Given: Preconditions
    When: Action
    Then: Expected outcome
    """

# ❌ WRONG - Missing starting newline  
def test_invalid_case():
    """123e4567-e89b-12d3-a456-426614174000: Invalid scenario.
    Given: Preconditions"""

# ❌ WRONG - Missing ending newline
def test_invalid_case():
    """
    123e4567-e89b-12d3-a456-426614174000: Invalid scenario.
    Given: Preconditions"""

# ❌ WRONG - Both missing
def test_invalid_case():
    """123e4567-e89b-12d3-a456-426614174000: Invalid scenario."""
```

### Multi-line Scenarios

For complex scenarios, use additional detail in each section:

```python
def test_federation_created_should_have_active_status():
    """
    Given: A valid federation request with required fields
           - name: "Test Federation"
           - owner_id: 12345
           - member_count: 3
    When: FederationService.create() is called
    Then: Status should be 'active'
          Created timestamp should be set
          ID should be generated
    """
```

## Project Test Structure: Mirror Source Tree

Tests MUST mirror the source package structure. Each source module gets a corresponding test file.

**Naming convention**: `*_test.py` suffix (configure in `pyproject.toml`: `python_files = ["*_test.py"]`)

```
tests/
├── unit/
│   ├── __init__.py                 # Empty marker
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── disputes_test.py        # Tests for domain/disputes.py
│   │   ├── reputation_test.py      # Tests for domain/reputation.py
│   │   └── value_objects_test.py   # Tests for domain/value_objects.py
│   ├── storage/
│   │   ├── __init__.py
│   │   └── sqlite/
│   │       ├── __init__.py
│   │       ├── sqlite_connection_test.py
│   │       └── sqlite_schema_test.py
│   └── models_test.py              # Tests for models.py (enums + dataclasses)
├── integration/
│   ├── __init__.py                 # Empty marker
│   └── storage/
│       ├── __init__.py
│       ├── factory_test.py         # Tests for storage/factory.py
│       ├── memory/
│       │   ├── __init__.py
│       │   └── [entity]_repo_test.py
│       └── sqlite/
│           ├── __init__.py
│           └── [entity]_repo_test.py
├── conftest.py                     # Shared fixtures
└── python-project-template_test.py  # Smoke test
```

### Mirror Source Tree Rule
For each source module `python_module_template/<path>/<module>.py`, create a corresponding test file `tests/<path>/<module>_test.py`:

| Source | Test |
|--------|------|
| `python_module_template/models.py` | `tests/unit/models_test.py` |
| `python_module_template/domain/<module>.py` | `tests/unit/domain/<module>_test.py` |
| `python_module_template/storage/factory.py` | `tests/integration/storage/factory_test.py` |
| `python_module_template/storage/memory/adapters.py` | `tests/integration/storage/memory/*_repo_test.py` |

## Test Workflow

1. **Write failing test** (RED phase)
   - Use descriptive naming: `test_[condition]_should_[outcome]`
   - Embed test data directly in test file
   - Place test file in mirror location under `tests/`

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
