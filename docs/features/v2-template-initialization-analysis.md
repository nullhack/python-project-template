# Feature Analysis: V2 Template Initialization System

## Executive Summary
Replace cookiecutter with a dedicated subagent-based initialization system that provides dynamic, intelligent project setup for fresh Python projects using minimal templating and AI-enhanced workflows.

## Business Context
### Problem Statement
The current cookiecutter-based approach is static and doesn't integrate well with AI-enhanced development workflows. Developers need a more intelligent, dynamic setup process that seamlessly integrates with OpenCode agents from project creation.

### Stakeholders
- **Primary Users**: Python developers creating new projects from this template
- **Business Owner**: Template maintainers and OpenCode ecosystem
- **Technical Owner**: Python Project Template development team

### Success Metrics
- Setup time under 2 minutes for complete project initialization
- Zero configuration errors during setup
- 100% integration with existing OpenCode agent workflows
- Developer satisfaction with setup experience

## Functional Requirements

### User Stories
**As a Python developer**, I want to create a new project from the V2 template so that I have a fully configured, AI-enhanced development environment ready immediately.

**As a development team lead**, I want consistent project structure across all team projects so that developers can easily switch between projects and maintain quality standards.

### Acceptance Criteria
#### Scenario 1: Fresh Project Creation
```gherkin
Given: A developer wants to create a new Python project
When: They run the template initialization command
Then: A fully configured project should be created with:
  - Correct project metadata in all files
  - Working development environment
  - All OpenCode agents operational
  - Clean git repository initialized
  - All tests passing
```

#### Scenario 2: Dynamic Content Substitution
```gherkin
Given: Template files with placeholder content
When: Developer provides project metadata during setup
Then: All placeholders should be replaced with actual values
  - Project names in pyproject.toml
  - Author information in README.md
  - Package/module names in code files
  - GitHub URLs and references
```

#### Scenario 3: Clean State Initialization
```gherkin
Given: Template contains development state files
When: Project initialization completes
Then: All state files should be reset to clean initial state
  - TODO.md contains fresh project setup tasks
  - EPICS.md contains template epic structure
  - No development history from template
```

### Process Flow
1. **Agent Invocation**: Developer calls `@project-initializer` agent
2. **Metadata Collection**: Agent prompts for required project information
3. **Validation**: Agent validates inputs (names, email format, etc.)
4. **Template Processing**: Agent processes .template files and replaces placeholders
5. **File Operations**: Agent moves .template files to active files
6. **State Reset**: Agent initializes clean state files
7. **Git Initialization**: Agent creates fresh git repository
8. **Environment Setup**: Agent runs initial setup commands
9. **Validation**: Agent verifies setup completion

### Data Requirements
#### Inputs
- **Project Name**: String - Human-readable project name (e.g., "My Awesome Project")
- **Project Slug**: String - URL/directory-safe name (e.g., "my-awesome-project")
- **Package Name**: String - Python package name (e.g., "my_awesome_project")
- **Module Name**: String - Main module name (e.g., "my_awesome_module")
- **Author Name**: String - Full name for attribution
- **Author Email**: Email - Valid email address
- **GitHub Username**: String - GitHub username for URLs
- **Description**: String - One-line project description
- **License**: String - License type (default: MIT)

#### Outputs
- **Active Project Files**: All .template files processed and moved to final names
- **Updated pyproject.toml**: Complete project metadata
- **Clean State Files**: Fresh TODO.md, EPICS.md with project-specific content
- **Git Repository**: Initialized with initial commit
- **Development Environment**: Virtual environment and dependencies installed

