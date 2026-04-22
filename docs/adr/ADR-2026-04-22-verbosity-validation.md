# ADR-2026-04-22 — verbosity-validation

**Status:** Accepted
**Date:** 2026-04-22
**Author:** system-architect
**Feature:** display-version

---

## Context

`main()` accepts a `verbosity` string from the CLI. Python's `logging.basicConfig` silently falls back to `WARNING` when given an unrecognised level name, producing no error and potentially confusing users who mistype a level. The caller needs a fast, descriptive failure rather than silent misconfiguration.

## Decision

We will validate `verbosity` against the closed set `{DEBUG, INFO, WARNING, ERROR, CRITICAL}` before calling `logging.basicConfig`. An invalid value raises `ValueError` with a message that names the invalid input and lists all valid options. The type alias `ValidVerbosity` documents this constraint in the type system.

## Consequences

- **Positive:** Misconfigured verbosity fails loudly at startup; the error message is self-documenting.
- **Negative:** Custom log level names (registered via `logging.addLevelName`) are not accepted; this is intentional — the template targets standard usage.
- **Neutral:** The validation logic is a single guard clause; it adds no meaningful complexity.

---

> ADRs are append-only. To revise a decision, create a new ADR and set the Status of this one to "Superseded by ADR-YYYY-MM-DD-<new-slug>".
