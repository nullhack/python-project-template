---
name: verify-traceability
description: "Verify 1-1 correspondence between @id tags in the feature file and test functions in tests/features/"
---

# Verify Traceability

Load [[software-craft/test-design#key-takeaways]] and [[requirements/gherkin#key-takeaways]] before starting. 

1. Extract all `@id` tags from the feature file.
2. Extract all test function names from `tests/features/<feature_slug>/`.
3. Check 1-1 correspondence per [[software-craft/test-design#concepts]]:
   - IF an `@id` tag has no corresponding test function → MISSING TEST: feature is not done. List the orphan `@id` tags.
   - IF a test function in `tests/features/` has no corresponding `@id` tag → ORPHAN TEST: belongs in `tests/unit/`, not `tests/features/`. List the orphan test functions.
   - IF all `@id` tags map to exactly one test function → traceability is complete.
4. Verify semantic depth per [[software-craft/test-design#concepts]] — for each `@id` example that describes a user-facing command or API invocation, verify the corresponding test exercises the entry point described in the acceptance criterion (e.g., command handler, API endpoint), not just the domain logic in isolation. A test that calls domain methods directly when the AC describes a user-facing command is a semantic alignment gap — it has structural traceability but wrong semantic depth.
5. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.