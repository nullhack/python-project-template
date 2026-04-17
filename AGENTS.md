# Python Project Template

A Python template to quickstart any project with a production-ready workflow, quality tooling, and AI-assisted development.

## Workflow Overview

Features flow through 6 steps with a WIP limit of 1 feature at a time. The filesystem enforces WIP:
- `docs/features/backlog/<feature-name>.feature` — features waiting to be worked on
- `docs/features/in-progress/<feature-name>.feature` — exactly one feature being built right now
- `docs/features/completed/<feature-name>.feature` — accepted and shipped features

```
STEP 1: SCOPE          (product-owner)  → discovery + Gherkin stories + criteria
STEP 2: ARCH           (developer)      → read all backlog features, design module structure
STEP 3: TEST FIRST     (developer)      → sync stubs, write failing tests
STEP 4: IMPLEMENT      (developer)      → Red-Green-Refactor, commit per green test
STEP 5: VERIFY         (reviewer)       → run all commands, review code
STEP 6: ACCEPT         (product-owner)  → demo, validate, move folder to completed/
```

**PO picks the next feature from backlog. Developer never self-selects.**

**Verification is adversarial.** The reviewer's job is to try to break the feature, not to confirm it works. The default hypothesis is "it might be broken despite green checks; prove otherwise."

## Roles

- **Product Owner (PO)** — AI agent. Interviews the stakeholder, writes discovery docs, Gherkin features, and acceptance criteria. Accepts or rejects deliveries.
- **Stakeholder** — Human. Answers PO's questions, provides domain knowledge, approves PO syntheses to confirm discovery is complete.
- **Developer** — AI agent. Architecture, test bodies, implementation, git. Never edits `.feature` files. Escalates spec gaps to PO.
- **Reviewer** — AI agent. Adversarial verification. Reports spec gaps to PO.

## Agents

- **product-owner** — defines scope (4 phases), picks features, accepts deliveries
- **developer** — architecture, tests, code, git, releases (Steps 2-4 + release)
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
| `code-quality` | developer | pre-handoff (redirects to `verify`) |
| `pr-management` | developer | 6 |
| `git-release` | developer | 6 |
| `create-skill` | developer | meta |

**Session protocol**: Every agent loads `skill session-workflow` at session start. Load additional skills as needed for the current step.

## Step 1 — SCOPE (4 Phases)

### Phase 1 — Project Discovery (once per project)
PO creates `docs/features/discovery.md` using the 3-session template. **Skip Phase 1 entirely if `discovery.md` Status is BASELINED.** To add features to an existing project: append new questions to Session 1 and re-fill from there.

- **Session 1** — Individual scope elicitation: 5Ws + Success + Failure + Out-of-scope. Gap-finding per answer using CIT, Laddering, and CI Perspective Change. PO writes synthesis; stakeholder confirms or corrects. PO runs silent pre-mortem on confirmed synthesis. Template §1 must be confirmed before Session 2.
- **Session 2** — Cluster / big picture: questions target clusters and cross-cutting concerns. Gap-finding per cluster. Level 2 synthesis when transitioning between clusters. Template §2 must be complete before Session 3.
- **Session 3** — Synthesis approval + feature derivation: PO produces full synthesis of all clusters; stakeholder approves or corrects (PO refines until approved). Domain analysis: nouns/verbs → subject areas → FDD "Action object" feature names. Create `backlog/<name>.feature` stubs. Write `Status: BASELINED` to `discovery.md`.

### Phase 2 — Feature Discovery (per feature)
Each `.feature` file has its own 3-session discovery template in its description. **Sessions are enforced by the template: each section must be filled before proceeding to the next.**

- **Session 1** — Individual entity elicitation: populate Entities table from project discovery; generate questions from entity gaps using CIT, Laddering, CI Perspective Change. PO writes synthesis; stakeholder confirms. Silent pre-mortem on confirmed synthesis.
- **Session 2** — Cluster / big picture: questions target clusters of behavior within this feature. Gap-finding per cluster. Level 2 cluster transition summaries.
- **Session 3** — Feature synthesis approval + story derivation: PO produces synthesis of feature scope and clusters; stakeholder approves or corrects (PO refines until approved). Clusters become candidate user stories (Rules). Write `Status: BASELINED` to `.feature` discovery section.

