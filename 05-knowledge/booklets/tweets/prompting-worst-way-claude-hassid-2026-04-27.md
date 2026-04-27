---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Prompting is the worst way to use Claude.md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "Prompting Is the Worst Way to Use Claude — Claude Cowork Setup"
author: "Ruben Hassid"
url: "https://twitter.com/rubenhassid/status/2042558212990292013"
tags: ["#readwise", "#thread", "#claude", "#claude-cowork", "#context-engineering", "#workflow"]
relevance: "medium"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Prompting Is the Worst Way to Use Claude — Claude Cowork Setup

## Summary
Detailed guide to the Claude Cowork setup: replace ad-hoc prompting with a persistent file system that Claude reads before every task. Three core files (about-me, anti-ai-writing-style, my-company) plus a 4-folder structure. Also covers token management, Wispr Flow voice dictation, and the April 2026 Cowork update.

## Key Points
- **8 files replace prompting:** about-me.md (identity), voice-profile.md (writing taste), anti-ai-writing-style.md (what to avoid), Cowork folder (4-folder system), Global Instructions, one starter prompt, Connectors, Plugins
- **3-folder Cowork structure:** ABOUT ME (read automatically), OUTPUTS (Claude writes here), TEMPLATES (saved skeletons). Nothing else
- **Token management rules:** Restart conversation rather than follow-up messages; fresh session every ~20 messages; batch tasks in one message; use Sonnet not Opus for quick tasks; keep ABOUT ME files under 2,000 tokens
- **Keep context files lean:** One developer found 98.5% of tokens went to re-reading history, only 1.5% to actual output — short files + fresh sessions is the right model
- **Wispr Flow for voice input:** Dictate answers to Claude's questions rather than typing — richer context, faster, more natural

## Why It Matters
The context engineering pattern (files over prompts) aligns with how COG is structured. The token management advice is practical for anyone hitting Claude Pro limits.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Prompting is the worst way to use Claude.md|Full thread →]]

---
*Processed from Readwise by COG*
