---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/If you’ve been procrastinating on learning loops, read this.md"
date_processed: "2026-07-19"
created: "2026-07-19 09:32"
title: "WTF Is a Loop? (Steinberger vs Cherny) — learning loops"
author: "Matt Van Horn (via Aakash Gupta)"
tags: ["#readwise", "#thread", "#agentic-ai", "#loops", "#claude-code", "#harness"]
relevance: "high"
related_projects: ["mcp-governance"]
status: "processed"
---

# Thread: WTF Is a Loop? (Steinberger vs Cherny)

## Summary
A `/last30days` synthesis of the June 2026 "you should be designing loops that prompt your agents, not prompting agents" discourse (Peter Steinberger, Boris Cherny). It gives the cleanest available definition of an agentic loop, its five-stage lineage, and the punchline that the loop — not the model — is now the expensive part.

## Key Points
- **Definition:** a loop is a small program that prompts the agent, reads the output, decides if it is done, and re-prompts if not. You stop being the thing inside the loop; you author the loop and the model becomes a subroutine. Cherny: "My job is to write loops" (259 PRs in 30 days, 100% written by Claude Code).
- **Five-stage lineage:** ReAct (2022) → AutoGPT (2023) → ralph loop (Huntley, 2025, context reset to anchor files) → productised `/goal` with a validator (spring 2026) → multi-agent orchestration loops that supervise other loops on a schedule with durable git-backed state (now). Single-agent ralph is old hat; orchestration on top is the new layer.
- **"Cron with a decision-maker in the body":** scheduling is cron; what cron never had is a model deciding the next action each tick. The engineering is everything you wrap around that decision so it does not run off a cliff.
- **The loop is only as good as its feedback / self-verification** (Cherny's tip five; roborev-style continuous review). An open loop with no feedback is "a machine for generating confident mistakes."
- **The cost shifted from tokens to loop management.** Uber capped engineers at $1,500/tool/month after burning its annual AI budget in four months. Every serious write-up converges on three hard stops: **max iterations, no-progress detection, and a token/$ budget ceiling.**
- **"It's not loops, it's skills":** the loop is plumbing; the durable asset is the library of sharp, named, tested skills it calls.

## Why It Matters
This is the richest single source behind the loop-governance thinking already in the vault. It directly reinforces [[agentic-ai-governance-framework]] Principle 10 (loop budget: max iterations, no-progress, cost ceiling) and [[harness-design-standard-framework]] (loop budget as a harness component), and echoes the existing [[braindump-2026-06-14-1937-wtf-is-a-loop]]. The "skills are the asset, loops are plumbing" line is the same conclusion COG's own loop-engineering reference reaches. **Strong braindump candidate** if you want to fold the extra detail (five-stage lineage, the three hard stops, the cost-shift receipts) into the governance framework as fresh evidence.

## Full Thread
[[Readwise/Full Document Contents/Tweets/If you’ve been procrastinating on learning loops, read this|Full thread →]]

---
*Processed from Readwise by COG*
