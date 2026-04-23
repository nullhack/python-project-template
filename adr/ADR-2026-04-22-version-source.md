# ADR-2026-04-22-version-source

## Status

Accepted

## Context

The `cli-entrypoint` feature requires the `--version` flag to print the application's version string. The feature rule states: "the version string is always read from package metadata at runtime; it is never hardcoded." The decision is how to access that metadata.

## Interview

| Question | Answer |
|---|---|
| How should the `--version` flag read the version string at runtime? | `importlib.metadata.version()` — stdlib canonical API for installed package metadata |
| What about reading `pyproject.toml` directly with `tomllib`? | Works but requires file path resolution and I/O; `importlib.metadata` is simpler |
| Should we expose a `__version__` constant in `app/__init__.py`? | No — creates a second source of truth that still needs `importlib.metadata` or hardcoding to populate |

## Decision

Use `importlib.metadata.version("temple8")` at runtime.

## Reason

`importlib.metadata` is the canonical stdlib API for reading installed package metadata since Python 3.8. It reads from the distribution's `METADATA` file, which is the single source of truth set by `pyproject.toml`. This satisfies the "never hardcoded" rule with the least code and zero file I/O complexity.

## Alternatives Considered

- **Hardcoded string**: violates the explicit feature rule; drifts from `pyproject.toml` over time.
- **Read `pyproject.toml` at runtime with `tomllib`**: works, but requires file path resolution and adds I/O; `importlib.metadata` is simpler and the stdlib-blessed approach.
- **`app.__version__` constant in `__init__.py`**: requires a second source of truth; still needs `importlib.metadata` or hardcoding to populate it — one extra indirection with no benefit.

## Consequences

- (+) Single source of truth: `pyproject.toml` → installed metadata → runtime
- (+) Works correctly in editable installs (`uv sync`) and wheel installs
- (+) Zero additional imports beyond stdlib
- (-) Requires the package to be installed (not just on `sys.path` as a raw directory) — acceptable since the feature's Given step is "the application package is installed"
