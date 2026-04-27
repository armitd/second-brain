---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/LLM Knowledge Bases.md"
date_processed: "2026-04-27"
created: "2026-04-27 09:55"
title: "LLM Knowledge Bases — Andrej Karpathy"
author: "Andrej Karpathy"
url: "https://twitter.com/karpathy/status/2039805659525644595"
tags: ["#readwise", "#thread", "#llm-wiki", "#knowledge-management", "#obsidian", "#agentic-ai"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: LLM Knowledge Bases — Andrej Karpathy

## Summary
Karpathy's original tweet describing the LLM Wiki pattern: index raw sources into a `raw/` directory, use an LLM to compile a markdown wiki incrementally, run lint health-checks, and query the wiki via an LLM agent. Obsidian as the frontend. LLM writes and maintains all wiki content — human curates sources, not structure.

## Key Points
- **Ingest:** Raw sources → `raw/` → LLM compiles into markdown wiki with summaries, backlinks, concept articles
- **IDE:** Obsidian as frontend — view raw data, compiled wiki, and derived visualisations
- **Q&A:** LLM answers complex questions against the wiki; valuable answers filed back as new wiki pages
- **Lint:** LLM health-checks find inconsistent data, missing links, interesting connections for new article candidates
- **No RAG needed at this scale:** LLM auto-maintains index files and reads relevant context without vector databases
- **Endgame:** Synthetic data + finetuning so the LLM internalises the corpus into weights — "LLM becomes your knowledge base"

## Why It Matters
This is the origin post for the LLM Wiki pattern that underpins COG. Already captured as a braindump via the gist. This tweet version is the primary source.

## Full Thread
[[Readwise/Full Document Contents/Tweets/LLM Knowledge Bases.md|Full thread →]]

---
*Processed from Readwise by COG*
