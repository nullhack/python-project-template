# Scientific Research — Requirements Elicitation

Foundations for the PO interview structure, Gherkin criteria, and feature discovery in this template.

---

### 17. INVEST Criteria for User Stories

| | |
|---|---|
| **Source** | Wake, B. (2003). *INVEST in Good Stories, and SMART Tasks*. XP123.com. |
| **Date** | 2003 |
| **Alternative** | Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley. |
| **Status** | Confirmed |
| **Core finding** | Stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable produce fewer downstream defects and smoother development cycles. |
| **Mechanism** | INVEST serves as a quality gate before stories enter development. "Testable" forces the PO to express observable outcomes (directly enabling Given/When/Then). "Small" forces decomposition. "Independent" prevents hidden ordering dependencies. |
| **Where used** | INVEST gate in Phase 3 of `scope/SKILL.md`. |

---

### 18. Example Mapping (Rules Layer)

| | |
|---|---|
| **Source** | Wynne, M. (2015). *Introducing Example Mapping*. Cucumber Blog. https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Date** | 2015 |
| **Status** | Confirmed |
| **Core finding** | Inserting a "rules" layer between stories and examples prevents redundant or contradictory acceptance criteria. A story with many rules needs splitting; a story with many open questions is not ready for development. |
| **Mechanism** | Four card types: Story (yellow), Rules (blue), Examples (green), Questions (red). The rules layer groups related examples under the business rule they illustrate. Red cards (unanswered questions) are a first-class signal to stop and investigate. |
| **Where used** | `Rules (Business):` section in each `.feature` file. PO identifies business rules before writing Examples in Stage 2 Step B. |

---

### 19. Declarative Gherkin

| | |
|---|---|
| **Source** | Cucumber Team. (2024). *Better Gherkin*. Cucumber Documentation. https://cucumber.io/docs/bdd/better-gherkin/ |
| **Date** | 2024 |
| **Status** | Confirmed |
| **Core finding** | Declarative Gherkin ("When Bob logs in") produces specifications that survive UI changes. Imperative Gherkin ("When I click the Login button") couples specs to implementation details and breaks on every UI redesign. |
| **Mechanism** | Declarative steps describe *what happens* at the business level. Imperative steps describe *how the user interacts with a specific UI*. AI agents are especially prone to writing imperative Gherkin because they mirror literal steps. |
| **Where used** | Declarative vs. imperative table in Stage 2 Step B (Criteria) of `scope/SKILL.md`. |

---

### 20. MoSCoW Prioritization (Within-Story Triage)

| | |
|---|---|
| **Source** | Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley (DSDM origin). |
| **Date** | 1994 |
| **Status** | Confirmed |
| **Core finding** | Classifying requirements as Must/Should/Could/Won't forces explicit negotiation about what is essential vs. desired. When applied *within* a single story, it reveals bloated stories that should be split. |
| **Mechanism** | DSDM mandates that Musts cannot exceed 60% of total effort. At the story level: if a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred. This prevents gold-plating and keeps stories small. |
| **Where used** | MoSCoW triage in Stage 2 Step B (Criteria) of `scope/SKILL.md`. |

---

### 28. Active Listening — Paraphrase-Clarify-Summarize

| | |
|---|---|
| **Source** | Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago. |
| **Date** | 1957 |
| **Alternative** | McNaughton, D. et al. (2008). Learning to Listen. *Topics in Early Childhood Special Education*, 27(4), 223–231. |
| **Status** | Confirmed — foundational clinical research; widely replicated |
| **Core finding** | Active listening — paraphrasing what was heard in the listener's own words, asking clarifying questions, then summarising the main points and intent — reduces misunderstanding, builds trust, and confirms mutual understanding before proceeding. |
| **Mechanism** | Paraphrasing forces the listener to reconstruct the speaker's meaning, surfacing gaps immediately. Clarifying questions address residual ambiguity. Summarizing creates a shared record that both parties can confirm or correct. |
| **Where used** | PO summarization protocol in `scope/SKILL.md`: after each interview round, PO produces a "Here is what I understood" block before proceeding. |

---

### 28a. Active Listening — Three-Level Structure

