Feature: CLI Entrypoint

  The application exposes a command-line interface via `python -m app`.
  Running with `--help` prints the application name, tagline, and available
  options then exits with code 0. Running with `--version` prints the
  application name and its current version (read from package metadata, which
  is sourced from `pyproject.toml`) then exits with code 0. Running with an
  unrecognised flag exits with code 2 and prints a usage error. The entire
  implementation lives in `app/__main__.py` with no new dependencies — both
  `argparse` and `importlib.metadata` are Python stdlib.

  Status: BASELINED (2026-04-22)

  Rules (Business):
  - The version string is always read from package metadata at runtime; it is never hardcoded.
  - The help description must match the project tagline from `pyproject.toml`.
  - Both `--help` and `--version` exit with code 0.
  - Unrecognised arguments exit with code 2.

  Constraints:
  - Zero new dependencies (argparse and importlib.metadata are stdlib).
  - All production code lives in `app/__main__.py` only — no new files.
  - Version format follows the project's calver scheme (e.g. `7.2.20260423`); tests must not assume semver.

  Rule: Help output
    As a developer using the template
    I want to run `python -m app --help` and see the app name, tagline, and available options
    So that I know the CLI is wired up correctly and understand what the entry point offers

    @id:c1a2b3d4
    Example: Help flag prints description and exits successfully
      Given the application package is installed
      When the user runs `python -m app --help`
      Then the output contains the application name "temple8"
      And the output contains the tagline
      And the process exits with code 0

    @id:e5f6a7b8
    Example: Help flag lists available options
      Given the application package is installed
      When the user runs `python -m app --help`
      Then the output contains "--help"
      And the output contains "--version"

  Rule: Version output
    As a developer using the template
    I want to run `python -m app --version` and see the current version
    So that I can verify the installed package version matches what I expect

    @id:c9d0e1f2
    Example: Version flag prints name and version string then exits successfully
      Given the application package is installed
      When the user runs `python -m app --version`
      Then the output contains "temple8"
      And the output contains the version string from package metadata
      And the process exits with code 0

    @id:a3b4c5d6
    Example: Version string matches package metadata at runtime
      Given the application package is installed
      When the user runs `python -m app --version`
      Then the version in the output matches `importlib.metadata.version("temple8")`

  Rule: Unrecognised arguments
    As a developer using the template
    I want unrecognised flags to produce a clear error
    So that I know immediately when I have mistyped a command

    @id:e7f8a9b0
    Example: Unknown flag exits with error code
      Given the application package is installed
      When the user runs `python -m app --unknown-flag`
      Then the process exits with code 2

    @id:b1c2d3e4
    Example: No arguments runs without error
      Given the application package is installed
      When the user runs `python -m app` with no arguments
      Then the process exits with code 0

  ## Changes

  | Session | Q-IDs | Change |
  |---------|-------|--------|
  | 2026-04-22 S1 | Q8, Q9, Q11 | Created: CLI entrypoint with --help, --version, unknown-flag handling |
