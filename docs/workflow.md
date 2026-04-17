# Development Workflow

This document describes the complete feature lifecycle used to develop software with this framework.

---

## Overview

Features flow through 6 steps with a WIP limit of 1 feature at a time. The filesystem enforces the limit:

```
docs/features/backlog/<name>.feature      ← waiting
docs/features/in-progress/<name>.feature  ← exactly one being built
docs/features/completed/<name>.feature    ← accepted and shipped
```

Each step has a designated agent and a specific deliverable. No step is skipped.

---

## Full Workflow Diagram

```
╔══════════════════════════════════════════════════════════════════════╗
║                    FEATURE LIFECYCLE (WIP = 1)                       ║
╚══════════════════════════════════════════════════════════════════════╝

  FILESYSTEM ENFORCES WIP:
  backlog/<name>.feature  →  in-progress/<name>.feature  →  completed/<name>.feature


┌─────────────────────────────────────────────────────────────────────┐
│  STEP 1 — SCOPE                              agent: product-owner   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Phase 1 — Project Discovery                                        │
│  [runs ONCE; skip if discovery.md BASELINED]                        │
│  [adding features later: append new Qs to Session 1, re-fill]      │
│                                                                     │
│    Session 1 — Individual Scope Elicitation                         │
│      5Ws + Success + Failure + Out-of-scope                         │
│      Gap-finding per answer: CIT · Laddering · CI Perspective       │
│      [new questions from elucidation added in the moment]           │
│      Level 1: paraphrase each answer on the spot                    │
│      → PO writes synthesis → stakeholder confirms or corrects       │
│      → PO runs silent pre-mortem on confirmed synthesis             │
│      [template §1: synthesis confirmed → unlocks Session 2]         │
│                                                                     │
│    Session 2 — Cluster / Big Picture                                │
│      Questions target clusters and cross-cutting concerns           │
│      Gap-finding per cluster: CIT · Laddering · CI Perspective      │
│      [new questions from elucidation added in the moment]           │
│      Level 1: paraphrase each answer                                │
│      Level 2: synthesis when transitioning between clusters         │
│      [template §2: all clusters answered → unlocks Session 3]       │
│                                                                     │
│    Session 3 — Synthesis Approval + Feature Derivation              │
│      PO produces full synthesis across all clustered areas          │
│      → stakeholder approves or corrects; PO refines until approved  │
│      [template §3: approval → unlocks domain analysis]              │
│      Domain analysis: nouns/verbs → subject areas                   │
│      Name features (FDD "Action object" / Affinity clusters)        │
│      Create backlog/<name>.feature stubs                            │
│      Status: BASELINED written to discovery.md                      │
│                                                                     │
│  Phase 2 — Feature Discovery (repeats per feature)                  │
│  [each .feature has its own 3-session discovery template]           │
│                                                                     │
│    Session 1 — Individual Entity Elicitation                        │
│      Populate Entities table from project discovery                 │
│      Gap-finding per answer: CIT · Laddering · CI Perspective       │
│      [new questions from elucidation added in the moment]           │
│      Level 1: paraphrase each answer                                │
│      → PO writes synthesis → stakeholder confirms or corrects       │
│      → PO runs silent pre-mortem on confirmed synthesis             │
│      [template §1: synthesis confirmed → unlocks Session 2]         │
│                                                                     │
│    Session 2 — Cluster / Big Picture for this Feature               │
│      Questions target clusters of behavior within this feature      │
│      Gap-finding per cluster: CIT · Laddering · CI Perspective      │
│      [new questions from elucidation added in the moment]           │
│      Level 1: paraphrase · Level 2: cluster transition summaries    │
│      [template §2: all clusters answered → unlocks Session 3]       │
│                                                                     │
│    Session 3 — Feature Synthesis Approval + Story Derivation        │
│      PO produces synthesis of feature scope and clusters            │
│      → stakeholder approves or corrects; PO refines until approved  │
│      Clusters → candidate user stories (Rules)                      │
│      Status: BASELINED written to .feature discovery section        │
│      [template §3: approval + stories → unlocks decomp check]       │
│                                                                     │
│    DECOMPOSITION CHECK                                              │
│      >2 distinct concerns OR >8 candidate Examples?                 │
│      YES → split into separate .feature files, re-run Phase 2       │
│      NO  → proceed                                                  │
│                                                                     │
│  Phase 3 — Stories (PO alone)                                       │
│    Clusters from Phase 2 Session 2 → one Rule: block per story      │
│    INVEST gate: all 6 letters must pass before committing           │
│    commit: feat(stories): write user stories for <name>             │
│                                                                     │
│  Phase 4 — Criteria (PO alone)                                      │
│    4.1 Pre-mortem per Rule (all Rules checked before Examples)      │
│    4.2 Write @id-tagged Examples (Given/When/Then, declarative)     │
│        MoSCoW triage: Must / Should / Could per Example             │
│    4.3 Review checklist                                             │
│    commit: feat(criteria): write acceptance criteria for <name>     │
│    ★ FROZEN — changes require @deprecated + new Example             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓  PO picks feature from backlog
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 2 — ARCHITECTURE                           agent: developer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PREREQUISITES (stop if any fail — escalate to PO)                 │
│    [ ] in-progress/ has no .feature file (WIP = 1)                 │
│    [ ] feature Status: BASELINED                                    │
│    [ ] feature has Rule: + Example: + @id tags                      │
│    [ ] package name confirmed (pyproject.toml → directory exists)   │
│                                                                     │
│  mv backlog/<name>.feature → in-progress/<name>.feature             │
│                                                                     │
│  READ (all before writing anything)                                 │
│    docs/features/discovery.md (project-level)                      │
│    ALL backlog .feature files (discovery + entities sections)       │
│    in-progress .feature file (full: Rules + Examples + @id)        │
│                                                                     │
│  DOMAIN ANALYSIS                                                    │
│    From Entities table + Rules (Business) in .feature file:        │
│    Nouns → named classes, value objects, aggregates                 │
│    Verbs → method names with typed signatures                       │
│    Datasets → named types (not bare dict/list)                      │
│    Bounded Context check: same word, different meaning across       │
│      features? → module boundary goes there                         │
│    Cross-feature entities → candidate shared domain layer           │
│                                                                     │
│  SILENT PRE-MORTEM (before writing anything)                        │
│    "In 6 months this design is a mess. What mistakes did we make?"  │
│    For each candidate class: >2 ivars? >1 reason to change?         │
│    For each external dep: is it behind a Protocol?                  │
│    Any noun serving double duty across modules?                     │
│    Any structure missing a named design pattern?                    │
│    → If pattern smell detected: load skill design-patterns          │
│                                                                     │
│  Write Architecture section in in-progress .feature file            │
│    ### Module Structure                                             │
│      <package>/domain/<noun>.py                                     │
│        class <Noun>:          ← named class + responsibilities      │
│            field: Type                                              │
│        def <verb>(<Noun>) -> <Type>: ...  ← typed signatures        │
│        class <DepName>(Protocol): ...     ← external dep contract   │
│      <package>/domain/service.py          ← cross-entity operations │
│      <package>/adapters/<dep>.py          ← Protocol impl           │
│    ### Key Decisions                                                │
│      ADR-NNN: <title>                                               │
│      Decision: <what>                                               │
│      Reason: <why in one sentence>                                  │
│      Alternatives considered: <what was rejected and why>           │
│    ### Build Changes (new runtime deps — requires PO approval)      │
│                                                                     │
│  NOTE: signatures are informative — tests/implementation may        │
│  refine them; record significant changes as ADR updates             │
│                                                                     │
│  ARCHITECTURE SMELL CHECK — hard gate (fix before commit)           │
│    [ ] No planned class with >2 responsibilities (SOLID-S)         │
│    [ ] No planned class with >2 instance variables (OC-8)          │
│    [ ] All external deps assigned a Protocol/Adapter (SOLID-D +    │
│        Hexagonal Architecture)                                      │
│    [ ] No noun with different meaning across planned modules        │
│        (DDD Bounded Context)                                        │
│    [ ] No missing Creational pattern: repeated construction         │
│        without Factory/Builder                                      │
│    [ ] No missing Structural pattern: type-switching logic          │
│        without Strategy/Visitor                                     │
│    [ ] No missing Behavioral pattern: state machine or scattered    │
│        notification without State/Observer                          │
│    [ ] Each ADR consistent with each @id AC — no contradictions    │
│    [ ] Technically infeasible story → escalate to PO               │
│                                                                     │
│  commit: feat(<name>): add architecture                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 3 — TEST FIRST                             agent: developer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  uv run task gen-tests   →  creates tests/features/<name>/          │
│                              one <rule-slug>_test.py per Rule:      │
│                              test_<rule_slug>_<hex>() per Example   │
│  Write test bodies (real assertions, not raise NotImplementedError) │
│  Confirm every test FAILS (ImportError / AssertionError)            │
│  ★ STOP — reviewer checks test design + semantic alignment          │
│  ★ WAIT for APPROVED                                                │
│  commit: test(<name>): write failing tests                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 4 — IMPLEMENT                              agent: developer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  For each failing test (one at a time):                             │
│                                                                     │
│    RED → GREEN → REFACTOR → SELF-DECLARE ─STOP─ REVIEWER ─WAIT─   │
│                                                          ↓ APPROVED │
│                                                       COMMIT        │
│                                                          ↓          │
│                                                    next test        │
│                                                                     │
│  RED:         confirm test fails                                    │
│  GREEN:       minimum code to pass (YAGNI + KISS only)              │
│  REFACTOR:    DRY → SOLID → Object Calisthenics (9 rules)           │
│               → type hints → docstrings                             │
│  SELF-DECLARE: write ## Self-Declaration block in TODO.md           │
│               24 first-person declarations (YAGNI×2, KISS×2,        │
│               DRY×2, SOLID×5, OC×9, Patterns×3, Semantic×1)        │
│               "As a developer I declare [rule] — YES | file:line"   │
│               or N/A | reason; load design-patterns if smell found   │
│  REVIEWER:    code-design check only (no lint/pyright/coverage)     │
│               reviewer independently verifies YES claims            │
│               reviewer does NOT re-audit self-declared failures     │
│  COMMIT:      feat(<name>): implement <what>                        │
│                                                                     │
│  After all tests green:                                             │
│    lint + static-check + test + timeout run  (all must pass)        │
│    developer pre-mortem (2-3 sentences)                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 5 — VERIFY                                  agent: reviewer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Default hypothesis: broken despite green checks                    │
│                                                                     │
│  1. Read feature file — all @id Examples, interaction model         │
│  2. Check commit history — one commit per test, clean status        │
│  3. Production-grade gate:                                          │
│       app exits cleanly + output changes with input                 │
│  4. Code review (stop on first failure):                            │
│       4a Correctness (dead code, DRY, YAGNI)                        │
│       4b KISS (one thing, nesting, size)                            │
│       4c SOLID (5-row table)                                        │
│       4d Object Calisthenics (9-row table)                          │
│       4e Design Patterns (5 smells)                                 │
│       4f Tests (docstrings, contracts, @id coverage, naming)        │
│       4g Code Quality (noqa, type hints, docstrings, coverage)      │
│  5. Run: gen-tests --orphans → lint → static-check → test           │
│  6. Interactive verification (if UI involved)                       │
│  7. Written report: APPROVED or REJECTED                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ APPROVED
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 6 — ACCEPT                             agent: product-owner   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PO runs/observes the feature (real user interaction)               │
│  Checks against original Rule: user stories                         │
│                                                                     │
│  ACCEPTED:                                                          │
│    mv in-progress/<name>.feature → completed/<name>.feature         │
│    developer creates PR (squash merge) + tags release               │
│                                                                     │
│  REJECTED:                                                          │
│    feedback in TODO.md → back to relevant step                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Feature File Structure

Each feature is a single `.feature` file. The free-form description before the first `Rule:` contains all discovery content added progressively through the workflow:

```
Feature: <title>

  Discovery:

  Status: ELICITING | BASELINED (YYYY-MM-DD)

  Entities:
  | Type | Name | Candidate Class/Method | In Scope |

  Rules (Business):
  - <business rule>

  Constraints:
  - <non-functional requirement>

  Session 1 — Individual Entity Elicitation:
  | ID | Question | Answer | Status |     ← OPEN / ANSWERED
  Synthesis: <PO synthesis — confirmed by stakeholder>

  Session 2 — Cluster / Big Picture:
  | ID | Question | Answer | Status |
  Clusters: <named topic clusters derived from answers>

  Session 3 — Feature Synthesis:
  Synthesis: <full synthesis across clusters>
  Approved: YES / NO

  Architecture:                         ← added at Step 2 by developer

  ### Module Structure
  - <package>/domain/entity.py — ...

  ### Key Decisions
  ADR-001: <title>
  Decision: <what>
  Reason: <why>

  Rule: <story title>
    As a <role>
    I want <goal>
    So that <benefit>

    @id:a3f2b1c4
    Example: <scenario>
      Given <context>
      When <action>
      Then <observable outcome>