**Decomposition check**: after Session 3, does this feature span >2 distinct concerns OR have >8 candidate Examples? YES → split into separate `.feature` files, re-run Phase 2. NO → proceed.

### Phase 3 — Stories (PO alone)
Clusters from Phase 2 Session 2 → one `Rule:` block per user story. Each `Rule:` has the user story header (`As a / I want / So that`) as its description — no `Example:` blocks yet. INVEST gate: all 6 letters must pass. Commit: `feat(stories): write user stories for <name>`

### Phase 4 — Criteria (PO alone)
Pre-mortem per Rule (all Rules must be checked before writing Examples). Write `Example:` blocks — declarative Given/When/Then, MoSCoW triage (Must/Should/Could) per Example. Review checklist (4.3). Commit: `feat(criteria): write acceptance criteria for <name>`

**Criteria are frozen**: no `Example:` changes after commit. Change = `@deprecated` tag + new Example with new `@id`.

## Filesystem Structure

```
docs/features/
  discovery.md                        ← project-level (Status + Questions only)
  backlog/<feature-name>.feature      ← one per feature; discovery + Rules + Examples
  in-progress/<feature-name>.feature  ← file moves here at Step 2
  completed/<feature-name>.feature    ← file moves here at Step 6

tests/
  features/<feature-name>/
    <rule-slug>_test.py               ← one per Rule: block, stubs from gen-tests
  unit/
    <anything>_test.py                ← developer-authored extras (no @id traceability)
```

Tests in `tests/unit/` are developer-authored extras not covered by any `@id` criterion. Any test style is valid — plain `assert` or Hypothesis `@given`. Use Hypothesis when the test covers a **property** that holds across many inputs (mathematical invariants, parsing contracts, value object constraints). Use plain pytest for specific behaviors or single edge cases discovered during refactoring.

- `@pytest.mark.slow` is mandatory on every `@given`-decorated test (Hypothesis is genuinely slow)
- `@example(...)` is optional but encouraged when using `@given` to document known corner cases
- No `@id` tags — tests with `@id` belong in `tests/features/`, generated by `gen-tests`

## Gherkin Format

```gherkin
Feature: Bounce physics

  Discovery:

  Status: BASELINED (2026-01-10)

  Entities:
  | Type | Name | Candidate Class/Method | In Scope |
  |------|------|----------------------|----------|
  | Noun | Ball | Ball | Yes |
  | Verb | Bounce | Ball.bounce() | Yes |

  Rules (Business):
  - Ball velocity reverses on wall contact

  Constraints:
  - Physics runs at 60fps

  Questions:
  | ID | Question | Answer | Status |
  |----|----------|--------|--------|
  | Q1 | Does gravity apply? | No, constant velocity | ANSWERED |

  All questions answered. Discovery frozen.

  Rule: Wall bounce
    As a game engine
    I want balls to bounce off walls
    So that gameplay feels physical

    @id:a3f2b1c4
    Example: Ball bounces off top wall
      Given a ball moving upward reaches y=0
      When the physics engine processes the next frame
      Then the ball velocity y-component becomes positive

    @deprecated @id:b5c6d7e8
    Example: Old behavior no longer needed
      Given ...
      When ...
      Then ...
```

- Each feature is a **single `.feature` file**; user stories are `Rule:` blocks within it
- The feature description (free text before the first `Rule:`) contains all discovery content: Status, Entities, Rules (business), Constraints, Questions, and later Architecture
- `@id:<8-char-hex>` — generated with `uv run task gen-id`
- `@deprecated` — marks superseded criteria; `gen-tests` adds `@pytest.mark.deprecated` to the mapped test
- `Example:` keyword (not `Scenario:`)
- Each Example must be observably distinct from every other

## Test Conventions

### Test Stub Generation

