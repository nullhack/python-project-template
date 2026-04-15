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

**Verification is adversarial.** The reviewer's job is to try to break the feature, not to confirm it works. The default hypothesis is "it might be broken despite green checks; prove otherwise."

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
| `extend-criteria` | any agent | when a gap is found |
| `create-skill` | developer | meta |

## Development Commands

```bash
# Install dependencies
uv sync --all-extras

# Run the application (for humans)
uv run task run

# Run the application with timeout (for agents — prevents hanging on infinite loops)
# Exit code 124 means the process was killed; treat as FAIL
timeout 10s uv run task run

# Run tests (fast, no coverage)
uv run task test-fast

# Run full test suite with coverage
uv run task test

# Run slow tests only
uv run task test-slow

# Lint and format
uv run task lint

# Type checking
uv run task static-check

# Serve documentation
uv run task doc-serve
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
test_<short_title>                       # function name
```

### Docstring Format (mandatory)
```python
def test_email_requires_at_symbol():
    """a1b2c3d4-e5f6-7890-abcd-ef1234567890

    Given: An email address without an @ symbol
    When: EmailAddress is constructed
    Then: A ValueError is raised with a descriptive message
    """
    # Given
    invalid = "not-an-email"
    # When
    # Then
    with pytest.raises(ValueError):
        EmailAddress(invalid)
```

Rules:
- First line: `<uuid>` only — no description
- Mandatory blank line between UUID and Given
- `# Given`, `# When`, `# Then` comments in the test body
- Assert behavior, not structure — no `isinstance()`, `type()`, or internal attributes
- Never use `noqa` or `type: ignore`
- Never use `pytest.skip` or `pytest.mark.xfail` without written justification in the docstring

## Code Quality Standards

- **Principles (in priority order)**: YAGNI > KISS > DRY > SOLID > Object Calisthenics
- **Linting**: ruff, Google docstring convention, `noqa` forbidden
- **Type checking**: pyright, 0 errors required
- **Coverage**: 100% (measured against your actual package, not `app` unless that is your package)
- **Function length**: ≤ 20 lines
- **Class length**: ≤ 50 lines
- **Max nesting**: 2 levels
- **Instance variables**: ≤ 2 per class
- **Semantic alignment**: tests must operate at the same abstraction level as the acceptance criteria they cover. If the AC says "when the user presses W," the test must send W through the actual input mechanism, not call an internal helper.
- **Integration tests**: multi-component features and features involving user interaction require at least one `@pytest.mark.integration` test that exercises the public entry point.

## Verification Philosophy

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.
- Both are required. All-green automated checks are necessary but not sufficient for APPROVED.

## Feature Document Format

One file per feature, lives in `docs/features/`. PO writes the top sections; developer adds `## Architecture`.

**Naming:** `<verb>-<object>.md` — imperative verb first, kebab-case, 2–4 words.
Examples: `display-version.md`, `authenticate-user.md`, `export-metrics-csv.md`
Title matches: `# Feature: <Verb> <Object>` in Title Case.

```markdown
# Feature: <Verb> <Object>

## User Stories
- As a <role>, I want <goal> so that <benefit>

## Acceptance Criteria
- `<uuid>`: <Short description ending with a period>.
  Source: <stakeholder | po | developer | reviewer | bug>

  Given: <precondition>
  When: <action>
  Then: <single observable outcome>

## Notes
<constraints, risks, out-of-scope items>

## Architecture  ← Developer adds this in Step 2
### Module Structure
### Key Decisions (ADRs)
### Build Changes (needs PO approval: yes/no)
```

**Source field values:**
- `stakeholder` — an external stakeholder gave this requirement to the PO
- `po` — the PO originated this criterion independently
- `developer` — a gap found during Step 4 implementation
- `reviewer` — a gap found during Step 5 verification
- `bug` — a post-merge regression; the feature doc was reopened

**Gaps and Defects:** When any agent finds a missing behavior, load `skill extend-criteria`. It provides the decision rule (gap within scope vs. new feature), UUID assignment, and commit protocol. For post-merge defects, the feature doc moves from `completed/` back to `in-progress/`.

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
- [x] `<uuid>`: <description>          ← done
- [~] `<uuid>`: <description>          ← in progress
- [ ] `<uuid>`: <description>          ← next
- [-] `<uuid>`: <description>          ← cancelled

## Next
<One actionable sentence>
```

## Setup

To initialize a new project from this template:
```bash
@setup-project
```

The setup agent will ask for your project name, GitHub username, author info, and configure all template placeholders.
