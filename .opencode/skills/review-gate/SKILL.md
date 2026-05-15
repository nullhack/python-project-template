---
name: review-gate
description: "Two-tier review with fail-fast: design -> structure"
---

# Review Gate

Available knowledge: [[software-craft/code-review]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[architecture/reconciliation#key-takeaways]]. `in` artifacts: read all before starting work.

**Fail-fast rule**: Stop at first failure in any tier. Do NOT proceed to next tier if current tier fails.

## Tier 1: Design Review

1. Verify implementation aligns with domain spec per [[software-craft/code-review#concepts]]: entities match domain spec, value objects enforce invariants, use cases follow aggregate boundaries.
2. Verify implementation aligns with architectural decisions per [[software-craft/code-review#concepts]]: ADR compliance, quality attributes met.
3. Verify all `# Constraints:` in the .feature file are met in the implementation. For technology constraints, read domain_spec.md `### Technology Requirements` table and execute the Verification instruction for each row (grep imports, check file existence, inspect config). Zero evidence → FAIL. For quality attribute constraints, verify thresholds are enforced.
4. Verify implementation aligns with feature specification: all Examples have corresponding test implementations, behavior matches Gherkin steps.
5. Verify design principles adversarially per [[software-craft/tdd#key-takeaways]] priority order (YAGNI > KISS > DRY > ObjCal > Smells > SOLID > patterns):
   - **YAGNI**: No premature abstractions, no speculative generalization, no code without an exercising test.
   - **KISS**: No unnecessary complexity or over-engineering when a simpler solution exists.
   - **DRY**: No duplicated logic, unless the duplication is simpler than the wrong abstraction (KISS overrides DRY).
   - **ObjCal**: Load [[software-craft/object-calisthenics#key-takeaways]] — check 9 rules: one level of indentation, no `else`, wrapped primitives, one dot per line, no abbreviations, small entities, ≤2 instance variables, first-class collections, no getters/setters.
   - **Smells**: Load [[software-craft/smell-catalogue#key-takeaways]] — check for bloaters, OO abusers, change preventers, dispensables, couplers.
   - **SOLID**: Load [[software-craft/solid#key-takeaways]] — check SRP, OCP, LSP, ISP, DIP violations.
   - **Patterns**: Verify every design pattern is driven by a smell. Patterns without a motivating smell violate YAGNI.
6. **FAIL-FAST**: If any design violations found → exit `fail` with specific citations (file:line). Do NOT proceed to structure review.

## Tier 2: Structure Review

7. Verify structural traceability: run `beehave check` to confirm every Example in the feature file has a corresponding test and there are no orphan tests. pytest-beehave enforces this via title-based mapping.
8. Verify test quality per [[software-craft/test-design#concepts]]: tests follow AAA pattern, clear assertions, behavior-focused not implementation-coupled.
9. Run `task test` and verify all tests pass with coverage.
10. Run `ruff check .` and verify no functional lint violations (the default ruff config only includes bug-catching rules).
11. **FAIL-FAST**: If any structure violations found → exit `fail` with specific citations.
