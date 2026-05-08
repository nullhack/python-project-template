---
name: create-py-stubs
description: "Create minimum typed stubs and test stubs as domain model breadcrumbs for the current feature, then verify all planning artifacts are complete for baseline"
---

# Create Python Stubs

Available knowledge: [[architecture/technical-design]], [[software-craft/source-stubs]], [[software-craft/test-stubs]], [[software-craft/tdd]], [[requirements/decomposition#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read the feature file and identify all `@id` tags and the domain entities, value objects, and use cases referenced by the Examples.
2. For each referenced entity/value object/use case not yet implemented, create a minimal typed stub per [[software-craft/source-stubs#concepts]]: Protocol method signatures with `raise NotImplementedError` bodies, no docstrings, no type hints beyond the contract. These stubs are breadcrumbs from the domain model. The SE can add, remove, or modify them during implementation.
3. Create test stubs from the project's test stub template with `@id` traceability per [[software-craft/test-stubs#concepts]]. Each stub uses `@pytest.mark.skip(reason="not yet implemented")`, follows `test_<feature_stem>_<id>` naming, and has a docstring with a one-line description of what the example proves, a blank line, then the Gherkin steps: never MoSCoW tags or `...` ellipsis bodies.
4. Verify all `@id` tags from the feature file have corresponding test stubs per [[software-craft/test-stubs#key-takeaways]].
5. Verify decomposition per [[requirements/decomposition#key-takeaways]]: no more than 2 concerns, no more than 8 Must Examples.
6. Verify all planning artifacts are present and consistent: feature file, product definition, domain model, glossary.
7. Commit all changes to local main.
