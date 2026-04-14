# Python Project Template

A Python template to quickstart any project with a production-ready workflow, quality tooling, and AI-assisted development.

## Workflow Overview

Features flow through 6 steps with a WIP limit of 1 feature at a time. The filesystem enforces WIP:
- `docs/features/backlog/` — features waiting to be worked on
- `docs/features/in-progress/` — exactly one feature being built right now
- `docs/features/completed/` — accepted and shipped features

```
STEP 1: SCOPE          (product-owner)  → define user stories + acceptance criteria
STEP 2: BOOTSTRAP+ARCH (developer)      → set up build, design module structure
STEP 3: TEST FIRST     (developer)      → write failing tests mapped to UUIDs
STEP 4: IMPLEMENT      (developer)      → Red-Green-Refactor, commit per green test
STEP 5: VERIFY         (reviewer)       → run all commands, review code
STEP 6: ACCEPT         (product-owner)  → demo, validate, merge, tag
```

**PO picks the next feature from backlog. Developer never self-selects.**

## Agents

- **product-owner** — defines scope, acceptance criteria, picks features, accepts deliveries
- **developer** — architecture, tests, code, git, releases (Steps 2–4 + release)
- **reviewer** — runs commands and reviews code at Step 5, produces APPROVED/REJECTED report
- **setup-project** — one-time setup to initialize a new project from this template

## Skills

| Skill | Used By | Step |
|---|---|---|
| `session-workflow` | all agents | every session |
| `scope` | product-owner | 1 |
| `tdd` | developer | 3 |
| `implementation` | developer | 4 |
| `verify` | reviewer | 5 |
| `code-quality` | developer | pre-handoff |
| `pr-management` | developer | 6 |
| `git-release` | developer | 6 |
| `create-skill` | developer | meta |

## Development Commands

```bash
# Install dependencies
uv venv && uv pip install '.[dev]'

# Run the application (for humans)
task run

# Run the application with timeout (for agents — prevents hanging on infinite loops)
# Exit code 124 means the process was killed; treat as FAIL
timeout 10s task run

# Run tests (fast, no coverage)
task test-fast

# Run full test suite with coverage
task test

# Run slow tests only
task test-slow

# Lint and format
task lint

# Type checking
task static-check

# Serve documentation
task doc-serve
```

## Test Conventions

### Markers (3 only)
- `@pytest.mark.unit` — isolated, one function/class, no external state
- `@pytest.mark.integration` — multiple components, external state (DB, network, filesystem)
- `@pytest.mark.slow` — takes > 50ms; additionally applied to DB, Hypothesis, and terminal I/O tests

Every test gets exactly one of `unit` or `integration`. Slow tests additionally get `slow`.

### File and Function Naming
```
<descriptive-group-name>_test.py         # file name
test_<condition>_should_<outcome>        # function name
```

### Docstring Format (mandatory)
```python
def test_user_with_invalid_email_should_raise_validation_error():
    """a1b2c3d4-e5f6-7890-abcd-ef1234567890: Email validation rejects invalid input.

    Given: An email address without an @ symbol
    When: EmailAddress is constructed
    Then: A ValueError is raised with a descriptive message
    """
    # Given
    invalid = "not-an-email"
    # When / Then
    with pytest.raises(ValueError):
        EmailAddress(invalid)
```

Rules:
- First line: `<uuid>: <short description ending with a period>`
- Mandatory blank line between first line and Given
- `# Given`, `# When`, `# Then` comments in the test body
- Assert behavior, not structure — no `isinstance()`, `type()`, or internal attributes
- Never use `noqa`, `pytest.skip`, or `type: ignore`

## Code Quality Standards

- **Principles (in priority order)**: YAGNI > KISS > DRY > SOLID > Object Calisthenics
- **Linting**: ruff, Google docstring convention, `noqa` forbidden
- **Type checking**: pyright, 0 errors required
- **Coverage**: 100% (measured against your actual package, not `app` unless that is your package)
- **Function length**: ≤ 20 lines
- **Class length**: ≤ 50 lines
- **Max nesting**: 2 levels
- **Instance variables**: ≤ 2 per class

## Feature Document Format

One file per feature, lives in `docs/features/`. PO writes the top sections; developer adds `## Architecture`.

```markdown
# Feature: <Name>

## User Stories
- As a <role>, I want <goal> so that <benefit>

## Acceptance Criteria
- `<uuid>`: <Short description ending with a period>.
  Given: <precondition>
  When: <action>
  Then: <single observable outcome>
  Test strategy: unit | integration

## Notes
<constraints, risks, out-of-scope items>

## Architecture  ← Developer adds this in Step 2
### Module Structure
### Key Decisions (ADRs)
### Build Changes (needs PO approval: yes/no)
```

## Release Management

Version format: `v{major}.{minor}.{YYYYMMDD}`

- Minor bump for new features; major bump for breaking changes
- Same-day second release: increment minor, keep same date
- Each release gets a unique adjective-animal name generated from the PR/commit content

Use `@developer /skill git-release` for the full release process.

## Session Management

Every session: load `skill session-workflow`. Read `TODO.md` first, update it at the end.

`TODO.md` is a 15-line bookmark — not a project journal:
```markdown
# Current Work

Feature: <name>
Step: <1-6> (<step name>)
Source: docs/features/in-progress/<name>.md

## Progress
- [x] `<uuid>`: <description>
- [ ] `<uuid>`: <description>  ← next

## Next
<One actionable sentence>
```

## Setup

To initialize a new project from this template:
```bash
@setup-project
```

The setup agent will ask for your project name, GitHub username, author info, and configure all template placeholders.
