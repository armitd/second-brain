---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Google just dropped a free 8-minute lesson on building your....md"
date_processed: "2026-07-07"
created: "2026-07-07 13:15"
title: "Loops Explained: Claude, GPT, Mira and What Actually Works"
author: "Anatoli Kopadze (@AnatoliKopadze)"
url: "https://twitter.com/AnatoliKopadze/status/2070541643518775354"
tags: ["#readwise", "#thread", "#loop-engineering", "#agentic-ai"]
relevance: "medium"
related_projects: []
status: "processed"
---

# Thread: Loops Explained — What Actually Works (and When Not To)

## Summary
A clear primer on agent loops: what they are, the five building blocks, when they're worth it, the cost trap, and a no-code "light version." Notably even-handed about when a loop is a mistake.

## Key Points
- Five building blocks Claude Code/Codex now ship: **automation (heartbeat)**, **skill (reusable instructions)**, **sub-agents (separate maker from checker)**, **connectors (act, not suggest)**, and **the verifier (the gate)** — "everything else is plumbing; the verifier makes it real."
- Build a loop only when all four hold: task repeats ≥weekly; something can auto-reject bad output; the agent can do it end-to-end; "done" is objective, not taste.
- **Verify / State / Stop** are where people go wrong: no gate = the model grades its own homework; no state = repeats mistakes; no stop = runs all night billing you.
- The metric that matters: **cost per accepted change**. Below a ~50% accept rate, the loop costs more than it gives. Cites the "Ralph Wiggum loop" (agent exits early, keeps spending, produces nothing).
- Light version: run a manual loop inside any chat with goal + strict success criteria + self-check protocol. Heavy version (scheduled, event-triggered) needs hosting, gates, and budget guards.

## Why It Matters
Reinforces COG's loop-engineering discipline with a crisp "when NOT to loop" test and the cost-per-accepted-change metric — a useful yardstick for deciding which COG skills genuinely warrant scheduling vs. staying manual. Overlaps with the Raytar and Mac Mini threads; kept for its sharper framing of the verifier and cost economics.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Google just dropped a free 8-minute lesson on building your...|Full thread →]]

---
*Processed from Readwise by COG*
