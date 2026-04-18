---
name: scope
description: Step 1 — discover requirements through stakeholder interviews and write Gherkin acceptance criteria
version: "4.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Scope

This skill guides the PO through Step 1 of the feature lifecycle: interviewing the stakeholder, discovering requirements, and writing Gherkin specifications precise enough for a developer to write tests without asking questions.

## When to Use

When the PO is starting a new project or a new feature. The output is a set of `.feature` files in `docs/features/backlog/`.

## Overview

Step 1 has 4 phases:

| Phase | Who | Output |
|---|---|---|
| 1. Project Discovery | PO + stakeholder | `docs/features/discovery.md` + feature list |
| 2. Feature Discovery | PO + stakeholder | Discovery section embedded in `docs/features/backlog/<name>.feature` |
| 3. Stories | PO alone | `Rule:` blocks in the `.feature` file (no Examples) |
| 4. Criteria | PO alone | `Example:` blocks with `@id` tags under each `Rule:` |

Each phase produces a template-gated deliverable. A section must be complete and confirmed before the next section unlocks. Template enforcement is the process discipline — not a "baseline" command.

---

## Gap-Finding Techniques

Three techniques are applied across all interview sessions to surface what stakeholders have not yet said. Use them during every session, not just at the end.

### Critical Incident Technique (CIT) — Flanagan 1954
Ask about a specific past event rather than a general description. Schema-based recall ("usually we...") hides edge cases and workarounds. A concrete incident forces actual memory.

- "Tell me about a specific time when [X] worked exactly as you needed."
- "Tell me about a specific time when [X] broke down or frustrated you."
- Probe each incident: "What task were you doing? What happened next? What made it effective / ineffective?"

### Laddering / Means-End Chain — Reynolds & Gutman 1988
Climb from surface feature to underlying consequence to terminal value. The first answer is rarely the real constraint.

- "Why is that important to you?"
- "What does that enable?"
- "What would break if that were not available?"
- Stop when the stakeholder reaches a value they cannot explain further.

### CI Perspective Change — Fisher & Geiselman 1987
Ask the stakeholder to describe the same situation from another actor's point of view. Peripheral details and cross-role concerns surface that the primary perspective conceals.

- "What do you think the end user experiences in that situation?"
- "What would your team lead's concern be here?"
- "From the perspective of someone encountering this for the first time, what would they need to know?"

---

## Active Listening Protocol

Three levels of active listening apply throughout every interview session:

- **Level 1 — Per answer**: immediately paraphrase each answer before moving to the next question. "So if I understand correctly, you're saying that X happens when Y?" Catches misunderstanding in the moment.
- **Level 2 — Per group**: brief synthesis when transitioning between behavior groups. "We've covered [area A] and [area B]. Before I ask about [area C], here is what I understood so far: [summary]. Does that capture it?" Confirms completeness, gives stakeholder a recovery point.
- **Level 3 — End of session**: full synthesis of everything discussed. Present to stakeholder for approval. This is the accuracy gate, the baseline signal, and the input to domain modeling.

Do not introduce topic labels or categories during active listening. The summary must reflect what the stakeholder said, not new framing that prompts reactions to things they haven't considered.

---

## Phase 1 — Project Discovery

**When**: Once per project, before any features are scoped. **Skip entirely if `discovery.md` Status is `BASELINED`.** Adding features to an existing project: append new questions to Session 1 and re-fill from there.

### Session 1 — Individual Scope Elicitation

**Before the session**: Create `docs/features/discovery.md` using the project-level discovery template. Open to the Session 1 section.

**Ask the 7 standard questions** (present all at once):

1. **Who** are the users of this product?
2. **What** does the product do at a high level?
3. **Why** does it exist — what problem does it solve?
4. **When** and **where** is it used (environment, platform, context)?
5. **Success** — how do we know it works? What does "done" look like?
6. **Failure** — what does failure look like? What must never happen?
7. **Out-of-scope** — what are we explicitly not building?

**During the session**: Apply Level 1 active listening (paraphrase each answer). Apply CIT, Laddering, and CI Perspective Change per answer to surface gaps. Add new questions to the Questions table as they arise — do not defer to a later session.

**After the session**:

