# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/) with date build metadata in git tags.

## [v0.1.0+20260427] - 2026-04-27

### Added

- Python project template with CLI entrypoint, TDD workflow, adversarial verification, and AI-assisted delivery discipline
- Five-step delivery cycle: Scope → Architecture → TDD Loop → Verification → Acceptance
- Flow-based session management (`.flowr/flows/` and `.flowr/sessions/`)
- Product Owner, System Architect, and Software Engineer agent roles
- Skills for each step: `define-scope`, `architect`, `implement`, `verify`, `run-session`
- Supporting skills: `refactor`, `apply-patterns`, `check-quality`, `version-control`, `create-pr`, `git-release`, `update-docs`, `select-feature`, `design-colors`, `design-assets`
- Knowledge system under `.opencode/knowledge/` for SOLID, Object Calisthenics, design patterns, TDD, test conventions, and verification philosophy
- ADR template and interview protocol for architectural decisions
- Gherkin `.feature` files with `@id` traceability to test stubs
- `gherkin-official` integration for automatic `@id` assignment
- Self-Declaration (25-item) and Architect Review Stance Declaration for handoff quality
- `scripts/` directory with validation and automation scripts
- Documentation portal (`docs/index.html`), system architecture (`docs/system.md`), living glossary (`docs/glossary.md`)
- Branding system (`docs/branding.md`) with WCAG-validated color palettes and SVG asset generation
- CI workflows: `ci.yml`, `tag-release.yml`, `pypi-publish.yml`, `dependency-review.yml`
- Semver+date versioning: plain semver in `pyproject.toml`, `v{major}.{minor}.{patch}+{YYYYMMDD}` in git tags and CHANGELOG