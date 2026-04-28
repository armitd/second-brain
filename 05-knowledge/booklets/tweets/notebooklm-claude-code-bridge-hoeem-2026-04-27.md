---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/YOU JUST CONNECT CLAUDE CODE WITH NOTEBOOKLM AND IT EXTENDS....md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "Claude Code + NotebookLM Bridge — Extend Sessions by Offloading Document Analysis"
author: "hoeem (@hooeem)"
url: "https://twitter.com/hooeem/status/2042295647362019800"
tags: ["#readwise", "#thread", "#claude-code", "#notebooklm", "#context-engineering", "#workflow", "#rag"]
relevance: "medium"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Claude Code + NotebookLM Bridge — Extend Sessions by Offloading Document Analysis

## Summary
Full setup guide for connecting Claude Code with NotebookLM via `notebooklm-py` — an open-source CLI tool reverse-engineered from NotebookLM's internal protocols by Teng Ling. The idea: offload heavy document analysis (30+ documents) to NotebookLM's free RAG tier to save Claude tokens. Claude Code controls NotebookLM through a skill file, gaining persistent memory across sessions.

## Key Points
- **notebooklm-py:** open-source CLI (github.com/teng-lin/notebooklm-py) that lets you control NotebookLM from the terminal — create notebooks, upload sources, run queries, generate podcasts/slides/flashcards
- **NotebookLM tiers:** free = 50 sources/notebook, pro = 300 sources/notebook; processing is free
- **The bridge:** install notebooklm-py, write a Claude Code skill that teaches Claude how to call it, get persistent research memory at zero token cost
- **Skills are cross-tool:** the skill standard works across Claude Code, Cursor, Gemini CLI, Codex — not vendor-locked
- **Token savings:** heavy doc analysis that would drain Claude Pro in an afternoon runs free through NotebookLM

## Why It Matters
COG already uses NotebookLM as an active integration. This is the automation layer that could make COG's research workflows more scalable — particularly for processing large batches of Readwise content or running research against multiple documents.

## Full Thread
[[Readwise/Full Document Contents/Tweets/YOU JUST CONNECT CLAUDE CODE WITH NOTEBOOKLM AND IT EXTENDS....md|Full thread →]]

---
*Processed from Readwise by COG*
