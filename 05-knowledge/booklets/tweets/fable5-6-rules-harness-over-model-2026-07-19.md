---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Andrej Karpathy quietly published 9 rules for building AI agents.md"
date_processed: "2026-07-19"
created: "2026-07-19 09:32"
title: "Fable 5: 6 rules from Anthropic's docs (harness over model)"
author: "Moysei (@0xMoysei)"
tags: ["#readwise", "#thread", "#agentic-ai", "#claude", "#fable5", "#harness", "#prompt-engineering"]
relevance: "high"
related_projects: ["mcp-governance"]
status: "processed"
---

# Thread: Fable 5 — 6 Rules From Anthropic's Docs (Harness Over Model)

## Summary
Framed as Karpathy's "agents die from a weak harness, not a weak model", the substantive content is a migration guide for Claude Fable 5: setup and skills built for prior models (Opus-era CLAUDE.md, prescriptive skills) now *cap* Fable 5's quality. The through-line is subtraction — delete the scaffolding you added to compensate for weaker models.

## Key Points
- **Harness > model:** most agents fail from a weak harness, not a weak model; everything added to compensate for a weak model becomes dead weight once the model improves.
- **1. Give it the why** — put intent before the request; in a second-brain/agentic OS this tells the model which context files to read first.
- **2. Set explicit negatives** — pair each instruction with what *not* to do (Fable 5 takes unrequested actions, e.g. drafting unasked emails, defensive git branches).
- **3. Match the effort dial** (low/medium/high/xhigh) — high as default, xhigh for hard work, low for routine; low effort on Fable 5 can beat xhigh on prior models.
- **4. Stop over-planning, let it act** — "when you have enough information to act, act"; reserve Plan Mode for drafting the spec with a cheaper model, then hand the finished PRD to the stronger model for the long run.
- **5. Make it prove it** — bake a verification block into skills/CLAUDE.md; nearly eliminates fabricated "done" status in Anthropic's testing.
- **7. Delete before you add** — hardcoded process steps, exhaustive formatting rules, and defensive repetition now degrade output; point the model at your own session history to audit and rewrite your setup.

## Why It Matters
Reinforces [[harness-design-standard-framework]] (harness is the differentiator, not the model) and the "setup > prompting" thesis already folded in from the Boris Cherny note. The migration advice (audit CLAUDE.md and skills, delete over-prescriptive instructions, add verification) is directly actionable for COG's own configuration — and mirrors the model-agnostic-by-design principle in [[agentic-ai-governance-framework]] Principle 11. Practical prompt: run a setup-audit pass over COG's skills/CLAUDE.md for over-prescriptive, model-compensating instructions.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Andrej Karpathy quietly published 9 rules for building AI agents|Full thread →]]

---
*Processed from Readwise by COG*
