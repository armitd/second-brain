---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Claude + Obsidian have to be illegal.md"
date_processed: "2026-04-28"
created: "2026-04-28 09:21"
title: "Karpathy LLM Wiki — Full Prompt and Architecture"
author: "Defileo (@defileo)"
url: "https://twitter.com/defileo/status/2042241063612502162"
tags: ["#readwise", "#thread", "#karpathy", "#llm-wiki", "#obsidian", "#second-brain", "#prompt"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Karpathy LLM Wiki — Full Prompt and Architecture

## Summary
Thread contains the complete text of Karpathy's LLM Wiki idea file — the actual prompt designed to be copy-pasted into an LLM agent to set up the wiki pattern. Unique value vs other Karpathy summaries: this has the verbatim architecture specification including the three-layer model and the "wiki as persistent compounding artifact" framing.

## Key Points — Full Architecture

**Three layers:**
1. **Raw sources** — immutable source documents. LLM reads, never modifies. Source of truth.
2. **Wiki** — persistent, LLM-maintained structured markdown files. Summaries, cross-references, entity pages, topic articles. The "compiled" knowledge layer.
3. **Outputs** — answers, reports, artefacts generated from wiki queries. Can be filed back into wiki to enrich it.

**Core distinction from RAG:**
RAG re-derives knowledge from raw sources on every query. The wiki compiles knowledge once and keeps it current — cross-references already there, contradictions already flagged, synthesis already reflects everything read.

**Use cases from the prompt:**
- Personal: goals, health, psychology — journals + articles building a structured self-picture
- Research: weeks of papers building a comprehensive wiki with evolving thesis
- Book reading: chapter-by-chapter companion wiki (like fan wikis but built solo by LLM)
- Business/team: internal wiki fed by Slack, meeting transcripts, project docs — LLM does the maintenance no one wants to do
- Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives

**Karpathy's framing:** "You never write the wiki yourself. The LLM is the programmer; the wiki is the codebase; Obsidian is the IDE."

## Why It Matters
This is the actual source prompt for the LLM wiki pattern. Having it filed here means it can be retrieved and used directly. The business/team use case — LLM-maintained wiki from Slack + meeting transcripts — is directly relevant to Belron knowledge management.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Claude + Obsidian have to be illegal.md|Full thread →]]

---
*Processed from Readwise by COG*
