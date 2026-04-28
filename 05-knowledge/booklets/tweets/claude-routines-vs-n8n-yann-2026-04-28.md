---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/I put the entire Claude Routines Playbook into ONE Notion....md"
date_processed: "2026-04-28"
created: "2026-04-28 09:21"
title: "Claude Routines Replace n8n — Playbook for Natural Language Automation"
author: "Yann (@yanndine)"
url: "https://twitter.com/yanndine/status/2044770663718703525"
tags: ["#readwise", "#thread", "#claude-cowork", "#routines", "#automation", "#n8n", "#webhooks", "#workflow"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Claude Routines Replace n8n — Playbook for Natural Language Automation

## Summary
Yann's complete playbook for Claude Routines — the automation layer in Claude Cowork that replaces n8n-style node workflows. The core idea: describe your SOP in natural language, wire it to a trigger and connectors, and Claude runs the entire workflow autonomously without any drag-and-drop node building.

## Key Points

**What Routines are:**
- Triggered workflows that replace n8n: same event fires, Claude reads a natural language SOP, output lands in Slack/CRM with no node chains built
- Set up in under 5 minutes: name, description (numbered SOP), model selection, environment config, trigger, connectors

**Three trigger types:**
1. **Schedule** — fixed cadence (e.g., daily at 5:10am)
2. **API call** — accepts data payloads from Claude Code or external systems
3. **Webhook** — fires automatically from external events (Fireflies transcript completion, proposal signed, etc.)

**Writing a routine prompt that works unsupervised:**
- Numbered SOP structure
- Explicit finish line ("task is complete when X is in Y")
- Named connectors (reference by name)
- Avoid the three things that make outputs unpredictable (covered in full thread)

**Three production routines worth copying:**
1. **Daily inbox drafter** — runs at 5:10am, drafts email responses for review
2. **Transcript → Proposal** — fires from Fireflies webhook when a call ends, generates a proposal and sends for review
3. **Field monitor → Slack** — signal digest delivered to Slack in under 2 minutes of setup

**Converting n8n to Routines:**
Paste your n8n workflow JSON into Claude Code → ask it to translate the node chain into a natural language prompt → ready to run as a Routine

**Decision rule:**
- High-frequency, purely mechanical workflows → stay in n8n
- Judgment-required, prose-output, or connector-dependent workflows → Routines

## Why It Matters
The webhook trigger pattern (Fireflies → Routine → Proposal) is the same architecture as the automatic memory loop in the Claude + Obsidian AI employee thread. Routines are Cowork's answer to Make/Zapier/n8n — but the SOP is readable English rather than a node graph. High potential for Belron workflows where processes are currently manual.

## Full Thread
[[Readwise/Full Document Contents/Tweets/I put the entire Claude Routines Playbook into ONE Notion....md|Full thread →]]

---
*Processed from Readwise by COG*
