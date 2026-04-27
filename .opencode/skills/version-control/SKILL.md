---
name: version-control
description: Git branching, merge safety, and commit hygiene for feature development
version: "1.0"
author: software-engineer
audience: software-engineer
workflow: git-management
---

# Version Control

This skill governs all Git operations during feature development. The software-engineer owns branch creation, commit hygiene, merging to `main`, and post-mortem branch management.

See [[git/protocol]] for the Git safety protocol, branch naming conventions, commit hygiene format, and merge strategy rules. These rules are absolute — never violate them.

---

## Branch Lifecycle

### Normal Feature Flow

```
main --*-----------------------------*--->
         \                          /
          \-- feat/<stem> --*--*--*-/
```

1. **Create** from latest `main`
2. **Develop** all commits on the branch
3. **Merge** back to `main` with `--no-ff` after Step 5 acceptance

### Post-Mortem Fix Flow

```
main --*-----*-----------------------*--->
         \   /                        /
          \ /                        /
           * (start commit)         /
            \-- fix/<stem> --*--*--*-/
```

1. **Find** the feature's original start commit
2. **Branch** `fix/<stem>` from that commit
3. **Commit post-mortem** as the first commit on the new branch
4. **Redo** Steps 2-5 on `fix/<stem>`
5. **Merge** back to `main` with `--no-ff`

---

## 1. Create Feature Branch

Run at the start of Step 2 (before the system-architect writes stubs).

```bash
# Ensure you are on main and it is up to date
git branch --show-current   # must output: main
git fetch origin main
git merge --ff-only origin/main   # fast-forward only; if this fails, main has diverged — escalate

# Create and switch to feature branch
git checkout -b feat/<feature-stem>

# Push the branch to origin (establishes tracking)
git push -u origin feat/<feature-stem>
```

**Branch naming**: See [[git/protocol]] for the full branch naming conventions (`feat/`, `fix/`, `docs/`, `chore/`).

**If `main` has unmerged work**: The `git merge --ff-only` will fail. This means `main` is ahead of your local copy. Escalate to the PO or SA — do not resolve by merging or rebasing on your own.

---

## 2. Commit Hygiene

See [[git/protocol]] for the full conventional commits format, allowed types, and forbidden messages. In summary: every commit must follow `<type>(<scope>): <description>` with types from the approved list. Never commit without a type prefix.

---

## 3. Branch Verification

Run before every session start and before every handoff.

```bash
# Verify you are on the correct branch
git branch --show-current   # expect: feat/<feature-stem> or fix/<feature-stem>

# Verify working tree is clean
git status   # expect: "nothing to commit, working tree clean"

# Verify branch is ahead of main (has commits)
git log main..HEAD --oneline   # expect: 1+ commits listed
```

**If any check fails**:
- Wrong branch -> `git checkout feat/<feature-stem>` (or create it if missing)
- Dirty working tree -> commit or stash before continuing
- No commits ahead of main -> you have not started work on this branch

---

## 4. Merge Feature Branch to Main

Run after PO acceptance (Step 5). This is the only way code enters `main`.

```bash
# Ensure feature branch is clean and all commits are pushed
git status   # must be clean
git push origin feat/<feature-stem>

# Switch to main and update it
git checkout main
git fetch origin main
git merge --ff-only origin/main

# Check for merge conflicts before the real merge
git merge-tree $(git merge-base HEAD feat/<feature-stem>) HEAD feat/<feature-stem>
# If the output is non-empty, there are conflicts. Resolve them on the feature branch first.

# Merge with --no-ff to preserve feature boundary
git merge --no-ff feat/<feature-stem> -m "feat(<scope>): merge <feature-stem> to main"

# Push main
git push origin main

# Delete the feature branch (optional, but recommended)
git branch -d feat/<feature-stem>
git push origin --delete feat/<feature-stem>
```

See [[git/protocol#concepts]] for why `--no-ff` is required and what it preserves in project history.

---

## 5. Post-Mortem Branch

Run when a feature fails acceptance and the PO restarts it at Step 2.

```bash
# Find the feature's original start commit
# The start commit is the commit where the feature branch was created from main.
# It is typically the first commit on the old feature branch.
git log --all --grep="feat(<feature-stem>)" --oneline
# Or, if the branch still exists:
git log --reverse main..feat/<feature-stem> --oneline   # first line = start commit

# Checkout the start commit and create fix branch
git checkout -b fix/<feature-stem> <start-commit-sha>

# Commit the post-mortem as the first commit on the new branch
git add docs/post-mortem/YYYY-MM-DD-<feature-stem>-<keyword>.md
git commit -m "docs(post-mortem): root cause for <feature-stem> <keyword>"

# Push the fix branch
git push -u origin fix/<feature-stem>
```

The system-architect then begins Step 2 (arch-cycle subflow) on `fix/<feature-stem>`, reading the post-mortem as input. All subsequent work (stubs, tests, implementation) happens on this branch. It merges to `main` with `--no-ff` after acceptance.

**Old feature branch**: Keep it for reference until the fix branch is merged. Do not delete it prematurely — it contains the history the SA may need to consult.

---

## 6. Conflict Detection

Before merging a feature branch to `main`, check if `main` has diverged since the branch was created.

```bash
# Check if main has new commits not in the feature branch
git log feat/<feature-stem>..origin/main --oneline
# If output is non-empty, main has diverged.

# Preview the merge without touching files
git merge-tree $(git merge-base main feat/<feature-stem>) main feat/<feature-stem>
# Empty output = clean merge. Non-empty output = conflicts exist.
```

**If conflicts exist**: Resolve them on the feature branch before attempting merge to `main`.

```bash
git checkout feat/<feature-stem>
git merge main   # resolve conflicts, commit the merge
git push origin feat/<feature-stem>
```

Then retry the merge to `main`.

---

## Reference

- Pro Git, Scott Chacon & Ben Straub (free online: git-scm.com/book)
- Git Cheat Sheet (git-scm.com/cheatsheets)
- A successful Git branching model, Vincent Driessen (nvie.com/posts/a-successful-git-branching-model/)