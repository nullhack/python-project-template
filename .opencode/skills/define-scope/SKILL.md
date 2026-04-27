---
name: define-scope
description: Step 1 — discover requirements through stakeholder interviews and write Gherkin acceptance criteria
version: "6.0"
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
| **Stage 1 — Discovery** | PO + stakeholder | `docs/scope_journal.md` (Q&A) + `.feature` descriptions (with `## Changes` sections) |
| **Stage 2 — Specification** | PO alone | `Rule:` blocks + `Example:` blocks with `@id` tags in `.feature` files |

Stage 1 is iterative and ongoing — sessions happen whenever the PO or stakeholder needs to discover or refine scope. Stage 2 runs per feature, only after that feature has `Status: BASELINED`.

---

## Gap-Finding Techniques

See [[requirements/discovery-techniques]] for CIT, Laddering, and CI Perspective Change techniques. Apply these during every interview session to surface what stakeholders have not yet said.

---

## Active Listening Protocol

See [[requirements/discovery-techniques]] for the three levels of active listening (per answer, per group, end of session). Apply throughout every interview session. Do not introduce topic labels or categories during active listening — the summary must reflect what the stakeholder said.

---

## Stage 1 — Discovery

Discovery is a continuous, iterative process. Sessions happen whenever scope needs to be established or refined — for a new project, for a new feature, or when new information emerges. There is no "Phase 1" vs "Phase 2" distinction; every session follows the same structure.

### Session Start (every session)

**Required reads** (before asking any questions):

| Read | Why |
|---|---|
| `docs/scope_journal.md` | Resume check — was the previous session interrupted? |
| `docs/system.md` § Domain Model | Check existing entities (read-only; SA-owned) |
| `.feature` files (`## Changes` sections) | Consistency check — past session changes |
| `docs/glossary.md` | Anchor interview language in existing domain terms |
| `docs/branding.md` | Align tone and wording with project identity |

**Before asking any questions:**

1. Check `docs/scope_journal.md` for the most recent session block.
   - If the most recent block has `Status: IN-PROGRESS` → the previous session was interrupted. Resume it: check which `.feature` files need updating (compare journal Q&A against current `.feature` descriptions), write the `## Changes` rows if missing, then mark the block `Status: COMPLETE`. Only then begin a new session.
   - If `docs/scope_journal.md` does not exist → this is the first session. Create `docs/scope_journal.md` using the template in `scope-journal.md.template` in this skill's directory.
2. Read the `## Domain Model` section of `docs/system.md` (if the file exists) to check existing entities. The PO reads this section but never writes to `system.md` — it is SA-owned. If `system.md` does not yet have a Domain Model section, the SA will add it at Step 2.
3. Declare session scope to the stakeholder: announce the total groups and estimated question count (e.g., "3 groups: General (7 Q), Cross-cutting, Feature: login").
4. Open `docs/scope_journal.md` and append a new session header:
   ```markdown
   ## YYYY-MM-DD — Session N
   Status: IN-PROGRESS
   ```
    Write this header **before** asking any questions. This is the durability marker — if the session is interrupted, the next agent sees `IN-PROGRESS` and knows writes are pending.

### Interview Protocol

**Progress declaration (first message):**
State the session structure upfront:
> "This discovery session has 3 question groups:
> 1. General (7 questions) — about users, goals, success/failure
> 2. Cross-cutting — about behaviour groups, integrations, lifecycle events
> 3. Feature: <name> — about specific functionality
>
> I will ask one group at a time and summarise before moving on."

**Question grouping:**
- One `question` tool call per question group
- Each question within the group uses a clear `header` showing progress, e.g.:
  - `General — Q1/7`
  - `General — Q2/7`
  - `Feature: login — Q3/5`

**Input types:**
- **Checkbox (`multiple: true`)**: for multi-select answers (e.g., "Which platforms?" "Which user roles?")
- **Options**: for single-select with known choices (e.g., "Priority: High / Medium / Low")
- **Fill-up field (free text)**: for open-ended responses that cannot be pre-listed

