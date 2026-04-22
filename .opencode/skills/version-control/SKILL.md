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

## Git Safety Protocol (read first — never violate)

These rules are absolute. Violating them risks destroying shared history or losing work.

- **No force push**: `git push --force` and `git push --force-with-lease` are forbidden.
- **No history rewrite on pushed branches**: After a branch has been pushed to `origin`, do not `git rebase -i`, `git commit --amend`, or `git reset --hard` on it. These commands rewrite history that others may have fetched.
- **Use `git revert` to undo**: If a commit on a pushed branch must be undone, create a new revert commit. This appends history safely.
- **No commits directly to `main`**: All feature work happens on branches. `main` receives code only via `--no-ff` merge from an approved feature branch.

---

## Branch Lifecycle

### Normal Feature Flow

```
main ──●────────────────────────────●─────►
        \                          /
         \── feat/<stem> ──●──●──●/
```

1. **Create** from latest `main`
2. **Develop** all commits on the branch
3. **Merge** back to `main` with `--no-ff` after Step 5 acceptance

### Post-Mortem Fix Flow

```
main ──●─────●───────────────────────●─────►
        \   /                        /
         \ /                        /
          ● (start commit)         /
           \── fix/<stem> ──●──●──●/
```

1. **Find** the feature's original start commit
2. **Branch** `fix/<stem>` from that commit
3. **Commit post-mortem** as the first commit on the new branch
4. **Redo** Steps 2–5 on `fix/<stem>`
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

**Branch naming**:
- `feat/<feature-stem>` — new feature
- `fix/<feature-stem>` — post-mortem restart of a failed feature
- `docs/<scope>` — documentation-only changes
- `chore/<scope>` — tooling, deps, CI

**If `main` has unmerged work**: The `git merge --ff-only` will fail. This means `main` is ahead of your local copy. Escalate to the PO or SA — do not resolve by merging or rebasing on your own.

---

## 2. Commit Hygiene

Every commit on a feature branch must follow conventional commits:

```
<type>(<scope>): <description>

Types: feat, fix, test, refactor, chore, docs, perf, ci
```

**Forbidden commit messages** (reject immediately if you are tempted to use them):
- `wip`, `temp`, `fix tests`, `oops`, `try again`, `asdf`
- Any commit without a type prefix

**Commit early, commit often**: A feature branch with 10 small, well-described commits is better than 1 giant commit. But do not commit broken code (tests must pass at each commit during Step 3).

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
- Wrong branch → `git checkout feat/<feature-stem>` (or create it if missing)
- Dirty working tree → commit or stash before continuing
- No commits ahead of main → you have not started work on this branch

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

**Why `--no-ff`**: Fast-forward merges erase the feature boundary from history. With `--no-ff`, the merge commit groups all feature commits together, making the feature revertible as a single unit.

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

The system-architect then begins Step 2 on `fix/<feature-stem>`, reading the post-mortem as input. All subsequent work (stubs, tests, implementation) happens on this branch. It merges to `main` with `--no-ff` after acceptance.

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
