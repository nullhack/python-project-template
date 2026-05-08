---
name: write-test
description: "Write a failing test body for one BDD example"
---

# Write Test

Available knowledge: [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]]. `in` artifacts: read all before starting work. 

1. Pick the next unimplemented `@id` from the feature file: order by fewest dependencies first per [[software-craft/tdd#concepts]]. IF the `@id` belongs to a structural (invariant) Rule → also generate a Hypothesis property test in `tests/unit/` per [[software-craft/test-design#concepts]], using the counterexamples surfaced by the behavior pre-mortem per [[requirements/pre-mortem#concepts]].
2. Write a failing test that specifies the expected behavior per [[software-craft/tdd#key-takeaways]]. Preserve the full docstring from the test stub. The Gherkin steps (Given/When/Then) are immutable specification content for traceability and must not be removed, shortened, or reformatted.
3. IF a spec gap or inconsistency is discovered → do NOT modify specification documents (domain_model.md, glossary.md, product_definition.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
4. Run `task test-fast` to confirm the test fails for the right reason (RED) per [[software-craft/tdd#key-takeaways]].
