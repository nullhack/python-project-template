---
name: setup-assess
description: "Interview user to understand project needs and assess parameters for template setup"
---

# Setup Assess

Load [[requirements/interview-techniques#key-takeaways]] before starting. 

1. Use interview techniques per [[requirements/interview-techniques#concepts]] to understand project context.
2. Start with general questions (Funnel Level 1):
   - What problem will this Python project solve?
   - What kind of Python project is this? (CLI tool, web service, library, data pipeline, etc.)
   - Who will use this project? (just you, your team, public users, other developers)
   - When do you need this project ready for first use?
3. Probe CI workflow needs (Funnel Level 2):
   - Do you want the full CI pipeline (linting, testing, docs, PyPI publishing)?
   - What level of testing do you plan? (basic unit tests, full coverage, property testing)
   - Will you need automated documentation generation?
   - Do you plan to publish this to PyPI or keep it private?
4. Validate parameter constraints (Funnel Level 3):
   - Are there any naming conventions you need to follow? (company standards, existing project family)
   - Do you already know of any major dependencies you'll need? (for context only)
5. Use CIT probes if setup concerns emerge:
   - Tell me about the last Python project you set up — what was tedious about the initial configuration?
   - Describe a time when project setup took longer than expected — what caused the delay?
6. Use Laddering if constraints are unclear:
   - Why is [constraint] important for this project?
   - What would happen if [setup choice] were different?
7. Write assessment summary for confirmation before proceeding.
8. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.