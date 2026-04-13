---
name: requirements-management
description: Generate and manage requirements documentation with hybrid business + technical format
license: MIT
compatibility: opencode
metadata:
  audience: business-analyst
  workflow: requirements-gathering
---

## What I do
Create comprehensive requirements documentation in `docs/requirements/REQUIREMENTS.md` using a hybrid business + technical format with Example-based acceptance criteria.

## When to use me
- When starting a new epic or feature
- During the /init workflow (called by @requirements-gatherer)
- Before architect reviews requirements
- When updating existing requirements

## Requirements Document Structure

### docs/requirements/REQUIREMENTS.md Template

```markdown
# [Project Name] - Requirements

## Business Context

### User Stories
- As a [user type], I want [functionality] so that [business value]
- As a [user type], I want [functionality] so that [business value]

### Business Value & Success Metrics
- [Measurable business outcomes]
- [ROI expectations]
- [User satisfaction criteria]
- [Key performance indicators]

## Technical Requirements

### Functional Requirements
- **[Feature Area]:** [Description of required functionality]
  - [Specific capability with acceptance criteria]
  - [Additional capability]
  
- **[Integration Area]:** [Description of integration needs]
  - [Integration points and dependencies]
  - [Data exchange requirements]

### Non-Functional Requirements
- **Performance:**
  - Response time: < [X] ms for [operation]
  - Throughput: [X] requests/second
  - Concurrent users: Support [X] users
  
- **Scalability:**
  - Horizontal scaling capability
  - Database capacity: [X] records
  - Growth projection: [X]% annually
  
- **Security:**
  - Authentication: [Method]
  - Authorization: [Level]
  - Data encryption: [At rest/in transit/both]
  
- **Reliability:**
  - Uptime: [X]% (e.g., 99.9%)
  - Recovery time: < [X] minutes
  - Backup strategy: [Frequency] backups

### Technology Constraints
- Python version: >=3.13
- Framework: [Name]
- Database: [Type]
- Infrastructure: [Platform]

## Acceptance Criteria (UUID Format)

### Feature: [Feature Name]

Generate UUID for each acceptance criteria:
```bash
python -c "import uuid; print(uuid.uuid4())"
```

### 123e4567-e89b-12d3-a456-426614174000
Given: [Preconditions or initial system state]
When: [User action or system trigger]
Then: [Expected outcome or system response]

### 123e4567-e89b-12d3-a456-426614174001
Given: [Different preconditions]
When: [Different action]  
Then: [Different outcome]

### 123e4567-e89b-12d3-a456-426614174002
Given: [Edge case preconditions]
When: [Edge case action]
Then: [Expected handling]

## Documentation Files Structure

### docs/requirements/
```
docs/requirements/
├── REQUIREMENTS.md              # Main requirements document
├── stakeholder_analysis.md       # Stakeholder interview notes
├── acceptance_criteria.md      # Detailed acceptance criteria
├── technical_specs.md          # Technical specifications
└── version_history.md          # Requirements change log
```

## Stakeholder Interview Process

### Before Interview
1. **Research**: Understand the domain and problem space
2. **Prepare Questions**: Business value, user needs, constraints
3. **Set Expectations**: Explain Example format for acceptance criteria

### Interview Questions Template
1. "What problem are you trying to solve?"
2. "Who are the users and their roles?"
3. "What are the key user workflows?"
4. "What are the success metrics?"
5. "What constraints exist (time, budget, technical)?"
6. "What happens if we don't do this?"
7. "What's the simplest version that provides value?"

### Interview Output Format
```markdown
## Stakeholder Interview: [Name/Role]

### Key Insights
- [Insight 1]: [Description]
- [Insight 2]: [Description]

### Expressed Needs
- [Need 1]: [Priority - High/Medium/Low]
- [Need 2]: [Priority]

### Business Value
- [Primary business driver]
- [Expected outcomes]

### Constraints Identified
- [Constraint 1]
- [Constraint 2]
```

## User Story Format

### Template
```markdown
### US-[Number]: [User Story Title]

**As a** [user type or persona],
**I want** [functionality or feature],
**So that** [business value or benefit].

**Priority**: [P0/P1/P2/P3]
**Estimated Effort**: [Small/Medium/Large]
**Dependencies**: [List of dependent stories]
```

### Example
```markdown
### US-001: User Authentication

**As a** registered user,
**I want** to log in with my credentials,
**So that** I can access my personalized dashboard.

**Priority**: P0 (Critical)
**Estimated Effort**: Medium
**Dependencies**: None
```

## Acceptance Criteria Format (Example-Based)

### Structure
```markdown
### AC-[Number]: [Criteria Description]

**Example**: [Descriptive scenario name]
```
Given: [Precondition or initial state]
When: [Action or trigger]
Then: [Expected outcome]
```

**Validation**:
- [ ] Test verifies Given state exists
- [ ] Test verifies When action is performed  
- [ ] Test verifies Then outcome occurs
```

### Examples
```markdown
### AC-001: Successful User Login

**Example**: Valid credentials authenticate user
```
Given: A registered user with email "user@example.com" and password "secret123"
When: The user submits login credentials
Then: The user should be granted access to the application
And: A user session should be created
```

### AC-002: Invalid Login Rejection

**Example**: Invalid password shows error
```
Given: A registered user with email "user@example.com" exists
When: The user submits incorrect password
Then: Access should be denied
And: Error message "Invalid credentials" should be displayed
```
```

## Technical Specification Guidelines

### API Requirements Format
```markdown
### API: [Endpoint Name]

**Endpoint**: `[METHOD] /api/v1/[resource]`

**Request**:
```json
{
  "field1": "type",
  "field2": "type"
}
```

**Response** (Success):
```json
{
  "status": "success",
  "data": { ... }
}
```

**Response** (Error):
```json
{
  "status": "error",
  "message": "description"
}
```

**Acceptance Criteria**:
- [ ] Valid request returns 200 status
- [ ] Missing required fields returns 400
- [ ] Unauthorized returns 401
- [ ] Not found returns 404
```

### Database Requirements Format
```markdown
### Entity: [Entity Name]

**Table**: `[table_name]`

| Column | Type | Constraints | Description |
|--------|------|-------------|--------------|
| id | UUID | PRIMARY KEY | Unique identifier |
| created_at | TIMESTAMP | NOT NULL | Creation timestamp |
| updated_at | TIMESTAMP | NOT NULL | Last update timestamp |

**Relationships**:
- [Entity A] 1:N [Entity B]
- [Entity C] 1:1 [Entity D]
```

## Version History

### Change Log Format
```markdown
## Version History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| YYYY-MM-DD | 1.0.0 | Initial requirements | @requirements-gatherer |
| YYYY-MM-DD | 1.1.0 | Added [feature] | [Author] |
```

## Hand-off to Architect

After requirements are complete, document for architect:
1. **Summary**: 2-3 sentence overview
2. **Business Value**: Primary outcomes expected
3. **Key Features**: Must-have capabilities
4. **Constraints**: Technical, time, budget limits
5. **Risks**: Identified potential issues
6. **Dependencies**: External systems and requirements

The architect will use this to create docs/roadmap.md with technical breakdown.