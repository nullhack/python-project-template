---
name: epic-workflow
description: Select and manage features from architecture and business backlogs with architecture-first prioritization
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-selection
---
## What I do

I manage feature selection and progression using an architecture-first approach. I select features from either `docs/features/architecture/backlog/` or `docs/features/business/backlog/`, prioritizing architecture features for unit/smoke test development.

## Key Concepts

- **Architecture Features**: Technical requirements that drive unit and smoke tests
- **Business Features**: User-facing requirements that drive integration and system tests  
- **Feature → TODO**: Direct selection of features for immediate development
- **Architecture-First**: Priority selection from architecture backlog for foundational testing
- **Independent Lifecycle**: Architecture and business features complete separately

## When to use me

- When selecting the next feature for development
- When completing a feature and ready to move to the next
- When managing feature progression through backlog → completed
- When ensuring architecture-driven development approach

## Feature Selection Strategy

### Priority Order
1. **First Priority**: `docs/features/architecture/backlog/` (technical features)
2. **Second Priority**: `docs/features/business/backlog/` (business features)

### Rationale
- **Architecture features** → unit tests, smoke tests (foundational)
- **Business features** → integration tests, system tests (require foundation)

## Feature Directory Structure

```
docs/features/
├── architecture/
│   ├── backlog/           # Technical features awaiting development
│   │   └── <feature-name>/
│   │       └── architecture-feature.md
│   └── completed/         # Technical features delivered
│       └── <feature-name>/
└── business/
    ├── backlog/           # Business features awaiting development  
    │   └── <feature-name>/
    │       └── business-feature.md
    └── completed/         # Business features delivered
        └── <feature-name>/
```

## Feature Selection Commands

### `next-feature` - Select Next Feature for Development
Selects the next feature using architecture-first priority:

```bash
@developer /skill epic-workflow next-feature
```

**Selection Logic:**
1. Check `docs/features/architecture/backlog/` for available features
2. If architecture features exist: Select first architecture feature
3. If no architecture features: Check `docs/features/business/backlog/`
4. If business features exist: Select first business feature
5. If no features exist: Prompt for feature creation

**Output:**
- Updates TODO.md with selected feature
- Creates 8-phase development plan
- Provides feature summary and acceptance criteria

### `complete-feature` - Move Feature to Completed
Moves current feature from backlog to completed:

```bash
@developer /skill epic-workflow complete-feature
```

**Completion Logic:**
- Moves feature from `backlog/` to `completed/` in appropriate directory
- Updates TODO.md status
- Clears current feature from active development
- Ready for next feature selection

### `status` - Show Feature Pipeline Status
Displays current feature pipeline:

```bash
@developer /skill epic-workflow status
```

**Output:**
- Current feature in development (from TODO.md)
- Available architecture features count
- Available business features count
- Recently completed features

## Integration with 8-Phase Workflow

Feature selection integrates with the 8-phase development cycle:

### Feature Selection → TODO Creation
```
1. Feature selected (architecture-first priority)
2. TODO.md updated with:
   - Phase 1: Requirements Review
   - Phase 2: Feature Definition  
   - Phase 3: Architecture Analysis
   - Phase 4: Test Development (TDD)
   - Phase 5: Design & Signatures
   - Phase 6: Implementation
   - Phase 7: Final Quality Assurance
   - Phase 8: Feature Completion
3. @manager creates test signatures from feature acceptance criteria
4. @developer implements through phases
```

### Feature Completion → Next Selection
```
1. All 8 phases completed with @overseer approvals
2. Feature moved from backlog/ to completed/
3. TODO.md cleared for next feature
4. Automatic progression to next feature selection
```

## Feature Types and Testing Strategy

### Architecture Features
**Content**: Technical specifications, component designs, ADRs
**Test Focus**: Unit tests, smoke tests, component integration
**Example**: "JWT Token Management System", "Database Connection Pool"

### Business Features  
**Content**: User stories, business requirements, workflows
**Test Focus**: Integration tests, system tests, end-to-end scenarios
**Example**: "User Authentication", "Product Search"

## Example Workflow

### Starting Development
```bash
# Select next feature (architecture-first)
@developer /skill epic-workflow next-feature

# Result: Architecture feature selected
# TODO.md updated with 8-phase plan
# @manager creates test signatures
# Development begins with Phase 1
```

### Completing Development
```bash
# After all 8 phases complete
@developer /skill epic-workflow complete-feature

# Result: Feature moved to completed/
# TODO.md cleared
# Ready for next feature selection
```

### Checking Status
```bash
@developer /skill epic-workflow status

# Result: Pipeline overview
# - Current: JWT Token Management (Phase 4/8)
# - Architecture backlog: 3 features
# - Business backlog: 2 features  
# - Recently completed: Database Connection Pool
```

## Quality Integration

### @overseer Checkpoints
Each phase includes mandatory @overseer review:
- Requirements completeness
- Test quality and coverage
- Architecture compliance
- Implementation standards

### Feature Completion Criteria
Feature only moves to completed/ when:
- [ ] All 8 phases completed
- [ ] All @overseer approvals obtained
- [ ] All tests passing
- [ ] Quality gates satisfied

## Migration from Epic System

This skill replaces the previous epic-based approach with direct feature selection:
- **Old**: Epic → Multiple Features → Complex tracking
- **New**: Feature → TODO → Direct implementation
- **Benefits**: Simpler workflow, architecture-first priority, independent feature lifecycle

Use this skill anywhere the old epic-workflow was referenced for seamless transition to the new architecture-first approach.