# Python Project Template

A Python template to quickstart any project with a production-ready workflow, quality tooling, and AI-assisted development.

## Workflow Overview

Features flow through 5 steps with a WIP limit of 1 feature at a time. The filesystem enforces WIP:
- `docs/features/backlog/<feature-name>.feature` — features waiting to be worked on
- `docs/features/in-progress/<feature-name>.feature` — exactly one feature being built right now
- `docs/features/completed/<feature-name>.feature` — accepted and shipped features

```
STEP 1: SCOPE          (product-owner)  → discovery + Gherkin stories + criteria
STEP 2: ARCH           (software-engineer)      → read all features + existing package files, write domain stubs (signatures only, no bodies); decisions appended to docs/architecture.md
STEP 3: TDD LOOP       (software-engineer)      → RED → GREEN → REFACTOR, one @id at a time
STEP 4: VERIFY         (reviewer)       → run all commands, review code
STEP 5: ACCEPT         (product-owner)  → demo, validate, move .feature to completed/ (PO only)
```

**PO picks the next feature from backlog. Software-engineer never self-selects.**

**Verification is adversarial.** The reviewer's job is to try to break the feature, not to confirm it works. The default hypothesis is "it might be broken despite green checks; prove otherwise."

## Roles

- **Product Owner (PO)** — AI agent. Interviews the stakeholder, writes discovery docs, Gherkin features, and acceptance criteria. Accepts or rejects deliveries. **Sole owner of all `.feature` file moves** (backlog → in-progress before Step 2; in-progress → completed after Step 5 acceptance).
- **Stakeholder** — Human. Answers PO's questions, provides domain knowledge, approves PO syntheses to confirm discovery is complete.
- **Software Engineer** — AI agent. Architecture, test bodies, implementation, git. Never edits or moves `.feature` files. Escalates spec gaps to PO. If no `.feature` file is in `in-progress/`, stops and escalates to PO.
- **Reviewer** — AI agent. Adversarial verification. Reports spec gaps to PO. Never moves `.feature` files. After APPROVED report, stops and escalates to PO for Step 5.

## Feature File Chain of Responsibility

`.feature` files are owned exclusively by the PO. **No other agent ever moves or edits them.**

| Transition | Who | When |
|---|---|---|
| `backlog/` → `in-progress/` | PO only | Before Step 2 begins; only if `Status: BASELINED` |
| `in-progress/` → `completed/` | PO only | After Step 5 acceptance |

**If an agent (SE or reviewer) finds no `.feature` in `in-progress/`**: update TODO.md with the correct `Next:` escalation line and stop. Never self-select a backlog feature.

## Agents

- **product-owner** — defines scope (Stage 1 Discovery + Stage 2 Specification), picks features, accepts deliveries
- **software-engineer** — architecture, tests, code, git, releases (Steps 2-3 + release)
- **reviewer** — runs commands and reviews code at Step 4, produces APPROVED/REJECTED report
- **setup-project** — one-time setup to initialize a new project from this template

## Skills

| Skill | Used By | Step |
|---|---|---|
| `session-workflow` | all agents | every session |
| `feature-selection` | product-owner | between features (idle state) |
| `scope` | product-owner | 1 |
| `implementation` | software-engineer | 2, 3 |
| `design-patterns` | software-engineer | 2, 3 (on-demand, when GoF pattern needed) |
| `refactor` | software-engineer | 3 (REFACTOR phase + preparatory refactoring) |
| `verify` | reviewer | 4 |
| `code-quality` | software-engineer | pre-handoff (redirects to `verify`) |
| `pr-management` | software-engineer | 5 |
| `git-release` | software-engineer | 5 |
| `living-docs` | product-owner | 5 (after acceptance) + on stakeholder demand |
| `create-skill` | software-engineer | meta |
| `create-agent` | human-user | meta |

**Session protocol**: Every agent loads `skill session-workflow` at session start. Load additional skills as needed for the current step.

## Step 1 — SCOPE

Step 1 has two stages:

### Stage 1 — Discovery (PO + stakeholder, iterative)

Discovery is a continuous process. Sessions happen whenever scope needs to be established or refined — for a new project, new features, or new information. Every session follows the same structure:

**Session question order:**
1. **General** (5Ws + Success + Failure + Out-of-scope) — first session only, if the journal doesn't exist yet
2. **Cross-cutting** — behavior groups, bounded contexts, integration points, lifecycle events
3. **Per-feature** — one feature at a time; extract entities from `docs/discovery.md` Domain Model; gap-finding with CIT, Laddering, CI Perspective Change

**Real-time split rule**: if the PO detects >2 concerns or >8 candidate Examples for a feature during per-feature questions, split immediately — record the split in the journal, create stub `.feature` files, continue questions for both in the same session.

**After questions (PO alone, in order):**
1. Append answered Q&A (in groups) to `docs/discovery_journal.md` — only answered questions
2. Rewrite `.feature` description for each feature touched — others stay unchanged
3. Append session synthesis block to `docs/discovery.md` — LAST, after all `.feature` updates

**Session status**: the journal session header begins with `Status: IN-PROGRESS` (written before questions). Updated to `Status: COMPLETE` after all writes. If a session is interrupted, the next agent detects `IN-PROGRESS` and resumes the pending writes before starting a new session.

**Baselining**: PO writes `Status: BASELINED (YYYY-MM-DD)` in the `.feature` file when the stakeholder approves that feature's discovery and the decomposition check passes.

Commit per session: `feat(discovery): <session summary>`

### Stage 2 — Specification (PO alone, per feature)

