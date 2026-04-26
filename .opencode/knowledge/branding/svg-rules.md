---
domain: branding
tags: [svg, assets, banner, logo, accessibility]
last-updated: 2026-04-26
---

# SVG Structure Rules

## Key Takeaways

- Set `viewBox` on every SVG root; no fixed `width`/`height`; use CSS custom properties for colors with fallback hex.
- Add `role="img"` and `aria-label` on every `<svg>` for WCAG 1.1.1 compliance; ensure readability at 400px wide (banners) and 32px (logos).
- Banners use `viewBox="0 0 1200 300"` with a three-zone layout: left accent (20%), center text (60%), right optional graphic (20%).
- Logos use `viewBox="0 0 100 100"` (square) with one recognizable shape readable at 16px; no text in the mark.

## Concepts

**SVG Structure Constraints**: All SVGs must follow W3C SVG 2 spec constraints: always set `viewBox`, never fixed dimensions, colors via CSS custom properties with fallback hex, system font stack (no external imports), no external `<image>` refs (raster only if base64-inlined), and WCAG accessibility attributes on every `<svg>` element.

**WCAG Accessibility**: Add `role="img"` and `aria-label` on every `<svg>` for WCAG 1.1.1 compliance. Ensure readability at minimum display sizes: 400px wide for banners, 32px for logos.

**Banner Layout**: Banners use `viewBox="0 0 1200 300"` with three zones: left accent (20%), center title+tagline (60%), right optional graphic (20%).

**Logo Layout**: Logos use `viewBox="0 0 100 100"` (square) with one recognizable shape readable at 16px, no text in the mark.

## Content

### SVG Structure Constraints

All SVGs must follow these constraints (W3C SVG 2 spec — CSS properties take precedence over presentation attributes; inline `<style>` required for cascade control):

- `viewBox="0 0 W H"` always set; no fixed `width`/`height` on `<svg>` root
- Colors via CSS custom properties: `--color-primary`, `--color-accent` with fallback hex
- System font stack: `font-family: system-ui, -apple-system, sans-serif` (no external imports)
- No external `<image>` refs; raster only if base64-inlined
- `role="img"` and `aria-label="<description>"` on every `<svg>` (WCAG 1.1.1 — non-text content requires text alternative)
- Readable at minimum display size: banner at 400px wide, logo at 32px

### Banner Layout

- `viewBox="0 0 1200 300"`
- Three zones:
  - Left 20% — logo mark or geometric accent
  - Center 60% — project name (48-64px, weight 700) + tagline (20-24px, weight 400)
  - Right 20% — optional secondary graphic or empty

### Logo Layout

- `viewBox="0 0 100 100"` (square)
- One recognizable shape readable at 16px
- No text in the mark; create a separate lockup if text is needed

### Example SVG Structure

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" role="img" aria-label="<project-name> banner">
  <style>
    :root { --color-primary: #XXXXXX; --color-accent: #XXXXXX; }
    .bg    { fill: var(--color-primary); }
    .title { fill: #ffffff; font-family: system-ui, -apple-system, sans-serif; font-size: 56px; font-weight: 700; }
    .sub   { fill: var(--color-accent); font-family: system-ui, -apple-system, sans-serif; font-size: 22px; }
  </style>
  <rect class="bg" width="1200" height="300"/>
</svg>
```

## Related

- [[branding/wcag-colors]] — color palette selection and contrast validation