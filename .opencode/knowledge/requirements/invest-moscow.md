---
domain: requirements
tags: [stories, prioritization, INVEST, MoSCoW]
last-updated: 2026-04-26
---

# INVEST and MoSCoW

## Key Takeaways

- Every Rule must pass all six INVEST letters before committing: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- MoSCoW triage classifies Examples as Must (required for correctness), Should (high value but deferrable), or Could (nice-to-have edge case).
- If Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, split the Rule immediately.
- The PO must self-declare INVEST-I, INVEST-V, INVEST-S, and INVEST-T before committing stories; every DISAGREE is a hard blocker.

## Concepts

**INVEST Criteria**: Every Rule (user story) must pass all six letters before committing. Independent means deliverable without other Rules. Negotiable means details open to discussion. Valuable means delivers something the user cares about. Estimable means a software-engineer can estimate effort. Small means completable in one feature cycle. Testable means verifiable with a concrete test.

**MoSCoW Triage**: For each candidate Example, classify priority as Must (required for correctness, without it the feature is wrong), Should (high value but deferrable, the feature works without it but is diminished), or Could (nice-to-have edge case, low risk if deferred).

**Split Rules**: If Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, split the Rule immediately.

**INVEST Self-Declaration**: Before committing stories, the PO must self-declare INVEST-I, INVEST-V, INVEST-S, and INVEST-T. Every DISAGREE is a hard blocker. Common mistakes: "As the system, I want..." has no business value; stories containing "and" should be split; duplicate stories should be merged or differentiated.

## Content

### INVEST Criteria

Every Rule (user story) must pass all six letters before committing:

| Letter | Question | FAIL action |
|---|---|---|
| **I**ndependent | Can this Rule be delivered without other Rules? | Split or reorder dependencies |
| **N**egotiable | Are details open to discussion with the software-engineer? | Remove over-specification |
| **V**aluable | Does it deliver something the end user cares about? | Reframe or drop |
| **E**stimable | Can a software-engineer estimate the effort? | Split or add discovery questions |
| **S**mall | Completable in one feature cycle? | Split into smaller Rules |
| **T**estable | Can it be verified with a concrete test? | Rewrite with observable outcomes |

### Good Stories Characteristics

- **Independent**: can be delivered without other stories
- **Negotiable**: details can be discussed
- **Valuable**: delivers something the user cares about
- **Estimable**: the software-engineer can estimate effort
- **Small**: completable in one feature cycle
- **Testable**: can be verified with a concrete test

### Common Mistakes to Avoid

- "As the system, I want..." — no business value. Every story must name a user role who benefits.
- Stories containing "and" — break them into two separate Rules.
- Stories that duplicate another Rule — merge or differentiate.
- Stories that span multiple unrelated concerns — split immediately.

### MoSCoW Triage

For each candidate Example, classify priority:

- **Must**: required for the Rule to be correct. Without it, the feature is wrong.
- **Should**: high value but deferrable. The feature works without it but is diminished.
- **Could**: nice-to-have edge case. Low risk if deferred.

If Musts alone exceed 8 or the Rule spans >2 concerns, split the Rule.

### INVEST Self-Declaration

Before committing stories, the PO must declare:

- INVEST-I: each Rule is Independent — AGREE/DISAGREE
- INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE
- INVEST-S: each Rule is Small enough for one development cycle — AGREE/DISAGREE
- INVEST-T: each Rule is Testable — AGREE/DISAGREE

Every DISAGREE is a hard blocker — fix before committing.

## Related

- [[requirements/discovery-techniques]] — techniques for surfacing stories during interviews
- [[requirements/gherkin]] — writing Examples from triaged stories
- [[requirements/wsjf]] — scoring features for backlog priority