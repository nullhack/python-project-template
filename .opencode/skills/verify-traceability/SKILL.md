---
name: verify-traceability
description: "Verify example-to-test traceability via beehave check and semantic depth"
---

# Verify Traceability

Available knowledge: [[software-craft/test-design#key-takeaways]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work.

1. Run `beehave check` to verify structural traceability: every Example in the feature file has exactly one corresponding test function, and every test function traces back to an Example. pytest-beehave enforces this via title-based mapping (Example title → function name `test_<slug>`). `beehave check` reports: unmapped-scenario, unmapped-test, misplaced-test, missing-placeholder, missing-literal, example-mismatch.
2. IF `beehave check` reports any violations → traceability is incomplete. List the specific violations.
3. IF `beehave check` passes → structural traceability is complete.
4. Verify semantic depth per [[software-craft/test-design#concepts]]: for each Example that describes a user-facing command or API invocation, verify the corresponding test exercises the entry point described in the acceptance criterion (e.g., command handler, API endpoint), not just the domain logic in isolation. A test that calls domain methods directly when the AC describes a user-facing command is a semantic alignment gap: it has structural traceability but wrong semantic depth.
