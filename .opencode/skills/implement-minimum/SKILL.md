---
name: implement-minimum
description: "Write the minimum production code needed to make the failing test pass"
---

# Implement Minimum

Load [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], and [[software-craft/solid]] before starting. 

1. Write the minimum code to make the failing test pass AND satisfy reviewer checks per [[software-craft/tdd#key-takeaways]]. Add docstrings, type hints, and lint compliance only when reviewers require them — not proactively.
2. IF a spec gap or inconsistency is discovered during implementation → do NOT modify specification documents (domain_model.md, technical_design.md, glossary.md, product_definition.md, system.md, context_map.md, ADRs, feature files). These are owned by other flow states. Flag the gap in output notes. The SE may ONLY modify production code and test code.
3. Run `task test-fast` to confirm the test passes (GREEN).
4. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
5. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.