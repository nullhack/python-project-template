/* global d3, dagre, FLOWVIZ_DATA */

(function () {
  "use strict";

  const errEl = document.getElementById("error");
  const metaEl = document.getElementById("flowMeta");
  const crumbsEl = document.getElementById("crumbs");
  const selectEl = document.getElementById("flowSelect");
  const backBtn = document.getElementById("backBtn");
  const fitBtn = document.getElementById("fitBtn");
  const resetBtn = document.getElementById("resetBtn");
  const tooltipEl = document.getElementById("tooltip");
  const svg = d3.select("#svg");

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function showError(msg, err) {
    const detail = err ? `\n${err.stack || err}` : "";
    errEl.textContent = `${msg}${detail}`;
    errEl.style.display = "block";
  }

  function clearError() {
    errEl.style.display = "none";
    errEl.textContent = "";
  }

  function showTooltip(html, event) {
    tooltipEl.innerHTML = html;
    tooltipEl.style.display = "block";
    const ttRect = tooltipEl.getBoundingClientRect();
    let x = event.clientX + 14;
    let y = event.clientY - 10;
    if (x + ttRect.width > window.innerWidth - 8) x = event.clientX - ttRect.width - 14;
    if (y + ttRect.height > window.innerHeight - 8) y = window.innerHeight - ttRect.height - 8;
    tooltipEl.style.left = x + "px";
    tooltipEl.style.top = y + "px";
  }

  function hideTooltip() {
    tooltipEl.style.display = "none";
  }

  if (!window.FLOWVIZ_DATA || !FLOWVIZ_DATA.flows) {
    showError(
      "Missing data bundle. Run: python3 scripts/generate-flowviz-data.py",
    );
    return;
  }

  const flows = FLOWVIZ_DATA.flows;
  const flowNames = Object.keys(flows).sort();

  // Populate selector.
  for (const name of flowNames) {
    const opt = document.createElement("option");
    opt.value = name;
    opt.textContent = name;
    selectEl.appendChild(opt);
  }

  const state = {
    stack: [],
    current: FLOWVIZ_DATA.defaultFlow || flowNames[0],
  };
  state.stack = [state.current];
  selectEl.value = state.current;

  // SVG plumbing: a single zoomable group.
  const defs = svg.append("defs");
  defs
    .append("marker")
    .attr("id", "arrow")
    .attr("viewBox", "0 0 10 10")
    .attr("refX", 9)
    .attr("refY", 5)
    .attr("markerWidth", 7)
    .attr("markerHeight", 7)
    .attr("orient", "auto-start-reverse")
    .append("path")
    .attr("d", "M 0 0 L 10 5 L 0 10 z")
    .attr("fill", "#7a86b8");

  const gRoot = svg.append("g").attr("class", "root");
  const gEdges = gRoot.append("g").attr("class", "edges");
  const gNodes = gRoot.append("g").attr("class", "nodes");

  const zoom = d3
    .zoom()
    .scaleExtent([0.2, 2.5])
    .on("zoom", (event) => {
      gRoot.attr("transform", event.transform);
    });
  svg.call(zoom);

  function nodeSize(n) {
    // Best-effort sizing without measuring text.
    // Rect sizes tuned for readability and dense graphs.
    if (n.type === "exit") return { w: 120, h: 44 };
    if (n.type === "subflow") return { w: 180, h: 56 };
    return { w: 160, h: 52 };
  }

  function wrapLabel(label, maxLen) {
    const words = String(label).split(/\s+/).filter(Boolean);
    const lines = [];
    let line = [];
    let len = 0;
    for (const w of words) {
      const add = (line.length ? 1 : 0) + w.length;
      if (len + add > maxLen && line.length) {
        lines.push(line.join(" "));
        line = [w];
        len = w.length;
      } else {
        line.push(w);
        len += add;
      }
    }
    if (line.length) lines.push(line.join(" "));
    return lines.slice(0, 3);
  }

  function updateCrumbs() {
    crumbsEl.textContent = "";
    state.stack.forEach((name, idx) => {
      if (idx > 0) crumbsEl.appendChild(document.createTextNode("  >  "));
      const isLast = idx === state.stack.length - 1;
      if (isLast) {
        const span = document.createElement("span");
        span.textContent = name;
        span.style.color = "#e6e9f5";
        span.style.fontWeight = "700";
        crumbsEl.appendChild(span);
      } else {
        const a = document.createElement("a");
        a.href = "#";
        a.textContent = name;
        a.addEventListener("click", (e) => {
          e.preventDefault();
          navigateToIndex(idx);
        });
        crumbsEl.appendChild(a);
      }
    });
  }

  function updateMeta(flow) {
    const exits = (flow.exits || []).join(", ") || "(none)";
    metaEl.innerHTML =
      `<div><strong>${flow.flow}</strong> <span style="opacity:0.8">v${flow.version}</span></div>` +
      `<div style="margin-top:6px">Nodes: ${flow.nodes.length}, Edges: ${flow.edges.length}</div>` +
      `<div style="margin-top:6px">Exits: ${exits}</div>`;
  }

  function fitToGraph() {
    const svgNode = svg.node();
    const bbox = gRoot.node().getBBox();
    const width = svgNode.clientWidth || 800;
    const height = svgNode.clientHeight || 600;
    if (!bbox.width || !bbox.height) return;
    const pad = 30;
    const scale = Math.min(
      (width - pad * 2) / bbox.width,
      (height - pad * 2) / bbox.height,
    );
    const tx = (width - bbox.width * scale) / 2 - bbox.x * scale;
    const ty = (height - bbox.height * scale) / 2 - bbox.y * scale;
    svg
      .transition()
      .duration(250)
      .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));
  }

  function resetView() {
    svg
      .transition()
      .duration(200)
      .call(zoom.transform, d3.zoomIdentity);
  }

  function render(flowName) {
    clearError();
    const flow = flows[flowName];
    if (!flow) {
      showError(`Unknown flow: ${flowName}`);
      return;
    }
    updateMeta(flow);
    updateCrumbs();

    // Build dagre graph.
    const g = new dagre.graphlib.Graph({ multigraph: true });
    g.setGraph({
      rankdir: "TB",
      nodesep: 25,
      ranksep: 60,
      edgesep: 8,
      marginx: 20,
      marginy: 20,
    });
    g.setDefaultEdgeLabel(() => ({}));

    for (const n of flow.nodes) {
      const s = nodeSize(n);
      g.setNode(n.id, {
        width: s.w,
        height: s.h,
        ...n,
      });
    }

    // Use stable keys for multi-edges.
    for (let i = 0; i < flow.edges.length; i++) {
      const e = flow.edges[i];
      g.setEdge(e.source, e.target, { ...e, _i: i }, `e${i}`);
    }

    dagre.layout(g);

    const laidNodes = g.nodes().map((id) => ({ id, ...g.node(id) }));
    const laidEdges = g.edges().map((ed) => ({ ...ed, ...g.edge(ed) }));

    const firstState = flow.nodes.find((n) => n.type !== "exit");
    const firstNode = firstState ? laidNodes.find((n) => n.id === firstState.id) : null;

    // Render edges.
    const edgeSel = gEdges.selectAll("g.edge").data(laidEdges, (d) => d.name);
    edgeSel.exit().remove();
    const edgeEnter = edgeSel.enter().append("g").attr("class", "edge");
    edgeEnter.append("path").attr("class", "edge-path");
    const edgesMerged = edgeEnter.merge(edgeSel);

    const line = d3
      .line()
      .x((p) => p.x)
      .y((p) => p.y)
      .curve(d3.curveCatmullRom.alpha(0.5));

    edgesMerged
      .select("path.edge-path")
      .attr("class", (d) => `edge-path ${d.kind === "exit" ? "exit" : ""}`)
      .attr("marker-end", "url(#arrow)")
      .attr("d", (d) => line(d.points || []));

    edgesMerged
      .on("mouseenter", (event, d) => {
        const src = flow.nodes.find((n) => n.id === d.source);
        const tgt = flow.nodes.find((n) => n.id === d.target);
        const srcLabel = src ? esc(src.label || src.id) : esc(d.source);
        const tgtLabel = tgt ? esc(tgt.label || tgt.id) : esc(d.target);
        const label = esc(d.label || "(default)");
        let html = `<div class="tt-title">${srcLabel} → ${tgtLabel}</div>` +
          `<div class="tt-edge"><span class="tt-edge-label">${label}</span> → ${tgtLabel}</div>`;
        if (d.when && Object.keys(d.when).length > 0) {
          const conds = Object.entries(d.when).map(([k, v]) => `${esc(k)}: ${esc(v)}`).join("<br>");
          html += `<div class="tt-attr"><strong>When:</strong><br>${conds}</div>`;
        }
        showTooltip(html, event);
      })
      .on("mousemove", (event) => {
        const ttRect = tooltipEl.getBoundingClientRect();
        let x = event.clientX + 14;
        let y = event.clientY - 10;
        if (x + ttRect.width > window.innerWidth - 8) x = event.clientX - ttRect.width - 14;
        if (y + ttRect.height > window.innerHeight - 8) y = window.innerHeight - ttRect.height - 8;
        tooltipEl.style.left = x + "px";
        tooltipEl.style.top = y + "px";
      })
      .on("mouseleave", hideTooltip);

    // Render nodes.
    const nodeSel = gNodes.selectAll("g.node").data(laidNodes, (d) => d.id);
    nodeSel.exit().remove();
    const nodeEnter = nodeSel
      .enter()
      .append("g")
      .attr("class", (d) => `node ${d.type || "state"}`)
      .style("cursor", (d) => (d.type === "subflow" ? "pointer" : "default"))
      .on("click", (event, d) => {
        if (d.type !== "subflow") return;
        if (!d.subflow || !flows[d.subflow]) return;
        navigateToFlow(d.subflow);
      });

    nodeEnter.append("rect");
    nodeEnter
      .append("text")
      .attr("text-anchor", "middle")
      .attr("dominant-baseline", "middle");

    nodeEnter
      .on("mouseenter", (event, d) => {
        const outEdges = flow.edges.filter((e) => e.source === d.id);
        let html = `<div class="tt-title">${d.label || d.id}</div>`;
        if (d.attrs) {
          const labelMap = {
            description: "Description",
            owner: "Owner",
            input_artifacts: "In",
            edited_artifacts: "Edit",
            output_artifacts: "Out",
          };
          const ordered = ["description", "owner", "input_artifacts", "edited_artifacts", "output_artifacts"];
          const rest = Object.keys(d.attrs).filter((k) => !ordered.includes(k));
          const allKeys = [...ordered, ...rest];
          for (const key of allKeys) {
            if (d.attrs[key] == null) continue;
            const label = labelMap[key] || key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, " ");
            const val = d.attrs[key];
            if (Array.isArray(val) && val.length === 0) continue;
            if (Array.isArray(val)) {
              html += `<div class="tt-attr"><strong>${esc(label)}:</strong><br>${val.map(esc).join("<br>")}</div>`;
            } else {
              html += `<div class="tt-attr"><strong>${esc(label)}:</strong> ${esc(val)}</div>`;
            }
          }
        }
        if (d.subflow) html += `<div class="tt-attr">subflow: ${d.subflow} v${d.subflowVersion || "?"}</div>`;
        if (d.type && !d.attrs) html += `<div class="tt-attr">type: ${d.type}</div>`;
        if (outEdges.length) {
          html += `<div style="margin-top:4px">`;
          for (const e of outEdges) {
            const tgt = flow.nodes.find((n) => n.id === e.target);
            const tgtLabel = tgt ? esc(tgt.label || tgt.id) : esc(e.target);
            const edgeLabel = esc(e.label || "(default)");
            html += `<div class="tt-edge"><span class="tt-edge-label">${edgeLabel}</span> → ${tgtLabel}</div>`;
          }
          html += `</div>`;
        }
        showTooltip(html, event);
      })
      .on("mousemove", (event) => {
        const ttRect = tooltipEl.getBoundingClientRect();
        let x = event.clientX + 14;
        let y = event.clientY - 10;
        if (x + ttRect.width > window.innerWidth - 8) x = event.clientX - ttRect.width - 14;
        if (y + ttRect.height > window.innerHeight - 8) y = window.innerHeight - ttRect.height - 8;
        tooltipEl.style.left = x + "px";
        tooltipEl.style.top = y + "px";
      })
      .on("mouseleave", hideTooltip);
    const nodesMerged = nodeEnter.merge(nodeSel);

    nodesMerged.attr("transform", (d) => `translate(${d.x - d.width / 2},${d.y - d.height / 2})`);

    nodesMerged
      .select("rect")
      .attr("width", (d) => d.width)
      .attr("height", (d) => d.height);

    nodesMerged.select("text").each(function (d) {
      const text = d3.select(this);
      text.selectAll("tspan").remove();
      const maxLen = d.type === "subflow" ? 18 : 16;
      const lines = wrapLabel(d.label || d.id, maxLen);
      const lineHeight = 13;
      const startY = d.height / 2 - ((lines.length - 1) * lineHeight) / 2;
      for (let i = 0; i < lines.length; i++) {
        text
          .append("tspan")
          .attr("x", d.width / 2)
          .attr("y", startY + i * lineHeight)
          .text(lines[i]);
      }
    });

    // Initial state indicator (small grey circle + arrow to first state)
    const startSel = gNodes.selectAll("g.start-node").data(firstNode ? [firstNode] : []);
    startSel.exit().remove();
    const startEnter = startSel.enter().append("g").attr("class", "start-node");
    startEnter.append("circle").attr("class", "outer").attr("r", 8).attr("cx", 0).attr("cy", 0);
    startEnter.append("circle").attr("class", "inner").attr("r", 4).attr("cx", 0).attr("cy", 0);

    const startMerged = startEnter.merge(startSel);
    startMerged.attr("transform", (d) => {
      const cy = d.y - d.height / 2 - 28;
      return `translate(${d.x},${cy})`;
    });

    // Also add the arrow marker line from start circle to first node
    const startEdgeSel = gEdges.selectAll("path.start-edge").data(firstNode ? [firstNode] : []);
    startEdgeSel.exit().remove();
    startEdgeSel.enter().append("path").attr("class", "start-edge")
      .merge(startEdgeSel)
      .attr("d", (d) => {
        const cx = d.x;
        const cy = d.y - d.height / 2 - 20;
        return `M${cx},${cy} L${d.x},${d.y - d.height / 2}`;
      });

    // Initial fit after render.
    fitToGraph();
  }

  function navigateToFlow(flowName) {
    state.current = flowName;
    state.stack.push(flowName);
    selectEl.value = flowName;
    render(flowName);
  }

  function navigateToIndex(idx) {
    state.stack = state.stack.slice(0, idx + 1);
    state.current = state.stack[state.stack.length - 1];
    selectEl.value = state.current;
    render(state.current);
  }

  // UI handlers.
  selectEl.addEventListener("change", () => {
    state.current = selectEl.value;
    state.stack = [state.current];
    render(state.current);
  });

  backBtn.addEventListener("click", () => {
    if (state.stack.length <= 1) return;
    state.stack.pop();
    state.current = state.stack[state.stack.length - 1];
    selectEl.value = state.current;
    render(state.current);
  });
  fitBtn.addEventListener("click", () => fitToGraph());
  resetBtn.addEventListener("click", () => resetView());

  // Boot.
  try {
    render(state.current);
  } catch (e) {
    showError("Failed to render graph.", e);
  }
})();
