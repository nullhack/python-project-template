---
name: implementation
description: Step 4 — Red-Green-Refactor cycle, one test at a time, with commit per green test
version: "1.0"
author: developer
audience: developer
workflow: feature-lifecycle
---

# Implementation

Make the failing tests pass one at a time. Each green test gets its own commit. Refactor only after tests are green.

## The Cycle

```
Pick one failing test
  → RED: confirm it fails
  → GREEN: write the minimum code to make it pass
  → REFACTOR: clean up, apply principles
  → COMMIT
  → pick next failing test
```

Never write production code before picking a specific failing test. Never refactor while tests are red.

## Implementation Order

1. Start with the simplest test: data classes, value objects, pure functions
2. Work outward: state machines, I/O, orchestration
3. Follow the order of acceptance criteria in the feature doc

## Architecture Section (do this first, then verify against AC)

Before writing any production code, add `## Architecture` to `docs/features/in-progress/<name>.md`:

```markdown
## Architecture

### Module Structure
- `<package>/domain/entity.py` — data classes and value objects
- `<package>/domain/service.py` — business logic
- `<package>/storage/repository.py` — persistence interface

### Key Decisions
ADR-001: <title>
Decision: <what>
Reason: <why in one sentence>
Alternatives considered: <what was rejected and why>

### Build Changes (needs PO approval: yes/no)
- New runtime dependency: <name> — reason: <why>
- New package in pyproject.toml packages list: <name>
- Changed entry point: <old> → <new>
```

If any build changes need PO approval, stop and ask before proceeding.

**Architecture contradiction check**: After writing the Architecture section, compare each ADR against each AC. If any architectural decision contradicts or circumvents an acceptance criterion (e.g., "demo-first" vs. "when the user presses W"), flag it and resolve with the PO before writing any production code. This is not optional.

## Signature Design

Design signatures before writing bodies. Use Python protocols for abstractions:

```python
from typing import Protocol
from dataclasses import dataclass

# Value objects: frozen + slots
@dataclass(frozen=True, slots=True)
class EmailAddress:
    """A validated email address."""

    value: str

    def __post_init__(self) -> None:
        """Validate the email format on creation."""
        if "@" not in self.value:
            raise ValueError(f"Invalid email: {self.value!r}")

# Protocol for dependency inversion
class UserRepository(Protocol):
    """Persistence interface for users."""

    def save(self, user: "User") -> None: ...
    def find_by_email(self, email: EmailAddress) -> "User | None": ...

# Google docstrings on all public functions
def register_user(email: EmailAddress, repo: UserRepository) -> "User":
    """Register a new user with the given email address.

    Args:
        email: The validated email address for the new user.
        repo: Repository for persisting the user.

    Returns:
        The newly created and persisted user.

    Raises:
        DuplicateEmailError: If the email is already registered.
    """
```

## RED — Confirm the Test Fails

```bash
uv run pytest tests/<file>_test.py::test_<name> -v
```

Expected: `FAILED` or `ERROR`. If it passes before you've written code, the test is wrong — fix it.

## GREEN — Minimum Implementation

Write the least code that makes the test pass. Apply during GREEN:
- **YAGNI**: if the test doesn't require it, don't write it
- **KISS**: the simplest code that passes

Do NOT apply during GREEN: DRY, SOLID, Object Calisthenics — those come in refactor.

```bash
uv run pytest tests/<file>_test.py::test_<name> -v   # must be PASSED
uv run task test                                      # must all still pass
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

After refactor, before committing, run through this table. Each row is a mandatory check:

| If you see... | Then you must... | Before committing |
|---|---|---|
| Function > 20 lines | Extract helper | Verify line count |
| Nesting > 2 levels | Extract to function | Verify max depth |
| Bare `int`/`str` as domain concept | Wrap in value object | Verify no raw primitives in signatures |
| > 4 positional parameters | Group into dataclass | Verify parameter count |
| `list[X]` as domain collection | Wrap in collection class | Verify no bare lists |
| No classes in domain code | Reconsider — are you writing procedural code? | Verify at least one domain class exists |

### Design Pattern Decision Table

Not "use patterns everywhere" — use when a pattern solves a structural problem you already have:

| If your code has... | Consider... | Why |
|---|---|---|
| Multiple `if/elif` branches on type/state | State or Strategy pattern | Eliminates conditional complexity |
| Constructor that does complex setup | Factory or Builder | Separates construction from use |
| Multiple components that must work together | Facade | Single entry point reduces coupling |
| External dependency (I/O, DB, network) | Repository/Adapter pattern | Enables testing via Protocol |
| Event-driven flow | Observer or pub/sub | Decouples producers from consumers |

> **Note**: `uv run task test` runs `--doctest-modules`, which executes code examples embedded in source docstrings. Keep `Examples:` blocks in Google-style docstrings valid and executable. If an example should not be run, mark it with `# doctest: +SKIP`.

```bash
uv run task test          # must still pass
uv run task lint          # must exit 0
uv run task static-check  # must exit 0
```

## COMMIT

```bash
git add -A
git commit -m "feat(<feature-name>): implement <what this test covers>"
```

Then move to the next failing test.

## Self-Verification Before Handoff

After all tests are green, before telling the reviewer you are ready:

```bash
uv run task lint                # exit 0
uv run task static-check        # exit 0, 0 errors
uv run task test                # exit 0, all pass, coverage 100%
timeout 10s uv run task run     # exit non-124; exit 124 = hung process = fix it
```

All four must pass. Do not hand off broken work.

**Manual verification**: After all four commands pass, run the app and manually verify it does what the AC says, not just what the tests check. If the feature involves user interaction, interact with it yourself.

**Production-grade check**: Before handing off, answer honestly: if you change an input, does the output change accordingly? If any output is static regardless of input, the implementation is not complete — fix it before handing off. The reviewer will verify this by running the app and changing an input.

**Developer pre-mortem** (write this before handing off to reviewer): In 2–3 sentences, answer: "If this feature shipped but was broken for the user, what would be the most likely reason?" Include this in the handoff message or as a `## Pre-mortem` subsection in the feature doc's Architecture section.
