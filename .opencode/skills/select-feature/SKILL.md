---
name: select-feature
description: "Select the next feature to develop by detecting delivery status from disk evidence, following delivery order"
---

# Select Feature

`in` artifacts: read all before starting work.

1. List available feature files in `docs/features/`.
2. IF no feature files exist → exit via `no-features`; features need discovery first.
3. Read `product_definition.md` to obtain the delivery order (ordered list of feature slugs). Validate against `domain_spec.md` context map to ensure dependency order is respected.
4. For each feature slug in delivery order, determine delivery status with a single pipeline
   — do NOT open or read individual feature or test files:

    a. Check if the feature file has Example blocks (any line starting with `Example:`).
       If none, the feature has not been broken down into BDD examples yet → feature is incomplete (select it).

    b. Run `beehave check <slug>` to verify structural traceability:
       - Any output (errors) → some Examples lack matching test functions or there are orphan tests → feature is incomplete (select it).
       - No output (clean) → all Examples have matching test functions.

    c. If beehave check is clean, run the tests scoped to that feature's test directory
      using the project's test runner (see Project Commands table).
      - Any failures → feature is incomplete (select it).
      - All pass → feature is delivered (skip).

    d. If the test directory does not exist, beehave check will report errors
       → feature is incomplete (select it).

5. Select the first incomplete feature by delivery order.
6. IF every feature in the delivery order is delivered (diff clean + tests pass for all) →
   exit via `no-features`.
7. Set the `feature_id` session param to the selected feature's filename stem (without `.feature` extension).
