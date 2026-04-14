# Feature: Display Version

## User Stories
- As a developer, I want to retrieve the application version programmatically so that I can display or log it at runtime.
- As a developer, I want to control log verbosity via a parameter so that I can tune output for different environments.

## Acceptance Criteria
- `3f2a1b4c-d5e6-7890-abcd-ef1234567890`: Version string is read from pyproject.toml.
  Source: po

  Given: pyproject.toml exists with a version field
  When: version() is called
  Then: The returned string matches the version in pyproject.toml

- `7a8b9c0d-e1f2-3456-bcde-f12345678901`: Version call emits a log message.
  Source: po

  Given: pyproject.toml exists with a version field
  When: version() is called
  Then: An INFO log message in the format "Version: <version>" is emitted

- `a1b2c3d4-e5f6-7890-abcd-ef1234567890`: Version appears in logs at DEBUG and INFO verbosity.
  Source: po

  Given: A verbosity level of DEBUG or INFO is passed to main()
  When: main() is called
  Then: The version string appears in the log output

- `b2c3d4e5-f6a7-8901-bcde-f12345678901`: Version is absent from logs at WARNING and above.
  Source: po

  Given: A verbosity level of WARNING, ERROR, or CRITICAL is passed to main()
  When: main() is called
  Then: The version string does not appear in the log output

- `e5f6a7b8-c9d0-1234-defa-012345678903`: Invalid verbosity raises a descriptive error.
  Source: po

  Given: An invalid verbosity string is passed to main()
  When: main() is called
  Then: A ValueError is raised with the invalid value and valid options listed

## Notes
- This is the template example feature shipped with the project skeleton.
- Tests live in `tests/version_test.py`.
- No out-of-scope items; this feature is complete and serves as a reference implementation.

## Architecture

### Module Structure
- `app/version.py` — `version()` function; reads `pyproject.toml` via `tomllib`
- `main.py` — `main(verbosity)` entry point; configures logging, calls `version()`

### Key Decisions (ADRs)

ADR-001: Read version from pyproject.toml at runtime
Decision: Use `tomllib` to read the version field from `pyproject.toml` at runtime
Reason: Avoids duplicating the version between `pyproject.toml` and a `__version__` constant
Alternatives considered: Hardcoded `__version__` in `app/__init__.py` — rejected to keep a single source of truth

ADR-002: Enforce verbosity via Literal type alias
Decision: Define `ValidVerbosity` as a `Literal` type alias for the five standard log level strings
Reason: Catches invalid verbosity values at the type-checker level before runtime
Alternatives considered: Accepting a plain `str` and validating at runtime only — rejected because it defers errors that the type checker can catch earlier

### Build Changes (needs PO approval: yes/no)
no
