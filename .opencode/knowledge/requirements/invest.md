---
domain: requirements
tags: [INVEST, rules, quality-criteria, self-declaration]
last-updated: 2026-04-29
---

# INVEST Criteria, Wake, 2003

## Key Takeaways

- Every Rule must pass all six INVEST letters: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- Each letter has a specific FAIL action: split or reorder dependencies (I), remove over-specification (N), reframe or drop (V), split or add discovery (E), split into smaller Rules (S), rewrite with observable outcomes (T).
- Common mistakes: Rules with no beneficiary lack business value; duplicate Rules should be merged or differentiated. Split triggers per [[requirements/decomposition#key-takeaways]].
- Self-declare INVEST-I, INVEST-V, INVEST-S, and INVEST-T; every DISAGREE is a hard blocker.

## Concepts

**INVEST Criteria**: Every Rule must pass all six letters. Independent means deliverable without other Rules. Negotiable means details open to discussion. Valuable means delivers something the user cares about. Estimable means a software-engineer can estimate effort. Small means completable in one feature cycle. Testable means verifiable with a concrete test.

**FAIL Actions**: Each letter has a specific corrective action when a Rule fails. Independent → split or reorder dependencies. Negotiable → remove over-specification. Valuable → reframe or drop. Estimable → split or add discovery questions. Small → split into smaller Rules. Testable → rewrite with observable outcomes.

**Self-Declaration**: Declare INVEST-I (each Rule is Independent), INVEST-V (each Rule delivers Value to a named user), INVEST-S (each Rule is Small enough for one development cycle), and INVEST-T (each Rule is Testable). Every DISAGREE is a hard blocker. The procedural steps for self-declaration are in the refine-features skill.

## Content

### INVEST Criteria Table

| Letter | Question | FAIL action |
|---|---|---|
| **I**ndependent | Can this Rule be delivered without other Rules? | Split or reorder dependencies |
| **N**egotiable | Are details open to discussion with the software-engineer? | Remove over-specification |
| **V**aluable | Does it deliver something the end user cares about? | Reframe or drop |
| **E**stimable | Can a software-engineer estimate the effort? | Split or add discovery questions |
| **S**mall | Completable in one feature cycle? | Split into smaller Rules |
| **T**estable | Can it be verified with a concrete test? | Rewrite with observable outcomes |

### Common Mistakes to Avoid

- Rule with no beneficiary: no business value. Every Rule must name a user role who benefits.
- Duplicate Rules: merge or differentiate.
- Split triggers (bounded context, independently testable outcomes): per [[requirements/decomposition#key-takeaways]]
### Self-Declaration Protocol

Before committing Rules, declare:

- INVEST-I: each Rule is Independent. AGREE/DISAGREE
- INVEST-V: each Rule delivers Value to a named user. AGREE/DISAGREE
- INVEST-S: each Rule is Small enough for one development cycle. AGREE/DISAGREE
- INVEST-T: each Rule is Testable. AGREE/DISAGREE

Every DISAGREE is a hard blocker.

## Related

- [[requirements/moscow]]: prioritizing Examples within a Rule
- [[requirements/decomposition]]: splitting Rules that fail INVEST-S or span bounded contexts
- [[requirements/gherkin]]: writing Examples from INVEST-qualified Rules
- [[requirements/pre-mortem]]: finding hidden failure modes in rules