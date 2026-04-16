---
name: implementation
description: Step 4 — Red-Green-Refactor cycle, one test at a time, with commit per green test
version: "2.2"
author: developer
audience: developer
workflow: feature-lifecycle
---

# Implementation

Make the failing tests pass one at a time. Each green test gets its own commit after reviewer approval. Refactor only after tests are green.

## Developer Quality Gate Priority Order

During Step 4, correctness priorities are (in order):

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns
2. **One test green** — the specific test under work passes, plus `test-fast` still passes
3. **Reviewer code-design check** — reviewer verifies design + semantic alignment (no lint/pyright/coverage)
4. **Commit** — only after reviewer APPROVED
5. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run only at developer handoff (before Step 5)

Design correctness is far more important than lint/pyright/coverage compliance. Never run lint, static-check, or coverage during the Red-Green-Refactor cycle — those are handoff-only checks.

## The Cycle

```
Pick one failing test
  → RED: confirm it fails
  → GREEN: write the minimum code to make it pass
  → REFACTOR: clean up, apply design principles
  → SELF-DECLARE: complete the Design Self-Declaration checklist
  ─── STOP ─── do not proceed until reviewer checks ───
  → REVIEWER CHECK: reviewer audits self-declaration against actual code
  ─── WAIT for APPROVED ───
  → COMMIT (only after reviewer APPROVED)
  → Update TODO.md: mark @id [x], update Cycle State to next test
  → pick next failing test
```

**Hard gates**: The cycle has two hard gates — you must STOP before the reviewer check, and WAIT for APPROVED before committing. Never batch multiple tests before a reviewer interaction. Never commit without reviewer approval.

Never write production code before picking a specific failing test. Never refactor while tests are red.

**TODO.md Cycle State is mandatory.** Update `## Cycle State` at every phase transition (RED → GREEN → REFACTOR → SELF-DECLARE → REVIEWER → COMMITTED). If the Cycle State block is missing, add it before proceeding.

## Step 2 — Architecture (do this first)

### Package Verification (mandatory — before writing any code)

1. Read `pyproject.toml` → locate `[tool.setuptools]` → record the value of `packages = ["<name>"]`
2. Confirm that directory exists on disk: `ls <name>/`
3. Write the correct package name at the top of your working notes for this session
4. All new source files go under `<name>/` — never under a template placeholder or any other directory

If `packages` is missing or the directory does not exist, stop and resolve with the stakeholder before writing any code.

**Prerequisites — verify before starting:**
1. `docs/features/in-progress/` contains only `.gitkeep` (no `.feature` files). If another `.feature` file exists, **STOP** — another feature is already in progress.
2. The feature file's discovery section has `Status: BASELINED`. If not, escalate to the PO — Step 1 is incomplete.
3. The feature file contains `Rule:` blocks with `Example:` blocks and `@id` tags. If not, escalate to PO — criteria have not been written.

**Steps:**

1. Move the feature file from `backlog/` to `in-progress/`:
   ```bash
   mv docs/features/backlog/<name>.feature docs/features/in-progress/<name>.feature
   ```
2. Update `TODO.md` Source path from `backlog/` to `in-progress/`.
3. Read both `docs/features/discovery.md` (project-level) and the feature file's discovery section
4. Run a silent pre-mortem: YAGNI, KISS, DRY, SOLID, Object Calisthenics, design patterns
5. Add the Architecture section to `docs/features/in-progress/<name>.feature` (append to the feature description, before the first `Rule:`):

```gherkin
  Architecture:

  ### Module Structure
  - `<package>/domain/entity.py` — data classes and value objects
  - `<package>/domain/service.py` — business logic

  ### Key Decisions
  ADR-001: <title>
  Decision: <what>
  Reason: <why in one sentence>
  Alternatives considered: <what was rejected and why>

  ### Build Changes (needs PO approval: yes/no)
  - New runtime dependency: <name> — reason: <why>
```

