---
name: setup-configure
description: "Gather and confirm project parameters, validate template files exist"
---

# Setup Configure

Template resolution: templates live in `.templates/`. The instance path is the template path with `.templates/` prefix removed and `.template` suffix removed. Discover templates at runtime with `find .templates -name '*.template'`. Some templates contain `{variable}` tokens (e.g. `{project_name}`, `{YYYYMMDD}`) that the setup skill replaces with actual values.

1. Check that all required template files exist and set evidence:
   - `pyproject_toml`: Check `pyproject.toml` exists
   - `readme_md`: Check `README.md` exists
   - `github_workflows_ci_yml`: Check `.github/workflows/ci.yml` exists
   - `license`: Check `LICENSE` exists
   - `tests_unit_main_test_py`: Check `tests/unit/main_test.py` exists
   - `app_directory`: Check `app/` directory exists
2. IF any template files are missing → set evidence to false, exit `missing_files`.
3. Read `template-config.yaml` defaults section.
4. Present the 6 current values to the user based on the assessment:
   - `github_username` — GitHub handle used in URLs and git remote
   - `project_name` — kebab-case repository name (e.g. my-awesome-project)
   - `package_name` — snake_case Python package directory (e.g. my_awesome_project)
   - `project_description` — one sentence describing what the project does
   - `author_name` — author's full name
   - `author_email` — author's email address
5. For each parameter, ask: "Use this value or enter a new one?" Accept default if confirmed.
6. Show summary table:

   | Parameter | Old (default) | New |
   |---|---|---|
   | github_username | ... | ... |
   | project_name | ... | ... |
   | package_name | ... | ... |
   | project_description | ... | ... |
   | author_name | ... | ... |
   | author_email | ... | ... |

   Note: `github_username` will be used in both `pyproject.toml` URLs and `git remote set-url`. Confirm they are correct.
7. Ask the user to confirm before proceeding.
8. Update the defaults section in `template-config.yaml` with confirmed values.
9. Set all template existence evidence to `==true`.
10. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.