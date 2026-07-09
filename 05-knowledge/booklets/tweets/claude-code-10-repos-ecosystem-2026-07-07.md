---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/THIS GUY OPENED A 41,000-STAR GITHUB REPO AND SHOWED WHY....md"
date_processed: "2026-07-07"
created: "2026-07-07 13:15"
title: "10 Open-Source Repos That Make Claude Code 10x Better"
author: "Gipp (@gippp69) / Yarchi (@undefinedKi)"
url: "https://twitter.com/gippp69/status/2071158827584561636"
tags: ["#readwise", "#thread", "#claude-code", "#agentic-ai", "#ai-security"]
relevance: "high"
related_projects: ["MCP Governance"]
competitive_intel: true
status: "processed"
---

# Thread: 10 Open-Source Repos That Make Claude Code 10x Better

## Summary
A curated tour of the Claude Code extension ecosystem, arguing raw Claude Code is only ~20% of the product — the other 80% (memory, security, QA, agent teams, persistence) lives in open-source add-ons. Reviews 10 repos with install patterns and honest caveats.

## Key Points
- **ECC (Everything Claude Code)** — discipline layer: tests before "done", stops faking passing checks, project memory across sessions. Started the "configs as a product" wave.
- **GStack (Garry Tan/YC)** — turns one agent into a virtual startup team (CEO, eng manager, designer, reviewer, QA, release); 23 commands (/office-hours, /plan-eng-review, /review, /qa, /ship).
- **Matt Pocock skills** — "skills for real engineers, not vibe coding": /grill-me, /tdd, /improve-codebase-architecture to stop the model building the wrong thing.
- **Graphify** — turns a codebase into a queryable knowledge graph; ~1,700 tokens/query vs 123,000 (claimed ~71x cut). Went viral off Karpathy's knowledge-base workflow.
- **GBrain (Garry Tan)** — a whole-working-life memory layer (146k pages, 24k people, 5k companies) that synthesises answers, not links.
- **SkillSpector (NVIDIA)** — security scanner for agent skills; cites a study of 42,447 skills where **26% contained a vulnerability and 5% showed likely malicious intent**. Gives a 0–100 safety score.
- Also: Anthropic Cybersecurity Skills (817 playbooks mapped to MITRE ATT&CK/NIST), OpenMontage (video), DeerFlow (ByteDance parallel sub-agents), OpenClaw (250k+ stars, agent in your messaging apps).
- Advice: install one at a time, and scan everything with SkillSpector first — "popularity isn't safety."

## Why It Matters
Two angles. (1) **MCP Governance**: the SkillSpector stat (26% of agent skills vulnerable, 5% likely malicious) is a hard, citable data point for the "why govern agent/skill supply chains" argument, and NVIDIA shipping a skill-scanner validates the threat as real at scale. (2) A map of the Claude Code power-user ecosystem — several of these (project memory, knowledge-graph, maker/checker agent teams) mirror or could strengthen COG's own architecture.

## Full Thread
[[Readwise/Full Document Contents/Tweets/THIS GUY OPENED A 41,000-STAR GITHUB REPO AND SHOWED WHY...|Full thread →]]

---
*Processed from Readwise by COG*
