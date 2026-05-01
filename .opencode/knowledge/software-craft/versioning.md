---
domain: software-craft
tags: [semver, calver, versioning, release, pypi]
last-updated: 2026-04-30
---

# Versioning Scheme

## Key Takeaways

- Version scheme: `major.minor.patch` (semver) in `pyproject.toml`; git tags append build date: `v{major}.{minor}.{patch}+{YYYYMMDD}`
- PyPI strips `+build_metadata` — `pyproject.toml` must contain only `major.minor.patch`
- Breaking changes bump major; new features bump minor; fixes bump patch
- Changelog format: `## [v{version}+{date}] - {codename} - {date}`
- Release codenames come from `docs/branding.md`
- New projects start at `0.1.0` (pure semver, no date suffix)
- Git tags are created manually via `gh workflow run tag-release.yml -f version=X.Y.Z` — no auto-trigger on push

## Concepts

**Why semver+calver hybrid**: Semver communicates breaking changes for dependency resolution — `pip install my-project>=8.0.0,<9.0.0` works correctly because the major version signals compatibility. Pure calver (e.g. `2026.4.30`) communicates timing but not compatibility. The `+YYYYMMDD` build metadata suffix (semver §10) provides release-date traceability without affecting version ordering or dependency resolution. See [[software-craft/versioning#key-takeaways]].

**pyproject.toml as single source of truth**: The `version` field in `pyproject.toml` contains only `major.minor.patch` (e.g. `8.0.0`). The `tag-release` workflow reads this field and appends `+YYYYMMDD` when creating the git tag. PyPI reads the version directly from the built wheel/sdist, which contains only the semver core.

**Git tags with build metadata**: Tags follow `v{version}+{YYYYMMDD}` format (e.g. `v8.0.0+20260430`). The `tag-release` CI workflow creates these on manual trigger via `gh workflow run tag-release.yml -f version=X.Y.Z`. The date is the tag creation date, not the commit date.

**Release process**: Merge PRs to main freely — no auto-tags or auto-releases. When ready to release, ensure `pyproject.toml` has the correct version, then trigger: `gh workflow run tag-release.yml -f version=X.Y.Z`. The workflow validates the version matches `pyproject.toml`, runs `release-check`, creates tag `vX.Y.Z+YYYYMMDD`, and pushes it. Publishing (PyPI, GitHub Releases, etc.) is project-specific — not part of this convention.

**Changelog entries**: Each release section uses `## [v{version}+{date}] - {codename} - {date}`. The codename follows the convention in `docs/branding.md` (default: adjective-greek-figure).

**Historical note**: Pre-v8 releases used tags like `v7.2.20260423` where `20260423` occupied the semver patch field. This is neither valid semver (patch should be a small integer) nor proper calver. Starting with v8.0.0, the date is correctly placed in build metadata after `+`.

## Release Process

1. Merge PRs to main freely — no auto-tags, no auto-releases.
2. When ready to release, ensure `pyproject.toml` has the correct version.
3. Trigger the release workflow: `gh workflow run tag-release.yml -f version=X.Y.Z`
4. The workflow validates version matches `pyproject.toml`, runs `release-check`, creates tag `vX.Y.Z+YYYYMMDD`, and pushes it.
5. Publishing (PyPI, GitHub Releases, etc.) is project-specific — not part of this convention.

## References

- [[process/preston-werner_2013]] — SemVer 2.0.0 specification
- [[process/calver_2020]] — Calendar Versioning convention