#### Template Files Required
- **pyproject.toml.template**: Project metadata, dependencies, tool configuration
- **README.md.template**: Project documentation with dynamic content
- **python_package_template/**: Entire package directory (rename to actual package name)

## Non-Functional Requirements

### Performance
- **Setup Time**: Complete initialization in under 2 minutes
- **Validation Speed**: Input validation in under 1 second
- **File Operations**: Template processing in under 10 seconds

### Security
- **Input Validation**: Sanitize all user inputs to prevent injection
- **File Safety**: Validate file paths to prevent directory traversal
- **Git Safety**: Clean git initialization without sensitive data

### Scalability
- **Project Size**: Support projects from simple scripts to enterprise applications
- **Template Growth**: Architecture supports adding new template files easily
- **Agent Integration**: Seamless integration with all existing OpenCode agents

## Technical Constraints
- Must maintain compatibility with existing OpenCode agent ecosystem
- Should work on Linux, macOS, and Windows
- Requires Python 3.13+, UV, Git, and OpenCode
- Must preserve all current template functionality
- No external API dependencies for core functionality

## Integration Points
### External Systems
- **Git**: Repository initialization and management
- **UV**: Virtual environment and dependency management
- **OpenCode**: Agent integration and workflow management
- **File System**: Template file processing and project structure creation

## Risk Assessment
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Template file corruption during processing | High | Low | Backup original files, validate before processing |
| Invalid user input causing setup failure | Medium | Medium | Comprehensive input validation and error messages |
| Git initialization conflicts | Medium | Low | Check for existing .git directory, clear error messages |
| Missing dependencies breaking setup | High | Low | Validate tool availability before starting |

## Out of Scope
- V1 to V2 migration functionality
- Updating existing projects
- GUI interface for setup
- Integration with IDEs beyond command line
- Support for non-Python projects
- Automatic GitHub repository creation

## Agent Design: project-initializer

### Agent Name
**project-initializer** - Dedicated agent for V2 template initialization

### Agent Responsibilities
1. **Interactive Setup**: Prompt user for all required project metadata
2. **Input Validation**: Validate all inputs according to Python/Git conventions
3. **Template Processing**: Process .template files and replace placeholders
4. **File Operations**: Move template files to final locations with correct names
5. **State Initialization**: Create clean TODO.md and EPICS.md for new project
6. **Environment Setup**: Initialize git repository and development environment
7. **Verification**: Validate that setup completed successfully

### Agent Workflow
```bash
# Usage
@project-initializer

# Agent prompts for:
# - Project name: "My Awesome Project"
# - Author: "John Doe"
# - Email: "john@example.com"
# - GitHub username: "johndoe"
# - Description: "An awesome Python project"

# Agent then:
# 1. Validates all inputs
# 2. Processes template files
# 3. Renames package directories
# 4. Initializes clean state
# 5. Sets up git repository
# 6. Installs dependencies
# 7. Runs initial tests
```

## Minimal Template Files

### Files Requiring .template Versions
1. **pyproject.toml.template**
   - Project name, description, author, email
   - Package name in setuptools configuration
   - Repository URLs

2. **README.md.template**
   - Project name in title and descriptions
   - Author attribution
   - GitHub URLs and badges
   - Package/module names in code examples

3. **python_package_template/** (entire directory)
   - Rename to actual package name
   - Update import statements in __init__.py
   - Update module names

### Files Reset to Clean State
1. **TODO.md**: Replace with fresh project setup tasks
2. **EPICS.md**: Reset to template epic structure
3. **Git history**: Fresh repository with initial commit

### Files Unchanged
- All .opencode/ agent and skill definitions
- tests/ directory structure
- Dockerfile
- .gitignore
- LICENSE
- All development tooling configuration

## Placeholder Format
Use `{{VARIABLE_NAME}}` format for consistency:
- `{{PROJECT_NAME}}` - Human-readable project name
- `{{PROJECT_SLUG}}` - URL-safe project name
- `{{PACKAGE_NAME}}` - Python package name
- `{{MODULE_NAME}}` - Main module name
- `{{AUTHOR_NAME}}` - Author full name
- `{{AUTHOR_EMAIL}}` - Author email
- `{{GITHUB_USERNAME}}` - GitHub username
- `{{DESCRIPTION}}` - Project description
- `{{LICENSE}}` - License type

## Questions for Architect
1. Should the project-initializer agent be a standalone script or integrated into the OpenCode agent system?
2. What's the preferred approach for template file processing - simple string replacement or a template engine?
3. How should we handle package directory renaming (python_package_template → actual_package_name)?
4. Should the agent validate GitHub username existence or just format?
5. What's the error recovery strategy if setup fails partway through?
6. Should there be a "dry run" mode to preview changes before applying?

## Implementation Priority
1. **Phase 1**: Create project-initializer agent with basic functionality
2. **Phase 2**: Implement template file processing
3. **Phase 3**: Add input validation and error handling
4. **Phase 4**: Integrate with git and environment setup
5. **Phase 5**: Add comprehensive testing and documentation

## Appendix

### Example Template Processing
**Before (pyproject.toml.template):**
```toml
[project]
name = "{{PROJECT_SLUG}}"
description = "{{DESCRIPTION}}"
authors = [
    { name = "{{AUTHOR_NAME}}", email = "{{AUTHOR_EMAIL}}" }
]
```

**After (pyproject.toml):**
```toml
[project]
name = "my-awesome-project"
description = "An awesome Python project"
authors = [
    { name = "John Doe", email = "john@example.com" }
]
```

### Fresh State Files
**TODO.md (after initialization):**
```markdown
# My Awesome Project - Development TODO

## Current Epic: Project Foundation
## Current Feature: Initial Development

### Phase 0: Project Setup
- [x] Project initialized from V2 template
- [ ] Review and customize README.md
- [ ] Define first business epic in EPICS.md
- [ ] Implement core functionality
```