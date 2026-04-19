Feature: Display version

  Reads the application version from pyproject.toml at runtime and logs it at INFO
  level. Log output is controlled by a verbosity parameter; the version is visible
  at DEBUG and INFO but suppressed at WARNING and above. An invalid verbosity value
  raises a descriptive error.

  Status: COMPLETED

  Rules (Business):
  - Version is read from pyproject.toml at runtime using tomllib
  - Log verbosity is controlled by a ValidVerbosity parameter passed to main()
  - Valid verbosity levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - An invalid verbosity value raises a ValueError with the invalid value and valid options
  - The version string is logged at INFO level; visible at DEBUG and INFO, not at WARNING+

  Constraints:
  - No hardcoded __version__ constant — pyproject.toml is the single source of truth
  - Entry point: app/__main__.py (main(verbosity) function)
  - Version logic: app/version.py (version() function)

  Rule: Version retrieval
    As a software-engineer
    I want to retrieve the application version programmatically
    So that I can display or log it at runtime

    @id:3f2a1b4c
    Example: Version string is read from pyproject.toml
      Given pyproject.toml exists with a version field
      When version() is called
      Then the returned string matches the version in pyproject.toml

    @id:7a8b9c0d
    Example: Version call emits an INFO log message
      Given pyproject.toml exists with a version field
      When version() is called
      Then an INFO log message in the format "Version: <version>" is emitted

  Rule: Verbosity control
    As a software-engineer
    I want to control log verbosity via a parameter
    So that I can tune output for different environments

    @id:a1b2c3d4
    Example: Version appears in logs at DEBUG and INFO verbosity
      Given a verbosity level of DEBUG or INFO is passed to main()
      When main() is called
      Then the version string appears in the log output

    @id:b2c3d4e5
    Example: Version is absent from logs at WARNING and above
      Given a verbosity level of WARNING, ERROR, or CRITICAL is passed to main()
      When main() is called
      Then the version string does not appear in the log output

    @id:e5f6a7b8
    Example: Invalid verbosity raises a descriptive error
      Given an invalid verbosity string is passed to main()
      When main() is called
      Then a ValueError is raised with the invalid value and valid options listed
