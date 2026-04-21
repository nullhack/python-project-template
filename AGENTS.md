# Python Project Template

A Python template to quickstart any project with a production-ready workflow, quality tooling, and AI-assisted development.

## Workflow Overview

Features flow through 5 steps with a WIP limit of 1 feature at a time. The filesystem enforces WIP:
- `docs/features/backlog/<feature-stem>.feature` — features waiting to be worked on
- `docs/features/in-progress/<feature-stem>.feature` — exactly one feature being built right now
- `docs/features/completed/<feature-stem>.feature` — accepted and shipped features

```
STEP 1: SCOPE          (product-owner)     → discovery + Gherkin stories + criteria
STEP 2: ARCH           (system-architect)  → branch from main; read system.md + glossary.md + in-progress feature + targeted package files; write domain stubs; create/update domain-model.md; significant decisions as docs/adr/ADR-YYYY-MM-DD-<slug>.md; system.md rewritten
STEP 3: TDD LOOP       (software-engineer) → RED → GREEN → REFACTOR, one @id at a time
STEP 4: VERIFY         (system-architect)  → run all commands, review code against architecture
STEP 5: ACCEPT         (product-owner)     → demo, validate, SE merges branch to main with --no-ff, move .feature to completed/ (PO only)
```

### Branch Model

All feature work happens on branches. `main` is the single source of truth and receives code only via `--no-ff` merge from an approved feature branch.

**Normal flow**:
1. SE creates `feat/<stem>` from latest `main` at Step 2 start
2. All commits live on `feat/<stem>` through Steps 2–4
3. After PO acceptance (Step 5), SE merges `feat/<stem>` to `main` with `--no-ff`
4. SE deletes the feature branch

**Post-mortem flow** (failed feature restart):
1. Find the feature's original start commit
2. SE creates `fix/<stem>` from that commit
3. Post-mortem is committed as the first commit on `fix/<stem>`
4. Steps 2–5 rerun on `fix/<stem>`, then merge to `main` with `--no-ff`

**Git Safety Protocol** (absolute — never violate):
- No force push (`git push --force` forbidden)
- No history rewrite on pushed branches (no `rebase -i`, `commit --amend`, `reset --hard` after push)
- Use `git revert` to undo changes on shared history
- No commits directly to `main`

**Closed loop**: SA designs → SE builds → SA reviews. The same mind that designed the architecture verifies it. No context loss.

**PO picks the next feature from backlog. No agent self-selects.**

**Verification is adversarial.** The system-architect's job is to try to break the feature, not to confirm it works. The default hypothesis is "it might be broken despite green checks; prove otherwise."

## Roles

- **Product Owner (PO)** — AI agent. Interviews the stakeholder, writes discovery docs, Gherkin features, and acceptance criteria. Accepts or rejects deliveries. **Sole owner of all `.feature` file moves** (backlog → in-progress before Step 2; in-progress → completed after Step 5 acceptance).
- **Stakeholder** — Human. Answers PO's questions, provides domain knowledge, approves PO syntheses to confirm discovery is complete.
- **System Architect (SA)** — AI agent. Designs architecture, writes domain stubs, records decisions in ADRs, and verifies implementation respects those decisions. Owns `docs/domain-model.md`, `docs/system.md`, and `docs/adr/ADR-*.md`. Never edits or moves `.feature` files. Escalates spec gaps to PO.
- **Software Engineer (SE)** — AI agent. Implements everything: test bodies, production code, releases. Owns all `.py` files under the package. Never edits or moves `.feature` files. Escalates spec gaps to PO. If no `.feature` file is in `in-progress/`, stops and escalates to PO.

## Feature File Chain of Responsibility

`.feature` files are owned exclusively by the PO. **No other agent ever moves, creates, or edits them.**

| Transition | Who | When |
|---|---|---|
| `backlog/` → `in-progress/` | PO only | Before Step 2 begins; only if `Status: BASELINED` |
| `in-progress/` → `completed/` | PO only | After Step 5 acceptance |

**If an agent (SE or SA) finds no `.feature` in `in-progress/`**: update TODO.md with the correct `Next:` escalation line and stop. Never self-select a backlog feature.

