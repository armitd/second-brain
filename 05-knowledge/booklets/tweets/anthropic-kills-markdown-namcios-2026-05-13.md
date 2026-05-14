---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/A Anthropic acabou de matar o Markdown.md"
date_processed: "2026-05-13"
created: "2026-05-13 17:10"
title: "Anthropic Is Killing Markdown (HTML as AI Output)"
author: "Felipe Demartini (@namcios)"
tags: ["#readwise", "#thread", "#agentic-ai", "#claude-code", "#ai-output-formats"]
relevance: "medium"
related_projects: ["mcp-governance"]
competitive_intel: true
status: "processed"
---

# Thread: Anthropic Is Killing Markdown — HTML as the New AI Output Format

## Summary
A Claude Code engineer published an article arguing that Markdown was never the right format for human-AI communication — it was just what we had. Now with 1M-token contexts, HTML as AI output is superior: interactive, visually rich, and usable as shared memory between agents. This Portuguese-language thread summarises the argument and its implications.

## Key Points
- Markdown assumes you'll read top-to-bottom; HTML assumes you want to interact with what matters
- Concrete examples: 30 project tickets → draggable kanban; rate-limiting logic → SVG flowchart with inline code; code reviews → colourised diffs with dependency graphs; animation params → sliders with live preview
- HTML is 2-4× slower to generate, but that cost effectively disappeared with million-token context windows
- Crucially: the generated HTML isn't just for humans — verifier agents also read it. The spec stops being a document and becomes **shared memory between agents**

## Why It Matters
The shift from Markdown-as-document to HTML-as-interface is directly relevant to agentic AI design and the future of agent-to-agent communication. If AI specs become living interfaces rather than static reports, this changes how MCP payloads, agent handoffs, and governance artefacts should be designed. Worth watching as a design signal for [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]].

**Competitive intel note:** Thread references work by a Claude Code (Anthropic) engineer — Anthropic is on the [[03-professional/COMPETITIVE-WATCHLIST|competitive watchlist]].

## Full Thread
[[Readwise/Full Document Contents/Tweets/A Anthropic acabou de matar o Markdown|Full thread (Portuguese) →]]

---
*Processed from Readwise by COG*
