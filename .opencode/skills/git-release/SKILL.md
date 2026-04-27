---
name: git-release
description: Create releases with hybrid major.minor.patch+date versioning and optional custom release naming
version: "2.0"
author: stakeholder
audience: stakeholder
workflow: release-management
---

# Git Release

## When to Use

The stakeholder triggers a release after the product owner accepts a feature at Step 5. The software-engineer or system-architect loads this skill when instructed by the stakeholder to create a tagged GitHub release. Releases happen from `main` only — never from feature branches.

## Version Format

`v{major}.{minor}.{patch}+{YYYYMMDD}`

| Location | Format | Example |
|---|---|---|
| `pyproject.toml` | Plain semver (no build metadata) | `0.1.0` |
| Git tags | semver + date | `v0.1.0+20260427` |
| CHANGELOG entries | semver + date | `## [v0.1.0+20260427]` |

PyPI rejects the `+` local version identifier (PEP 440), so `pyproject.toml` must contain plain semver only. The date suffix is appended when creating git tags and CHANGELOG entries — it gives humans a quick way to see when a release was made.

### Bump Rules

- **Patch** (`0.1.0` → `0.1.1`): bug fixes
- **Minor** (`0.1.0` → `0.2.0`): new features
- **Major** (`0.1.0` → `1.0.0`): breaking changes
- **Same-day second release**: increment patch, keep same date suffix (`v0.1.0+20260427` → `v0.1.1+20260427`)

## Release Naming

**Default**: no release name — the version tag alone is the release identifier. This is the industry-standard baseline (git tag, GitHub release title = version string).

**Custom naming**: if `docs/branding.md` exists and `Release Naming > Convention` is set, apply it. The convention field specifies the pattern (e.g. `adjective-greek-figure`, `adjective-animal`, `codename`).

Check previous names to avoid repetition:
```bash
gh release list --limit 20
```

## Release Process

**Guard**: `git branch --show-current` must output `main`. If not, stop — releases happen from `main` only.

```bash
git checkout main
git fetch origin main
git merge --ff-only origin/main   # fast-forward only; if this fails, main has diverged — resolve first
```



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
# Determine major.minor.patch based on change type, then:
# new_version="v{major}.{minor}.{patch}+${current_date}"
```

### 3. Update version in pyproject.toml

Set the plain semver version (no `+` or date suffix):
```bash
# Update pyproject.toml version field to the new plain semver (e.g. 0.2.0)
# The date suffix is only added to git tags and CHANGELOG — never in pyproject.toml
```

### 4. Update CHANGELOG.md

Add at the top. If a release name was generated in Step 0, include it; otherwise omit it:
```markdown
## [v{semver}+{date}] - {YYYY-MM-DD}[- {Release Name}]

### Added
- description (#PR-number)

### Changed
- description (#PR-number)

### Fixed
- description (#PR-number)
```

### 5. Update living docs

Run the `update-docs` skill to reflect the newly accepted feature in the Context and Container sections and the glossary. This step runs inline — do not commit separately.

Load and execute the full `update-docs` skill now:
- Update `## Context` section in `docs/system.md`
- Update `## Container` section in `docs/system.md` (if multi-container)
- Update `docs/glossary.md` (living glossary)

The `update-docs` commit step is **skipped** here — all changed files are staged together with the version bump in step 6.

### 6. Run release-check

Run the automated pre-release checklist before committing:

```bash
uv run task release-check
```

If this fails, fix the issues and rerun. Do not commit until it passes.

### 7. Regenerate lockfile and commit version bump

After updating `pyproject.toml`, regenerate the lockfile — CI runs `uv sync --locked` and will fail if it is stale:

```bash
uv lock
git add pyproject.toml CHANGELOG.md uv.lock \
  docs/system.md docs/glossary.md
git commit -m "chore(release): bump version to v{semver}+{date}[- {Release Name}]"
# Include " - {Release Name}" only if a release name was generated in Step 0; omit otherwise.
```

### 8. Create GitHub release

Assign the SHA first so it expands correctly inside the notes string:

```bash
SHA=$(git rev-parse --short HEAD)
# Construct the full tag with date suffix
TAG_VERSION="v{semver}+$(date +%Y%m%d)"
git tag "${TAG_VERSION}"
git push origin "${TAG_VERSION}"
gh release create "${TAG_VERSION}" \
  --title "${TAG_VERSION}[- {Release Name}]" \
  --notes "# ${TAG_VERSION}[- {Release Name}]

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
# Replace [- {Release Name}] with the actual name, or omit the bracketed portion entirely if Step 0 produced no name.
```

### 9. If a hotfix commit follows the release tag

If CI fails after the release (e.g. a stale lockfile) and a hotfix commit is pushed, reassign the tag and GitHub release to that commit:

```bash
# Delete the old tag locally and on remote
git tag -d "${TAG_VERSION}"
git push origin ":refs/tags/${TAG_VERSION}"

# Recreate the tag on the hotfix commit
git tag "${TAG_VERSION}" {hotfix-sha}
git push origin "${TAG_VERSION}"

# Update the GitHub release to point to the new tag
gh release edit "${TAG_VERSION}" --target {hotfix-sha}
```

The release notes and title do not need to change — only the target commit moves.

## Quality Checklist

- [ ] `task release-check` passes (runs version alignment, changelog entry, lint, static-check, tests, doc-build)
- [ ] `pyproject.toml` version updated (plain semver, no `+` or date)
- [ ] `<package>/__version__` matches `pyproject.toml` version (if present)
- [ ] CHANGELOG.md updated
- [ ] `update-docs` skill run — Context, Container sections, and glossary reflect the new feature
- [ ] Release name not used before
- [ ] Release notes follow the template format
- [ ] If a hotfix was pushed after the tag: tag reassigned to hotfix commit
