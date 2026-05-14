---
name: write-test
description: "Write a failing test body for one BDD example"
---

# Write Test

Available knowledge: [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]]. `in` artifacts: read all before starting work.

1. Pick the next test function with an `...` (Ellipsis) body from the auto-generated test stubs: prefer tests within the same Rule file before moving to the next Rule, and order by fewest dependencies first per [[software-craft/tdd#concepts]]. pytest-beehave creates stubs with `test_<scenario_title_slug>` naming and `...` bodies (auto-skipped during collection). IF the Example belongs to a structural (invariant) Rule → also generate a Hypothesis property test in `tests/unit/` per [[software-craft/test-design#concepts]], using the counterexamples surfaced by the behavior pre-mortem per [[requirements/pre-mortem#concepts]].
2. Write a failing test that specifies the expected behavior per [[software-craft/tdd#key-takeaways]]. Replace the `...` body with the test implementation. The test function name (derived from the Example title) is immutable — it is the traceability link maintained by pytest-beehave.
3. IF a spec gap or inconsistency is discovered → do NOT modify specification documents (domain_model.md, glossary.md, product_definition.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
4. Run `task test-fast` to confirm the test fails for the right reason (RED) per [[software-craft/tdd#key-takeaways]].
