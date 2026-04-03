---
name: template-release
description: Manage complete releases of the cookiecutter template with testing, documentation, themed naming and semantic versioning
license: MIT
compatibility: opencode
metadata:
  audience: template-maintainers
  workflow: template-management
---
## What I do
Handle the complete release process for the cookiecutter template repository including version management, testing, documentation deployment, and GitHub releases.

## When to use me
Use this when ready to release a new version of the cookiecutter template after making improvements, adding features, or fixing bugs.

## Template Versioning Strategy

### Hybrid Calver Versioning for Template
Use hybrid versioning: `v{major}.{minor}.{YYYYMMDD}`

**Version Bump Guidelines:**
- **Major (v2.x.20260401)**: Breaking changes to cookiecutter variables, major workflow changes, removed features
- **Minor (v1.x.20260315)**: New agents, new skills, workflow enhancements, new features, or same-day releases

**Examples:**
```
v1.0.20260302  # Initial release on March 2, 2026
v1.1.20260315  # Added repo-manager agent and git-release skill on March 15
v1.2.20260315  # Second release same day (increment minor)
v1.3.20260320  # Added template-manager meta agent on March 20
v2.0.20260401  # Changed cookiecutter.json structure (breaking) on April 1
```

## Release Process Workflow

### Phase 1: Pre-Release Validation
```bash
# 1. Run comprehensive template tests
echo "🧪 Running template tests..."
bash scripts/template_test.sh

# 2. Validate template repository structure
echo "🔍 Validating template structure..."
test -f cookiecutter.json || { echo "❌ Missing cookiecutter.json"; exit 1; }
test -d "{{cookiecutter.project_slug}}" || { echo "❌ Missing template directory"; exit 1; }
test -f README.md || { echo "❌ Missing template README"; exit 1; }

# 3. Check for unresolved TODOs or FIXMEs
echo "📝 Checking for unresolved items..."
if grep -r "TODO\|FIXME" . --exclude-dir=.git --exclude="*.md" | grep -v "example"; then
    echo "⚠️  Found unresolved TODO/FIXME items - consider addressing before release"
fi
```

### Phase 2: Version Calculation and Update
```bash
# Get current version from git tags
current_version=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.00000000")

# Calculate new version
current_date=$(date +%Y%m%d)
current_major=$(echo $current_version | sed 's/v\([0-9]\+\)\..*/\1/')
current_minor=$(echo $current_version | sed 's/v[0-9]\+\.\([0-9]\+\).*/\1/')
current_date_in_tag=$(echo $current_version | sed 's/v[0-9]\+\.[0-9]\+\.\([0-9]\{8\}\).*/\1/')

case $bump_type in
    "major")
        new_version=$(echo "v$((current_major + 1)).0.${current_date}")
        ;;
    "minor")
        # If same day as last release, increment minor further
        if [ "$current_date_in_tag" = "$current_date" ]; then
            new_version=$(echo "v${current_major}.$((current_minor + 2)).${current_date}")
        else
            new_version=$(echo "v${current_major}.$((current_minor + 1)).${current_date}")
        fi
        ;;
    "revision")
        if [ "$current_date_in_tag" = "$current_date" ]; then
            new_version=$(echo "v${current_major}.$((current_minor + 1)).${current_date}")
        else
            new_version=$(echo "v${current_major}.${current_minor}.${current_date}")
        fi
        ;;
esac

echo "🔖 Next version: $new_version ($bump_type bump)"
```

### Phase 3: Update Documentation and Changelog
```bash
# Update CHANGELOG.md
echo "📝 Updating CHANGELOG.md..."
cat > CHANGELOG_ENTRY.tmp << EOF
## [$new_version] - $(date +%Y-%m-%d)

### Added
$(git log ${current_version}..HEAD --grep="feat:" --pretty="- %s" | sed 's/feat: //')

### Changed  
$(git log ${current_version}..HEAD --grep="refactor:" --pretty="- %s" | sed 's/refactor: //')

### Fixed
$(git log ${current_version}..HEAD --grep="fix:" --pretty="- %s" | sed 's/fix: //')

### Removed
$(git log ${current_version}..HEAD --grep="BREAKING CHANGE" --pretty="- %s")

EOF

# Insert at top of CHANGELOG.md (after header)
if [ -f CHANGELOG.md ]; then
    sed -i '2r CHANGELOG_ENTRY.tmp' CHANGELOG.md
else
    echo "# Changelog\n\nAll notable changes to this cookiecutter template will be documented in this file.\n" > CHANGELOG.md
    cat CHANGELOG_ENTRY.tmp >> CHANGELOG.md
fi

rm CHANGELOG_ENTRY.tmp

# Update README.md with latest version info if needed
sed -i "s/Version: v[0-9]\+\.[0-9]\+\.[0-9]\+/Version: $new_version/g" README.md
```

### Phase 4: Final Template Test with New Version
```bash
# Test template generation one final time
echo "🧪 Final template validation..."
cookiecutter . --no-input

# Validate generated project
generated_project=$(ls -d */ | grep -v ".git" | head -1 | sed 's/\///')
cd "$generated_project"

# Quick smoke test
python -m venv venv
source venv/bin/activate
pip install uv
uv pip install '.[dev]'
python -m ruff check . || { echo "❌ Generated project linting failed"; exit 1; }

cd ..
rm -rf "$generated_project"
echo "✅ Final validation passed"
```

### Phase 5: Create Release with Themed Naming

**IMPORTANT**: You must use your AI capabilities to analyze the commits and generate an appropriate themed name. Do NOT use random/hardcoded selection.

1. **Get commits since last release:**
```bash
git log ${current_version}..HEAD --oneline
```

