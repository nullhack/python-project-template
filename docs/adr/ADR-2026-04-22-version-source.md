# ADR-2026-04-22 — version-source

**Status:** Accepted
**Date:** 2026-04-22
**Author:** system-architect
**Feature:** display-version

---

## Context

The application needs to expose its own version at runtime. Two options exist: hardcode a `__version__` constant in the source tree, or read the version from `pyproject.toml` — the file that already serves as the project's authoritative metadata record. Duplicating the version introduces drift risk; a single source of truth eliminates it. Python 3.11+ ships `tomllib` in the standard library, so no additional dependency is required.

## Decision

We will read the version from `pyproject.toml` at runtime using `tomllib`. No `__version__` constant will be defined anywhere in the package. The `pyproject.toml` `[project] version` field is the single source of truth.

## Consequences

- **Positive:** Version is never out of sync between the package and its metadata; no extra release step to update a constant.
- **Negative:** `version()` performs a file read on every call; this is acceptable for a CLI tool but would be a concern in a hot path.
- **Neutral:** Requires Python ≥ 3.11 (tomllib). This matches the project's `requires-python = ">=3.13"` constraint.

---

> ADRs are append-only. To revise a decision, create a new ADR and set the Status of this one to "Superseded by ADR-YYYY-MM-DD-<new-slug>".
