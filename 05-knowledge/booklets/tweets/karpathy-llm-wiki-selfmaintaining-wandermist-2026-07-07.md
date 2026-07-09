---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/How I Built a Second Brain That Maintains Itself.md"
date_processed: "2026-07-07"
created: "2026-07-07 13:15"
title: "How I Built a Second Brain That Maintains Itself (Karpathy LLM Wiki pattern)"
author: "wandermist (@wandermist)"
url: "https://twitter.com/wandermist/status/2070454234189893747"
tags: ["#readwise", "#thread", "#second-brain", "#llm-wiki", "#karpathy"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: How I Built a Second Brain That Maintains Itself

## Summary
A step-by-step implementation of Andrej Karpathy's "LLM Wiki" pattern using Claude Code + Obsidian. Instead of RAG (re-reading raw docs at query time), the LLM incrementally *compiles and maintains* a persistent, interlinked markdown wiki that compounds over time — updating entity pages, revising summaries, flagging contradictions on every new source.

## Key Points
- Karpathy: "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."
- **Three layers:** Raw Sources (immutable, AI reads never writes) / The Wiki (AI-owned markdown pages) / The Schema (a CLAUDE.md telling the AI the structure, conventions, and ingest/query/maintain workflows).
- Karpathy's metaphor: "Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase."
- Workflow: create vault → give Claude Code the gist → ingest a source ("one source, 5–15 wiki pages updated") → query ("what do we know about X across all sources?") with [[wikilink]] citations → periodically "lint the wiki" for contradictions, orphans, stale claims.
- **Use case #4 is Business & Competitive Intelligence:** ingest competitor posts, call transcripts, industry reports; the wiki builds/updates an entity page per competitor and answers "top three objections this quarter" with citations.

## Why It Matters
This is the **exact foundational pattern COG is built on** (raw sources → immutable; AI-maintained knowledge; CLAUDE.md schema). The vault's Readwise-as-raw-sources convention and the `05-knowledge/` booklets are a direct instance. The competitive-intelligence use case maps precisely onto COMPETITIVE-WATCHLIST.md — validation that COG's watchlist workflow is a recognised, deliberate application of the LLM Wiki pattern.

## Full Thread
[[Readwise/Full Document Contents/Tweets/How I Built a Second Brain That Maintains Itself|Full thread →]]

---
*Processed from Readwise by COG*
