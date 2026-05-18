---
domain: writing
tags: [ai-writing, detection, language-markers, rlhf-bias, humanization]
last-updated: 2026-05-18
---

# AI Language Markers

## Key Takeaways

- Identify vocabulary overrepresentation — some words appear 10-48,000x more frequently in AI than human writing, with intensifier adverbs (significantly, effectively, increasingly) as additional vocabulary-level signals.
- Attribute marker patterns to RLHF annotation bias and formal-source training dominance — the "delve" origin (Nigerian annotator selection bias) illustrates the mechanism.
- Detect hedging verbs ("ensuring/ensures" at 4.3x, "rather than" at 2.5x) and filler phrases ("It's worth noting that" at 31x) as the strongest 2026-era signals.
- Recognize structural formulaicity: em dash overuse (2.6x), "X plays a crucial role in shaping Y" (most formulaic trigram), uniform sentence length, rule of three.
- Distinguish chatbot artifacts ("Absolutely!", "Great question!", "I'd be happy to help!") as conversational voice markers separate from content markers.
- Apply multi-signal detection scoring across vocabulary, structure, hedging, voice, and model-specific dimensions — no single marker is diagnostic; 5+ hits across tiers indicates likely AI generation.
- Claude-specific patterns (first-person avoidance, compulsive balance, conclusion recycling) are subtler than vocabulary markers but form a consistent fingerprint; multi-turn conversations accumulate verbal tics 110% by turn 5+.

## Concepts

**Vocabulary Overrepresentation** — LLMs use certain words at rates 10-48,000x higher than human writers. The most extreme cases (breathtaking: 36,261x; vibrant: 1,260x; intricate: 115x; testament: 228x) come from corpus analysis comparing AI and human text at scale. These words appear in formal writing (tourism, academic, marketing) that dominates training data, then get amplified by RLHF reviewers who rate formal-sounding text higher. Intensifier adverbs (significantly, effectively, increasingly, remarkably, undeniably) function as vocabulary-level padding that inflates claims without evidence.

**RLHF Annotation Bias** — The "delve" origin story is illustrative: research traced the 48x overrepresentation to many RLHF annotators being from Nigeria, where "delve" is common in business English. This selection bias amplified the word globally across all LLM output. Each training stage (pre-training on formal sources, RLHF preference for "neutral competence") narrows style toward technically correct but distinctive-free writing. More broadly, LLMs are trained on formal sources (Wikipedia, academic papers, news) where these words naturally occur, and human reviewers in RLHF consistently rate formal-sounding text higher. Each training stage narrows the style toward "neutral competence" — technically correct but stripped of anything distinctive.

**Hedging Verbs and Filler Phrases** — AI systematically inflates significance: every topic is "pivotal" or "crucial," every change "shapes" something, every feature "serves as" something. The copula avoidance pattern (using "serves as" instead of "is") shows a 10%+ decrease in "is"/"are" usage post-2023. WriteHuman's 2026 data shows "ensuring/ensures" at 4.3x overrepresentation and "rather than" at 2.5x (17,251 AI vs 6,859 human occurrences). Filler phrases add zero information value: "It's worth noting that" (31x), "It's important to note" (27x), "In today's digital age" (24x), "In the realm of" (22x).

