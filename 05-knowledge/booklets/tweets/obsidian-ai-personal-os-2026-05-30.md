---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/How to Turn Obsidian Into a Personal Operating System That Never Breaks Down.md, Readwise/Full Document Contents/Tweets/Six months ago my Obsidian vault had 2,000 notes and....md, Readwise/Full Document Contents/Tweets/OBSIDIAN CREATES TENSION BETWEEN YOUR NODES.md, Readwise/Full Document Contents/Tweets/This is what happens when you actually connect Claude to....md, Readwise/Full Document Contents/Tweets/This is how you compress 100 hours of content into....md, Readwise/Full Document Contents/Tweets/THIS MAN HASN'T OPENED HIS TASK MANAGER IN A WEEK....md, Readwise/Tweets/Tweets From Leopardracer.md, Readwise/Tweets/Tweets From Mr. Buzzoni.md"
date_processed: "2026-05-30"
created: "2026-05-30 10:11"
title: "Obsidian + AI as personal operating system"
author: "CyrilXBT, Leopardracer, Mr. Buzzoni, Dami-Defi"
tags: ["#readwise", "#thread", "#obsidian", "#second-brain", "#ai", "#productivity", "#claude-code"]
relevance: "medium"
related_projects: []
status: "processed"
---

# Thread Cluster: Obsidian + AI as Personal Operating System

## Summary
A cluster of threads from late May 2026 describing the same architecture: Obsidian as a structured storage layer, Claude (via MCP filesystem access) as the intelligence layer, and automation (N8N or similar) as the third layer that makes the system self-maintaining. The central claim is that most Obsidian systems fail because they require manual maintenance on bad days — the three-layer architecture solves this.

## Key Points

### The three-layer architecture (CyrilXBT / "How to Turn Obsidian into a Personal OS")
- **Layer 1 — Storage:** Obsidian. Plain text Markdown. Human-readable and machine-readable.
- **Layer 2 — Intelligence:** Claude Code connected via Filesystem MCP. Reads vault, makes connections, generates outputs, updates files.
- **Layer 3 — Automation:** N8N (on a $5 server). Schedules workflows, fires triggers, calls Claude API, passes data between systems without user initiation.
- Without automation: "a tool you use." Without intelligence: "an archive." All three together: "a system that operates."

### Why most Obsidian systems break
- **Manual maintenance burden** — requires regular updates to stay accurate; falls behind when life gets busy; abandoned when unreliable
- **Complexity compounding** — simple structure grows baroque; 20 minutes to navigate after 6 months
- **No intelligence layer** — captures information but never surfaces it contextually

### The vault organization problem (CyrilXBT / "Six months ago...")
- Most people organize Obsidian like a filing cabinet (optimized for storage) rather than a thinking system (optimized for retrieval)
- Tags applied inconsistently are worse than no tags at all
- The fix: rebuild the structure around retrieval pathways, not folder hierarchy

### Content compression (Mr. Buzzoni / Leopardracer)
- NotebookLM + Obsidian workflow: YouTube-to-NotebookLM extension dumps entire channels into NotebookLM → structured mega-summary in minutes → Audio Overviews for passive consumption
- Leopardracer: Claude connected to vault reads books, generates flashcards and mind maps from highlights

## Why It Matters
Relevant to COG's architecture design. The three-layer model (Obsidian + Claude via MCP + automation) is essentially what COG is building toward. The "bad day design" principle — systems should be durable when you're inconsistent, not only efficient when you're disciplined — is a useful framing for evaluating whether COG's current structure is resilient enough.

## Full Threads
[[Readwise/Full Document Contents/Tweets/How to Turn Obsidian Into a Personal Operating System That Never Breaks Down.md|Full Obsidian OS thread →]]
[[Readwise/Full Document Contents/Tweets/Six months ago my Obsidian vault had 2,000 notes and....md|Vault organization thread →]]

---
*Processed from Readwise by COG*
