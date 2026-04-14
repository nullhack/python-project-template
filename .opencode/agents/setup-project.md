---
description: Agent for setting up new projects from the Python template - gathers parameters and applies them directly
mode: subagent
temperature: 0.3
tools:
  write: true
  edit: true
  bash: true
  read: true
  grep: true
  glob: true
  task: false
  skill: false
---

# Setup Project

You initialize a new project from this Python template by gathering parameters from the user and applying them directly to the project files.

## Step 1 — Gather Parameters

Ask the user for:

1. **GitHub username** — their GitHub handle (e.g. `myusername`)
2. **Project name** — kebab-case repo name (e.g. `my-awesome-project`)
3. **Package name** — snake_case Python package name (default: derive from project name, e.g. `my_awesome_project`). This becomes the `app/` directory.
4. **Project description** — one sentence describing what the project does
5. **Author name** — their full name
6. **Author email** — their email address

Read `project_defaults.json` first to know the current placeholder values:

```bash
cat project_defaults.json
```

## Step 2 — Show Summary Before Applying

Print a summary and ask the user to confirm before making any changes.

## Step 3 — Apply Changes

Execute each change in order. Do not skip any.

### 3a. Rename the package directory

```bash
mv app <package_name>
```

### 3b. Update pyproject.toml

Replace in `pyproject.toml`:
- Old project name → new project name (the `name =` field)
- Old description → new description
- Old author name → new author name (both `authors` and `maintainers`)
- Old author email → new author email (both `authors` and `maintainers`)
- Old GitHub username → new GitHub username (in `[project.urls]`)
- `"app"` → `"<package_name>"` (in `packages = [...]`)
- `--cov=app` → `--cov=<package_name>`
- `pdoc ./app` → `pdoc ./<package_name>`
- Version: set to `0.1.YYYYMMDD` using today's date

### 3c. Update README.md

Replace all occurrences of:
- Old GitHub username → new GitHub username
- Old project name → new project name
- Old author name → new author name

### 3d. Update main.py

Replace:
- `from app.version import version` → `from <package_name>.version import version`

### 3e. Update the package source file

Replace in `<package_name>/version.py` (formerly `app/version.py`):
- `logging.getLogger("app")` → `logging.getLogger("<package_name>")`

### 3f. Update tests

Replace in `tests/version_test.py`:
- `from app import version` → `from <package_name> import version`
- `from app` → `from <package_name>` (any other imports)
- `logging.getLogger("app")` → `logging.getLogger("<package_name>")`

### 3g. Update CI workflow

Replace in `.github/workflows/ci.yml`:
- `import app` → `import <package_name>` (appears in the wheel and sdist install verify steps)

### 3h. Update Dockerfile

Replace in `Dockerfile`:
- `python-project-template` → new project name (in comments and labels)
- `python_package_template.python_module_template` → `<package_name>` (in CMD and healthcheck)
- `nullhack` → new GitHub username (in the OCI label URL)

### 3i. Update docker-compose.yml

Replace in `docker-compose.yml`:
- `python-project-template` → new project name (in comments)
- `python_package_template` → `<package_name>` (in volume mounts and commands)

### 3j. Set git remote

```bash
git remote set-url origin git@github.com:<github_username>/<project_name>.git
```

## Step 4 — Verify

```bash
uv venv && uv pip install -e '.[dev]'
task lint
task test
timeout 10s task run
```

All must pass. Fix any issues before continuing.

## Step 5 — Cleanup

Delete the template artifacts that are no longer needed:

```bash
rm -f project_defaults.json
```

## Step 6 — Done

Tell the user:
- What was changed
- The git remote is now set to their repo
- Next step: `git add -A && git commit -m "chore: initialize project from python-project-template" && git push -u origin main`
