---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Tweets/Tweets From Khairallah AL-Awady.md, Readwise/Tweets/Tweets From Suryansh Tiwari.md, Readwise/Full Document Contents/Tweets/Claude Code feels completely different once you install this.md"
date_processed: "2026-05-30"
created: "2026-05-30 10:11"
title: "Claude Code ecosystem setup — what most users miss"
author: "Khairallah AL-Awady, Suryansh Tiwari"
tags: ["#readwise", "#thread", "#claude-code", "#setup", "#productivity", "#anthropic"]
relevance: "high"
related_projects: []
status: "processed"
---

# Thread: Claude Code Ecosystem Setup — What Most Users Miss

## Summary
Boris Cherny (creator of Claude Code at Anthropic) explained in a May 2026 podcast why most users underperform with Claude: the gap isn't intelligence or prompting skill, it's setup. Two separate threads capture his core argument and Anthropic's new `claude-code-setup` plugin that automates much of the configuration.

## Key Points

### The core argument (Boris Cherny via Khairallah AL-Awady)
- The difference between power users and casual users is **setup, not prompting**
- Most users leave blank: Custom Instructions, Memory, Projects, keyboard shortcuts, Artifacts rendering
- "If you've been using Claude for more than a month and never left the chat window, you have at least 30 untouched features. Probably 38."
- Key features most users miss:
  - **Custom Instructions** — persistent system prompt injected into every conversation; eliminates re-explaining your role every session
  - **Memory** — Claude remembers things across conversations if you actively tell it ("remember that I use X") — most users re-explain their stack every session
  - **Projects** — dedicated workspaces with their own system prompt and uploaded files; one for research, one for code, one for writing
  - **Extended Thinking** — makes Claude slow down and reason through edge cases before answering; dramatically better on complex analysis
  - **Multiple parallel conversations** — separate threads for separate workflows; most users collapse everything into one context

### The `claude-code-setup` plugin (Suryansh Tiwari)
- Anthropic quietly released an official plugin: `claude-code-setup`
- Install: `/plugin install claude-code-setup@claude-plugins-official`
- What it does: scans your project and recommends → hooks, skills, MCP servers, subagents, automations — then sets them up step-by-step
- "Most people are using Claude Code completely vanilla — which is why their experience feels messy. The real power comes from the ecosystem around it."

## Why It Matters
Directly relevant to COG setup and optimisation. The "setup not prompting" framing validates the COG architecture (CLAUDE.md, skills, hooks, memory) as the right investment. The `claude-code-setup` plugin is worth testing to see if it surfaces any gaps in the current COG configuration.

## Full Thread
[[Readwise/Full Document Contents/Tweets/Boris Cherny, the creator of Claude Code at Anthropic, just....md|Boris Cherny full thread →]]
[[Readwise/Full Document Contents/Tweets/Claude Code feels completely different once you install this.md|claude-code-setup plugin thread →]]

---
*Processed from Readwise by COG*
