---
name: commit-implementation
description: "Commit the reviewed, passing implementation with traceability to feature files"
---

# Commit Implementation

Load [[software-craft/git-conventions#key-takeaways]] before starting. 

1. Run `task test` and `ruff check .` to verify all tests pass and lint is clean before committing.
2. Commit with traceability per [[software-craft/git-conventions#content]] — use granular commit format with @id tags.
3. IF the commit is a refactoring (no behavior change) → use `refactor(<scope>):` type per [[software-craft/git-conventions#concepts]].
4. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
5. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.