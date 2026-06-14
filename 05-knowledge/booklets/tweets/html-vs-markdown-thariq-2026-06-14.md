---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/A Anthropic acabou de matar o Markdown.md"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
author: "Thariq (@trq212), surfaced by Felipe Demartini (@namcios)"
tags: ["#readwise", "#thread", "#html", "#markdown", "#agent-outputs", "#mcp-governance", "#claude-code"]
relevance: "high"
related_projects: ["MCP Governance"]
status: "processed"
---

# Thread: HTML Over Markdown for Agent Outputs

**Author:** Thariq (@trq212), Anthropic Claude Code engineer — May 8, 2026

## Summary
A Claude Code engineer at Anthropic makes the case for HTML as the default output format over Markdown. The core argument: Markdown is for reading, HTML is for using. With 1M token context windows, the generation cost difference no longer matters. The most important implication: HTML specs become shared memory between agents, not just documents for humans.

## Key Points

- **Markdown assumption**: you'll read top to bottom. **HTML assumption**: you want to see what matters and interact with it.
- Markdown fails in practice — "I have found it difficult to read a markdown file of more than a hundred lines. I certainly am not able to get anyone else in my organisation to read it."
- HTML is 2–4x slower to generate than Markdown — but with 1M token context windows, this cost has effectively disappeared

### Real use cases replacing walls of Markdown text
- 30 project tickets → draggable Kanban with Now/Next/Later/Cut columns and export button
- Rate limiting logic → SVG flowchart with inline code
- Code review → colourised diff with dependency graphs between modules
- Animation parameters, colours, regex, cron jobs → sliders with live preview
- Project specs → 6 side-by-side options with interactive mockups

### The agent-to-agent implication (most important for MCP Governance)
> "The generated HTML is not just for humans. The verification agent also reads it. The spec has stopped being a document and become shared memory between agents."

**Markdown is a report. HTML is an interface. Reports are for reading. Interfaces are for continuing the work.**

- The verification agent reads the HTML spec with the same richness as the human — structured layout, linked sections, dependency diagrams
- This is a paradigm shift from "AI outputs text for humans to read" to "AI outputs structured artefacts that downstream agents consume"

### Practical start
Don't make a skill for it. Just ask Claude: "make an HTML file" or "make an HTML artifact." The trick is knowing what you want the artifact to do. Add a "copy as JSON" or "copy as prompt" button to turn UI edits back into something you can paste into Claude Code.

## Why It Matters
The MCP Governance project is thinking about specs, audit trails, and governance artefacts — all currently planned as Markdown documents. If the agent-verification pipeline is reading specs rather than just humans, HTML may be the right substrate for governance artefacts: richer, more parseable, interactive for human review. Worth exploring whether COG's own skill outputs should shift to HTML for multi-step workflows.

## Full Thread
[[Readwise/Full Document Contents/Tweets/A Anthropic acabou de matar o Markdown|Full thread →]]

---
*Processed from Readwise by COG*
