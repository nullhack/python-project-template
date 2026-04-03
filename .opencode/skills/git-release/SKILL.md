---
name: git-release
description: Create semantic releases with hybrid major.minor.calver versioning and themed naming
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: release-management
---
## What I do
Manage the complete release process including version calculation, changelog generation, release creation, and themed naming based on PR sentiment analysis.

## When to use me
Use this when ready to create a new release after features are complete and tested.

## Hybrid Versioning System

### Version Format
`v{major}.{minor}.{YYYYMMDD}`

**Components:**
- **Major**: Breaking changes (e.g., API changes, removed features)
- **Minor**: New features, significant enhancements, or same-day releases
- **Date**: Release date in YYYYMMDD format

**Examples:**
```
v1.0.20260302  # Version 1.0, release on March 2, 2026
v1.1.20260315  # Version 1.1, release on March 15, 2026
v1.2.20260315  # Version 1.2, second release same day
v2.0.20260401  # Version 2.0, breaking changes on April 1, 2026
```

### Version Bump Rules
```bash
# Feature release (minor bump)
v1.2.20260302 → v1.3.{today}

# Breaking change (major bump)  
v1.2.20260302 → v2.0.{today}

# Same day release (increment minor by 2)
v1.2.20260302 → v1.3.20260302
```

## Release Naming Strategy

### Adjective-Animal Themes
Generate release names by analyzing PR sentiment and selecting appropriate themes.

### Theme Categories

#### Performance & Speed
**Adjectives**: swift, rapid, lightning, blazing, turbo, speedy, agile
**Animals**: cheetah, falcon, hare, gazelle, hawk, dolphin, hummingbird

Examples: `swift cheetah`, `lightning falcon`, `rapid gazelle`

#### Security & Protection  
**Adjectives**: vigilant, guardian, watchful, secure, protective, stalwart, fortress
**Animals**: owl, bear, hawk, wolf, eagle, rhinoceros, mastiff

Examples: `vigilant owl`, `guardian bear`, `watchful hawk`

#### Innovation & Features
**Adjectives**: creative, innovative, clever, brilliant, inventive, pioneering, ingenious
**Animals**: fox, dolphin, raven, octopus, monkey, parrot, crow

Examples: `creative fox`, `innovative dolphin`, `clever raven`

#### Stability & Fixes
**Adjectives**: persistent, diligent, careful, steadfast, reliable, thorough, patient
**Animals**: badger, ant, turtle, ox, elephant, beaver, bull

Examples: `persistent badger`, `diligent ant`, `careful turtle`

#### Refactoring & Cleanup
**Adjectives**: elegant, graceful, nimble, refined, polished, pristine, sleek
**Animals**: swan, deer, cat, crane, jaguar, seal, panther

Examples: `elegant swan`, `graceful deer`, `nimble cat`

#### Documentation & Knowledge
**Adjectives**: wise, thoughtful, scholarly, insightful, learned, enlightened, sage
**Animals**: elephant, whale, owl, sloth, tortoise, raven, dolphin

Examples: `wise elephant`, `thoughtful whale`, `scholarly owl`

## PR Sentiment Analysis

### Analysis Process
1. **Gather Recent PRs**
   ```bash
   gh pr list --state merged --base develop --limit 20 --json title,body,labels
   ```

2. **Categorize by Keywords**
   ```python
   performance_keywords = ["optimize", "performance", "speed", "cache", "faster"]
   security_keywords = ["security", "auth", "encrypt", "vulnerability", "safe"]
   feature_keywords = ["add", "implement", "new", "feature", "enhance"]
   fix_keywords = ["fix", "bug", "error", "issue", "patch"]
   refactor_keywords = ["refactor", "clean", "restructure", "improve", "organize"]
   docs_keywords = ["docs", "documentation", "readme", "guide", "explain"]
   ```

3. **Calculate Dominant Theme**
   ```python
   def analyze_pr_sentiment(prs):
       scores = {
           "performance": 0,
           "security": 0, 
           "features": 0,
           "fixes": 0,
           "refactoring": 0,
           "documentation": 0
       }
       
       for pr in prs:
           text = f"{pr['title']} {pr['body']}".lower()
           # Score based on keyword frequency and PR importance
       
       return max(scores, key=scores.get)
   ```

4. **Select Theme Name**
   ```python
   def generate_release_name(dominant_theme):
       themes = {
           "performance": [("swift", "cheetah"), ("lightning", "falcon"), ("rapid", "hare")],
           "security": [("vigilant", "owl"), ("guardian", "bear"), ("watchful", "hawk")],
           "features": [("creative", "fox"), ("innovative", "dolphin"), ("clever", "raven")],
           # ... etc
       }
       
       return random.choice(themes[dominant_theme])
   ```

## Release Process Workflow

