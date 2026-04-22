# Glossary — temple8

Living glossary of domain terms. PO updates after each discovery session.
SA reads before Step 2. SE reads before Step 3.

All terms are reconciled against `docs/system.md` (Domain Model section) and `docs/discovery.md`.

---

## Terms

| Term | Type | Definition | First seen |
|------|------|------------|------------|
| `Version` | Noun | The semver string (`MAJOR.MINOR.YYYYMMDD`) stored under `[project] version` in `pyproject.toml` and read at runtime via `tomllib`. Never duplicated as a source-code constant. | 2026-04-22 |
| `ValidVerbosity` | Noun | A string value drawn from the closed set `{DEBUG, INFO, WARNING, ERROR, CRITICAL}` — the five standard Python log level names. Any other value is invalid and raises `ValueError`. | 2026-04-22 |
| `version()` | Verb | The function in `app/version.py` that reads `pyproject.toml`, emits an INFO log message in the format `"Version: <version>"`, and returns the version string. | 2026-04-22 |
| `main(verbosity)` | Verb | The CLI entry point in `app/__main__.py`. Accepts a `ValidVerbosity` string, configures the root logger, then calls `version()`. Raises `ValueError` on invalid verbosity. | 2026-04-22 |
| `feature-stem` | Noun | The kebab-case filename (without `.feature` extension) used to identify a feature across `docs/features/`, branch names (`feat/<stem>`), and test directories (`tests/features/<stem>/`). | 2026-04-22 |

---

> Entries are append-only. To correct a definition, add a new row with the corrected text and mark the old one *(superseded by <date>)*.
