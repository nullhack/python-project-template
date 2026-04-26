---
name: design-colors
description: Select and validate a project color palette with WCAG contrast compliance
version: "1.0"
author: designer
audience: designer
workflow: branding
---

# Design Colors

Select a color palette for the project and validate it for accessibility. Propose the result for `docs/branding.md` — changes require stakeholder approval.

## When to Use

- Stakeholder provides a theme word or asks for a color palette
- `docs/branding.md` exists but has no colors yet
- Stakeholder requests a color change

## Step-by-Step

### 1. Read branding context

Read `docs/branding.md`. If colors are already set and the stakeholder has not asked to change them, stop — do not overwrite.

### 2. Select primary hue

Map the project theme or mission to a hue. See [[branding/wcag-colors]] for the hue semantics table mapping themes to hues and their semantic meanings.

### 3. Build the palette

Use a complementary scheme by default — a muted primary plus a pure complementary accent. See [[branding/wcag-colors]] for the complementary color scheme theory, primary/accent definitions, and when alternative schemes are appropriate.

### 4. Validate WCAG 2.1 AA

Any color used as a text background must achieve at least 4.5:1 contrast with white `#FFFFFF`. See [[branding/wcag-colors]] for the WCAG 2.1 AA contrast formula and calculation steps. If contrast is below 4.5:1, darken the primary until compliant. Accent colors on non-text surfaces are exempt.

### 5. Propose to branding

Update `docs/branding.md` under `## Visual` (requires stakeholder approval):

```markdown
- **Primary color:** `#XXXXXX`  — <hue> (<semantic rationale>)
- **Accent color:** `#XXXXXX`   — <hue> (<semantic rationale>)

> Colors meet WCAG 2.1 AA (X.X:1 contrast) when white text is placed on the primary.
```

## Checklist

- [ ] Existing colors checked before proceeding
- [ ] Hue chosen from theme/mission semantics
- [ ] Primary is muted/deep (not pure saturated)
- [ ] Accent is complementary or stakeholder-specified
- [ ] White-on-primary contrast >= 4.5:1 calculated and reported
- [ ] `docs/branding.md` updated with hex codes, rationale, and contrast note