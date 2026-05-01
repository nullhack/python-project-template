---
name: merge-local
description: "Squash-merge feature commits into local main, pull remote main, and resolve conflicts"
---

# Merge Local

Load [[software-craft/git-conventions#key-takeaways]] before starting. 

1. Pull latest remote main: `git fetch origin main && git merge --ff-only origin/main` into local main.
2. If remote main has diverged, rebase the feature branch on updated main before squash-merging.
3. Squash all feature commits into a single commit per [[software-craft/git-conventions#concepts]].
4. Merge the squashed commit into local main.
5. Run feature-type verification per [[software-craft/git-conventions#content]].
6. Run `uv run task test-fast` to verify all tests pass on local main.
7. If conflicts arise during rebase or merge:
   - IF the conflict is a straightforward text merge → resolve and continue.
   - IF the conflict requires a design decision → present options to the stakeholder with consequences before resolving.
8. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
9. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.