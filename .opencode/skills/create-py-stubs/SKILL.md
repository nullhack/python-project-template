---
name: create-py-stubs
description: "Create minimum typed source stubs as domain model breadcrumbs, generate test stubs via pytest-beehave, then verify all planning artifacts are complete for baseline"
---

# Create Python Stubs

Available knowledge: [[architecture/technical-design]], [[software-craft/source-stubs]], [[software-craft/test-stubs]], [[software-craft/tdd]], [[requirements/decomposition#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read the feature file and identify the domain entities, value objects, and use cases referenced by the Examples.
2. For each referenced entity/value object/use case not yet implemented, create a minimal typed stub per [[software-craft/source-stubs#concepts]]: Protocol method signatures with `raise NotImplementedError` bodies, no docstrings, no type hints beyond the contract. These stubs are breadcrumbs from the domain model. The SE can add, remove, or modify them during implementation.
3. Run `beehave generate <feature_id>` to generate test stubs from the feature file. pytest-beehave creates one test function per Example, using `test_<scenario_title_slug>` naming, with an `...` (Ellipsis) body. Stubs are auto-skipped by pytest-beehave during collection — no `@pytest.mark.skip` decorator is needed.
4. Run `beehave check` to verify all Examples in the feature file have corresponding test stubs and there are no orphan tests. This replaces manual @id-to-stub traceability verification.
5. Verify decomposition per [[requirements/decomposition#key-takeaways]]: no more than 2 concerns, no more than 8 Must Examples.
6. Verify all planning artifacts are present and consistent: feature file, product definition, domain model, glossary.
7. Commit all changes to the local dev branch.
