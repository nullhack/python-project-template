# Python Project Template - AI-Enhanced Development

This is the meta repository for the AI-Enhanced Python Project Cookiecutter Template.

## Template Overview

| Information | Details |
|-------------|---------|
| **Purpose** | Create AI-enhanced Python projects with comprehensive development workflows |
| **AI Integration** | OpenCode agents and skills for TDD development |
| **Quality Standards** | SOLID principles, object calisthenics, 100% coverage |
| **Versioning** | Hybrid major.minor.calver for generated projects |
| **Architecture** | Test-driven development with architect approval workflow |

## Meta Agent for Template Management

### Available Agent

- **template-manager**: Meta agent for managing the cookiecutter template repository itself

### Available Skills

- **template-test**: Test cookiecutter template generation with various configurations
- **template-release**: Manage template releases with semantic versioning

## Template Structure

```
python-project-template/
├── cookiecutter.json                     # Template configuration
├── {{cookiecutter.project_slug}}/        # Generated project template
│   ├── .opencode/                        # AI agents for generated projects
│   │   ├── agents/
│   │   │   ├── developer.md              # Main development agent
│   │   │   ├── architect.md              # Design review agent
│   │   │   └── repo-manager.md           # Repository management agent
│   │   └── skills/
│   │       ├── feature-definition/       # SOLID feature planning
│   │       ├── prototype-script/         # Quick validation scripts
│   │       ├── tdd/                      # Test-driven development
│   │       ├── signature-design/         # Interface design
│   │       ├── implementation/           # TDD implementation
│   │       ├── code-quality/             # Quality enforcement
│   │       ├── git-release/              # Release management
│   │       └── pr-management/            # Pull request workflows
│   ├── pyproject.toml                    # Project configuration
│   └── AGENTS.md                         # Generated project AI documentation
├── .opencode/                            # Meta agents for template itself
│   ├── agents/template-manager.md        # This meta agent
│   └── skills/
│       ├── template-test/                # Template testing
│       └── template-release/             # Template release management
└── docs/                                 # Template documentation
```

## What Generated Projects Get

When developers use this template, they get:

### AI-Powered Development Workflow
1. **Feature Definition** → SOLID principles planning
2. **Prototype Validation** → Quick scripts with real data
3. **Test-Driven Development** → TDD tests with pytest/hypothesis
4. **Signature Design** → Modern Python interfaces
5. **Architecture Review** → AI architect approval
6. **Implementation** → TDD methodology
7. **Quality Assurance** → Comprehensive quality checks

### Repository Management
- Hybrid versioning: `v1.2.20260302` (major.minor.calver)
- Themed releases: "swift cheetah", "vigilant owl", "creative fox"
- Automated PR workflows with conventional commits
- GitHub CLI integration

### Code Quality Standards
- SOLID principles enforcement
- Object calisthenics compliance
- 100% test coverage requirement
- Comprehensive linting with ruff
- Static type checking with pyright
- Property-based testing with Hypothesis
- API documentation with pdoc
- BDD-style test reports with pytest-html-plus

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

## Generated Project Features

### Agents Included in Generated Projects
- **@developer**: Complete 7-phase development workflow
- **@architect**: Design review and SOLID principles enforcement
- **@repo-manager**: Git operations, PRs, and themed releases

### Skills Included in Generated Projects
- **feature-definition**, **prototype-script**, **tdd**
- **signature-design**, **implementation**, **code-quality**
- **git-release**, **pr-management**
- **create-skill**, **create-agent**

### Example Generated Project Usage
```bash
# In a generated project
@developer /skill feature-definition     # Define new feature
@developer /skill prototype-script       # Create prototype
@developer /skill tdd                # Write tests
@architect                               # Get design approval
@developer /skill implementation         # Implement feature
@repo-manager /skill pr-management       # Create PR
@repo-manager /skill git-release         # Create release
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