---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/HE STRAPPED A BATTERY TO A $599 MAC MINI AND....md"
date_processed: "2026-07-22"
created: "2026-07-22 18:39"
title: "Claude on a Mac Mini — the always-on second brain (loop engineering)"
author: "Gipp (@gippp69)"
tags: ["#readwise", "#thread", "#second-brain", "#agentic-ai", "#loop-engineering"]
relevance: "high"
related_projects: ["hive", "openclaw-raspi"]
status: "processed"
---

# Thread: Claude on a Mac Mini — the always-on second brain

## Summary
A base ~$599 Mac Mini (optionally battery-powered for portability) running always-on cron/launchd jobs + ~200 lines of Python becomes an autonomous second brain: three loops turn every lecture, saved article, and note into structured Obsidian markdown that updates itself daily, for a few dollars a month in API calls. The real argument is about *who does the work*: the model stops waiting for you to trigger it and runs the whole job on a box you own, into files you own, on a schedule you set.

## Key Points (loop engineering)
- **A loop, not a chat:** in the chat *you* are the trigger; close the tab and work stops. A loop runs the cycle, checks its own work, fixes what's weak, repeats until done.
- **Three parts people get wrong:**
  - **Verify must be a hard rule, not a vibe** (e.g. "at least 2 wiki links to existing notes") — otherwise Claude grades its own homework and scores itself a 9.
  - **Remember what was already tried** — or the loop repeats the same mistake forever.
  - **Know when to stop** — a stop condition prevents all-night token burn on a bad input; verify fails → skip, log why, move on.
- **Model mixing:** Sonnet only where judgment matters; Haiku (~12× cheaper) for tagging, scoring, sanity checks. "You don't run the deep fryer to boil an egg."
- **Build order that survives production:** reliable manual run in chat → Python script → wrap in a loop (verify gate + stop condition) → *only then* put it on cron. Scheduling something you haven't proved by hand is how loops blow up while you sleep.
- **Economics:** a portable local box can offset recurring cloud costs (storage, automation, transcription, VPS) if the workflow is built right.

## Why It Matters
This is essentially COG's own architecture described from the outside — Mac Mini + Obsidian + Claude, split Sonnet/Haiku by task, loops with verify + stop conditions. It maps directly onto the vault's `loop-engineering` skill and the `openclaw-raspi` project. Strong **Hive** candidate as a concrete "build your own always-on AI second brain" story. Possible **braindump candidate** — the verify-gate / stop-condition / model-mixing framing could seed a loop-engineering note in your own words.

## Full Thread
[[Readwise/Full Document Contents/Tweets/HE STRAPPED A BATTERY TO A $599 MAC MINI AND...|Full thread →]]

---
*Processed from Readwise by COG*