1. Write the **Session 1 Synthesis** in `discovery.md`: a 3–5 sentence summary of who the users are, what the product does, why it exists, its success/failure conditions, and explicit out-of-scope boundaries.
2. Present the synthesis to the stakeholder: "Here is my understanding of what you told me — please correct anything that is missing or wrong."
3. Stakeholder confirms or corrects. PO refines until approved.
4. Run a **silent pre-mortem** on the confirmed synthesis: "Imagine we build exactly what was described, ship it, and it fails. What was missing?" Add any discoveries as new questions to the Questions table.
5. Mark `Template §1: CONFIRMED` in `discovery.md`. This unlocks Session 2.

### Session 2 — Behavior Groups / Big Picture

**Before the session**: Review the confirmed Session 1 synthesis. Identify behavior groups (cross-cutting concerns, system-wide constraints, integration points, lifecycle questions). Prepare group-level questions.

**During the session**: Apply Level 1 active listening per answer. Apply Level 2 active listening when transitioning between groups. Apply CIT, Laddering, and CI Perspective Change per group. Add new questions in the moment.

**After the session**:

1. For each group, write a **Group Summary** in `discovery.md`.
2. Mark `Template §2: CONFIRMED` in `discovery.md`. This unlocks Session 3.

### Session 3 — Synthesis Approval + Feature Derivation

**Before the session**: Produce a **Full Synthesis** across all behavior groups from Sessions 1 and 2. Write it to `discovery.md`.

**During the session**: Present the full synthesis to the stakeholder. "This is my understanding of the full scope. Please correct anything that is missing or wrong." Stakeholder approves or corrects. PO refines until the stakeholder explicitly approves.

**After the session** (PO alone):

1. Domain analysis: extract all nouns (candidate entities) and verbs (candidate operations) from the approved synthesis.
2. Group nouns into subject areas (Bounded Contexts: where the same word means different things, a new context begins).
3. Name each subject area as a feature using FDD "Action object" triples: "Calculate the total of a sale", "Validate the password of a user", "Enroll a student in a seminar".
4. For each feature: create `docs/features/backlog/<name>.feature` using the feature file template (discovery section only — no Rules yet).
5. Write `Status: BASELINED (YYYY-MM-DD)` to `discovery.md`.

Commit: `feat(discovery): baseline project discovery`

---

## Phase 2 — Feature Discovery

**When**: Per feature, after project discovery is baselined. Each `.feature` file has its own 3-session discovery template in its description.

### Session 1 — Individual Entity Elicitation

**Before the session**: Open `docs/features/backlog/<name>.feature`.

1. **Populate the Entities table**: extract nouns (candidate classes) and verbs (candidate methods) from the project discovery synthesis that are relevant to this feature. Mark each as in-scope or not.
2. **Generate questions from entity gaps**: for each in-scope entity, ask internally:
   - What are its boundaries and edge cases?
   - What happens when it is missing, invalid, or at its limits?
   - How does it interact with other in-scope entities?
3. Add questions to the Session 1 Questions table.
4. Run a **silent pre-mortem**: "Imagine the developer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?" Add any discoveries as new questions.

**During the session**: Apply Level 1 active listening per answer. Apply CIT, Laddering, and CI Perspective Change per answer. Add new questions in the moment.

**After the session**:

1. Write the **Session 1 Synthesis** in the `.feature` file: summarize the key entities, their relationships, and the constraints that emerged.
2. Present the synthesis to the stakeholder. Stakeholder confirms or corrects. PO refines until approved.
3. Run a **silent pre-mortem** on the confirmed synthesis.
4. Mark `Template §1: CONFIRMED`. This unlocks Session 2.

### Session 2 — Behavior Groups / Big Picture for This Feature

**Before the session**: Review the confirmed Session 1 synthesis. Identify behavior groups within this feature (happy paths, error paths, edge cases, lifecycle events, integration points).

**During the session**: Apply Level 1 active listening per answer. Apply Level 2 active listening when transitioning between groups. Apply CIT, Laddering, and CI Perspective Change per group.

**After the session**:

1. Write **Group Summaries** in the `.feature` file. Name each group — these names become candidate `Rule:` titles.
2. Mark `Template §2: CONFIRMED`. This unlocks Session 3.

### Session 3 — Feature Synthesis Approval + Story Derivation

**Before the session**: Produce a **Full Synthesis** of the feature scope, covering all behavior groups from Sessions 1 and 2.

