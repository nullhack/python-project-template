---
domain: requirements
tags: [pre-mortem, prospective-hindsight, risk-identification, specification]
last-updated: 2026-04-29
---

# Pre-Mortem Technique

## Key Takeaways

- Prospective hindsight catches approximately 30% more issues than forward-looking review (Klein, 1998); frame the question as "it already failed — why?" to activate explanation mode.
- Apply the pre-mortem at three stages: before writing Examples (specification), before writing design or stubs (architecture), and before implementation (TDD).
- At specification: "Imagine this feature was built exactly as described, all tests pass, but it doesn't work for the user. What would be missing?"
- At architecture: for each candidate class check >2 instance variables (Object Calisthenics — Bay, 2008) or >1 reason to change (SRP — Martin, 2000); for each external dependency check if it is behind a Protocol (Hexagonal Architecture — Cockburn, 2005); for each noun check if it serves double duty across modules.
- All pre-mortems must complete before moving to the next stage; they are condition gates in the flow, not optional exercises.

## Concepts

**Prospective Hindsight Mechanism**: Asking "imagine this failed — why?" catches 30% more issues than forward-looking review (Klein, 1998). The brain is better at explaining past events than predicting future ones (Kahneman, 2011). By framing as "it already failed," you activate explanation mode (System 2 reasoning) rather than prediction mode (System 1 heuristic).

**Specification Pre-Mortem**: Before writing Examples for any Rule, ask "What observable behaviours must we prove for this Rule to be complete?" All Rules must have their pre-mortems completed before any Examples are written. This surfaces hidden requirements that forward-looking analysis misses.

**Architecture Pre-Mortem**: Before writing design or stubs, ask "In 6 months this design is a mess. What mistakes did we make?" Check each candidate class for >2 instance variables → split (Object Calisthenics — Bay, 2008) or >1 reason to change → isolate (SRP — Martin, 2000). Check each external dependency for Protocol encapsulation (Hexagonal Architecture — Cockburn, 2005). Check each noun for cross-module double duty.

**Flow Condition Gates**: Pre-mortem completion is encoded as condition gates in the flow YAML. The `premortem_done` condition on `bdd-features.done` requires `premortem_done: ==true`. The `design_declared` condition on `tdd-cycle.all_green` requires self-declaration including design correctness checks that subsume the architecture pre-mortem. Self-declaration uses explicit AGREE/DISAGREE commitments — a commitment device (Cialdini, 2001) that makes the declaration psychologically binding. Adversarial framing during pre-mortem analysis — "find what's wrong" rather than "confirm it's right" — leverages adversarial collaboration (Mellers et al., 2001) to produce stronger reasoning.

## Content

### Specification Pre-Mortem

Before writing Examples for any Rule:

> "Imagine the software-engineer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"

All Rules must have their pre-mortems completed before any Examples are written. Record the findings in the feature's Questions section or as additional Rules.

In the planning flow, this is enforced by the `premortem_done` condition on the `bdd-features.done` transition.

### Architecture Pre-Mortem

Before writing design or stubs:

> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class:
- >2 instance variables? → split (Object Calisthenics — Bay, 2008)
- >1 reason to change? → isolate (SRP — Martin, 2000)

For each external dependency:
- Is it behind a Protocol? → if not, add one (Hexagonal Architecture — Cockburn, 2005)

For each noun:
- Serving double duty across modules? → isolate into separate contexts

### Implementation Pre-Mortem

Before the TDD cycle, the design self-declaration covers YAGNI, KISS, DRY, Object Calisthenics per [[software-craft/object-calisthenics#key-takeaways]], smells per [[software-craft/smell-catalogue#key-takeaways]], SOLID per [[software-craft/solid#key-takeaways]], and semantic alignment. This is the TDD-stage pre-mortem, encoded as the `design_declared` condition on `tdd-cycle.all_green`.

## Related

- [[requirements/interview-techniques]] — gap-finding techniques used during discovery interviews
- [[requirements/invest]] — story quality criteria that pre-mortem findings may affect
- [[requirements/gherkin]] — writing Examples after pre-mortem analysis
- [[software-craft/tdd]] — design self-declaration subsumes the implementation pre-mortem
- [[software-craft/object-calisthenics]] — ObjCal-7 (two instance variables) checked in architecture pre-mortem
- [[software-craft/smell-catalogue]] — pattern smells checked in implementation pre-mortem
- [[software-craft/solid]] — SOLID checks in implementation pre-mortem