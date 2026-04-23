# ADR-2026-04-22-cli-parser-library

## Status

Accepted

## Context

The `cli-entrypoint` feature requires a CLI parsing library to handle `--help` and `--version` flags. The feature constraint is explicit: zero new runtime dependencies. The template must be installable with no extras, and the CLI skeleton is a demonstration feature, not a production CLI framework.

## Interview

| Question | Answer |
|---|---|
| Which CLI parsing library should the `cli-entrypoint` feature use? | `argparse` — the zero-dependency constraint makes stdlib the only viable option |
| What about `click` or `typer` for ergonomics? | Rejected — both add runtime dependencies violating the feature constraint |
| Is `argparse` sufficient for future CLI growth? | Yes for the skeleton; if complexity grows, revisit in a new ADR |

## Decision

Use `argparse` from the Python stdlib.

## Reason

The zero-dependency constraint is non-negotiable for a template that must install cleanly with `uv sync` and no extras. `argparse` is sufficient for a 2-flag (`--help`, `--version`) CLI skeleton, and its `action="version"` built-in satisfies the version-output criterion directly.

## Alternatives Considered

- **`click`**: ergonomic, widely used, but adds a runtime dependency — violates the zero-dependency constraint.
- **`typer`**: built on click + type hints, even heavier — same violation.

## Consequences

- (+) Zero install footprint — no `requirements.txt` entry, no version pinning for the CLI layer
- (+) `argparse` `action="version"` handles exit-0 and version string format natively
- (+) `build_parser()` is independently testable without subprocess overhead
- (-) `argparse` API is more verbose than click/typer for complex CLIs — acceptable for a 2-flag demonstration skeleton