| | |
|---|---|
| **Source** | Synthesis of: Nielsen (2010); Farrell (2017); Ambler (2002); Wynne (2015). |
| **Date** | 2010–2015 |
| **Status** | Synthesized rule of thumb — each component individually confirmed |
| **Core finding** | Active listening in requirements interviews operates at three granularities: **Level 1** (per answer) — immediate paraphrase; **Level 2** (per topic cluster) — transition summary; **Level 3** (end of interview) — full synthesis serving four downstream purposes. |
| **Level 3 — four uses** | 1. Accuracy gate (NN/G). 2. Scope crystallization (Ambler/FDD). 3. Input to domain modelling (Ambler/FDD). 4. Baseline trigger (Wynne/Cucumber). |
| **Where used** | Stage 1 Discovery sessions in `scope/SKILL.md`. |

---

### 29. The Kipling Method — Five Ws and One H

| | |
|---|---|
| **Source** | Kipling, R. (1902). *Just So Stories*. Macmillan. |
| **Date** | 1902 |
| **Alternative** | Hermagoras of Temnos (2nd century BCE) — seven circumstances of rhetoric. |
| **Status** | Practitioner synthesis — journalism, business analysis, investigative methodology |
| **Core finding** | The six interrogative questions (Who, What, When, Where, Why, How) form a complete framework for gathering all essential facts about any situation. Together they ensure completeness and prevent gaps. |
| **Where used** | Stage 1 Discovery, General questions (first session): the initial seven questions are an adaptation of the 5W1H framework. |

---

### 30. BA Requirements Question Framework

| | |
|---|---|
| **Source** | Brandenburg, L. (2025). *Requirements Discovery Checklist Pack*. TechCanvass. |
| **Date** | 2025 |
| **Status** | Practitioner synthesis — consolidated BA methodology, not peer-reviewed |
| **Core finding** | Ten questions consistently make the most difference in requirements elicitation: (1) What problem are we solving? (2) What happens if we do nothing? (3) Who uses this? (4) What does success look like? (5) Walk me through how this works today. (6) Where does this usually break? (7) What decisions will this help? (8) What should definitely not happen? (9) What happens if input is wrong? (10) What assumptions are we making? |
| **Where used** | Stage 1 Discovery, General questions: the "Success", "Failure", and "Out-of-scope" questions map to this framework. |

---

### 43. Feature-Driven Development — Domain Modeling to Feature List

| | |
|---|---|
| **Source** | Ambler, S. W. (2002). *Agile Modeling*. Wiley. https://www.agilemodeling.com/essays/fdd.htm |
| **Date** | 2002 |
| **Alternative** | Palmer, S. R., & Felsing, J. M. (2002). *A Practical Guide to Feature-Driven Development*. Prentice Hall. |
| **Status** | Confirmed |
| **Core finding** | FDD requires domain modelling *before* feature naming. Features are expressed as "Action result object" triples. Features group into Feature Sets (shared domain object), which group into Subject Areas. |
| **Mechanism** | Domain modelling extracts the vocabulary (nouns = candidate classes, verbs = candidate methods). Feature identification then asks: "what verbs act on each noun?" |
| **Where used** | Stage 1 Discovery in `scope/SKILL.md`: after session synthesis, PO performs domain analysis (nouns/verbs → subject areas → FDD "Action object" feature names) for first session. |

---

### 44. Affinity Mapping / KJ Method — Bottom-Up Feature Identification

| | |
|---|---|
| **Source** | Krause, R., & Pernice, K. (2024). Affinity Diagramming. *Nielsen Norman Group*. https://www.nngroup.com/articles/affinity-diagram/ |
| **Date** | 2024 (method origin: Kawakita, J., 1960s) |
| **Alternative** | Kawakita, J. (1967). *Abduction*. Chuokoronsha. |
| **Status** | Confirmed |
| **Core finding** | Affinity diagramming groups raw observations/requirements into clusters by bottom-up similarity — no categories are named until grouping is complete. This prevents confirmation bias from top-down pre-labelling. |
| **Where used** | Stage 1 Discovery in `scope/SKILL.md` (alternative to FDD domain modelling): PO uses affinity mapping on interview answers to derive feature clusters. Best suited when working from interview transcripts solo. |

---

### 45. Event Storming — Domain Events to Functional Areas

