---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Anthropic shows this video to every new employee.md"
date_processed: "2026-06-29"
created: "2026-06-29 10:25"
title: "Stop Being the Loop — How to Make Claude Work While You Sleep"
author: "Raytar (@Raytar)"
url: "https://twitter.com/Raytar/status/2070219094255599645/"
tags: ["#readwise", "#thread", "#claude-code", "#loops", "#agentic-ai", "#ai-literacy"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Stop Being the Loop — Claude Loops vs. Prompting

## Summary
Boris Cherny (built Claude Code at Anthropic) declared in June 2026: "I don't prompt Claude anymore." His job is now writing loops — small systems that prompt Claude repeatedly until work is done. The thread explains the five beats of any loop, the distinction between /goal and /loop commands, and why loop engineering fundamentally changes how Claude is used.

## Key Points
- **You are the loop right now.** When you paste a prompt, check the output, paste the error back, and check again — you are performing the work a loop should do. The loop takes over the checking-and-deciding function.
- **Five beats of any loop:** Find the work → Do it → Check itself → Remember → Go again.
- **"Prompting is doing the work. Loop engineering is managing the worker."** — the single line that captures the shift.
- **`/goal`** is the finish-line loop: describe what "done" looks like; a second copy of Claude checks after every turn whether the goal is met; stops itself when it is. Use when there's a pile to clear.
- **`/loop`** is the rhythm loop: runs on a beat (e.g. every 30 minutes). Use when there's no finish line — just an ongoing monitoring task.
- **The state file is the quiet hero.** Without it, every run starts from zero. With it, the loop picks up exactly where it left off, including on a schedule.
- **When not to use a loop:** one-off tasks, vague work, anything that doesn't repeat. Loops cost more (multiple Claude calls per item).

## Why It Matters
This thread is the clearest practitioner-level explanation of the loops model that underpins COG's own automation architecture. The /goal and /loop commands are the Claude Code native implementation of the TRIGGER → DO → VERIFY → ITERATE → STOP pattern. The Boris Cherny framing — "my job is writing loops, not prompting" — is the correct mental model for how to use Claude Code at scale.

## Source
- **Author:** Raytar (@Raytar)
- **Posted:** June 23, 2026
- **Full thread:** [[Readwise/Full Document Contents/Tweets/Anthropic shows this video to every new employee|Full thread →]]

---
*Processed from Readwise by COG · 2026-06-29*
