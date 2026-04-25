---
version: alpha
name: Belron Brand Design System
description: Visual identity tokens and rationale for the Belron® brand, derived from the official Belron Brand Guidelines. For use by AI coding agents building Belron-branded digital interfaces.

colors:
  primary: "#e13a2b"
  yellow: "#ffdd00"
  neutral: "#575756"
  white: "#ffffff"
  purple: "#373896"
  teal: "#02ab93"

typography:
  headline:
    fontFamily: Helvetica Neue
    fontWeight: 700
    lineHeight: 1.1
  subheading:
    fontFamily: Helvetica Neue
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: Helvetica Neue
    fontWeight: 300
    lineHeight: 1.5
  headline-digital:
    fontFamily: Arial
    fontWeight: 700
    lineHeight: 1.1
  body-digital:
    fontFamily: Arial
    fontWeight: 400
    lineHeight: 1.5

spacing:
  logo-min: "90px"
  gutter: "4px"
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "48px"

rounded:
  none: "0px"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    typography: "{typography.headline-digital}"
  button-secondary:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.neutral}"
    typography: "{typography.body-digital}"
  surface-default:
    backgroundColor: "{colors.white}"
  surface-brand:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
  surface-accent:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.neutral}"
  heading:
    textColor: "{colors.neutral}"
    typography: "{typography.headline}"
  body-text:
    textColor: "{colors.neutral}"
    typography: "{typography.body}"
---

# Belron® Brand Design System

## Overview

Belron® is the world's leading vehicle glass repair and replacement company, operating across 34+ countries under brands including Autoglass, Carglass, and Safelite. The brand communicates **clarity, confidence, and contemporary professionalism**.

Clarity is the governing principle across all communications. Layouts should feel open and uncluttered. White space is a design element — embrace it generously. A minimal approach is required: not all colours used simultaneously, no clashing combinations, and always as few details as necessary.

The brand has a bold, geometric character rooted in its signature 34° angle motif, which appears across all collateral as a corner cut on colour blocks and images. This angle exactly mirrors the corners of the Belron® logo graphic device.

## Colors

The lead palette is yellow, neutral grey, and red — used in combinations across all communications. White space is equally important and must be treated as a colour.

- **Primary / Red (`#e13a2b`):** The most dominant brand colour. Used for primary calls-to-action, key headlines, and brand-defining moments. Pantone 485 C. When red dominates a layout (50%+), other colours should appear at small percentages only.
- **Yellow (`#ffdd00`):** Warm and high-energy. Used for backgrounds, the Belron® angle device, and highlights. Pantone 109 C. Never use at equal weight to primary red — one must dominate.
- **Neutral / Grey (`#575756`):** The anchor. Used for body text, secondary surfaces, and balance. Pantone Cool Gray 10 CP. Prevents the palette from becoming too saturated.
- **White (`#ffffff`):** Essential. Generous white space creates the contemporary look that defines the brand. Always embrace it.
- **Purple (`#373896`):** Primarily for internal communications. Use externally only as a small accent, highlight, or within text. Pantone 267 C. Never dominant on external-facing interfaces.
- **Teal (`#02ab93`):** Primarily for internal communications. Same rules as purple for external use. Pantone 3275 C. Do not associate teal with any specific topic or section.

Tints of any palette colour can add depth when a full colour doesn't work in context. When one lead colour dominates, complement with only small percentages of others.

**Don'ts:** Never use all colours simultaneously. Avoid clashing combinations such as red and purple at equal weight. Never create a rainbow effect.

## Typography

Helvetica Neue is the heart of the Belron® visual style — a geometric sans-serif that communicates clarity and modernity. Use varied weights to create strong typographic contrast.

- **Headlines:** Helvetica Neue Bold (700) — print, events, online graphics
- **Subheadings:** Helvetica Neue Regular (400)
- **Body:** Helvetica Neue Light (300)
- **Digital substitute:** Arial — used for web, email, PowerPoint, Word where Helvetica Neue is unavailable

Font stack for digital: `"Helvetica Neue", Arial, sans-serif`

Never use decorative or complex typefaces. The simple, open quality of these fonts adds to the feeling of space.

## Layout & Spacing

Belron® uses a compact grid system flexible for any requirement.

- **Portrait layouts:** 6-column grid | 19mm margins | 4mm gutters
- **Landscape layouts:** 8-column grid | 19mm margins | 4mm gutters
- **Logo minimum (print):** 30mm wide
- **Logo minimum (digital):** 90px wide
- **Logo exclusion area:** Width of the 'B' character in the logo — keep clear on all sides

The grid can be used in any combination of columns. Layouts should feel open — do not pack content into every column.

## Shapes

The **Belron® angle** is the defining geometric motif — a 34° corner cut applied to blocks of colour, images, or textures. It exactly mirrors the corners of the Belron® logo graphic device.

**Rules:**
1. Always exactly 34° — never approximate
2. One corner per element only
3. Top-right or bottom-left of a colour block only
4. Logo preferred at bottom-right when angle is used — never bottom-left or top-right alongside the angle
5. The Belron® stripe anchors the logo

**Stripe sizes:** A0: 7mm | A1: 6mm | A2: 5mm | A3: 4mm | A4–A6: 3mm. Landscape = right edge. Portrait = bottom edge. Consistent colour per campaign — never multiple stripe colours in one campaign.

## Components

**Logo integrity — absolute rules:**
1. Never change the colours
2. Never stretch or compress
3. Never add drop shadows
4. Never remove graphic devices
5. Never crop
6. Never resize individual elements
7. Always opaque solid form — never transparent
8. Always full-colour with ® symbol

**Icons:** 2D flat style, full colour palette, simple structure. Can appear in a box, solid on white, or white reversed out of an image. Always legible. Do not associate colours with specific topics.

**Textures:** Broken Screen, Ice, Leaf, Clouds, Raindrops, Sunbeams. Colour tint overlays permitted. Never place over people.

## Do's and Don'ts

**Do:**
- Embrace generous white space
- Use one dominant lead colour per layout
- Use varied type weights for hierarchy
- Apply 34° angle to one corner only
- Maintain logo exclusion area
- Validate colour contrast against WCAG AA

**Don't:**
- Use all colours simultaneously
- Use purple or teal as dominant colours on customer-facing interfaces
- Alter the logo in any way
- Apply the angle to more than one corner
- Position logo bottom-left or top-right when angle is present
- Use multiple stripe colours in one campaign

---

*Generated from Belron® Brand Guidelines (© Belron® 2017) | Validate against current brand guidelines before production deployment*
