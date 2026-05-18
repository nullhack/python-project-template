---
name: refine-features
description: "Transform simulation-created context-level .feature files into final feature-level files with stable titles, descriptions, rules, and constraints"
---

# Refine Features

Available knowledge: [[requirements/feature-boundaries]], [[requirements/feature-discovery#concepts]], [[requirements/invest]], [[requirements/decomposition]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work.

This state transforms the output of spec-validation (context-level .feature files) into the final feature-level structure that develop-flow will use. After this state, .feature file structure (Feature titles, Rule titles, Constraints) is FROZEN. Only Examples/Outlines may be added during develop-flow.

1. Read `product_definition.md`, `domain_spec.md`, `glossary.md`, and `features/*.feature` from `in` artifacts. The .feature files are simulation-created (one per bounded context, named by context).
2. Read `product_definition.md` delivery order. This determines feature priority and grouping.
3. For each bounded context in `domain_spec.md`, identify feature candidates per [[requirements/feature-boundaries#key-takeaways]]:
   - Map candidates to bounded contexts. IF a candidate spans multiple contexts → flag for splitting.
   - Map candidates to entities and aggregate boundaries. IF a candidate requires cross-aggregate transactions → flag for splitting.
4. Create feature-level .feature files by splitting context-level files per [[requirements/feature-discovery#concepts]]:
   - Name each feature per [[requirements/feature-boundaries#content]]: use the delivery step name, validated for clarity and specificity.
   - The Feature title slug MUST match the .feature filename stem per [[requirements/gherkin#concepts]].
   - Redistribute Rule blocks across split features. When a context .feature file is split into multiple features, move Rule blocks to the appropriate feature file. Do NOT edit Rule block content — only redistribute. IF a rule spans multiple features → flag for cross-cutting handling.
   - Delete the original context-level .feature files after all their Rules have been redistributed to feature-level files.
5. Write a Feature description for each feature per [[requirements/feature-discovery#concepts]]: what it provides, which context it serves, why it exists, key entities. The description replaces the simulation-era placeholder text.
6. Validate each Rule block's title per [[requirements/gherkin#key-takeaways]]: 2–6 words, descriptive, unique within the feature file, no special characters. Count words by splitting on whitespace. IF a title is outside the range → rephrase while preserving meaning. Do NOT rewrite the behavioral description paragraph — it is the simulation-validated rule body.
7. Check decomposition per [[requirements/decomposition#key-takeaways]].
8. Map quality attributes from `product_definition.md` to features. Write each as a `# Constraints:` bullet in the .feature file. Technology constraints from `domain_spec.md` Integration Points are already present from simulation — verify they remain and add quality attribute constraints.
9. Run context coverage gap analysis: every bounded context from `domain_spec.md` must be covered by at least one .feature file. IF any gap → flag it.
10. Validate each feature passes INVEST criteria per [[requirements/invest#concepts]]. Every criterion that fails is a hard blocker: fix before advancing. IF a feature fails Independent or Small → split per [[requirements/decomposition#key-takeaways]]. IF a feature fails Negotiable or Valuable → flag for stakeholder decision.
11. Commit all .feature file changes to the local dev branch.

**Stability contract**: After this state completes, Feature titles, Rule titles, and the number of Rules per feature are FROZEN. Develop-flow may only add Examples/Outlines to existing Rules. Renaming, splitting, or removing existing structural elements would break beehave's title-based mapping to test files and functions.