---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/how the creator of claude code actually writes software.md"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
title: "How Boris Cherny (creator of Claude Code) actually writes software"
author: "Rohit (@rohit4verse)"
tags: ["#readwise", "#thread", "#claude-code", "#boris-cherny", "#workflow", "#agentic-ai", "#parallel-agents"]
relevance: "high"
related_projects: ["MCP Governance"]
status: "processed"
---

# Thread: Boris Cherny's Actual Claude Code Workflow

**Author:** Rohit (@rohit4verse) — breakdown of Boris Cherny's personal setup

## Summary
Boris Cherny (creator of Claude Code at Anthropic) revealed his personal workflow. It's not one agent — it's 15 simultaneous Claude streams, treated like a distributed development team. The key insight: context engineering replaces prompt engineering. The CLAUDE.md becomes compounding institutional memory. Planning mode before execution is the "measure twice, cut once" discipline.

## The Parallel Orchestration Setup

**5 terminal Claude Code instances + 10 browser sessions = 15 parallel streams running simultaneously.**

- Terminal tabs numbered 1–5
- System notifications tell him exactly when a specific Claude instance needs input
- Each instance works on different aspects of the same project or completely separate tasks
- Uses `--teleport` command to move context back and forth between terminal and browser sessions
- Checks in on sessions from his iPhone via Claude iOS app

> "This isn't multitasking. This is orchestration. When you are blocked on one task waiting for Claude to think or execute, you are not sitting idle. You are managing four other active streams of work."

**Model choice:** Opus 4.5 with thinking (not Sonnet). Reasoning: "Most developers optimize for model speed. Boris optimizes for total task completion time — including all the back-and-forth corrections you make with faster, less capable models."

## CLAUDE.md as Compounding Institutional Memory

The Anthropic Claude Code team shares a **single CLAUDE.md file checked into git**. The whole team contributes to it multiple times a week.

> "The file contains every mistake Claude has made and every correction the team wants it to remember. When Claude does something incorrectly, they add it to CLAUDE.md so it never happens again."

**How it compounds:** Every mistake → CLAUDE.md → prevents future mistakes → AI gets smarter with every sprint.

During code review, Boris tags `@.claude` on coworkers' pull requests to add items to the CLAUDE.md as part of the PR review process. Automated via the Claude Code GitHub action.

> "This is compounding engineering."

## Context Engineering Over Prompt Engineering

Instead of writing better prompts, you structure better context through files, folders, and documentation.

Directory pattern:
- `/business-info` — strategy docs
- `/writing-styles` — tone guides  
- `/examples` — past work

Instead of a long prompt: "Write a PRD using the style in /writing-styles/technical.md based on the context in /business-info."

The CLI shows real-time token usage and cost — forces awareness of context bloat. `clear` command resets context between unrelated tasks.

## Planning Mode: Measure Twice, Cut Once

**Planning mode: shift + tab twice in Claude Code.**

Boris uses planning mode before every substantive session. Goes back and forth with Claude until he's happy with the plan. Only then switches to auto-accept-edits mode.

> "With a good plan, Claude can usually one-shot the implementation."

> "Planning mode lets you map out what you're doing and how before jumping in. That gives you time to review the approach, tweak things, and catch bad assumptions before the AI wastes tokens going the wrong way."

## Slash Commands for Inner Loop

Slash commands in `.claude/commands/`, checked into git. Boris runs `/commit-push-pr` dozens of times a day. Commands are pre-optimised with inline bash to pre-fetch git info.

> "Slash commands turn repetitive tasks into one command. They are custom APIs for your specific workflow."

## Subagents for Post-Coding Review

- **Code simplifier subagent** — simplifies code after Claude finishes working
- **Verify app subagent** — detailed instructions for testing Claude Code end-to-end
- **Persona-based review agents** — system architect (structure), senior engineer (patterns), integration specialist (interfaces), technical author (synthesis)

## Why It Matters

**MCP Governance:** The CLAUDE.md-as-institutional-memory model is directly applicable to a Belron agent governance framework. Rather than policy documents, governance "rules" could live in CLAUDE.md files scoped to each project or tool — compounding as agents make mistakes and the team corrects them. This shifts governance from a top-down policy layer to an emergent, team-maintained artifact.

**Planning mode as a COG default:** The "plan before execute" discipline maps exactly to COG's "Use Plan Mode before complex skill runs" instruction in CLAUDE.md.

## Related
- [[braindump-2026-06-14-1937-wtf-is-a-loop]] — loop theory (Boris's 3-stage evolution, 200 agents reading GitHub/Slack/Twitter)
- [[claude-setup-reference-batch-2026-06-14]] — covers CLAUDE.md 21 rules and Karpathy's 4 rules

## Full Thread
[[Readwise/Full Document Contents/Tweets/how the creator of claude code actually writes software|Full thread →]]

---
*Processed from Readwise by COG*
