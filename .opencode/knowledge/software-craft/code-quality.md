---
domain: software-craft
tags: [code-quality, linting, type-checking, review-standards]
last-updated: 2026-04-26
---

# Code Quality Standards

## Key Takeaways

- Design correctness (YAGNI > KISS > DRY > SOLID > OC > patterns) outweighs lint and type compliance.
- Enforce size limits: functions ≤20 lines, classes ≤50 lines, max 2 levels of nesting, ≤2 instance variables per behavioural class.
- Tests must operate at the same abstraction level as their acceptance criteria (semantic alignment).
- Quality gates run in order: design correctness, then one test green, then lint/typecheck/coverage at handoff.

## Concepts

**Design Correctness Priority**: YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

**Size Limits and Enforcement**: Functions must be ≤20 lines (code lines only, excluding docstrings). Classes must be ≤50 lines. Maximum nesting is 2 levels. Instance variables are ≤2 per class (dataclasses, Pydantic models, value objects, and TypedDicts are exempt). These limits are enforced during the TDD loop and at handoff.

**Semantic Alignment**: Tests must operate at the same abstraction level as the acceptance criteria they cover. If the criterion is about user-facing behaviour, the test should test user-facing behaviour — not implementation details.

**Quality Gate Priority Order**: During Step 3 (TDD Loop) and before handoff to Step 4: first verify design correctness (YAGNI through patterns), then verify one test is green (the specific test plus `test-fast` still passes), then run quality tooling (`lint`, `static-check`, full `test` with coverage).

## Content

### Principles (Priority Order)

YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code

Design correctness is far more important than lint/pyright/coverage compliance. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

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

### Quality Gate Priority Order

During Step 3 (TDD Loop) and before handoff to Step 4:

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code
2. **One test green** — the specific test under work passes, plus `test-fast` still passes
3. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run at handoff to SA

## Related

- [[software-craft/solid]]
- [[software-craft/object-calisthenics]]
- [[software-craft/verification-philosophy]]
- [[software-craft/test-design]]