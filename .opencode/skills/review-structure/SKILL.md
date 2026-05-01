---
name: review-structure
description: "Verify test coverage, test quality, and behavior-vs-implementation coupling"
---

# Review Structure

Load [[software-craft/test-design]], [[software-craft/tdd]], and [[software-craft/code-review]] before starting. 

1. Declare adversarial stance per [[software-craft/code-review#concepts]] — default hypothesis: "tests might be coupled to the wrong thing."
2. Verify tests specify observable behaviour, not implementation details, per [[software-craft/test-design#key-takeaways]].
3. IF a test breaks when refactoring preserves behaviour → flag it as implementation-coupled per [[software-craft/test-design#concepts]].
4. Verify each @id test exercises the entry point described in its acceptance criterion per [[software-craft/test-design#key-takeaways]]. If the AC describes a user-facing command with flags, the test must pass those flags through the command handler — not call domain methods directly. Domain-layer stubs test domain logic, but they don't verify that command flags reach the domain.
5. Run `task test-coverage` to verify test coverage meets the project threshold.
6. Verify @id-to-test traceability — every @id in the feature file must have exactly one test in tests/features/<feature_slug>/, and every test in tests/features/ must trace back to an @id. Missing tests → REJECT (feature not done). Orphan tests in tests/features/ → REJECT (move to tests/unit/).
7. Stop at the first failure per [[software-craft/code-review#key-takeaways]] — write a minimal REJECTED report with file:line evidence.
8. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
9. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.