| | |
|---|---|
| **Source** | Brandolini, A. (2013–present). *EventStorming*. Leanpub / eventstorming.com. https://eventstorming.com |
| **Date** | 2013 |
| **Status** | Confirmed |
| **Core finding** | Event Storming is a collaborative workshop where domain experts place past-tense domain events on a timeline. Sorting the events creates natural Functional Area clusters — these are candidate feature groups. The workshop also produces Ubiquitous Language, a Problem Inventory, and Actor roles. |
| **Mechanism** | Temporal sequencing of domain events forces resolution of conflicting mental models across organisational silos. Clusters emerge from shared vocabulary and causal proximity. |
| **Where used** | Optional alternative in Stage 1 Discovery in `scope/SKILL.md` for cross-silo discovery. |

---

### 46. Critical Incident Technique — Gap-Finding via Past Events

| | |
|---|---|
| **Source** | Flanagan, J. C. (1954). "The critical incident technique." *Psychological Bulletin*, 51(4), 327–357. https://doi.org/10.1037/h0061470 |
| **Date** | 1954 |
| **Alternative** | Rosala, M. (2020). The Critical Incident Technique in UX. *Nielsen Norman Group*. https://www.nngroup.com/articles/critical-incident-technique/ |
| **Status** | Confirmed — foundational; ~200 follow-on empirical studies |
| **Core finding** | Anchoring an interview on a specific past incident ("Tell me about a time when X broke down") breaks schema-based recall. Stakeholders describing actual past events report real workarounds, edge cases, and failure modes that never surface when asked "how does this usually work?" |
| **Mechanism** | Direct questions elicit the stakeholder's mental schema — a sanitized, gap-free description of how things *should* work. Incidents bypass the schema because episodic memory is anchored to specific sensory and emotional detail. |
| **Where used** | Cross-cutting and per-feature questions (gap-finding) in Stage 1 Discovery in `scope/SKILL.md`. |

---

### 47. Cognitive Interview — Memory-Enhancing Elicitation Technique

| | |
|---|---|
| **Source** | Fisher, R. P., & Geiselman, R. E. (1992). *Memory-Enhancing Techniques for Investigative Interviewing: The Cognitive Interview*. Charles C. Thomas. |
| **Date** | 1984 (original); 1987 (enhanced CI); 1992 (manual) |
| **Alternative** | Moody, W., Will, R. P., & Blanton, J. E. (1996). Enhancing knowledge elicitation using the cognitive interview. *Expert Systems with Applications*, 10(1), 127–133. |
| **Status** | Confirmed — meta-analysis: Köhnken et al. (1999), *Psychology, Crime & Law*, 5(1-2), 3–27. |
| **Core finding** | The enhanced CI elicits ~35% more correct information than standard interviews with equal accuracy rates. |
| **Mechanism** | Four retrieval mnemonics: (1) mental reinstatement of context; (2) report everything; (3) temporal reversal; (4) perspective change. Each mnemonic opens a different memory access route, collectively surfacing what direct questions cannot. |
| **Where used** | Cross-cutting and per-feature questions (gap-finding) in Stage 1 Discovery in `scope/SKILL.md`. |

---

### 48. Laddering / Means-End Chain — Surfacing Unstated Motivations

| | |
|---|---|
| **Source** | Reynolds, T. J., & Gutman, J. (1988). "Laddering theory, method, analysis, and interpretation." *Journal of Advertising Research*, 28(1), 11–31. |
| **Date** | 1988 |
| **Status** | Confirmed — operationalised in IS research (Hunter & Beck 2000) |
| **Core finding** | Repeatedly asking "Why is that important to you?" climbs a means-end chain from concrete attribute → functional consequence → psychosocial consequence → terminal value. The stakeholder's first answer is rarely the real constraint. |
| **Mechanism** | The Gherkin "So that [benefit]" clause is structurally a single-rung means-end ladder. Full laddering reveals value conflicts between stakeholders whose surface requirements look identical but whose ladders diverge at the consequence level. |
| **Where used** | Cross-cutting and per-feature questions (gap-finding) in Stage 1 Discovery in `scope/SKILL.md`. |

---

### 49. Funnel Technique — Question Ordering to Prevent Priming

| | |
|---|---|
| **Source** | Rosala, M., & Moran, K. (2022). The Funnel Technique in Qualitative User Research. *Nielsen Norman Group*. https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/ |
| **Date** | 2022 |
| **Alternative** | Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. |
| **Status** | Confirmed — standard NNG qualitative research protocol |
| **Core finding** | Starting with broad open-ended questions before narrowing to specifics prevents the interviewer from priming the interviewee's responses. |
| **Mechanism** | Priming bias is structural: any category name the interviewer introduces activates a schema that filters what the interviewee considers worth reporting. The funnel sequences questions so the interviewee's own categories emerge first. |
| **Where used** | Within each Stage 1 Discovery session in `scope/SKILL.md`. |

