Feature: Verbosity control
  As a developer
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
