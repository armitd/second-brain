---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/how the creator of claude code actually writes software.md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "How the Creator of Claude Code Actually Writes Software"
author: "Rohit (summarising Boris Cherny)"
url: "https://x.com/rohit4verse/status/2011105761867510229"
tags: ["#readwise", "#thread", "#claude-code", "#agentic-ai", "#software-development", "#workflow"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: How the Creator of Claude Code Actually Writes Software

## Summary
A breakdown of Boris Cherny's (Claude Code creator) personal development workflow. Runs 15 parallel Claude instances simultaneously — 5 in terminal, 10 in browser. Treats AI as a distributed development team, not a single assistant. Uses shared CLAUDE.md files, planning mode, subagents, MCP tool integrations, and PostToolUse hooks.

## Key Points
- **Parallel orchestration:** 5 terminal + 10 browser Claude instances running simultaneously. When blocked on one, manage 4 others. This is orchestration, not multitasking
- **Model choice:** Opus 4.5 with thinking for everything. Optimises for total task completion time, not model speed — fewer corrections needed
- **CLAUDE.md as institutional memory:** Shared across team, checked into git, updated multiple times a week. Every mistake Claude makes gets added so it never recurs — "compounding engineering"
- **Planning mode first:** Shift+Tab twice. Plan until the approach is right, then switch to auto-accept-edits mode. "Measure twice, cut once applied to AI coding"
- **Slash commands in `.claude/commands/`:** Every repeated workflow gets a slash command. `/commit-push-pr` runs dozens of times a day
- **Subagents for review:** Code simplifier subagent, verify app subagent. Persona-based review agents (architect, senior engineer, integration specialist, technical author) run concurrently
- **MCP tool integration:** Claude searches/posts Slack, runs BigQuery, pulls Sentry logs — all via MCP servers checked into `.mcp.json`
- **Verification loop non-negotiable:** Give Claude a way to verify its work — 2-3x improvement in output quality
- **Permission management:** Pre-allow safe bash commands in `/permissions` rather than using `--dangerously-skip-permissions` blindly

## Why It Matters
Practical workflow intelligence for anyone using Claude Code seriously. The CLAUDE.md-as-institutional-memory pattern is immediately applicable. The MCP+Slack+BigQuery integration is directly relevant to the EA Copilot agent concept.

## Full Thread
[[Readwise/Full Document Contents/Tweets/how the creator of claude code actually writes software.md|Full thread →]]

---
*Processed from Readwise by COG*