---

### 50. Issues in Requirements Elicitation — Why Direct Questions Fail

| | |
|---|---|
| **Source** | Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. Software Engineering Institute, Carnegie Mellon University. https://www.sei.cmu.edu/library/abstracts/reports/92tr012.cfm |
| **Date** | 1992 |
| **Alternative** | Sommerville, I., & Sawyer, P. (1997). *Requirements Engineering: A Good Practice Guide*. Wiley. |
| **Status** | Confirmed — foundational SEI technical report |
| **Core finding** | Stakeholders have three structural problems that make direct questioning insufficient: (1) they omit information that is "obvious" to them; (2) they have trouble communicating needs they have never had to articulate; (3) they may not know what they want until they see what they don't want. |
| **Mechanism** | Expert knowledge is largely procedural and tacit. When asked "how does the system work?", experts describe what they believe happens, not what actually happens. Gap-finding techniques are required because they bypass the expert's mental schema. |
| **Where used** | Theoretical justification for the 3-session interview structure and use of CIT, CI, and Laddering in `scope/SKILL.md`. |

---

## Bibliography

1. Ambler, S. W. (2002). *Agile Modeling*. Wiley. https://www.agilemodeling.com/essays/fdd.htm
2. Brandenburg, L. (2025). *Requirements Discovery Checklist Pack*. TechCanvass.
3. Brandolini, A. (2013–present). *EventStorming*. https://eventstorming.com
4. Christel, M. G., & Kang, K. C. (1992). *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012. https://www.sei.cmu.edu/library/abstracts/reports/92tr012.cfm
5. Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley.
6. Cohn, M. (2004). *User Stories Applied*. Addison-Wesley.
7. Cucumber Team. (2024). Better Gherkin. https://cucumber.io/docs/bdd/better-gherkin/
8. Farrell, S. (2017). UX Research Cheat Sheet. *Nielsen Norman Group*. https://www.nngroup.com/articles/ux-research-cheat-sheet/
9. Fisher, R. P., & Geiselman, R. E. (1992). *Memory-Enhancing Techniques for Investigative Interviewing*. Charles C. Thomas.
10. Flanagan, J. C. (1954). The critical incident technique. *Psychological Bulletin*, 51(4), 327–357. https://doi.org/10.1037/h0061470
11. Kawakita, J. (1967). *Abduction*. Chuokoronsha.
12. Kipling, R. (1902). *Just So Stories*. Macmillan.
13. Köhnken, G., Milne, R., Memon, A., & Bull, R. (1999). The cognitive interview: A meta-analysis. *Psychology, Crime & Law*, 5(1-2), 3–27.
14. Krause, R., & Pernice, K. (2024). Affinity Diagramming. *Nielsen Norman Group*. https://www.nngroup.com/articles/affinity-diagram/
15. McNaughton, D. et al. (2008). Learning to Listen. *Topics in Early Childhood Special Education*, 27(4), 223–231.
16. Moody, W., Will, R. P., & Blanton, J. E. (1996). Enhancing knowledge elicitation using the cognitive interview. *Expert Systems with Applications*, 10(1), 127–133.
17. Nielsen, J. (2010). *Interviewing Users*. Nielsen Norman Group. https://www.nngroup.com/articles/interviewing-users/
18. Palmer, S. R., & Felsing, J. M. (2002). *A Practical Guide to Feature-Driven Development*. Prentice Hall.
19. Reynolds, T. J., & Gutman, J. (1988). Laddering theory, method, analysis, and interpretation. *Journal of Advertising Research*, 28(1), 11–31.
20. Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago.
21. Rosala, M. (2020). The Critical Incident Technique in UX. *Nielsen Norman Group*. https://www.nngroup.com/articles/critical-incident-technique/
22. Rosala, M., & Moran, K. (2022). The Funnel Technique. *Nielsen Norman Group*. https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/
23. Wake, B. (2003). INVEST in Good Stories, and SMART Tasks. *XP123.com*.
24. Wynne, M. (2015). Introducing Example Mapping. *Cucumber Blog*. https://cucumber.io/blog/bdd/example-mapping-introduction/
