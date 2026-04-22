# Version Control & Branching Strategies

## 63. Pro Git — Scott Chacon & Ben Straub

**Source**: Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. Free online: https://git-scm.com/book

**Key Insight**: Git's distributed model makes branching and merging cheap daily operations, not rare scary events. The book covers the full Git object model (blobs, trees, commits, refs), which explains why operations like `rebase` rewrite history while `revert` appends it — critical for our "no history rewrite" safety protocol.

**Relevance**: Foundation for all Git operations in the project. The object model chapter explains why `git revert` is safe on shared branches while `rebase` is not.

---

## 64. A Successful Git Branching Model — Vincent Driessen

**Source**: Driessen, V. (2010). A successful Git branching model. https://nvie.com/posts/a-successful-git-branching-model/

**Key Insight**: The "git-flow" model defines `master`/`develop` as infinite-lifetime branches, with `feature/*`, `release/*`, and `hotfix/*` as short-lived supporting branches. The `--no-ff` merge is explicitly recommended to preserve feature boundaries in history, making whole-feature reverts possible.

> "The `--no-ff` flag causes the merge to always create a new commit object, even if the merge could be performed with a fast-forward. This avoids losing information about the historical existence of a feature branch."

**Relevance**: Direct basis for our branch model. We use `feat/<stem>` and `fix/<stem>` branches, merge to `main` with `--no-ff`, and delete branches after merge.

---

## 65. Git Cheat Sheet — Git SCM

**Source**: Git SCM. Git Cheat Sheet. https://git-scm.com/cheat-sheet

**Key Insight**: Quick reference for everyday commands. Covers `git merge-tree` for conflict detection without touching working tree, `git log --follow` for renamed files, and `git reflog` for recovery — all relevant to our workflow.

**Relevance**: Operational reference for the SE when executing branch operations.

---

## 66. Common Git Issues & Anti-Patterns

**Source**: Fowler, M. (2013). Patterns for Managing Source Code Branches. https://martinfowler.com/articles/branching-patterns.html

**Key Insight**: Fowler contrasts "feature branching" (short-lived branches, frequent integration) with "release branching" (long-lived stabilization branches). Our model is feature branching: branches live only for the duration of one feature, then merge to `main`.

**Anti-patterns to avoid**:
- **Long-lived feature branches**: increase merge conflict risk and integration pain
- **Force push on shared branches**: destroys history that others may have fetched
- **Squash merge on collaborative branches**: erases individual commit authorship and makes bisect harder
- **Committing directly to main**: bypasses review and breaks the closed loop

**Relevance**: Validates our WIP=1 approach and our safety protocol against force push and history rewrite.

---

## 67. Merge vs. Rebase — When to Use Each

**Source**: Atlassian Git Tutorial. Merging vs. Rebasing. https://www.atlassian.com/git/tutorials/merging-vs-rebasing

**Key Insight**: Rebase rewrites commit history by replaying commits on top of a new base. This is fine for local, unpushed branches but dangerous for shared branches because it changes commit SHAs that others may reference. Merge preserves history but creates merge commits.

**Our rule**: Never rebase a pushed branch. Use `git merge main` on the feature branch to resolve conflicts, then `--no-ff` merge the feature branch to `main`.
