---
domain: git
tags: [git, branching, commits, merge-safety]
last-updated: 2026-04-26
---

# Git Protocol

## Key Takeaways

- Never force push, never rewrite pushed history, never commit directly to main — these rules are absolute.
- Use conventional commits: `<type>(<scope>): <description>` with types from the approved list; reject messages without type prefixes.
- Merge feature branches to main with `--no-ff` only; fast-forward merges erase feature boundaries from history.
- Verify branch state before every session start and handoff: correct branch, clean working tree, commits ahead of main.

## Concepts

**Git Safety Protocol (Absolute)**: Four non-negotiable rules: no force push, no history rewrite on pushed branches, use `git revert` to undo, and no commits directly to `main`. All feature work happens on branches; `main` receives code only via `--no-ff` merge from an approved feature branch.

**Branch Naming and Commit Hygiene**: Feature branches use `feat/<feature-stem>`, post-mortem branches use `fix/<feature-stem>`, documentation branches use `docs/<scope>`, and chore branches use `chore/<scope>`. Every commit follows conventional commits format. Forbidden commit messages include `wip`, `temp`, `fix tests`, and any commit without a type prefix.

**Why --no-ff**: Fast-forward merges erase the feature boundary from history. With `--no-ff`, the merge commit groups all feature commits together, making the feature revertible as a single unit. `git revert -m 1 <merge-commit>` undoes the entire feature.

**Branch Verification and Post-Mortem**: Before every session start and handoff, verify: correct branch, clean working tree, commits ahead of main. When a feature fails acceptance, create a `fix/<stem>` branch from the original start commit and commit the post-mortem as the first commit.

## Content

### Git Safety Protocol (Absolute — Never Violate)

These rules are non-negotiable. Violating them risks destroying shared history or losing work.

1. **No force push**: `git push --force` and `git push --force-with-lease` are forbidden.
2. **No history rewrite on pushed branches**: After a branch has been pushed to `origin`, do not `git rebase -i`, `git commit --amend`, or `git reset --hard` on it. These commands rewrite history that others may have fetched.
3. **Use `git revert` to undo**: If a commit on a pushed branch must be undone, create a new revert commit. This appends history safely.
4. **No commits directly to `main`**: All feature work happens on branches. `main` receives code only via `--no-ff` merge from an approved feature branch.

### Branch Naming Conventions

| Pattern | Purpose |
|---|---|
| `feat/<feature-stem>` | New feature development |
| `fix/<feature-stem>` | Post-mortem restart of a failed feature |
| `docs/<scope>` | Documentation-only changes |
| `chore/<scope>` | Tooling, deps, CI |

### Commit Hygiene

Every commit on a feature branch must follow conventional commits:

```
<type>(<scope>): <description>

Types: feat, fix, test, refactor, chore, docs, perf, ci
```

**Forbidden commit messages** (reject immediately):
- `wip`, `temp`, `fix tests`, `oops`, `try again`, `asdf`
- Any commit without a type prefix

Commit early and often. A feature branch with 10 small, well-described commits is better than 1 giant commit. But do not commit broken code — tests must pass at each commit during Step 3.

### Why --no-ff

Fast-forward merges erase the feature boundary from history. With `--no-ff`, the merge commit groups all feature commits together, making the feature revertible as a single unit.

```
main --*-----------------------------*--->
         \                           /
          \-- feat/<stem> --*--*--*-/
```

The merge commit created by `--no-ff` serves as a permanent marker: "these commits belong to feature X." If the feature needs to be reverted, a single `git revert -m 1 <merge-commit>` undoes the entire feature.

### Branch Verification

Run before every session start and before every handoff:

```bash
git branch --show-current   # expect: feat/<feature-stem> or fix/<feature-stem>
git status                   # expect: "nothing to commit, working tree clean"
git log main..HEAD --oneline # expect: 1+ commits listed
```

If any check fails:
- Wrong branch: `git checkout feat/<feature-stem>` (or create it if missing)
- Dirty working tree: commit or stash before continuing
- No commits ahead of main: you have not started work on this branch

### Post-Mortem Branch

When a feature fails acceptance and the PO restarts it:

```bash
git log --all --grep="feat(<feature-stem>)" --oneline
git checkout -b fix/<feature-stem> <start-commit-sha>
```

The post-mortem document is committed as the first commit on the new branch. All subsequent work happens on `fix/<feature-stem>`, which merges to `main` with `--no-ff` after acceptance.

## Related

- [[workflow/state-machine]] — state transitions that trigger git operations
- [[architecture/adr]] — ADR commits follow the same hygiene rules