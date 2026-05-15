---
name: discover-features
description: "Identify feature boundaries from simulation-created .feature files, validated against bounded contexts and delivery order"
---

# Discover Features

Available knowledge: [[requirements/feature-boundaries]], [[requirements/feature-discovery#concepts]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, domain_spec.md, features/*.feature, and glossary.md from `in` artifacts.
2. Read simulation-created .feature files (one per bounded context from spec-validation). Read product_definition.md delivery order. These are the two inputs for feature candidate identification.
3. Read rules from .feature files (written by simulation). These are the rules that must be distributed to features.
4. For each candidate, map it to bounded contexts from the domain spec. IF a candidate spans multiple contexts → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
5. For each candidate, map it to entities and state machines from the domain spec. IF a candidate requires cross-aggregate transactions → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
6. Redistribute Rule blocks across split features. When a coarse .feature file is split into multiple features, move Rule blocks to the appropriate feature file. Do NOT edit Rule block content — only redistribute. IF a rule spans multiple features → flag for cross-cutting handling.
7. Name each feature per [[requirements/feature-boundaries#content]]: use the delivery step name, validated for clarity and specificity. The Feature title slug MUST match the .feature filename stem per [[requirements/gherkin#concepts]].
8. Write a description for each feature per [[requirements/feature-boundaries#content]]: what it provides, which context it serves, why it exists, key entities.
9. Map quality attributes from product_definition.md to features. Write each as a `# Constraints:` bullet in the .feature file.
10. Edit each `.feature` file: update Feature title and description if the feature was split/renamed. Verify the new Feature title is 2–6 words and unique across all feature files per [[requirements/gherkin#key-takeaways]]. Count words by splitting on whitespace. If a title fails, rephrase and re-verify. The Feature title slug must match the .feature filename stem. Add `# Constraints:` comments from quality attribute mapping (Step 9). Feature files already exist from simulation — this step edits, not creates.
11. Run context coverage gap analysis: every bounded context from domain_spec.md covered by at least one .feature file. IF any gap → flag it.
