---
name: git-release
description: Create releases with hybrid major.minor.calver versioning and optional custom release naming
version: "1.1"
author: software-engineer
audience: software-engineer
workflow: release-management
---

# Git Release

Create a tagged GitHub release after the PO accepts the feature (Step 5).

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

**Default**: no release name — the version tag alone is the release identifier. This is the industry-standard baseline (git tag, GitHub release title = version string).

**Custom naming**: if `docs/branding.md` exists and `Release Naming > Convention` is set, apply it. The convention field specifies the pattern (e.g. `adjective-greek-figure`, `adjective-animal`, `codename`).

Check previous names to avoid repetition:
```bash
gh release list --limit 20
```

## Release Process

### 0. Read branding

Read `docs/branding.md` if it exists:

- If `Release Naming > Convention` is set: use that convention for the release name. Analyze commits and PRs to choose a name that reflects the release theme.
- If `Release Naming > Theme` is set: constrain the name to that thematic domain.
- If `Release Naming > Excluded words` is set: omit those words.
- If the file is absent or `Release Naming > Convention` is blank: skip naming — use version string only.

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

Add at the top. If a release name was generated in Step 0, include it; otherwise omit it:
```markdown
## [v{version}] - {YYYY-MM-DD}[ - {Release Name}]

### Added
- description (#PR-number)

### Changed
- description (#PR-number)

### Fixed
- description (#PR-number)
```

### 5. Update living docs

Run the `update-docs` skill to reflect the newly accepted feature in C4 diagrams and the glossary. This step runs inline — do not commit separately.

Load and execute the full `update-docs` skill now:
- Update `docs/c4/context.md` (C4 Level 1)
- Update `docs/c4/container.md` (C4 Level 2, if multi-container)
- Update `docs/glossary.md` (living glossary)

The `living-docs` commit step is **skipped** here — all changed files are staged together with the version bump in step 6.

### 6. Regenerate lockfile and commit version bump

After updating `pyproject.toml`, regenerate the lockfile — CI runs `uv sync --locked` and will fail if it is stale:

```bash
uv lock
git add pyproject.toml <package>/__init__.py CHANGELOG.md uv.lock \
  docs/c4/context.md docs/c4/container.md docs/glossary.md
git commit -m "chore(release): bump version to v{version}[ - {Release Name}]"
# Include " - {Release Name}" only if a release name was generated in Step 0; omit otherwise.
```

### 7. Create GitHub release

Assign the SHA first so it expands correctly inside the notes string:

```bash
SHA=$(git rev-parse --short HEAD)
gh release create "v{version}" \
  --title "v{version}[ - {Release Name}]" \
  --notes "# v{version}[ - {Release Name}]

> *\"{one-line tagline matching the release theme}\"*   ← include only if a release name was generated

## Changelog

### Added
- feat: description (#PR)

### Fixed
- fix: description (#PR)

### Changed
- refactor/chore/docs: description (#PR)

## Summary

2-3 sentences describing what this release accomplishes[ and why the name fits — omit if no name].

---
**SHA**: \`${SHA}\`"
# Replace [ - {Release Name}] with the actual name, or omit the bracketed portion entirely if Step 0 produced no name.
```

### 8. If a hotfix commit follows the release tag

If CI fails after the release (e.g. a stale lockfile) and a hotfix commit is pushed, reassign the tag and GitHub release to that commit:

```bash
# Delete the old tag locally and on remote
git tag -d "v{version}"
git push origin ":refs/tags/v{version}"

# Recreate the tag on the hotfix commit
git tag "v{version}" {hotfix-sha}
git push origin "v{version}"

# Update the GitHub release to point to the new tag
gh release edit "v{version}" --target {hotfix-sha}
```

The release notes and title do not need to change — only the target commit moves.

## Quality Checklist

- [ ] `task test` passes
- [ ] `task lint` passes
- [ ] `task static-check` passes
- [ ] `pyproject.toml` version updated
- [ ] `uv lock` run after version bump — lockfile must be up to date
- [ ] `<package>/__version__` matches `pyproject.toml` version
- [ ] CHANGELOG.md updated
- [ ] `update-docs` skill run — C4 diagrams and glossary reflect the new feature
- [ ] Release name not used before
- [ ] Release notes follow the template format
- [ ] If a hotfix was pushed after the tag: tag reassigned to hotfix commit
