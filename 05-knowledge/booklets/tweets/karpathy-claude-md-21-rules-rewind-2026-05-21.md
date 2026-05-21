---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Andrej Karpathy spent 4 minutes in an interview explaining a....md"
date_processed: "2026-05-21"
created: "2026-05-21 14:16"
title: "Karpathy's CLAUDE.md — The 21-Rule Framework for Claude Code"
author: "@0xDepressionn (via @rewind02)"
tags: ["#readwise", "#thread", "#claude-code", "#productivity", "#ai-workflow"]
relevance: "high"
related_projects: []
braindump_candidate: false
braindump_actioned: "2026-05-21"
braindump_outcome: "Behaviour Rules, Permanent Facts, and ERRORS.md added to CLAUDE.md and vault root"
status: "processed"
---

# Thread: Karpathy's CLAUDE.md — The 21-Rule Framework for Claude Code

## Summary
Andrej Karpathy identified 4 behaviours that make Claude Code fail; a developer (@0xDepressionn) expanded them into 21 rules organised into three sections: **Defaults** (context and communication), **Behaviour** (scope control), and **Memory + Stack** (persistent context). The post went viral — 82,000 GitHub stars, #1 trending. Coding accuracy reportedly improved from 65% to 94%.

## Key Points

### Section 1 — Defaults (stop re-explaining yourself)
- Kill filler phrases; start every response with the actual answer
- Match response length to task complexity
- Show 2-3 approach options before acting
- Admit uncertainty explicitly before including it
- Declare who you are, what you know, what you're still learning — once
- Lock your current project context in a permanent prompt
- Define your writing voice and style parameters

### Section 2 — Behaviour (stop unauthorised changes)
- Scope lock: only modify what was explicitly requested; mention other issues but don't touch them
- Confirm before rewriting any existing content
- Hard stop before any destructive action (deleting files, dropping DB records, overwriting)
- Production environment actions require explicit in-session confirmation — no exceptions
- Always summarise what changed: files touched, modifications, files not touched, follow-up needed
- Never send, post, or schedule anything without explicit in-session confirmation
- Think through architecture and debugging before writing any code

### Section 3 — Memory + Stack (stop forgetting decisions)
- Maintain a `MEMORY.md` decision log — what was decided, why, what was rejected and why
- End-of-session summary written to `MEMORY.md` when prompted
- Maintain an `ERRORS.md` failure log — approaches that didn't work and what worked instead
- Permanent facts list: always-true constraints Claude must apply every session
- Lock the tech stack — never suggest alternatives unless asked
- Use extended thinking for architecture, performance tradeoffs, database design
- Karpathy's original 4 rules: (1) Ask don't assume, (2) Simplest solution first, (3) Don't touch unrelated code, (4) Flag uncertainty explicitly

## The Economics Case Made in the Thread
- 30 min/day re-explaining context = **$375/week per developer** at $150/hr
- 1 hr/week reverting unauthorised changes = **$225/week per developer**
- 2 hrs/week recovering from forgotten decisions = **$375/week per developer**
- Total: **$975/week per developer** — team of 5: **$253,500/year**
- CLAUDE.md setup: 2 hours. Karpathy's 4 rules alone: 2 minutes.

## Why It Matters
The framework directly applies to how Armo uses Claude Code daily. The MEMORY.md pattern in particular mirrors what COG's auto-memory system does at the conversation level — this is the project-level equivalent. The ERRORS.md idea is novel and worth adopting.

## ⚠️ Braindump Candidate
This thread contains a complete, structured framework (>500 words of original thinking) directly applicable to active Claude Code workflows. Consider running `/braindump` on this content to extract what to adopt from the 21 rules into your own CLAUDE.md.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Andrej Karpathy spent 4 minutes in an interview explaining a....|Full thread →]]

**Source tweet:** [View on X](https://twitter.com/rewind02/status/2056850947947827403) | Thread by: [View original](https://twitter.com/0xDepressionn/status/2055999112470839383)

---
*Processed from Readwise by COG*
