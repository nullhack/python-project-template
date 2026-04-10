# Python Project Template - Enterprise Development Framework

This repository contains an enterprise-grade Cookiecutter template for Python projects with integrated AI-enhanced development workflows.

## Template Overview

| Component | Description |
|-----------|-------------|
| **Purpose** | Generate Python projects with enterprise development practices and AI-powered workflows |
| **Methodology** | Test-Driven Development (TDD) with mandatory quality gates |
| **Standards** | SOLID principles, Object Calisthenics, DRY/KISS, 100% test coverage |
| **Versioning** | Semantic versioning for template, hybrid calver for generated projects |
| **Architecture** | Domain-driven design with architectural review process |

## Template Management Team

### DevOps and Release Engineering

- **template-manager**: DevOps Engineer specializing in template lifecycle management, CI/CD pipelines, and quality assurance
- **repo-manager**: Release Engineer managing version control, pull requests, and semantic releases

### Available Skills

- **template-test**: Test cookiecutter template generation with various configurations
- **template-release**: Manage template releases with semantic versioning
- **git-release**: Create semantic releases for the template repository
- **pr-management**: Create and manage pull requests for template improvements

## Template Structure

```
python-project-template/
├── cookiecutter.json                     # Template configuration
├── {{cookiecutter.project_slug}}/        # Generated project template
│   ├── .opencode/                        # AI agents for generated projects
│   │   ├── agents/
│   │   │   ├── developer.md              # Main development agent
│   │   │   ├── architect.md              # Design review agent
│   │   │   ├── requirements-gatherer.md  # Business analyst agent
│   │   │   ├── overseer.md               # QA specialist agent
│   │   │   └── repo-manager.md           # Repository management agent
│   │   └── skills/
│   │       ├── session-workflow/         # Session state management
│   │       ├── epic-workflow/            # Epic-based development
│   │       ├── feature-definition/       # SOLID feature planning
│   │       ├── prototype-script/         # Quick validation scripts
│   │       ├── tdd/                      # Test-driven development
│   │       ├── signature-design/         # Interface design
│   │       ├── implementation/           # TDD implementation
│   │       ├── code-quality/             # Quality enforcement
│   │       ├── git-release/              # Release management
│   │       ├── pr-management/            # Pull request workflows
│   │       ├── create-skill/             # Create new skills
│   │       └── create-agent/             # Create new agents
│   ├── pyproject.toml                    # Project configuration
│   └── AGENTS.md                         # Generated project AI documentation
├── .opencode/                            # Meta agents for template itself
│   ├── agents/
│   │   ├── template-manager.md           # Template development and management
│   │   └── repo-manager.md               # Template repository operations
│   └── skills/
│       ├── template-test/                # Template testing
│       ├── template-release/             # Template release management
│       ├── git-release/                  # Semantic releases for template
│       └── pr-management/                # Pull request workflows for template
└── docs/                                 # Template documentation
```

## What Generated Projects Get

When developers use this template, they get:

### Epic-Based Development with QA Gates
1. **Requirements Gathering** → Business analyst interviews and analysis
2. **QA Checkpoint** → Requirements completeness review
3. **Test-Driven Development** → BDD tests with pytest/hypothesis
4. **QA Checkpoint** → Test quality review
5. **Design & Architecture** → Pattern selection and SOLID design
6. **Implementation** → TDD methodology (Red-Green-Refactor)
7. **QA Checkpoint** → SOLID/DRY/KISS compliance review
8. **Final Quality** → Comprehensive quality checks
9. **QA Checkpoint** → Final approval before feature completion
10. **Automatic Progression** → System moves to next feature in epic

### AI Agents with Industry Roles
- **@developer** → Development lead with TDD workflow and QA integration
- **@architect** → Software architect for design patterns and SOLID principles
- **@requirements-gatherer** → Business analyst using BABOK principles  
- **@overseer** → QA specialist with mandatory quality checkpoints
- **@repo-manager** → Release engineer for repository operations

### Repository Management
- Hybrid versioning: `v1.2.20260302` (major.minor.calver)
- AI-generated themed releases (unique per release): "Blooming Narwhal", "Crystal Jellyfish", "Electric Firefly"
- Automated PR workflows with conventional commits
- GitHub CLI integration

