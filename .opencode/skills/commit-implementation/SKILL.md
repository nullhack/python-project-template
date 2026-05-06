---
name: commit-implementation
description: "Commit the reviewed, passing implementation with traceability to feature files"
---

# Commit Implementation

Available knowledge: [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Run `task test` and `ruff check .` to verify all tests pass and lint is clean before committing.
2. Commit with traceability per [[software-craft/git-conventions#content]]: use granular commit format with @id tags.
3. IF the commit is a refactoring (no behavior change) → use `refactor(<scope>):` type per [[software-craft/git-conventions#concepts]].
