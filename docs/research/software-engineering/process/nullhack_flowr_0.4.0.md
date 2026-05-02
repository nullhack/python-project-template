# flowr 0.4.0 — Non-Deterministic State Machine Engine for Workflow Kneading

## Citation

nullhack/flowr. (2026). flowr v0.4.0. GitHub. https://github.com/nullhack/flowr

## Source Type

Software Release / Implementation

## Method

Implementation Analysis (source code review)

## Verification Status

Verified

## Confidence

High

## Key Insight

flowr 0.4.0 adds session management, configuration resolution, and flow name resolution — turning flowr from a stateless inspection tool into a workflow engine that tracks and persists agent progress through flow states.

## Core Findings

1. **Session Management**: New `session` subcommand group (`init`, `show`, `set-state`, `list`) persists workflow progress as YAML files in `.flowr/sessions/`. Sessions track current flow, state, call stack (for subflow nesting), and params. Atomic writes prevent corruption.

2. **Session-Aware Commands**: `check`, `next`, and `transition` accept `--session <name>` to resolve flow/state from the session instead of requiring explicit arguments. `transition --session` auto-updates the session after transition — eliminates manual YAML editing.

3. **Subflow Call Stack**: Sessions maintain a `stack` of `SessionStackFrame(flow, state)` entries. Entering a subflow pushes a frame; exiting pops it. Provides proper return-to-parent semantics.

4. **Pyproject.toml Configuration**: `[tool.flowr]` section in `pyproject.toml` configures `flows_dir`, `sessions_dir`, `default_flow`, and `default_session`. CLI flags override pyproject.toml which overrides defaults. `flowr config` command shows resolved configuration with source tracking.

5. **Flow Name Resolution**: Commands accept short flow names (e.g., `architecture-flow`) instead of requiring full file paths (e.g., `.flowr/flows/architecture-flow.yaml`). Resolution checks file path first, then searches the configured flows directory.

6. **Named Condition Groups**: States define `conditions:` blocks with reusable condition sets. Transitions reference them by name in `when:` clauses instead of inlining all conditions. Unknown references are validation errors.

7. **Enhanced Validation**: New validators: subflow contract checking (parent `next` keys must match child `exits`), cross-flow cycle detection (DFS), condition reference validation (named groups must exist), unused condition group warnings (SHOULD level). Violations have MUST/SHOULD severity.

8. **Condition Operators**: Expanded beyond `==` to include `!=`, `>=`, `<=`, `>`, `<`, and `~=` (approximate numeric match within 5%). Numeric portion extracted from both condition and evidence before comparison.

9. **JSON Evidence Input**: `--evidence-json` flag accepts evidence as a JSON object alongside `--evidence key=value` pairs.

10. **Flow-Level `attrs` and `params`**: Flows declare arbitrary metadata in `attrs` and typed parameters in `params` (with optional defaults).

## Mechanism

flowr operates as a thin enforcement layer over YAML-defined state machines. Flows are immutable once loaded. Sessions are the mutable runtime state, persisted as YAML with atomic writes (temp-file-then-rename). The engine validates flow definitions at load time (MUST/SHOULD severity), resolves guard conditions from named groups, and tracks subflow entry/exit via a call stack. Configuration resolution follows CLI > pyproject.toml > defaults priority.

## Relevance

flowr is the workflow engine that powers temple8's flow-based delivery system. The 0.4.0 additions make the golden rules enforceable by tooling: session management replaces manual session editing (Rule 1), flow name resolution simplifies CLI usage, and configuration from pyproject.toml removes hardcoded paths.

## Related Research

Connects to finite state machine theory (Harel, 1987), workflow management patterns (Russell et al., 2006), and the temple8 knowledge files on flowr specification and operations.