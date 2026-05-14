Feature: CLI Entrypoint

  The command-line interface is the primary entry point for users interacting
  with the application. It provides help output, version information, and
  graceful error handling for unrecognised arguments.

  Rule: Help output
    As a user
    I want to see helpful usage information
    So that I can discover available commands and flags

    Example: Help output contains app name and tagline
      Given the application package is installed
      When the user runs `python -m app --help`
      Then the output contains the application name "temple8"
      And the output contains the tagline
      And the process exits with code 0

    Example: Help output lists help and version flags
      Given the application package is installed
      When the user runs `python -m app --help`
      Then the output contains "--help"
      And the output contains "--version"

  Rule: Version output
    As a user
    I want to see the application version
    So that I can verify which version is installed

    Example: Version output contains app name and version
      Given the application package is installed
      When the user runs `python -m app --version`
      Then the output contains "temple8"
      And the output contains the version string from package metadata
      And the process exits with code 0

    Example: Version output matches metadata
      Given the application package is installed
      When the user runs `python -m app --version`
      Then the version in the output matches `importlib.metadata.version("temple8")`

  Rule: Unrecognised arguments
    As a user
    I want clear feedback when I provide invalid arguments
    So that I know what went wrong

    Example: Unrecognised flag exits with code 2
      Given the application package is installed
      When the user runs `python -m app --unknown-flag`
      Then the process exits with code 2

    Example: No arguments exits with code 0
      Given the application package is installed
      When the user runs `python -m app` with no arguments
      Then the process exits with code 0
