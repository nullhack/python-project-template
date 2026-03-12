---
name: template-test
description: Test cookiecutter template generation with automatic responses and validate generated project quality
license: MIT
compatibility: opencode
metadata:
  audience: template-maintainers
  workflow: template-management
---
## What I do
Test the cookiecutter template generation process with various configurations, validate the generated projects work correctly, and ensure all OpenCode agents/skills function properly.

## When to use me
Use this before any template release, after making changes to template files, or when validating template functionality.

## Template Testing Strategy

### Test Scenarios

#### 1. Default Generation Test
```bash
# Test with all default values from cookiecutter.json
cookiecutter . --no-input

# Expected output directory: python-project-example/
# (based on default project_name in cookiecutter.json)
```

#### 2. Custom Values Test
```bash
# Test with custom configuration
cookiecutter . --no-input \
  full_name="Jane Developer" \
  email="jane@example.com" \
  github_username="jane-dev" \
  project_name="My Awesome Project" \
  project_short_description="An amazing Python project using AI workflows" \
  minimum_coverage="90" \
  license="Apache_2.0" \
  version="0.2.0"

# Expected output directory: my-awesome-project/
```

#### 3. Edge Cases Test
```bash
# Test with edge case values
cookiecutter . --no-input \
  project_name="Project With Spaces And-Hyphens_Underscores" \
  project_short_description="A very long description that tests how the template handles lengthy text input and ensures it doesn't break any generated files or configurations" \
  minimum_coverage="100" \
  github_username="user-with-hyphens"

# Expected output directory: project-with-spaces-and-hyphens-underscores/
```

## Validation Checklist

### Generated Project Structure
```bash
# Verify directory structure
test -d "${project_dir}"
test -d "${project_dir}/.opencode"
test -d "${project_dir}/.opencode/agents"
test -d "${project_dir}/.opencode/skills"
test -f "${project_dir}/pyproject.toml"
test -f "${project_dir}/README.md"
test -f "${project_dir}/AGENTS.md"
test -f "${project_dir}/DEVELOPMENT_WORKFLOW.md"
```

### File Content Validation
```bash
# Check cookiecutter variables were substituted correctly
grep -q "{{cookiecutter" "${project_dir}"/* && echo "ERROR: Unsubstituted variables found"

# Validate pyproject.toml syntax
cd "${project_dir}"
python -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))" || echo "ERROR: Invalid pyproject.toml"

# Check README has project name
grep -q "${project_name}" README.md || echo "ERROR: Project name not in README"
```

### OpenCode Agents Validation
```bash
# Test agent YAML frontmatter is valid
for agent in .opencode/agents/*.md; do
    python -c "
import yaml
with open('$agent', 'r') as f:
    content = f.read()
    if '---' in content:
        yaml_part = content.split('---')[1]
        yaml.safe_load(yaml_part)
" || echo "ERROR: Invalid YAML in $agent"
done
```

### Skills Validation
```bash
# Test skill YAML frontmatter is valid
for skill in .opencode/skills/*/SKILL.md; do
    python -c "
import yaml
with open('$skill', 'r') as f:
    content = f.read()
    if '---' in content:
        yaml_part = content.split('---')[1] 
        yaml.safe_load(yaml_part)
" || echo "ERROR: Invalid YAML in $skill"
done

# Check skill naming consistency
for skill_dir in .opencode/skills/*/; do
    skill_name=$(basename "$skill_dir")
    grep -q "name: $skill_name" "$skill_dir/SKILL.md" || echo "ERROR: Skill name mismatch in $skill_dir"
done
```

