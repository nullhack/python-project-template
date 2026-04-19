# Development Workflow

This document describes the complete feature lifecycle used to develop software with this framework.

---

## Overview

Features flow through 5 steps with a WIP limit of 1 feature at a time. The filesystem enforces the limit:

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
│  Stage 1 — Discovery (PO + stakeholder, iterative)                  │
│  Sessions happen any time scope needs establishing or refining.     │
│  Every session follows the same structure.                          │
│                                                                     │
│    SESSION START                                                     │
│      Check docs/discovery_journal.md last block for Status:        │
│        IN-PROGRESS → resume interrupted session first               │
│        (missing file) → create journal + discovery.md from templates│
│      Append new session header to journal:                          │
│        ## YYYY-MM-DD — Session N                                    │
│        Status: IN-PROGRESS          ← written BEFORE any questions  │
│                                                                     │
│    QUESTION ORDER                                                    │
│      1. General (5Ws + Success + Failure + Out-of-scope)            │
│         [first session only, if journal did not exist yet]          │
│         Gap-finding per answer: CIT · Laddering · CI Perspective    │
│         Level 1: paraphrase each answer on the spot                 │
│      2. Cross-cutting (behavior groups, bounded contexts,           │
│         integration points, lifecycle events)                       │
│         Level 2: synthesis when transitioning between groups        │
│      3. Per-feature (one feature at a time)                         │
│         Extract entities from docs/discovery.md Domain Model        │
│         Gap-finding: CIT · Laddering · CI Perspective               │
│         Silent pre-mortem per feature                               │
│         REAL-TIME SPLIT: if >2 concerns OR >8 candidate Examples    │
│           → split immediately, record in journal, create stubs,     │
│             continue questions for both features in this session    │
│                                                                     │
│    AFTER QUESTIONS (PO alone, in this order)                        │
│      1. Append answered Q&A to journal (in groups; answered only)   │
│      2. Rewrite .feature description for each touched feature       │
│         [untouched features stay exactly as-is]                     │
│      3. Append session synthesis block to discovery.md (LAST)       │
│         [only after all .feature files are updated]                 │
│      4. Mark journal session: Status: COMPLETE                      │
│      commit: feat(discovery): <session summary>                     │
│                                                                     │
│    BASELINING A FEATURE                                             │
│      When stakeholder approves feature discovery + decomp passes:   │
│      PO writes Status: BASELINED (YYYY-MM-DD) in the .feature file  │
│      Gate: feature may only enter Stage 2 when BASELINED            │
│                                                                     │
│  Stage 2 — Specification (PO alone, per feature)                    │
│  Only runs on features with Status: BASELINED.                      │
│  If a gap needs stakeholder input → open a new Stage 1 session.    │
│                                                                     │
│    Step A — Stories                                                  │
│      Derive one Rule: block per user story from feature description │
│      INVEST gate: all 6 letters must pass before committing         │
│      commit: feat(stories): write user stories for <name>           │
│                                                                     │
│    Step B — Criteria                                                 │
│      Pre-mortem per Rule (all Rules checked before Examples)        │
│      Write @id-tagged Examples (Given/When/Then, declarative)       │
│      MoSCoW triage: Must / Should / Could per Example               │
│      Review checklist                                               │
│      commit: feat(criteria): write acceptance criteria for <name>   │
│      ★ FROZEN — changes require @deprecated + new Example           │
│                                                                     │
│  Bug Handling                                                        │
│    PO adds @bug @id:<hex> Example to relevant Rule: in .feature     │
│    SE implements @id test in tests/features/<name>/                 │
│    SE also writes @given Hypothesis test in tests/unit/ (whole class)│
│    Both tests required · SE follows normal TDD loop (Step 3)        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓  PO picks feature from backlog — only if Status: BASELINED
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 2 — ARCHITECTURE                           agent: software-engineer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PREREQUISITES (stop if any fail — escalate to PO)                 │
│    [ ] in-progress/ has no .feature file (WIP = 1)                 │
│    [ ] feature Status: BASELINED                                    │
│    [ ] feature has Rule: + Example: + @id tags                      │
│    [ ] package name confirmed (pyproject.toml → directory exists)   │
│                                                                     │
│  READ (all before writing anything)                                 │
│    docs/discovery.md (project-level synthesis changelog)           │
│    ALL backlog .feature files (narrative + Rules + Examples)        │
│    in-progress .feature file (full: Rules + Examples + @id)        │
│    ALL existing .py files in <package>/  ← know what exists first  │
│                                                                     │
│  DOMAIN ANALYSIS                                                    │
│    From Domain Model in docs/discovery.md + Rules (Business):      │
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
│  WRITE STUBS INTO PACKAGE (signatures only — bodies must be `...`) │
│    If file exists → add class/method; do not remove existing code  │
│    If file does not exist → create with signatures only             │
│    File placement (common patterns, not required names):            │
│      <package>/domain/<noun>.py   ← entities, value objects        │
│      <package>/domain/service.py  ← cross-entity operations        │
│      Do not pre-create ports/ or adapters/ without a concrete dep  │
│    Stub rules:                                                      │
│      Bodies: `...` only — no logic, no conditionals                │
│      No docstrings — add after GREEN when signatures are stable     │
│      No inline comments, no TODO, no speculative code              │
│                                                                     │
│  RECORD ARCHITECTURAL DECISIONS (significant only)                  │
│    Append to docs/architecture.md                                  │
│      ## YYYY-MM-DD — <feature>: <title>                            │
│      Decision: <what>  Reason: <why>                               │
│      Alternatives considered: <what was rejected and why>           │
│                                                                     │
│  ARCHITECTURE SMELL CHECK — hard gate (fix before commit)           │
│    [ ] No class with >2 responsibilities (SOLID-S)                 │
│    [ ] No behavioural class with >2 instance variables (OC-8;      │
│        dataclasses, Pydantic models, value objects, TypedDicts      │
│        are exempt)                                                  │
│    [ ] All external deps assigned a Protocol (SOLID-D + Hexagonal) │
│        N/A if no external dependencies identified in scope          │
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
│  commit: feat(<name>): add architecture stubs                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 3 — TDD LOOP                              agent: software-engineer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PREREQUISITES (stop if any fail — escalate to PO)                 │
│    [ ] Architecture stubs present in <package>/ (Step 2 committed) │
│    [ ] Read docs/architecture.md — all architectural decisions      │
│    [ ] All tests written in tests/features/<feature>/              │
│                                                                     │
│  Build TODO.md test list                                            │
│    List all @id tags from in-progress .feature file                │
│    Order: fewest dependencies first; most impactful within that    │
│    Each @id = one TODO item, status: pending                       │
│                                                                     │
│  OUTER LOOP — one @id at a time                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Pick next pending @id → mark in_progress in TODO.md       │   │
│  │  (WIP limit: exactly one in_progress at all times)         │   │
│  │                                                             │   │
│  │  INNER LOOP                                                 │   │
│  │  ┌───────────────────────────────────────────────────────┐ │   │
│  │  │  RED                                                  │ │   │
│  │  │    Read stubs in <package>/ — base test on them       │ │   │
│  │  │    Write test body (Given/When/Then → Arrange/Act/Assert) │ │
│  │  │    Update stub signatures as needed — edit .py directly │ │ │
│  │  │    uv run task test-fast                              │ │   │
│  │  │    EXIT: this @id FAILS                               │ │   │
│  │  │    (if it passes: test is wrong — fix it first)       │ │   │
│  │  ├───────────────────────────────────────────────────────┤ │   │
│  │  │  GREEN                                                │ │   │
│  │  │    Write minimum code — YAGNI + KISS only             │ │   │
│  │  │    (no DRY, SOLID, OC here — those belong in REFACTOR)│ │   │
│  │  │    uv run task test-fast                              │ │   │
│  │  │    EXIT: this @id passes AND all prior tests pass     │ │   │
│  │  │    (fix implementation only; do not advance @id)      │ │   │
│  │  ├───────────────────────────────────────────────────────┤ │   │
│  │  │  REFACTOR                                             │ │   │
│  │  │    Load skill refactor — follow its protocol          │ │   │
│  │  │    uv run task test-fast after each individual change │ │   │
│  │  │    EXIT: test-fast passes; no smells remain           │ │   │
│  │  └───────────────────────────────────────────────────────┘ │   │
│  │                                                             │   │
│  │  Mark @id completed in TODO.md                             │   │
│  │  Commit when a meaningful increment is green               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│  Repeat until all @id items completed                              │
│                                                                     │
│  QUALITY GATE (all @id green)                                      │
│    uv run task lint                                                │
│    uv run task static-check                                        │
│    uv run task test           (coverage must be 100%)              │
│    timeout 10s uv run task run                                     │
│    coverage < 100%: add test in tests/unit/ for uncovered branch   │
│      (do NOT add @id tests for coverage — @id tests are AC only)   │
│    All must pass before handing off                                │
│                                                                     │
│  SELF-DECLARATION (once, after all quality gates pass)             │
│    Communicate verbally to reviewer:                               │
│      * YAGNI, KISS, DRY, SOLID, OC checklist — AGREE/DISAGREE     │
│        with file:line evidence for each claim                      │
│      * DISAGREE requires inline justification                      │
│                                                                     │
│  → Hand off to Step 4 (Verify)                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 4 — VERIFY                                  agent: reviewer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Default hypothesis: BROKEN. Prove otherwise or REJECT.             │
│                                                                     │
│  4a. READ                                                           │
│    in-progress .feature file (Rules + Examples + @id)             │
│    Self-Declaration communicated verbally by software-engineer     │
│                                                                     │
│  4b. pyproject.toml GATE                                           │
│    git diff main -- pyproject.toml                                 │
│    Any change → REJECT immediately                                 │
│    software-engineer must revert + get stakeholder approval        │
│                                                                     │
│  4c. COMMIT HISTORY                                                 │
│    git log --oneline main..HEAD                                    │
│    All commits follow conventional commit format?                  │
│    No "fix tests", "wip", "temp" commits?                          │
│                                                                     │
│  4d. COMMANDS                                                       │
│    uv run task lint           (must exit 0)                        │
│    uv run task static-check   (must exit 0)                        │
│    uv run task test           (must exit 0, coverage 100%)         │
│    timeout 10s uv run task run (exit 124 = hung = REJECT)          │
│                                                                     │
│  4e. PRODUCTION GATE                                                │
│    Does the application behave as described in the feature file?   │
│    Run manually or via integration test — not just green CI        │
│    Input → output check for each Rule: block                       │
│                                                                     │
│  4f. CODE REVIEW (semantic — not covered by tooling)               │
│    [ ] Tests operate at same abstraction level as AC              │
│    [ ] No test asserts implementation details                      │
│    [ ] Each @id test covers exactly one Example                   │
│    [ ] No logic in tests (no if/for/while)                         │
│    [ ] Module structure matches Architecture section               │
│    [ ] No external dependency outside adapters/                   │
│    [ ] Docstrings explain why, not what                             │
│                                                                     │
│  4g. SELF-DECLARATION AUDIT                                        │
│    For every AGREE claim: find the file:line — does it hold?        │
│    For every DISAGREE claim: is the deviation justified?           │
│    Undeclared violations → REJECT                                  │
│                                                                     │
│  4h. INTERACTIVE (if any doubt remains)                            │
│    Ask software-engineer one targeted question per ambiguity        │
│    Do not proceed to report if question is unanswered              │
│                                                                     │
│  4i. REPORT                                                         │
│    APPROVED — all gates passed, no undeclared violations           │
│    REJECTED — list each failure with file:line and required fix    │
│                                                                     │
│  On APPROVED → notify PO                                            │
│  On REJECTED → return to software-engineer (Step 3 quality gate)  │
└─────────────────────────────────────────────────────────────────────┘
                               ↓ APPROVED
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 5 — ACCEPT                             agent: product-owner   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PO runs/observes the feature (real user interaction)               │
│  Checks against original Rule: user stories                         │
│                                                                     │
│  ACCEPTED:                                                          │
│    mv in-progress/<name>.feature → completed/<name>.feature         │
│    software-engineer creates PR (squash merge) + tags release               │
│                                                                     │
│  REJECTED:                                                          │
│    feedback in TODO.md → back to relevant step                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Feature File Structure

