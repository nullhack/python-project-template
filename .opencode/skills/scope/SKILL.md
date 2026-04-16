---
name: scope
description: Step 1 — discover requirements through stakeholder interviews and write Gherkin acceptance criteria
version: "3.0"
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

---

## Phase 1 — Project Discovery

**When**: Once per project, before any features are scoped.

### 1.1 Create Project Discovery Document

Create `docs/features/discovery.md` with Status + Questions only (no Entities table). See the format in the "Discovery Document Formats" section below.

### 1.2 Ask the 7 Standard Questions

Present all questions to the stakeholder at once:

1. **Who** are the users of this product?
2. **What** does the product do at a high level?
3. **Why** does it exist — what problem does it solve?
4. **When** and **where** is it used (environment, platform, context)?
5. **Success** — how do we know it works? What does "done" look like?
6. **Failure** — what does failure look like? What must never happen?
7. **Out-of-scope** — what are we explicitly not building?

### 1.3 Silent Pre-mortem

After receiving answers, run this internally (do not show the stakeholder):

> "Imagine we build exactly what the stakeholder described, ship it, and it fails. What was missing from their answers?"

Generate targeted follow-up questions from this analysis. Add them to the Questions table in `discovery.md`.

### 1.4 Follow Up

Present all follow-up questions at once. Continue until all questions have status `ANSWERED`.

### 1.5 Baseline

When all questions are answered, autonomously set `Status: BASELINED` in `docs/features/discovery.md`.

From the answers, identify the feature list. For each feature, create `docs/features/backlog/<name>.feature` using the feature file template (discovery section only — no Rules yet).

Commit: `feat(discovery): baseline project discovery`

---

## Phase 2 — Feature Discovery

**When**: Per feature, after project discovery is baselined.

### 2.1 Derive Questions from Feature Entities

Open `docs/features/backlog/<name>.feature`. This step happens **before** any stakeholder interaction.

1. **Populate the Entities table**: Extract nouns (candidate classes/models) and verbs (candidate methods/features) from project discovery answers relevant to this feature. Mark each as in-scope or not.
2. **Generate questions from entities**: For each in-scope entity, ask:
   - What are its boundaries and edge cases?
   - What happens when it's missing, invalid, or at its limits?
   - How does it interact with other entities?
3. **Add questions from gaps**: Questions from areas not covered by project discovery, ambiguities specific to this feature, and boundary conditions.
4. **Silent pre-mortem** (before the first interview round):

> "Imagine the developer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"

Add any discoveries as new questions to the Questions table.

### 2.2 Interview

Present **all** questions to the stakeholder at once. After receiving answers:

1. Mark answered questions as `ANSWERED` in the Questions table
2. Run a silent pre-mortem on the new answers — generate follow-up questions
3. Present follow-up questions to the stakeholder
4. Repeat until the stakeholder says **"baseline"** to freeze discovery

### 2.3 Feature Decomposition Check

Before moving to Phase 3, check: does this feature span **>2 distinct concerns** OR have **>8 candidate Examples**? If yes:

1. Split into separate `.feature` files in `backlog/` — each addressing a single cohesive concern
2. Populate the discovery section for each split feature
3. Re-run Phase 2 for any split feature that needs its own discovery

### 2.4 Baseline

When the stakeholder says "baseline" (and decomposition check passes), set `Status: BASELINED (YYYY-MM-DD)` in the feature file's discovery section.

Commit: `feat(discovery): baseline <name> feature discovery`

---

## Phase 3 — Stories

**When**: After feature discovery is baselined. PO works alone.

### 3.1 Write Rule Blocks

Add one `Rule:` block per user story to the `.feature` file, after the discovery section.

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

For each `Rule:` block, ask internally:

> "What observable behaviors must we prove for this Rule to be complete?"

### 4.2 Write Example Blocks

Add `Example:` blocks under each `Rule:`. Each Example gets an `@id:<8-char-hex>` tag.

**ID generation**:
```bash
uv run task gen-id
```

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

Write Examples that describe *what happens*, not *how the user clicks through the UI*. Imperative steps couple tests to specific UI layouts and break when the UI changes.

**MoSCoW triage**: When a Rule spans multiple concerns or has many candidate Examples, ask for each one: is this a **Must** (required for the Rule to be correct), a **Should** (high value but deferrable), or a **Could** (nice-to-have edge case)? If the Rule spans >2 concerns or Musts alone exceed 8, the Rule needs splitting.

**Common mistakes to avoid**:
- "Then: It works correctly" (not measurable)
- "Then: The system updates the database and sends an email" (split into two Examples)
- Multiple behaviors in one Example (split them)
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behavior descriptions

### 4.3 Review Checklist

Before committing:
- [ ] Every `Rule:` block has at least one Example
- [ ] Every `@id` is unique within this feature (check: `grep "@id:" docs/features/backlog/<name>.feature`)
- [ ] Every Example has `Given/When/Then`
- [ ] Every `Then` is a single, observable, measurable outcome
- [ ] No Example tests implementation details
- [ ] If user interaction is involved, the interaction model is declared in the Feature description
- [ ] Each Example is observably distinct from every other
- [ ] No single feature file spans multiple unrelated concerns

### 4.4 Final Pre-mortem

Before committing, one last check:

> "Imagine the developer builds exactly what these Examples say, all automated tests pass, but the feature doesn't work for the user. What would be missing?"

Add any discoveries as new Examples.

### 4.5 Commit and Freeze

```bash
git add docs/features/backlog/<name>.feature
git commit -m "feat(criteria): write acceptance criteria for <name>"
```

**After this commit, the `Example:` blocks are frozen.** Any change requires:
1. Add `@deprecated` tag to the old Example
2. Write a new Example with a new `@id`
3. Run `uv run task gen-tests` to sync test stubs

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
  | Noun | Ball | Ball | Yes |
  | Verb | Bounce | Ball.bounce() | Yes |

  Rules (Business):
  - <Business rule that applies across multiple Examples>

  Constraints:
  - <Non-functional requirement specific to this feature>

  Questions:
  | ID | Question | Answer | Status |
  |----|----------|--------|--------|
  | Q1 | ... | ... | OPEN / ANSWERED |

  All questions answered. Discovery frozen.

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

The **Rules (Business)** section captures the business-rule layer: each rule may generate multiple Examples, and identifying rules first prevents redundant or contradictory Examples.

The **Constraints** section captures non-functional requirements. Testable constraints should become `Example:` blocks with `@id` tags.

### Project-Level Discovery (`docs/features/discovery.md`)

```markdown
# Discovery: <project-name>

## State
Status: ELICITING | BASELINED

## Questions
| ID | Question | Answer | Status |
|----|----------|--------|--------|
| Q1 | Who are the users? | ... | OPEN / ANSWERED |
```

No Entities table at project level.
