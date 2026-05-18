---
name: select-feature
description: "Select the next feature to develop by detecting delivery status from disk evidence, deriving priority from dependency count and WSJF"
---

# Select Feature

Available knowledge: [[requirements/wsjf#key-takeaways]]. `in` artifacts: read all before starting work.

1. List available feature files in `docs/features/`.
2. IF no feature files exist → exit via `no-features`; features need discovery first.
3. For each feature, determine delivery status — do NOT open or read individual feature or test files:

   a. Check if the feature file has Example blocks (any line starting with `Example:`).
      If none, the feature has not been broken down into BDD examples yet → feature is incomplete.

   b. Run `beehave check <slug>` to verify structural traceability:
      - Any output (errors) → some Examples lack matching test functions or there are orphan tests → feature is incomplete.
      - No output (clean) → all Examples have matching test functions.

   c. If beehave check is clean, run `task test-fast` scoped to that feature's test directory.
      - Any failures → feature is incomplete.
      - All pass → feature is delivered (skip).

   d. If the test directory does not exist, beehave check will report errors → feature is incomplete.

4. IF every feature is delivered → exit via `no-features`.
5. Collect all incomplete features. Derive dependency count for each from `domain_spec.md` context map:
   - Count how many other incomplete features this feature depends on (via integration points and entity relationships in the context map).
   - Filter: select features with the **lowest dependency count** first (0 = no dependencies).
6. IF only one feature has the lowest dependency count → select it. Skip to step 8.
7. IF multiple features tie on dependency count → score each tied feature per [[requirements/wsjf#key-takeaways]]:
   - Estimate Value (1-5, mapped to Kano categories) and Effort (1-5, mapped to complexity).
   - Compute WSJF = Value / Effort.
   - Select the highest WSJF score; ties broken by Value.
8. Set the `feature_id` session param to the selected feature's filename stem (without `.feature` extension).
