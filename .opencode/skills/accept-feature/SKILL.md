---
name: accept-feature
description: "Validate business behavior against BDD scenarios from the end user's perspective"
---

# Accept Feature

Available knowledge: [[requirements/gherkin#key-takeaways]], [[software-craft/test-design#key-takeaways]]. `in` artifacts: read all before starting work.

1. Run `task test-build` to verify all tests pass with coverage.
2. Verify all BDD scenarios pass from the end user's perspective, not the test harness, per [[software-craft/test-design#key-takeaways]].
3. IF a scenario passes in the test harness but fails from the user's perspective → flag it as a semantic alignment gap per [[software-craft/test-design#concepts]].
4. Verify structural traceability via `beehave check`: every Example in the feature file must have exactly one corresponding test function, and every test function must trace back to an Example. pytest-beehave enforces this via title-based mapping. Any violations reported by `beehave check` mean the feature is not done.
5. Verify semantic depth: for each Example that describes a user-facing command or API invocation, verify the test exercises the command/API handler, not just domain logic. Tests that bypass the entry point described in the acceptance criterion have structural traceability but wrong semantic depth per [[software-craft/test-design#concepts]].
6. Verify quality attributes are met.
7. Verify definition of done criteria are satisfied.
8. Verify every stakeholder Q&A from interview notes maps to either a passing test or an explicit stakeholder deferral. Produce a traceability matrix: for each Q&A topic, list the test function name (derived from the Example title) or the deferral reason. Untraced requirements = incomplete delivery.
