---
domain: workflow
tags: [flowr, cli, commands, transitions, evidence, session]
last-updated: 2026-05-01
---

# Flowr Operations

## Key Takeaways

- Use `python -m flowr check <flow> <state>` to inspect a state's attrs, owner, skills, and transitions at state entry.
- Use `python -m flowr next <flow> <state> --evidence key=value` to see which transitions pass given your evidence.
- Use `python -m flowr transition <flow> <state> <trigger> --evidence key=value` to advance to the next state.
- Use `python -m flowr check <flow> <state> <target>` to see the conditions guarding a specific transition.
- Set evidence based on work completed before advancing — guarded transitions will not pass without it.
- Always activate the virtual environment first: `source .venv/bin/activate`.

## Concepts

**State Entry**: Before starting work, inspect the current state to confirm the owner, skills, input artifacts, output artifacts, and available transitions.

**Evidence**: Some transitions are guarded by conditions (e.g., `feature_accepted: ==ACCEPTED`, `all_ids_have_stubs: ==true`). Set evidence with `--evidence key=value` when advancing. If a transition is guarded and evidence is not set, the transition will fail.

**Choosing a Path**: After completing work, use `next` with your evidence to see which transitions are available. Choose the path that matches your work outcome. Do not guess transition names — check first.

**Flow File Resolution**: Flow files are in `.flowr/flows/`. The flow name matches the YAML file stem (e.g., `planning-flow` for `.flowr/flows/planning-flow.yaml`).

## Content

### Command Reference

All commands require the virtual environment: `source .venv/bin/activate`

| Command | Purpose | Example |
|---------|---------|---------|
| `python -m flowr validate <flow>.yaml` | Validate a flow definition | `python -m flowr validate .flowr/flows/planning-flow.yaml` |
| `python -m flowr validate` | Validate all flows | `python -m flowr validate` (no arg) |
| `python -m flowr states <flow>.yaml` | List all states in a flow | `python -m flowr states .flowr/flows/planning-flow.yaml` |
| `python -m flowr check <flow>.yaml <state>` | Show state attrs, owner, skills, and transitions | `python -m flowr check .flowr/flows/planning-flow.yaml feature-selection` |
| `python -m flowr check <flow>.yaml <state> <target>` | Show conditions for a specific transition target | `python -m flowr check .flowr/flows/planning-flow.yaml feature-breakdown bdd-features` |
| `python -m flowr next <flow>.yaml <state>` | Show which transitions are available (unguarded always shown) | `python -m flowr next .flowr/flows/planning-flow.yaml feature-selection` |
| `python -m flowr next <flow>.yaml <state> --evidence key=value` | Show which transitions pass given evidence | `python -m flowr next .flowr/flows/planning-flow.yaml feature-breakdown --evidence independent=true` |
| `python -m flowr transition <flow>.yaml <state> <trigger>` | Compute next state for a trigger | `python -m flowr transition .flowr/flows/planning-flow.yaml feature-selection selected` |
| `python -m flowr transition <flow>.yaml <state> <trigger> --evidence key=value` | Advance with evidence | `python -m flowr transition .flowr/flows/planning-flow.yaml feature-breakdown done --evidence independent=true valuable=true` |
| `python -m flowr mermaid <flow>.yaml` | Export flow as Mermaid diagram | `python -m flowr mermaid .flowr/flows/planning-flow.yaml` |

### Workflow Pattern

Every state follows the same pattern:

1. **Enter**: `python -m flowr check <flow> <state>` — confirm owner, skills, attrs, and transitions.
2. **Work**: Execute the skill, reading `in` artifacts and writing `out` artifacts.
3. **Evidence**: Set any evidence required by guarded transitions based on work completed.
4. **Choose**: `python -m flowr next <flow> <state> --evidence key=value` — see which paths are available.
5. **Advance**: `python -m flowr transition <flow> <state> <trigger> --evidence key=value` — move to the next state.

### Session Protocol Integration

- The `owner` field from `check` output determines which agent to dispatch to (PO → product-owner, SE → software-engineer, SA → system-architect, DE → domain-expert, R → reviewer, Design Agent → design-agent, Setup Agent → setup-agent).
- The `skills` field lists which skills to load and execute.
- The `in` and `out` fields define the artifact contract — what you may read and what you may write.
- Do not skip the check step or guess transitions. Always verify the current state before starting work.

## Related

- [[workflow/flowr-spec]]