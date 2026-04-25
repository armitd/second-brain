---
type: "url-bookmark"
category: "tools"
domain: "github.com"
date_saved: "2026-04-25"
date_accessed: "2026-04-25"
url: "https://github.com/google-labs-code/design.md"
title: "design.md — Visual Identity Format for AI Coding Agents"
author: "Google Labs"
published: "2026"
tags: ["#bookmark", "#tool", "#agentic-ai", "#design-systems", "#enterprise-architecture", "#ai-tools", "#mcp"]
relevance: "high"
status: "to-evaluate"
related_projects: ["mcp-governance", "contact-centre-future"]
confidence: "high"
---

# design.md — Visual Identity Format for AI Coding Agents

## What It Does
A standardised format specification (YAML + markdown) that gives AI coding agents a persistent, structured understanding of a design system — both the exact design tokens and the human rationale behind them. Think of it as a machine-readable brand/design brief that any agent can consume.

## Key Features
- **Hybrid format:** YAML front matter for tokens (colours, typography, spacing, components) + markdown prose for design rationale
- **CLI tooling:** `lint`, `diff`, `export`, `spec` commands
- **Token interoperability:** Export to Tailwind and W3C Design Token Format (DTCG)
- **WCAG AA contrast checking** built in
- **Version diffing:** Detects regressions between design system iterations

## Strategic Context
design.md is part of **Stitch by Google** — Google's design-to-code agent product. By open-sourcing the spec, Google is making it tool-agnostic so it works across any platform, not just Stitch.

This was a **direct competitive move against Anthropic's Claude Design**, which has restrictive rate limits. Charly Wargnier (@DataChaz) noted: *"Anthropic really thought they had us locked down with Claude Design's ridiculous rate limits… and now Google has literally countered it straight away."* Announced 21 April 2026.

This is Google Labs defining a standard for how agents consume design context — a direct parallel to what MCP does for tool/data access. If design.md gains adoption, it becomes part of the agentic AI stack alongside MCP. Relevant to your EA governance work: if Belron builds AI-assisted frontends or contact centre interfaces, agents will need to understand Belron's design system. This is the emerging standard for how that works.

**7.7k stars, 622 forks, Apache-2.0 — serious traction for an alpha.**

## Additional Sources
- Official Google blog: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/
- DataChaz tweet thread: https://twitter.com/DataChaz/status/2047245316391670042
- Stitch by Google: https://twitter.com/stitchbygoogle

## Practical Takeaways
- [ ] Prototype design.md with a small Belron token set — test with Claude Code before waiting for v1 📅 2026-05-02
- [ ] Add a "design context standards for agentic interfaces" section to MCP Governance framework 📅 2026-05-02
- [ ] Flag to Belron brand/design system owner — this affects how brand standards are encoded for AI across all 35 countries and brands (Autoglass, Carglass, Safelite) 📅 2026-04-30
- [ ] Monitor vendor standard war — bet on Apache-2.0 open standard over Anthropic or Google proprietary versions 📅 2026-05-09
- [ ] Monitor for design.md reaching stable v1 — candidate for Belron EA standards consideration 📅 2026-05-09

## Related Knowledge
- **Connected projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]], [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW|AI Damage Assessment PoC]]
- **Related themes:** Agentic AI platforms, enterprise architecture standards, MCP/A2A protocols, brand governance

## Source Details
| Field | Value |
|-------|-------|
| Domain | github.com/google-labs-code |
| Author | Google Labs |
| Language | TypeScript (94.3%) |
| Status | Alpha — active development |
| Stars | 7.7k |
| License | Apache-2.0 |

## Processing Notes
- **Extracted:** 2026-04-25
- **Category Confidence:** 95% — open-source tool/spec from Google Labs
- **Review Needed:** no

---

*Processed by COG URL Curator*