## Agents

- **product-owner** — defines scope (Stage 1 Discovery + Stage 2 Specification), picks features, accepts deliveries
- **system-architect** — architecture and domain design (Step 2), adversarial technical review (Step 4)
- **software-engineer** — TDD loop, implementation, tests, code, git, releases (Step 3 + release)
- **designer** — creates and updates visual assets (SVG banners, logos) and maintains `docs/branding.md`
- **setup-project** — one-time setup to initialize a new project from this template

## Skills

| Skill | Used By | Step |
|---|---|---|
| `run-session` | all agents | every session |
| `select-feature` | product-owner | between features (idle state) |
| `define-scope` | product-owner | 1 |
| `architect` | system-architect | 2 |
| `implement` | software-engineer | 3 |
| `apply-patterns` | system-architect, software-engineer | 2, 3 (on-demand, when GoF pattern needed) |
| `refactor` | software-engineer | 3 (REFACTOR phase + preparatory refactoring) |
| `verify` | system-architect | 4 |
| `check-quality` | software-engineer | pre-handoff (redirects to `verify`) |
| `version-control` | software-engineer | Step 2 (branch creation), Step 5 (merge to main), post-mortem branches |
| `create-pr` | system-architect | post-acceptance |
| `git-release` | stakeholder | post-acceptance |
| `update-docs` | product-owner | post-acceptance + on stakeholder demand |
| `design-colors` | designer | branding, color, WCAG compliance |
| `design-assets` | designer | SVG asset creation and updates |
| `create-skill` | software-engineer | meta |
| `create-agent` | human-user | meta |

**Branding**: Agents that generate docs, diagrams, release names, or visual assets read `docs/branding.md` if present. Absent or blank fields fall back to defaults (adjective-animal release names, Mermaid default colors, no wording constraints). `docs/branding.md` and `docs/assets/` are owned by the designer agent.

**Session protocol**: Every agent loads `skill run-session` at session start. Load additional skills as needed for the current step.

## Step 1 — SCOPE

Step 1 has two stages:

### Stage 1 — Discovery (PO + stakeholder, iterative)

Discovery follows a block structure per session. See `skill define-scope` for the full protocol.

**Block A — Session Start**: Resume check (if `IN-PROGRESS`), read `domain-model.md` (existing entities), declare scope.

**Block B — General & Cross-cutting**: 5Ws, behavioral groups, bounded contexts. Active listening + reconciliation against `glossary.md` and `domain-model.md`.

**Block C — Feature Discovery (per feature)**: Detailed questions, pre-mortem, create/update `.feature` files.

**Block D — Session Close**: Append Q&A to `scope_journal.md`, update `glossary.md`, append synthesis to `discovery.md`, regression check on completed features, mark `COMPLETE`.

**Key rules**:
- PO owns `scope_journal.md`, `discovery.md`, `glossary.md`, and `.feature` files
- PO reads `domain-model.md` but never writes to it — entity suggestions go in `discovery.md` for SA formalization at Step 2
- Real-time split rule: >2 concerns or >8 candidate Examples → split immediately
- Completed feature touched and changed → move to `backlog/`

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
1. **PO** adds a `@bug` Example to the relevant `Rule:` in the `.feature` file and moves (or keeps) the feature in `backlog/` for normal scheduling.
2. **SA** handles Step 2 (architecture) and **SE** handles Step 3 (TDD loop) when the feature is selected for development. The SE implements the specific `@bug`-tagged test in `tests/features/<feature_slug>/` and also writes a `@given` Hypothesis property test in `tests/unit/` covering the whole class of inputs.
3. Both tests are required. SE follows the normal TDD loop (Step 3).

### Acceptance Failure & Restart

