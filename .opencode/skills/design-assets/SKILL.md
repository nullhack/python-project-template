---
name: design-assets
description: Author and update SVG visual assets using project branding identity
version: "1.0"
author: designer
audience: designer
workflow: branding
---

# Design Assets

Create or update `docs/assets/logo.svg` and `docs/assets/banner.svg` from the project's branding identity in `docs/branding.md`.

## When to Use

- Stakeholder requests a new or updated logo or banner
- `docs/assets/` is empty after project setup

## Step-by-Step

### 1. Read branding

Read `docs/branding.md`. Extract: project name, tagline, primary/accent colors, tone of voice. If colors are absent, run `skill design-colors` first.

### 2. Apply SVG structure rules

All SVGs must follow these constraints (W3C SVG 2 spec — CSS properties take precedence over presentation attributes; inline `<style>` required for cascade control):

- `viewBox="0 0 W H"` always set; no fixed `width`/`height` on `<svg>` root
- Colors via CSS custom properties: `--color-primary`, `--color-accent` with fallback hex
- System font stack: `font-family: system-ui, -apple-system, sans-serif` (no external imports)
- No external `<image>` refs; raster only if base64-inlined
- `role="img"` and `aria-label="<description>"` on every `<svg>` (WCAG 1.1.1 — non-text content requires text alternative)
- Readable at minimum display size: banner at 400px wide, logo at 32px

### 3. Banner layout

`viewBox="0 0 1200 300"`. Three zones:

- Left 20% — logo mark or geometric accent
- Center 60% — project name (48–64px, weight 700) + tagline (20–24px, weight 400)
- Right 20% — optional secondary graphic or empty

### 4. Logo layout

`viewBox="0 0 100 100"` (square). One recognizable shape readable at 16px. No text in the mark; create a separate lockup if text is needed.

### 5. Write the SVG

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" role="img" aria-label="<project-name> banner">
  <style>
    :root { --color-primary: #XXXXXX; --color-accent: #XXXXXX; }
    .bg    { fill: var(--color-primary); }
    .title { fill: #ffffff; font-family: system-ui, -apple-system, sans-serif; font-size: 56px; font-weight: 700; }
    .sub   { fill: var(--color-accent); font-family: system-ui, -apple-system, sans-serif; font-size: 22px; }
  </style>
  <rect class="bg" width="1200" height="300"/>
  <!-- content -->
</svg>
```

### 6. Commit

```bash
git add docs/assets/
git commit -m "design(assets): <create|update> <banner|logo>"
```

## Checklist

- [ ] `docs/branding.md` read before writing any SVG
- [ ] Colors sourced from `docs/branding.md`; `skill design-colors` run if absent
- [ ] `viewBox` set; no fixed `width`/`height` on `<svg>` root
- [ ] Colors use CSS custom properties with fallback hex
- [ ] System font stack; no external imports
- [ ] `role="img"` and `aria-label` present
- [ ] Banner readable at 400px wide; logo readable at 32px
- [ ] Files committed to `docs/assets/`
