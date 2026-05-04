---
domain: requirements
tags: [feature-discovery, story-mapping, backlog-creation, discovery]
last-updated: 2026-05-04
---

# Feature Discovery

## Key Takeaways

- Feature discovery materializes `.feature` file stubs from the delivery order, domain model, and interview notes. It is a mechanical step, not a new workshop — the stories were already identified during earlier discovery states.
- Each `.feature` file receives a title, 2-4 sentence description, coarse Rules (Business) bullet points, and Constraints — but NOT full Rule blocks (As a/I want/So that) or Examples.
- Story mapping and event storming (earlier discovery states) produced the bounded contexts, domain events, and delivery order that feed this step. This state just writes the stubs.
- Features enter `Status: ELICITING` during discovery. They advance to `BASELINED` after planning (breakdown + BDD + baseline confirmation).
- The feature-discovery state bridges discovery (domain model, scope) and planning (per-feature specification and development).

## Concepts

**Feature Discovery as Materialization**: After Event Storming identifies bounded contexts, the domain model formalizes entities and aggregates, and the scope boundary defines the delivery order, feature discovery materializes this work into `.feature` file stubs. It reads the existing artifacts and writes one stub per delivery order step. The "discovery" already happened in earlier states — this step captures it in the feature template format.

**Story Mapping and Event Storming as Precursors** (Patton, 2014; Brandolini, 2012): The bounded contexts, domain events, and delivery order produced by earlier discovery states ARE the story map's backbone and release slices. Feature discovery translates that map into the `.feature` template format — coarse Rules (Business) bullet points serve as one-line story summaries.

**Feature Lifecycle**: Features follow a three-stage lifecycle across flows:
1. **Discovery** (`feature-discovery` state): Story mapping creates `.feature` stubs with title, description, coarse Rules (Business), and Constraints. Status: ELICITING.
2. **Planning** (`feature-breakdown` state): Coarse Rules are expanded into full Rule blocks with As a/I want/So that format. INVEST validation is applied. Status remains ELICITING.
3. **Planning** (`ready` state): After BDD Examples are written and baseline confirmed, Status advances to BASELINED.

**Coarse vs. Detailed Rules**: The `Rules (Business)` section in the `.feature` template receives one-line bullet points during discovery — e.g., "Token identifies a tradeable asset by symbol." Full `Rule:` blocks with As a/I want/So that format are written during planning's `feature-breakdown` state. This separation prevents premature specification (Cohn, 2004) while ensuring the whole product is mapped before any single feature is developed.

## Related

- [[requirements/invest]] — story quality criteria applied during planning refinement
- [[requirements/wsjf]] — feature prioritization applied to BASELINED features
- [[requirements/gherkin]] — Examples written during planning BDD phase
- [[requirements/interview-techniques]] — interview methods used during discovery
- [[requirements/decomposition]] — splitting Rules during planning refinement
