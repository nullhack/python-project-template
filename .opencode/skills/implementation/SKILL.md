---
name: implementation
description: Steps 2-3 — Architecture + TDD Loop, one @id at a time
version: "3.0"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Implementation

Steps 2 (Architecture) and 3 (TDD Loop) combined into a single skill. The software-engineer owns both.

## Developer Quality Gate Priority Order

During implementation, correctness priorities are (in order):

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns
2. **One @id green** — the specific test under work passes, plus `test-fast` still passes
3. **Commit** — when a meaningful increment is green
4. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run at end-of-feature handoff

Design correctness is far more important than lint/pyright/coverage compliance. Never run lint, static-check, or coverage during the TDD loop — those are handoff-only checks.

---

## Step 2 — Architecture

### Prerequisites (stop if any fail — escalate to PO)

1. `docs/features/in-progress/` contains only `.gitkeep` (no `.feature` files). If another `.feature` file exists, **STOP** — another feature is already in progress.
2. The feature file's discovery section has `Status: BASELINED`. If not, escalate to PO — Step 1 is incomplete.
3. The feature file contains `Rule:` blocks with `Example:` blocks and `@id` tags. If not, escalate to PO — criteria have not been written.
4. Package name confirmed: read `pyproject.toml` → locate `[tool.setuptools]` → confirm directory exists on disk.

### Package Verification (mandatory — before writing any code)

1. Read `pyproject.toml` → locate `[tool.setuptools]` → record `packages = ["<name>"]`
2. Confirm directory exists: `ls <name>/`
3. All new source files go under `<name>/` — never under a template placeholder.

### Move Feature File

```bash
mv docs/features/backlog/<name>.feature docs/features/in-progress/<name>.feature
```

Update `TODO.md` Source path from `backlog/` to `in-progress/`.

### Read Phase (all before writing anything)

1. Read `docs/features/discovery.md` (project-level)
2. Read **ALL** `.feature` files in `docs/features/backlog/` (discovery + entities sections)
3. Read in-progress `.feature` file (full: Rules + Examples + @id)

### Domain Analysis

From Entities table + Rules (Business) in `.feature` file:
- **Nouns** → named classes, value objects, aggregates
- **Verbs** → method names with typed signatures
- **Datasets** → named types (not bare dict/list)
- **Bounded Context check**: same word, different meaning across features? → module boundary
- **Cross-feature entities** → candidate shared domain layer

### Silent Pre-mortem (before writing anything)

> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class:
- >2 ivars? → split
- >1 reason to change? → isolate

For each external dep:
- Is it behind a Protocol? → if not, add

For each noun:
- Serving double duty across modules? → isolate

If pattern smell detected, load `skill design-patterns`.

### Write Architecture Section

Append to `docs/features/in-progress/<name>.feature` (before first `Rule:`):

```gherkin
  Architecture:

  ### Module Structure
  - `<package>/domain/<noun>.py` — named class + responsibilities
  - `<package>/domain/service.py` — cross-entity operations
  - `<package>/adapters/<dep>.py` — Protocol implementation

  ### Key Decisions
  ADR-001: <title>
  Decision: <what>
  Reason: <why in one sentence>
  Alternatives considered: <what was rejected and why>

  ### Build Changes (needs PO approval: yes/no)
  - New runtime dependency: <name> — reason: <why>
```

Signatures are informative — tests/implementation may refine them. Record significant changes as ADR updates.

### Architecture Smell Check (hard gate)

- [ ] No planned class with >2 responsibilities (SOLID-S)
- [ ] No planned class with >2 instance variables (OC-8)
- [ ] All external deps assigned a Protocol/Adapter (SOLID-D + Hexagonal)
- [ ] No noun with different meaning across planned modules (DDD BC)
- [ ] No missing Creational pattern
- [ ] No missing Structural pattern  
- [ ] No missing Behavioral pattern
- [ ] Each ADR consistent with each @id AC — no contradictions

If any check fails: fix before committing.

