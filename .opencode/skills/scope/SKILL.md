---
name: scope
description: Step 1 — discover requirements through stakeholder interviews and write Gherkin acceptance criteria
version: "5.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Scope

This skill guides the PO through Step 1 of the feature lifecycle: interviewing the stakeholder, discovering requirements, and writing Gherkin specifications precise enough for a developer to write tests without asking questions.

## When to Use

When the PO is starting a new project, adding features, or refining an existing feature. The output is a set of `.feature` files in `docs/features/backlog/` ready for development.

## Overview

Step 1 has two stages:

| Stage | Who | Output |
|---|---|---|
| **Stage 1 — Discovery** | PO + stakeholder | `docs/discovery_journal.md` (Q&A) + `docs/discovery.md` (synthesis) + `.feature` descriptions |
| **Stage 2 — Specification** | PO alone | `Rule:` blocks + `Example:` blocks with `@id` tags in `.feature` files |

Stage 1 is iterative and ongoing — sessions happen whenever the PO or stakeholder needs to discover or refine scope. Stage 2 runs per feature, only after that feature has `Status: BASELINED`.

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
- **Level 3 — End of session**: full synthesis of everything discussed. Present to stakeholder for approval. This is the accuracy gate and the input to domain modeling.

Do not introduce topic labels or categories during active listening. The summary must reflect what the stakeholder said, not new framing that prompts reactions to things they haven't considered.

---

## Stage 1 — Discovery

Discovery is a continuous, iterative process. Sessions happen whenever scope needs to be established or refined — for a new project, for a new feature, or when new information emerges. There is no "Phase 1" vs "Phase 2" distinction; every session follows the same structure.

### Session Start (every session)

**Before asking any questions:**

1. Check `docs/discovery_journal.md` for the most recent session block.
   - If the most recent block has `Status: IN-PROGRESS` → the previous session was interrupted. Resume it: check which `.feature` files need updating (compare journal Q&A against current `.feature` descriptions), write the `discovery.md` synthesis block if missing, then mark the block `Status: COMPLETE`. Only then begin a new session.
   - If `docs/discovery_journal.md` does not exist → this is the first session. Create both `docs/discovery_journal.md` and `docs/discovery.md` using the templates at the end of this skill.
2. Open `docs/discovery_journal.md` and append a new session header:
   ```markdown
   ## YYYY-MM-DD — Session N
   Status: IN-PROGRESS
   ```
   Write this header **before** asking any questions. This is the durability marker — if the session is interrupted, the next agent sees `IN-PROGRESS` and knows writes are pending.

### Question Order (within every session)

Questions follow this order. Skip a group only if it was already fully covered in a prior session.

**1. General questions** (skip entirely if any prior session has covered these)

Ask all 7 at once:

1. **Who** are the users of this product?
2. **What** does the product do at a high level?
3. **Why** does it exist — what problem does it solve?
4. **When** and **where** is it used (environment, platform, context)?
5. **Success** — how do we know it works? What does "done" look like?
6. **Failure** — what does failure look like? What must never happen?
7. **Out-of-scope** — what are we explicitly not building?

Apply Level 1 active listening per answer. Apply CIT, Laddering, and CI Perspective Change per answer to surface gaps. Add new questions in the moment.

**2. Cross-cutting questions**

Target behavior groups, bounded contexts, integration points, lifecycle events, and system-wide constraints. Apply Level 2 active listening when transitioning between groups.

**3. Feature questions** (one feature at a time)

For each feature the session touches:
- Extract relevant nouns and verbs from `docs/discovery.md` Domain Model (if it exists)
- Generate questions from entity gaps: boundaries, edge cases, interactions, failure modes
- Run a silent pre-mortem: "Imagine the developer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"
- Apply CIT, Laddering, and CI Perspective Change per question

