---
name: review-structure
description: "Verify test coverage, test quality, and behavior-vs-implementation coupling"
---

# Review Structure

Available knowledge: [[software-craft/test-design]], [[software-craft/tdd]], [[software-craft/code-review]]. `in` artifacts: discover and read on demand as needed. 

1. This review tier checks test quality and coverage ONLY. Do not flag lint, docstring, or naming issues — those belong to conventions review.
2. Declare adversarial stance per [[software-craft/code-review#concepts]] — default hypothesis: "tests might be coupled to the wrong thing."
3. Verify tests specify observable behaviour, not implementation details, per [[software-craft/test-design#key-takeaways]].
4. IF a test breaks when refactoring preserves behaviour → flag it as implementation-coupled per [[software-craft/test-design#concepts]].
5. Verify each @id test exercises the entry point described in its acceptance criterion per [[software-craft/test-design#key-takeaways]]. If the AC describes a user-facing command with flags, the test must pass those flags through the command handler — not call domain methods directly. Domain-layer stubs test domain logic, but they don't verify that command flags reach the domain.
6. Run `task test-coverage` to verify test coverage meets the project threshold.
7. Verify @id-to-test traceability — every @id in the feature file must have exactly one test in tests/features/<feature_slug>/, and every test in tests/features/ must trace back to an @id. Missing tests → REJECT (feature not done). Orphan tests in tests/features/ → REJECT (move to tests/unit/).
8. Stop at the first failure per [[software-craft/code-review#key-takeaways]] — write a minimal REJECTED report with file:line evidence.
9. When flagging issues, include file:line references — e.g., "test_login.py:45 tests domain method directly instead of command handler". Vague findings create rework.
10. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
11. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.