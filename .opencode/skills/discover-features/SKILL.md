---
name: discover-features
description: "Identify feature boundaries from the delivery order and simulation results, validated against bounded contexts"
---

# Discover Features

Available knowledge: [[requirements/feature-boundaries]], [[requirements/feature-discovery#concepts]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, behavioral_spec.md, simulation_results.md, and glossary.md from `in` artifacts.
2. List the delivery order steps from product_definition.md. Each step is a feature candidate per [[requirements/feature-boundaries#key-takeaways]].
3. List all discovered rules from simulation_results.md. These are the rules that must be distributed to features.
4. For each candidate, map it to bounded contexts from the behavioral spec. IF a candidate spans multiple contexts → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
5. For each candidate, map it to entities and state machines from the behavioral spec. IF a candidate requires cross-aggregate transactions → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
6. Distribute simulation rules to features: each rule from simulation_results.md belongs to the feature whose context and entities it involves. IF a rule spans multiple features → split the rule or flag for cross-cutting handling.
7. Name each feature per [[requirements/feature-boundaries#content]]: use the delivery step name, validated for clarity and specificity. The Feature title slug MUST match the .feature filename stem per [[requirements/gherkin#concepts]].
8. Write a description for each feature per [[requirements/feature-boundaries#content]]: what it provides, which context it serves, why it exists, key entities.
9. Identify cross-cutting quality attributes from product_definition.md that will become Constraints — note which features they distribute to per [[requirements/feature-boundaries#content]] — but do NOT write Constraints yet; discover-rules will write them.
10. Create a `.feature` file from the template at `.templates/docs/features/<feature_name>.feature.template` for each feature with title and description. Do NOT write `# Business rules:` or `# Constraints:` — those come from the discover-rules skill. The feature files are intentionally incomplete at this stage; discover-rules (which runs in the same state) will finalize them with business rules and constraints.
11. Run context coverage gap analysis per [[requirements/feature-discovery#content]]: every bounded context covered by at least one feature? IF any gap → flag it.
