---
name: feature-definition
description: Define new features following SOLID principles with clear requirements and acceptance criteria
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Help define new features with clear requirements, acceptance criteria, and technical specifications following SOLID, DRY, KISS principles and object calisthenics.

## When to use me
Use this at the start of any new feature development to establish clear requirements and scope.

## Feature Definition Process

### 1. Feature Overview
- **Name**: Clear, descriptive feature name
- **Purpose**: What problem does this solve?
- **Value**: Why is this feature needed?

### 2. Requirements Analysis
- **Functional Requirements**: What the feature must do
- **Non-functional Requirements**: Performance, security, usability
- **Constraints**: Technical or business limitations

### 3. Acceptance Criteria
Define clear test scenarios using the naming convention:
```
test_when_[condition]_should_[expected_outcome]
```

### 4. Technical Specifications
- **Input/Output Definitions**: What goes in, what comes out
- **Data Structures**: Expected formats (JSON, HTML, return values)
- **Dependencies**: External libraries or services
- **Error Handling**: Edge cases and failure scenarios

### 5. Object Calisthenics Compliance
- Single responsibility per class/function
- No primitive obsession - use value objects
- Wrap collections in dedicated classes
- First-class collections only
- Maximum one dot per line
- No abbreviations
- Keep entities small (< 50 lines per class)

### 6. SOLID Principles Check
- **S**ingle Responsibility: Each class has one reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Derived classes must be substitutable
- **I**nterface Segregation: Clients shouldn't depend on unused methods
- **D**ependency Inversion: Depend on abstractions, not concretions

### Example Feature Definition
```
Feature: User Authentication API

Purpose: Secure user login system
Value: Protects user data and provides personalized experience

Functional Requirements:
- Accept email/password credentials
- Return JWT token on success
- Rate limiting to prevent brute force

Acceptance Criteria:
Given a valid user credential
When POST /auth/login is called
Then return 200 with JWT token

Given invalid credentials
When POST /auth/login is called  
Then return 401 with error message

Technical Specifications:
Input: {"email": "user@example.com", "password": "secret"}
Output: {"token": "jwt.token.here", "expires": "2024-01-01T00:00:00Z"}
Error: {"error": "Invalid credentials", "code": "AUTH_001"}
```