# Scope Journal: temple8

> Append-only record of all discovery session Q&A.
> Written by the product-owner. Read by the product-owner for resume checks.
> Never edit past entries — append new session blocks only.

---

## 2026-04-22 — Session 1

Status: COMPLETE

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

### Feature: cli-entrypoint

| ID | Question | Answer |
|----|----------|--------|
| Q9 | Which behavioural areas are in scope for the template's own feature backlog? | Just one simple command in the base package — useful for any starting project, simple enough not to bloat the app, and showcasing the template's capabilities end-to-end. |
| Q10 | What kind of command would be "useful for any starting project"? Candidate options presented: version, hello/greet, info/about, config show, health. | Stakeholder asked: "if I choose version, what will it add to my app/ folder?" — confirmed interest in version-style command after seeing the footprint (one file, ~10 lines, zero new dependencies). |
| Q11 | Three options presented: (A) `--help` only, (B) `--version` only, (C) `--help` + `--version` combined. Stakeholder also asked how a help/usage command would look in code and terminal. Full code sketches and tradeoff table provided. Which option for the demonstration feature? | Option C — `--help` + `--version` combined. `python -m app --help` shows app name, tagline, and available options. `python -m app --version` shows `temple8 <version>` read from package metadata. Zero new dependencies, all code in `app/__main__.py`. |


