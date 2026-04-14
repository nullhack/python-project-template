---
name: git-release
description: Create releases with hybrid major.minor.calver versioning and AI-generated adjective-animal naming
version: "1.0"
author: developer
audience: developer
workflow: release-management
---

# Git Release

Create a tagged GitHub release after the PO accepts the feature (Step 6).

## Version Format

`v{major}.{minor}.{YYYYMMDD}`

- **Major**: breaking changes (API changes, removed features)
- **Minor**: new features; also incremented if two releases happen on the same day
- **Date**: today in YYYYMMDD format

Examples:
```
v1.2.20260302  →  v1.3.20260415   (new feature, new day)
v1.2.20260302  →  v2.0.20260415   (breaking change)
v1.2.20260415  →  v1.3.20260415   (same-day second release)
```

## Release Naming

Each release gets a unique adjective-animal name. Analyze the commits and PRs since the last release, identify the theme, and choose a name that reflects it.

**Good adjectives**: `electric`, `radiant`, `crystalline`, `luminous`, `surging`, `aurora`, `verdant`, `boundless`, `tidal`, `velvet`

**Good animals** (avoid overused: fox, owl, dolphin, cheetah): `narwhal`, `axolotl`, `capybara`, `quokka`, `pangolin`, `kestrel`, `jellyfish`, `manta`, `cuttlefish`, `kingfisher`, `ibis`, `firefly`, `dragonfly`

Check previous names to avoid repetition:
```bash
git tag -l --sort=-v:refname | head -10
```

## Release Process

### 1. Analyze changes since last release

```bash
last_tag=$(git describe --tags --abbrev=0)
git log ${last_tag}..HEAD --oneline
gh pr list --state merged --limit 20 --json title,number,labels
```

### 2. Calculate new version

```bash
current_date=$(date +%Y%m%d)
# Determine major.minor based on change type, then:
# new_version="v{major}.{minor}.${current_date}"
```

### 3. Update version in pyproject.toml and package __init__.py

Both must match:
```bash
# Update pyproject.toml version field
# Update <package>/__version__ to match
```

### 4. Update CHANGELOG.md

Add at the top:
```markdown
## [v{version}] - {Adjective Animal} - {YYYY-MM-DD}

### Added
- description (#PR-number)

### Changed
- description (#PR-number)

### Fixed
- description (#PR-number)
```

### 5. Commit version bump

```bash
git add pyproject.toml <package>/__init__.py CHANGELOG.md
git commit -m "chore(release): bump version to v{version} - {Adjective Animal}"
```

### 6. Create GitHub release

```bash
gh release create "v{version}" \
  --title "v{version} - {Adjective Animal}" \
  --notes "$(cat <<'EOF'
# v{version} - {Adjective Animal}

> *"{one-line poetic tagline matching the release theme}"*

## Changelog

### Added
- feat: description (#PR)

### Fixed
- fix: description (#PR)

### Changed
- refactor/chore/docs: description (#PR)

## Summary

2-3 sentences describing what this release accomplishes and why the name fits.

---
**SHA**: `$(git rev-parse --short HEAD)`
EOF
)"
```

## Quality Checklist

- [ ] `task test` passes
- [ ] `task lint` passes
- [ ] `task static-check` passes
- [ ] `pyproject.toml` version updated
- [ ] `<package>/__version__` matches `pyproject.toml` version
- [ ] CHANGELOG.md updated
- [ ] Release name not used before
- [ ] Release notes follow the template format
