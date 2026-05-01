---
name: write-test
description: "Write a failing test body for one BDD example"
---

# Write Test

Load [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], and [[software-craft/solid]] before starting. 

1. Pick the next unimplemented `@id` from the feature file — order by fewest dependencies first per [[software-craft/tdd#concepts]].
2. Write a failing test that specifies the expected behavior per [[software-craft/tdd#key-takeaways]].
3. IF a spec gap or inconsistency is discovered → do NOT modify specification documents (domain_model.md, technical_design.md, glossary.md, product_definition.md, system.md, context_map.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
4. Run `task test-fast` to confirm the test fails for the right reason (RED) per [[software-craft/tdd#key-takeaways]].
5. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.