Each feature is a single `.feature` file. The description contains the feature description and Status line. All Q&A lives in `docs/discovery_journal.md`; architectural decisions live in `docs/architecture.md`.

```
Feature: <title>

  <2–4 sentence description of what this feature does and why it exists.>

  Status: ELICITING | BASELINED (YYYY-MM-DD)

  Rules (Business):
  - <business rule>

  Constraints:
  - <non-functional requirement>

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

Three discovery sources:
- `docs/discovery_journal.md` — raw Q&A from all scope sessions (PO, append-only)
- `docs/discovery.md` — synthesis changelog, domain model, feature list (PO, append-only)
- `docs/architecture.md` — all architectural decisions (software-engineer, append-only)

---

## Architecture Artifacts

Architectural decisions made during Step 2 are appended to `docs/architecture.md`:

```markdown
## YYYY-MM-DD — <feature-name>: <short title>

Decision: <what was decided — one sentence>
Reason: <why — one sentence>
Alternatives considered: <what was rejected and why>
Feature: <feature-name>
```

Write a block only for non-obvious decisions with real trade-offs — module boundaries, external dependency strategy, Protocol vs. concrete class, data model choices. Routine YAGNI choices do not need a record. The file is append-only; when a decision changes, append a new block that supersedes the old one.

Domain entity and service stubs (signatures, no bodies) live directly in the package under `<package>/domain/`, `<package>/ports/`, and `<package>/adapters/` — written at Step 2, filled in during Step 3.

---

## Supporting Tools

| Command | When | Purpose |
|---|---|---|
| `uv run task gen-todo` | Every session | Reads in-progress `.feature` → syncs `TODO.md` |
| `uv run task test-fast` | Step 3 cycle | Fast test run (no coverage) — used during Red-Green-Refactor |
| `uv run task test` | Handoff, Step 4 | Full suite with coverage — must reach 100% |
| `uv run task lint` | Handoff, Step 4 | ruff — must exit 0 |
| `uv run task static-check` | Handoff, Step 4 | pyright — must exit 0, 0 errors |
| `timeout 10s uv run task run` | Handoff, Step 4 | App must exit cleanly (exit 124 = hang = fix it) |

---

## Test Layout

```
tests/
  features/<feature-name>/
    <rule_slug>_test.py     ← software-engineer-written, one per Rule: block
                              function: test_<feature_slug>_<8char_hex>()
  unit/
    <anything>_test.py      ← software-engineer-authored extras, no @id traceability
                              plain pytest or Hypothesis @given (software-engineer choice)
```

---

## TODO.md Structure

```markdown
# Current Work

Feature: <name>
Step: <1-5> (<step name>)
Source: docs/features/in-progress/<name>.feature

## Cycle State
Test: @id:<hex> — <description>
Phase: RED | GREEN | REFACTOR

## Progress
- [x] @id:<hex>: <done>
- [~] @id:<hex>: <in progress>
- [ ] @id:<hex>: <next>

## Next
<one actionable sentence>
```

`## Cycle State` is updated at every phase transition. This section is present only during Step 3; omit when in other steps.

---

## Roles

| Role | Type | Responsibilities |
|---|---|---|
| **Stakeholder** | Human | Answers questions, provides domain knowledge, approves syntheses |
| **Product Owner** | AI agent | Interviews stakeholder, writes `.feature` files, picks features, accepts deliveries |
| **Software Engineer** | AI agent | Architecture, tests, code, git, releases |
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
| Instance variables per class | ≤ 2 (behavioural classes only; dataclasses, Pydantic models, value objects, TypedDicts are exempt) |
| `noqa` comments | 0 |
| `type: ignore` comments | 0 |
| Orphaned tests | 0 |
| Hypothesis tests missing `@pytest.mark.slow` | 0 |
