---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Your Claude setup rots over time. Detox it in 60 seconds (with this self-audit prompt).md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "Your Claude Setup Rots Over Time — CLAUDE.md Self-Audit Prompt"
author: "Ole Lehmann (@itsolelehmann)"
url: "https://twitter.com/itsolelehmann/status/2036533756572639611"
tags: ["#readwise", "#thread", "#claude-code", "#claude-md", "#context-engineering", "#maintenance"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Your Claude Setup Rots Over Time — CLAUDE.md Self-Audit Prompt

## Summary
Ole Lehmann identifies a key maintenance failure mode: CLAUDE.md files accumulate dead, contradictory, and redundant rules over time, which degrades Claude's output quality. The fix is a self-audit prompt that asks Claude to read all setup files and flag rules that are now default behaviour, contradict other rules, are redundant, were one-off fixes, or are too vague to act on. Pairs well with a weekly scheduled audit via Cowork scheduled tasks.

## Key Points
- **CLAUDE.md degrades without active pruning:** rules added for past problems persist and pollute future context
- **Self-audit prompt categories:** flag rules that are (1) now Claude's default behaviour, (2) contradictory, (3) redundant, (4) one-off fixes that don't generalise, (5) too vague to act on
- **Delete aggressively:** flagged rules should be removed, not archived
- **Schedule weekly:** pair with Cowork or similar to run the audit on a regular cadence
- **Signal of rot:** when Claude output quality drops despite no obvious prompt change, stale CLAUDE.md is a likely culprit

## Why It Matters
Directly applicable to COG's CLAUDE.md and skills. As skills accumulate, the same rot pattern will emerge. A periodic self-audit pass is a sensible addition to COG maintenance.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Your Claude setup rots over time. Detox it in 60 seconds (with this self-audit prompt).md|Full thread →]]

---
*Processed from Readwise by COG*