2. **Analyze the commits using your AI** to determine what this release is about:
   - Read each commit message and PR description
   - Understand the story/narrative of the release

3. **Generate a unique themed name** based on your analysis:
   - Create an adjective-animal pair that reflects the content
   - Avoid overused combinations (fox, owl, dolphin, cheetah)
   - Make it creative and memorable

**Good examples**: Blooming Narwhal, Crystal Jellyfish, Velvet Manta, Electric Firefly, Aurora Moth, Tidal Otter

4. **Create the release:**
```bash
# Commit version changes
git add CHANGELOG.md README.md
git commit -m "chore(release): prepare $new_version

- Update changelog with latest changes
- Bump version references in documentation
- Final template validation completed"

# Create annotated tag
git tag -a $new_version -m "Release $new_version \"$release_name\"

$(git log ${current_version}..HEAD --oneline | head -10)

See CHANGELOG.md for complete details."

# Push changes and tags
git push origin main
git push origin $new_version

# Create GitHub release with themed name (use the AI-generated name as title)
changelog_section=$(sed -n "/## \[$new_version\]/,/## \[/p" CHANGELOG.md | head -n -1)

gh release create $new_version \
  --title "$release_name" \
  --notes "$changelog_section" \
  --latest
```

### Phase 6: Documentation Deployment
```bash
# Deploy documentation using the template's own task
# Note: This uses the generated project's doc-publish task as reference

echo "📖 Deploying documentation..."

# If template has its own docs directory
if [ -d "docs" ]; then
    # Build and deploy documentation
    pip install mkdocs mkdocs-material
    mkdocs gh-deploy --force
    echo "✅ Documentation deployed to GitHub Pages"
else
    echo "ℹ️  No template documentation directory found"
fi

# Update template README with latest release info
echo "📝 Updating template README with release info..."
sed -i "s/Latest Release: .*/Latest Release: [$new_version](https:\/\/github.com\/$(gh repo view --json owner,name --jq '.owner.login + \"/\" + .name')\/releases\/tag\/$new_version)/" README.md

git add README.md
git commit -m "docs: update README with latest release info"
git push origin main
```

## Release Types and Procedures

### Regular Release (Minor/Patch)
```bash
# Standard release workflow
@template-manager /skill template-test   # Validate template
@template-manager /skill template-release --type=minor
```

### Emergency Patch Release
```bash
# Hot fix workflow
git checkout main
git checkout -b hotfix/critical-template-bug
# ... make minimal fixes ...
git commit -m "fix(template): resolve critical cookiecutter generation issue"
git push origin hotfix/critical-template-bug

gh pr create --title "Critical Template Fix" --body "Emergency fix for template generation"
# After merge:
@template-manager /skill template-release --type=patch --emergency
```

### Major Release (Breaking Changes)
```bash
# Breaking changes require careful handling
@template-manager /skill template-test   # Extra validation
# Review breaking change documentation
@template-manager /skill template-release --type=major
# Send notification to template users
```

## Release Validation Checklist

### Pre-Release Requirements
- [ ] All template tests pass (`/skill template-test`)
- [ ] Generated projects pass quality checks
- [ ] CHANGELOG.md is updated
- [ ] README.md reflects current state
- [ ] No unresolved TODO/FIXME items
- [ ] Documentation builds successfully
- [ ] Version bump type is appropriate

### Post-Release Validation
- [ ] GitHub release created successfully
- [ ] Documentation deployed to GitHub Pages
- [ ] Template can be used immediately: `cookiecutter gh:username/repo`
- [ ] Generated projects work correctly
- [ ] Release announcement prepared (if needed)

### Breaking Change Considerations
For major releases with breaking changes:
- [ ] Migration guide created
- [ ] Breaking changes documented in CHANGELOG
- [ ] Deprecation warnings added (if possible)
- [ ] Communication plan for existing users

## Integration with Generated Project Releases

### Template vs Project Release Coordination
```bash
# Template releases create new versions of the workflow
# Generated projects inherit the workflow but version independently

# Template release workflow:
# 1. Template v1.2.0 introduces new agent
# 2. New projects get the new agent automatically
# 3. Existing projects can regenerate to get updates

# Communication between systems:
echo "Template Release: $new_version" >> .template-releases
echo "Compatible with generated project workflow: v1.x.x" >> .template-releases
```

### Automated Release Notifications
```bash
# Create release announcement
cat > RELEASE_ANNOUNCEMENT.md << EOF
# 🚀 Python Project Template $new_version Released

## What's New
$changelog_section

## How to Use
\`\`\`bash
cookiecutter gh:your-username/python-project-template
\`\`\`

## Upgrading Existing Projects
To get the latest features in existing projects:
1. Backup your current project
2. Regenerate from the new template
3. Merge changes carefully

See [Migration Guide](docs/migration.md) for details.
EOF
```

## Example Release Commands

### Standard Minor Release
```bash
# After adding new skills/agents
git add .
git commit -m "feat(agents): add template-manager meta agent"
@template-manager /skill template-release
# Output: "Created release v1.2.20260320 with new meta agent functionality"
```

### Patch Release  
```bash
# After fixing documentation or bugs
git add .
git commit -m "fix(docs): correct cookiecutter variable examples"
@template-manager /skill template-release
# Output: "Created release v1.2.20260320 with documentation fixes"
```

### Major Release
```bash
# After changing cookiecutter.json structure
git add .
git commit -m "feat!: restructure cookiecutter variables for better usability

BREAKING CHANGE: cookiecutter.json format changed"
@template-manager /skill template-release
# Output: "Created release v2.0.20260401 with breaking changes - migration guide included"
```