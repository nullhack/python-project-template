---
name: pr-management
description: Create and manage pull requests with proper formatting, labels, and workflow integration
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: git-management
---
## What I do
Streamline pull request creation and management with standardized formatting, automated labeling, and integration with the project's development workflow.

## When to use me
Use this when creating PRs, managing code reviews, or handling PR lifecycle operations.

## PR Creation Workflow

### Branch Naming Conventions
```bash
# Feature branches
feature/user-authentication
feature/api-optimization
feature/dashboard-redesign

# Bug fix branches  
fix/authentication-bug
fix/performance-issue
fix/ui-alignment

# Hotfix branches
hotfix/security-patch
hotfix/critical-bug

# Documentation branches
docs/api-documentation
docs/setup-guide

# Refactoring branches
refactor/auth-service
refactor/database-layer
```

### Conventional Commit Messages
```bash
# Format: <type>(<scope>): <description>
git commit -m "feat(auth): add JWT authentication system"
git commit -m "fix(api): resolve timeout issues in user endpoint" 
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(db): simplify user query methods"
git commit -m "perf(cache): optimize Redis connection pooling"
git commit -m "test(auth): add integration tests for login flow"
```

**Commit Types:**
- `feat` - New features
- `fix` - Bug fixes
- `docs` - Documentation changes
- `style` - Code formatting (no logic changes)
- `refactor` - Code restructuring (no behavior changes)
- `perf` - Performance improvements
- `test` - Adding or updating tests
- `build` - Build system changes
- `ci` - CI/CD pipeline changes
- `chore` - Maintenance tasks

### PR Template Structure
```markdown
## Summary
Brief description of what this PR accomplishes.

## Type of Change
- [ ] 🚀 New feature
- [ ] 🐛 Bug fix
- [ ] 📚 Documentation update
- [ ] 🔧 Refactoring
- [ ] ⚡ Performance improvement
- [ ] 🧪 Test addition/improvement
- [ ] 🔨 Build/CI changes

## Changes Made
- Specific change 1
- Specific change 2
- Specific change 3

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed
- [ ] All tests passing

## Quality Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console.log/print statements left
- [ ] Type hints added (Python)

## Related Issues
Fixes #123
Related to #456

## Screenshots/Examples
(If applicable)

## Breaking Changes
(If any)

## Migration Notes
(If applicable)
```

## PR Creation Commands

### Standard Feature PR
```bash
# 1. Create and switch to feature branch
git checkout develop
git pull origin develop
git checkout -b feature/user-dashboard

# 2. Make changes and commit
git add .
git commit -m "feat(dashboard): add user dashboard with analytics"

# 3. Push branch
git push origin feature/user-dashboard

# 4. Create PR with template
gh pr create \
  --title "Add User Dashboard with Analytics" \
  --body-file .github/pull_request_template.md \
  --label "feature" \
  --label "frontend" \
  --reviewer @team-leads \
  --assignee @me
```

### Bug Fix PR
```bash
git checkout -b fix/authentication-timeout
# ... make fixes ...
git commit -m "fix(auth): resolve JWT token timeout handling"
git push origin fix/authentication-timeout

gh pr create \
  --title "Fix authentication timeout handling" \
  --body "Resolves issue where JWT tokens weren't properly refreshed on timeout" \
  --label "bug" \
  --label "security" \
  --reviewer @security-team
```

### Documentation PR
```bash
git checkout -b docs/api-examples
# ... update docs ...
git commit -m "docs(api): add comprehensive API usage examples"
git push origin docs/api-examples

gh pr create \
  --title "Add comprehensive API usage examples" \
  --body "Enhances API documentation with practical examples and use cases" \
  --label "documentation" \
  --label "enhancement"
```

## PR Management Operations

### Draft PR for Work in Progress
```bash
gh pr create \
  --title "[WIP] Implement user authentication" \
  --body "Work in progress - authentication system implementation" \
  --draft \
  --label "wip"

# Convert draft to ready when complete
gh pr ready 123
```

### PR Review Management
```bash
# Request review from specific users
gh pr edit 123 --add-reviewer @alice,@bob

# Request review from teams  
gh pr edit 123 --add-reviewer @team/backend-team

# Add labels
gh pr edit 123 --add-label "priority:high" --add-label "needs-testing"

# Update PR description
gh pr edit 123 --body "Updated description with new requirements"
```

### Automated PR Checks
```bash
# Check PR status
gh pr status

# View PR checks
gh pr checks 123

# Wait for checks to complete
gh pr checks 123 --watch

# View detailed check output
gh run view $(gh pr view 123 --json headRefOid --jq .headRefOid)
```

## PR Labels and Categories

### Standard Labels
```yaml
# Type labels
- name: "feature"
  color: "0e8a16"
  description: "New feature or enhancement"

- name: "bug"  
  color: "d73a4a"
  description: "Bug fix"

- name: "documentation"
  color: "0075ca"
  description: "Documentation changes"

- name: "refactor"
  color: "fbca04"
  description: "Code refactoring"

- name: "performance"
  color: "ff6600"
  description: "Performance improvements"

# Priority labels
- name: "priority:critical"
  color: "b60205"
  description: "Critical priority"

- name: "priority:high"
  color: "d93f0b"
  description: "High priority"

- name: "priority:medium"
  color: "fbca04"
  description: "Medium priority"

- name: "priority:low"
  color: "0e8a16"
  description: "Low priority"

# Size labels
- name: "size:xs"
  color: "c2e0c6"
  description: "< 10 lines changed"

- name: "size:s" 
  color: "7fcdcd"
  description: "10-29 lines changed"

- name: "size:m"
  color: "bfd4f2"
  description: "30-99 lines changed"

- name: "size:l"
  color: "d4c5f9"
  description: "100-499 lines changed"

- name: "size:xl"
  color: "f9d0c4"
  description: "500+ lines changed"
```

