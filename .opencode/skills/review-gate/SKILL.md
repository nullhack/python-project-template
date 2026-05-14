---
name: review-gate
description: "Three-tier review with fail-fast: design -> structure -> conventions"
---

# Review Gate

Available knowledge: [[software-craft/code-review]], [[software-craft/test-design]], [[software-craft/smell-catalogue]]. `in` artifacts: read all before starting work.

**Fail-fast rule**: Stop at first failure in any tier. Do NOT proceed to next tier if current tier fails.

## Tier 1: Design Review

1. Verify implementation aligns with domain model per [[software-craft/code-review#concepts]]: entities match domain model, value objects enforce invariants, use cases follow aggregate boundaries.
2. Verify implementation aligns with architectural decisions per [[software-craft/code-review#concepts]]: ADR compliance, quality attributes met.
3. Verify implementation aligns with feature specification: all Examples have corresponding test implementations, behavior matches Gherkin steps.
4. **FAIL-FAST**: If any design violations found → exit `fail` with specific citations (file:line). Do NOT proceed to structure review.

## Tier 2: Structure Review

5. Verify structural traceability: run `beehave check` to confirm every Example in the feature file has a corresponding test and there are no orphan tests. pytest-beehave enforces this via title-based mapping.
6. Verify test quality per [[software-craft/test-design#concepts]]: tests follow AAA pattern, clear assertions, behavior-focused not implementation-coupled.
7. Run `task test-coverage` and verify coverage meets project standards.
8. **FAIL-FAST**: If any structure violations found → exit `fail` with specific citations. Do NOT proceed to conventions review.

## Tier 3: Conventions Review

9. Run `ruff check .` and verify no lint violations.
10. Run `ruff format --check .` and verify formatting compliance.
11. Verify all functions have Google-style docstrings per project standards.
12. Verify all public interfaces have complete type hints and pass pyright checks.
13. **FAIL-FAST**: If any convention violations found → exit `fail` with specific citations.
