# Scientific Research — AI Agent Design

Foundations for the agent architecture, file structure, and context management decisions in this template.

---

### 21. Minimal-Scope Agent Design

| | |
|---|---|
| **Source** | OpenAI. (2024). *Agent definitions*. OpenAI Agents SDK Documentation. https://platform.openai.com/docs/guides/agents/define-agents |
| **Date** | 2024 |
| **Alternative** | Anthropic. (2024). *Building effective agents*. Anthropic Engineering Blog. https://www.anthropic.com/engineering/building-effective-agents |
| **Status** | Confirmed — corrects the belief that subagents should be "lean routing agents" |
| **Core finding** | "Define the smallest agent that can own a clear task. Add more agents only when you need separate ownership, different instructions, different tool surfaces, or different approval policies." The split criterion is ownership boundary, not instruction volume. |
| **Mechanism** | Multiple agents competing to own the same concern create authority conflicts and inconsistent tool access. The right unit is the smallest coherent domain that requires exclusive responsibility. |
| **Where used** | Agent design in `.opencode/agents/*.md` — 5 agents, each owning a distinct domain (PO, system-architect, software-engineer, designer, setup). |

---

### 22. Context Isolation via Subagents

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. https://www.anthropic.com/engineering/claude-code-best-practices |
| **Date** | 2025 |
| **Status** | Confirmed — the primary reason subagents exist is context isolation, not routing |
| **Core finding** | Subagents run in their own context windows and report back summaries, keeping the main conversation clean for implementation. Every file read in a subagent burns tokens in a child window, not the primary window. |
| **Mechanism** | Context window is the primary performance constraint for LLM agents. Investigation tasks rapidly exhaust context if done inline. Delegating to a subagent quarantines that cost; the primary agent receives only the distilled result. A fresh context in the subagent also prevents anchoring bias from prior conversation state. |
| **Where used** | OpenCode `task` tool usage in all agents; `explore` and `general` built-in subagents. |

---

### 23. On-Demand Skill Loading (Context Budget)

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. https://www.anthropic.com/engineering/claude-code-best-practices |
| **Date** | 2025 |
| **Alternative** | OpenCode. (2026). *Agent Skills*. OpenCode Documentation. https://opencode.ai/docs/skills/ |
| **Status** | Confirmed (vendor guidance) — benefit on task completion quality extrapolated from RAG retrieval literature |
| **Core finding** | "CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows only relevant sometimes, use skills instead. Claude loads them on demand without bloating every conversation." Bloated always-loaded files cause Claude to ignore critical instructions. |
| **Mechanism** | Every token in an unconditionally-loaded file competes for attention against the task prompt. Long always-loaded files push important instructions beyond effective attention range, causing silent non-compliance. Skills are injected only when the task calls for them, preserving the primary context budget. |
| **Where used** | `AGENTS.md` carries only shared project conventions and commands; all step-specific workflows live in `.opencode/skills/*.md` and are loaded via the `skill` tool only when the relevant step begins. |

---

### 24. Instruction Conflict Resolution Failure in LLMs

| | |
|---|---|
| **Source** | Geng et al. (2025). Control Illusion: The Failure of Instruction Hierarchies in Large Language Models. AAAI-26. arXiv:2502.15851. https://arxiv.org/abs/2502.15851 |
| **Date** | 2025 |
| **Alternative** | Wallace et al. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv:2404.13208. |
| **Status** | Confirmed — peer-reviewed (AAAI-26), replicated across 6 models |
| **Core finding** | LLMs do not reliably prioritize system-prompt instructions over conflicting instructions from other sources. Resolution is inconsistent and biased by pretraining-derived priors, not by prompt structure or position. |
| **Mechanism** | No structural separation between instruction sources enforces reliable priority at inference time. When the same directive appears in two locations with divergent content, the model selects between them based on statistical priors from pretraining. |
| **Where used** | Justifies single source of truth in `AGENTS.md`: workflow details duplicated across agent files and skills that drift out of sync produce conflicting instructions the model cannot resolve reliably. |

---

### 25. Positional Attention Degradation in Long Contexts

| | |
|---|---|
| **Source** | Liu et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*. arXiv:2307.03172. https://arxiv.org/abs/2307.03172 |
| **Date** | 2023 |
| **Alternative** | McKinnon (2025). arXiv:2511.05850 — effect attenuated for simple retrieval in Gemini 2.5+; persists for multi-hop reasoning. |
| **Status** | Confirmed with caveat — robust for multi-hop reasoning; attenuated for simple retrieval in frontier models (2025–2026) |
| **Core finding** | Performance on tasks requiring retrieval from long contexts follows a U-shaped curve: highest when relevant content is at the beginning or end of the context, degraded when content falls in the middle. |
| **Mechanism** | Transformer attention is not uniform across token positions. Content placed in the middle of a long context receives less attention weight regardless of its relevance. |
| **Where used** | Supports keeping always-loaded files lean. Duplicated workflow detail in always-loaded files increases total context length, pushing other content into lower-attention positions. |