### Auto-Labeling Rules
```yaml
# .github/labeler.yml
"frontend":
  - "frontend/**"
  - "src/components/**"
  - "**/*.tsx"
  - "**/*.css"

"backend":
  - "backend/**"
  - "src/api/**"
  - "**/*.py"

"documentation":
  - "docs/**"
  - "**/*.md"
  - "README.md"

"tests":
  - "tests/**"
  - "**/*test*"
  - "**/*spec*"

"ci":
  - ".github/**"
  - "Dockerfile"
  - "docker-compose.yml"
```

## PR Integration with Development Workflow

### Feature Development Flow
```bash
# 1. Start feature development
/skill feature-definition  # Define requirements
/skill prototype-script    # Create prototype
/skill tdd            # Write tests

# 2. Create PR for design review
git checkout -b feature/user-auth
git add tests/
git commit -m "test(auth): add authentication test suite"
git push origin feature/user-auth

gh pr create \
  --title "[DESIGN] Authentication system test suite" \
  --body "Test-driven design for authentication system. Ready for @architect review." \
  --label "design-review" \
  --label "tests" \
  --reviewer @architect \
  --draft

# 3. After architect approval, implement
/skill signature-design   # Design interfaces
/skill implementation     # Implement features

git add src/
git commit -m "feat(auth): implement JWT authentication system"
git push origin feature/user-auth

# 4. Mark ready for review
gh pr ready
gh pr edit --remove-label "design-review" --add-label "feature"
```

### Quality Gates Integration
```bash
# PR status checks (via GitHub Actions)
name: PR Quality Gates
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Run tests
        run: task test
      
      - name: Check linting
        run: task lint
      
      - name: Type checking
        run: task static-check
      
      - name: Coverage report
        run: task test-report
        
      - name: Size labeling
        uses: codelytv/pr-size-labeler@v1
```

### Automated PR Workflows
```bash
# Auto-merge for dependency updates
gh pr merge 123 --auto --squash

# Close stale PRs
gh pr list --state open --json number,updatedAt | \
  jq '.[] | select(.updatedAt < "2024-01-01") | .number' | \
  xargs -I {} gh pr close {}

# Bulk label application
gh pr list --label "bug" --json number | \
  jq -r '.[].number' | \
  xargs -I {} gh pr edit {} --add-label "needs-testing"
```

## PR Review Guidelines

### Review Checklist
```markdown
## Code Review Checklist

### Functionality
- [ ] Code does what it's supposed to do
- [ ] Edge cases are handled
- [ ] Error handling is appropriate
- [ ] Performance implications considered

### Code Quality  
- [ ] Follows project coding standards
- [ ] SOLID principles applied
- [ ] Object calisthenics followed
- [ ] No code smells detected

### Testing
- [ ] Adequate test coverage
- [ ] Tests are meaningful
- [ ] Test naming conventions followed
- [ ] Property-based tests where appropriate

### Documentation
- [ ] Code is self-documenting
- [ ] Complex logic explained
- [ ] API documentation updated
- [ ] README updated if needed

### Security
- [ ] No sensitive data exposed
- [ ] Input validation present
- [ ] Authentication/authorization correct
- [ ] No SQL injection risks
```

### Review Commands
```bash
# Approve PR
gh pr review 123 --approve --body "LGTM! Great work on the authentication system."

# Request changes
gh pr review 123 --request-changes --body "Please address the security concerns mentioned inline."

# Add review comments
gh pr comment 123 --body "Consider using a constant for the timeout value."

# Check PR conversation
gh pr view 123
```

## Emergency PR Procedures

### Hotfix Process
```bash
# 1. Create hotfix from main
git checkout main
git pull origin main  
git checkout -b hotfix/critical-security-fix

# 2. Make minimal fix
git add .
git commit -m "fix(security): patch authentication vulnerability"

# 3. Create emergency PR
gh pr create \
  --title "🚨 CRITICAL: Security vulnerability patch" \
  --body "Emergency security fix - requires immediate review and merge" \
  --label "critical" \
  --label "security" \
  --label "hotfix" \
  --reviewer @security-team \
  --reviewer @team-leads

# 4. Fast-track review process
gh pr merge --admin --squash
```

### Rollback PR
```bash
# Create rollback PR
git checkout main
git revert HEAD~1  # Revert last commit
git checkout -b fix/rollback-problematic-change

gh pr create \
  --title "Rollback: Revert problematic authentication changes" \
  --body "Rolling back changes due to production issues" \
  --label "rollback" \
  --label "critical"
```

## Integration Examples

### With Release Management
```bash
# After PR merge, check if release needed
merged_prs=$(gh pr list --state merged --base develop --limit 10)
if [[ $(echo "$merged_prs" | wc -l) -ge 5 ]]; then
  echo "Consider creating release - 5+ PRs merged"
  @repo-manager /skill git-release
fi
```

### With CI/CD Pipeline

```yaml
# Auto-deployment for specific labels
name: Auto Deploy
on:
  pull_request:
    types: [closed]
    
jobs:
  deploy:
    if: github.event.pull_request.merged && contains(github.event.pull_request.labels.*.name, 'deploy:staging')
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          echo "Deploying PR #${{ github.event.pull_request.number }} to staging"
          # Deployment commands...
```