**During the session**: Present the full synthesis to the stakeholder. Stakeholder approves or corrects. PO refines until explicitly approved.

**After the session** (PO alone):

1. Map each named group from Session 2 to a candidate user story (Rule).
2. Write `Status: BASELINED (YYYY-MM-DD)` to the `.feature` file's discovery section.
3. Mark `Template §3: CONFIRMED`.

Commit: `feat(discovery): baseline <name> feature discovery`

### Decomposition Check

After Session 3, before moving to Phase 3:

Does this feature span **>2 distinct concerns** OR have **>8 candidate Examples**?

- **YES** → split into separate `.feature` files in `backlog/`, each addressing a single cohesive concern. Re-run Phase 2 for any split feature that needs its own discovery.
- **NO** → proceed to Phase 3.

---

## Phase 3 — Stories

**When**: After feature discovery is baselined and decomposition check passes. PO works alone.

### 3.1 Write Rule Blocks

Clusters from Phase 2 Session 2 → one `Rule:` block per user story. Add after the discovery section in the `.feature` file.

Each `Rule:` block contains:
- The rule title (2-4 words, kebab-friendly)
- The user story header as the rule description (no `Example:` blocks yet):

```gherkin
  Rule: Menu Display
    As a player
    I want to see a menu when the game starts
    So that I can select game options
```

Good stories are:
- **Independent**: can be delivered without other stories
- **Negotiable**: details can be discussed
- **Valuable**: delivers something the user cares about
- **Estimable**: the developer can estimate effort
- **Small**: completable in one feature cycle
- **Testable**: can be verified with a concrete test

Avoid: "As the system, I want..." (no business value). Break down stories that contain "and" into two Rules.

### 3.2 INVEST Gate

Before committing, verify every Rule passes:

| Letter | Question | FAIL action |
|---|---|---|
| **I**ndependent | Can this Rule be delivered without other Rules? | Split or reorder dependencies |
| **N**egotiable | Are details open to discussion with the developer? | Remove over-specification |
| **V**aluable | Does it deliver something the end user cares about? | Reframe or drop |
| **E**stimable | Can a developer estimate the effort? | Split or add discovery questions |
| **S**mall | Completable in one feature cycle? | Split into smaller Rules |
| **T**estable | Can it be verified with a concrete test? | Rewrite with observable outcomes |

### 3.3 Review Checklist

- [ ] Every Rule has a distinct user role and benefit
- [ ] No Rule duplicates another
- [ ] Rules collectively cover all entities marked in-scope in the discovery section
- [ ] Every Rule passes the INVEST gate

Commit: `feat(stories): write user stories for <name>`

---

## Phase 4 — Criteria

**When**: After stories are written. PO works alone.

### 4.1 Silent Pre-mortem Per Rule

For each `Rule:` block, ask internally before writing any Examples:

> "What observable behaviors must we prove for this Rule to be complete?"

All Rules must have their pre-mortems completed before any Examples are written.

### 4.2 Write Example Blocks

Add `Example:` blocks under each `Rule:`. Each Example gets an `@id:<8-char-hex>` tag.

**Format** (mandatory):

```gherkin
  Rule: Wall bounce
    As a game engine
    I want balls to bounce off walls
    So that gameplay feels physical

    @id:a3f2b1c4
    Example: Ball bounces off top wall
      Given a ball moving upward reaches y=0
      When the physics engine processes the next frame
      Then the ball velocity y-component becomes positive
```

**Rules**:
- `@id` tag on the line before `Example:`
- `Example:` keyword (not `Scenario:`)
- `Given/When/Then` in plain English
- `Then` must be a single, observable, measurable outcome — no "and"
- **Observable means observable by the end user**, not by a test harness
- **Declarative, not imperative** — describe behavior, not UI steps
- Each Example must be observably distinct from every other
- If a single feature spans multiple concerns, split into separate `.feature` files
- If user interaction is involved, the Feature description must declare the interaction model

**Declarative vs. imperative Gherkin**:

| Imperative (wrong) | Declarative (correct) |
|---|---|
| Given I type "bob" in the username field | Given a registered user Bob |
| When I click the Login button | When Bob logs in |
| Then I see "Welcome, Bob" on the dashboard | Then Bob sees a personalized welcome |