If the stakeholder reports failure **after the PO has attempted Step 5 acceptance**:
1. **PO does not move the `.feature` file to `completed/`**. Ensure it remains in `in-progress/`.
2. **Team compiles a compact post-mortem** (`docs/post-mortem/YYYY-MM-DD-<feature-stem>-<keyword>.md`, max 15 lines, process-level root cause).
3. **SE creates a fix branch** from the feature's original start commit: `git checkout -b fix/<stem> <start-sha>`. The post-mortem is committed as the first commit on this branch.
4. **PO scans `docs/post-mortem/`** and selects relevant files by matching `<feature-stem>` or `<failure-keyword>`.
5. **PO reads selected post-mortems**, then resets TODO.md to Step 2 with context.
6. **SA restarts Step 2** on `fix/<stem>`, reading relevant post-mortems as input. The same feature re-enters the ARCH step.
7. After acceptance, SE merges `fix/<stem>` to `main` with `--no-ff`.

Post-mortems are append-only, never edited. If a failure mode recurs, write a new file referencing the old one.

## Filesystem Structure

```
docs/
  scope_journal.md                    ← raw Q&A, PO appends after every session
  discovery.md                        ← session synthesis changelog, PO appends after every session
  domain-model.md                     ← living domain model, SA creates/updates at Step 2, PO reads only
  adr/                                ← one file per decision: ADR-YYYY-MM-DD-<slug>.md, SA creates at Step 2
  system.md                           ← current-state overview (completed features only), SA rewrites at Step 2, PO reviews at Step 5
  glossary.md                         ← living glossary, PO updates after each session
  branding.md                         ← project identity, colors, release naming, wording (designer owns)
  assets/                             ← logo.svg, banner.svg, and other visual assets (designer owns)
  context.md                          ← C4 Level 1 diagram, PO updates via update-docs skill
  container.md                        ← C4 Level 2 diagram, PO updates via update-docs skill (if multi-container)
  post-mortem/                         ← compact post-mortems, PO-owned, append-only
  features/
    backlog/<feature-stem>.feature    ← narrative + Rules + Examples
    in-progress/<feature-stem>.feature
    completed/<feature-stem>.feature

tests/
  features/<feature_slug>/
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
tests/features/<feature_slug>/<rule_slug>_test.py
```

### Stub Format

Stubs are auto-generated by pytest-beehave. The SA triggers generation at Step 2 end by running `uv run task test-fast`. pytest-beehave reads the in-progress `.feature` file and creates one skipped function per `@id`:

```python
@pytest.mark.skip(reason="not yet implemented")
def test_<feature_slug>_<@id>() -> None:
    """
    <@id steps raw text including new lines>
    """
```

### Markers
- `@pytest.mark.slow` — takes > 50ms; applied to Hypothesis tests and any test with I/O, network, or DB
- `@pytest.mark.deprecated` — auto-skipped by pytest-beehave; used for superseded Examples

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

During Step 3 (TDD Loop) and before handoff to Step 4:

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code
2. **One test green** — the specific test under work passes, plus `test-fast` still passes
3. **Quality tooling** — `lint`, `static-check`, full `test` with coverage run at handoff to SA

Design correctness is far more important than lint/pyright/coverage compliance. A well-designed codebase with minor lint issues is better than a lint-clean codebase with poor design.

## Verification Philosophy

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.
- Both are required. All-green automated checks are necessary but not sufficient for APPROVED.
- System-architect defaults to REJECTED unless correctness is proven.

## Release Management

Version format: `v{major}.{minor}.{YYYYMMDD}`

- Minor bump for new features; major bump for breaking changes
- Same-day second release: increment minor, keep same date
- Release name: defined by `docs/branding.md > Release Naming > Convention`; absent or blank defaults to version string only (no name)

**Releases happen from `main` only.** The SE ensures `main` is up to date with `origin/main` before creating a release. No releases from feature branches.

The stakeholder initiates the release process. When the stakeholder requests a release, the system-architect or software-engineer loads `skill git-release` to execute it.

## Session Management

Every session: load `skill run-session`. Read `TODO.md` first, update it at the end.

`TODO.md` is a session bookmark — not a project journal. See `.opencode/skills/run-session/SKILL.md` for the full structure including the Cycle State block used during Step 3.

## Setup

To initialize a new project from this template:
```bash
@setup-project
```

The setup agent will ask for your project name, GitHub username, author info, and configure all template placeholders.
