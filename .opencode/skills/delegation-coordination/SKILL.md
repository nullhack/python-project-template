---
name: delegation-coordination
description: Enable proper agent handoffs and workflow coordination with explicit delegation rules
license: MIT
compatibility: opencode
metadata:
  audience: all-agents
  workflow: agent-coordination
---

## What I do
Define explicit delegation rules and provide guidance for proper agent handoffs throughout the development workflow. Each agent knows when and how to delegate to other agents.

## When to use me
- When determining which agent to call for specific tasks
- During workflow transitions between development phases
- When quality issues require specific expertise
- During /init workflow progression

## Agent Delegation Matrix

### Requirements Gathering Phase
```
@requirements-gatherer completes → @architect (design review)
                            → @overseer (requirements quality check if needed)
                            → @manager (handoff to planning)
```

### Architecture Review Phase
```
@architect completes → @manager (create TODOs)
                    → @requirements-gatherer (if requirements unclear)
                    → @overseer (architectural compliance)
```

### Development Phase
```
@developer needs help → @architect (design questions)
                     → @overseer (mandatory checkpoints)
                     → @manager (workflow issues)
                     → @repo-manager (Git operations)

@developer completes phase → @overseer (QA checkpoint)
                          → @manager (phase transition)
```

### Quality Assurance Phase
```
@overseer detects issue → Auto-delegate based on issue type:
                        • Code issues → @developer
                        • Architecture → @architect
                        • Requirements → @requirements-gatherer  
                        • Workflow → @manager

@overseer approves → @developer (proceed to next phase)
                 → @manager (feature completion)
```

### Release Phase
```
@manager initiates release → @repo-manager (Git/PR tasks)
                          → @overseer (final release approval)
```

## Explicit Delegation Rules

### @requirements-gatherer Delegation Rules
**Delegates to when:**
- Requirements are complete and need architectural review → @architect
- Requirements quality needs validation → @overseer
- Project coordination needed after requirements → @manager

**Delegation pattern:**
```markdown
1. Complete stakeholder interviews
2. Create docs/requirements/REQUIREMENTS.md
3. Generate acceptance criteria with Example format
4. → Call @architect for technical review
```

### @architect Delegation Rules
**Delegates to when:**
- Architecture is approved and TODOs needed → @manager
- Requirements are incomplete/unclear → @requirements-gatherer  
- Architectural compliance needs review → @overseer
- Technical feasibility questions → @developer for assessment

**Delegation pattern:**
```markdown
1. Review REQUIREMENTS.md for technical feasibility
2. Create/update EPICS.md with technical architecture
3. Validate SOLID principle compliance
4. → Call @manager when architecture approved
```

### @manager Delegation Rules
**Delegates to when:**
- Development phases need execution → @developer
- QA checkpoints require enforcement → @overseer
- Architectural decisions arise → @architect
- Git/release operations needed → @repo-manager

**Delegation pattern:**
```markdown
1. Create comprehensive 7-phase TODOs
2. Embed mandatory @overseer checkpoints
3. Coordinate agent handoffs at phase transitions
4. → Call @developer to start Phase 1
```

### @developer Delegation Rules
**Delegates to when:**
- Design review needed → @architect
- QA checkpoints reached → @overseer  
- Workflow coordination needed → @manager
- Git/PR operations needed → @repo-manager
- Technical questions during implementation → @architect

**Delegation pattern:**
```markdown
1. Execute current phase tasks using skills
2. Request @overseer review at checkpoints
3. Call @architect for design questions
4. Update TODO progress
```

### @overseer Delegation Rules (Auto-Recovery)
**Auto-delegates to when:**
- Code quality issues detected → @developer
- Architecture violations found → @architect
- Requirements conflicts discovered → @requirements-gatherer
- Workflow problems identified → @manager

**Auto-delegation pattern:**
```markdown
1. Detect quality violation
2. Identify issue type
3. → Call appropriate agent for fix
4. Block progress until resolved
5. Wait for manual retry of validation
```