**MoSCoW triage**: For each candidate Example, classify as Must (required for the Rule to be correct), Should (high value but deferrable), or Could (nice-to-have edge case). If Musts alone exceed 8 or the Rule spans >2 concerns, split the Rule.

**Common mistakes to avoid**:
- "Then: It works correctly" — not measurable
- "Then: The system updates the database and sends an email" — split into two Examples
- Multiple behaviors in one Example — split them
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behavior descriptions

### 4.3 Review Checklist

Before committing:
- [ ] Every `Rule:` block has at least one Example
- [ ] Every `@id` is unique within this feature
- [ ] Every Example has `Given/When/Then`
- [ ] Every `Then` is a single, observable, measurable outcome
- [ ] No Example tests implementation details
- [ ] If user interaction is involved, the interaction model is declared in the Feature description
- [ ] Each Example is observably distinct from every other
- [ ] No single feature file spans multiple unrelated concerns

### 4.4 Commit and Freeze

```bash
git add docs/features/backlog/<name>.feature
git commit -m "feat(criteria): write acceptance criteria for <name>"
```

**After this commit, the `Example:` blocks are frozen.** Any change requires:
1. Add `@deprecated` tag to the old Example
2. Write a new Example with a new `@id`

---

## Feature File Format

Each feature is a single `.feature` file. The free-form description before the first `Rule:` contains all discovery content. Architecture is added later by the developer (Step 2).

```gherkin
Feature: <Feature title>

  Discovery:

  Status: ELICITING | BASELINED (YYYY-MM-DD)

  Entities:
  | Type | Name | Candidate Class/Method | In Scope |
  |------|------|----------------------|----------|
  | Noun | Ball | Ball                 | Yes      |
  | Verb | Bounce | Ball.bounce()      | Yes      |

  Rules (Business):
  - <Business rule that applies across multiple Examples>

  Constraints:
  - <Non-functional requirement specific to this feature>

  Session 1 — Individual Entity Elicitation:
  | ID | Question | Answer | Status |
  |----|----------|--------|--------|
  | Q1 | ... | ... | OPEN / ANSWERED |
  Template §1: CONFIRMED
  Synthesis: <PO synthesis — confirmed by stakeholder>

  Session 2 — Behavior Groups / Big Picture:
  | ID | Question | Answer | Status |
  |----|----------|--------|--------|
  | Q2 | ... | ... | OPEN / ANSWERED |
  Template §2: CONFIRMED
  Behavior Groups:
  - <Behavior group name>: <one-sentence summary>

  Session 3 — Feature Synthesis:
  Synthesis: <full synthesis across all behavior groups>
  Template §3: CONFIRMED — stakeholder approved YYYY-MM-DD

  Rule: <User story title>
    As a <role>
    I want <goal>
    So that <benefit>

    @id:a3f2b1c4
    Example: <Concrete scenario title>
      Given <initial context>
      When <event or action>
      Then <observable outcome>

    @deprecated @id:b5c6d7e8
    Example: <Superseded scenario>
      Given ...
      When ...
      Then ...
```

The **Rules (Business)** section captures business rules that hold across multiple Examples. Identifying rules first prevents redundant or contradictory Examples.

The **Constraints** section captures non-functional requirements. Testable constraints should become `Example:` blocks with `@id` tags.

---

## Project-Level Discovery (`docs/features/discovery.md`)

```markdown
# Discovery: <project-name>

## State
Status: ELICITING | BASELINED (YYYY-MM-DD)

## Session 1 — Individual Scope Elicitation

| ID | Question | Answer | Status |
|----|----------|--------|--------|
| Q1 | Who are the users? | ... | OPEN / ANSWERED |

Template §1: CONFIRMED
Synthesis: <PO synthesis — confirmed by stakeholder>
Pre-mortem: <gaps identified; new questions added above>

## Session 2 — Behavior Groups / Big Picture

| ID | Question | Answer | Status |
|----|----------|--------|--------|
| Q2 | ... | ... | OPEN / ANSWERED |

Template §2: CONFIRMED
Behavior Groups:
- <Behavior group name>: <one-sentence summary>

## Session 3 — Full Synthesis

<3–6 paragraph synthesis of all scope, behavior groups, and boundaries>

Template §3: CONFIRMED — stakeholder approved YYYY-MM-DD
```

No Entities table at project level.
