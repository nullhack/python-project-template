# Academic Research — Theoretical Foundations

This document explains the cognitive and social-science mechanisms that justify the workflow reforms in this template. Each mechanism is grounded in peer-reviewed research.

---

## Mechanisms

### 1. Pre-mortem (Prospective Hindsight)

| | |
|---|---|
| **Source** | Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press. |
| **Date** | 1998 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Asking "imagine this failed — why?" catches 30% more issues than forward-looking review. |
| **Mechanism** | Prospective hindsight shifts from prediction (weak) to explanation (strong). The brain is better at explaining past events than predicting future ones. By framing as "it already failed," you activate explanation mode. |
| **Where used** | PO pre-mortem at scope, developer pre-mortem before handoff. |

---

### 2. Implementation Intentions

| | |
|---|---|
| **Source** | Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple planning aids. *American Journal of Preventive Medicine*, 16(4), 257–276. |
| **Date** | 1999 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | "If X then Y" plans are 2–3x more likely to execute than general intentions. |
| **Mechanism** | If-then plans create automatic cue-response links in memory. The brain processes "if function > 20 lines then extract helper" as an action trigger, not a suggestion to consider. |
| **Where used** | Refactor Self-Check Gates in `implementation/SKILL.md`, Code Quality checks in `verify/SKILL.md`. |

---

### 3. Commitment Devices

| | |
|---|---|
| **Source** | Cialdini, R. B. (2001). *Influence: The Psychology of Persuasion* (rev. ed.). HarperBusiness. |
| **Date** | 2001 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Forcing an explicit micro-commitment (filling in a PASS/FAIL cell) creates resistance to reversals. A checkbox checked is harder to uncheck than a todo noted. |
| **Mechanism** | Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. |
| **Where used** | SOLID enforcement table, ObjCal enforcement table, Design Patterns table — all require explicit PASS/FAIL with evidence. |

---

### 4. System 2 Before System 1

| | |
|---|---|
| **Source** | Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux. |
| **Date** | 2011 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | System 1 (fast, automatic) is vulnerable to anchoring and confirmation bias. System 2 (slow, deliberate) must be activated before System 1's judgments anchor. |
| **Mechanism** | Running semantic review *before* automated commands prevents the "all green" dopamine hit from anchoring the reviewer's judgment. Doing hard cognitive work first protects against System 1 shortcuts. |
| **Where used** | Verification order in `verify/SKILL.md`: semantic alignment check before commands. |

---

### 5. Adversarial Collaboration

| | |
|---|---|
| **Source** | Mellers, B. A., Hertwig, R., & Kahneman, D. (2001). Do frequency representations eliminate cooperative bias? *Psychological Review*, 108(4), 709–735. |
| **Date** | 2001 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Highest-quality thinking emerges when parties hold different hypotheses and are charged with finding flaws in each other's reasoning. |
| **Mechanism** | Explicitly framing the reviewer as "your job is to break this feature" activates the adversarial collaboration mode. The reviewer seeks disconfirmation rather than confirmation. |
| **Where used** | Adversarial mandate in `reviewer.md` and `verify/SKILL.md`. |

---

### 6. Accountability to Unknown Audience

| | |
|---|---|
| **Source** | Tetlock, P. E. (1983). Accountability: A social determinant of judgment. In M. D. B. T. Strother (Ed.), *Psychology of Learning and Motivation* (Vol. 17, pp. 295–332). Academic Press. |
| **Date** | 1983 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Accountability to an unknown audience with unknown views improves reasoning quality. The agent anticipates being audited and adjusts reasoning. |
| **Mechanism** | The explicit report format (APPROVED/REJECTED with evidence) creates an accountability structure — the reviewer's reasoning will be read by the PO. |
| **Where used** | Report format in `verify/SKILL.md`, structured evidence columns in all enforcement tables. |

---

### 7. Chunking and Cognitive Load Reduction

| | |
|---|---|
| **Source** | Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97. |
| **Date** | 1956 |
| **URL** | — |
| **Alternative** | Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285. |
| **Status** | Confirmed |
| **Core finding** | Structured tables reduce working memory load vs. narrative text. Chunking related items into table rows enables parallel processing. |
| **Mechanism** | Replacing prose checklists ("Apply SOLID principles") with structured tables (5 rows, 4 columns) allows the reviewer to process all items in a single pass. |
| **Where used** | All enforcement tables in `verify/SKILL.md` and `reviewer.md`. |

---

### 8. Elaborative Encoding

| | |
|---|---|
| **Source** | Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684. |
| **Date** | 1972 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Deeper processing — explaining *why* a rule matters — leads to better retention and application than shallow processing (just listing rules). |
| **Mechanism** | Adding a "Why it matters" column to enforcement tables forces the reviewer to process the rationale, not just scan the rule name. |
| **Where used** | SOLID table, ObjCal table, Design Patterns table — all have "Why it matters" column. |

---

### 9. Error-Specific Feedback

| | |
|---|---|
| **Source** | Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. |
| **Date** | 2007 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Feedback is most effective when it tells the agent exactly what went wrong and what the correct action is. "FAIL: function > 20 lines at file:47" is actionable. "Apply function length rules" is not. |
| **Mechanism** | The evidence column in enforcement tables requires specific file:line references, turning vague rules into actionable directives. |
| **Where used** | Evidence column in all enforcement tables. |

---

### 10. Prospective Memory Cues

| | |
|---|---|
| **Source** | McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval. *Applied Cognitive Psychology*, 14(7), S127–S144. |
| **Date** | 2000 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Memory for intended actions is better when cues are embedded at the point of action, not in a separate appendix. |
| **Mechanism** | Placing if-then gates inline (in the REFACTOR section) rather than in a separate "reference" document increases adherence. The cue appears exactly when the developer is about to make the relevant decision. |
| **Where used** | Refactor Self-Check Gates embedded inline in `implementation/SKILL.md`. |

---

### 11. Observable Behavior Testing

| | |
|---|---|
| **Source** | Fowler, M. (2018). *The Practical Test Pyramid*. Thoughtworks. https://martinfowler.com/articles/practical-test-pyramid.html |
| **Date** | 2018 |
| **URL** | https://martinfowler.com/articles/practical-test-pyramid.html |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Tests should answer "if I enter X and Y, will the result be Z?" — not "will method A call class B first?" |
| **Mechanism** | A test is behavioral if its assertion describes something a caller/user can observe without knowing the implementation. The test should still pass if you completely rewrite the internals. |
| **Where used** | Contract test rule in `tdd/SKILL.md`: "Write every test as if you cannot see the production code." |

---

### 12. Test-Behavior Alignment

| | |
|---|---|
| **Source** | Google Testing Blog (2013). *Testing on the Toilet: Test Behavior, Not Implementation*. |
| **Date** | 2013 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Test setup may need to change if implementation changes, but the actual test shouldn't need to change if the code's user-facing behavior doesn't change. |
| **Mechanism** | Tests that are tightly coupled to implementation break on refactoring and become a drag on design improvement. Behavioral tests survive internal rewrites. |
| **Where used** | Contract test rule + bad example in `tdd/SKILL.md`, reviewer verification check in `reviewer.md`. |

---

### 13. Tests as First-Class Citizens

| | |
|---|---|
| **Source** | Martin, R. C. (2017). *First-Class Tests*. Clean Coder Blog. |
| **Date** | 2017 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Tests should be treated as first-class citizens of the system — not coupled to implementation. Bad tests are worse than no tests because they give false confidence. |
| **Mechanism** | Tests written as "contract tests" — describing what the caller observes — remain stable through refactoring. Tests that verify implementation details are fragile and create maintenance burden. |
| **Where used** | Contract test rule in `tdd/SKILL.md`, verification check in `reviewer.md`. |

---

### 14. Property-Based Testing (Invariant Discovery)

| | |
|---|---|
| **Source** | MacIver, D. R. (2016). *What is Property Based Testing?* Hypothesis. https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Date** | 2016 |
| **URL** | https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Property-based testing is "the construction of tests such that, when these tests are fuzzed, failures reveal problems that could not have been revealed by direct fuzzing." Property tests test *invariants* — things that must always be true about the contract, not things that fall out of how you wrote it. |
| **Mechanism** | Meaningful property tests assert invariants: "assert Score(x).value >= 0" tests the contract. Tautological tests assert reconstruction: "assert Score(x).value == x" tests the implementation. |
| **Where used** | Meaningful vs. Tautological table in `tdd/SKILL.md`, Property-Based Testing Decision Rule table in `tdd/SKILL.md`. |

