# Feature Discovery: display-version

## Status
completed

## Entities

**Nouns**: version string, pyproject.toml, log output, verbosity level, entry point  
**Verbs**: retrieve, display, log, configure, validate

## Rules
- Version is read from `pyproject.toml` at runtime using `tomllib`
- Log verbosity is controlled by a `ValidVerbosity` parameter passed to `main()`
- Valid verbosity levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL
- An invalid verbosity value raises a `ValueError` with the invalid value and the list of valid options
- The version string is logged at INFO level; it is visible at DEBUG and INFO but not at WARNING or above

## Constraints
- No hardcoded `__version__` constant — `pyproject.toml` is the single source of truth
- Entry point: `app/__main__.py` (`main(verbosity)` function)
- Version logic: `app/version.py` (`version()` function)

## Questions
All questions answered. Discovery frozen.
