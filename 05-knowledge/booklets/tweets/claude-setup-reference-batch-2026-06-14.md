---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
author: "Various"
tags: ["#readwise", "#thread", "#claude-setup", "#reference", "#claude-code", "#prompts"]
relevance: "medium"
related_projects: []
status: "processed"
---

# Claude Setup & Advanced Use — Reference Batch (June 2026)

Four full-thread captures covering Claude setup guides and advanced use patterns. Filed together as complementary reference material.

---

## 1. Karpathy's CLAUDE.md — 21 Rules (rewind/@0xDepressionn)

**Source:** Andrej Karpathy identified 4 rules; a developer expanded to 21 and published — 82,000 stars, #1 GitHub Trending. Coding accuracy: 65% → 94%.

**Karpathy's original 4 rules:**
1. Ask, don't assume — if unclear, ask before writing a single line
2. Simplest solution first — no abstractions not explicitly requested
3. Don't touch unrelated code — even if you think it could be improved
4. Flag uncertainty explicitly — before proceeding, not after

**Key cost framing:** Average developer spends 30 min/day re-explaining context to Claude. At $150/hour = $375/week. Team of 5 = $1,875/week. A CLAUDE.md file costs 2 hours to write.

**Three CLAUDE.md sections:** Defaults (who I am, what I know), Behaviour (scope lock, confirm before destroy, show what changed), Memory + Stack (MEMORY.md decision log, ERRORS.md failure log, tech stack lock).

**Full thread:** [[Readwise/Full Document Contents/Tweets/Andrej Karpathy spent 4 minutes in an interview explaining a...|Full thread →]]

---

## 2. Claude Can Do All of This — 17 Hidden Features (Anatoli Kopadze)

A comprehensive walkthrough of Claude features most users have never touched. Key items:

- **Projects** — persistent workspace with system prompt + uploaded files; most impactful single change
- **Memory** — builds a profile over time across conversations; off by default
- **Artifacts** — live preview panel for code/documents; changes the entire experience
- **Extended Thinking** — step-by-step reasoning mode; significant difference on complex tasks
- **Web Search** — real-time; most users don't know it exists
- **Claude in Chrome** — browser extension; Claude sees and acts on active tab
- **Cowork (desktop app)** — file system access; reads/edits actual files without copy-paste
- **Scheduled Tasks** — set once, runs on schedule, saves output to folder; turns Claude from reactive to proactive
- **Skills in Cowork** — install capabilities like plugins; persistent operational behaviors
- **Prompt Caching (API)** — `"cache_control": {"type": "ephemeral"}` on large system prompts; up to 90% cost reduction + faster responses

**Full thread:** [[Readwise/Full Document Contents/Tweets/Anthropic engineer.md|Full thread →]]

---

## 3. claude-code-setup Plugin (Suryansh Tiwari)

Anthropic released an official plugin: `/plugin install claude-code-setup@claude-plugins-official`

The plugin scans your project and recommends: hooks, skills, MCP servers, subagents, automations — then sets everything up step-by-step. Described as an "ecosystem bootstrapper" not just a setup utility.

Key framing: "The real power of Claude Code is the ecosystem around it. Claude Code by itself is powerful. Claude Code connected to hooks, skills, MCP servers, subagents, automations, memory systems becomes something entirely different. It stops behaving like a chatbot. It starts behaving like an operational AI environment."

Transition being described: "AI answers questions" → "AI participates inside systems" → "Autonomous operational environments"

**Full thread:** [[Readwise/Full Document Contents/Tweets/Claude Code feels completely different once you install this.md|Full thread →]]

---

## 4. ChatGPT is the iPhone, Claude is the Mac — 8 Advanced Prompts (Jack)

8-prompt system for power-user Claude workflows:
1. Persistent brain — operating profile at session start
2. Writing partner — deconstruct great writing, then replicate technique in your voice
3. Multi-role team — Strategist → Researcher → Writer → Editor → Distributor in sequence
4. Senior critique — explicitly frames for ruthless feedback, not validation
5. Structured decision framework — Type 1/2, bias detection, 10/10/10 rule
6. Executive synthesis — synthesise document into insight, not summary; "make me sound sharper for having read this"
7. Knowledge processing pipeline — mental model extraction + 7-day retention check
8. Weekly AI audit — grade your own Claude usage; identify busywork Claude could automate

**Full thread:** [[Readwise/Full Document Contents/Tweets/ChatGPT is the iPhone.md|Full thread →]]

---

## 5. Opus 4.8 Launch — Competitive Note (Alex Finn)

**Date:** May 28, 2026 (confirmed from @claudeai embed)

@claudeai: *"Introducing Claude Opus 4.8: it builds on Opus 4.7 with sharper judgment, more honesty about its own progress, and the ability to work independently for longer than its predecessors. Available today at the same price."*

Note: Alex Finn's framing includes "Dynamic Workflow mode" and "Ultracode mode" which appear to be speculative/hype additions beyond the official announcement. The official release note (sharper judgment, more honesty, longer independence) is the reliable signal.

**Competitive intel:** Claude Opus 4.8 shipped May 28, 2026 — added to COMPETITIVE-WATCHLIST under Anthropic.

---
*Processed from Readwise by COG*