6. **Architecture contradiction check**: Compare each ADR against each AC. If any architectural decision contradicts or circumvents an acceptance criterion, flag it and resolve with the PO before writing any production code.
7. **PO domain acknowledgement**: Share the Architecture section with the PO for domain model acknowledgement before Step 3 begins. A one-line response ("no contradictions") is sufficient.
8. If a user story is not technically feasible, escalate to the PO.
9. If any build changes need PO approval, stop and ask before proceeding.

Commit: `feat(<feature-name>): add architecture`

**After committing:** Run `uv run task gen-tests -- --check` to verify stub sync. If changes are shown, run `uv run task gen-tests` to apply them.

## Implementation Order

1. Start with the simplest test: data classes, value objects, pure functions
2. Work outward: state machines, I/O, orchestration
3. Follow the order of acceptance criteria in the `.feature` files

## RED — Confirm the Test Fails

```bash
uv run pytest tests/features/<name>/<story>_test.py::test_<func> -v
```

Expected: `FAILED` or `ERROR`. If it passes before you've written code, the test is wrong — fix it.

Update `## Cycle State` in TODO.md:
```
Test: `@id:<hex>` — <description>
Phase: RED
```

## GREEN — Minimum Implementation

Write the least code that makes **this one test** pass. "Green" means the specific test under work passes — not the full suite.

Apply during GREEN:
- **YAGNI**: if the test doesn't require it, don't write it
- **KISS**: the simplest code that passes

Do NOT apply during GREEN: DRY, SOLID, Object Calisthenics — those come in refactor.

```bash
uv run pytest tests/features/<name>/<story>_test.py::test_<func> -v   # this test must PASS
uv run task test-fast                                                   # no regressions
```

Update `## Cycle State` Phase: `GREEN`

## REFACTOR — Apply Principles (in priority order)

1. **DRY**: extract duplication
2. **SOLID**: split classes that have grown beyond one responsibility
3. **Object Calisthenics** (enforce all 9 rules):
   1. One level of indentation per method — extract inner blocks to named helpers
   2. No `else` after `return` — return early, flatten the happy path
   3. Wrap all primitives — `EmailAddress(str)` not raw `str` for domain concepts
   4. First-class collections — wrap `list[User]` in a `UserList` class
   5. One dot per line — `user.address` then `address.city`, never `user.address.city`
   6. No abbreviations — `calculate` not `calc`, `manager` not `mgr`
   7. Small entities — functions ≤ 20 lines, classes ≤ 50 lines
   8. ≤ 2 instance variables — if a class has 3+ `self.x` in `__init__`, group related
      fields into a new named value object (Rule 3) or collection class (Rule 4). The fix
      must produce a **new named class** — hardcoding constants, inlining literals,
      using class-level variables, or moving fields to a parent class are all invalid
      workarounds and remain FAIL.
   9. No getters/setters — use commands (`activate()`) and queries (`is_active()`)
4. **Type hints**: add/fix type annotations on all public functions and classes
5. **Docstrings**: Google-style on all public functions and classes

### Design Pattern Decision Table

Use when a pattern solves a structural problem you already have:

| If your code has... | Consider... | Why |
|---|---|---|
| Multiple `if/elif` branches on type/state | State or Strategy pattern | Eliminates conditional complexity |
| Constructor that does complex setup | Factory or Builder | Separates construction from use |
| Multiple components that must work together | Facade | Single entry point reduces coupling |
| External dependency (I/O, DB, network) | Repository/Adapter pattern | Enables testing via Protocol |
| Event-driven flow | Observer or pub/sub | Decouples producers from consumers |

### Doctest Check

If you added or modified a `Examples:` block in a Google-style docstring, verify it passes:

```bash
uv run pytest --doctest-modules <module_path>
```

> **Note**: `uv run task test` runs `--doctest-modules`. Keep `Examples:` blocks in Google-style docstrings valid and executable.

### Refactor Self-Check Gates

After refactor, before moving to self-declaration:

| If you see... | Then you must... | Before proceeding |
|---|---|---|
| Function > 20 lines | Extract helper | Verify line count |
| Nesting > 2 levels | Extract to function | Verify max depth |
| Bare `int`/`str` as domain concept | Wrap in value object | Verify no raw primitives in signatures |
| > 4 positional parameters | Group into dataclass | Verify parameter count |
| `list[X]` as domain collection | Wrap in collection class | Verify no bare lists |
| Class with 3+ `self.x` in `__init__` | Group related fields into a new named value object (OC-3) or collection class (OC-4) — **not** a dict, tuple, class variable, constant, or parent class | Count `self.` assignments again; each fix must produce a new named class |

```bash
uv run task test-fast     # must still pass — the ONLY check during refactor
```

Do NOT run `uv run task lint` or `uv run task static-check` during the cycle. Those are handoff-only checks (before Step 5).

Update `## Cycle State` Phase: `REFACTOR`

### Design Self-Declaration

After refactor is complete and `test-fast` passes, write the self-declaration **into `TODO.md`** under a `## Self-Declaration` block (replacing any prior one), then request the reviewer check. The reviewer will read `TODO.md` directly — do not paste the checklist into a separate message.

**Write this block into `TODO.md` now, filling in every item before requesting review:**

```markdown
## Self-Declaration (@id:<hex>)
- [ ] YAGNI-1: No abstractions beyond current AC — `file:line`
- [ ] YAGNI-2: No speculative parameters or flags for hypothetical future use — `file:line`
- [ ] KISS-1: Every function has one job, describable in one sentence without "and" — `file:line`
- [ ] KISS-2: No unnecessary indirection, wrapper layers, or complexity — `file:line`
- [ ] DRY-1: No logic block duplicated across two or more locations — `file:line`
- [ ] DRY-2: Every shared concept extracted to exactly one place — `file:line`
- [ ] SOLID-S: Each class/function has one reason to change — `file:line`
- [ ] SOLID-O: New behavior added by extension, no existing class body edited — `file:line` or N/A
- [ ] SOLID-L: Every subtype fully substitutable; no narrowed contract or surprise raise — `file:line` or N/A
- [ ] SOLID-I: No Protocol/ABC forces an implementor to leave a method as `...` or raise — `file:line` or N/A
- [ ] SOLID-D: Domain classes depend on Protocols, not on I/O or framework imports directly — `file:line`
- [ ] OC-1: Max one indent level per method; inner blocks extracted to named helpers — deepest: `file:line`
- [ ] OC-2: No `else` after `return`; all branches return early and the happy path is flat — `file:line` or N/A
- [ ] OC-3: No bare `int`/`str`/`float` as domain concepts in public signatures; each wrapped in a named type — `file:line` or N/A
- [ ] OC-4: No bare `list[X]`/`set[X]` as domain values; each wrapped in a named collection class — `file:line` or N/A
- [ ] OC-5: No `a.b.c()` chains; each dot navigation step assigned to a named local — `file:line` or N/A
- [ ] OC-6: No abbreviations anywhere; every name is a full word readable without context — `file:line` or N/A
- [ ] OC-7: Every function ≤ 20 lines, every class ≤ 50 lines — longest: `file:line`
- [ ] OC-8: Every class has ≤ 2 `self.x` in `__init__`; if > 2 before this cycle, name the new value object extracted and cite `file:line` per class
- [ ] OC-9: No `get_x()`/`set_x()` pairs; state changes via commands, queries return values — `file:line` or N/A
- [ ] Semantic: test Given/When/Then operates at the same abstraction level as the AC — `file:line`
```

*For every item: check the box AND cite `file:line` evidence, or write `N/A` with a one-line reason. An unchecked box or missing evidence is an automatic REJECTED.*

Update `## Cycle State` Phase: `SELF-DECLARE`

## REVIEWER CHECK — Code Design Only

After each test goes green + refactor + self-declaration, **STOP** and request a reviewer check. The reviewer will read the `## Self-Declaration` block from `TODO.md` directly — point them to it.

**STOP — request a reviewer check of code design and semantic alignment.**
**WAIT for APPROVED before committing.**

The reviewer is scoped to **code design only** (not full Step 5):

**What the reviewer receives**: The developer's completed `## Self-Declaration` block in `TODO.md`, with `file:line` evidence for each rule.