Commit: `feat(<feature-name>): add architecture`

---

## Step 3 — TDD Loop

### Prerequisites

- [ ] Architecture section present in in-progress `.feature` file
- [ ] All tests written in `tests/features/<feature-name>/`

### Build TODO.md Test List

1. List all `@id` tags from in-progress `.feature` file
2. Order: fewest dependencies first; most impactful within that set
3. Each `@id` = one TODO item, status: `pending`

### Outer Loop — One @id at a time

**WIP limit**: exactly one `in_progress` at all times.

For each pending `@id`:

```
INNER LOOP
├── RED
│   ├── Write test body (Given/When/Then → Arrange/Act/Assert)
│   ├── uv run task test-fast
│   └── EXIT: this @id FAILS
│       (if it passes: test is wrong — fix it first)
│
├── GREEN
│   ├── Write minimum code — YAGNI + KISS only
│   │   (no DRY, SOLID, OC here — those belong in REFACTOR)
│   ├── uv run task test-fast
│   └── EXIT: this @id passes AND all prior tests pass
│       (fix implementation only; do not advance to next @id)
│
└── REFACTOR
    ├── Apply: DRY → SOLID → OC → patterns
    ├── Load design-patterns skill if smell detected
    ├── Add type hints and docstrings
    ├── uv run task test-fast after each change
    └── EXIT: test-fast passes; no smells remain

Mark @id completed in TODO.md
Commit when a meaningful increment is green
```

### Quality Gate (all @id green)

```bash
uv run task lint
uv run task static-check
uv run task test          # coverage must be 100%
timeout 10s uv run task run
```

If coverage < 100%: add test in `tests/unit/` for uncovered branch (do NOT add @id tests for coverage).

All must pass before Self-Declaration.

### Self-Declaration (once, after all quality gates pass)

Write into `TODO.md` under a `## Self-Declaration` block:

```markdown
## Self-Declaration
As a software-engineer I declare:
* YAGNI: no code without a failing test — AGREE/DISAGREE | file:line
* YAGNI: no speculative abstractions — AGREE/DISAGREE | file:line
* KISS: simplest solution that passes — AGREE/DISAGREE | file:line
* KISS: no premature optimization — AGREE/DISAGREE | file:line
* DRY: no duplication — AGREE/DISAGREE | file:line
* DRY: no redundant comments — AGREE/DISAGREE | file:line
* SOLID-S: one reason to change per class — AGREE/DISAGREE | file:line
* SOLID-O: open for extension, closed for modification — AGREE/DISAGREE | file:line
* SOLID-L: subtypes substitutable — AGREE/DISAGREE | file:line
* SOLID-I: no forced unused deps — AGREE/DISAGREE | file:line
* SOLID-D: depend on abstractions, not concretions — AGREE/DISAGREE | file:line
* OC-1: one level of indentation per method — AGREE/DISAGREE | deepest: file:line
* OC-2: no else after return — AGREE/DISAGREE | file:line
* OC-3: primitive types wrapped — AGREE/DISAGREE | file:line
* OC-4: first-class collections — AGREE/DISAGREE | file:line
* OC-5: one dot per line — AGREE/DISAGREE | file:line
* OC-6: no abbreviations — AGREE/DISAGREE | file:line
* OC-7: ≤20 lines per function, ≤50 per class — AGREE/DISAGREE | longest: file:line
* OC-8: ≤2 instance variables per class — AGREE/DISAGREE | file:line
* OC-9: no getters/setters — AGREE/DISAGREE | file:line
* Patterns: no creational smell — AGREE/DISAGREE | file:line
* Patterns: no structural smell — AGREE/DISAGREE | file:line
* Patterns: no behavioral smell — AGREE/DISAGREE | file:line
* Semantic: tests operate at same abstraction as AC — AGREE/DISAGREE | file:line
```

A `DISAGREE` answer is not automatic rejection — state the reason inline and fix before handing off.

### Hand off to Step 4 (Verify)

