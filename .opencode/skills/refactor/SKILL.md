---
name: refactor
description: "Improve code structure while keeping all tests passing, then cycle to the next example or exit"
---

# Refactor

Load [[software-craft/tdd]], [[software-craft/refactoring]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]], and [[software-craft/refactoring-techniques]] before starting. 

1. Review the code for improvement opportunities while keeping all tests passing per [[software-craft/tdd#concepts]].
2. Refactor only if there is a test that would break if the refactoring is wrong per [[software-craft/tdd#key-takeaways]].
3. Apply small steps: one refactoring at a time, tests green after each step, no new functionality per [[software-craft/refactoring#key-takeaways]].
4. Apply design-only transformations per [[software-craft/tdd#concepts]] — YAGNI > KISS > DRY > OC > SOLID > patterns. Do not apply convention compliance (docstrings, type hints, import ordering, format changes) — those belong in the Conventions Phase.
5. IF a class has >2 instance variables → split per [[software-craft/object-calisthenics#key-takeaways]].
6. IF a method uses `else` → replace with early return or guard clause per [[software-craft/object-calisthenics#key-takeaways]].
7. IF code calls `obj.get_x()` then decides → replace with Tell, Don't Ask per [[software-craft/object-calisthenics#key-takeaways]].
8. IF Long Method → Extract Method per [[software-craft/smell-catalogue#concepts]].
9. IF Switch Statements or repeated `if/elif` on type → Replace Conditional with Polymorphism per [[software-craft/smell-catalogue#concepts]].
10. IF Feature Envy → Move Method per [[software-craft/smell-catalogue#concepts]].
11. IF Primitive Obsession → Replace Data Value with Object per [[software-craft/smell-catalogue#concepts]].
12. IF Data Clumps → Introduce Parameter Object per [[software-craft/smell-catalogue#concepts]].
13. IF Shotgun Surgery or Divergent Change → Extract Class per [[software-craft/smell-catalogue#concepts]].
14. IF no improvement is needed → skip refactoring and proceed to the next test.
15. IF a spec gap or inconsistency is discovered during refactoring → do NOT modify specification documents (domain_model.md, technical_design.md, glossary.md, product_definition.md, system.md, context_map.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
16. Commit refactor changes separately from feature changes per [[software-craft/git-conventions#concepts]].
17. Run `task test-fast` to confirm all tests remain green after refactoring.
18. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
19. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.