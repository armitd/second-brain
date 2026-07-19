---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Best breakdown of Karpathy's second brain system I've seen.md"
date_processed: "2026-07-19"
created: "2026-07-19 09:32"
title: "Best breakdown of Karpathy's second brain system"
author: "Corey Ganim / Nick Spisak"
tags: ["#readwise", "#thread", "#second-brain", "#llm-wiki", "#knowledge-infrastructure", "#cog"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: Karpathy's "Second Brain" System — 80/20 Build

## Summary
A step-by-step distillation of Andrej Karpathy's LLM-powered personal knowledge base pattern: dump everything into folders, let the AI compile a wiki, and query your own knowledge that gets smarter each time. This is the exact pattern COG itself is built on.

## Key Points
- **Three folders:** `raw/` (dump everything) → `wiki/` (AI organises it) → `outputs/` (AI answers your questions).
- **One schema file (`CLAUDE.md`)** tells the AI how to organise the knowledge — the whole system hinges on this.
- **Don't organise by hand.** Drop raw files in, tell the AI "compile the wiki", walk away.
- **Compounding loop:** ask questions against your knowledge base, save answers back; every question makes the next one better.
- **Monthly health check:** have the AI flag contradictions, missing sources, and gaps.
- **"Skip Obsidian":** the author argues a folder of `.md` files + a good schema beats 47 plugins. (COG runs the same pattern *inside* Obsidian — the two are not mutually exclusive.)

## Why It Matters
This is the reference articulation of the pattern COG implements: `Readwise/` + `00-inbox/raw/` as the raw layer, `05-knowledge/` as the compiled wiki, `CLAUDE.md` as the schema, and consolidation cycles as the "compile the wiki" + monthly health-check steps. Directly maps onto [[llm-wiki-knowledge-infrastructure-framework]]. The "monthly health check for contradictions and gaps" is essentially the `/knowledge-consolidation` + `/memory-hygiene` loop — worth noting COG already does this, and the "outputs/ saved back" idea is a prompt to be more deliberate about saving answers back into the vault.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Best breakdown of Karpathy's second brain system I've seen|Full thread →]]

---
*Processed from Readwise by COG*
