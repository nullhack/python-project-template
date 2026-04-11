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

## Epic Structure

Epics are tracked in `EPICS.md` with this format:

```markdown
# Project Epics

## Epic: [Epic Name]
**Status**: In Progress | Complete
**Business Value**: [Why this epic matters]

### Features:
1. **[Feature Name]** - Status: Complete ✅
   - Acceptance Criteria: [What defines done]
   - QA Status: Approved by @overseer on YYYY-MM-DD
   
2. **[Feature Name]** - Status: In Progress 🔄
   - Acceptance Criteria: [What defines done]
   - QA Status: Pending
   
3. **[Feature Name]** - Status: Pending ⏸️
   - Acceptance Criteria: [What defines done]
   - QA Status: Not Started
```

## Feature Development Cycle

### 1. Feature Initiation
When starting a new feature:
```
1. Read EPICS.md to find next pending feature
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
1. Update feature status to "Complete ✅"
2. Record QA approval date and agent
3. Automatically identify next pending feature
4. Start new feature cycle or close epic
```

## Automatic Feature Progression

After completing a feature:
1. The system checks for next pending feature in the epic
2. If found, automatically initiates the new feature cycle
3. If no pending features, marks epic as complete
4. Suggests next epic from backlog

## QA Enforcement Protocol

**Mandatory QA checkpoints cannot be skipped:**
- After requirements gathering
- After TDD phase
- After implementation
- Before marking feature complete

If @overseer requests changes:
- Development cannot proceed until issues resolved
- Changes must be re-reviewed
- QA status tracked in EPICS.md

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