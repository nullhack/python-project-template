<div align="center">

<img src="docs/assets/banner.svg" alt="temple8" width="100%"/>

<br/><br/>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](https://nullhack.github.io/temple8/coverage/)
[![CI](https://img.shields.io/github/actions/workflow/status/nullhack/temple8/ci.yml?style=for-the-badge&label=CI)](https://github.com/nullhack/temple8/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-%E2%89%A513-blue?style=for-the-badge)](https://www.python.org/downloads/)

**From zero to hero — production-ready Python, without the ceremony.**

</div>

---

You have tried to ship features with AI assistants. The agent writes code, you review it, and somehow the spec still drifts from the implementation. Tests pass but the feature doesn't match what stakeholders asked for. Architecture decisions vanish into commit messages nobody reads. The review cycle is a black box — either everything passes or nothing does, with no structured progression.

**temple8 replaces ad-hoc agent orchestration with state machines that route every step through the right agent with the right skills at the right time.**

Flow definitions in YAML declare what happens at each state: who owns it, what they may read, what they must produce, and which conditions gate the next transition. No agent guesses what to do next. No step is skipped. No artifact is written outside its contract.

---

## Who is this for?

### Developers — TDD with traceability, not just coverage

You write BDD scenarios from stakeholder interviews. Tests are linked to feature specs with `@id` tags. Every `Given/When/Then` maps to a test function. No orphan tests, no missing tests. Red-green-refactor cycles are enforced — you can't skip to implementation.

### Product Owners — Living documentation that never drifts

Feature files are the contract. Acceptance criteria are BDD scenarios, not bullet points in a ticket. The delivery flow tracks whether a feature is `BASELINED`, `ACCEPTED`, or rejected — with evidence at every gate. You see exactly what was built and why.

### Architects — Adversarial review that catches what linters miss

Three-tier review: design alignment (does it match the domain model?), structure (coverage, traceability, coupling), conventions (formatting, naming, lint). Each tier can fail independently. No rubber-stamping through one monolithic gate.

---

## What it does

```
flowr check      →  inspect a state's owner, skills, and transitions
flowr next       →  see which transitions pass given your evidence
flowr transition →  advance to the next state with evidence
```

**State machines route the work.** YAML flows define the delivery pipeline — discovery, architecture, planning, TDD cycles, review gates, delivery. Each state declares an owner, skills, input/output artifacts, and guard conditions. The engine validates transitions. The agent executes.

**Agents execute it.** Each state's `owner` dispatches to the right agent (PO, SE, SA, DE, R). Skills are loaded per state. Input/output contracts prevent scope creep. Evidence gates prevent premature transitions.

**Branch discipline is explicit.** Every state declares `git: main` or `git: feature`. Project-phase work commits to main. Feature work commits to a feature branch. No ambiguity about where changes belong.

---

## Quick start

```bash
git clone https://github.com/nullhack/temple8
cd temple8
curl -LsSf https://astral.sh/uv/install.sh | sh  # skip if uv is already installed
uv sync --all-extras
opencode && @setup-project                        # personalise for your project
uv run task test && uv run task lint && uv run task static-check
```

---

## Commands

```bash
uv run task test          # full suite + coverage
uv run task test-fast     # fast, no coverage (use during TDD loop)
uv run task lint          # ruff format + check
uv run task static-check  # pyright type checking
uv run task run           # run the app
uv run task doc-build     # build API docs + coverage report
```

---

## Documentation

- **[Product Definition](https://nullhack.github.io/temple8/)** — product boundaries, users, and scope
- **[System Overview](https://nullhack.github.io/temple8/)** — architecture, domain model, module structure, and constraints
- **[Glossary](https://nullhack.github.io/temple8/)** — living domain glossary

---

## License

MIT — see [LICENSE](LICENSE).

**Author:** [@nullhack](https://github.com/nullhack) · [Documentation](https://nullhack.github.io/temple8)

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/temple8.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/temple8/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/temple8.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/temple8/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/temple8.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/temple8/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/temple8.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/temple8/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/temple8/blob/main/LICENSE