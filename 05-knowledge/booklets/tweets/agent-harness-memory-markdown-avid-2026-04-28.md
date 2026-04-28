---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/In 14 minutes, this Anthropic engineer who wrote Building Effective....md"
date_processed: "2026-04-28"
created: "2026-04-28 09:21"
title: "Agent Harnesses — Memory is Markdown, Brain is Git, Harness is Thin Conductor"
author: "Avid (@Av1dlive)"
url: "https://twitter.com/Av1dlive/status/2044821377988092278"
tags: ["#readwise", "#thread", "#agents", "#agent-harness", "#memory", "#claude-code", "#architecture"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Agent Harnesses — Memory is Markdown, Brain is Git, Harness is Thin Conductor

## Summary
Thread links to a 14-minute video from an Anthropic engineer (Building Effective Agents author) and contains Avid's synthesis of agent harness architecture principles. Key argument: you don't need to build a model — you need to build the infrastructure around it. Includes Garry Tan's memorable framing and Harrison Chase's case for why harnesses aren't going away.

## Key Points

**What you actually need to build (not the model):**
1. Memory that persists across sessions
2. Skills that encode how tasks should be done
3. Protocols that govern what the agent can and cannot do

**Garry Tan's framing:**
> "If your memory dies when your harness dies, you built the harness too thick. Memory is markdown. Skills are markdown. Brain is a git repo. The harness is a thin conductor — it reads the files, it doesn't own them."

**Harrison Chase (LangChain) on harnesses not going away:**
- Agent harnesses are how you build agents and are not going anywhere
- The scaffolding needed in 2023 has been replaced by *different* scaffolding — models absorbing scaffolding is a myth
- Using a closed/proprietary harness = yielding control of your agent's memory to a third party
- Memory (and therefore harnesses) should be open so you own your memory
- Claude Code's leaked source = 512k lines of code. That IS the harness. Even Anthropic invests heavily in harnesses.

**The harness evolution:**
RAG chains (2022) → complex flows/LangGraph (2023) → agent harnesses (2024+)

## Why It Matters
Directly validates the COG architecture: CLAUDE.md/skills/vault = open memory in files you own; Claude Code = thin harness. Garry Tan's framing ("the harness reads files, doesn't own them") is the exact principle behind why COG stores everything as markdown rather than inside any proprietary AI memory layer.

## Full Thread
[[Readwise/Full Document Contents/Tweets/In 14 minutes, this Anthropic engineer who wrote Building Effective....md|Full thread →]]

---
*Processed from Readwise by COG*
