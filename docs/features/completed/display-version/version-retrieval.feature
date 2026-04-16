Feature: Version retrieval
  As a developer
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
