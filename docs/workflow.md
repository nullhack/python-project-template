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
│  STEP 2 — ARCHITECTURE                           agent: software-engineer   │
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
│  STEP 3 — TDD LOOP                              agent: software-engineer   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PREREQUISITES (stop if any fail — escalate to PO)                 │
│    [ ] Architecture section present in in-progress .feature file   │
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
│  │  │    Write test body (Given/When/Then → Arrange/Act/Assert) │ │
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
│  │  │    Apply: DRY → SOLID → OC → patterns                 │ │   │
│  │  │    Load design-patterns skill if smell detected       │ │   │
│  │  │    Add type hints and docstrings                      │ │   │
│  │  │    uv run task test-fast after each change            │ │   │
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
│      (do NOT add @id tests for coverage — @id tests are AC only)     │
│    All must pass before Self-Declaration                           │
│                                                                     │
│  SELF-DECLARATION (once, after all quality gates pass)             │
│    As a software-engineer I declare:                               │
│      * YAGNI: no code without a failing test — YES/NO | file:line │
│      * YAGNI: no speculative abstractions — YES/NO | file:line   │
│      * KISS: simplest solution that passes — YES/NO | file:line   │
│      * KISS: no premature optimization — YES/NO | file:line       │
│      * DRY: no duplication — YES/NO | file:line                  │
│      * DRY: no redundant comments — YES/NO | file:line            │
│      * SOLID-S: one reason to change per class — YES/NO | file:line│
│      * SOLID-O: open for extension, closed for modification        │
│                   — YES/NO | file:line                            │
│      * SOLID-L: subtypes substitutable — YES/NO | file:line       │
│      * SOLID-I: no forced unused deps — YES/NO | file:line        │
│      * SOLID-D: depend on abstractions, not concretions            │
│                   — YES/NO | file:line                            │
│      * OC-1: one level of indentation per method — YES/NO | file:line│
│      * OC-2: no else after return — YES/NO | file:line            │
│      * OC-3: primitive types wrapped — YES/NO | file:line        │
│      * OC-4: first-class collections — YES/NO | file:line        │
│      * OC-5: one dot per line — YES/NO | file:line                │
│      * OC-6: no abbreviations — YES/NO | file:line                │
│      * OC-7: ≤20 lines per function — YES/NO | file:line          │
│      * OC-8: ≤2 instance variables per class — YES/NO | file:line │
│      * OC-9: no getters/setters — YES/NO | file:line              │
│      * Patterns: no creational smell — YES/NO | file:line         │
│      * Patterns: no structural smell — YES/NO | file:line         │
│      * Patterns: no behavioral smell — YES/NO | file:line         │
│      * Semantic: tests operate at same abstraction as AC           │
│                   — YES/NO | file:line                            │
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
│    Self-Declaration from software-engineer                         │
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
│    For every YES claim: find the file:line — does it hold?          │
│    For every NO claim: is the deviation justified?                 │
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
    <rule-slug>_test.py     ← developer-written, one per Rule: block
                              function: test_<rule_slug>_<8char_hex>()
  unit/
    <anything>_test.py      ← developer-authored extras, no @id traceability
                              plain pytest or Hypothesis @given (developer choice)
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

## Self-Declaration
As a software-engineer I declare:
* YAGNI: no code without a failing test — AGREE/DISAGREE | file:line
* YAGNI: no speculative abstractions — AGREE/DISAGREE | file:line
* KISS: simplest solution that passes — AGREE/DISAGREE | file:line
* KISS: no premature optimization — AGREE/DISAGREE | file:line
* DRY: no duplication — AGREE/DISAGREE | file:line
* DRY: no redundant comments — AGREE/DISAGREE | file:line
* SOLID-S: one reason to change per class — AGREE/DISAGREE | file:line
* SOLID-O: open for extension, closed for modification — AGREE/DISAGREE | file:line
* SOLID-L: subtypes substitutable — AGREE/DISAGREE | file:line
* SOLID-I: no forced unused deps — AGREE/DISAGREE | file:line
* SOLID-D: depend on abstractions, not concretions — AGREE/DISAGREE | file:line
* OC-1: one level of indentation per method — AGREE/DISAGREE | deepest: file:line
* OC-2: no else after return — AGREE/DISAGREE | file:line
* OC-3: primitive types wrapped — AGREE/DISAGREE | file:line
* OC-4: first-class collections — AGREE/DISAGREE | file:line
* OC-5: one dot per line — AGREE/DISAGREE | file:line
* OC-6: no abbreviations — AGREE/DISAGREE | file:line
* OC-7: ≤20 lines per function, ≤50 per class — AGREE/DISAGREE | longest: file:line
* OC-8: ≤2 instance variables per class — AGREE/DISAGREE | file:line
* OC-9: no getters/setters — AGREE/DISAGREE | file:line
* Patterns: no creational smell — AGREE/DISAGREE | file:line
* Patterns: no structural smell — AGREE/DISAGREE | file:line
* Patterns: no behavioral smell — AGREE/DISAGREE | file:line
* Semantic: tests operate at same abstraction as AC — AGREE/DISAGREE | file:line

## Progress
- [x] @id:<hex>: <done>
- [~] @id:<hex>: <in progress>
- [ ] @id:<hex>: <next>

## Next
<one actionable sentence>
```

`## Cycle State` is updated at every phase transition. `## Self-Declaration` is written once after all quality gates pass in Step 3. Both sections are present only during Step 3; omit when in other steps.

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
