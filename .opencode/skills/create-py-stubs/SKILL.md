---
name: create-py-stubs
description: "Create minimum typed stubs and test stubs as domain model breadcrumbs for the current feature"
---

# Create Python Stubs

Available knowledge: [[architecture/technical-design]], [[software-craft/stub-design]], [[software-craft/tdd]]. `in` artifacts: read all before starting work.

1. Read the feature file and identify all `@id` tags and the domain entities, value objects, and use cases referenced by the Examples.
2. For each referenced entity/value object/use case not yet implemented, create a minimal typed stub per [[software-craft/stub-design#concepts]]: Protocol method signatures with `raise NotImplementedError` bodies, no docstrings, no type hints beyond the contract. These stubs are breadcrumbs from the domain model. The SE can add, remove, or modify them during implementation.
3. Create test stubs from the project's test stub template with `@id` traceability per [[software-craft/stub-design#concepts]]. Each stub uses `@pytest.mark.skip(reason="not yet implemented")`, follows `test_<feature_stem>_<id>` naming, and contains raw Gherkin steps in the docstring: never MoSCoW tags or `...` ellipsis bodies.
4. Verify all `@id` tags from the feature file have corresponding test stubs per [[software-craft/stub-design#key-takeaways]].