---

### 26. Modular Prompt De-duplication Reduces Interference

| | |
|---|---|
| **Source** | Sharma & Henley (2026). Modular Prompt Optimization. arXiv:2601.04055. https://arxiv.org/abs/2601.04055 |
| **Date** | 2026 |
| **Status** | Partially confirmed — single-agent reasoning benchmarks only; not tested on multi-file agent architectures |
| **Core finding** | Structured prompts with explicit section de-duplication outperform both monolithic prompts and unstructured modular prompts. The mechanism cited is "reducing redundancy and interference between components." |
| **Mechanism** | Redundant content across prompt sections creates competing attention targets. De-duplication concentrates relevant signal in one canonical location per concern. |
| **Where used** | Supports the rule that skills and agent routing files contain no duplication of `AGENTS.md` content or of each other. |

---

### 27. Agent File Architecture — Three-File Separation

| | |
|---|---|
| **Source** | Convergence of entries 23, 24, 25, 26. |
| **Date** | — |
| **Status** | Inferred — no direct A/B test of this architecture exists; supported by convergence of confirmed and partially confirmed findings above |
| **Core finding** | Three distinct failure modes (instruction conflict on drift, positional attention degradation, redundancy interference) converge to produce a three-file split with defined content rules for each. |
| **Mechanism** | Each file runs at a different time and serves a different purpose. Mixing concerns across files reintroduces the failure modes the split is designed to prevent. |
| **Where used** | Structural rule for `AGENTS.md`, `.opencode/agents/*.md`, and `.opencode/skills/*.md`. |

| File | Runs when | Contains | Does NOT contain |
|---|---|---|---|
| `AGENTS.md` | Every session, always loaded | Project conventions, shared commands, formats, standards | Step procedures, role-specific rules, path specs |
| `.opencode/agents/*.md` | When that role is invoked | Role identity, step ownership, skill load instructions, tool permissions, escalation paths | Workflow details, principle lists, path specs, commit formats |
| `.opencode/skills/*.md` | On demand, when that step begins | Full procedural instructions for that step, self-contained | Duplication of `AGENTS.md` content or other skills |

---

### 72. Actor Model — Message-Passing Ownership

| | |
|---|---|
| **Source** | Hewitt, C., Bishop, P., & Steiger, R. (1973). *A universal modular actor formalism for artificial intelligence*. IJCAI. |
| **Date** | 1973 |
| **Status** | Confirmed — foundational for single-ownership agent design |
| **Core finding** | Actors are computational entities that communicate exclusively via asynchronous message passing. Each actor has a single mailbox, processes messages sequentially, and can spawn child actors. No shared state, no direct method calls. |
| **Mechanism** | The Actor Model eliminates race conditions by construction: an actor can only modify its own state. Message passing creates explicit handoff points where ownership transfers. This maps directly to AI agent design where each agent owns a distinct domain and communicates via structured handoffs (e.g., PO → SA → SE → SA → PO). |
| **Where used** | Agent ownership boundaries in `.opencode/agents/*.md`; single-feature-at-a-time WIP limit in `FLOW.md`. |

---

### 73. CSP — Synchronous Communication and Deadlock Freedom

| | |
|---|---|
| **Source** | Hoare, C. A. R. (1978). *Communicating sequential processes*. Communications of the ACM, 21(8), 666–677. |
| **Date** | 1978 |
| **Status** | Confirmed — formal basis for structured handoff protocols |
| **Core finding** | Processes communicate via synchronous channels (rendezvous). A process that tries to send on a channel blocks until the receiver is ready. This explicit synchronization prevents the "lost update" problem. |
| **Mechanism** | CSP's channel-based communication ensures that handoffs are atomic: either both parties are ready (handoff succeeds) or the sender waits (no partial state). Applied to AI workflow design: each step transition in `FLOW.md` is a rendezvous point where the outgoing agent commits state before the incoming agent reads it. |
| **Where used** | Step transition protocol in `FLOW.md` — commit before handoff; session end protocol in `run-session/SKILL.md`. |

---

### 74. Session Types — Protocol Conformance by Construction

| | |
|---|---|
| **Source** | Honda, K. (1993). *Types for dyadic interaction*. CONCUR '93. |
| **Date** | 1993 |
| **Status** | Confirmed — type-safe communication protocols |
| **Core finding** | Session types statically verify that communicating parties follow a prescribed protocol. The type checker ensures send/receive sequences match, preventing protocol violations at compile time. |
| **Mechanism** | Just as session types enforce "send A then receive B then send C", the `FLOW.md` state machine enforces "Step 1 → Step 2 → Step 3 → Step 4 → Step 5". Each state has a defined owner and valid transitions. The auto-detection rules act as a runtime type checker: if the filesystem state doesn't match the expected state, the protocol halts. |
| **Where used** | `FLOW.md` state machine definition; `flow/SKILL.md` auto-detection rules. |