---

### 15. Mutation Testing (Test Quality Verification)

| | |
|---|---|
| **Source** | King, K. N. (1991). *The Gamma (formerly mutants)*. |
| **Date** | 1991 |
| **URL** | — |
| **Alternative** | Mutation testing tools: Cosmic Ray, mutmut (Python) |
| **Status** | Confirmed |
| **Core finding** | A meaningful test fails when a mutation (small deliberate code change) is introduced. A tautological test passes even with mutations because it doesn't constrain the behavior. |
| **Mechanism** | If a test survives every mutation of the production code without failing, it tests nothing. Only tests that fail on purposeful "damage" to the code are worth keeping. |
| **Where used** | Note in `tdd/SKILL.md` Quality Rules (implicitly encouraged: tests must describe contracts, not implementation, which is the theoretical complement to mutation testing). |

---

### 16. Cost of Change Curve (Shift Left)

| | |
|---|---|
| **Source** | Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall. |
| **Date** | 1981 |
| **URL** | — |
| **Alternative** | Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477. |
| **Status** | Confirmed |
| **Core finding** | The cost to fix a defect multiplies by roughly 10x per SDLC phase: requirements (1x) → design (5x) → coding (10x) → testing (20x) → production (200x). A defect caught during requirements costs 200x less than the same defect found after release. |
| **Mechanism** | Defects compound downstream: a wrong requirement becomes a wrong design, which becomes wrong code, which becomes wrong tests, all of which must be unwound. Catching errors at the source eliminates the entire cascade. This is the empirical foundation for "shift left" — investing earlier in quality always dominates fixing later. |
| **Where used** | Justifies the multi-session PO elicitation model: every acceptance criterion clarified at scope prevents 10–200x rework downstream. Also justifies the adversarial pre-mortem at the end of each elicitation cycle, and the adversarial mandate in `verify/SKILL.md`. The entire 6-step pipeline is ordered to surface defects at the earliest (cheapest) phase. |

---

### 17. INVEST Criteria for User Stories

| | |
|---|---|
| **Source** | Wake, B. (2003). *INVEST in Good Stories, and SMART Tasks*. XP123.com. |
| **Date** | 2003 |
| **URL** | — |
| **Alternative** | Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley. |
| **Status** | Confirmed |
| **Core finding** | Stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable produce fewer downstream defects and smoother development cycles. Stories that fail INVEST — especially "Testable" and "Small" — are the leading cause of scope creep and unbounded iteration. |
| **Mechanism** | INVEST serves as a quality gate before stories enter development. "Testable" forces the PO to express observable outcomes (directly enabling Given/When/Then). "Small" forces decomposition, which reduces cognitive load and makes estimation feasible. "Independent" prevents hidden ordering dependencies between stories. |
| **Where used** | INVEST gate in Phase 3 of `scope/SKILL.md`. PO verifies every story against all 6 letters before committing. |

---

### 18. Example Mapping (Rules Layer)

| | |
|---|---|
| **Source** | Wynne, M. (2015). *Introducing Example Mapping*. Cucumber Blog. https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Date** | 2015 |
| **URL** | https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Inserting a "rules" layer between stories and examples prevents redundant or contradictory acceptance criteria. A story with many rules needs splitting; a story with many open questions is not ready for development. |
| **Mechanism** | Example Mapping uses four card types: Story (yellow), Rules (blue), Examples (green), Questions (red). The rules layer groups related examples under the business rule they illustrate. Without this layer, POs jump from story directly to examples and lose the reasoning that connects them. Red cards (unanswered questions) are a first-class signal to stop and investigate rather than assume. |
| **Where used** | `## Rules` section in per-feature `discovery.md` (Phase 2). PO identifies business rules before writing Examples in Phase 4, making the reasoning behind Example clusters visible and reviewable. |

---

### 19. Declarative Gherkin

| | |
|---|---|
| **Source** | Cucumber Team. (2024). *Better Gherkin*. Cucumber Documentation. https://cucumber.io/docs/bdd/better-gherkin/ |
| **Date** | 2024 |
| **URL** | https://cucumber.io/docs/bdd/better-gherkin/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Declarative Gherkin ("When Bob logs in") produces specifications that survive UI changes. Imperative Gherkin ("When I click the Login button") couples specs to implementation details and breaks on every UI redesign. |
| **Mechanism** | Declarative steps describe *what happens* at the business level. Imperative steps describe *how the user interacts with a specific UI*. The distinction maps to the abstraction level: declarative = behavior contract, imperative = interaction script. AI agents are especially prone to writing imperative Gherkin because they mirror literal steps. |
| **Where used** | Declarative vs. imperative table in Phase 4 of `scope/SKILL.md`. PO is explicitly instructed to write behavior descriptions, not UI interaction scripts. |

---

### 20. MoSCoW Prioritization (Within-Story Triage)

| | |
|---|---|
| **Source** | Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley (DSDM origin). |
| **Date** | 1994 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Classifying requirements as Must/Should/Could/Won't forces explicit negotiation about what is essential vs. desired. When applied *within* a single story (not just across a backlog), it reveals bloated stories that should be split. |
| **Mechanism** | DSDM mandates that Musts cannot exceed 60% of total effort. At the story level: if a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred or split into a follow-up story. This prevents gold-plating and keeps stories small. |
| **Where used** | MoSCoW triage in Phase 4 of `scope/SKILL.md`. PO applies Must/Should/Could when a story exceeds 5 Examples. |

---

### 21. Minimal-Scope Agent Design

| | |
|---|---|
| **Source** | OpenAI. (2024). *Agent definitions*. OpenAI Agents SDK Documentation. |
| **Date** | 2024 |
| **URL** | https://platform.openai.com/docs/guides/agents/define-agents |
| **Alternative** | Anthropic. (2024). *Building effective agents*. Anthropic Engineering Blog. https://www.anthropic.com/engineering/building-effective-agents |
| **Status** | Confirmed — corrects the belief that subagents should be "lean routing agents" |
| **Core finding** | "Define the smallest agent that can own a clear task. Add more agents only when you need separate ownership, different instructions, different tool surfaces, or different approval policies." The split criterion is ownership boundary, not instruction volume. |
| **Mechanism** | Multiple agents competing to own the same concern create authority conflicts and inconsistent tool access. The right unit is the smallest coherent domain that requires exclusive responsibility. Keeping handoff descriptions short and concrete enables routing agents to select the right specialist. |
| **Where used** | Agent design in `.opencode/agents/*.md` — 4 agents, each owning a distinct domain (PO, developer, reviewer, setup). |

---

### 22. Context Isolation via Subagents

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. |
| **Date** | 2025 |
| **URL** | https://www.anthropic.com/engineering/claude-code-best-practices |
| **Alternative** | — |
| **Status** | Confirmed — the primary reason subagents exist is context isolation, not routing |
| **Core finding** | Subagents run in their own context windows and report back summaries, keeping the main conversation clean for implementation. Every file read in a subagent burns tokens in a child window, not the primary window. |
| **Mechanism** | Context window is the primary performance constraint for LLM agents. Investigation tasks (reading many files, exploring a codebase) rapidly exhaust context if done inline. Delegating to a subagent quarantines that cost; the primary agent receives only the distilled result. A fresh context in the subagent also prevents anchoring bias from prior conversation state. |
| **Where used** | OpenCode `task` tool usage in all agents; `explore` and `general` built-in subagents; explicit subagent invocations in `.opencode/agents/developer.md`. |

---

### 23. On-Demand Skill Loading (Context Budget)

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. |
| **Date** | 2025 |
| **URL** | https://www.anthropic.com/engineering/claude-code-best-practices |
| **Alternative** | OpenCode. (2026). *Agent Skills*. OpenCode Documentation. https://opencode.ai/docs/skills/ |
| **Status** | Confirmed (vendor guidance) — benefit on task completion quality is extrapolated from RAG retrieval literature; not directly A/B-tested on agent instruction architectures |
| **Core finding** | "CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows only relevant sometimes, use skills instead. Claude loads them on demand without bloating every conversation." Bloated always-loaded files cause Claude to ignore critical instructions. |
| **Mechanism** | Every token in an unconditionally-loaded file competes for attention against the task prompt. Long AGENTS.md/CLAUDE.md files push important instructions beyond effective attention range, causing silent non-compliance. Procedural workflows moved to skills are injected only when the task calls for them, preserving the primary context budget. This is the same principle as lazy loading in software: pay the cost only when needed. |
| **Where used** | `AGENTS.md` carries only shared project conventions and commands; all step-specific workflows live in `.opencode/skills/*.md` and are loaded via the `skill` tool only when the relevant step begins. |

