---
name: scope
description: Step 1 — define user stories, acceptance criteria with UUID traceability, and test strategy
version: "1.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Scope

This skill guides the product owner through Step 1 of the feature lifecycle: defining what to build with enough precision that a developer can write tests without asking questions.

## When to Use

When the PO is starting a new feature. The output is a feature document in `docs/features/backlog/`.

## Step-by-Step

### 1. Create the Feature Document

Create `docs/features/backlog/<feature-name>.md`. Use kebab-case for the filename.

```markdown
# Feature: <Name>

## User Stories
- As a <role>, I want <goal> so that <benefit>

## Acceptance Criteria

- `<uuid>`: <Short description>.
  Given: <precondition>
  When: <action>
  Then: <expected outcome>
  Test strategy: unit | integration

## Notes
<constraints, risks, out-of-scope items, dependencies>
```

### 2. Write User Stories

Each story follows the format: "As a `<role>`, I want `<goal>` so that `<benefit>`."

Good stories are:
- **Independent**: can be delivered without other stories
- **Negotiable**: details can be discussed
- **Valuable**: delivers something the user cares about
- **Estimable**: the developer can estimate effort
- **Small**: completable in one feature cycle
- **Testable**: can be verified with a concrete test

Avoid: "As the system, I want..." (no business value). Break down stories that contain "and" into two stories.

### 3. Write Acceptance Criteria

Each criterion maps directly to one test. Write as many as needed — one per observable behavior.

**UUID generation**:
```bash
python -c "import uuid; print(uuid.uuid4())"
```

**Format** (mandatory — exactly this structure):
```markdown
- `a1b2c3d4-e5f6-7890-abcd-ef1234567890`: Ball bounces off top wall.
  Given: A ball moving upward reaches y=0
  When: The physics engine processes the next frame
  Then: The ball velocity y-component becomes positive
  Test strategy: unit
```

**Rules**:
- UUID must be unique across the entire project, not just this feature
- First line: UUID + colon + short description ending with a period
- Given/When/Then on separate indented lines
- Test strategy is `unit` (isolated) or `integration` (multiple components)
- Use plain English, not technical jargon in Given/When/Then
- "Then" must be a single observable, measurable outcome — no "and"

**Common mistakes to avoid**:
- "Then: It works correctly" (not measurable)
- "Then: The system updates the database and sends an email" (split into two criteria)
- Multiple behaviors in one criterion (split them)
- Criteria that test implementation details ("Then: the Strategy pattern is used")

### 4. Identify Test Strategy Per Criterion

For each criterion, decide:

| Strategy | Use When |
|---|---|
| `unit` | One function or class in isolation; no external dependencies |
| `integration` | Multiple components working together; external state (DB, filesystem, network) |

When in doubt, start with `unit`. The developer may upgrade to `integration` if the implementation requires it.

### 5. Review Checklist

Before committing:
- [ ] Every user story has at least one acceptance criterion
- [ ] Every UUID is unique (check existing feature docs)
- [ ] Every criterion has Given/When/Then and a test strategy
- [ ] "Then" is a single, observable, measurable outcome
- [ ] No criterion tests implementation details
- [ ] Out-of-scope items are explicitly listed in Notes

### 6. Commit and Notify Developer

```bash
git add docs/features/backlog/<feature-name>.md
git commit -m "feat(scope): define <feature-name> acceptance criteria"
```

Then move the feature to in-progress when ready to start:
```bash
mv docs/features/backlog/<feature-name>.md docs/features/in-progress/<feature-name>.md
git add -A
git commit -m "chore(workflow): start <feature-name>"
```

Update TODO.md to reflect the new current feature.

## MoSCoW Prioritization

When ordering multiple features in the backlog, use:
- **Must**: required for the product to work
- **Should**: high value, strong business case
- **Could**: nice to have, low risk to defer
- **Won't**: explicitly out of scope for now

Add a `Priority: Must | Should | Could | Won't` line to each feature doc's Notes section.
