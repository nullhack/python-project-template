# Scope Journal: temple8

---

## 2026-04-22 — Session 1

Status: IN-PROGRESS

### General

| ID | Question | Answer |
|----|----------|--------|
| Q1 | Who are the users? | Python engineers starting a new project who want rigorous tooling without the setup cost. |
| Q2 | What does the product do at a high level? | Provides a fully configured Python project skeleton: CI, quality tooling, test infrastructure, and an AI-assisted five-step delivery workflow. |
| Q3 | Why does it exist — what problem does it solve? | Setting up a production-grade Python environment from scratch is expensive and often skipped; engineers then accrue quality debt from day one. |
| Q4 | When and where is it used? | At project inception — cloned once, then evolved as features are added via the built-in workflow. |
| Q5 | Success — what does "done" look like? | An engineer clones the template and ships a meaningful first feature within a single session, with all quality gates passing. |
| Q6 | Failure — what must never happen? | The template introduces more friction than it removes, or locks engineers into choices they cannot override. |
| Q7 | Out-of-scope — what are we explicitly not building? | Runtime infrastructure (databases, queues, cloud deployment), UI frameworks, domain-specific business logic. |

### Runtime Behaviour

| ID | Question | Answer |
|----|----------|--------|
| Q8 | Should the template ship with any working feature, or be purely empty? | It should ship with exactly one working demonstration feature so engineers see the full workflow end-to-end. |
| Q9 | What is the simplest useful feature for that demonstration? | Displaying the application version read from `pyproject.toml` — it exercises the full stack with no external dependencies. |

### Feature: display-version

| ID | Question | Answer |
|----|----------|--------|
| Q10 | Where is the authoritative version stored? | In `pyproject.toml` under `[project] version`. No other copy should exist. |
| Q11 | How should verbosity be controlled? | Via a string parameter to `main()` matching Python's standard log level names. Invalid values should raise a `ValueError`. |
| Q12 | At what log level should the version be emitted? | INFO — visible by default in most environments, suppressible by raising to WARNING. |
| Q13 | Is the version needed at import time, or only when `main()` runs? | Only when `main()` runs; no module-level side effects. |
| Q14 | What should happen with an unrecognised verbosity string? | Raise `ValueError` naming the invalid value and listing the valid options. |

Status: COMPLETE
