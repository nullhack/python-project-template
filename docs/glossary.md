# Glossary: temple8

> Living glossary of domain terms used in this project.
> Written and maintained by the product-owner during Step 1 discovery.
> Append-only: never edit or remove past entries. If a term changes, mark it retired in favour of the new entry and write a new entry.
> Code and tests take precedence over this glossary — if they diverge, refactor the code, not this file.

---

## Entry Format

```
## <Term>

**Definition:** <one sentence — genus + differentia: "A [category] that [distinguishes it from others in that category]">

**Aliases:** <deprecated synonyms the team should stop using, or "none">

**Example:** <one sentence showing the term in use in this project; optional but encouraged>

**Source:** <feature stem or discovery session date>
```

Entries are sorted alphabetically.

---

## Acceptance Criteria

**Definition:** A set of conditions that a feature must satisfy before the product-owner considers it complete.

**Aliases:** Definition of Done (different concept — do not conflate), exit criteria

**Example:** "The CLI entrypoint acceptance criterion states: given the package is installed, when the user runs `python -m app --version`, then the output contains the version string from package metadata."

**Source:** template — BDD practice (Gherkin `Example:` blocks with `@id` tags)

---

## ADR (Architecture Decision Record)

**Definition:** A short document that records a significant architectural decision — the context that triggered it, the self-interview questions and answers that led to the decision, the alternatives considered, and the consequences. One ADR can group multiple related Q&A pairs that converge on a single decision.

**Aliases:** decision log entry, design decision record

**Example:** "ADR-2026-04-22-cli-parser-library records why the team chose argparse over click for the CLI skeleton, including the self-interview questions the SA asked before stakeholder validation."

**Source:** template — Nygard (2011), MADR format

---

## Agent

**Definition:** An AI assistant assigned a specific role in the development workflow, operating within defined boundaries and producing defined outputs.

**Aliases:** AI agent, LLM agent, assistant

**Example:** "The product-owner agent interviews the stakeholder and writes `.feature` files; the software-engineer agent implements the tests and production code."

**Source:** template — this project's workflow

---

## BDD (Behaviour-Driven Development)

**Definition:** A collaborative software development practice in which acceptance criteria are written as concrete examples of system behaviour, expressed in a structured natural language understood by both stakeholders and developers.

**Aliases:** Behaviour-Driven Development, Behavior-Driven Development (US spelling)

**Example:** "The team uses BDD to write Gherkin `Example:` blocks that become the executable specification for each feature."

**Source:** template — North (2006) BDD origin paper

---

## Backlog

**Definition:** The ordered collection of features that have been discovered and baselined but not yet started.

**Aliases:** feature backlog, product backlog

**Example:** "The product-owner moves `cli-entrypoint.feature` from `backlog/` to `in-progress/` when the team is ready to begin implementation."

**Source:** template — this project's workflow

---

## Bounded Context

**Definition:** A boundary within a domain model inside which a particular ubiquitous language is internally consistent and unambiguous.

**Aliases:** context boundary, model boundary

**Example:** "In a retail system, 'Product' means a catalogue entry in the browsing context but means a fulfilment line item in the shipping context — they are different concepts in different bounded contexts."

**Source:** template — Evans (2003) DDD; Fowler (2014) BoundedContext bliki

---

## CLI Entrypoint

**Definition:** The `app/__main__.py` module that wires the application's command-line interface, exposing `--help` and `--version` flags via Python's stdlib `argparse`.

**Aliases:** entry point, main module, CLI entry

**Example:** "Running `python -m app --version` invokes the CLI entrypoint and prints the application name and version."

**Source:** 2026-04-22 — Session 1; feature `cli-entrypoint`

---

## DDD (Domain-Driven Design)

**Definition:** A software design approach that centres the codebase around an explicit model of the business domain, using the same language in code, tests, and stakeholder conversations.

**Aliases:** Domain-Driven Design

**Example:** "Following DDD, the team names the Python class `Invoice` because the accountant calls it an invoice — not `BillingDocument` or `PaymentRecord`."

**Source:** template — Evans (2003) Domain-Driven Design; Evans (2015) DDD Reference

---

## Demonstration Feature

**Definition:** The single working feature that ships with the template to show engineers the full five-step delivery workflow end-to-end before they build their own features.

**Aliases:** demo feature, starter feature

**Example:** "The `cli-entrypoint` feature is the demonstration feature — it implements `--help` and `--version` flags and is delivered through all five workflow steps."

**Source:** 2026-04-22 — Session 1 (Q8, Q9)

---

## Domain Event

