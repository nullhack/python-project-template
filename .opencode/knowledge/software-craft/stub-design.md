---
domain: software-craft
tags: [stub-design, typed-stubs, traceability, package-structure]
last-updated: 2026-04-30
---

# Stub Design

## Key Takeaways

- Stubs are created in two phases: project-level creates the package skeleton; feature-level creates typed source stubs and test stubs per feature.
- Every `@id` tag in the feature file must have a corresponding test stub; traceability is verified before implementation begins.
- Package structure mirrors the module structure from technical design — each module maps to a Python package, each contract maps to a Protocol file.
- Feature branches are created from the latest main before any implementation begins.
- Source stubs are breadcrumbs from the domain model — the SE can add, remove, or modify them during implementation as the real shape emerges from TDD.

## Concepts

**Two-Phase Stub Creation** — Stubs are created at two different points in the flow. At project-structuring time, the SA creates the package skeleton only: directory structure mirroring the module layout, `__init__.py` files, port interfaces (Protocol abstractions from hexagonal architecture), and aggregate root class signatures. No entity, value object, or use case stubs are created at this stage. At feature planning time (after BDD examples are written), the SA creates minimum typed stubs for the entities, value objects, and use cases referenced by the current feature's Examples, plus test stubs for each `@id` tag. These feature-level stubs are breadcrumbs from the domain model — the SE can add, remove, or modify them during TDD as the real implementation shape emerges.

**Typed Stubs from Contracts** — At feature level, Protocol interfaces are derived from the three contract types defined in technical design: API contracts (REST endpoints → Protocol methods), event contracts (domain events → dataclasses with event schema), and interface definitions (hexagonal ports → Protocol abstractions). These stubs compile but have no behaviour — they serve as the architecture's skeleton.

**Minimum Stub Principle** — Source stubs contain the absolute minimum needed to compile and trace. Protocol method signatures with `raise NotImplementedError` bodies — no docstrings, no type hints beyond the contract (return types and parameter types required by the Protocol). Docstrings, type hints, and lint compliance (ruff check, ruff format) are added when reviewers require them, not proactively during stubbing or TDD. Adding them early is waste because refactoring changes code shape and invalidates them.

**@id Traceability Chain** — Each `@id` tag in the feature file produces one test stub at `tests/features/<feature_slug>/<rule_slug>_test.py` with a function named `test_<feature_stem>_<id>`. The `stubs_traceable` condition on the `create-py-stubs.done` transition verifies that `all_ids_have_stubs: ==true`. This ensures no acceptance criterion is lost between planning and implementation.

**Test Stub Format** — Every test stub follows the project's test stub template (located in `.templates/`). The format requires:
- Decorated with `@pytest.mark.skip(reason="not yet implemented")` — never use `...` ellipsis bodies
- Docstring contains the raw Gherkin steps (Given/When/Then) for traceability
- Body is `raise NotImplementedError` — so the test fails explicitly if the skip decorator is removed prematurely
- Function name follows `test_<feature_stem>_<id>` naming convention
- No MoSCoW tags or priority labels anywhere in the stub

**Package Structure from Module Structure** — The module structure section of technical design maps directly to the package layout: each module becomes a Python package, each Protocol becomes a file in that package, and each test module mirrors its production counterpart. The domain package depends on nothing; infrastructure packages depend on domain Protocols, never the reverse.

**Branch Setup** — Implementation begins on a feature branch (`feat/<stem>`) created from the latest main. Branch naming follows [[software-craft/git-conventions]]. The branch exists before any stubs are written — the first commit on the branch is the project structure.

**Scaffolding Order** — Create artifacts in this order: (1) feature branch from main, (2) package directories from module structure, (3) port interfaces and aggregate root signatures, (4) per-feature: Protocol stubs from contracts + test stubs from @id tags, (5) verify all @ids have corresponding test stubs.

## Related

- [[architecture/contract-design]] — the three contract types that define stub shapes
- [[architecture/technical-design]] — module structure and package layout
- [[requirements/gherkin]] — @id tag format and traceability convention
- [[software-craft/git-conventions]] — branch naming and commit format