---
name: implementation
description: Step 4 — Red-Green-Refactor cycle, one test at a time, with commit per green test
version: "2.0"
author: developer
audience: developer
workflow: feature-lifecycle
---

# Implementation

Make the failing tests pass one at a time. Each green test gets its own commit after reviewer approval. Refactor only after tests are green.

## Developer Quality Gate Priority Order

During Step 4, correctness priorities are (in order):

1. **Design correctness** — YAGNI, KISS, DRY, SOLID, Object Calisthenics, appropriate design patterns
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
  ─── STOP ─── do not proceed until reviewer checks ───
  → REVIEWER CHECK: reviewer verifies code design + semantic alignment
  ─── WAIT for APPROVED ───
  → COMMIT (only after reviewer APPROVED)
  → pick next failing test
```

**Hard gates**: The cycle has two hard gates — you must STOP before the reviewer check, and WAIT for APPROVED before committing. Never batch multiple tests before a reviewer interaction. Never commit without reviewer approval.

Never write production code before picking a specific failing test. Never refactor while tests are red.

## Step 2 — Architecture (do this first)

Before writing any production code, add `## Architecture` to `docs/features/in-progress/<name>/discovery.md`:

1. Move the feature folder from `backlog/` to `in-progress/`:
   ```bash
   mv docs/features/backlog/<name>/ docs/features/in-progress/<name>/
   ```
2. Read both `docs/features/discovery.md` (project-level) and the feature's `discovery.md`
3. Run a silent pre-mortem: design patterns, SOLID, DRY, KISS, Object Calisthenics
4. Add the Architecture section:

```markdown
## Architecture

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

5. **Architecture contradiction check**: Compare each ADR against each AC. If any architectural decision contradicts or circumvents an acceptance criterion, flag it and resolve with the PO before writing any production code.
6. If a user story is not technically feasible, escalate to the PO.
7. If any build changes need PO approval, stop and ask before proceeding.

Commit: `feat(<feature-name>): add architecture`

## Implementation Order

1. Start with the simplest test: data classes, value objects, pure functions
2. Work outward: state machines, I/O, orchestration
3. Follow the order of acceptance criteria in the `.feature` files

## RED — Confirm the Test Fails

```bash
uv run pytest tests/features/<name>/<story>_test.py::test_<func> -v
```

Expected: `FAILED` or `ERROR`. If it passes before you've written code, the test is wrong — fix it.

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

## REFACTOR — Apply Principles (in priority order)

1. **DRY**: extract duplication
2. **SOLID**: split classes that have grown beyond one responsibility
3. **Object Calisthenics** (enforce all 9 rules):
   1. One level of indentation per method — extract inner blocks to helpers
   2. No `else` after `return` — return early, flatten the happy path
   3. Wrap all primitives — `EmailAddress(str)` not raw `str` for domain concepts
   4. First-class collections — wrap `list[User]` in a `UserList` class
   5. One dot per line — `user.address` then `address.city`, never `user.address.city`
   6. No abbreviations — `calculate` not `calc`, `manager` not `mgr`
   7. Small entities — functions ≤ 20 lines, classes ≤ 50 lines
   8. ≤ 2 instance variables — extract to value objects or split the class
   9. No getters/setters — use commands (`activate()`) and queries (`is_active()`)
4. **Type hints**: add/fix type annotations on all public functions and classes
5. **Docstrings**: Google-style on all public functions and classes

### Refactor Self-Check Gates

After refactor, before requesting reviewer check:

| If you see... | Then you must... | Before committing |
|---|---|---|
| Function > 20 lines | Extract helper | Verify line count |
| Nesting > 2 levels | Extract to function | Verify max depth |
| Bare `int`/`str` as domain concept | Wrap in value object | Verify no raw primitives in signatures |
| > 4 positional parameters | Group into dataclass | Verify parameter count |
| `list[X]` as domain collection | Wrap in collection class | Verify no bare lists |

### Design Pattern Decision Table

Use when a pattern solves a structural problem you already have:

| If your code has... | Consider... | Why |
|---|---|---|
| Multiple `if/elif` branches on type/state | State or Strategy pattern | Eliminates conditional complexity |
| Constructor that does complex setup | Factory or Builder | Separates construction from use |
| Multiple components that must work together | Facade | Single entry point reduces coupling |
| External dependency (I/O, DB, network) | Repository/Adapter pattern | Enables testing via Protocol |
| Event-driven flow | Observer or pub/sub | Decouples producers from consumers |

> **Note**: `uv run task test` runs `--doctest-modules`. Keep `Examples:` blocks in Google-style docstrings valid and executable.

```bash
uv run task test-fast     # must still pass — the ONLY check during refactor
```

Do NOT run `uv run task lint` or `uv run task static-check` during the cycle. Those are handoff-only checks (before Step 5).

## REVIEWER CHECK — Code Design Only

After each test goes green + refactor, **STOP** and request a reviewer check. The reviewer loads the `verify` skill but is scoped to **code design only**:

**What the reviewer checks (code-design scope)**:
- **YAGNI, KISS, DRY, SOLID, Object Calisthenics** — are design principles followed in priority order?
- **Appropriate design patterns** — is the code structure right for the problem?
- **Semantic alignment** — does the test operate at the same abstraction level as the AC?
- **No internal-state testing** — assertions on observable behavior, not private attributes

**What the reviewer does NOT check** (deferred to Step 5):
- Lint compliance
- Pyright/type checking
- Coverage metrics
- Full test suite

The reviewer responds with **APPROVED** or **REJECTED** with specific issues. If REJECTED, fix the issues and request review again. This is a **hard gate** — do not commit until APPROVED.

## COMMIT (after reviewer approval)

```bash
git add -A
git commit -m "feat(<feature-name>): implement <what this test covers>"
```

Then move to the next failing test.

## Handling Spec Gaps

If during implementation you discover a behavior not covered by existing acceptance criteria:
- **Do not extend criteria yourself** — escalate to the PO
- Note the gap in TODO.md under `## Next`
- The PO will decide whether to add a new Example to the `.feature` file

Extra tests in `tests/unit/` are allowed freely (coverage, edge cases, etc.) — these do not need `@id` traceability.

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

After all tests are green, before telling the reviewer you are ready for full Step 5 review:

```bash
uv run task lint                # exit 0
uv run task static-check        # exit 0, 0 errors
uv run task test                # exit 0, all pass, coverage 100%
timeout 10s uv run task run     # exit non-124; exit 124 = hung process = fix it
```

All four must pass. Do not hand off broken work.

**Manual verification**: Run the app and verify it does what the AC says, not just what the tests check.

**Production-grade check**: If you change an input, does the output change accordingly? If any output is static regardless of input, the implementation is not complete.

**Developer pre-mortem**: In 2-3 sentences, answer: "If this feature shipped but was broken for the user, what would be the most likely reason?" Include this in the handoff message.
