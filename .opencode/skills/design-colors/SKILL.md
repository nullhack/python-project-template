---
name: design-colors
description: "Select and validate a colour palette with WCAG contrast, dark-mode counterparts, and hue semantics"
---

# Design Colours

Available knowledge: [[design/color-systems#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Read `docs/branding.md` and extract the personality adjectives from the Identity section.
2. Propose a primary hue based on the hue-semantics table in [[design/color-systems#content]]. The primary must reinforce the personality adjectives.
3. Determine the saturation and value for the primary using the saturation–value personality map in [[design/color-systems#concepts]]. The same hue expresses different personalities at different saturation/value levels (e.g., blue at high saturation = "tech/digital"; blue at low saturation, dark value = "corporate/authoritative").
4. Select a harmony type based on the desired emotional effect per [[design/color-systems#concepts]]: complementary for vibrancy, split-complementary for balanced contrast, analogous for calm unity. For 2-colour brand marks, use complementary or split-complementary.
5. Propose an accent colour using the selected harmony type. Maximum 2 colours in the logo mark.
6. Propose background, text-primary, and text-secondary colours.
7. For each colour pair (text on background, accent on background, dark-mode primary on dark background), calculate the WCAG contrast ratio using the formula in [[design/color-systems#concepts]]. Every text–background pair must meet ≥4.5:1 (AA). Every large-text pair must meet ≥3:1.
8. Balance visual weight in the composition using Itten's contrast of extension per [[design/color-systems#content]] — verify that accent and primary areas follow the visual weight ratios (yellow:violet ≈ 1:3, orange:blue ≈ 1:2, red:green ≈ 1:1).
9. Propose dark-mode counterparts for each colour. Do not simply invert — use off-white (#e0e0e0 or similar) on dark backgrounds, and adjust accent saturation for dark contexts per [[design/color-systems#key-takeaways]].
10. Present the full palette to the stakeholder as a table: colour role, hex value, RGB, dark-mode hex, WCAG ratio on primary background, and the Itten visual weight ratio.
11. IF stakeholder approves → write the Visual section of `docs/branding.md`. IF stakeholder requests changes → revise and re-verify contrast ratios (go to step 2).
12. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.