### Generated Project Quality Tests
```bash
# Install dependencies and run tests
cd "${project_dir}"
python -m venv venv
source venv/bin/activate
pip install uv
uv pip install '.[dev]'

# Run all quality checks that should pass in generated project
task test || echo "ERROR: Tests failed in generated project"
task lint || echo "ERROR: Linting failed in generated project"  
task static-check || echo "ERROR: Type checking failed in generated project"

# Test documentation generation
task doc-report || echo "ERROR: Documentation build failed"

# Verify coverage meets minimum requirement
coverage_result=$(coverage report --format=total)
min_coverage=$(grep 'minimum_coverage' pyproject.toml | grep -o '[0-9]\+')
if [ "$coverage_result" -lt "$min_coverage" ]; then
    echo "ERROR: Coverage $coverage_result% below minimum $min_coverage%"
fi
```

## Complete Testing Script

### Automated Test Runner
```bash
#!/bin/bash
# template_test.sh - Comprehensive template testing script

set -e

# Configuration
TEMPLATE_DIR=$(pwd)
TEST_DIR="/tmp/template-tests"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Clean up previous tests
rm -rf "$TEST_DIR"
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"

echo "🧪 Starting cookiecutter template tests at $TIMESTAMP"

# Test 1: Default configuration
echo "📋 Test 1: Default configuration"
cookiecutter "$TEMPLATE_DIR" --no-input
default_project=$(ls -d */ | head -1 | sed 's/\///')
echo "✅ Generated project: $default_project"

# Test 2: Custom configuration
echo "📋 Test 2: Custom configuration"
cookiecutter "$TEMPLATE_DIR" --no-input \
  full_name="Test Developer" \
  email="test@example.com" \
  github_username="test-dev" \
  project_name="Custom Test Project" \
  project_short_description="Testing template with custom values" \
  minimum_coverage="95" \
  license="MIT" \
  version="1.0.0"

custom_project="custom-test-project"
echo "✅ Generated project: $custom_project"

# Test 3: Edge cases  
echo "📋 Test 3: Edge case configuration"
cookiecutter "$TEMPLATE_DIR" --no-input \
  project_name="Edge Case Project With Long Name" \
  project_short_description="This is a very long description to test edge cases and ensure the template handles it properly without breaking anything" \
  minimum_coverage="100" \
  github_username="edge-case-user"

edge_project="edge-case-project-with-long-name"
echo "✅ Generated project: $edge_project"

# Validation function
validate_project() {
    local project_dir=$1
    local project_name=$2
    
    echo "🔍 Validating $project_dir..."
    
    cd "$project_dir"
    
    # Structure validation
    test -d ".opencode" || { echo "❌ Missing .opencode directory"; return 1; }
    test -d ".opencode/agents" || { echo "❌ Missing .opencode/agents"; return 1; }
    test -d ".opencode/skills" || { echo "❌ Missing .opencode/skills"; return 1; }
    test -f "pyproject.toml" || { echo "❌ Missing pyproject.toml"; return 1; }
    test -f "README.md" || { echo "❌ Missing README.md"; return 1; }
    test -f "AGENTS.md" || { echo "❌ Missing AGENTS.md"; return 1; }
    test -f "DEVELOPMENT_WORKFLOW.md" || { echo "❌ Missing DEVELOPMENT_WORKFLOW.md"; return 1; }
    
    # Check for unsubstituted variables
    if grep -r "{{cookiecutter" . --exclude-dir=venv 2>/dev/null; then
        echo "❌ Found unsubstituted cookiecutter variables"
        return 1
    fi
    
    # Validate pyproject.toml syntax
    python -c "
import tomllib
try:
    with open('pyproject.toml', 'rb') as f:
        tomllib.load(f)
    print('✅ pyproject.toml is valid')
except Exception as e:
    print(f'❌ pyproject.toml is invalid: {e}')
    exit(1)
"
    
    # Validate YAML frontmatter in agents
    for agent in .opencode/agents/*.md; do
        if [ -f "$agent" ]; then
            python -c "
import yaml, sys
with open('$agent', 'r') as f:
    content = f.read()
    if '---' in content:
        parts = content.split('---')
        if len(parts) >= 3:
            try:
                yaml.safe_load(parts[1])
                print('✅ Valid YAML in $agent')
            except Exception as e:
                print(f'❌ Invalid YAML in $agent: {e}')
                sys.exit(1)
"
        fi
    done
    
    # Validate YAML frontmatter in skills
    for skill in .opencode/skills/*/SKILL.md; do
        if [ -f "$skill" ]; then
            python -c "
import yaml, sys
with open('$skill', 'r') as f:
    content = f.read()
    if '---' in content:
        parts = content.split('---')
        if len(parts) >= 3:
            try:
                yaml.safe_load(parts[1])
                print('✅ Valid YAML in $skill')
            except Exception as e:
                print(f'❌ Invalid YAML in $skill: {e}')
                sys.exit(1)
"
        fi
    done
    
    # Check project name appears in key files
    grep -q "$project_name" README.md || { echo "❌ Project name not in README.md"; return 1; }
    grep -q "$project_name" AGENTS.md || { echo "❌ Project name not in AGENTS.md"; return 1; }
    
    # Install dependencies and test
    echo "📦 Installing dependencies..."
    python -m venv venv
    source venv/bin/activate
    pip install uv
    uv pip install '.[dev]' || { echo "❌ Dependency installation failed"; return 1; }
    
    # Run quality checks
    echo "🔧 Running quality checks..."
    
    # Linting
    python -m ruff check . || { echo "❌ Ruff linting failed"; return 1; }
    echo "✅ Linting passed"
    
    # Type checking  
    python -m pyright || { echo "❌ Type checking failed"; return 1; }
    echo "✅ Type checking passed"
    
    # Tests
    python -m pytest tests/ || { echo "❌ Tests failed"; return 1; }
    echo "✅ Tests passed"
    
    # Documentation build
    python -m mkdocs build || { echo "❌ Documentation build failed"; return 1; }
    echo "✅ Documentation build passed"
    
    echo "✅ Project $project_dir validation completed successfully"
    cd ..
    return 0
}

# Run validations
validate_project "$default_project" "Python Project Example"
validate_project "$custom_project" "Custom Test Project" 
validate_project "$edge_project" "Edge Case Project With Long Name"

echo "🎉 All template tests passed successfully!"
echo "📊 Test summary:"
echo "   - Default configuration: ✅"
echo "   - Custom configuration: ✅"
echo "   - Edge case configuration: ✅"
echo "   - Structure validation: ✅"
echo "   - YAML validation: ✅"
echo "   - Quality checks: ✅"
echo "   - Generated projects work: ✅"

# Cleanup
echo "🧹 Cleaning up test artifacts..."
rm -rf "$TEST_DIR"
echo "✅ Template testing completed successfully at $(date)"
```

