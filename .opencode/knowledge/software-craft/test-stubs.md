---
domain: software-craft
tags: [test-stubs, traceability]
last-updated: 2026-05-08
---

# Test Stubs

## Key Takeaways

- Every `@id` tag in the feature file must have a corresponding test stub; traceability is verified at baseline.
- Test stubs follow the project template: one-line description of what the example proves, blank line, Gherkin steps (`test_<feature_stem>_<id>` naming, `raise NotImplementedError` body, skip decorator, no MoSCoW tags).

## Concepts

**@id Traceability Chain**. Each `@id` tag in the feature file produces one test stub at `tests/features/<feature_slug>/<rule_slug>_test.py` with a function named `test_<feature_stem>_<id>`. The `stubs-traceable` condition on the `create-py-stubs.done` transition verifies that `all-ids-have-stubs: ==verified`. This ensures no acceptance criterion is lost between planning and implementation.

**Test Stub Format**. Every test stub follows the project's test stub template (located in `.templates/`). The format requires:
- Decorated with `@pytest.mark.skip(reason="not yet implemented")`, never use `...` ellipsis bodies
- Docstring begins with a one-line description of what this specific example proves, followed by a blank line, then the Gherkin steps (Given/When/Then) for traceability
- Body is `raise NotImplementedError`, so the test fails explicitly if the skip decorator is removed prematurely
- Function name follows `test_<feature_stem>_<id>` naming convention
- No MoSCoW tags or priority labels anywhere in the stub

## Related

- [[requirements/gherkin]]: @id tag format and traceability convention
- [[software-craft/source-stubs]]: typed source stubs and scaffolding order