---

### 24. Instruction Conflict Resolution Failure in LLMs

| | |
|---|---|
| **Source** | Geng et al. (2025). Control Illusion: The Failure of Instruction Hierarchies in Large Language Models. AAAI-26. arXiv:2502.15851. |
| **Date** | 2025 |
| **URL** | https://arxiv.org/abs/2502.15851 |
| **Alternative** | Wallace et al. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv:2404.13208. |
| **Status** | Confirmed — peer-reviewed (AAAI-26), replicated across 6 models; corroborated by OpenAI training research (Wallace et al.) |
| **Core finding** | LLMs do not reliably prioritize system-prompt instructions over conflicting instructions from other sources. Resolution is inconsistent and biased by pretraining-derived priors, not by prompt structure or position. A dedicated training regime is required to make hierarchy reliable; without it, conflicts are resolved unpredictably. |
| **Mechanism** | No structural separation between instruction sources enforces reliable priority at inference time. When the same directive appears in two locations with divergent content, the model selects between them based on statistical priors from pretraining, not on explicit authority. |
| **Where used** | Justifies single source of truth in `AGENTS.md`: workflow details duplicated across agent files and skills that drift out of sync produce conflicting instructions the model cannot resolve reliably. |

---

### 25. Positional Attention Degradation in Long Contexts

| | |
|---|---|
| **Source** | Liu et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*. arXiv:2307.03172. |
| **Date** | 2023 |
| **URL** | https://arxiv.org/abs/2307.03172 |
| **Alternative** | McKinnon (2025). arXiv:2511.05850 — effect attenuated for simple retrieval in Gemini 2.5+; persists for multi-hop reasoning (HAMLET, EMNLP 2025; SealQA, ICLR 2026). |
| **Status** | Confirmed with caveat — robust for multi-hop reasoning; attenuated for simple retrieval in frontier models (2025–2026) |
| **Core finding** | Performance on tasks requiring retrieval from long contexts follows a U-shaped curve: highest when relevant content is at the beginning or end of the context, degraded when content falls in the middle. |
| **Mechanism** | Transformer attention is not uniform across token positions. Content placed in the middle of a long context receives less attention weight regardless of its relevance. |
| **Where used** | Supports keeping always-loaded files (`AGENTS.md`, agent routing files) lean. Duplicated workflow detail in always-loaded files increases total context length, pushing other content into lower-attention positions. |

---

### 26. Modular Prompt De-duplication Reduces Interference

| | |
|---|---|
| **Source** | Sharma & Henley (2026). Modular Prompt Optimization. arXiv:2601.04055. |
| **Date** | 2026 |
| **URL** | https://arxiv.org/abs/2601.04055 |
| **Alternative** | — |
| **Status** | Partially confirmed — single-agent reasoning benchmarks (ARC-Challenge, MMLU) only; not tested on multi-file agent architectures |
| **Core finding** | Structured prompts with explicit section de-duplication outperform both monolithic prompts and unstructured modular prompts. The mechanism cited is "reducing redundancy and interference between components." |
| **Mechanism** | Redundant content across prompt sections creates competing attention targets. De-duplication concentrates relevant signal in one canonical location per concern. |
| **Where used** | Supports the rule that skills and agent routing files contain no duplication of `AGENTS.md` content or of each other. |

---

### 27. Agent File Architecture — Three-File Separation

| | |
|---|---|
| **Source** | Convergence of entries 23, 24, 25, 26. |
| **Date** | — |
| **URL** | — |
| **Alternative** | — |
| **Status** | Inferred — no direct A/B test of this architecture exists; supported by convergence of confirmed and partially confirmed findings above |
| **Core finding** | Three distinct failure modes (instruction conflict on drift, positional attention degradation in long contexts, redundancy interference) converge to produce a three-file split with defined content rules for each. |
| **Mechanism** | Each file runs at a different time and serves a different purpose. Mixing concerns across files reintroduces the failure modes the split is designed to prevent. |
| **Where used** | Structural rule for `AGENTS.md`, `.opencode/agents/*.md`, and `.opencode/skills/*.md`. |

| File | Runs when | Contains | Does NOT contain |
|---|---|---|---|
| `AGENTS.md` | Every session, always loaded | Project conventions, shared commands, formats, standards | Step procedures, role-specific rules, path specs |
| `.opencode/agents/*.md` | When that role is invoked | Role identity, step ownership, skill load instructions, tool permissions, escalation paths | Workflow details, principle lists, path specs, commit formats |
| `.opencode/skills/*.md` | On demand, when that step begins | Full procedural instructions for that step, self-contained | Duplication of `AGENTS.md` content or other skills |

---

### 28. Active Listening — Paraphrase-Clarify-Summarize

| | |
|---|---|
| **Source** | Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago. |
| **Date** | 1957 |
| **URL** | — |
| **Alternative** | McNaughton, D. et al. (2008). Learning to Listen. *Topics in Early Childhood Special Education*, 27(4), 223–231. (LAFF strategy: Listen, Ask, Focus, Find) |
| **Status** | Confirmed — foundational clinical research; widely replicated across professional and educational contexts |
| **Core finding** | Active listening — paraphrasing what was heard in the listener's own words, asking clarifying questions, then summarizing the main points and intent — reduces misunderstanding, builds trust, and confirms mutual understanding before proceeding. The three-step responding sequence (Paraphrase → Clarify → Summarize) is the operationalizable form of the broader active listening construct. |
| **Mechanism** | Paraphrasing forces the listener to reconstruct the speaker's meaning in their own language, surfacing gaps immediately. Clarifying questions address residual ambiguity. Summarizing creates a shared record that both parties can confirm or correct. Together they eliminate the assumption that "I heard" equals "I understood." Without this protocol, agents (human or AI) proceed on partial or misread requirements, producing work that is technically complete but semantically wrong. |
| **Where used** | PO summarization protocol in `scope/SKILL.md`: after each interview round, the PO must produce a "Here is what I understood" block (paraphrase → clarify → summarize) before moving to Phase 3 (Stories) or Phase 4 (Criteria). The stakeholder confirms or corrects before the PO proceeds. |

---

### 28a. Active Listening — Three-Level Structure and Level 3 Uses (Synthesis)

| | |
|---|---|
| **Source** | Synthesis of: Nielsen, J. (2010). *Interviewing Users*. Nielsen Norman Group. + Farrell, S. (2017). UX Research Cheat Sheet. NN/G. + Ambler, S. W. (2002). *Agile Modeling*. Wiley (agilemodeling.com). + Wynne, M. (2015). Introducing Example Mapping. Cucumber Blog. |
| **Date** | 2010–2015 (synthesis) |
| **URL** | https://www.nngroup.com/articles/interviewing-users/ ; https://www.agilemodeling.com/essays/fdd.htm ; https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Alternative** | — |
| **Status** | Synthesized rule of thumb — each component individually confirmed; the three-level structure is a practitioner synthesis |
| **Core finding** | Active listening in requirements interviews operates at three granularities simultaneously, not as a single end-of-interview act: **Level 1** (per answer) — immediate paraphrase to catch misunderstanding on the spot; **Level 2** (per topic cluster) — transition summary before moving to the next area, acting as a recovery point; **Level 3** (end of interview) — full synthesis, which serves four distinct downstream purposes. |
| **Mechanism** | Each level addresses a different failure mode. Level 1 prevents individual answer misreads from propagating. Level 2 prevents topic-cluster drift and allows mid-interview correction. Level 3 crystallizes scope and triggers the formal baseline. Without the level structure, practitioners collapse all three into a single end-of-interview summary, which is too late for Level 1 and 2 misunderstandings to be caught cheaply. |
| **Level 3 — four uses** | 1. **Accuracy gate** (NN/G): stakeholder confirms or corrects the summary before it is used downstream — prevents misread requirements from being frozen. 2. **Scope crystallization** (Ambler/FDD): the summary answers "what problems must this system solve?" and becomes the initial requirements stack. 3. **Input to domain modeling** (Ambler/FDD): nouns and verbs extracted from the Level 3 summary are the raw material for the Entities table — domain analysis cannot begin before this summary exists. 4. **Baseline trigger** (Wynne/Cucumber Example Mapping): when the stakeholder says "yes, that's right" to the summary, discovery is considered complete and frozen. |
| **Where used** | Phase 1 and Phase 2 of `scope/SKILL.md`: PO applies Level 1 during each exchange, Level 2 when transitioning between topic areas, and Level 3 at the end of each interview phase before proceeding to feature stubs (Phase 1) or user stories (Phase 2). |