## Integration with CI/CD

### GitHub Actions Template Test
```yaml
# .github/workflows/template-test.yml
name: Template Testing

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test-template:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.13']
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install cookiecutter
      run: |
        pip install cookiecutter
    
    - name: Test default template generation
      run: |
        cookiecutter . --no-input
        
    - name: Test custom template generation
      run: |
        cookiecutter . --no-input \
          project_name="CI Test Project" \
          project_short_description="Testing in CI" \
          minimum_coverage="95"
    
    - name: Validate generated projects
      run: |
        # Run validation on both generated projects
        for project in python-project-example ci-test-project; do
          cd $project
          python -m venv venv
          source venv/bin/activate
          pip install uv
          uv pip install '.[dev]'
          python -m ruff check .
          python -m pyright
          python -m pytest
          cd ..
        done
```

## Quality Metrics

### Template Health Indicators
- ✅ All test scenarios pass
- ✅ Generated projects have 100% test coverage by default
- ✅ All YAML frontmatter is valid
- ✅ No unsubstituted cookiecutter variables
- ✅ Generated projects pass linting and type checking
- ✅ Documentation builds successfully
- ✅ All OpenCode agents and skills are properly formatted

### Performance Benchmarks
- Template generation time: < 5 seconds
- Generated project setup time: < 30 seconds
- Quality check runtime: < 60 seconds
- Documentation build time: < 15 seconds