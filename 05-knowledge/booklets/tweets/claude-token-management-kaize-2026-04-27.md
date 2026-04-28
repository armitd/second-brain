---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/I stopped hitting Claude's usage limits - 10 things I changed.md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "10 Ways to Stop Hitting Claude's Usage Limits — Token Management Guide"
author: "kaize (@0x_kaize)"
url: "https://twitter.com/0x_kaize/status/2038286026284667239"
tags: ["#readwise", "#thread", "#claude", "#token-management", "#context-engineering", "#workflow"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: 10 Ways to Stop Hitting Claude's Usage Limits — Token Management Guide

## Summary
Practical guide to reducing Claude token consumption. Key insight: Claude re-reads the entire conversation history on every turn, so token cost compounds quadratically — message 30 costs 31x more than message 1. 10 specific habits to stop burning tokens unnecessarily.

## Key Points
- **Token cost compounds quadratically:** at ~500 tokens/exchange — 5 messages costs 7.5K tokens, 20 messages costs 105K, 30 messages costs 232K
- **Edit original prompts, don't follow up:** clicking Edit and regenerating replaces the exchange instead of stacking it. "No, I meant X" as a follow-up burns double the tokens
- **Fresh chat every 15–20 messages:** one developer found 98.5% of tokens went to re-reading history, 1.5% to actual output
- **Batch questions into one message:** three separate prompts = three full context reloads; one message with three tasks = one reload
- **Use Projects for recurring files:** PDFs uploaded to Projects are cached — re-reading doesn't burn tokens each session
- **Save persistent context in Memory settings:** eliminate the "Act as a..." setup messages at the start of every chat
- **Turn off unused features:** web search, connectors, Explore mode all add tokens to every response even when not needed
- **Fresh session + paste summary:** when a chat gets long → ask Claude to summarize → copy → new chat → paste as first message

## Why It Matters
Directly applicable to COG session management. The 15-20 message limit and batching advice are consistent with what Ruben Hassid recommends in the Cowork setup. The quadratic token cost formula explains why COG is designed around fresh sessions with lean context files.

## Full Thread
[[Readwise/Full Document Contents/Tweets/I stopped hitting Claude's usage limits - 10 things I changed.md|Full thread →]]

---
*Processed from Readwise by COG*