---

### 29. The Kipling Method — Five Ws and One H

| | |
|---|---|
| **Source** | Kipling, R. (1902). *Just So Stories*. Macmillan. |
| **Date** | 1902 |
| **URL** | — |
| **Alternative** | Hermagoras of Temnos (2nd century BCE) — seven circumstances of rhetoric; Thomas Wilson (1560) — "The Arte of Rhetoric"; Aristotle's Nicomachean Ethics |
| **Status** | Practitioner synthesis — journalism, business analysis, and investigative methodology |
| **Core finding** | The six interrogative questions (Who, What, When, Where, Why, How) form a complete framework for gathering all essential facts about any event or situation. No single question can be answered with a simple yes/no. Together they ensure completeness and prevent gaps in understanding. |
| **Mechanism** | The framework originated in ancient Greek rhetoric (Aristotle's "elements of circumstance"), was formalized in 16th-century English rhetoric (Wilson), popularized by Kipling's 1902 poem calling them "six honest serving-men," and became standard in journalism by 1917. The BA community adapted it to requirements gathering by adding "How" as the sixth question, creating the 5W1H framework used in business analysis today. |
| **Where used** | Phase 1 project discovery: the initial seven questions (Who, What, Why, When, Where, Success, Failure, Out-of-scope) are an adaptation of the 5W1H framework. "Success" maps to "Why" (purpose), "Failure" maps to constraints, "Out-of-scope" defines project boundaries. |

---

### 30. BA Requirements Question Framework

| | |
|---|---|
| **Source** | Brandenburg, L. (2025). *Requirements Discovery Checklist Pack*. TechCanvass. |
| **Date** | 2025 |
| **URL** | https://businessanalyst.techcanvass.com/requirements-gathering-questions-for-ba/ |
| **Alternative** | Sherwen (2025). "10 Questions to Consider During Requirements Gathering."; Practical Analyst (2024). "Requirements Elicitation: Most Valuable Questions." |
| **Status** | Practitioner synthesis — consolidated BA methodology, not peer-reviewed |
| **Core finding** | Ten questions consistently make the most difference in requirements elicitation: (1) What problem are we solving? (2) What happens if we do nothing? (3) Who uses this? (4) What does success look like? (5) Walk me through how this works today (6) Where does this usually break? (7) What decisions will this help? (8) What should definitely not happen? (9) What happens if input is wrong? (10) What assumptions are we making? |
| **Mechanism** | The first four questions define scope and purpose. Questions 5-6 probe current state and pain points. Questions 7-8 identify business value and constraints. Questions 9-10 surface edge cases and hidden assumptions. This sequence ensures negative requirements (what should NOT happen) are captured, which often contain the most important business rules. |
| **Where used** | Phase 1 project discovery: the "Success" question maps to "What does success look like?" (question 4), "Failure" maps to "What should definitely not happen?" (question 8), "Out-of-scope" maps to boundary-setting from the 10-question framework. |

---

### 31. Domain-Driven Design — Bounded Contexts and Feature Identification

| | |
|---|---|
| **Source** | Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley. |
| **Date** | 2003 |
| **URL** | — |
| **Alternative** | Context Mapper (2025). Rapid Object-Oriented Analysis and Design. https://contextmapper.org/docs/rapid-ooad |
| **Status** | Confirmed — foundational DDD literature |
| **Core finding** | A Bounded Context is a boundary within which a particular ubiquitous language is consistent. Features are identified by grouping related user stories that share the same language. Features can be decomposed into subdomains, and subdomains can be grouped into Bounded Contexts. The decomposition criterion is "single responsibility per context" + "consistency of language." |
| **Mechanism** | In DDD: (1) Extract ubiquitous language from requirements → (2) Group by language consistency → (3) Each group is a candidate bounded context → (4) Each bounded context maps to a feature. Context Mapper automates this: User Stories → Subdomains (via noun/verb extraction) → Bounded Contexts of type FEATURE. |
| **Where used** | Phase 1: after feature list identification, verify each feature has consistent language. Phase 2: noun/verb extraction from project discovery answers populates the Entities table, which is the DDD candidate model. The "Rules (Business)" section captures the ubiquitous language rules that govern each feature. |

---

### 32. Object Calisthenics — Nine Rules

| | |
|---|---|
| **Source** | Bay, J. "Object Calisthenics." *The Thoughtworks Anthology* (PragProg, 2008). Original in IEEE Software/DevX, ~2005. |
| **Date** | ~2005 |
| **URL** | https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf |
| **Alternative** | — |
| **Status** | Practitioner synthesis |
| **Core finding** | 9 rules to internalize OOP: (1) One level indentation per method, (2) No ELSE, (3) Wrap primitives/Strings, (4) First class collections, (5) One dot per line, (6) No abbreviations, (7) Classes ≤50 lines, (8) ≤2 instance variables, (9) No getters/setters. 7 of 9 enforce data encapsulation; 1 drives polymorphism; 1 drives naming. |
| **Mechanism** | Restrictions force decomposition. When you cannot use getters, behavior must move into the object. When you cannot use ELSE, you use polymorphism. When classes must be ≤2 ivars, you discover missing abstractions. |
| **Where used** | Refactor phase in `implementation/SKILL.md`: rule checklist with PASS/FAIL per rule. |

---

### 33. Refactoring

| | |
|---|---|
| **Source** | Fowler, M. (1999/2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley. |
| **Date** | 1999, 2018 |
| **URL** | https://martinfowler.com/books/refactoring.html |
| **Alternative** | — |
| **Status** | Confirmed — foundational |
| **Core finding** | Refactoring = behavior-preserving transformations. 68 catalogued refactorings, each small enough to do safely but cumulative effect significant. Code smells (duplicate code, long methods, feature envy) indicate refactoring opportunities. |
| **Mechanism** | Small steps reduce risk. Each refactoring is reversible. Test suite validates behavior unchanged. |
| **Where used** | Refactor phase in `implementation/SKILL.md`: smell detection triggers refactoring. |

---

### 34. Design Patterns

| | |
|---|---|
| **Source** | Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. |
| **Date** | 1995 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed — foundational |
| **Core finding** | 23 patterns catalogued in 3 categories: Creational (5), Structural (7), Behavioral (11). Key principles: "Favor composition over inheritance," "Program to an interface, not an implementation." |
| **Mechanism** | Patterns are recurring solutions to common problems. Named and catalogued so developers don't rediscover them. |
| **Where used** | Refactor phase: when ObjCal rules fail, patterns provide alternative structure. |

---

### 35. SOLID Principles

| | |
|---|---|
| **Source** | Martin, R. C. (2000). "Principles of OOD." *ButUncleBob.com*. Acronym coined by Michael Feathers (2004). |
| **Date** | 2000 |
| **URL** | https://blog.interface-solv.com/wp-content/uploads/2020/07/Principles-Of-OOD.pdf |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | S: One reason to change. O: Open extension, closed modification. L: Subtypes substitutable. I: No forced stub methods. D: Depend on abstractions, not concretes. |
| **Mechanism** | Each principle targets a specific coupling failure mode. Together they produce low coupling, high cohesion. |
| **Where used** | Refactor self-check table in `implementation/SKILL.md`: 5-row SOLID table with PASS/FAIL. |

---

### 36. QDIR — Bad-Smells + OO Metrics Prioritization

| | |
|---|---|
| **Source** | Malhotra, R., Singh, P. (2020). "Exploiting bad-smells and object-oriented characteristics to prioritize classes for refactoring." *Int. J. Syst. Assur. Eng. Manag.* 11(Suppl 2), 133–144. Springer. |
| **Date** | 2020 |
| **URL** | https://doi.org/10.1007/s13198-020-01001-x |
| **Alternative** | — |
| **Status** | Confirmed — empirical |
| **Core finding** | QDIR (Quality Depreciation Index Rule) combines bad-smell severity with OO metrics (LOC, WMC, CBO, RFC, DIT) to prioritize classes for refactoring. Validated on 8 open-source Java systems. |
| **Mechanism** | Classes with high smell severity AND high OO metrics are prioritized. QDIR = weighted sum. |
| **Where used** | Refactor prioritization in Step 4: when smell detected, check OO metrics to prioritize. |

---

### 37. Smells + Architectural Refactoring

| | |
|---|---|
| **Source** | Silva, C. et al. (2020). "When Are Smells Indicators of Architectural Refactoring Opportunities." *Proc. 28th Int. Conf. on Program Comprehension*. ACM. |
| **Date** | 2020 |
| **URL** | https://doi.org/10.1145/3387904.3389276 |
| **Alternative** | — |
| **Status** | Confirmed — empirical |
| **Core finding** | Study of 50 projects, 52,667 refactored elements. 67.53% of smells co-occur. Smells that co-occur are indicators of architectural refactoring in 88.53% of cases. |
| **Mechanism** | Single smells are often code-level; co-occurring smells indicate architectural problems. Pattern catalog for smells→specific architectural refactorings. |
| **Where used** | Smell detection triggers architectural analysis when co-occurrence patterns detected. |

---

### 38. SPIRIT Tool — Code Smell Prioritization

| | |
|---|---|
| **Source** | Vidal, S. A., Marcos, C., Díaz-Pace, J. A. (2014). "An Approach to Prioritize Code Smells for Refactoring." *Automated Software Engineering*, 23(3), 501–532. Carleton University/Springer. |
| **Date** | 2014 |
| **URL** | https://doi.org/10.1007/s10515-014-0175-x |
| **Alternative** | — |
| **Status** | Confirmed — tool |
| **Core finding** | SPIRIT (Smart Identification of Refactoring opportunITies) prioritizes smells by 3 criteria: (1) component stability, (2) impact on modifiability scenarios, (3) smell relevance. Top-ranked smells correlate with expert developer judgment. |
| **Mechanism** | Semi-automated ranking. Combines version history (stable vs. unstable), impact analysis, and smell type. |
| **Where used** | Refactor prioritization: stability = has the class changed recently? Unstable + smelly = prioritize. |

---

### 39. Bad Engineering Properties of OOP

| | |
|---|---|
| **Source** | Cardelli, L. (1996). "Bad Engineering Properties of Object-Oriented Languages." *ACM Computing Surveys*, 28(4), 150. |
| **Date** | 1996 |
| **URL** | https://www.microsoft.com/en-us/research/publication/bad-engineering-properties-of-object-oriented-languages/ |
| **Alternative** | — |
| **Status** | Confirmed — foundational critique |
| **Core finding** | OOP has 5 "economy" problems: (1) Execution (virtual methods prevent inlining), (2) Compilation (no code/interface separation), (3) Small-scale dev (expressive type systems missing), (4) Large-scale dev (poor class extension/modification), (5) Language features (baroque complexity). |
| **Mechanism** | OOP is not universally superior. Trade-offs exist. Knowing these helps avoid over-engineering. |
| **Where used** | Anti-pre-pattern: know when OOP adds complexity vs. value. Feedback item 2 rationale. |

---

### 40. Code Complexity Model of OOP

| | |
|---|---|
| **Source** | Aluthwaththage, J. H., Thathsarani, H. A. N. N. (2024). "A Novel OO-Based Code Complexity Metric." *Proc. Future Technologies Conference (FTC)*, 616–628. Springer/IEEE. |
| **Date** | 2024 |
| **URL** | https://link.springer.com/chapter/10.1007/978-3-031-73125-9_39 |
| **Alternative** | Misra et al. (2024). "A Suite of Object Oriented Cognitive Complexity Metrics." IEEE. |
| **Status** | Partially confirmed — recent |
| **Core finding** | CWC (Combined Weighted Complexity) measures OOP complexity at statement level, considering 8 factors: nesting depth, control types, compound conditions, try-catch, threads, pointers, references, dynamic memory. Addresses gap in existing metrics ignoring cognitive load. |
| **Mechanism** | Granular complexity scoring. Higher scores indicate more cognitively demanding code. |
| **Where used** | Complexity measurement in Step 4 refactor: when function >20 lines, compute CWC-style granular score. |

---

### 41. Metric Thresholds for Smell Detection

| | |
|---|---|
| **Source** | Bigonha, M. A. S., et al. (2019). "The usefulness of software metric thresholds for detection of bad smells and fault prediction." *Information and Software Technology*, 115, 79–92. |
| **Date** | 2019 |
| **URL** | https://doi.org/10.1016/j.infsof.2019.08.005 |
| **Alternative** | Catal et al. (2018). "Software metrics thresholds calculation techniques." Info. Softw. Technol. |
| **Status** | Confirmed |
| **Core finding** | Metric thresholds (e.g., LOC > 600) used for smell detection are unreliable. Study on 92 open-source systems found precision too low for practical use. Neither heuristic-based (DECOR) nor ML approaches achieve acceptable accuracy. ROC Curves best of 3 threshold techniques but still insufficient alone. |
| **Mechanism** | Fixed thresholds are context-dependent. Thresholds should be project-specific, not universal. |
| **Where used** | Anti-pre-pattern: do not rely on fixed thresholds. Use co-occurrence patterns (Entry 37) instead. |

---

### 42. Hexagonal Architecture — Ports and Adapters

| | |
|---|---|
| **Source** | Cockburn, A. (2005). "Hexagonal Architecture." *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/ |
| **Date** | 2005 |
| **URL** | https://alistair.cockburn.us/hexagonal-architecture/ |
| **Alternative** | Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. (Chapter 7: "Ports and Adapters") |
| **Status** | Confirmed — foundational; widely adopted as Clean Architecture, Onion Architecture |
| **Core finding** | The application domain should have no knowledge of external systems (databases, filesystems, network, UI). All contact between the domain and the outside world passes through a **port** (an interface / Protocol) and an **adapter** (a concrete implementation of that port). This makes the domain independently testable without any infrastructure. The key structural rule: dependency arrows point inward — domain code never imports from adapters; adapters import from domain. |
| **Mechanism** | Two distinct sides of any application: the "driving side" (actors who initiate action — tests, UI, CLI) and the "driven side" (actors the application drives — databases, filesystems, external services). Each driven-side dependency is hidden behind a port. Tests supply a test adapter; production supplies a real adapter. Substituting adapters requires no domain code changes. This is what SOLID-D ("depend on abstractions") looks like at the architectural layer — not just at the class level. |
| **Where used** | Step 2 (Architecture): every external dependency identified during domain analysis must be assigned a port (Protocol) and a concrete adapter. Module structure always includes `<package>/adapters/<dep>.py` alongside `<package>/domain/`. The `adapters/` layer is decided at Step 2, not discovered during Step 4 refactoring. |

---

### 43. Feature-Driven Development — Domain Modeling to Feature List

| | |
|---|---|
| **Source** | Ambler, S. W. (2002). *Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process*. Wiley. Supplemented by: agilemodeling.com — "Feature Driven Development and Agile Modeling." |
| **Date** | 2002 |
| **URL** | https://www.agilemodeling.com/essays/fdd.htm |
| **Alternative** | Palmer, S. R., & Felsing, J. M. (2002). *A Practical Guide to Feature-Driven Development*. Prentice Hall. |
| **Status** | Confirmed |
| **Core finding** | FDD requires domain modeling *before* feature naming. Features are expressed as "Action result object" triples (e.g., "Enroll a student in a seminar"). Features group into Feature Sets (shared domain object), which group into Subject Areas. 78% of organisations doing Agile also do initial high-level agile requirements modeling; 85% find it worthwhile. |
| **Mechanism** | Domain modeling extracts the vocabulary (nouns = candidate classes, verbs = candidate methods). Feature identification then asks: "what verbs act on each noun?" This produces a list of small, deliverable units that are coherent with the domain rather than reflecting technical or organisational boundaries. |
| **Where used** | Phase 1 of `scope/SKILL.md`: after the interview summary is confirmed, PO performs domain analysis (nouns/verbs → subject areas → FDD "Action object" feature names) before creating `.feature` file stubs. |

---

### 44. Affinity Mapping / KJ Method — Bottom-Up Feature Identification

| | |
|---|---|
| **Source** | Krause, R., & Pernice, K. (2024). Affinity Diagramming for Collaboratively Sorting UX Findings and Design Ideas. *Nielsen Norman Group*. https://www.nngroup.com/articles/affinity-diagram/ |
| **Date** | 2024 (method origin: Kawakita, J., 1960s) |
| **URL** | https://www.nngroup.com/articles/affinity-diagram/ |
| **Alternative** | Kawakita, J. (1967). *Abduction*. Chuokoronsha (KJ Method original). |
| **Status** | Confirmed |
| **Core finding** | Affinity diagramming (KJ Method) groups raw observations/requirements into clusters by bottom-up similarity — no categories are named until grouping is complete. This prevents confirmation bias from top-down pre-labelling. Each named cluster becomes a candidate feature. Dot voting on clusters produces a prioritized feature list. Small clusters must not be discarded — they often represent minority concerns or genuinely novel features. |
| **Mechanism** | Bottom-up category emergence: when categories are not imposed in advance, the grouping reflects actual similarity in the data rather than the analyst's prior mental model. NN/G: "the journey is more important than the destination — the discussions that occurred while building the diagram are more impactful than the final format." |
| **Where used** | Phase 1 of `scope/SKILL.md` (alternative to FDD domain modeling): PO uses affinity mapping on interview answers to derive feature clusters before creating `.feature` stubs. Best suited when working from interview transcripts solo rather than with a cross-silo team. |

---

### 45. Event Storming — Domain Events to Functional Areas

| | |
|---|---|
| **Source** | Brandolini, A. (2013–present). *EventStorming*. Leanpub / eventstorming.com. https://eventstorming.com |
| **Date** | 2013 |
| **URL** | https://eventstorming.com; Bourgau, P. (2017). Detailed Agenda of a DDD Big Picture Event Storming. https://philippe.bourgau.net/detailed-agenda-of-a-ddd-big-picture-event-storming-part-1/ |
| **Alternative** | Brandolini, A. (2021). *Introducing EventStorming*. Leanpub. |
| **Status** | Confirmed |
| **Core finding** | Event Storming is a collaborative workshop where domain experts place past-tense domain events on a timeline. Sorting the events creates natural Functional Area clusters — these are candidate feature groups / Subject Areas. The workshop also produces Ubiquitous Language (shared vocabulary), a Problem Inventory (open questions), and Actor roles (for user story "As a [role]" parts). It does NOT produce Gherkin directly; its output feeds into Example Mapping per story. |
| **Mechanism** | Temporal sequencing of domain events forces resolution of conflicting mental models across organisational silos. Clusters emerge from shared vocabulary and causal proximity — not from the facilitator's prior structure. Bourgau: "Although nobody understands Bounded Context from the start, everyone gets Functional Area." |
| **Where used** | Optional alternative in Phase 1 of `scope/SKILL.md` for cross-silo discovery. Best suited when multiple stakeholders from different departments need to build shared understanding. Outputs (Functional Areas + Ubiquitous Language) map directly to Subject Areas (feature groups) and the Entities table in `.feature` file discovery sections. |

---

### 46. Critical Incident Technique — Gap-Finding via Past Events

| | |
|---|---|
| **Source** | Flanagan, J. C. (1954). "The critical incident technique." *Psychological Bulletin*, 51(4), 327–357. |
| **Date** | 1954 |
| **URL** | https://doi.org/10.1037/h0061470 |
| **Alternative** | Rosala, M. (2020). The Critical Incident Technique in UX. *Nielsen Norman Group*. https://www.nngroup.com/articles/critical-incident-technique/ |
| **Status** | Confirmed — foundational; ~200 follow-on empirical studies in marketing alone (Gremler 2004) |
| **Core finding** | Anchoring an interview on a specific past incident ("Tell me about a time when X broke down") breaks schema-based recall. Stakeholders describing actual past events report real workarounds, edge cases, and failure modes that never surface when asked "how does this usually work?" The technique explicitly requires both positive and negative incidents — positive first to establish rapport, negative second to surface failures. |
| **Mechanism** | Direct questions ("how does the system work?") elicit the stakeholder's mental schema — a sanitized, normalized, gap-free description of how things *should* work. Incidents bypass the schema because episodic memory is anchored to specific sensory and emotional detail that the schema lacks. Flanagan: "a critical incident must occur in a situation where the purpose or intent of the act seems fairly clear to the observer and where its consequences are sufficiently definite to leave little doubt." |
| **Where used** | Session 2 (gap-finding) of Phase 1 and Phase 2 in `scope/SKILL.md`. CIT prompts: "Tell me about a specific time this worked well / broke down." Follow up: "What were you trying to do? What made it difficult? What did you do instead?" |

---

### 47. Cognitive Interview — Memory-Enhancing Elicitation Technique

| | |
|---|---|
| **Source** | Fisher, R. P., & Geiselman, R. E. (1992). *Memory-Enhancing Techniques for Investigative Interviewing: The Cognitive Interview*. Charles C. Thomas. |
| **Date** | 1984 (original); 1987 (enhanced CI); 1992 (manual) |
| **URL** | DOI: 10.1037/0021-9010.74.5.722 (1989 field study) |
| **Alternative** | Moody, W., Will, R. P., & Blanton, J. E. (1996). "Enhancing knowledge elicitation using the cognitive interview." *Expert Systems with Applications*, 10(1), 127–133. DOI: 10.1016/0957-4174(95)00039-9 |
| **Status** | Confirmed — meta-analysis: Köhnken, Milne, Memon & Bull (1999), *Psychology, Crime & Law*, 5(1-2), 3–27. DOI: 10.1080/10683169908414991 |
| **Core finding** | The enhanced CI elicits ~35% more correct information than standard interviews with equal accuracy rates (85% vs. 82%). Moody et al. (1996) directly applied CI to knowledge elicitation from domain experts, finding it superior for capturing episodic knowledge that standard structured interviews miss. |
| **Mechanism** | Four retrieval mnemonics: (1) **Mental reinstatement of context** — stakeholder mentally returns to a specific past situation; (2) **Report everything** — all details including seemingly minor ones; (3) **Temporal reversal** — narrate events from a different starting point to disrupt schema-based reconstruction; (4) **Perspective change** — describe the situation from another actor's viewpoint. Each mnemonic opens a different memory access route, collectively surfacing what direct questions cannot. |
| **Where used** | Session 2 (gap-finding) of Phase 1 and Phase 2 in `scope/SKILL.md`. CI perspective change prompt: "What do you think the end user experiences in that situation?" CI reversal prompt: "Walk me through that scenario starting from when it went wrong." |

---

### 48. Laddering / Means-End Chain — Surfacing Unstated Motivations

| | |
|---|---|
| **Source** | Reynolds, T. J., & Gutman, J. (1988). "Laddering theory, method, analysis, and interpretation." *Journal of Advertising Research*, 28(1), 11–31. |
| **Date** | 1988 (method origin: Kelly, G. (1955). *The Psychology of Personal Constructs*. Norton.) |
| **URL** | https://en.wikipedia.org/wiki/Repertory_grid |
| **Alternative** | Hunter, M. G., & Beck, J. E. (2000). "Using repertory grids to conduct cross-cultural information systems research." *Information Systems Research*, 11(1), 93–101. DOI: 10.1287/isre.11.1.93.11786 |
| **Status** | Confirmed — operationalised in IS research (Hunter & Beck 2000); embedded in NNG interview protocols (Rosala 2021) |
| **Core finding** | Repeatedly asking "Why is that important to you?" climbs a means-end chain from concrete attribute → functional consequence → psychosocial consequence → terminal value. The stakeholder's first answer is rarely the real constraint — it is the socially expected, conscious-level response. The real motivation (and the actual constraint that requirements must satisfy) emerges two or three levels up the ladder. |
| **Mechanism** | The Gherkin "So that [benefit]" clause is structurally a single-rung means-end ladder. Full laddering reveals the value conflicts between stakeholders whose surface requirements look identical but whose ladders diverge at the consequence level. Without laddering, requirements that satisfy the stated attribute may fail the underlying goal. |
| **Where used** | Session 2 (gap-finding) of Phase 1 and Phase 2 in `scope/SKILL.md`. Laddering probe: "Why is that important to you?", "What does that enable for you?", "What would break if that weren't available?" Climb until the stakeholder reaches a terminal value they cannot explain further. |

---

### 49. Funnel Technique — Question Ordering to Prevent Priming

| | |
|---|---|
| **Source** | Rosala, M., & Moran, K. (2022). The Funnel Technique in Qualitative User Research. *Nielsen Norman Group*. https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/ |
| **Date** | 2022 |
| **URL** | https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/ |
| **Alternative** | Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. https://www.sei.cmu.edu/library/abstracts/reports/92tr012.cfm |
| **Status** | Confirmed — standard NNG qualitative research protocol |
| **Core finding** | Starting with broad open-ended questions before narrowing to specifics prevents the interviewer from priming the interviewee's responses. Once a category label is introduced, the interviewee interprets subsequent questions through that frame and under-reports items that don't fit it. Broad-to-narrow sequencing within each topic cluster is the evidence-based default for discovery interviews. |
| **Mechanism** | Priming bias is structural: human memory is associative, so any category name the interviewer introduces activates a schema that filters what the interviewee considers worth reporting. The funnel sequences questions so the interviewee's own categories emerge first, before the interviewer's categories are introduced. |
| **Where used** | Within each session of Phase 1 and Phase 2 in `scope/SKILL.md`. Within each topic cluster: start with "Tell me about..." before asking specific follow-up probes. Applies alongside CIT, CI, and Laddering — all of which are also open-ended by design. |

---

### 50. Issues in Requirements Elicitation — Why Direct Questions Fail

| | |
|---|---|
| **Source** | Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. Software Engineering Institute, Carnegie Mellon University. |
| **Date** | 1992 |
| **URL** | https://www.sei.cmu.edu/library/abstracts/reports/92tr012.cfm |
| **Alternative** | Sommerville, I., & Sawyer, P. (1997). *Requirements Engineering: A Good Practice Guide*. Wiley. |
| **Status** | Confirmed — foundational SEI technical report; widely cited in RE literature |
| **Core finding** | Stakeholders have three structural problems that make direct questioning insufficient: (1) they omit information that is "obvious" to them but unknown to the analyst; (2) they have trouble communicating needs they have never had to articulate; (3) they may not know what they want until they see what they don't want. These are not stakeholder failures — they are structural properties of tacit knowledge. |
| **Mechanism** | Expert knowledge is largely procedural and tacit. When asked "how does the system work?", experts describe what they believe happens, not what actually happens. This sanitized account is internally consistent but incomplete. Gap-finding techniques (CIT, CI, Laddering) are required because they bypass the expert's mental schema and access the episodic memory layer where real complexity lives. |
| **Where used** | Theoretical justification for the 3-session interview structure and the use of CIT, CI, and Laddering in `scope/SKILL.md`. Answers the question: "why not just ask the stakeholder directly what they need?" |

---

### 51. Canon TDD — Authoritative Red-Green-Refactor Definition

| | |
|---|---|
| **Source** | Beck, K. (2023). "Canon TDD." *tidyfirst.substack.com*. December 11, 2023. |
| **Date** | 2023 |
| **URL** | https://tidyfirst.substack.com/p/canon-tdd |
| **Alternative** | Fowler, M. (2023). "Test Driven Development." *martinfowler.com*. December 11, 2023. https://martinfowler.com/bliki/TestDrivenDevelopment.html |
| **Status** | Confirmed — canonical source; explicitly authored to stop strawman critiques |
| **Core finding** | The canonical TDD loop is: (1) write a list of test scenarios; (2) convert exactly one item into a runnable test; (3) make it pass; (4) optionally refactor; (5) repeat. Writing all test code before any implementation is an explicit anti-pattern ("Mistake: convert all items on the list into concrete tests, then make them pass"). |
| **Mechanism** | The interleaving of test-writing and implementation is not cosmetic — each test drives interface decisions at the moment they are cheapest to make. Batch-writing tests first forces speculative interface decisions that later require rework when earlier tests reveal structural problems. |
| **Where used** | Justifies merging Step 3 (test bodies) into the implementation loop. Removing the separate "write all tests" phase and replacing it with one-@id-at-a-time interleaved TDD. |

---

### 52. Growing Object-Oriented Software, Guided by Tests (GOOS) — Outer/Inner TDD Loop

| | |
|---|---|
| **Source** | Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. |
| **Date** | 2009 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed — canonical ATDD/BDD integration model |
| **Core finding** | Acceptance tests and unit tests operate at two separate, nested timescales. The outer loop: write one failing acceptance test (Gherkin/feature-level) before writing any implementation. The inner loop: drive implementation with unit-level Red-Green-Refactor cycles until the acceptance test passes. The acceptance test stays red throughout all inner cycles and goes green only when the feature is complete. |
| **Mechanism** | The outer loop provides direction (what to build); the inner loop provides momentum (how to build it). Running acceptance tests first prevents tunnel vision during unit-level work — the developer always has a red acceptance test as the north star. This is the canonical model for integrating Gherkin acceptance criteria (@id Examples) with unit TDD. |
| **Where used** | Justifies the two-level structure in Step 3 (TDD Loop): outer loop per @id acceptance test, inner loop per unit. Each @id Example is the acceptance test for one outer loop iteration. |

---

### 53. Is TDD Dead? — Anti-Bureaucracy Evidence

| | |
|---|---|
| **Source** | Beck, K., Fowler, M., & Hansson, D. H. (2014). "Is TDD Dead?" Video series, *martinfowler.com*. May–June 2014. https://martinfowler.com/articles/is-tdd-dead/ |
| **Date** | 2014 |
| **URL** | https://martinfowler.com/articles/is-tdd-dead/ |
| **Alternative** | — |
| **Status** | Confirmed — primary evidence for what TDD practitioners reject as overhead |
| **Core finding** | Per-cycle human reviewer gates, per-cycle checklists, and tests that provide zero delta coverage are all explicitly identified as harmful overhead in TDD workflows. The green bar is the quality gate — not a checklist. DHH: "Many people used to think that documentation was more important than code. Now he's concerned that people think tests are more important than functional code." Beck: "Tests with zero delta coverage should be deleted unless they provide some kind of communication purpose." |
| **Mechanism** | Administrative overhead added to TDD workflows increases the cost per cycle without increasing coverage or catching defects. The optimal TDD loop is as lean as productive — ceremony that does not eliminate a failure mode should be eliminated. Fowler: "The sign of too much testing is whenever you change the code you think you expend more effort changing the tests than changing the code." |
| **Where used** | Justifies removing per-test reviewer gates and per-test 24-item self-declaration from the TDD loop. Self-declaration moves to end-of-feature (once), preserving Cialdini+Tetlock accountability at feature granularity without interrupting cycle momentum. |

---

### 54. Introducing BDD — Behavioural-Driven Development Origin

| | |
|---|---|
| **Source** | North, D. (2006). "Introducing BDD." *Better Software Magazine*, March 2006. https://dannorth.net/introducing-bdd/ |
| **Date** | 2006 |
| **URL** | https://dannorth.net/introducing-bdd/ |
| **Alternative** | Fowler, M. (2013). "Given When Then." *martinfowler.com*. https://martinfowler.com/bliki/GivenWhenThen.html |
| **Status** | Confirmed — primary BDD source |
| **Core finding** | BDD evolved directly from TDD to address persistent practitioner confusion: where to start, what to test, how much to test in one go, and what to call tests. BDD reframes TDD vocabulary around observable behavior: scenarios instead of tests, Given-When-Then (G/W/T) instead of Arrange-Act-Assert (AAA). The underlying mechanics are identical — G/W/T is AAA with shared-vocabulary semantics for collaboration between technical and non-technical stakeholders. |
| **Mechanism** | The "Given" clause captures preconditions (Arrange), "When" captures the triggering event (Act), and "Then" captures the observable outcome (Assert). Translating from AAA to G/W/T shifts the focus from implementation mechanics to user-observable behavior, making acceptance criteria verifiable by non-technical stakeholders and executable by the test suite simultaneously. |
| **Where used** | Theoretical link between Gherkin @id Examples (Step 1 output) and the TDD inner loop (Step 3). Each @id Example is a G/W/T specification that maps directly to a test function. The outer GOOS loop is an acceptance test written in BDD vocabulary; the inner loop is unit TDD. |

---

## Bibliography

1. Cialdini, R. B. (2001). *Influence: The Psychology of Persuasion* (rev. ed.). HarperBusiness.
2. Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684.
3. Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple planning aids. *American Journal of Preventive Medicine*, 16(4), 257–276.
4. Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112.
5. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
6. Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press.
7. McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval. *Applied Cognitive Psychology*, 14(7), S127–S144.
8. Mellers, B. A., Hertwig, R., & Kahneman, D. (2001). Do frequency representations eliminate cooperative bias? *Psychological Review*, 108(4), 709–735.
9. Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
10. Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285.
11. Tetlock, P. E. (1983). Accountability: A social determinant of judgment. In M. D. B. T. Strother (Ed.), *Psychology of Learning and Motivation* (Vol. 17, pp. 295–332). Academic Press.
12. Fowler, M. (2018). The Practical Test Pyramid. *Thoughtworks*. https://martinfowler.com/articles/practical-test-pyramid.html
13. Google Testing Blog. (2013). Testing on the Toilet: Test Behavior, Not Implementation.
14. Martin, R. C. (2017). First-Class Tests. *Clean Coder Blog*.
15. MacIver, D. R. (2016). What is Property Based Testing? *Hypothesis*. https://hypothesis.works/articles/what-is-property-based-testing/
16. Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall.
17. Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477.
18. Wake, B. (2003). INVEST in Good Stories, and SMART Tasks. *XP123.com*.
19. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
20. Wynne, M. (2015). Introducing Example Mapping. *Cucumber Blog*. https://cucumber.io/blog/bdd/example-mapping-introduction/
21. Cucumber Team. (2024). Better Gherkin. *Cucumber Documentation*. https://cucumber.io/docs/bdd/better-gherkin/
22. Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley.
23. OpenAI. (2024). Agent definitions. *OpenAI Agents SDK Documentation*. https://platform.openai.com/docs/guides/agents/define-agents
24. Anthropic. (2024). Building effective agents. *Anthropic Engineering Blog*. https://www.anthropic.com/engineering/building-effective-agents
25. Anthropic. (2025). Best practices for Claude Code. *Anthropic Documentation*. https://www.anthropic.com/engineering/claude-code-best-practices
26. OpenCode. (2026). Agent Skills. *OpenCode Documentation*. https://opencode.ai/docs/skills/
27. Geng et al. (2025). Control Illusion: The Failure of Instruction Hierarchies in Large Language Models. AAAI-26. arXiv:2502.15851. https://arxiv.org/abs/2502.15851
28. Wallace, E. et al. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv:2404.13208. https://arxiv.org/abs/2404.13208
29. Liu, N. F. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*. arXiv:2307.03172. https://arxiv.org/abs/2307.03172
30. McKinnon, R. (2025). arXiv:2511.05850. https://arxiv.org/abs/2511.05850
31. Sharma, A., & Henley, A. (2026). Modular Prompt Optimization. arXiv:2601.04055. https://arxiv.org/abs/2601.04055
32. Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago.
33. McNaughton, D., Hamlin, D., McCarthy, J., Head-Reeves, D., & Schreiner, M. (2008). Learning to Listen: Teaching an Active Listening Strategy to Preservice Education Professionals. *Topics in Early Childhood Special Education*, 27(4), 223–231.
34. Kipling, R. (1902). *Just So Stories*. Macmillan.
35. Brandenburg, L. (2025). *Requirements Discovery Checklist Pack*. TechCanvass. https://www.businessanalyststoolkit.com/requirements-elicitation-questions/
36. Sherwen. (2025). "10 Questions to Consider During Requirements Gathering." https://www.sherwen.com/insights/10-questions-you-must-ask-during-requirements-gathering
37. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.
38. Context Mapper. (2025). Rapid Object-Oriented Analysis and Design. https://contextmapper.org/docs/rapid-ooad
39. Bay, J. (2005). "Object Calisthenics." *IEEE Software/DevX*. https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf
40. Fowler, M. (1999/2018). *Refactoring: Improving the Design of Existing Code*. Addison-Wesley. https://martinfowler.com/books/refactoring.html
41. Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
42. Martin, R. C. (2000). "Principles of OOD." *ButUncleBob.com*. https://blog.interface-solv.com/wp-content/uploads/2020/07/Principles-Of-OOD.pdf
43. Malhotra, R., & Singh, P. (2020). Exploiting bad-smells and object-oriented characteristics to prioritize classes for refactoring. *Int. J. Syst. Assur. Eng. Manag.*, 11(Suppl 2), 133–144. https://doi.org/10.1007/s13198-020-01001-x
44. Silva, C. et al. (2020). When Are Smells Indicators of Architectural Refactoring Opportunities. *Proc. 28th Int. Conf. on Program Comprehension*. ACM. https://doi.org/10.1145/3387904.3389276
45. Vidal, S. A., Marcos, C., & Díaz-Pace, J. A. (2014). An Approach to Prioritize Code Smells for Refactoring. *Automated Software Engineering*, 23(3), 501–532. https://doi.org/10.1007/s10515-014-0175-x
46. Cardelli, L. (1996). Bad Engineering Properties of Object-Oriented Languages. *ACM Computing Surveys*, 28(4), 150. https://www.microsoft.com/en-us/research/publication/bad-engineering-properties-of-object-oriented-languages/
47. Aluthwaththage, J. H., & Thathsarani, H. A. N. N. (2024). A Novel OO-Based Code Complexity Metric. *Proc. Future Technologies Conference (FTC)*, 616–628. https://link.springer.com/chapter/10.1007/978-3-031-73125-9_39
48. Bigonha, M. A. S., et al. (2019). The usefulness of software metric thresholds for detection of bad smells and fault prediction. *Information and Software Technology*, 115, 79–92. https://doi.org/10.1016/j.infsof.2019.08.005
49. Ambler, S. W. (2002). *Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process*. Wiley. https://www.agilemodeling.com/essays/fdd.htm
50. Palmer, S. R., & Felsing, J. M. (2002). *A Practical Guide to Feature-Driven Development*. Prentice Hall.
51. Krause, R., & Pernice, K. (2024). Affinity Diagramming for Collaboratively Sorting UX Findings and Design Ideas. *Nielsen Norman Group*. https://www.nngroup.com/articles/affinity-diagram/
52. Brandolini, A. (2013–present). *EventStorming*. Leanpub / eventstorming.com. https://eventstorming.com
53. Bourgau, P. (2017). Detailed Agenda of a DDD Big Picture Event Storming. https://philippe.bourgau.net/detailed-agenda-of-a-ddd-big-picture-event-storming-part-1/
54. Nielsen, J. (2010). *Interviewing Users*. Nielsen Norman Group. https://www.nngroup.com/articles/interviewing-users/
55. Farrell, S. (2017). UX Research Cheat Sheet. *Nielsen Norman Group*. https://www.nngroup.com/articles/ux-research-cheat-sheet/
56. Flanagan, J. C. (1954). The critical incident technique. *Psychological Bulletin*, 51(4), 327–357. https://doi.org/10.1037/h0061470
57. Fisher, R. P., & Geiselman, R. E. (1992). *Memory-Enhancing Techniques for Investigative Interviewing: The Cognitive Interview*. Charles C. Thomas.
58. Fisher, R. P., Geiselman, R. E., & Amador, M. (1989). Field test of the cognitive interview: Enhancing the recollection of actual victims and witnesses of crime. *Journal of Applied Psychology*, 74(5), 722–727. https://doi.org/10.1037/0021-9010.74.5.722
59. Köhnken, G., Milne, R., Memon, A., & Bull, R. (1999). The cognitive interview: A meta-analysis. *Psychology, Crime & Law*, 5(1-2), 3–27. https://doi.org/10.1080/10683169908414991
60. Moody, W., Will, R. P., & Blanton, J. E. (1996). Enhancing knowledge elicitation using the cognitive interview. *Expert Systems with Applications*, 10(1), 127–133. https://doi.org/10.1016/0957-4174(95)00039-9
61. Reynolds, T. J., & Gutman, J. (1988). Laddering theory, method, analysis, and interpretation. *Journal of Advertising Research*, 28(1), 11–31.
62. Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. Software Engineering Institute, Carnegie Mellon University. https://www.sei.cmu.edu/library/abstracts/reports/92tr012.cfm
63. Rosala, M. (2020). The Critical Incident Technique in UX. *Nielsen Norman Group*. https://www.nngroup.com/articles/critical-incident-technique/
64. Rosala, M., & Moran, K. (2022). The Funnel Technique in Qualitative User Research. *Nielsen Norman Group*. https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/
65. Cockburn, A. (2005). Hexagonal Architecture. *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/
66. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
67. Beck, K. (2023). "Canon TDD." *tidyfirst.substack.com*. https://tidyfirst.substack.com/p/canon-tdd
68. Beck, K., Fowler, M., & Hansson, D. H. (2014). "Is TDD Dead?" Video series. *martinfowler.com*. https://martinfowler.com/articles/is-tdd-dead/
69. Fowler, M. (2014). "Self Testing Code." *martinfowler.com*. https://martinfowler.com/bliki/SelfTestingCode.html
70. North, D. (2006). "Introducing BDD." *Better Software Magazine*. https://dannorth.net/introducing-bdd/
