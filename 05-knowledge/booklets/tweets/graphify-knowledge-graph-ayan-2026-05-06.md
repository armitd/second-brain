---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/🚨 BREAKING Someone just built the exact tool Andrej Karpathy....md"
date_processed: "2026-05-06"
created: "2026-05-06 14:05"
title: "Graphify — Knowledge Graph Tool Built 48hrs After Karpathy's Request"
author: "Muhammad Ayan (@socialwithaayan)"
tags: ["#readwise", "#thread", "#llm-wiki", "#knowledge-management", "#tools", "#claude-code"]
relevance: "medium"
related_projects: []
status: "processed"
---

# Thread: Graphify — Karpathy's Requested Tool, Built in 48 Hours

## Summary

48 hours after Andrej Karpathy's LLM Knowledge Bases post, someone shipped **Graphify** — an open-source tool that runs inside Claude Code, points at any folder, and produces a full knowledge graph with backlinked Obsidian vault, wiki index, and plain English Q&A. Claims 71.5x fewer tokens per query compared to reading raw files.

## Key Points

- **One command to run:** `/graphify` inside Claude Code, point at any folder
- **Output:** navigable knowledge graph + Obsidian vault with backlinks + wiki starting at `index.md` + Q&A interface
- **Multi-format support:** code in 13 languages, PDFs, images (Claude Vision), markdown
- **Token efficiency:** 71.5x fewer tokens per query vs. reading raw files
- **No setup overhead:** no vector database, no config files, no embeddings
- **Open source, free:** `pip install graphify && graphify install` — repo at github.com/safishamsi/graphify

## Why It Matters

This is the "product" that Karpathy described as missing (he called his own approach "a hacky collection of scripts"). Graphify automates the knowledge graph compilation step, which is the most time-consuming part of the LLM wiki workflow. The 71.5x token efficiency claim (if valid) is significant — it means querying a large knowledge base costs almost nothing.

Relevance to COG: this is the type of tool that could make the COG vault's knowledge base structure more queryable without loading full documents into context.

## Full Thread
[[Readwise/Full Document Contents/Tweets/🚨 BREAKING Someone just built the exact tool Andrej Karpathy....|Full thread →]]

---
*Processed from Readwise by COG*
