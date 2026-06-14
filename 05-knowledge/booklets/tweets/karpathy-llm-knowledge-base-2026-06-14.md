---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Building a personal knowledge base for my agents is increasingly....md"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
title: "Karpathy: LLM Knowledge Bases + Personal KB for Agents"
author: "Andrej Karpathy (@karpathy) + elvis/@omarsar0 (DAIR.AI)"
tags: ["#readwise", "#thread", "#second-brain", "#llm-kb", "#obsidian", "#cog", "#personal-os"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: Karpathy's LLM Knowledge Base Architecture

**Authors:** Andrej Karpathy + Elvis (Omar Sanseviero/@omarsar0, DAIR.AI)

## Summary
Karpathy's canonical April 2026 post on LLM knowledge bases: using LLMs not to manipulate code, but to maintain a living wiki over raw knowledge sources. Elvis builds on it with a month-of-implementation account of what the system looks like in production with 100s of research papers. This is the intellectual foundation for COG.

## Karpathy's Architecture

**Four phases:**

### 1. Data Ingest
- Index source documents (articles, papers, repos, images) into a `raw/` directory
- Use LLM to incrementally "compile" a wiki — a collection of `.md` files in a directory structure
- Wiki includes summaries, backlinks, categories, concept articles, and cross-links
- Obsidian Web Clipper extension for web articles; hotkey to download related images locally
- **The LLM maintains the wiki; you rarely touch it directly**

### 2. IDE (Obsidian as frontend)
- Obsidian for viewing raw data, compiled wiki, and derived visualisations
- Plugins for additional rendering (Marp for slides, etc.)

### 3. Q&A
- Once the wiki is large enough (~100 articles, ~400K words), complex queries across the wiki work well
- LLM auto-maintains index files and brief summaries; reads related data fairly easily at this scale
- "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files."

### 4. Output
- Results rendered as markdown files, Marp slideshows, or matplotlib images — all viewable in Obsidian
- Outputs "filed" back into the wiki to enhance it for further queries
- "My own explorations and queries always 'add up' in the knowledge base"

**Health checks / linting:** LLM health checks find inconsistent data, impute missing data via web search, suggest new article candidates, find interesting connections.

## The Key Quote
> "Everyone should be building both their own agent harnesses and their personal knowledge bases. Those are going to be a huge differentiator in where things are headed."

## Elvis's Production Implementation (DAIR.AI)
- Curates research papers daily; tuned a Skill over months to auto-identify high-signal papers
- Papers indexed via markdown files with metadata; semantic search + visual artifacts
- Agent orchestrator with MCP tools generates interactive visualisations over the knowledge base
- "The knowledge that the agents are able to surface from this basic setup is already extremely useful."
- Key insight: "The automations and autoresearch are only as good as what you feed them. The research questions are only as good as the insights the agents have access to."

## Why It Matters for COG
This is the intellectual provenance of COG's design. Specifically:
- The `raw/` → wiki compilation pattern maps directly to Readwise/ → booklets/ → process-readwise skill
- The "LLM maintains the wiki, you rarely touch it directly" philosophy is why process-readwise handles all filings automatically
- The Obsidian frontend role in Karpathy's system is exactly COG's vault role
- Karpathy's "Further explorations" (synthetic data + fine-tuning) hints at the long-term direction: a personal model that has KB contents in its weights, not just context

## Related
- [[cyrilxbt-obsidian-masterclass-2026-06-14]] — applies this architecture for a second brain
- [[dami-defi-claude-obsidian-system-2026-06-14]] — practitioner account of the same pattern
- [[karpathy-loop-shared-memory-caura-2026-06-14]] — Karpathy loop as the agent harness

## Full Thread
[[Readwise/Full Document Contents/Tweets/Building a personal knowledge base for my agents is increasingly...|Full thread →]]

---
*Processed from Readwise by COG*
