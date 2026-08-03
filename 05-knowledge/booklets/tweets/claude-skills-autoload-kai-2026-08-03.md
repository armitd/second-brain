---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/i genuinely can't understand why this isn't the first thing....md"
date_processed: "2026-08-03"
created: "2026-08-03 10:34"
title: "The Claude skills folder system nobody uses"
author: "kai (@0xkkai)"
tags: ["#readwise", "#thread", "#claude", "#agentic-ai", "#claude-code"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: The Claude Skills Folder System Nobody Uses

## Summary
Anthropic shipped a folder-based system where Claude loads specialized instructions automatically based on what's being asked — no prompt engineering required after initial setup. Drop a folder into a skills directory containing a SKILL.md that describes a trigger condition; Claude reads the description once, then silently pulls in the full skill (instructions, scripts, examples) only when relevant.

## Key Points
- Structure: a skill folder with a `SKILL.md` stating "trigger this when the user asks about X"
- Context stays empty until a skill is actually needed — one Claude instance behaves like many specialists without manual context management
- Example use cases given: a writing-voice skill (loads only when drafting), a codebase-conventions skill (loads only in that repo), an accounting-flow skill (loads only on invoice/receipt/expense mentions)

## Why It Matters
This is the same skills architecture this vault already runs on (COG's `.claude/skills/` directory) — useful as an external, independent description of why the pattern works, for anyone unfamiliar with how COG itself is structured.

## Full Thread
[[Readwise/Full Document Contents/Tweets/i genuinely can't understand why this isn't the first thing....md|Full thread →]]

---
*Processed from Readwise by COG*
