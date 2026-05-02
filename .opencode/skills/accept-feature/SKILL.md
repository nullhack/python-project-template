---
name: accept-feature
description: "Validate business behavior against BDD scenarios from the end user's perspective"
---

# Accept Feature

Available knowledge: [[requirements/gherkin#key-takeaways]], [[software-craft/test-design#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Run `task test-build` to verify all tests pass with coverage.
2. Verify all BDD scenarios pass from the end user's perspective, not the test harness, per [[software-craft/test-design#key-takeaways]].
3. IF a scenario passes in the test harness but fails from the user's perspective → flag it as a semantic alignment gap per [[software-craft/test-design#concepts]].
4. Verify @id-to-test traceability — every @id in the feature file must have exactly one test in tests/features/<feature_slug>/, and every test in tests/features/ must trace back to an @id. Missing @id tests → feature is not done. Orphan tests in tests/features/ → must move to tests/unit/.
5. Verify semantic depth — for each @id that describes a user-facing command or API invocation, verify the test exercises the command/API handler, not just domain logic. Tests that bypass the entry point described in the acceptance criterion have structural traceability but wrong semantic depth per [[software-craft/test-design#concepts]].
6. Verify quality attributes are met.
7. Verify definition of done criteria are satisfied.
8. Verify every stakeholder Q&A from interview notes maps to either a passing @id test or an explicit stakeholder deferral. Untraced requirements = incomplete delivery.
9. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
10. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.