**Real-time split rule**: if, during feature questions, the PO detects >2 distinct concerns OR >8 candidate Examples for a single feature, **split immediately**:
1. Record the split in the journal: note the original feature name and the two new names
2. Create stub `.feature` files for both parts (if they don't already exist)
3. Continue feature questions for both new features in sequence within the same session

### After Questions (PO alone, same session)

**Step A — Write answered Q&A to journal**

Append all answered Q&A to `docs/discovery_journal.md`, in groups (general, cross-cutting, then per-feature). Write only answered questions. Unanswered questions are discarded.

Group headers use this format:
- General group: `### General`
- Cross-cutting group: `### <Group Name>`
- Feature group: `### Feature: <feature-name>`

**Step B — Update .feature descriptions**

For each feature touched in this session: rewrite the `.feature` file description to reflect the current state of understanding. Only touched features are updated; all others remain exactly as-is.

If a feature is new (just created as a stub): write its initial description now.

**Step C — Append session synthesis to discovery.md (LAST)**

After all `.feature` files are updated, append one `## Session: YYYY-MM-DD` block to `docs/discovery.md`. The block contains:
- `### Feature List` — which features were added or changed (0–N entries); if nothing changed, write "No changes"
- `### Domain Model` — new or updated domain entities and verbs; if nothing changed, write "No changes"
- `### Scope` (first session only) — 3–5 sentence synthesis of who the users are, what the product does, why it exists, success/failure conditions, and explicit out-of-scope

**Step D — Mark session complete**

Update the session header in `docs/discovery_journal.md`:
```markdown
## YYYY-MM-DD — Session N
Status: COMPLETE
```

**Commit**: `feat(discovery): <one-sentence summary of session>`

### Baselining a Feature

A feature is baselined when the stakeholder has explicitly approved its discovery. The PO writes `Status: BASELINED (YYYY-MM-DD)` in the `.feature` file.

**Gate**: a feature may only be baselined when:
- Its description accurately reflects the stakeholder's approved understanding
- Its candidate user stories (Rule candidates) are identified
- The decomposition check passes: does not span >2 concerns AND does not have >8 candidate Examples

A baselined feature is ready for Stage 2. The PO may baseline features one at a time — not all at once.

---

## Stage 2 — Specification

Stage 2 runs per feature, after `Status: BASELINED`. PO works alone. No stakeholder involvement.

If the PO discovers a gap during Stage 2 that requires stakeholder input: stop Stage 2, open a new Stage 1 session, resolve the gap, then return to Stage 2.

### Step A — Stories

Derive `Rule:` blocks from the baselined feature description. One `Rule:` per user story.

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

**INVEST Gate** — verify every Rule before committing:

| Letter | Question | FAIL action |
|---|---|---|
| **I**ndependent | Can this Rule be delivered without other Rules? | Split or reorder dependencies |
| **N**egotiable | Are details open to discussion with the developer? | Remove over-specification |
| **V**aluable | Does it deliver something the end user cares about? | Reframe or drop |
| **E**stimable | Can a developer estimate the effort? | Split or add discovery questions |
| **S**mall | Completable in one feature cycle? | Split into smaller Rules |
| **T**estable | Can it be verified with a concrete test? | Rewrite with observable outcomes |

**Review checklist:**
- [ ] Every Rule has a distinct user role and benefit
- [ ] No Rule duplicates another
- [ ] Rules collectively cover all entities in scope from the feature description
- [ ] Every Rule passes the INVEST gate

Commit: `feat(stories): write user stories for <name>`

### Step B — Criteria

Add `Example:` blocks under each `Rule:`. PO writes all Examples alone, based on the approved feature description and domain knowledge. No stakeholder review of individual Examples.

**Silent pre-mortem per Rule** (before writing any Examples):

> "What observable behaviors must we prove for this Rule to be complete?"

All Rules must have their pre-mortems completed before any Examples are written.

**Example format** (mandatory):

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

**Review checklist:**
- [ ] Every `Rule:` block has at least one Example
- [ ] Every `@id` is unique within this feature
- [ ] Every Example has `Given/When/Then`
- [ ] Every `Then` is a single, observable, measurable outcome
- [ ] No Example tests implementation details
- [ ] If user interaction is involved, the interaction model is declared in the Feature description
- [ ] Each Example is observably distinct from every other
- [ ] No single feature file spans multiple unrelated concerns

**Self-Declaration (mandatory before criteria commit)**

Communicate verbally to the next agent. Every `DISAGREE` is a **hard blocker** — fix before committing. Do not commit until all items are AGREE or have a documented resolution.

- INVEST-I: each Rule is Independent (no hidden ordering or dependency between Rules) — AGREE/DISAGREE | conflict:
- INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE | Rule:
- INVEST-S: each Rule is Small enough for one development cycle — AGREE/DISAGREE | Rule:
- INVEST-T: each Rule is Testable (I can write a pass/fail Example for it) — AGREE/DISAGREE | Rule:
- Observable: every Then is a single, observable, measurable outcome — AGREE/DISAGREE | file:line
- No impl details: no Example tests internal state or implementation — AGREE/DISAGREE | file:line
- Coverage: every entity in the feature description appears in at least one Rule — AGREE/DISAGREE | missing:
- Distinct: no two Examples test the same observable behavior — AGREE/DISAGREE | file:line
- Unique IDs: all @id values are unique within this feature — AGREE/DISAGREE
- Pre-mortem: I ran a pre-mortem on each Rule and found no hidden failure modes — AGREE/DISAGREE | Rule:
- Scope: no Example introduces behavior outside the feature boundary — AGREE/DISAGREE | file:line

Commit: `feat(criteria): write acceptance criteria for <name>`

**After this commit, `Example:` blocks are frozen.** Any change requires:
1. Add `@deprecated` tag to the old Example
2. Write a new Example with a new `@id`

---

## Bug Handling

When a defect is reported against a completed or in-progress feature:

1. **PO** adds a new Example to the relevant `Rule:` block in the `.feature` file:

   ```gherkin
   @bug @id:<new-8-char-hex>
   Example: <what the bug is>
     Given <conditions that trigger the bug>
     When <action>
     Then <correct behavior>
   ```

2. **SE** implements the specific test in `tests/features/<feature-name>/` (the `@id` test).
3. **SE** also writes a `@given` Hypothesis property test in `tests/unit/` covering the whole class of inputs that triggered the bug — not just the single case.
4. Both tests are required — neither is optional.
5. SE follows the normal TDD loop (Step 3) for the new `@id`.

---

## Feature File Format

Each feature is a single `.feature` file. The description block contains the feature description and Status. All Q&A belongs in `docs/discovery_journal.md`; all architectural decisions belong in `docs/architecture.md`.

```gherkin
Feature: <Feature title>

  <2–4 sentence description of what this feature does and why it exists.
  Written in plain language, always kept current by the PO.>

  Status: ELICITING | BASELINED (YYYY-MM-DD)

  Rules (Business):
  - <Business rule that applies across multiple Examples>

  Constraints:
  - <Non-functional requirement specific to this feature>

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

What is **not** in `.feature` files:
- Entities table — domain model lives in `docs/discovery.md`
- Session Q&A blocks — live in `docs/discovery_journal.md`
- Template §N markers — live in `docs/discovery_journal.md` session blocks
- Architecture section — lives in `docs/architecture.md`

---

## Project-Level Discovery Templates

Three files hold project-level discovery content. Use these templates when creating them for the first time.

### `docs/discovery_journal.md` — Raw Q&A (append-only)

```markdown
# Discovery Journal: <project-name>

---

## YYYY-MM-DD — Session 1
Status: IN-PROGRESS

### General

| ID | Question | Answer |
|----|----------|--------|
| Q1 | Who are the users? | ... |
| Q2 | What does the product do at a high level? | ... |
| Q3 | Why does it exist — what problem does it solve? | ... |
| Q4 | When and where is it used? | ... |
| Q5 | Success — what does "done" look like? | ... |
| Q6 | Failure — what must never happen? | ... |
| Q7 | Out-of-scope — what are we explicitly not building? | ... |

### <Group Name>

| ID | Question | Answer |
|----|----------|--------|
| Q8 | ... | ... |

### Feature: <feature-name>

| ID | Question | Answer |
|----|----------|--------|
| Q9 | ... | ... |

Status: COMPLETE
```

Rules:
- Session header written first with `Status: IN-PROGRESS` before any Q&A
- Only answered questions are written; unanswered questions are discarded
- Questions grouped by topic (general, cross-cutting groups, per-feature)
- `Status: COMPLETE` written at the end of the session block, after all writes are done
- Never edit past entries — only append new session blocks

### `docs/discovery.md` — Synthesis Changelog (append-only)

```markdown
# Discovery: <project-name>

---

## Session: YYYY-MM-DD

### Scope
<3–5 sentence synthesis of who the users are, what the product does, why it exists,
success/failure conditions, and out-of-scope boundaries.>
(First session only. Omit this subsection in subsequent sessions.)

### Feature List
- `<feature-name>` — <one-sentence description of what changed or was added>
(Write "No changes" if no features were added or modified this session.)

### Domain Model
| Type | Name | Description | In Scope |
|------|------|-------------|----------|
| Noun | <name> | <description> | Yes |
| Verb | <name> | <description> | Yes |
(Write "No changes" if domain model was not updated this session.)
```

Rules:
- Each session appends one `## Session: YYYY-MM-DD` block
- Synthesis block is written LAST — only after all `.feature` file descriptions are updated
- No project-level `Status: BASELINED` — feature-level BASELINED in `.feature` files is the gate
- Never edit past blocks — append only; later blocks extend or supersede earlier ones

### `docs/architecture.md` — Architectural Decisions (append-only, software-engineer)

```markdown
# Architecture: <project-name>

---

## YYYY-MM-DD — <feature-name>: <short title>

Decision: <what was decided — one sentence>
Reason: <why — one sentence>
Alternatives considered: <what was rejected and why>
Feature: <feature-name>
```

Rules: Append-only. When a decision changes, append a new block that supersedes the old one. Cross-feature decisions use `Cross-feature:` in the header. Only write a block for non-obvious decisions with meaningful trade-offs.

Base directory for this skill: file:///home/user/Documents/projects/python-project-template/.opencode/skills/scope
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>/home/user/Documents/projects/python-project-template/.opencode/skills/scope/discovery-template.md</file>
</skill_files>
