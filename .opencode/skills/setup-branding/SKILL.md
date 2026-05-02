---
name: setup-branding
description: "Interview stakeholder to establish brand identity: personality, visual metaphor, wording, and release naming"
---

# Setup Branding

Available knowledge: [[design/identity-design#key-takeaways]], [[requirements/interview-techniques#key-takeaways]]. `in` artifacts: discover and read on demand as needed. 

1. Ask the stakeholder for the project name (if not already set in `pyproject.toml`).
2. Ask for a one-sentence tagline describing what the project does.
3. Ask for 3 personality adjectives that define the brand tone per [[design/identity-design#concepts]]. If the stakeholder cannot articulate them, offer the hue-semantics table in [[design/color-systems#content]] as a prompt.
4. Ask what the project must NOT convey. Record forbidden adjectives or visual metaphors.
5. Ask where the logo will appear most (GitHub avatar, README, npm, terminal, website). Rank by frequency.
6. Ask for 5 peer/competitor project logos. Record what they have in common and how this project should differ.
7. Ask for the release naming convention per [[software-craft/versioning#key-takeaways]]. If not decided, offer the `adjective-noun` pattern and ask for a theme word (e.g., "Greek antiquity", "space", "mythology").
8. Ask for wording rules: words to avoid and words to prefer per [[design/identity-design#concepts]].
9. Write results to `docs/branding.md` using the template at `.templates/docs/branding/branding.md.template`. Fill in Identity, Release Naming, and Wording sections. Leave Visual section with placeholder headings for the next state.
10. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.