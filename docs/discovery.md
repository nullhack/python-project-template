# Discovery: temple8

---

## Session: 2026-04-22

### Context

temple8 is a Python project template used by Python engineers who want to start a new project with production-ready tooling already in place. The product eliminates setup boilerplate — quality tooling, CI, test infrastructure, and an AI-assisted delivery workflow are all preconfigured. It exists because the cost of setting up a rigorous environment from scratch discourages engineers from applying good practices from day one. Success means an engineer can clone the template and ship a meaningful first feature within a single session. Failure means the template introduces more friction than it removes, or that it locks engineers into choices they cannot override.

Out of scope: runtime infrastructure (databases, message queues, cloud deployment), UI frameworks, and any domain-specific business logic.

### Feature List

- `display-version` — The application reads its own version from `pyproject.toml` at runtime and logs it; log output is gated by a verbosity parameter.

### Domain Model

| Type | Name | Description | In Scope |
|------|------|-------------|----------|
| Noun | `Version` | Semver string read from `pyproject.toml` via `tomllib` | Yes |
| Noun | `ValidVerbosity` | Closed set of five standard Python log level names | Yes |
| Verb | `version()` | Reads version and emits INFO log | Yes |
| Verb | `main(verbosity)` | Configures logging and calls `version()` | Yes |
