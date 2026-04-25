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

## Why This Matters
This is Google Labs defining a standard for how agents consume design context — a direct parallel to what MCP does for tool/data access. If design.md gains adoption, it becomes part of the agentic AI stack alongside MCP. Relevant to your EA governance work: if Belron builds AI-assisted frontends or contact centre interfaces, agents will need to understand Belron's design system. This is the emerging standard for how that works.

**7.7k stars, 622 forks, Apache-2.0 — serious traction for an alpha.**

## Practical Takeaways
- [ ] Monitor for design.md reaching stable v1 — candidate for Belron EA standards consideration 📅 2026-05-09
- [ ] Cross-reference with MCP Governance — is there a design token MCP server pattern emerging? 📅 2026-05-02

## Related Knowledge
- **Connected projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]]
- **Related themes:** Agentic AI platforms, enterprise architecture standards, MCP/A2A protocols

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
