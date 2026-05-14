---
name: discover-rules
description: "Distribute simulation-discovered rules and constraints into feature files from simulation results"
---

# Discover Rules

Available knowledge: [[requirements/feature-discovery#concepts]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, domain_spec.md, simulation_results.md, glossary.md, and all `.feature` files (created by discover-features in this same state) from `in` artifacts.
2. List all rules discovered across all simulation iterations from simulation_results.md.
3. For each rule, identify which feature it belongs to based on the bounded context and entities it involves. IF a rule spans multiple features → flag for cross-cutting handling.
4. Write each rule as a coarse bullet under the `# Business rules:` comment block in the relevant `.feature` file. Rules are descriptive statements — no numbered prefixes. They map directly to Example titles written later by write-bdd-features.
5. For each quality attribute in product_definition.md, map it to the feature(s) that enforce it. Write each as a Constraint with a measurable threshold under `# Constraints:` in the relevant `.feature` file.
6. Run traceability verification:
   - Every simulation rule → at least one feature's business rules.
   - Every quality attribute → at least one feature's constraints.
   - Every feature → at least one business rule.
   IF any gap → flag it. Do NOT silently fill gaps with assumed rules.
7. Write all `# Business rules:` bullets and `# Constraints:` into each `.feature` file. Do NOT write full `Rule:` blocks (As a/I want/So that) or `Example:` blocks — those require the adversarial analysis of breakdown.
