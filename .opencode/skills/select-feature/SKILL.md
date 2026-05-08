---
name: select-feature
description: "Select the next feature to develop by detecting delivery status from disk evidence, following delivery order"
---

# Select Feature

`in` artifacts: read all before starting work.

1. List available feature files in `docs/features/`.
2. IF no feature files exist → exit via `no-features`; features need discovery first.
3. Read `product_definition.md` to obtain the delivery order (ordered list of feature slugs).
4. For each feature slug in delivery order, determine delivery status with a single pipeline
   — do NOT open or read individual feature or test files:

    a. Count @id tags in the feature file. If zero, the feature has not been
       broken down into BDD examples yet → feature is incomplete (select it).

         grep -c '@id:' docs/features/<slug>.feature

    b. Extract every @id tag from the feature file and the matching test function
      hex suffixes from the test directory, then compare:

        diff \
          <(grep -oP '@id:\K\w+' docs/features/<slug>.feature | sort -u) \
          <(grep -rh "def test_<slug>_" tests/features/<slug>/ 2>/dev/null \
             | grep -oP 'test_<slug>_\K\w+' | sort -u)

      - Diff produces output → some @id tags lack matching test functions →
        feature is incomplete (select it).
      - Diff is clean → all @id tags have matching test functions.

    c. If diff is clean, run the tests scoped to that feature's test directory
      using the project's test runner (see Project Commands table).
      - Any failures → feature is incomplete (select it).
      - All pass → feature is delivered (skip).

    d. If the test directory does not exist, grep returns nothing and diff
       exits non-zero → feature is incomplete (select it). This also covers
       the case where no test files exist to match @id tags.

5. Select the first incomplete feature by delivery order.
6. IF every feature in the delivery order is delivered (diff clean + tests pass for all) →
   exit via `no-features`.
7. Set the `feature-id` session param to the selected feature's filename stem (without `.feature` extension).
