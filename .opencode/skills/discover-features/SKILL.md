---
name: discover-features
description: "Identify feature boundaries from the delivery order, validated against bounded contexts and aggregate boundaries"
---

# Discover Features

Available knowledge: [[requirements/feature-boundaries]], [[requirements/feature-discovery#concepts]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, domain_model.md, and glossary.md from `in` artifacts.
2. List the delivery order steps from product_definition.md. Each step is a feature candidate per [[requirements/feature-boundaries#key-takeaways]].
3. For each candidate, map it to bounded contexts using the domain model's entity table. IF a candidate spans multiple contexts → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
4. For each candidate, map it to aggregate boundaries using the domain model's aggregate boundary table. IF a candidate requires cross-aggregate transactions → flag for splitting per [[requirements/feature-boundaries#key-takeaways]].
5. Name each feature per [[requirements/feature-boundaries#content]]: use the delivery step name, validated for clarity and specificity.
6. Write a description for each feature per [[requirements/feature-boundaries#content]]: what it provides, which context it serves, why it exists, key entities.
7. Identify cross-cutting quality attributes from product_definition.md that will become Constraints — note which features they distribute to per [[requirements/feature-boundaries#content]] — but do NOT write Constraints yet; discover-rules will write them.
8. Create a `.feature` file from the template at `.templates/docs/features/feature.feature.template` for each feature with title, description, Status: ELICITING, and an empty Questions table. Do NOT write Rules (Business) or Constraints — those come from the discover-rules skill.
9. Run context coverage gap analysis per [[requirements/feature-discovery#content]]: every bounded context covered by at least one feature? IF any gap → add a Questions entry flagging it.