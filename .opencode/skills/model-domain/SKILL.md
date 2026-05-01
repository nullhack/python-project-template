---
name: model-domain
description: "Formalize candidates into bounded contexts, entities, relationships, and aggregate boundaries"
---

# Model Domain

Load [[domain-modeling/event-storming#key-takeaways]] before starting. 

1. Define bounded contexts per [[domain-modeling/event-storming#key-takeaways]].
2. Define entities within each context — name, attributes, lifecycle.
3. Define relationships between entities — associations, dependencies, invariants.
4. Define aggregate boundaries per [[domain-modeling/event-storming#key-takeaways]].
5. Write a summary of the domain model.
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
