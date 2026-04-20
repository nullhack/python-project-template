---
name: create-pr
description: Create pull requests with conventional commits, proper formatting, and branch workflow
version: "1.0"
author: software-engineer
audience: software-engineer
workflow: git-management
---

# Create PR

## When to Use

Load this skill after the reviewer approves the feature (Step 4 APPROVED) and the PO has accepted it (Step 5). Use it to create and merge the feature pull request.

## Step-by-Step

### Branch Naming

```
feature/<feature-stem>    # new feature
fix/<issue-description>   # bug fix
refactor/<scope>          # refactoring
docs/<scope>              # documentation
chore/<scope>             # tooling, deps, CI
```

## Conventional Commits

```
<type>(<scope>): <description>

Types: feat, fix, test, refactor, chore, docs, perf, ci
```

Examples:
```bash
git commit -m "feat(auth): implement JWT token generation"
git commit -m "test(auth): add failing tests for token expiry"
git commit -m "fix(physics): correct ball velocity sign after wall bounce"
git commit -m "refactor(game-loop): extract timing logic to dedicated class"
git commit -m "chore(deps): add python-dotenv dependency"
```

## PR Creation

```bash
# Push branch
git push -u origin feature/<feature-stem>

# Create PR
gh pr create \
  --title "feat(<scope>): <description>" \
  --body "$(cat <<'EOF'
## Summary
- <What this PR does in 1-3 bullet points>

## Acceptance Criteria
- [x] `@id:<hex>`: <description>
- [x] `@id:<hex>`: <description>

## Testing
- All tests pass: `task test`
- Linting clean: `task lint`
- Type checking clean: `task static-check`
- Application runs: `timeout 10s task run` (exit 124 = hung = fix it)

## Reviewer Notes
<Any context the reviewer needs>
EOF
)"
```

## PR Checklist Before Creating

- [ ] Branch is up to date with main (`git rebase main`)
- [ ] All commits follow conventional commit format
- [ ] `task lint` exits 0
- [ ] `task static-check` exits 0
- [ ] `task test` exits 0, coverage 100%
- [ ] `timeout 10s task run` exits with code ≠ 124
- [ ] PR description includes all `@id` acceptance criteria

## Merging

Use squash merge for feature branches to keep main history clean:
```bash
gh pr merge <number> --squash --delete-branch
```

After merge, update local main:
```bash
git checkout main
git pull origin main
```