**What the reviewer does**: Independently inspects the actual code for each rule the developer claimed compliant. The self-declaration is an audit target — the reviewer verifies claims, not just reads them.

**What the reviewer does NOT check** (deferred to Step 5):
- Lint compliance
- Pyright/type checking
- Coverage metrics
- Full test suite

The reviewer responds using this template:

```markdown
## Code-Design Check — @id:<hex>

| Rule | Developer Claims | Reviewer Verdict | Evidence |
|------|-----------------|------------------|----------|
| YAGNI | <summary> | PASS / FAIL | `file:line` or N/A |
| KISS | <summary> | PASS / FAIL | `file:line` or N/A |
| DRY | <summary> | PASS / FAIL | `file:line` or N/A |
| SOLID-S | <summary> | PASS / FAIL | `file:line` or N/A |
| SOLID-O | <summary> | PASS / FAIL | `file:line` or N/A |
| SOLID-L | <summary> | PASS / FAIL | `file:line` or N/A |
| SOLID-I | <summary> | PASS / FAIL | `file:line` or N/A |
| SOLID-D | <summary> | PASS / FAIL | `file:line` or N/A |
| OC-1 thru OC-9 | <summary> | PASS / FAIL | `file:line` or N/A |
| Design patterns | <summary> | PASS / FAIL | `file:line` or N/A |
| Semantic alignment | <summary> | PASS / FAIL | `file:line` or N/A |

Decision: APPROVED / REJECTED
```

Any row where Reviewer Verdict = FAIL is a rejection. The reviewer must cite `file:line` evidence for every FAIL.

If REJECTED:
- Mark the `@id` row as `[~]` in TODO.md (do not downgrade to `[ ]`)
- Update `## Cycle State` Phase to `REVIEWER(code-design)`
- Fix the specific issues raised
- Do not commit
- Request re-review after fix

This is a **hard gate** — do not commit until APPROVED.

Update `## Cycle State` Phase: `REVIEWER(code-design)`

## COMMIT (after reviewer approval)

```bash
git add -A
git commit -m "feat(<feature-name>): implement <what this test covers>"
```

Update TODO.md:
- Mark the `@id` row `[x]` with ` — reviewer(code-design) APPROVED`
- Update `## Cycle State` Phase to `COMMITTED`
- Update `## Next` to the next failing test

Then move to the next failing test.

## Handling Spec Gaps

If during implementation you discover a behavior not covered by existing acceptance criteria:
- **Do not extend criteria yourself** — escalate to the PO
- Note the gap in TODO.md under `## Next`
- The PO will decide whether to add a new Example to the `.feature` file

Extra tests in `tests/unit/` are allowed freely (coverage, edge cases, etc.) — these do not need `@id` traceability. **Every test in `tests/unit/` must be a Hypothesis property test: `@given` is required, `@pytest.mark.slow` is mandatory, plain `assert` tests without `@given` are forbidden.**

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
        """Validate the email format on creation."""
        if "@" not in self.value:
            raise ValueError(f"Invalid email: {self.value!r}")

class UserRepository(Protocol):
    """Persistence interface for users."""

    def save(self, user: "User") -> None: ...
    def find_by_email(self, email: EmailAddress) -> "User | None": ...
```

## Self-Verification Before Handoff

After all tests are green and every per-test cycle has been committed with reviewer approval, complete these final checks before handing off to the reviewer for full Step 5 verification.

**Manual verification**: Run the app and verify it does what the AC says, not just what the tests check.

**Production-grade check**: If you change an input, does the output change accordingly? If any output is static regardless of input, the implementation is not complete.

**Developer pre-mortem**: In 2-3 sentences, answer: "If this feature shipped but was broken for the user, what would be the most likely reason?" Include this in the handoff message.

**Quality tooling** — run all four, all must pass:

```bash
uv run task lint
uv run task static-check
uv run task test
timeout 10s uv run task run
```

Do not hand off broken work. These are the only commands that run at handoff — the Design Self-Declaration was already completed and verified per-test during each REFACTOR cycle.
