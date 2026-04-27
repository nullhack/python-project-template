---
domain: software-craft
tags: [code-quality, linting, type-checking, review-standards]
last-updated: 2026-04-27
---

# Code Quality Standards

## Key Takeaways

- Design correctness (YAGNI > KISS > DRY > SOLID > OC > patterns) outweighs lint and type compliance.
- Enforce size limits: functions ≤20 lines, classes ≤50 lines, max 2 levels of nesting, ≤2 instance variables per behavioural class.
- Tests must operate at the same abstraction level as their acceptance criteria (semantic alignment).
- The two-phase quality gate enforces design-first: design correctness is verified at Step 4 before coverage and cosmetic tooling are checked at Step 4B.

## Concepts

**Design Correctness Priority**: YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

**Size Limits and Enforcement**: Functions must be ≤20 lines (code lines only, excluding docstrings). Classes must be ≤50 lines. Maximum nesting is 2 levels. Instance variables are ≤2 per class (dataclasses, Pydantic models, value objects, and TypedDicts are exempt). These limits are enforced during Step 3A (design review) and at Step 4B (completion verification).

**Semantic Alignment**: Tests must operate at the same abstraction level as the acceptance criteria they cover. If the criterion is about user-facing behaviour, the test should test user-facing behaviour — not implementation details.

**Two-Phase Quality Gate**: Quality is enforced in two separate phases to avoid wasting effort on code that might be redesigned:
- **Phase 1 (Step 3A → Step 4)**: Design correctness — YAGNI through patterns, verified by `test-fast` and feature-type run. No lint, coverage, or type checking during this phase.
- **Phase 2 (Step 3B → Step 4B)**: Cosmetic tooling — coverage threshold, lint, pyright, docstrings. Only run after design is approved.

## Content

### Principles (Priority Order)

YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code

Design correctness is far more important than lint/pyright/coverage compliance. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

### Two-Phase Quality Gate

Step 3A → Step 4 (Design Verification):

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > OC > patterns
2. **One test green** — the specific test passes, plus `test-fast` still passes
3. **Feature-type run** — CLI/Library/Mixed verification that the app or module works
4. **SA design review** — adversarial review of design claims

Step 3B → Step 4B (Completion Verification):

5. **Coverage threshold** — `test-coverage` meets configured threshold
6. **Lint** — `ruff check` and `ruff format` pass
7. **Type checking** — `pyright` exits 0
8. **SA completion review** — re-run commands independently, verify coverage

### Automated Checks

- **Linting**: ruff format, ruff check, Google docstring convention, `noqa` forbidden
- **Type checking**: pyright, 0 errors required
- **Coverage**: enforced by `test-coverage`

### Size Limits

- **Function length**: ≤ 20 lines (code lines only, excluding docstrings)
- **Class length**: ≤ 50 lines (code lines only, excluding docstrings)
- **Max nesting**: 2 levels
- **Instance variables**: ≤ 2 per class (exception: dataclasses, Pydantic models, value objects, and TypedDicts are exempt — they may carry as many fields as the domain requires)

### Semantic Alignment

Tests must operate at the same abstraction level as the acceptance criteria they cover. If the criterion is about user-facing behaviour, the test should test user-facing behaviour — not implementation details.

### Feature-Type Verification

Not all features have a CLI entry point. Choose the appropriate verification:

| Feature Type | How to Verify |
|---|---|
| CLI | `timeout 10s uv run task run` — app exits cleanly (0 or non-124), output changes with input |
| Library | `uv run python -c "import <package>; <public_api_call>"` — module imports, API callable |
| Mixed | Both CLI and library checks |

## Related

- [[software-craft/solid]]
- [[software-craft/object-calisthenics]]
- [[software-craft/verification-philosophy]]
- [[software-craft/test-design]]