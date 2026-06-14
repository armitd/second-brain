---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/The third era of AI software development.md"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
title: "The third era of AI software development + Karpathy Sequoia Ascent 2026"
author: "Michael Truell (@mntruell, Cursor CEO) + Andrej Karpathy"
tags: ["#readwise", "#thread", "#agentic-ai", "#cloud-agents", "#vibe-coding", "#agentic-engineering", "#cursor"]
relevance: "high"
related_projects: ["AI Damage Assessment", "MCP Governance"]
status: "processed"
---

# Thread: The Third Era of AI Software Development

**Authors:**
- Michael Truell, CEO Cursor (@mntruell) — "The third era of AI software development"
- Andrej Karpathy — Fireside chat at Sequoia Ascent 2026 (same theme)

## Summary
Two independent framing articles published within days of each other, both reaching the same conclusion: we are entering the third era of AI-assisted software, characterised by cloud agents that work independently over long timescales with minimal human direction. The human role shifts from directing every step to defining the problem and reviewing artifacts.

## The Three Eras (Truell/Cursor)

| Era | Defining capability | Human role |
|-----|--------------------|----|
| 1 | Tab autocomplete — low-entropy repetitive work | Types most code; AI fills in |
| 2 | Synchronous agents — task execution with human in loop | Directs each step; reviews inline |
| 3 | Cloud agents — independent, long-timescale, parallel | Defines the problem; reviews artifacts |

**Data point from Cursor:** Over one-third of all PRs merged internally at Cursor are now created by agents running autonomously on cloud VMs. "A year from now, we think the vast majority of development work will be done by these kinds of agents."

**Characteristics of developers adopting Era 3 at Cursor:**
1. Agents write almost 100% of their code
2. Developers spend time breaking down problems, reviewing artifacts, and giving feedback
3. Multiple agents spin up simultaneously rather than handholding one to completion

## Karpathy at Sequoia Ascent 2026

**Stephanie Zhan framing:** "Vibe coding raised the floor. Agentic engineering raises the ceiling."

**Three themes from Karpathy's talk:**
1. LLMs enable *new categories* of products, not just speed-ups — examples: menugen (fully LLM-app), `.md skills` replacing `.sh scripts`, LLM knowledge bases (computation over unstructured knowledge, previously impossible)
2. **Jaggedness**: LLMs fly on domains that are in the RL training distribution; they off-road in others. Understanding *which* domains are on-rails is the practical skill for using LLMs effectively
3. **Agent-native economy**: decomposition of products into sensors, actuators, and logic — asks how to make information maximally legible to LLMs; "agentic engineering" as the emerging skill set

## Why It Matters for Belron
- **AI Damage Assessment PoC:** The PoC sits in Era 2 (synchronous agent + human review). The Belron AI journey will move toward Era 3. The governance question is whether MCP Governance builds for Era 2 or anticipates Era 3.
- **Agentic engineering as a skill:** Karpathy identifies "agentic engineering" as the distinct new skill set. This is what separates an EA who understands the AI transformation from one who doesn't. The EA value is in being the person at Belron who can design and review agent systems, not just use them.
- **Jaggedness**: Very relevant to selecting AI use cases. The AI Damage Assessment use case is well within the RL distribution (computer vision, structured output, well-defined success criteria) — which is why foundation models perform well on it without fine-tuning.

## Full Threads
[[Readwise/Full Document Contents/Tweets/The third era of AI software development|Full thread →]]
[[Readwise/Full Document Contents/Tweets/Fireside chat at Sequoia Ascent 2026 from a ~week ago|Karpathy Sequoia →]]

---
*Processed from Readwise by COG*
