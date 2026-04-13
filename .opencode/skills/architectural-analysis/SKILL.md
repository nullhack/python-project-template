---
name: architectural-analysis
description: Create technical architecture features that complement business features with system design and architectural decisions
license: MIT
compatibility: opencode
metadata:
  audience: architects
  workflow: architecture-analysis
---

## What I do

Create architecture features in `docs/features/architecture/backlog/` that complement business features with technical requirements, system design decisions, and architectural acceptance criteria using UUID traceability.

## When to use me

- After business features are defined in `docs/features/business/backlog/`
- When technical requirements need to be derived from business needs
- To create architectural decisions that guide implementation
- To define technical acceptance criteria that drive unit and smoke tests

## Architecture Feature Creation Process

### 1. Business Feature Analysis
Read business features from `docs/features/business/backlog/` to understand:
- User requirements and business value
- Functional requirements 
- Non-functional requirements (performance, security, scalability)
- Integration points and dependencies

### 2. Technical Requirements Derivation
Transform business needs into technical requirements:
- **Component Responsibilities**: What technical components are needed?
- **Data Flow**: How does information move through the system?
- **Integration Patterns**: How do components communicate?
- **Cross-cutting Concerns**: Security, logging, validation, error handling

### 3. Architecture Feature Structure

Create architecture features using this template:

```markdown
# [Architecture Feature Name]

## Overview
**Purpose**: Technical capability that supports business feature(s)
**Business Context**: Which business features this architecture supports
**Technical Scope**: What technical concerns this addresses

## Component Design
### [ComponentName]
**Responsibility**: Single, clear purpose
**Interface**: Input/output contracts
**Dependencies**: What this component needs

### [AnotherComponent]  
**Responsibility**: Different single purpose
**Interface**: Clean contracts
**Dependencies**: Minimal coupling

## Architecture Decisions (ADRs)

### Decision: [Technology/Pattern Choice]
**Context**: Why this decision was needed
**Options**: What alternatives were considered  
**Choice**: What was selected and why
**Consequences**: Trade-offs and implications

## Technical Acceptance Criteria

### [UUID generated with python -c "import uuid; print(uuid.uuid4())"]
Given: [Technical preconditions - system state, configuration, data setup]
When: [Technical action - API call, system event, component interaction]
Then: [Technical outcome - response format, state change, behavior]

### [Another UUID]
Given: [Different technical scenario]
When: [Different technical trigger]  
Then: [Expected technical result]
```

### 4. UUID Generation for Acceptance Criteria

Generate UUIDs for each technical acceptance criteria:
```bash
python -c "import uuid; print(uuid.uuid4())"
```

Each acceptance criteria gets a unique UUID for test traceability.

### 5. Technical Focus Areas

Architecture features should address:

**System Design**:
- Component boundaries and responsibilities
- Interface definitions and contracts  
- Data transformation strategies
- Error handling patterns

**Quality Attributes**:
- Performance targets and strategies
- Security architecture decisions
- Scalability patterns
- Reliability mechanisms  

**Integration Architecture**:
- API design and contracts
- Message formats and protocols
- Database schema and access patterns
- External service integration

**Implementation Guidance**:
- Design patterns to use
- Code organization principles
- Testing strategies  
- Development constraints

### 6. Architecture Feature Naming

Use descriptive technical names that complement business features:
- Business: "User Authentication"  
- Architecture: "JWT Token Management System"

- Business: "Product Catalog Search"
- Architecture: "Full-Text Search Index Architecture" 

### 7. Quality Gates

Before completing architecture feature:
- [ ] All technical acceptance criteria have UUIDs
- [ ] Component responsibilities are single-purpose
- [ ] Architecture decisions are documented with rationale
- [ ] Technical requirements trace back to business needs
- [ ] Integration points are explicitly defined
- [ ] Cross-cutting concerns are addressed

## Integration with Development Workflow

### Phase 3: Architecture Analysis
1. **Read business features** from `docs/features/business/backlog/`
2. **Analyze technical needs** and architectural requirements
3. **Create architecture features** in `docs/features/architecture/backlog/`
4. **Document ADRs** for significant technical decisions
5. **Generate technical acceptance criteria** with UUIDs

### Handoff to Phase 4
Architecture features provide:
- **Technical acceptance criteria** for unit/smoke test creation
- **Component specifications** for interface design
- **Integration contracts** for system testing
- **Architectural constraints** for implementation guidance

## Example Architecture Feature

```markdown
# Database Connection Pool Management

## Overview
**Purpose**: Reliable database connection management for high-concurrency applications
**Business Context**: Supports "User Authentication" and "Data Synchronization" business features
**Technical Scope**: Connection lifecycle, resource management, error recovery

## Component Design
### ConnectionPool
**Responsibility**: Manage pool of reusable database connections
**Interface**: get_connection() -> Connection, release_connection(conn: Connection)
**Dependencies**: Database driver, configuration service

### ConnectionValidator
**Responsibility**: Verify connection health before use
**Interface**: is_valid(conn: Connection) -> bool
**Dependencies**: Database connection interface

## Architecture Decisions (ADRs)

### Decision: Use HikariCP-style connection pooling
**Context**: Need reliable connection management under high load
**Options**: Simple connection per request, basic pooling, advanced pooling with validation
**Choice**: Advanced pooling with health checks and automatic recovery
**Consequences**: Higher complexity but better reliability and performance

## Technical Acceptance Criteria

### a1b2c3d4-e5f6-7890-abcd-ef1234567890
Given: Database connection pool configured for 100 connections with health checks enabled
When: Application requests 150 concurrent connections under normal load
Then: Pool should serve connections without blocking and maintain response time < 10ms

### b2c3d4e5-f6g7-8901-bcde-f23456789012
Given: Database becomes temporarily unavailable 
When: Connection pool detects failed connections during health check
Then: Failed connections should be marked invalid and new connections attempted automatically

### c3d4e5f6-g7h8-9012-cdef-g34567890123
Given: Connection pool at 90% capacity
When: New connection requests arrive
Then: Pool should create new connections up to maximum limit and queue excess requests
```

## Output Location

Architecture features are created in:
```
docs/features/architecture/backlog/[feature-name]/
├── architecture-feature.md     # Main architecture specification
└── technical-acceptance-criteria.md  # Detailed UUID criteria (if needed separately)
```

## Success Criteria

Architecture feature is complete when:
- [ ] Technical requirements derived from business features
- [ ] All components have single responsibilities  
- [ ] Architecture decisions documented with ADRs
- [ ] Technical acceptance criteria have UUIDs
- [ ] Integration points explicitly defined
- [ ] Ready for manager to create test signatures