**Defaults:**
- Offer "Other" or pre-fill with most common answer when context permits
- Never force a stakeholder into a false dichotomy; always include "Something else / Not sure"

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

Apply Level 1 active listening per answer. Apply gap-finding techniques (see [[requirements/discovery-techniques]]) per answer to surface gaps. Add new questions in the moment.

**2. Cross-cutting questions**

Target behaviour groups, bounded contexts, integration points, lifecycle events, and system-wide constraints. Apply Level 2 active listening when transitioning between groups.

**3. Feature questions** (one feature at a time)

For each feature the session touches:
- Extract relevant nouns and verbs from `docs/glossary.md` and the `## Domain Model` section of `docs/system.md` (if it exists)
- Generate questions from entity gaps: boundaries, edge cases, interactions, failure modes
- Run a silent pre-mortem: "Imagine the developer builds this feature exactly as described, all tests pass, but the feature doesn't work for the user. What would be missing?"
- Apply gap-finding techniques (see [[requirements/discovery-techniques]]) per question

**Real-time split rule**: if, during feature questions, the PO detects >2 distinct concerns OR >8 candidate Examples for a single feature, **split immediately**:
1. Record the split in the journal: note the original feature name and the two new names
2. Create stub `.feature` files for both parts (if they don't already exist)
3. Continue feature questions for both new features in sequence within the same session

### Write Confirmation Gate

**Before writing ANY file:** `docs/scope_journal.md` or `.feature` files.

1. State exactly what will be written:
   > "I will now append the Q&A from this session to `docs/scope_journal.md`."

2. State exactly which file(s):
   > "I will create `docs/features/backlog/<feature-stem>.feature`."

3. **Ask for explicit confirmation** using the `question` tool:
   - `header: "Ready to write"`
   - Question text: "Confirm: write to `<path>`?"
   - Options: `["Yes, write it", "Show me a preview first", "No, I need changes"]`

4. Only proceed with `write`/`edit` if the answer is confirmation.

**This applies to all write operations in this skill**, including:
- `docs/scope_journal.md` (session header and Q&A)
- `docs/features/backlog/<feature-stem>.feature` (initial description or update)

### After Questions (PO alone, same session)

**Step A — Write answered Q&A to journal**

Append all answered Q&A to `docs/scope_journal.md`, in groups (general, cross-cutting, then per-feature). Write only answered questions. Unanswered questions are discarded.

Group headers use this format:
- General group: `### General`
- Cross-cutting group: `### <Group Name>`
- Feature group: `### Feature: <feature-stem>`

**Step B — Update glossary and .feature Changes**

1. Update `docs/glossary.md` **after** the session closes — batch update, not real-time during the interview. Read `glossary.md` before the session starts to anchor interview language; update it after all Q&A is complete. New or corrected definitions; edits allowed.
2. For each `.feature` file created or updated this session, append a row to its `## Changes` section:
   - **Session**: `YYYY-MM-DD SN` (e.g., `2026-04-22 S1`)
   - **Q-IDs**: journal question IDs that drove the change (e.g., `Q8, Q9, Q11`)
   - **Change**: concise summary of what changed (e.g., `Created: CLI entrypoint with --help, --version, unknown-flag handling`)
   - If the `.feature` file has no `## Changes` section yet, add one at the bottom before appending rows.
   - **Confirmations (no file change) → no row.**

The PO does **not** write `docs/system.md`. Entity and domain model updates are SA-owned and happen at Step 2.

**Step C — Update .feature descriptions**

For each feature touched in this session: rewrite the `.feature` file description to reflect the current state of understanding. Only touched features are updated; all others remain exactly as-is.

If a feature is new (just created as a stub): write its initial description now. Use the template in `feature.md.template`.

**Step D — Completed feature regression check**

If a `completed/` feature was touched and its description/rules changed:
- **Move it to `backlog/`**. Description changes always imply behaviour changes; cosmetic rewrites are never performed.
- Record the move in the `.feature` file's `## Changes` section: "Moved from completed to backlog due to changed requirements."

**Step E — Mark session complete**

Update the session header in `docs/scope_journal.md`:
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

**Required reads**:

| Read | Why |
|---|---|
| In-progress `.feature` file | The baselined description is the sole input for user stories |

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

See [[requirements/invest-moscow]] for INVEST criteria and characteristics of well-formed stories. Every Rule must pass all six INVEST letters before committing. Avoid "As the system, I want..." (no business value). Break down stories that contain "and" into two Rules.

**Review checklist:**
- [ ] Every Rule has a distinct user role and benefit
- [ ] No Rule duplicates another
- [ ] Rules collectively cover all entities in scope from the feature description
- [ ] Every Rule passes the INVEST gate (see [[requirements/invest-moscow#key-takeaways]])

Commit: `feat(stories): write user stories for <feature-stem>`

### Step B — Criteria

**Required reads**:

| Read | Why |
|---|---|
| In-progress `.feature` file | Rules and feature description are the sole input for Examples |

Add `Example:` blocks under each `Rule:`. PO writes all Examples alone, based on the approved feature description and domain knowledge. No stakeholder review of individual Examples.

**Silent pre-mortem per Rule** (before writing any Examples):

> "What observable behaviours must we prove for this Rule to be complete?"

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
- `Example:` keyword (not `Scenario:`)
- `Given/When/Then` in plain English
- `Then` must be a single, observable, measurable outcome — no "and"
- **Observable means observable by the end user**, not by a test harness
- **Declarative, not imperative** — describe behaviour, not UI steps (see [[requirements/gherkin#concepts]] for the declarative vs imperative comparison)
- Each Example must be observably distinct from every other

See [[requirements/invest-moscow#concepts]] for MoSCoW triage. Classify each candidate Example as Must, Should, or Could. If Musts alone exceed 8 or the Rule spans >2 concerns, split the Rule.

See [[requirements/gherkin]] for common mistakes to avoid when writing Examples.

**Review checklist:**
- [ ] Every `Rule:` block has at least one Example
- [ ] Every Example has `Given/When/Then`
- [ ] Every `Then` is a single, observable, measurable outcome
- [ ] No Example tests implementation details
- [ ] If user interaction is involved, the interaction model is declared in the Feature description
- [ ] Each Example is observably distinct from every other
- [ ] No single feature file spans multiple unrelated concerns

**Self-Declaration (mandatory before criteria commit)**

Communicate verbally to the next agent. Every `DISAGREE` is a **hard blocker** — fix before committing. Do not commit until all items are AGREE or have a documented resolution.

As a product-owner I declare that:
* INVEST-I: each Rule is Independent (no hidden ordering or dependency between Rules) — AGREE/DISAGREE | conflict:
* INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE | Rule:
* INVEST-S: each Rule is Small enough for one development cycle — AGREE/DISAGREE | Rule:
* INVEST-T: each Rule is Testable (I can write a pass/fail Example for it) — AGREE/DISAGREE | Rule:
* Observable: every Then is a single, observable, measurable outcome — AGREE/DISAGREE | file:line
* No impl details: no Example tests internal state or implementation — AGREE/DISAGREE | file:line
* Coverage: every entity in the feature description appears in at least one Rule — AGREE/DISAGREE | missing:
* Distinct: no two Examples test the same observable behaviour — AGREE/DISAGREE | file:line
* Pre-mortem: I ran a pre-mortem on each Rule and found no hidden failure modes — AGREE/DISAGREE | Rule:
* Scope: no Example introduces behaviour outside the feature boundary — AGREE/DISAGREE | file:line

### Step C — Assign @id tags

Run `uv run task assign-ids`. This auto-generates unique `@id:XXXXXXXX` tags (8-char hex) for any untagged `Example:` blocks across all `.feature` files, then verifies that all IDs are globally unique. Exit code 0 = success.

Only commit if `assign-ids` passes. If it reports errors, fix the `.feature` files and re-run.

Commit: `feat(criteria): write acceptance criteria for <feature-stem>`

**After this commit, `Example:` blocks are frozen.** Any change requires:
1. Add `@deprecated` tag to the old Example
2. Write a new Example and run `uv run task assign-ids` to assign its `@id` tag

---

## Bug Handling

When a defect is reported against a completed or in-progress feature:

1. **PO** adds a new Example to the relevant `Rule:` block in the `.feature` file:

   ```gherkin
   @bug
   Example: <what the bug is>
     Given <conditions that trigger the bug>
     When <action>
     Then <correct behaviour>
   ```

2. **SE** implements the specific test in `tests/features/<feature_slug>/` (the `@id` test).
3. **SE** also writes a `@given` Hypothesis property test in `tests/unit/` covering the whole class of inputs that triggered the bug — not just the single case.
4. Both tests are required — neither is optional.
5. SE follows the normal TDD loop (Step 3) for the new `@id`.

---

## Feature File Format

Each feature is a single `.feature` file. The description block contains the feature description and Status. All Q&A belongs in `docs/scope_journal.md`; all architectural decisions belong in `docs/adr/ADR-YYYY-MM-DD-<slug>.md`.

See `feature.md.template` in this skill's directory for the full template.

The **Rules (Business)** section captures business rules that hold across multiple Examples. Identifying rules first prevents redundant or contradictory Examples.

The **Constraints** section captures non-functional requirements. Testable constraints should become `Example:` blocks with `@id` tags.

What is **not** in `.feature` files:
- Domain model or entities — domain model lives in the `## Domain Model` section of `docs/system.md` (SA-owned)
- Session Q&A blocks — live in `docs/scope_journal.md`
- Architecture section — lives in `docs/adr/ADR-*.md`

---

## Post-Mortem Protocol

When a stakeholder reports failure after the PO has attempted Step 5 acceptance, the feature does **not** move to `completed/`. Instead, the team compiles a compact post-mortem and the feature restarts at Step 2.

### Trigger
Stakeholder reports a feature is wrong after PO acceptance attempt.

### Workflow
1. **PO ensures feature is in `in-progress/`** (move back if already shifted).
2. **Team compiles post-mortem** — max 15 lines, root cause at process level.
3. **SE creates fix branch** from the feature's original start commit:
   ```bash
   # Find the feature's original start commit
   git log --all --grep="feat(<feature-stem>)" --oneline
   # Or, if the old branch still exists:
   git log --reverse main..feat/<feature-stem> --oneline   # first line = start commit
   
   # Create fix branch from start commit
   git checkout -b fix/<feature-stem> <start-commit-sha>
   
   # Commit post-mortem as first commit on the new branch
   git add docs/post-mortem/YYYY-MM-DD-<feature-stem>-<keyword>.md
   git commit -m "docs(post-mortem): root cause for <feature-stem> <keyword>"
   
   # Push the fix branch
   git push -u origin fix/<feature-stem>
   ```
4. **PO scans `docs/post-mortem/`**, selects relevant files by `<feature-stem>` or `<failure-keyword>` in filename.
5. **PO reads selected post-mortems** for context before handoff.
6. **PO updates the session file in `.flowr/sessions/`**: set `state: step-2-arch` (enters arch-cycle subflow), `branch: fix/<feature-stem>`.
7. **SA begins Step 2** (arch-cycle subflow) on `fix/<feature-stem>`, reading relevant post-mortems as input.

### Document Format

File: `docs/post-mortem/YYYY-MM-DD-<feature-stem>-<failure-keyword>.md`

Use the template `post-mortem.md.template` in this skill's directory.

### Rules
- One file per incident. Never edit an existing post-mortem.
- If the same failure mode recurs, write a new post-mortem referencing the old one by filename.
- PO reads post-mortems selectively; never require reading all of them.

---

## Templates

All templates for files written by this skill live in this skill's directory:

- `scope-journal.md.template` — `docs/scope_journal.md` structure
- `feature.md.template` — `.feature` file structure
- `post-mortem.md.template` — `docs/post-mortem/YYYY-MM-DD-<feature-stem>-<keyword>.md` structure
- `glossary.md.template` — `docs/glossary.md` initial file (pre-filled with common jargon; PO appends project-specific entries)

Base directory for this skill: `.opencode/skills/define-scope/`
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>.opencode/skills/define-scope/feature.md.template</file>
<file>.opencode/skills/define-scope/scope-journal.md.template</file>
</skill_files>