**Structural Formulaicity** — AI text exhibits low "burstiness" (uniform sentence length), consistent use of the rule of three, and formulaic constructions like "Not X, but Y" and "X plays a crucial/critical/important role in shaping Y" (statistically the most formulaic trigram in WriteHuman's 80K+ dataset). Em dashes appear 2.6x more often in AI text (18.5% of AI inputs contain ≥1 vs 7.1% human), at 1 per 50-80 words vs human 1 per 500 words. Repetition-penalty code produces unnatural synonym cycling (character → protagonist → central figure → key player).

**Chatbot Artifacts** — These are "helpful assistant" voice markers: "Absolutely!", "Great question!", "I'd be happy to help!", "I hope this helps!", "Let me break this down", excessive bold formatting. These are specific to chatbot interactions rather than generated content, but persist in any conversational AI output. They are distinguishable from content markers because they index conversational role rather than topic or structure.

**Multi-Signal Detection Scoring** — No single marker definitively identifies AI writing; detection requires scoring across multiple dimensions simultaneously. The humanize-writing GitHub project established a heuristic where 5+ hits across vocabulary (3+ Tier 1 words, 5+ Tier 2 words), structural (uniform sections, rule of three, em dash frequency), and stylistic (hedging, significance inflation, absence of colloquial language) dimensions indicates likely AI generation. Multi-signal scoring is necessary because individual markers occur naturally in human writing, particularly formal and academic contexts.

## Content

### Tier 1: Single-Word Red Flags (overrepresented 9-36,000x vs human)

| Word | AI vs Human Frequency | Source |
|------|----------------------|--------|
| breathtaking | 36,261x | TextVisualization.app corpus |
| vibrant | 1,260x | TextVisualization.app corpus |
| testament | 228x | TextVisualization.app corpus |
| intricate | 115x | TextVisualization.app corpus |
| delve | 48x | Scientometrics study (2024 PubMed spike) |
| tapestry | 25-35x | TextVisualization.app corpus |
| multifaceted | 28x | Pangram Labs, Humanize AI Pro |
| nuanced | 22x | Reddit, detection tools |
| landscape (metaphorical) | 10-19x | Multiple sources |
| pivotal | 16x | Wikipedia AI writing page |
| crucial | 14x | Multiple sources |
| leverage (verb) | 13x | Noren, Humaneer |
| robust | 12x | Multiple sources |
| streamline | 11x | Multiple sources |
| utilize | 10x | Multiple sources |
| facilitate | 10x | Multiple sources |
| paramount | 9x | Multiple sources |
| endeavor | 9x | Multiple sources |
| realm | Clustered | Multiple sources |
| beacon | Clustered | Wikipedia AI writing page |
| underscore | Clustered | WriteHuman 2026 |
| foster | Clustered | Reddit, Wikipedia |
| embark | Clustered | Multiple sources |
| showcase/showcasing | Clustered | Wikipedia AI writing page |
| meticulous/meticulously | GPT-4 era hallmark | Wikipedia AI writing page |
| garner | GPT-4 era | Wikipedia AI writing page |
| bolster | GPT-4 era | Wikipedia AI writing page |
| kaleidoscope | Reddit-flagged | Reddit (300+ comments) |
| scaffold | Academic metaphor | Writing community lists |
| navigate (metaphorical) | Clustered | Multiple sources |
| harness | Clustered | Anti-slop, HumanizerTech |
| unlock | Clustered | Anti-slop, HumanizerTech |
| unveil | Clustered | Anti-slop, slopwash |
| champion (verb) | Clustered | Anti-slop |
| elevate (verb) | Clustered | Anti-slop, HumanizerTech |
| illuminate (verb) | Clustered | Anti-slop |
| seamless | Clustered | Bloomberry, Anti-slop |
| innovative | Clustered | Anti-slop, slopwash |
| ecosystem (metaphorical) | Clustered | Anti-slop |
| framework (metaphorical) | Clustered | Anti-slop |
| paradigm | Clustered | Anti-slop |
| synergy | Clustered | Anti-slop, corporate-speak lists |
| catalyst (metaphorical) | Clustered | Anti-slop |
| transformative | Clustered | Anti-slop, Bloomberry |
| compelling | Clustered | HumanizerTech |
| profound | Clustered | Anti-slop |
| scalable | Clustered | Anti-slop |
| optimize (non-technical) | Clustered | Anti-slop, HumanizerTech |
| empower | Clustered | Anti-slop, slopwash |
| maximize (non-technical) | Clustered | Anti-slop |
| embody | Clustered | Anti-slop |
| revolutionize | Clustered | Anti-slop, Bloomberry |
| boilerplate (noun) | Self-referential marker | Slopwash (detection category becomes the marker) |

### Tier 2: Hedging Verbs (2026 strongest signals)

| Word/Phrase | Overrepresentation | Source |
|-------------|-------------------|--------|
| ensuring/ensures | 4.3x | WriteHuman 2026 |
| highlights | Top 5 hedging verb | WriteHuman 2026 |
| supports | Top 5 hedging verb | WriteHuman 2026 |
| reflects | Top 5 hedging verb | WriteHuman 2026 |
| rather than | 2.5x (17,251 AI vs 6,859 human) | WriteHuman 2026 |

### Tier 3: Structural/Formulaic Patterns

| Pattern | Evidence | Source |
|---------|----------|--------|
| Em dash overuse | 18.5% AI vs 7.1% human (2.6x); 1/50-80 words vs 1/500 human | WriteHuman, Wikipedia |
| "X plays a crucial role in shaping Y" | Most formulaic trigram in dataset | WriteHuman 2026 |
| "capable of X" vs "able to X" | Highest-leverage humanization swap | WriteHuman 2026 |
| Copula avoidance ("serves as" vs "is") | 10%+ decrease in "is"/"are" post-2023 | Academic study |
| Significance inflation | Everything is "pivotal"/"crucial"/"groundbreaking" | Avasdream |
| -ing trailing clauses | "...highlighting its importance" restates what was said | Avasdream |
| "Not X, but Y" construction | Overused comparative structure | Wikipedia |
| Rule of three | Suspicious consistency in grouping | Wikipedia |
| Synonym cycling | Repetition-penalty produces unnatural rotation | Wikipedia |
| Uniform sentence length | Low burstiness, metronomic rhythm | Academic research |

### Tier 4: Filler Phrases

| Phrase | AI vs Human | Source |
|--------|-------------|--------|
| "It's worth noting that" | 31x | Humanize AI Pro |
| "It's important to note" | 27x | Humanize AI Pro |
| "In today's digital age" | 24x | Humanize AI Pro |
| "In the realm of" | 22x | Humanize AI Pro |
| "It is important to understand" | 20x | Humanize AI Pro |
| "In conclusion" / "To summarize" | 8-9x | Multiple sources |
| "As we navigate" | Clustered | Multiple sources |
| "Let's dive in" / "Let's explore" | Chatbot artifacts | Reddit, Wikipedia |
| "Whether you're a [X] or a [Y]" | Template scaffolding | Noren |
| "Here's the thing/kicker/deal" | Conversational filler | Anti-slop, slopwash |
| "Imagine a world where" | Grandiose opener | Anti-slop |
| "Fear not" | Archaic reassurance | Anti-slop |
| "That being said" | Hedging transition | Detection lists |
| Generic positive close | AI conclusion pattern | Multiple sources |

### Tier 5: Chatbot Artifacts ("Helpful Assistant" Voice)

| Artifact | Typical Source |
|----------|---------------|
| "Absolutely!" / "Certainly!" | ChatGPT |
| "Great question!" | Gemini |
| "I'd be happy to help!" | Claude |
| "I hope this helps!" | Claude |
| "Let me break this down" | ChatGPT |
| "That's a fantastic point" | All models |
| Excessive bold formatting | All models |

### Tier 6: Intensifier Adverbs

| Word | Source |
|------|--------|
| significantly | WriteHuman 2026 |
| effectively | WriteHuman 2026 |
| directly | WriteHuman 2026 |
| increasingly | WriteHuman 2026 |
| remarkably | Detection lists |
| undeniably | Detection lists (25% AI vs 5% human) |

### Detection Scoring Dimensions

No single marker is diagnostic. Multi-signal detection scores across these dimensions (5+ hits = likely AI-generated):

| Dimension | Signals |
|-----------|---------|
| Vocabulary | 3+ Tier 1 words, 5+ Tier 2 words |
| Structure | Uniform sections, rule of three, identical list lengths |
| Punctuation | Em dashes more than once per 3-4 paragraphs |
| Hedging | Every claim hedged, significance inflation in opening/closing |
| Filler | "It's worth noting" or similar filler phrases |
| Voice | No sentences under 8 words, no colloquial language, no personality |
| Comparative | "Not X, but Y" appears more than twice |
| Claude patterns | 3+ Tier 7 structural patterns present |

Source: humanize-writing GitHub reference, Bloomberry 2026 study (82% of AI outputs contain 2+ of: hedge openers, tricolon lists, em-dash connectors, resolution closers).

### Tier 7: Claude-Specific Structural Patterns

Claude produces smoother, less detectable prose than ChatGPT (70-85% detection vs 85-95%). These patterns are subtler than vocabulary markers but form a consistent fingerprint:

| Pattern | Description | Detector Weight |
|---------|-------------|----------------|
| First-person avoidance | Uses "one might argue", "it could be suggested" instead of "I think" — Constitutional AI safety artifact | Medium |
| Systematic scope acknowledgement | Pre-emptive limitations at predictable positions ("of course, this is just one perspective") | Medium |
| Compulsive balance | Always presents both sides, even when the prompt asks for a position | High |
| Three-part list compulsion | RLHF artifact from evaluators rewarding triads; more rigid than human grouping | Medium |
| Conclusion recycling | Restate → summarise → gesture forward, mechanically consistent | High |
| Extended analogy preference | Verbose structural development of single metaphor rather than brief comparison | Low |
| Smooth paragraph transitions | No abrupt shifts; every paragraph bridge is explicitly signposted | Medium |
| "according to the text" / "based on the text" | Claude-specific citation phrasing (arXiv TF-IDF analysis across 8 models) | High |

Claude also produces longer average sentence length with more complex clause structures than ChatGPT, and more consistent Markdown formatting.

Verbal tic accumulation (arXiv 2604.19139): Multi-turn conversations show 110% increase in verbal tics by turn 5+. Review multi-turn outputs with heightened scrutiny.

## Related

- [[agent-design/principles]]
