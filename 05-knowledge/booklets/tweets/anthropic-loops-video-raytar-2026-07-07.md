---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Anthropic shows this video to every new employee.md"
date_processed: "2026-07-07"
created: "2026-07-07 13:15"
title: "Stop Being the Loop: How to Make Claude Work While You Sleep"
author: "Raytar (@Raytar)"
url: "https://twitter.com/Raytar/status/2070219094255599645"
tags: ["#readwise", "#thread", "#loop-engineering", "#claude-code"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: Stop Being the Loop — Loop Engineering in Claude Code

## Summary
A practitioner walkthrough of loop engineering, anchored on Boris Cherny (who built Claude Code at Anthropic) saying in June 2026 "I don't prompt Claude anymore" — loops prompt Claude for him; his job is writing loops. The thread's thesis: most people *are* the loop (checking work, deciding the next step every time), and that is exactly the job a loop takes over.

## Key Points
- Every loop is five beats: **find the work → do it → check itself → remember → go again** (until done, then stop/ping).
- "Prompting is doing the work. Loop engineering is managing the worker."
- A loop differs from a cron job because there's a decision-maker (Claude) inside it that reacts to results — keep going, retry, undo, stop.
- Two Claude Code commands: **/goal** (works until a self-checked condition is true) and **/loop** (re-runs on a cadence). A second Claude copy verifies after each turn.
- The "fake sources" example: a one-shot brief invents citations; a loop with a hard verifier ("every claim ≥3 sources, every link must open") catches and fixes them. The verifier is the point.
- When NOT to loop: one-off tasks, vague goals, and cost — a self-checking loop runs Claude several times per item and burns usage limits faster.

## Why It Matters
This is the loop-engineering doctrine COG's own `loop-engineering` skill formalises (deterministic verifier, state/memory, stop conditions). Strong reinforcement of the verifier-first design already used in the daily-brief and process-readwise skills, and a clean external reference for explaining the pattern to others.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Anthropic shows this video to every new employee|Full thread →]]

---
*Processed from Readwise by COG*
