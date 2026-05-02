---
name: design-assets
description: "Create logo and banner using favicon-first, monochrome-first, progressive-simplification process"
---

# Design Assets

Available knowledge: [[design/project-assets#key-takeaways]], [[design/visual-harmony#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Read `docs/branding.md` and extract the personality adjectives, visual metaphor (if any), and colour palette from the Visual section.
2. Determine the logo type per [[design/identity-design#concepts]]: combination mark (new brands), abstract mark (established names), pictogram (strong visual metaphor), or letterform (compact avatar).
3. Select primary shapes that reinforce the personality adjectives per [[design/visual-harmony#concepts]]: circles for unity/calm, squares for stability, triangles for energy, hexagons for precision. Reduce to 1–3 geometric primitives maximum.
4. Select typeface class, weight, and tracking per the typography–personality mapping in [[design/visual-harmony#content]]: serif for tradition/authority, sans-serif for modernity/clarity, with weight (light=premium, bold=assertive) and spacing (wide=open, tight=urgent) as personality levers.
5. **Sketch phase**: Generate 20–40 rough concepts in monochrome (black on white) per [[design/project-assets#concepts]]. Work small. No colour yet. Apply Gestalt principles: use proximity for unity, similarity for grouping, and closure for simplification per [[design/visual-harmony#concepts]].
6. Select the top 3–5 concepts. Refine in vector. Still monochrome. Compose using rule of thirds or golden ratio per [[design/visual-harmony#concepts]] — place primary element at an intersection point for dynamic tension, or dead centre for calm stability.
7. **Stress-test each concept** against the evaluation checklist per [[design/project-assets#concepts]]:
   - 5-second test (show, remove, ask "what did you see?")
   - Blur test (Gaussian blur 3–5px; silhouette must hold)
   - Monochrome test (pure black on white, pure white on black)
   - Scalability test (legible at 16px and 500px)
   - Proximity test (distinguishable from 5 competitor logos)
   - "One thing" test (one dominant feature, not multiple)
8. Present the strongest concept to the stakeholder with stress-test results. IF stakeholder rejects → return to step 5.
9. **Add colour**: Apply the brand primary and accent colours from `docs/branding.md`. Use the harmony type (complementary, split-complementary, or analogous) already selected in the design-colors state. Maximum 2 colours in the mark. Apply saturation–value personality mapping per [[design/color-systems#concepts]]. Test on white, black, and mid-gray backgrounds per [[design/color-systems#key-takeaways]].
10. Balance visual weight using Itten's contrast of extension per [[design/color-systems#content]] — a small saturated accent can carry equal visual weight to a large muted background area.
11. **Create delivery set** per [[design/project-assets#concepts]]:
    - `docs/assets/logo.svg` — Master SVG, square viewBox, presentation attributes only, SVGO-optimised
    - `docs/assets/logo-dark.svg` — Dark-mode variant (or embedded `@media (prefers-color-scheme: dark)`)
    - `docs/assets/banner.svg` — README banner, composed using rule of thirds, tested on light and dark backgrounds
12. **Create favicon set** per [[design/project-assets#concepts]]: favicon.ico, icon.svg (with dark-mode media query), apple-touch-icon.png, icon-192.png, icon-512.png. Each size tier progressively simplified per [[design/project-assets#concepts]].
13. Update `docs/branding.md` Visual section with asset paths.
14. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.