### Step 1: Prepare Release
```bash
# Ensure clean state
git checkout develop
git pull origin develop

# Check for unreleased changes
git log --oneline $(git describe --tags --abbrev=0)..HEAD

# Create release branch
current_date=$(date +%Y%m%d)
git checkout -b release/v1.3.${current_date}
```

### Step 2: Analyze PRs and Generate Name
```bash
# Get merged PRs since last release
last_tag=$(git describe --tags --abbrev=0)
gh pr list --state merged --base develop --limit 20

# Example analysis output:
# Recent PRs:
# - "Optimize database query performance"
# - "Add caching layer for API responses"  
# - "Improve search algorithm efficiency"
# - "Speed up test suite execution"
#
# Dominant theme: PERFORMANCE (4 performance-related PRs)
# Selected name: "swift cheetah"
```

### Step 3: Update Version and Changelog
```bash
# Update pyproject.toml
sed -i 's/version = ".*"/version = "1.3.20260302"/' pyproject.toml

# Generate changelog entry
cat >> CHANGELOG.md << EOF
## [v1.3.20260302] - Swift Cheetah - 2026-03-02

### Performance Improvements
- Optimize database query performance (#123)
- Add caching layer for API responses (#124)  
- Improve search algorithm efficiency (#125)
- Speed up test suite execution (#126)

### Migration Notes
- No breaking changes in this release
- Cache configuration is optional but recommended

EOF

# Commit version bump
git add pyproject.toml CHANGELOG.md
git commit -m "chore(release): bump version to v1.3.20260302 - Swift Cheetah"
```

### Step 4: Create and Publish Release
```bash
# Merge to main
git checkout main
git merge release/v1.3.20260302

# Create tag
git tag v1.3.20260302

# Push to remote
git push origin main --tags

# Create GitHub release
gh release create v1.3.20260302 \
  --title "v1.3.20260302 - Swift Cheetah" \
  --notes-file CHANGELOG.md

# Sync develop branch  
git checkout develop
git merge main
git push origin develop

# Clean up release branch
git branch -d release/v1.3.20260302
git push origin --delete release/v1.3.20260302
```

### Step 5: Post-Release Tasks
```bash
# Verify release
gh release view v1.3.20260302

# Check CI/CD pipeline
gh workflow run deploy --ref v1.3.20260302

# Update project documentation
echo "Latest release: v1.3.20260302 - Swift Cheetah" > .release-info
```

## Hotfix Release Process

### Emergency Fixes (Same Day)
```bash
# Create hotfix from main
git checkout main
git checkout -b hotfix/critical-security-fix

# Make minimal changes
git add .
git commit -m "fix(security): patch authentication vulnerability"

# Create PR for review
gh pr create --title "Critical Security Hotfix" \
  --body "Emergency patch for authentication vulnerability"

# After merge, create revision release
current_date=$(date +%Y%m%d)
last_version=$(git describe --tags --abbrev=0)

# Calculate next revision (v1.3.20260302 → v1.3.20260302r2)
next_revision=$(echo $last_version | sed 's/r\([0-9]\+\)/r\1+1/')

git tag $next_revision
git push origin main --tags

gh release create $next_revision \
  --title "$next_revision - Guardian Bear (Hotfix)" \
  --notes "Emergency security patch"
```

## Integration with Quality Pipeline

### Pre-Release Validation
```bash
#!/bin/bash
# Release validation script

echo "🔍 Running pre-release validation..."

# Ensure all tests pass
task test || { echo "❌ Tests failed"; exit 1; }

# Verify linting
task lint || { echo "❌ Linting failed"; exit 1; }

# Check type safety
task static-check || { echo "❌ Type checking failed"; exit 1; }

# Validate version format
version=$(grep 'version =' pyproject.toml | cut -d'"' -f2)
if ! [[ $version =~ ^[0-9]+\.[0-9]+\.[0-9]{8}r[0-9]+$ ]]; then
    echo "❌ Invalid version format: $version"
    exit 1
fi

# Check changelog updated
if ! grep -q $version CHANGELOG.md; then
    echo "❌ Version not found in CHANGELOG.md"
    exit 1
fi

echo "✅ Pre-release validation passed!"
```

## Example Release Scenarios

### Feature Release
```bash
# Scenario: Added user dashboard, API improvements, new export feature
# Analysis: 3 feature PRs, 1 performance PR
# Theme: FEATURES (dominant)
# Name: "innovative dolphin"
# Version: v1.4.20260315
```

### Security Release
```bash
# Scenario: Authentication fixes, permission updates, security audit
# Analysis: 4 security PRs, 1 docs PR  
# Theme: SECURITY (dominant)
# Name: "vigilant owl"
# Version: v1.3.20260320
```

### Major Release
```bash
# Scenario: API v2, removed legacy endpoints, new architecture
# Analysis: Breaking changes detected
# Theme: Based on supporting PRs
# Name: "pioneering eagle" 
# Version: v2.0.20260401
```