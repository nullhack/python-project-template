---
name: structure-project
description: "Create project skeleton — branch, package directories, port interfaces, aggregate root signatures — from design artifacts"
---

# Structure Project

Load [[architecture/technical-design#key-takeaways]], [[software-craft/stub-design]], and [[software-craft/git-conventions#key-takeaways]] before starting. 

1. Create feature branch per [[software-craft/git-conventions#content]] — `feat/<stem>` from latest main.
2. Create package structure per [[architecture/technical-design#key-takeaways]]: directories, `__init__.py` files, port interfaces (Protocol abstractions from hexagonal architecture), and aggregate root class signatures.
3. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
4. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.