### @repo-manager Delegation Rules
**Delegates to when:**
- Release approval needed → @overseer
- Code changes needed for release → @developer
- Release coordination needed → @manager

**Delegation pattern:**
```markdown
1. Create feature branch
2. Manage PR workflow
3. Coordinate release process
4. → Call @overseer for final approval
```

## Workflow Transition Rules

### Phase Transitions (Managed by @manager)

#### Requirements → Architecture
**Trigger**: Requirements complete in REQUIREMENTS.md
**Action**: @requirements-gatherer → @architect
**Validation**: Architect confirms technical feasibility

#### Architecture → Planning  
**Trigger**: EPICS.md updated with technical design
**Action**: @architect → @manager
**Validation**: Manager creates detailed TODOs

#### Planning → Development
**Trigger**: TODOs created with QA checkpoints
**Action**: @manager → @developer
**Validation**: Developer confirms task assignment

### Phase Transitions (Development by @developer)

#### Test Development → Design
**Trigger**: Tests written with TDD
**Action**: @developer calls @signatures-design + @architect
**Validation**: Architect approves design

#### Design → Implementation
**Trigger**: Design approved
**Action**: @developer executes implementation
**Validation**: All tests pass, quality checks pass

#### Implementation → Quality
**Trigger**: Code implemented
**Action**: @developer calls @code-quality
**Validation**: @overseer final approval required

### QA Checkpoint Rules

#### Mandatory Checkpoints
1. **Phase 1 (Requirements)** → @overseer reviews completeness
2. **Phase 3 (Test Dev)** → @overseer reviews test quality
3. **Phase 4 (Design)** → @overseer reviews SOLID compliance
4. **Phase 5 (Implementation)** → @overseer reviews code quality
5. **Phase 6 (Final QA)** → @overseer final approval

#### Blocking Rules
- No phase can proceed without @overseer approval
- Quality issues trigger auto-delegation
- No bypasses allowed for checkpoints
- Manual retry required after fixes

## Delegation Decision Trees

### Quality Issue Detected
```
Issue Detected by @overseer
    ↓
Identify Issue Type
    ├── Code Quality → → @developer
    ├── Architecture → → @architect
    ├── Requirements → → @requirements-gatherer
    └── Workflow → → @manager
    ↓
Agent Fixes Issue
    ↓
Request Re-validation
    ↓
@overseer Reviews Fix
    ├── Approved → Proceed
    └── Rejected → Repeat delegation
```

### Phase Transition Request
```
Phase Complete
    ↓
Check QA Checkpoint Status
    ├── Not Approved → Fix issues first
    └── Approved → Continue
    ↓
Determine Next Agent
    ├── Next Phase → @developer
    ├── Completion → @manager
    └── Release → @repo-manager
    ↓
Handoff to Next Agent
```

## Error Recovery Patterns

### Issue: Agent Not Responding
```
1. Verify agent called correctly
2. Check agent availability
3. → Alternative: Call different agent
4. → Escalation: Use @manager for coordination
```

### Issue: Quality Not Resolved
```
1. Review @overseer feedback
2. Identify specific issues
3. → Delegate to appropriate agent
4. Request re-review
5. If still failing: Escalate to @architect
```

### Issue: Wrong Agent Called
```
1. Review task requirements
2. Identify correct agent per matrix
3. → Re-delegate to correct agent
4. Explain context to new agent
```

## Integration with Agents

Each agent should:
1. Know their delegation authority from this skill
2. Understand when to auto-delegate
3. Follow explicit pattern for handoffs
4. Maintain context during delegations

### Using This Skill
```markdown
When you need to call another agent:

1. Identify the task/expertise needed
2. Consult delegation matrix above
3. Call appropriate agent with clear context
4. Wait for completion
5. Continue workflow
```

Remember: Proper delegation ensures the right expertise is applied at the right time, maintaining workflow efficiency and quality standards.