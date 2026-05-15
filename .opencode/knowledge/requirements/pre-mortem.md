---
domain: requirements
tags: [pre-mortem, prospective-hindsight, risk-identification, specification]
last-updated: 2026-04-29
---

# Pre-Mortem Technique

## Key Takeaways

- Prospective hindsight catches approximately 30% more issues than forward-looking review (Klein, 1998); frame the question as "it already failed: why?" to activate explanation mode.
- Apply the pre-mortem at four levels of granularity: specification (missing observable behaviours), behavior (failure modes per distinct outcome), architecture (design principle violations), and implementation (design self-declaration).
- At specification: "Imagine this feature was built exactly as described, all tests pass, but it doesn't work for the user. What would be missing?"
- At behavior: "Imagine this specific behaviour went wrong in production — how?" Run per distinct `Then` outcome after grouping Examples per [[requirements/gherkin#concepts]]; add Examples for surfaced failure modes.
- At architecture: for each candidate class check [[software-craft/object-calisthenics#key-takeaways]] and [[software-craft/solid#key-takeaways]]; for each external dependency check [[architecture/technical-design#key-takeaways]]; for each noun check if it serves double duty across modules.
- All pre-mortems are enforced by condition gates in the flow: they are not optional exercises.

## Concepts

**Prospective Hindsight Mechanism**: Asking "imagine this failed: why?" catches 30% more issues than forward-looking review (Klein, 1998). The brain is better at explaining past events than predicting future ones (Kahneman, 2011). By framing as "it already failed," you activate explanation mode (System 2 reasoning) rather than prediction mode (System 1 heuristic).

**Specification Pre-Mortem**: Ask "What observable behaviours must we prove for this Rule to be complete?" This surfaces hidden requirements that forward-looking analysis misses.

**Behavior Pre-Mortem**: Ask "Imagine this specific behaviour went wrong in production — how would it fail?" Once Examples are grouped by distinct `Then` outcome per [[requirements/gherkin#concepts]], run this pre-mortem for each outcome independently. The framing varies by rule type:
- **Action rules**: "A user performs this action. What subtle real-world conditions would cause it to produce the wrong result?" (e.g., concurrent writes, stale reads, rounding, timezone shifts)
- **Behavioural rules**: "The system applies this business rule. What edge-case inputs would expose a gap in the logic?" (e.g., boundary crossing, empty/zero/null, ordering dependency)
- **Structural/invariant rules**: "This invariant must always hold. What counterexamples would break it?" — surface candidate counterexamples, then capture them in a Hypothesis property test per [[software-craft/test-design#concepts]] rather than as additional BDD Examples.
Add Examples for the failure modes surfaced. This is a distinct level from specification pre-mortem: specification asks "what behaviours are missing from the rule?"; behavior asks "how could this specific outcome fail in production?" per the prospective hindsight mechanism (Klein, 1998).

**Architecture Pre-Mortem**: Ask "In 6 months this design is a mess. What mistakes did we make?" Check each candidate class per [[software-craft/object-calisthenics]] and [[software-craft/solid]]. Check each external dependency per [[architecture/technical-design]]. Check each noun for cross-module double duty.

**Flow Condition Gates**: Pre-mortem completion is enforced by condition gates in the flow YAML. Self-declaration uses explicit AGREE/DISAGREE commitments (a commitment device (Cialdini, 2001) that makes the declaration psychologically binding). Adversarial framing during pre-mortem analysis ("find what's wrong" rather than "confirm it's right") uses adversarial collaboration (Mellers et al., 2001) to produce stronger reasoning.

## Content

### Specification Pre-Mortem

Ask:

> "Imagine the software-engineer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"

Record the findings as additional Rules or in interview notes.

### Behavior Pre-Mortem

Once Examples are grouped by distinct `Then` outcome per [[requirements/gherkin#concepts]], run for each outcome:

- **Action rules**: "A user performs this action. What subtle real-world conditions would cause it to produce the wrong result?" (e.g., concurrent writes, stale reads, rounding, timezone shifts)
- **Behavioural rules**: "The system applies this business rule. What edge-case inputs would expose a gap in the logic?" (e.g., boundary crossing, empty/zero/null, ordering dependency)
- **Structural/invariant rules**: "This invariant must always hold. What counterexamples would break it?" — surface candidate counterexamples, then capture them in a Hypothesis property test per [[software-craft/test-design#concepts]] rather than as additional BDD Examples.

Add Examples for the failure modes surfaced. This is a distinct level from specification pre-mortem: specification asks "what behaviours are missing from the rule?"; behavior asks "how could this specific outcome fail in production?"

### Architecture Pre-Mortem

Ask:

> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class, check per [[software-craft/object-calisthenics#concepts]] and [[software-craft/solid#concepts]].

For each external dependency, check per [[architecture/technical-design#concepts]].

For each noun, check for cross-module double duty.

### Implementation Pre-Mortem

The design self-declaration covers YAGNI, KISS, DRY, Object Calisthenics per [[software-craft/object-calisthenics#key-takeaways]], smells per [[software-craft/smell-catalogue#key-takeaways]], SOLID per [[software-craft/solid#key-takeaways]], and semantic alignment. This is the implementation-level pre-mortem, enforced by condition gates in the flow YAML.

## Related

- [[requirements/interview-techniques]]: gap-finding techniques used in interviews
- [[requirements/invest]]: INVEST criteria that pre-mortem findings may affect
- [[requirements/gherkin]]: writing Examples informed by pre-mortem analysis
- [[software-craft/tdd]]: design self-declaration subsumes the implementation pre-mortem
- [[software-craft/object-calisthenics]]: ObjCal-7 (two instance variables) checked in architecture pre-mortem
- [[software-craft/smell-catalogue]]: pattern smells checked in implementation pre-mortem
- [[software-craft/solid]]: SOLID checks in implementation pre-mortem
- [[software-craft/test-design]]: property-based testing for structural/invariant rules