---
name: scope
description: Step 1 — define user stories and acceptance criteria with UUID traceability
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

Create `docs/features/backlog/<verb>-<object>.md`. Filename must be kebab-case, imperative verb first, 2–4 words.
Examples: `display-version.md`, `authenticate-user.md`, `export-metrics-csv.md`

```markdown
# Feature: <Verb> <Object>

## User Stories
- As a <role>, I want <goal> so that <benefit>

## Acceptance Criteria

- `<uuid>`: <Short description>.
  Source: <stakeholder | po | developer | reviewer | bug>

  Given: <precondition>
  When: <action>
  Then: <expected outcome>

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
  Source: stakeholder

  Given: A ball moving upward reaches y=0
  When: The physics engine processes the next frame
  Then: The ball velocity y-component becomes positive
```

**Source values** (choose exactly one):
- `stakeholder` — an external stakeholder gave this requirement to the PO
- `po` — the PO originated this criterion independently
- `developer` — a gap found during Step 4 implementation
- `reviewer` — a gap found during Step 5 verification
- `bug` — a post-merge regression; the feature doc was reopened

**Rules**:
- UUID must be unique across the entire project, not just this feature
- First line: UUID + colon + short description ending with a period
- `Source:` on the next line, followed by a blank line, then Given/When/Then
- Use plain English, not technical jargon in Given/When/Then
- "Then" must be a single observable, measurable outcome — no "and"

**Common mistakes to avoid**:
- "Then: It works correctly" (not measurable)
- "Then: The system updates the database and sends an email" (split into two criteria)
- Multiple behaviors in one criterion (split them)
- Criteria that test implementation details ("Then: the Strategy pattern is used")

### 4. Review Checklist

Before committing:
- [ ] Filename is `<verb>-<object>.md`, imperative verb first, 2–4 words
- [ ] Title matches filename: `# Feature: <Verb> <Object>` in Title Case
- [ ] Every user story has at least one acceptance criterion
- [ ] Every UUID is unique (check existing feature docs)
- [ ] Every criterion has a `Source:` field with one of the five valid values
- [ ] Every criterion has Given/When/Then
- [ ] Blank line between `Source:` and `Given:`
- [ ] "Then" is a single, observable, measurable outcome
- [ ] No criterion tests implementation details
- [ ] Out-of-scope items are explicitly listed in Notes

### 5. Commit and Notify Developer

```bash
git add docs/features/backlog/<feature-name>.md
git commit -m "feat(scope): define <feature-name> acceptance criteria"
```

The developer moves the feature from `backlog/` to `in-progress/` as the first act of Step 2.

## MoSCoW Prioritization

When ordering multiple features in the backlog, use:
- **Must**: required for the product to work
- **Should**: high value, strong business case
- **Could**: nice to have, low risk to defer
- **Won't**: explicitly out of scope for now

Add a `Priority: Must | Should | Could | Won't` line to each feature doc's Notes section.
