---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/Claude Cowork The Ultimate Guide for PMs.md"
date_processed: "2026-04-28"
created: "2026-04-28 09:21"
title: "Claude Cowork — Ultimate Guide for PMs and Non-Developers"
author: "Paweł Huryn (@pawelhuryn)"
url: "https://x.com/pawelhuryn/status/2025939744316682724"
tags: ["#readwise", "#thread", "#claude-cowork", "#claude-code", "#mcp", "#workflow", "#skills", "#sub-agents"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Claude Cowork — Ultimate Guide for PMs and Non-Developers

## Summary
Paweł Huryn's comprehensive guide to Claude Cowork — the autonomous desktop agent in the Claude Desktop app. Key differentiation: Cowork runs in a sandboxed Linux VM, spawns parallel sub-agents, creates real files (.docx, .pptx, .xlsx, .pdf), and connects via MCP. Same underlying model and skill format as Claude Code, but with a visual interface rather than CLI. Author is a former engineer who chooses Cowork for day-to-day work over Claude Code.

## Key Points
- **Cowork vs Code:** Same model, same skill format, same MCP connectors. Code needs git/tmux/CLI. Cowork gives a visual interface. Code can do everything Cowork does — Cowork is the non-developer path.
- **Sandboxed Linux VM:** Cowork runs in a VM on your machine. Can't touch your OS outside the shared folder. Inside that folder: full read/write/delete access.
- **Parallel sub-agents:** Cowork decomposes complex tasks, spawns independent Claude instances for each subtask, runs them simultaneously. Shows plan and progress in real time — steerable mid-task.
- **Real files, not artifacts:** Delivers .docx, .pptx, .xlsx, .pdf directly to the folder you granted access to. Not a chat artifact — a file you can open immediately.
- **Skills:** Reusable instruction files that trigger automatically (e.g., "create a Word doc" loads the docx skill). Triggered via / autocomplete. Same skill format as Claude Code skills.
- **MCPs:** Built-in connectors for Gmail, GitHub, Slack, Google Drive + custom MCP servers. Anthropic manages the setup.
- **Scheduled tasks:** Cowork can run tasks on a schedule — cron-equivalent without the terminal.
- **Cross-session memory hack:** (covered in thread — involves a persistent memory file read at session start)

## Why It Matters
Cowork is the non-terminal equivalent of Claude Code for business users. The parallel sub-agent architecture mirrors what COG's team mode does. For Belron colleagues who aren't comfortable with Claude Code, Cowork is the accessible entry point to the same underlying power.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Claude Cowork The Ultimate Guide for PMs.md|Full thread →]]

---
*Processed from Readwise by COG*