---

### 75. Statecharts — Hierarchical State Machines with History

| | |
|---|---|
| **Source** | Harel, D. (1987). *Statecharts: A visual formalism for complex systems*. Science of Computer Programming, 8(3), 231–274. |
| **Date** | 1987 |
| **Status** | Confirmed — hierarchical states for workflow design |
| **Core finding** | Statecharts extend finite state machines with hierarchy (nested states), orthogonality (parallel regions), and history (return to previous substate). This makes complex systems tractable without state explosion. |
| **Mechanism** | The `FLOW.md` state machine uses hierarchical grouping: Step 3 contains substates [READY], [RED], [GREEN]. The history mechanism maps to interruption recovery: when resuming, auto-detection determines the exact substate without manual tracking. |
| **Where used** | `FLOW.md` state design; `flow/SKILL.md` detection rules for interruption recovery. |

---

### 76. Design by Contract — Preconditions and Postconditions

| | |
|---|---|
| **Source** | Meyer, B. (1986). *Eiffel: Programming for reusability and extendability*. SIGPLAN Notices, 22(2), 85–94. |
| **Date** | 1986 |
| **Status** | Confirmed — explicit contracts for step boundaries |
| **Core finding** | Software components should specify contracts: preconditions (what must be true before calling), postconditions (what will be true after), and invariants (what remains true). Violations indicate bugs. |
| **Mechanism** | Each `FLOW.md` state has preconditions (detect rules) and postconditions (success/failure transitions). The prerequisites table is a system-level precondition. When preconditions fail, the protocol halts rather than proceeding with invalid state. |
| **Where used** | Prerequisites table in `FLOW.md`; per-step preconditions in `flow/SKILL.md`, `architect/SKILL.md`, `implement/SKILL.md`. |

---

### 77. Petri Nets — Places, Transitions, and Token Flow

| | |
|---|---|
| **Source** | Petri, C. A. (1962). *Kommunikation mit Automaten*. PhD thesis, University of Bonn. |
| **Date** | 1962 |
| **Status** | Confirmed — formal model for concurrent workflow with resource constraints |
| **Core finding** | Petri Nets model systems as places (conditions), transitions (events), and tokens (resources). A transition fires only when all input places have tokens. This naturally models capacity constraints and competition for resources. |
| **Mechanism** | The WIP=1 constraint in `FLOW.md` is a Petri Net place with capacity 1: only one feature token can occupy the "in-progress" place at a time. The transition from [IDLE] to [STEP-1-DISCOVERY] requires the "in-progress" place to be empty (no token). This formalizes the single-feature constraint. |
| **Where used** | WIP limit of 1 in `AGENTS.md` and `FLOW.md`; filesystem-enforced WIP via `docs/features/in-progress/` directory. |

---

## Bibliography

1. Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents
2. Anthropic. (2025). Best practices for Claude Code. https://www.anthropic.com/engineering/claude-code-best-practices
3. Geng et al. (2025). Control Illusion. AAAI-26. arXiv:2502.15851. https://arxiv.org/abs/2502.15851
4. Harel, D. (1987). Statecharts: A visual formalism for complex systems. *Science of Computer Programming*, 8(3), 231–274.
5. Hewitt, C., Bishop, P., & Steiger, R. (1973). A universal modular actor formalism for artificial intelligence. *IJCAI*.
6. Hoare, C. A. R. (1978). Communicating sequential processes. *Communications of the ACM*, 21(8), 666–677.
7. Honda, K. (1993). Types for dyadic interaction. *CONCUR '93*.
8. Liu, N. F. et al. (2023). Lost in the Middle. *TACL*. arXiv:2307.03172. https://arxiv.org/abs/2307.03172
9. McKinnon, R. (2025). arXiv:2511.05850. https://arxiv.org/abs/2511.05850
10. Meyer, B. (1986). Eiffel: Programming for reusability and extendability. *SIGPLAN Notices*, 22(2), 85–94.
11. OpenAI. (2024). Agent definitions. https://platform.openai.com/docs/guides/agents/define-agents
12. OpenCode. (2026). Agent Skills. https://opencode.ai/docs/skills/
13. Petri, C. A. (1962). Kommunikation mit Automaten. PhD thesis, University of Bonn.
14. Sharma, A., & Henley, A. (2026). Modular Prompt Optimization. arXiv:2601.04055. https://arxiv.org/abs/2601.04055
15. Wallace, E. et al. (2024). The Instruction Hierarchy. arXiv:2404.13208.
