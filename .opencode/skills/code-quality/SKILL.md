---
name: code-quality
description: Enforce code quality using ruff, pytest coverage, and static type checking
version: "1.0"
author: developer
audience: developer
workflow: feature-lifecycle
---

# Code Quality

Run quality tools and interpret their output. All must pass before handing off to the reviewer.

## Commands

```bash
task lint                # ruff check + ruff format
task static-check        # pyright
task test                # pytest with coverage
timeout 10s task run     # application starts; exit 124 = hung = fix it
```

All four must pass before any step is considered complete. (`task run` passes if exit ≠ 124.)

## Ruff Configuration

The project uses a broad ruff rule set in `pyproject.toml`. Key rules:

| Category | Rules | What it checks |
|---|---|---|
| `A` | builtins | Shadowing built-in names |
| `ANN` | annotations | Missing type hints |
| `B` | bugbear | Likely bugs and design issues |
| `C9` | mccabe | Cyclomatic complexity > 10 |
| `D` | pydocstyle | Google-style docstrings |
| `E/W` | pycodestyle | Style violations |
| `F` | pyflakes | Unused imports, undefined names |
| `N` | pep8-naming | Naming conventions |
| `S` | bandit | Security issues |
| `SIM` | simplify | Simplifiable code patterns |
| `ANN` exempt in tests | — | No type hints required in test files |

**Golden rule: never use `noqa`.** Look up the rule at https://docs.astral.sh/ruff/rules/ and fix it properly.

### Common Fixes

```python
# ANN001: Missing type hint
def bad(name):           return f"Hello {name}"   # wrong
def good(name: str) -> str: return f"Hello {name}" # correct

# S101: assert in production code
assert data is not None              # wrong — raises AssertionError, skipped with -O
if data is None: raise ValueError()  # correct

# C901: function too complex — extract methods
# SIM: simplify conditions — use early returns
# ERA: eradicate — remove commented-out code
```

## Pyright Standards

```bash
task static-check
# Expected: 0 errors, 0 warnings
```

Requirements:
- All functions have type hints (args and return type)
- Use modern syntax: `list[str]` not `List[str]`, `str | None` not `Optional[str]`
- Protocol-based interfaces for dependency inversion
- Generic types with `TypeVar` where appropriate

```python
from typing import Protocol, TypeVar

T = TypeVar("T")

class Repository(Protocol[T]):
    def save(self, entity: T) -> None: ...
    def find_by_id(self, entity_id: str) -> T | None: ...
```

## Coverage Requirements

Coverage must be 100%. The `--cov=<package>` target must match the actual package directory.

```toml
# pyproject.toml — keep this aligned with your actual package name
test-report = "pytest --cov=<your-package> --cov-fail-under=100 ..."
```

If you have code that genuinely cannot be tested (e.g., `if __name__ == "__main__":`), use:
```python
if __name__ == "__main__":  # pragma: no cover
    main()
```

`pragma: no cover` is allowed only for entry point guards and platform-specific branches. Never for logic.

## Docstring Standards (Google style)

```python
def calculate_total(items: list[LineItem], discount: float = 0.0) -> float:
    """Calculate the total price after applying a discount.

    Args:
        items: Line items to sum.
        discount: Fractional discount to apply (0.0–1.0).

    Returns:
        Total price after discount, rounded to 2 decimal places.

    Raises:
        ValueError: If discount is not between 0.0 and 1.0.

    Example:
        >>> calculate_total([LineItem(price=10.0, qty=2)], discount=0.1)
        18.0
    """
```

Required on all public functions and classes. Not required on private helpers (`_name`).

## Complexity Limits

| Metric | Limit |
|---|---|
| Cyclomatic complexity | 10 |
| Function length | 20 lines |
| Class length | 50 lines |
| Max nesting | 2 levels |
| Instance variables | 2 per class |

If a function exceeds the limit, extract sub-functions. If a class exceeds the limit, split responsibilities.

## Structural Quality Checks

`lint`, `static-check`, and `test` verify **syntax-level** quality. They do NOT verify **design-level** quality (nesting depth, function length, value objects, design patterns). Both must pass.

Run through this table during refactor and before handoff:

| If you see... | Then you must... |
|---|---|
| Function > 20 lines | Extract helper |
| Nesting > 2 levels | Extract to function |
| Bare `int`/`str` as domain concept | Wrap in value object |
| > 4 positional parameters | Group into dataclass |
| `list[X]` as domain collection | Wrap in collection class |
| No classes in domain code | Introduce domain classes |

## Design Anti-Pattern Recognition

| Code smell | Indicates | Fix |
|---|---|---|
| 15+ functions, 0 classes | Procedural code disguised as modules | Introduce domain classes |
| 8+ parameters on a function | Missing abstraction | Group into dataclass/value object |
| Type alias (`X = int`) instead of value object | Primitive obsession | Wrap in frozen dataclass |
| 3+ nesting levels | Missing extraction | Extract to helper functions |
| `get_x()` / `set_x()` pairs | Anemic domain model | Replace with commands and queries |

## Pre-Handoff Checklist

- [ ] `task lint` exits 0, no auto-fixes needed
- [ ] `task static-check` exits 0, 0 errors, 0 warnings
- [ ] `task test` exits 0, all tests pass, coverage = 100%
- [ ] `task run` starts without error
- [ ] No `noqa` comments in source
- [ ] No `type: ignore` comments
- [ ] All public functions have type hints and docstrings
- [ ] `pyproject.toml` version matches `<package>/__version__`
- [ ] `--cov=<package>` matches actual package name