Only runs on features with `Status: BASELINED`. No stakeholder involvement. If a gap requires stakeholder input, open a new Stage 1 session first.

**Step A — Stories**: derive one `Rule:` block per user story from the baselined feature description. INVEST gate: all 6 letters must pass.
Commit: `feat(stories): write user stories for <name>`

**Step B — Criteria**: PO writes `Example:` blocks with `@id` tags under each `Rule:`. Pre-mortem per Rule before writing any Examples. MoSCoW triage per Example. Examples are frozen after commit.
Commit: `feat(criteria): write acceptance criteria for <name>`

**Criteria are frozen**: no `Example:` changes after commit. Adding a new Example with a new `@id` replaces old.

### Bug Handling

When a defect is reported:
1. **PO** adds a `@bug @id:<hex>` Example to the relevant `Rule:` in the `.feature` file and moves (or keeps) the feature in `backlog/` for normal scheduling.
2. **SE** handles the bug when the feature is selected for development (standard Step 2–3 flow): implements the specific `@bug`-tagged test in `tests/features/<feature-name>/` and also writes a `@given` Hypothesis property test in `tests/unit/` covering the whole class of inputs.
3. Both tests are required. SE follows the normal TDD loop (Step 3).

## Filesystem Structure

```
docs/
  discovery_journal.md                ← raw Q&A, PO appends after every session
  discovery.md                        ← synthesis changelog, PO appends after every session
  architecture.md                     ← all architectural decisions, SE appends after Step 2
  glossary.md                         ← living glossary, PO updates via living-docs skill
  c4/
    context.md                        ← C4 Level 1 diagram, PO updates via living-docs skill
    container.md                      ← C4 Level 2 diagram, PO updates via living-docs skill
  features/
    backlog/<feature-name>.feature    ← narrative + Rules + Examples
    in-progress/<feature-name>.feature
    completed/<feature-name>.feature

tests/
  features/<feature-name>/
    <rule_slug>_test.py               ← one per Rule: block, software-engineer-written
  unit/
    <anything>_test.py                ← software-engineer-authored extras (no @id traceability)
```

Tests in `tests/unit/` are software-engineer-authored extras not covered by any `@id` criterion. Any test style is valid — plain `assert` or Hypothesis `@given`. Use Hypothesis when the test covers a **property** that holds across many inputs (mathematical invariants, parsing contracts, value object constraints). Use plain pytest for specific behaviors or single edge cases discovered during refactoring.

- `@pytest.mark.slow` is mandatory on every `@given`-decorated test (Hypothesis is genuinely slow)
- `@example(...)` is optional but encouraged when using `@given` to document known corner cases
- No `@id` tags — tests with `@id` belong in `tests/features/`, written by software-engineer

## Test File Layout

```
tests/features/<feature-name>/<rule_slug>_test.py
```

### Stub Format (mandatory)

```python
@pytest.mark.skip(reason="not yet implemented")
def test_<feature_slug>_<@id>() -> None:
    """
    <@id steps raw text including new lines>
    """
```

### Markers
- `@pytest.mark.slow` — takes > 50ms; applied to Hypothesis tests and any test with I/O, network, or DB
- `@pytest.mark.deprecated` — auto-skipped by conftest; used for superseded Examples

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

# Run tests with coverage report generation
uv run task test-build

# Lint and format
uv run task lint

# Type checking
uv run task static-check

# Build documentation
uv run task doc-build
```

## Code Quality Standards

- **Principles (in priority order)**: YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicate code > failing code > no code
- **Linting**: ruff format, ruff check, Google docstring convention, `noqa` forbidden
- **Type checking**: pyright, 0 errors required
- **Coverage**: 100% (measured against your actual package)
- **Function length**: ≤ 20 lines (code lines only, excluding docstrings)
- **Class length**: ≤ 50 lines (code lines only, excluding docstrings)
- **Max nesting**: 2 levels
- **Instance variables**: ≤ 2 per class *(exception: dataclasses, Pydantic models, value objects, and TypedDicts are exempt — they may carry as many fields as the domain requires)*
- **Semantic alignment**: tests must operate at the same abstraction level as the acceptance criteria they cover

### Software-Engineer Quality Gate Priority Order

During Step 3 (TDD Loop), correctness priorities are:

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriated design patterns > complex code > complicated code > failing code > no code
2. **One test green** — the specific test under work passes, plus `test-fast` still passes
3. **Reviewer code-design check** — reviewer verifies design + semantic alignment (no lint/pyright/coverage yet)
5. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run only at software-engineer handoff (before Step 4)

Design correctness is far more important than lint/pyright/coverage compliance. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

## Verification Philosophy

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.
- Both are required. All-green automated checks are necessary but not sufficient for APPROVED.
- Reviewer defaults to REJECTED unless correctness is proven.

## Release Management

Version format: `v{major}.{minor}.{YYYYMMDD}`

- Minor bump for new features; major bump for breaking changes
- Same-day second release: increment minor, keep same date
- Each release gets a unique adjective-animal name

Use `@software-engineer /skill git-release` for the full release process. When requested by the stakeholder

## Session Management

Every session: load `skill session-workflow`. Read `TODO.md` first, update it at the end.

`TODO.md` is a session bookmark — not a project journal. See `.opencode/skills/session-workflow/SKILL.md` for the full structure including the Cycle State block used during Step 3.

## Setup

To initialize a new project from this template:
```bash
@setup-project
```

The setup agent will ask for your project name, GitHub username, author info, and configure all template placeholders.