```bash
uv run task gen-tests              # sync all features
uv run task gen-tests -- --check   # dry run
uv run task gen-tests -- --orphans # list orphaned tests
```

- backlog / in-progress: full write (create stubs, update docstrings, rename functions)
- completed: only toggle `@pytest.mark.deprecated` (no docstring changes)
- Orphaned tests (no matching `@id`) get `@pytest.mark.skip(reason="orphan: ...")`

### Test File Layout

```
tests/features/<feature-name>/<rule-slug>_test.py
```

### Function Naming

```python
def test_<rule_slug>_<8char_hex>() -> None:
```

### Docstring Format (mandatory)

```python
@pytest.mark.unit
def test_wall_bounce_a3f2b1c4() -> None:
    """
    Given: A ball moving upward reaches y=0
    When: The physics engine processes the next frame
    Then: The ball velocity y-component becomes positive
    """
    # Given
    # When
    # Then
    raise NotImplementedError
```

### Markers (4 total)
- `@pytest.mark.unit` — isolated, one function/class, no external state
- `@pytest.mark.integration` — multiple components, external state
- `@pytest.mark.slow` — takes > 50ms; additionally applied alongside `unit` or `integration`
- `@pytest.mark.deprecated` — auto-skipped by conftest hook; added by `gen-tests`

Every test gets exactly one of `unit` or `integration`. Slow tests additionally get `slow`.

## Development Commands

```bash
# Install dependencies
uv sync --all-extras

# Run the application (for humans)
uv run task run

# Run the application with timeout (for agents — prevents hanging)
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

# Generate an 8-char hex ID
uv run task gen-id

# Sync test stubs from .feature files
uv run task gen-tests

# Serve documentation
uv run task doc-serve
```

## Code Quality Standards

- **Principles (in priority order)**: YAGNI > KISS > DRY > SOLID > Object Calisthenics
- **Linting**: ruff, Google docstring convention, `noqa` forbidden
- **Type checking**: pyright, 0 errors required
- **Coverage**: 100% (measured against your actual package)
- **Function length**: ≤ 20 lines
- **Class length**: ≤ 50 lines
- **Max nesting**: 2 levels
- **Instance variables**: ≤ 2 per class
- **Semantic alignment**: tests must operate at the same abstraction level as the acceptance criteria they cover
- **Integration tests**: multi-component features require at least one `@pytest.mark.integration` test exercising the public entry point

### Developer Quality Gate Priority Order

During Step 4 (Implementation), correctness priorities are:

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns
2. **One test green** — the specific test under work passes, plus `test-fast` still passes
3. **Reviewer code-design check** — reviewer verifies design + semantic alignment (no lint/pyright/coverage)
4. **Commit** — only after reviewer APPROVED
5. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run only at developer handoff (before Step 5)

Design correctness is far more important than lint/pyright/coverage compliance. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

## Verification Philosophy

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.
- Both are required. All-green automated checks are necessary but not sufficient for APPROVED.
- Reviewer defaults to REJECTED unless correctness is proven.

## Deprecation Process

1. PO adds `@deprecated` tag to Example in `.feature` file
2. Run `uv run task gen-tests` — script adds `@pytest.mark.deprecated` to mapped test
3. Deprecated tests auto-skip via conftest hook
4. Feature is done when all non-deprecated tests pass
5. No special folder — features move to `completed/` normally

## Release Management

Version format: `v{major}.{minor}.{YYYYMMDD}`

- Minor bump for new features; major bump for breaking changes
- Same-day second release: increment minor, keep same date
- Each release gets a unique adjective-animal name

Use `@developer /skill git-release` for the full release process.

## Session Management

Every session: load `skill session-workflow`. Read `TODO.md` first, update it at the end.

`TODO.md` is a session bookmark — not a project journal. See `docs/workflow.md` for the full structure including the Cycle State and Self-Declaration blocks used during Step 4.

## Setup

To initialize a new project from this template:
```bash
@setup-project
```

The setup agent will ask for your project name, GitHub username, author info, and configure all template placeholders.