Signal completion to the reviewer. Provide:
- Feature file path
- Self-Declaration from TODO.md
- Summary of what was implemented

---

## Test Writing Conventions

### Test File Layout

```
tests/features/<feature-name>/<rule-slug>_test.py
```

- `<feature-name>` = the `.feature` file stem
- `<rule-slug>` = the `Rule:` title slugified

### Function Naming

```python
def test_<rule_slug>_<8char_hex>() -> None:
```

- `rule_slug` = the `Rule:` title with spaces/hyphens replaced by underscores, lowercase
- `8char_hex` = the `@id` from the `Example:` block

### Docstring Format (mandatory)

```python
@pytest.mark.unit
def test_wall_bounce_a3f2b1c4() -> None:
    """
    Given: A ball moving upward reaches y=0
    When: The physics engine processes the next frame
    Then: The ball velocity y-component becomes positive
    """
    # Given
    # When
    # Then
```

**Rules**:
- Docstring contains `Given:/When:/Then:` on separate indented lines
- No extra metadata in docstring — traceability comes from function name `@id` suffix

### Markers

Every test gets exactly one of:
- `@pytest.mark.unit` — isolated, no external state
- `@pytest.mark.integration` — multiple components, external state

Additionally:
- `@pytest.mark.slow` — takes > 50ms (Hypothesis, DB, network, terminal I/O)

```python
@pytest.mark.unit
def test_wall_bounce_a3f2b1c4() -> None:
    ...

@pytest.mark.integration
@pytest.mark.slow
def test_checkout_flow_b2c3d4e5() -> None:
    ...
```

### Hypothesis Tests

When using `@given` in `tests/unit/`:

```python
@pytest.mark.unit
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

**Rules**:
- `@pytest.mark.slow` is mandatory on every `@given`-decorated test
- `@example(...)` is optional but encouraged
- Never use Hypothesis for: I/O, side effects, network calls, database writes

### Semantic Alignment Rule

The test's Given/When/Then must operate at the **same abstraction level** as the AC's Given/When/Then.

| AC says | Test must do |
|---|---|
| "When the user presses W" | Send `"W"` through the actual input mechanism |
| "When `update_player` receives 'W'" | Call `update_player("W")` directly |

If testing through the real entry point is infeasible, escalate to PO to adjust the AC boundary.

### Quality Rules

- Write every test as if you cannot see the production code — test what a caller observes
- No `isinstance()`, `type()`, or internal attribute (`_x`) checks in assertions
- One assertion concept per test (multiple `assert` ok if they verify the same thing)
- No `pytest.skip` or `pytest.mark.xfail` without written justification
- Test data embedded directly in the test, not loaded from external files

### Test Tool Decision

| Situation | Location | Tool |
|---|---|---|
| Deterministic scenario from a `.feature` `@id` | `tests/features/` | Plain pytest |
| Property holding across many input values | `tests/unit/` | Hypothesis `@given` |
| Specific behavior or single edge case | `tests/unit/` | Plain pytest |
| Stateful system with sequences of operations | `tests/unit/` | Hypothesis stateful testing |

---

## Handling Spec Gaps

If during implementation you discover a behavior not covered by existing acceptance criteria:
- **Do not extend criteria yourself** — escalate to PO
- Note the gap in TODO.md under `## Next`
- The PO will decide whether to add a new Example to the `.feature` file

Extra tests in `tests/unit/` are allowed freely (coverage, edge cases, etc.) — these do not need `@id` traceability.

---

## Signature Design

Design signatures before writing bodies. Use Python protocols for abstractions:

```python
from typing import Protocol
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class EmailAddress:
    """A validated email address."""

    value: str

    def __post_init__(self) -> None:
        if "@" not in self.value:
            raise ValueError(f"Invalid email: {self.value!r}")

class UserRepository(Protocol):
    """Persistence interface for users."""

    def save(self, user: "User") -> None: ...
    def find_by_email(self, email: EmailAddress) -> "User | None": ...
```