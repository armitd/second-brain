---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Monica Lam (Stanford Professor).md"
date_processed: "2026-06-29"
created: "2026-06-29 10:25"
title: "The Stanford STORM Method — Multi-Perspective AI Research in 5 Minutes"
author: "Nav Toor (@heynavtoor) via Riley West (@rileywestreel)"
url: "https://twitter.com/rileywestreel/status/2068348900126106085/"
tags: ["#readwise", "#thread", "#ai-literacy", "#research-method", "#claude-code"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: The Stanford STORM Method

## Summary
Stanford's OVAL Lab published STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) at NAACL 2024. It produces research articles 25% better organized and 10% broader than single-prompt research by asking Claude to simulate 5–6 expert perspectives rather than one. Nav Toor's thread distils it into 4 copy-paste prompts requiring no setup — 5 minutes total.

## Key Points
- **The core problem:** "AI writes shallow reports for one reason — you ask it ONE question." STORM asks dozens, like a journalist.
- **The method:** Simulate 5–6 expert roles (practitioner, skeptic, economist, historian, academic) and ask each to analyze the topic from their lens. The practitioner sees what the academic misses; the skeptic challenges what the practitioner assumes.
- **Peer-reviewed result:** Articles built this way are **25% better organized and 10% broader** than single-prompt research (NAACL 2024).
- **Live tool:** storm.genie.stanford.edu — free, no sign-up, type a topic and watch it write.
- **4 prompts in Claude:**
  1. **Multi-Perspective Scan** — 5 expert views in 60 seconds
  2. **Contradiction Map** — where the 5 voices disagree (fights are where real understanding lives)
  3. **Synthesis** — multi-perspective briefing with specific action
  4. **Peer Review** — Claude grades its own work; catches source bias and fact misassociation
- **Time:** 5 minutes for output a PhD student takes 40–60 hours to produce by hand.
- **STORM's known weakness:** does not self-critique (source bias sneaks in). Prompt 4 (peer review) is the fix.

## Why It Matters
Directly applicable to EA research tasks at Belron: position papers, competitive analysis, vendor evaluations. Running STORM on "Genesys Cloud CX vs. Salesforce Agentforce for CCOTF" would produce a more structurally honest briefing than a single "compare these platforms" prompt. Also relevant to the AI Damage Assessment PoC for framing the build/buy/partner decision in a multi-perspective format before presenting to stakeholders.

## Source
- **Author:** Nav Toor (@heynavtoor), shared by Riley West (@rileywestreel)
- **Posted:** June 17, 2026
- **Full thread:** [[Readwise/Full Document Contents/Tweets/Monica Lam (Stanford Professor)|Full thread →]]

---
*Processed from Readwise by COG · 2026-06-29*
