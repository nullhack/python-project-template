---
name: epic-workflow
description: Manage epic-based development with features, QA checkpoints, and automatic progression to next features
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: epic-management
---
## What I do

I enable epic-based development where each epic contains multiple features. After completing a feature and passing QA, I automatically progress to the next feature in the epic. This creates a continuous development flow with quality checkpoints.

## Key Concepts

- **Epic**: A major capability containing multiple related features
- **Feature**: A single implementable unit with clear acceptance criteria
- **QA Checkpoint**: Mandatory review by the overseer agent after each phase
- **Feature Cycle**: Requirements → TDD → Implementation → QA → Next Feature

## When to use me

- When starting a new epic with multiple features
- When completing a feature and ready to move to the next
- When tracking progress across complex multi-feature development
- When ensuring QA gates are enforced at each checkpoint

## Feature Tracking

Features are tracked in `docs/roadmap.md` (architect breakdown) and `docs/features/backlog/` (business definitions):

```markdown
# docs/roadmap.md

## Feature: [Feature Name]
**Status**: In Progress | Complete
**Business Value**: [Why this feature matters]

### Technical Breakdown
- [Deliverable 1]
- [Deliverable 2]

# docs/features/backlog/<feature>.md

## Feature: [Feature Name]
**Business Description**: [What it does]
**Acceptance Criteria**: [What defines done]
```

## Feature Development Cycle

### 1. Feature Initiation
When starting a new feature:
```
1. Read docs/roadmap.md to find next pending feature
2. Call @requirements-gatherer if feature needs clarification
3. Update feature status to "In Progress 🔄"
4. Create feature-specific TODO in TODO.md
```

### 2. Feature Implementation Phases

Each feature follows these mandatory phases with QA checkpoints:

```
Phase 1: Requirements Analysis
- @requirements-gatherer collects detailed requirements
- Creates feature analysis document
- @architect reviews and approves design
- QA Checkpoint: @overseer reviews requirements completeness

Phase 2: Test-Driven Development
- @developer /skill tdd
- Write comprehensive tests
- QA Checkpoint: @overseer reviews test quality

Phase 3: Implementation
- @developer /skill implementation
- Implement to pass tests
- QA Checkpoint: @overseer reviews SOLID/DRY/KISS compliance

Phase 4: Final Quality Assurance
- @developer /skill code-quality
- All quality checks must pass
- QA Checkpoint: @overseer final approval
```

### 3. Feature Completion
```
1. Verify all TODO items complete
2. Overseer reviews and approves final QA
3. @overseer moves feature to docs/features/completed/ with metadata:
   - Test coverage (which UUIDs have tests)
   - QA approval date
   - Links to test files
4. Clear TODO.md for next feature
```

## Automatic Feature Progression

After completing a feature:
1. The system checks for next pending feature in roadmap
2. If found, automatically initiates the new feature cycle
3. If no pending features, all features are complete
4. Suggests next feature from docs/features/backlog/

## QA Enforcement Protocol

**Mandatory QA checkpoints cannot be skipped:**
- After requirements gathering
- After TDD phase
- After implementation
- Before marking feature complete

If @overseer requests changes:
- Development cannot proceed until issues resolved
- Changes must be re-reviewed
- QA status tracked in TODO.md session log

## Integration with TODO.md

TODO.md tracks current feature work:
```markdown
## Current Epic: [Epic Name]
## Current Feature: [Feature Name]

### Phase 1: Requirements Analysis
- [x] Requirements gathered
- [x] Analysis document created
- [x] Architect approval received
- [x] QA: Approved by @overseer

### Phase 2: Test Development
- [ ] TDD tests written
- [ ] QA: Pending @overseer review
```

## Commands

### Start new epic
```
@developer /skill epic-workflow start-epic "User Authentication"
```

### Progress to next feature
```
@developer /skill epic-workflow next-feature
```

### Check epic status
```
@developer /skill epic-workflow status
```

## Example Workflow

```bash
# 1. Start epic
@developer /skill epic-workflow start-epic "Payment Processing"

# 2. First feature begins automatically
@requirements-gatherer  # Gather requirements for Feature 1
@architect             # Review design
@developer /skill tdd  # Write tests
@overseer             # QA checkpoint - test review
@developer /skill implementation
@overseer             # QA checkpoint - code review
@developer /skill code-quality
@overseer             # Final QA approval

# 3. System automatically starts Feature 2
@requirements-gatherer  # Next feature begins...
```

This creates a continuous, quality-assured development flow that automatically progresses through all features in an epic.