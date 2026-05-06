---
domain: requirements
tags: [pre-mortem, prospective-hindsight, risk-identification, specification]
last-updated: 2026-04-29
---

# Pre-Mortem Technique

## Key Takeaways

- Prospective hindsight catches approximately 30% more issues than forward-looking review (Klein, 1998); frame the question as "it already failed: why?" to activate explanation mode.
- Apply the pre-mortem at three levels of granularity: specification (missing observable behaviours), architecture (design principle violations), and implementation (design self-declaration).
- At specification: "Imagine this feature was built exactly as described, all tests pass, but it doesn't work for the user. What would be missing?"
- At architecture: for each candidate class check [[software-craft/object-calisthenics#key-takeaways]] and [[software-craft/solid#key-takeaways]]; for each external dependency check [[architecture/hexagonal#key-takeaways]]; for each noun check if it serves double duty across modules.
- All pre-mortems are enforced by condition gates in the flow: they are not optional exercises.

## Concepts

**Prospective Hindsight Mechanism**: Asking "imagine this failed: why?" catches 30% more issues than forward-looking review (Klein, 1998). The brain is better at explaining past events than predicting future ones (Kahneman, 2011). By framing as "it already failed," you activate explanation mode (System 2 reasoning) rather than prediction mode (System 1 heuristic).

**Specification Pre-Mortem**: Ask "What observable behaviours must we prove for this Rule to be complete?" This surfaces hidden requirements that forward-looking analysis misses.

**Architecture Pre-Mortem**: Ask "In 6 months this design is a mess. What mistakes did we make?" Check each candidate class per [[software-craft/object-calisthenics]] and [[software-craft/solid]]. Check each external dependency per [[architecture/hexagonal]]. Check each noun for cross-module double duty.

**Flow Condition Gates**: Pre-mortem completion is enforced by condition gates in the flow YAML. Self-declaration uses explicit AGREE/DISAGREE commitments (a commitment device (Cialdini, 2001) that makes the declaration psychologically binding). Adversarial framing during pre-mortem analysis ("find what's wrong" rather than "confirm it's right") uses adversarial collaboration (Mellers et al., 2001) to produce stronger reasoning.

## Content

### Specification Pre-Mortem

Ask:

> "Imagine the software-engineer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"

Record the findings in the feature's Questions section or as additional Rules.

### Architecture Pre-Mortem

Ask:

> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class, check per [[software-craft/object-calisthenics#concepts]] and [[software-craft/solid#concepts]].

For each external dependency, check per [[architecture/hexagonal#concepts]].

For each noun, check for cross-module double duty.

### Implementation Pre-Mortem

The design self-declaration covers YAGNI, KISS, DRY, Object Calisthenics per [[software-craft/object-calisthenics#key-takeaways]], smells per [[software-craft/smell-catalogue#key-takeaways]], SOLID per [[software-craft/solid#key-takeaways]], and semantic alignment. This is the implementation-level pre-mortem, enforced by condition gates in the flow YAML.

## Related

- [[requirements/interview-techniques]]: gap-finding techniques used in interviews
- [[requirements/invest]]: story quality criteria that pre-mortem findings may affect
- [[requirements/gherkin]]: writing Examples informed by pre-mortem analysis
- [[software-craft/tdd]]: design self-declaration subsumes the implementation pre-mortem
- [[software-craft/object-calisthenics]]: ObjCal-7 (two instance variables) checked in architecture pre-mortem
- [[software-craft/smell-catalogue]]: pattern smells checked in implementation pre-mortem
- [[software-craft/solid]]: SOLID checks in implementation pre-mortem