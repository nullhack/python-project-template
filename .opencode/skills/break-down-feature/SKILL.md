---
name: break-down-feature
description: "Verify simulation-discovered rules are specific enough and write them as Rule blocks in the feature file"
---

# Break Down Feature

Available knowledge: [[requirements/invest]], [[requirements/decomposition]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work.

1. Discover and read the feature file, product definition, domain spec, and glossary from `in`. The feature file contains Rule blocks with behavioral descriptions (from simulation). These rules were discovered during spec simulation — they are already validated behavioral statements, not hypotheses.
2. For each Rule block in the .feature file:
   a. Verify the rule is specific enough to generate at least one Example. IF the rule is vague (e.g. "the system should handle errors") → flag for clarification.
   b. Verify the rule is not contradicted by another rule or by the domain spec.
   c. Verify the rule maps to at least one entity and state in the domain spec.
3. Validate each Rule block's title: 2–6 words, descriptive, unique within the feature file, and contain no special characters. If a title doesn't meet constraints, rephrase while preserving meaning. Do NOT rewrite the behavioral description paragraph — it is the simulation-validated rule body. Example:
    ```
    Rule: Order must contain at least one item
    ```
4. IF clarification is needed for a rule → ask the stakeholder targeted questions. Record answers in the relevant interview notes.
5. IF a Rule contains "and" or spans more than 2 concerns → split into separate Rule blocks per [[requirements/decomposition#key-takeaways]].
6. IF the feature has more than 8 rules → propose the split to the stakeholder with rationale per [[requirements/decomposition#key-takeaways]]. Stakeholder decides what's core vs. deferred.
7. Add Behavior hints under each Rule block. Format: `Behavior hints:` followed by `- <condition> → <outcome>` bullets. Each hint describes a behaviorally distinct outcome. Leave the `# Constraints:` comment block in place — these are non-functional requirements (performance, security, accessibility) that are not convertible to Gherkin Rules but must remain visible for the reviewer and implementer.
8. Validate the feature passes INVEST criteria per [[requirements/invest#concepts]]. Every criterion that fails is a hard blocker: fix before advancing.
