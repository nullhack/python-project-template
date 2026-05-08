---
name: domain-discovery
description: "Convergent synthesis: formalize event storming candidates into bounded contexts, entities, relationships, aggregate boundaries, and context map"
---

# Domain Discovery

Available knowledge: [[domain-modeling/domain-modeling]], [[domain-modeling/context-mapping#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read `domain_model.md` (written by facilitate-event-storming in the same state) and all interview notes.
2. List entity candidates from event subjects, command targets, and read model references per [[domain-modeling/domain-modeling#content]].
3. Classify each candidate as Entity (has identity + lifecycle) or Value Object (defined by attributes, immutable) per [[domain-modeling/domain-modeling#key-takeaways]].
4. Determine relationships between entities: composition, dependency, or domain flow. Assign cardinality (1:1, 1:N, M:N) per [[domain-modeling/domain-modeling#key-takeaways]].
5. Define aggregate boundaries per [[domain-modeling/domain-modeling#key-takeaways]]: group entities sharing invariants. Document root entity, invariants, and business reason for each grouping.
6. Identify context boundaries: group aggregates sharing a ubiquitous language. A boundary exists where terms change meaning, consistency requirements differ, or independent deployment is needed.
7. Map context relationships per [[domain-modeling/context-mapping#key-takeaways]]: classify each inter-context relationship (OHS, Conformist, Customer-Supplier, Partnership, ACL) and document translation rules.
8. Write formalized sections into `domain_model.md`: **bounded_contexts**, **entities**, **relationships**, **aggregate_boundaries**, **context_map**. If the file already has these sections from a prior iteration, edit them cumulatively — preserve valid content, update based on new information.
9. Add a **Changes** entry recording what was formalized and why.
