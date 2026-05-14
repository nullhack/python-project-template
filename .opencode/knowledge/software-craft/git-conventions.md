---
domain: software-craft
tags: [git, branching, commits, squash, pull-requests, conflict-resolution]
last-updated: 2026-05-14
---

# Git Conventions

## Key Takeaways

- Feature branches use granular commits per achievement; local dev receives single squashed commits per feature.
- Before merging to local dev: pull latest remote dev, resolve any conflicts feature by feature, then squash-merge.
- Granular commit format: `<type>(<scope>): <specific achievement>` (e.g., `feat(auth): add JWT signing method`).
- Squashed commit format includes Example title traceability, feature metadata, and approval trail.
- Multiple features can accumulate on local dev before creating a PR: the stakeholder decides when to publish.
- PR is an administrative step (dev → main) required by the git hosting platform; changes are already on dev.

## Concepts

**Two-Tier Commit Strategy**. Development happens on feature branches (`feat/<stem>` or `fix/<stem>`) with granular commits per achievement. Each small milestone gets its own commit for development traceability and easy bisection. Before merging to local dev, all feature commits are squashed into a single meaningful commit with Example title traceability.

**Local Dev as Staging Area**. Local dev accumulates squashed feature commits. Multiple features can be developed and squash-merged to local dev before publishing to remote. This allows integration testing of multiple features together and reduces PR noise. The stakeholder decides after each feature whether to continue developing more features or publish the batch. PRs go from dev to main on the remote.

**Conflict Prevention**. Before squash-merging, pull the latest remote dev to detect conflicts early. Resolve conflicts feature by feature on the feature branch. If conflicts require design decisions, present options to the stakeholder with consequences.

**Administrative PR**. The PR (dev → main) serves the git hosting platform's approval requirement, not merge mechanics. Changes are already on local dev. The PR documents what was built, provides traceability via Example titles, and enables the review/approval workflow.

**Conventional Commits**. Every commit follows `<type>(<scope>): <description>`. Types: `feat` (feature), `fix` (bug fix), `test` (test addition/modification), `refactor` (structural change with no behavior change), `chore` (tooling, deps, CI), `docs` (documentation). Forbidden: `wip`, `temp`, any commit without a type prefix.

## Content

### Branch Naming

| Branch Type | Format | Purpose |
|---|---|---|
| Feature | `feat/<feature-stem>` | New feature development |
| Fix | `fix/<feature-stem>` | Post-mortem fix for a rejected feature |
| Docs | `docs/<scope>` | Documentation changes |
| Chore | `chore/<scope>` | Tooling, deps, CI |

### Granular Commit Format

During development on a feature branch, each small achievement gets its own commit:

```
feat(auth): add JWT signing key configuration
test(auth): add failing test for token expiry
feat(auth): implement token expiry validation
refactor(auth): extract token validation to separate method
fix(auth): handle malformed token errors
```

Rules:
- One logical change per commit
- Refactor commits are separate from feature commits
- Never mix a structural change with a behavior addition in one commit
- Every commit leaves tests green

### Squashed Commit Format

Before merging to local dev, squash all feature commits into one:

```
feat(<scope>): <feature summary>

- Implemented: <Example title 1>
- Implemented: <Example title 2>
- Implemented: <Example title 3>

Feature: <feature-name>
Branch: feat/<feature-stem> → dev
Reviewed: SA approved (design + completion)
Accepted: PO approved
```

### Feature-Type Verification

Before any merge, verify the feature works in its delivery context:

| Feature Type | Verification Command |
|---|---|
| CLI | `timeout 10s uv run task run` |
| Library | `uv run python -c "import <package>; <public_api_call>"` |
| Mixed | Both commands above |

## Related

- [[software-craft/tdd]]: commit discipline (separate refactor from feature)
- [[software-craft/source-stubs]]: branch setup during project structuring
- [[software-craft/code-review]]: two-tier review before merge
