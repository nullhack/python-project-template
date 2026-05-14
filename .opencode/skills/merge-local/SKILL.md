---
name: merge-local
description: "Squash-merge feature commits into local dev branch, pull remote dev, and resolve conflicts"
---

# Merge Local

Available knowledge: [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: read all before starting work.

1. Pull latest remote dev: `git fetch origin dev && git checkout dev && git merge --ff-only origin/dev`.
2. If remote dev has diverged, rebase the feature branch on updated dev before squash-merging.
3. Squash all feature commits into a single commit per [[software-craft/git-conventions#concepts]].
4. Merge the squashed commit into local dev.
5. Run feature-type verification per [[software-craft/git-conventions#content]].
6. Run `uv run task test-fast` to verify all tests pass on local dev.
7. If conflicts arise during rebase or merge:
   - IF the conflict is a straightforward text merge → resolve and continue.
   - IF the conflict requires a design decision → present options to the stakeholder with consequences before resolving.