### Code Quality Standards
- SOLID principles enforcement with architect review
- DRY/KISS principles with overseer validation
- Object calisthenics compliance (9 rules)
- 100% test coverage requirement
- Comprehensive linting with ruff
- Static type checking with pyright
- Property-based testing with Hypothesis
- API documentation with pdoc
- BDD-style test reports with pytest-html-plus
- Mandatory QA gates that cannot be bypassed

## Template Usage

### Creating a New Project
```bash
# Use the latest template
cookiecutter gh:your-username/python-project-template

# Or use a specific version
cookiecutter gh:your-username/python-project-template --checkout v1.2.20260312
```

### Template Development Workflow
```bash
# 1. Make changes to template
# Edit template files, add new agents/skills

# 2. Test template generation
@template-manager /skill template-test

# 3. Create template release
@template-manager /skill template-release

# 4. Generated projects now have new features
```

## Template Versioning

### Hybrid Calver Versioning for Template
- **Major (v2.x.20260401)**: Breaking changes to cookiecutter variables
- **Minor (v1.x.20260315)**: New agents, skills, workflow features, or same-day releases

### Recent Releases
- **v1.0.20260312**: Initial release with development workflow
- **v1.1.20260312**: Added repository management agent
- **v1.2.20260312**: Added meta template management system
- **v1.3.20260313**: Added session-workflow skill
- **v1.4.20260313**: Added AI-driven themed naming
- **v1.5.20260403**: Replaced mkdocs with pdoc for API docs, added pytest-html-plus with BDD docstring display
- **v1.6.20260410**: Added QA-gated epic workflow with business analyst and QA specialist agents

## Generated Project Features

### Agents Included in Generated Projects
- **@developer**: Complete development workflow with mandatory QA gates
- **@architect**: Software architect for design patterns and SOLID principles
- **@requirements-gatherer**: Business analyst for stakeholder requirements
- **@overseer**: QA specialist enforcing quality at checkpoints
- **@repo-manager**: Git operations, PRs, and themed releases

### Skills Included in Generated Projects
- **session-workflow**, **epic-workflow** (multi-session and epic management)
- **feature-definition**, **prototype-script**, **tdd**
- **signature-design**, **implementation**, **code-quality**
- **git-release**, **pr-management**
- **create-skill**, **create-agent**

### Example Generated Project Usage
```bash
# In a generated project - Epic-based workflow
@requirements-gatherer               # Gather requirements
@overseer                           # QA: Requirements review
@developer /skill tdd               # Write tests  
@overseer                           # QA: Test quality review
@architect                          # Design approval
@developer /skill implementation    # Implement feature
@overseer                           # QA: Code quality review
@developer /skill epic-workflow next-feature  # Auto-progress to next
```

## Template Development

### Making Template Changes
1. **Update Template Files**: Modify files in `{{cookiecutter.project_slug}}/`
2. **Add New Agents/Skills**: Create in `.opencode/` directory
3. **Test Changes**: Use `@template-manager /skill template-test`
4. **Release Template**: Use `@template-manager /skill template-release`

### Quality Standards for Template
- All generated projects must pass quality checks
- Template testing with multiple configurations
- Documentation must be up-to-date
- YAML frontmatter must be valid in all agents/skills

### Contributing to Template
1. Fork the template repository
2. Make improvements following template standards
3. Test thoroughly with various configurations
4. Create PR with description of changes
5. Template maintainers will review and merge

## Template Management Workflow

### Agent Roles in Template Development
- **@template-manager**: Handles template-specific tasks like testing generation, validating cookiecutter variables, and releasing new template versions
- **@repo-manager**: Manages the template repository itself - creating PRs, commits, GitHub releases, and handling version control

### Example Template Development
```bash
# Working on template improvements
@template-manager /skill template-test    # Test template generation
@repo-manager /skill pr-management        # Create PR for changes
@template-manager /skill template-release # Release new template version
```

## Integration with OpenCode

The template is designed to work seamlessly with OpenCode:

```bash
# In generated projects
opencode
/opencode
/init                    # Generate fresh AGENTS.md

# Use the workflow
@developer               # Main development agent
@architect              # Architecture review
@repo-manager           # Repository operations
```

This template provides a complete AI-enhanced development environment for Python projects, ensuring high code quality, proper testing, and professional repository management.