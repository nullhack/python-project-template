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
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/downloads/)

**From zero to hero — production-ready Python, without the ceremony.**

</div>

---

A delivery system that treats documentation as a first-class artifact and enforces production rigor through an AI-assisted workflow. Your team ships features, not broken promises.

---

## Who is this for?

### Developers — AI pair programming with industry standards

You have used AI coding assistants. They generate code fast, but without tests, without traceability, and without review. This template enforces TDD by default: acceptance criteria exist before code, every requirement traces to a test, and an adversarial review gates every shipment. The AI writes tests first, respects your architecture, and ships code you would merge with confidence.

### Product Owners & Project Managers — Living documentation that earns trust

Stakeholders cannot read code. They read decisions. This template turns your repository into a transparent narrative: Gherkin stories trace requirements to tests, architecture decision records preserve reasoning, and a living domain model keeps everyone speaking the same language. Demo from the same source your engineers build from. No drift. No "trust me, it is done."

---

## The delivery cycle

```
SCOPE → ARCH → TDD LOOP → VERIFY → ACCEPT
```

Each feature moves through five steps. At any moment, exactly one feature is in progress — enforced by filesystem state, not convention:

```
docs/features/backlog/      ← scoped, waiting
docs/features/in-progress/  ← building now (max 1)
docs/features/completed/    ← accepted and shipped
```

Scope is written before architecture. Architecture is written before code. Code is reviewed adversarially before acceptance. Nothing moves to completed without explicit Product Owner sign-off.

---

## Living documentation views

Every artifact is version-controlled alongside the code that implements it.

**Feature narratives** — Gherkin `.feature` files in `docs/features/` show exactly what is scoped, building, or shipped. Each story maps directly to tests; no requirement is orphaned.

**Architecture decisions** — Every significant architectural choice is recorded as a dated ADR in `docs/adr/`. Six months from now, the team can reconstruct not just what was built, but why.

**Domain model and glossary** — A living domain model and glossary keep business language consistent across team, documentation, and code. No invented synonyms; no drift between what stakeholders say and what engineers build.

**System overview** — `docs/system.md` reflects only completed, accepted features. No stale speculation; no documentation that lies about current state.

**C4 diagrams** — Context and container diagrams generated from the same source as the code, giving stakeholders a precise picture of system boundaries.

**Post-mortems** — Failures become append-only organizational memory in `docs/post-mortem/`. The same failure mode does not repeat silently; it leaves a record.

---

## Development standards

**TDD by default** — Red → Green → Refactor, one acceptance criterion at a time. Every test is written before the code it validates. The loop is canonical: write the failing test, write the minimum code to pass, then refactor with the safety net of a green bar.

**Behavioral tests only** — Tests describe observable contracts, not implementation internals. A test that survives a complete internal rewrite is a good test. A test that breaks on refactoring is a liability.

**Coverage enforced** — Measured against your package. Threshold is defined in `pyproject.toml`. No untested paths ship. Coverage is a floor, not a goal.

**Design principles enforced** — YAGNI, KISS, DRY, SOLID, and Object Calisthenics are not guidelines — they are review gates. Every principle is checked with file and line evidence before a feature is approved.

**Refactoring as first-class** — The REFACTOR phase is not optional cleanup. Code smells trigger specific pattern applications. Complexity is managed continuously, not accumulated and then confronted.

**Git workflow with guardrails** — All work happens on feature branches. No force push. No history rewrite on shared branches. Conventional commits only. Clean merges to `main` via `--no-ff`. The branch model is simple and safe by default.

**Zero type errors** — Full static type checking with no exceptions, no `type: ignore` suppressions.

**Adversarial verification** — The architect who designed the system reviews it. The default hypothesis is "broken." Green automated checks are necessary but not sufficient for approval.

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
