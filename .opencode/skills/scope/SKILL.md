---
name: scope
description: Step 1 — discover requirements through stakeholder interviews and write Gherkin acceptance criteria
version: "2.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Scope

This skill guides the PO through Step 1 of the feature lifecycle: interviewing the stakeholder, discovering requirements, and writing Gherkin specifications precise enough for a developer to write tests without asking questions.

## When to Use

When the PO is starting a new project or a new feature. The output is a set of discovery documents and `.feature` files in `docs/features/backlog/<name>/`.

## Overview

Step 1 has 4 phases:

| Phase | Who | Output |
|---|---|---|
| 1. Project Discovery | PO + stakeholder | `docs/features/discovery.md` + feature list |
| 2. Feature Discovery | PO + stakeholder | `docs/features/backlog/<name>/discovery.md` |
| 3. Stories | PO alone | `<story-slug>.feature` files (no Examples) |
| 4. Criteria | PO alone | `Example:` blocks with `@id` tags |

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

From the answers, identify the feature list. For each feature, create `docs/features/backlog/<name>/discovery.md` using the per-feature template (with Entities table).

Commit: `feat(discovery): baseline project discovery`

---

## Phase 2 — Feature Discovery

**When**: Per feature, after project discovery is baselined.

### 2.1 Populate Feature Discovery

Open `docs/features/backlog/<name>/discovery.md`. Fill in:

- **Entities table**: Extract nouns (candidate classes/models) and verbs (candidate methods/features) from project discovery answers relevant to this feature. Mark each as in-scope or not.
- **Questions table**: Add questions from:
  - Gaps not covered by project discovery
  - Ambiguities specific to this feature
  - Boundary conditions and error cases

### 2.2 Interview

Present all questions to the stakeholder at once. Follow up on unanswered ones.

### 2.3 Silent Pre-mortem

After each round of answers:

> "Imagine the developer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"

Add any discoveries as new questions.

### 2.4 Baseline

When the stakeholder says "baseline", set `Status: BASELINED` in the feature `discovery.md`.

Commit: `feat(discovery): baseline <name> feature discovery`

---

## Phase 3 — Stories

**When**: After feature discovery is baselined. PO works alone.

### 3.1 Write User Story Files

Create one `.feature` file per user story in `docs/features/backlog/<name>/`.

Filename: `<story-slug>.feature` — kebab-case, 2-4 words.

Content (no Examples yet):

```gherkin
Feature: <Title in natural language>
  As a <role>
  I want <goal>
  So that <benefit>
```

Good stories are:
- **Independent**: can be delivered without other stories
- **Negotiable**: details can be discussed
- **Valuable**: delivers something the user cares about
- **Estimable**: the developer can estimate effort
- **Small**: completable in one feature cycle
- **Testable**: can be verified with a concrete test

Avoid: "As the system, I want..." (no business value). Break down stories that contain "and" into two stories.

### 3.2 INVEST Gate

Before committing, verify every story passes:

| Letter | Question | FAIL action |
|---|---|---|
| **I**ndependent | Can this story be delivered without other stories? | Split or reorder dependencies |
| **N**egotiable | Are details open to discussion with the developer? | Remove over-specification |
| **V**aluable | Does it deliver something the end user cares about? | Reframe or drop |
| **E**stimable | Can a developer estimate the effort? | Split or add discovery questions |
| **S**mall | Completable in one feature cycle? | Split into smaller stories |
| **T**estable | Can it be verified with a concrete test? | Rewrite with observable outcomes |

### 3.3 Review Checklist

- [ ] Every story has a distinct user role and benefit
- [ ] No story duplicates another
- [ ] Stories collectively cover all entities marked in-scope in `discovery.md`
- [ ] Every story passes the INVEST gate

Commit: `feat(stories): write user stories for <name>`

---

## Phase 4 — Criteria

**When**: After stories are written. PO works alone.

### 4.1 Silent Pre-mortem Per Story

For each `.feature` file, ask internally:

> "What observable behaviors must we prove for this story to be complete?"

### 4.2 Write Example Blocks

Add `Example:` blocks to each `.feature` file. Each Example gets an `@id:<8-char-hex>` tag.

**ID generation**:
```bash
uv run task gen-id
```

**Format** (mandatory):

```gherkin
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
- Soft limit: 3-10 Examples per Feature; each must be observably distinct
- If user interaction is involved, the Feature description must declare the interaction model

**Declarative vs. imperative Gherkin**:

| Imperative (wrong) | Declarative (correct) |
|---|---|
| Given I type "bob" in the username field | Given a registered user Bob |
| When I click the Login button | When Bob logs in |
| Then I see "Welcome, Bob" on the dashboard | Then Bob sees a personalized welcome |

Write Examples that describe *what happens*, not *how the user clicks through the UI*. Imperative steps couple tests to specific UI layouts and break when the UI changes.

**MoSCoW triage**: When a story has more than 5 Examples, ask for each one: is this a **Must** (required for the story to be correct), a **Should** (high value but deferrable), or a **Could** (nice-to-have edge case)? If Musts alone exceed 10, the story needs splitting.

**Common mistakes to avoid**:
- "Then: It works correctly" (not measurable)
- "Then: The system updates the database and sends an email" (split into two Examples)
- Multiple behaviors in one Example (split them)
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behavior descriptions

### 4.3 Review Checklist

Before committing:
- [ ] Every `.feature` file has at least one Example
- [ ] Every `@id` is unique within this feature (check: `grep -r "@id:" docs/features/backlog/<name>/`)
- [ ] Every Example has `Given/When/Then`
- [ ] Every `Then` is a single, observable, measurable outcome
- [ ] No Example tests implementation details
- [ ] If user interaction is involved, the interaction model is declared in the Feature description
- [ ] Soft limit 3-10 Examples per Feature is respected (justify exceptions)

### 4.4 Final Pre-mortem

Before committing, one last check:

> "Imagine the developer builds exactly what these Examples say, all automated tests pass, but the feature doesn't work for the user. What would be missing?"

Add any discoveries as new Examples.

### 4.5 Commit and Freeze

```bash
git add docs/features/backlog/<name>/
git commit -m "feat(criteria): write acceptance criteria for <name>"
```

**After this commit, the `.feature` files are frozen.** Any change requires:
1. Add `@deprecated` tag to the old Example
2. Write a new Example with a new `@id`
3. Run `uv run task gen-tests` to sync test stubs

---

## Discovery Document Formats

### Project-Level (`docs/features/discovery.md`)

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

### Per-Feature (`docs/features/backlog/<name>/discovery.md`)

```markdown
# Discovery: <feature-name>

## State
Status: ELICITING | BASELINED

## Entities
| Type | Name | Candidate Class/Method | In Scope |
|------|------|----------------------|----------|
| Noun | Ball | Ball | Yes |
| Verb | Bounce | Ball.bounce() | Yes |

## Rules
Business rules that apply across multiple Examples. Each rule explains *why* a group of Examples exists.

- <Rule description>

## Constraints
Non-functional requirements specific to this feature (performance, security, usability, etc.).

- <Constraint description>

## Questions
| ID | Question | Answer | Status |
|----|----------|--------|--------|
| Q1 | ... | ... | OPEN / ANSWERED |
```

The **Rules** section captures the business-rule layer from Example Mapping: each rule may generate multiple Examples, and identifying rules first prevents redundant or contradictory Examples.

The **Constraints** section captures non-functional requirements. Testable constraints should become `Example:` blocks with `@id` tags. System-wide constraints belong in the project-level `discovery.md`.
