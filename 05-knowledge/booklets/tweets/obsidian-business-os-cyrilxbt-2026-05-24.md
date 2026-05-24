---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/this is how the founder of obsidian actually takes notes....md"
date_processed: "2026-05-24"
created: "2026-05-24 12:38"
title: "Obsidian as a Business Operating System — Claude + MCP + N8N"
author: "CyrilXBT (@cyrilXBT) via Rohit (@rohit4verse)"
tags: ["#readwise", "#thread", "#obsidian", "#second-brain", "#claude", "#mcp", "#n8n", "#agentic-ai", "#automation"]
relevance: "high"
related_projects: ["mcp-governance", "contact-centre-future"]
status: "processed"
---

# Thread: Obsidian as a Business Operating System

*CyrilXBT's full guide to automating a business via Obsidian + Claude + N8N — surfaced via Rohit (@rohit4verse). Published May 2026.*

## Summary

A structured framework for turning an Obsidian vault from a passive note repository into an active business operating system. Three layers: **Knowledge Layer** (Obsidian plain text), **Intelligence Layer** (Claude Code via MCP), **Automation Layer** (N8N). Together they create a business that operates without human initiation on routine work.

## Architecture (Three Layers)

| Layer | Tool | Role |
|---|---|---|
| Knowledge Layer | Obsidian (Markdown) | Permanent context — never inaccessible, never requires a subscription |
| Intelligence Layer | Claude Code via MCP | Reads files, processes information, makes connections, generates outputs |
| Automation Layer | N8N | Clock and nervous system — fires workflows on schedule and on trigger |

## Six Business Systems Automated

1. **Client Intelligence** — Pre-call brief auto-generated 30 mins before every client call; communication logger appends interactions to client folders
2. **Project Operations** — Daily project pulse at 6AM; auto-updates project status from daily note conventions (DONE: [project] — [deliverable])
3. **Content Production** — Morning content brief; draft engine via QUEUE folder; weekly performance tracker
4. **Financial Operations** — Revenue logging via RECEIVED: conventions; monthly financial brief on 1st of month; invoice reminder on 25th
5. **Research & Intelligence** — Daily intelligence brief; research queue for async processing overnight
6. **Performance & Review** — Weekly review Sunday 8PM; quarterly business review on Q1 day

## Key Design Principles

- **QUEUE folder is the async interface.** Drop a file → Claude processes on next cycle → output appears in GENERATED. You never wait for it; it never waits for you.
- **CLAUDE.md is the business constitution.** Every automated workflow reads it before acting. Generic AI outputs become business-specific because of this file.
- **N8N trigger types:** Cron (scheduled), File Watch (QUEUE folder changes), Webhook (Stripe payments, calendar events). Self-hosted on a $5 DigitalOcean droplet = unlimited runs.
- **Compounding effect:** At 6 months, Claude has studied your thinking continuously. Pre-call briefs calibrated to actual patterns. Research builds on months of context. Accumulated context is the moat.

## Why This Matters for Active Projects

- **COG / Second Brain:** The architecture here is essentially what COG already implements. Worth using as a design reference when evaluating whether COG is generating synthesis (feedback loop) or just accumulating files (storage).
- **MCP Governance:** The "Intelligence Layer (Claude Code via MCP)" framing validates the Belron MCP RA architecture — MCP as the interface between automation and knowledge stores is a pattern appearing across multiple sources.
- **CCOTF:** The async QUEUE/GENERATED pattern for back-office automation is analogous to what the CCOTF automation layer (layer ⑤) needs to implement. Same asynchronous loop concept.

## Full Thread
[[Readwise/Full Document Contents/Tweets/this is how the founder of obsidian actually takes notes....|Thread →]]
[[Readwise/Full Document Contents/Tweets/How to Build an Obsidian Knowledge Vault That Gets Smarter Every Day Without You Doing Anything|CyrilXBT standalone article →]]

---
*Processed from Readwise by COG*