**Definition:** A record of something that happened in the domain that domain experts care about, expressed as a past-tense verb phrase.

**Aliases:** event, business event

**Example:** "`OrderPlaced`, `VersionDisplayed`, and `ReportGenerated` are domain events — they record facts that occurred, not commands to be executed."

**Source:** template — Vernon (2013) Implementing DDD

---

## Feature

**Definition:** A unit of user-visible functionality described by a `.feature` file containing a title, narrative, rules, and acceptance criteria examples.

**Aliases:** story, user story (broader concept — a feature here is a Gherkin file)

**Example:** "The `cli-entrypoint` feature covers all behaviour related to the application's command-line interface."

**Source:** template — this project's workflow

---

## Gherkin

**Definition:** A structured plain-English syntax for writing acceptance criteria using `Feature`, `Rule`, `Example`, `Given`, `When`, and `Then` keywords.

**Aliases:** Cucumber syntax, BDD syntax

**Example:** "`Given the application package is installed`, `When the user runs python -m app --version`, `Then the output contains the version string` is a Gherkin example."

**Source:** template — Cucumber project; North (2006) BDD origin

---

## Package Metadata

**Definition:** The runtime-accessible project information (name, version, description, author) stored in `pyproject.toml` and read at runtime via Python's `importlib.metadata` stdlib module.

**Aliases:** project metadata, distribution metadata

**Example:** "`importlib.metadata.version('temple8')` returns the plain semver version (e.g. `0.1.0`) at runtime, matching the `version` field in `pyproject.toml`."

**Source:** 2026-04-22 — Session 1 (Q10, Q11); feature `cli-entrypoint`

---

## Product Owner (PO)

**Definition:** The agent responsible for discovering requirements, writing acceptance criteria, and deciding whether delivered features meet stakeholder needs.

**Aliases:** PO

**Example:** "The product-owner interviews the stakeholder, writes `.feature` files, and either accepts or rejects delivered features at Step 5."

**Source:** template — this project's workflow (adapted from Scrum PO role)

---

## Skill

**Definition:** A markdown file loaded on demand that provides an agent with specialised instructions for a specific task.

**Aliases:** prompt skill, agent skill

**Example:** "The software-engineer loads the `implement` skill at the start of Step 3 to receive TDD loop instructions."

**Source:** template — this project's workflow

---

## Software Engineer (SE)

**Definition:** The agent responsible for writing tests, implementing production code, and maintaining the git history during the TDD loop.

**Aliases:** SE, developer, implementer

**Example:** "The software-engineer runs `uv run task test-fast` after every code change to verify the test suite stays green."

**Source:** template — this project's workflow

---

## Stakeholder

**Definition:** The human who owns the problem being solved, provides domain knowledge, and has final authority over whether delivered features meet their needs.

**Aliases:** user, domain expert, customer, product manager

**Example:** "The stakeholder answered Q11 by choosing Option C — `--help` + `--version` combined — as the demonstration feature."

**Source:** template — requirements-elicitation practice

---

## System Architect (SA)

**Definition:** The agent responsible for translating accepted requirements into an architectural design, writing domain stubs, recording architectural decisions, and verifying implementation against the design.

**Aliases:** SA, architect, technical lead

**Example:** "The system-architect reads `cli-entrypoint.feature`, writes domain stubs in `app/__main__.py`, and records the argparse decision as an ADR."

**Source:** template — this project's workflow

---

## TDD (Test-Driven Development)

**Definition:** A development practice in which a failing test is written before any production code, the minimum code needed to pass that test is written, and then the code is refactored while keeping the test green.

**Aliases:** Test-Driven Development, test-first development

**Example:** "Following TDD, the software-engineer writes a failing `test_cli_entrypoint_c1a2b3d4` test, then writes only enough production code to make it pass."

**Source:** template — Beck (2002) Test-Driven Development by Example

---

## Ubiquitous Language

**Definition:** A shared vocabulary built from domain-expert terms that is used consistently in all conversation, documentation, and code within a bounded context.

**Aliases:** domain language, shared language, common language

**Example:** "Because the stakeholder says 'help flag', the code uses `--help` as the argument name — the ubiquitous language ensures no translation layer exists between domain expert and code."

**Source:** template — Evans (2003) DDD; Evans (2015) DDD Reference

---

## WIP (Work In Progress)

**Definition:** The count of features currently being actively developed; this project enforces a WIP limit of one feature at a time.

**Aliases:** work in progress, in-flight work

**Example:** "If `docs/features/in-progress/` already contains a `.feature` file, the WIP limit is reached and no new feature may start until that one is accepted."

**Source:** template — Kanban WIP limit principle

---