```

Two discovery sources:
- `docs/features/discovery.md` — project-level 3-session discovery (once per project; additive for new features)
- Feature file description — per-feature 3-session discovery, entities, clusters, architecture

---

## Supporting Tools

| Command | When | Purpose |
|---|---|---|
| `uv run task gen-tests` | Step 3, Step 4 | Reads `.feature` files → creates/syncs test stubs in `tests/features/` |
| `uv run task gen-tests -- --check` | Before gen-tests | Dry run — preview what would change |
| `uv run task gen-tests -- --orphans` | Step 5 | List tests with no matching `@id` — already validated by gen-tests |
| `uv run task gen-todo` | Every session | Reads in-progress `.feature` → syncs `TODO.md` |
| `uv run task gen-id` | Step 1 Phase 4 | Generate 8-char hex `@id` for a new Example |
| `uv run task test-fast` | Step 4 cycle | Fast test run (no coverage) — used during Red-Green-Refactor |
| `uv run task test` | Handoff, Step 5 | Full suite with coverage — must reach 100% |
| `uv run task lint` | Handoff, Step 5 | ruff — must exit 0 |
| `uv run task static-check` | Handoff, Step 5 | pyright — must exit 0, 0 errors |
| `timeout 10s uv run task run` | Handoff, Step 5 | App must exit cleanly (exit 124 = hang = fix it) |

---

## Test Layout

```
tests/
  features/<feature-name>/
    <rule-slug>_test.py     ← generated by gen-tests, one per Rule: block
                              function: test_<rule_slug>_<8char_hex>()
  unit/
    <anything>_test.py      ← developer-authored extras, no @id traceability
                              plain pytest or Hypothesis @given (developer's choice)
```

---

## TODO.md Structure

```markdown
# Current Work

Feature: <name>
Step: <1-6> (<step name>)
Source: docs/features/in-progress/<name>.feature

## Cycle State
Test: @id:<hex> — <description>
Phase: RED | GREEN | REFACTOR | SELF-DECLARE | REVIEWER(code-design) | COMMITTED

## Self-Declaration (@id:<hex>)
As a developer I declare this code follows YAGNI-1 (no abstractions beyond current AC) — YES | `file:line`
As a developer I declare this code follows YAGNI-2 (no speculative parameters or flags) — YES | `file:line`
As a developer I declare this code follows KISS-1 (every function has one job) — YES | `file:line`
As a developer I declare this code follows KISS-2 (no unnecessary indirection) — YES | `file:line`
As a developer I declare this code follows DRY-1 (no duplicated logic) — YES | `file:line`
As a developer I declare this code follows DRY-2 (every shared concept in one place) — YES | `file:line`
As a developer I declare this code follows SOLID-S (one reason to change) — YES | `file:line`
As a developer I declare this code follows SOLID-O (extension not modification) — YES | `file:line` or N/A | reason
As a developer I declare this code follows SOLID-L (subtypes fully substitutable) — YES | `file:line` or N/A | reason
As a developer I declare this code follows SOLID-I (no forced stub methods) — YES | `file:line` or N/A | reason
As a developer I declare this code follows SOLID-D (domain depends on Protocols) — YES | `file:line`
As a developer I declare this code follows OC-1 (max one indent level per method) — YES | deepest: `file:line`
As a developer I declare this code follows OC-2 (no else after return) — YES | `file:line` or N/A | reason
As a developer I declare this code follows OC-3 (no bare primitives as domain concepts) — YES | `file:line` or N/A | reason
As a developer I declare this code follows OC-4 (no bare collections as domain values) — YES | `file:line` or N/A | reason
As a developer I declare this code follows OC-5 (no chained dot navigation) — YES | `file:line` or N/A | reason
As a developer I declare this code follows OC-6 (no abbreviations) — YES | `file:line` or N/A | reason
As a developer I declare this code follows OC-7 (functions ≤20 lines, classes ≤50 lines) — YES | longest: `file:line`
As a developer I declare this code follows OC-8 (≤2 instance variables per class) — YES | `file:line`
As a developer I declare this code follows OC-9 (no getters/setters) — YES | `file:line` or N/A | reason
As a developer I declare this code has no missing Creational pattern (no smell: repeated construction or scattered instantiation) — YES | `file:line` or N/A | reason
As a developer I declare this code has no missing Structural pattern (no smell: feature envy or parallel conditionals on type) — YES | `file:line` or N/A | reason
As a developer I declare this code has no missing Behavioral pattern (no smell: large state machine, scattered notification, or repeated algorithm skeleton) — YES | `file:line` or N/A | reason
As a developer I declare test abstraction matches AC level (semantic alignment) — YES | `file:line`

## Progress
- [x] @id:<hex>: <done> — reviewer(code-design) APPROVED
- [~] @id:<hex>: <in progress>
- [ ] @id:<hex>: <next>

## Next
<one actionable sentence>
```

`## Cycle State` is updated at every phase transition. `## Self-Declaration` is replaced per-test cycle. Both sections are present only during Step 4; omit when in other steps.

---

## Roles

| Role | Type | Responsibilities |
|---|---|---|
| **Stakeholder** | Human | Answers questions, provides domain knowledge, approves syntheses |
| **Product Owner** | AI agent | Interviews stakeholder, writes `.feature` files, picks features, accepts deliveries |
| **Developer** | AI agent | Architecture, tests, code, git, releases |
| **Reviewer** | AI agent | Adversarial verification — defaults to REJECTED until proven correct |

---

## Quality Gates (non-negotiable)

| Gate | Standard |
|---|---|
| Test coverage | 100% |
| Type errors (pyright) | 0 |
| Lint errors (ruff) | 0 |
| Function length | ≤ 20 lines |
| Class length | ≤ 50 lines |
| Max nesting | 2 levels |
| Instance variables per class | ≤ 2 |
| `noqa` comments | 0 |
| `type: ignore` comments | 0 |
| Orphaned tests | 0 |
| Hypothesis tests missing `@pytest.mark.slow` | 0 |
