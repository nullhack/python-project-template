---
name: structure-project
description: "Create project skeleton: branch, package directories, port interfaces, aggregate root signatures, from design artifacts"
---

# Structure Project

Available knowledge: [[architecture/technical-design#key-takeaways]], [[software-craft/stub-design]], [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: read all before starting work. 

1. Create feature branch per [[software-craft/git-conventions#content]]: `feat/<stem>` from latest main.
2. Create package structure per [[architecture/technical-design#key-takeaways]]: directories, `__init__.py` files, port interfaces (Protocol abstractions from hexagonal architecture), and aggregate root class signatures.
