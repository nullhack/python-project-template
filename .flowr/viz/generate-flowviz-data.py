#!/usr/bin/env python3
"""Generate FlowViz data bundle from flowr YAML.

Outputs a single JS file (`.flowr/viz/data.js`) that defines `window.FLOWVIZ_DATA`.
This is intentionally `file://` friendly: the HTML can be opened directly
without needing a local web server (no fetch/XHR).
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
FLOWS_DIR = ROOT / ".flowr" / "flows"
OUT_DIR = ROOT / ".flowr" / "viz"
OUT_FILE = OUT_DIR / "data.js"


def _title_case(s: str) -> str:
    return " ".join([p.capitalize() for p in s.replace("_", "-").split("-") if p])


def load_flow_yaml(path: Path) -> dict:
    """Load and validate a flowr YAML file."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict) or "flow" not in data:
        raise ValueError(f"Invalid flow YAML: {path}")
    return data


def _flatten_artifacts(artifacts: list | None) -> list[str]:
    if not artifacts:
        return []
    result: list[str] = []
    for item in artifacts:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, dict):
            for doc, sections in item.items():
                if isinstance(sections, list) and sections:
                    for sec in sections:
                        result.append(f"{doc}#{sec}")
                else:
                    result.append(doc)
    return result


def _flatten_attrs(attrs: dict | None) -> dict | None:
    if not attrs:
        return attrs
    flat = {}
    for key, val in attrs.items():
        if key in ("input_artifacts", "edited_artifacts", "output_artifacts"):
            flat[key] = _flatten_artifacts(val)
        else:
            flat[key] = val
    return flat


def _resolve_when(
    when_clause: dict | list | str,
    state_conditions: dict | None,
    state_id: str,
) -> dict[str, str] | None:
    """Resolve a when clause into a flat dict of conditions.

    Mirrors the flowr loader's resolve_when_clause logic but returns
    a plain dict suitable for JSON serialization instead of GuardCondition.
    """
    if isinstance(when_clause, dict):
        return dict(when_clause)

    items = [when_clause] if isinstance(when_clause, str) else list(when_clause)
    resolved: dict[str, str] = {}

    for item in items:
        if isinstance(item, dict):
            resolved.update(item)
        elif isinstance(item, str):
            # Named reference to a condition group on this state
            if not state_conditions or item not in state_conditions:
                raise ValueError(
                    f"Unknown condition reference '{item}' in state '{state_id}'"
                )
            resolved.update(state_conditions[item])

    return resolved or None


def _add_exit_node(
    nodes: list[dict], node_ids: set[str], target: str, exits: list[str]
) -> None:
    """Add an exit node to the graph if not already present."""
    if target not in node_ids:
        nodes.append({"id": target, "type": "exit", "label": _title_case(target)})
        node_ids.add(target)


def _process_dict_transitions(
    nxt: dict,
    st_id: str,
    exits: list[str],
    state_conditions: dict | None,
    nodes: list[dict],
    node_ids: set[str],
    edges: list[dict],
) -> None:
    """Process dict-format transitions (flowr normal form)."""
    for trigger, tgt in nxt.items():
        target: str | None = None
        when: dict[str, str] | None = None

        if isinstance(tgt, str):
            target = tgt
        elif isinstance(tgt, dict):
            target = tgt.get("to")
            raw_when = tgt.get("when")
            if raw_when is not None:
                when = _resolve_when(raw_when, state_conditions, st_id)

        if target is None:
            continue

        edge = {
            "source": st_id,
            "target": target,
            "label": "" if trigger == "default" else str(trigger),
            "kind": "exit" if target in exits else "transition",
        }
        if when:
            edge["when"] = when
        edges.append(edge)
        _add_exit_node(nodes, node_ids, target, exits)


def _process_list_transitions(
    nxt: list,
    st_id: str,
    exits: list[str],
    nodes: list[dict],
    node_ids: set[str],
    edges: list[dict],
) -> None:
    """Process list-format transitions (older/alternate format)."""
    for t in nxt:
        target = t["target"]
        cond = t.get("when", "default")
        edges.append(
            {
                "source": st_id,
                "target": target,
                "label": "" if cond == "default" else str(cond),
                "kind": "exit" if target in exits else "transition",
            }
        )
        _add_exit_node(nodes, node_ids, target, exits)


def build_graph(flow_data: dict) -> dict:
    """Build a visualization graph from flowr YAML data."""
    exits = list(flow_data.get("exits", []) or [])
    states = list(flow_data.get("states", []) or [])

    nodes: list[dict] = []
    edges: list[dict] = []

    for st in states:
        st_id = st["id"]
        is_subflow = "flow" in st
        node_type = "subflow" if is_subflow else "state"

        nodes.append(
            {
                "id": st_id,
                "type": node_type,
                "label": _title_case(st_id),
                "subflow": st.get("flow"),
                "subflowVersion": st.get("flow-version"),
                "attrs": _flatten_attrs(st.get("attrs")) or None,
            }
        )

    for ex in exits:
        nodes.append(
            {
                "id": ex,
                "type": "exit",
                "label": _title_case(ex),
            }
        )

    node_ids = {n["id"] for n in nodes}

    for st in states:
        st_id = st["id"]
        state_conditions = st.get("conditions")
        nxt = st.get("next")
        if not nxt:
            continue

        if isinstance(nxt, dict):
            _process_dict_transitions(
                nxt, st_id, exits, state_conditions, nodes, node_ids, edges
            )
        elif isinstance(nxt, list):
            _process_list_transitions(nxt, st_id, exits, nodes, node_ids, edges)

    return {
        "flow": flow_data["flow"],
        "version": flow_data.get("version", "0.0.0"),
        "exits": exits,
        "nodes": nodes,
        "edges": edges,
    }


def main() -> int:
    """Generate the flowviz data bundle from all flowr YAML files."""
    if not FLOWS_DIR.exists():
        raise SystemExit(f"Missing flows directory: {FLOWS_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    flows: dict[str, dict] = {}
    for p in sorted(FLOWS_DIR.glob("*.yaml")):
        data = load_flow_yaml(p)
        flows[data["flow"]] = build_graph(data)

    bundle = {
        "schema": 1,
        "defaultFlow": "main-flow" if "main-flow" in flows else min(flows),
        "flows": flows,
    }

    js = "window.FLOWVIZ_DATA = " + json.dumps(bundle, indent=2, sort_keys=True) + ";\n"
    OUT_FILE.write_text(js, encoding="utf-8")

    print(f"Wrote {OUT_FILE}")
    print(f"Flows: {', '.join(sorted(flows.keys()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
