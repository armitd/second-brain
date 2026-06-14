---
type: "braindump"
domain: "professional"
date: "2026-06-14"
created: "2026-06-14 19:37"
themes: ["agentic-ai", "loops", "claude-code", "orchestration", "mcp-governance"]
tags: ["#braindump", "#agentic-ai", "#loops", "#claude-code", "#orchestration", "#boris-cherny"]
status: "captured"
energy_level: "high"
emotional_tone: "engaged"
confidence: "high"
source_readwise: "Readwise/Full Document Contents/Tweets/WTF Is a Loop Peter Steinberger vs. Boris Cherny.md"
source_author: "Matt Van Horn (@mvanhorn)"
---

# Braindump: WTF Is a Loop? — The Definitive Analysis

*Source: Matt Van Horn's deep-dive on the Steinberger vs. Boris Cherny debate, June 2026. Processed as a braindump because this is substantive original research, not just a Twitter take.*

---

## Raw Thoughts

The most-repeated sentence in AI coding this week was six words: **"You should be designing loops that prompt your agents."** (Steinberger, June 7, 2026 — 2.2M views). The problem: almost nobody saying it could define what a loop actually is. Matt Van Horn ran his /last30days research tool across the discourse and produced the clearest synthesis I've seen.

---

## Content Analysis

### What a Loop Actually Is

Boris Cherny created Claude Code. His definition is the canonical one:

> "Now it's actually levelled up, I think, again, to the next wave of abstraction where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops."

Plain version: **A loop is a small program you write that prompts the coding agent for you, reads what it produced, decides whether it is done, and if not, prompts it again.** You stop being the thing inside the loop typing prompts. You become the author of the loop. The model becomes a subroutine.

Boris's 3-stage evolution:
1. Wrote code by hand with autocomplete
2. Ran 5–10 Claude sessions in parallel, prompting each one
3. Doesn't prompt at all — writes loops that prompt Claude; ~200 agents read his GitHub, Slack, and Twitter and decide what to build next

Receipt: "In the last 30 days, 100% of my contributions to Claude Code were written by Claude Code. I landed 259 PRs."

### The 5-Stage Lineage

| Stage | What | When | Notes |
|-------|------|------|-------|
| 1 | Academic while-loop | 2022 (ReAct paper) | Model reasons → calls tool → reads result → repeats |
| 2 | AutoGPT | 2023 | Goal + self-prompting → famous for spinning forever doing nothing |
| 3 | Ralph loop (Geoffrey Huntley) | July 2025 | Bash one-liner that pipes the same prompt file into the agent repeatedly; innovation = context resets to fixed anchor files each iteration |
| 4 | /goal command | Spring 2026 | Codex and Claude Code ship /goal — runs ralph loop until a validator confirms done |
| 5 | Orchestration loops | Now (Jun 2026) | What Boris and Steinberger actually mean: loop as unit of work, loops supervising loops, scheduling replaces human kickoff, git-backed durable state |

Stage 3 (ralph) is "old hat" by now. Stage 5 is genuinely new.

### Loops vs Cron — The Honest Answer

The sceptic line: "Cronjobs have funny re-branding rn."

The straight answer: half right. Yes, the scheduling layer is cron. Boris literally runs his on cron. `/loop` in Claude Code uses cron under the hood. But:

> **Cron runs a fixed script. A loop runs a model that looks at the current state, decides what to do next, does it, checks whether it worked, and decides whether to keep going. The decision is the agent's, not yours, and not a hardcoded branch.**

Stack those, let one loop dispatch and supervise others, give them durable shared state — you have something cron cannot express. Cron + decision-maker in the body = loop. The interesting engineering is everything you wrap around that decision so it doesn't run off a cliff.

### The Cost Shift — This Is the Crucial Part

> "The costliest thing in AI coding is no longer writing code, it's managing the agent loop."

**Uber capped its engineers at $1,500/person/month per tool for Claude Code and Cursor after burning its annual AI budget in four months.** Once the model writes the code for almost nothing, the cost moves to the loop running it.

The failure mode: loops that don't stop.

> "Without guardrails, you get infinite loops and billing surprises orders of magnitude over budget."

Every serious 2026 production write-up on loops converges on the same three hard stops:
1. **Maximum iteration count**
2. **No-progress detection**
3. **Token or dollar budget ceiling**

### The Real Asset — Skills, Not Loops

Van Horn's own synthesis, and the most durable take:

> "The loop is plumbing. The asset is the skill it calls."

Steinberger's other recurring point: if you do something more than once, turn it into an automated skill. If you do something hard, turn it into a skill afterward so next time is free.

- A loop with no reusable skills inside it is just a while-true around a stranger
- A loop that calls a library of sharp, tested, named skills is a system that compounds

**"Stop being the thing in the loop. Write the loop once, give it skills worth calling and feedback so it can check itself, cap it so it halts, and let it run on cron while you go decide what to build next."**

### Verification Is the Make-or-Break

> "A loop is only as good as its ability to check its own work."

roborev (Dan Kornas): reviews every commit in the background and feeds findings back into the agent while context is still fresh.

> "An open loop that writes code with no feedback is a machine for generating confident mistakes. A loop that writes, runs, reads the result, and corrects is the thing that actually works. The loop is not the magic. The feedback inside it is."

### Scale Reference

- Steve Yegge's Gas Town: 20–30 Claude Code instances coordinated by a Mayor agent; patrol agents run continuous loops; state stored in git so work survives a crash
- Gartner: agentic AI at peak of inflated expectations; ~17% of organisations actually deploying agents

---

## Questions Raised

- At what point does a Belron MCP governance framework need to account for loops, not just individual agent calls? The unit of governance might need to shift from "agent call" to "agent loop run"
- What does no-progress detection look like in a business process context (vs a coding context)? How does an agentic workflow know it's stuck vs just slow?
- The Uber $1,500/month cap is a real data point — what would a reasonable per-person AI tooling budget look like at Belron, and what guardrails would sit around it?

---

## Actions

- [ ] Share the Boris Cherny 3-stage evolution framing with the MCP Governance working group — it's the clearest articulation of the trajectory from "using AI" to "writing the system that uses AI"
- [ ] Add loop budget governance (max iterations, no-progress detection, cost ceiling) to the MCP Governance framework considerations
- [ ] Note: `/loop` in Claude Code is already available — the skill lives in `.claude/skills/loop/`

---
*Processed from Readwise by COG — source: [[Readwise/Full Document Contents/Tweets/WTF Is a Loop Peter Steinberger vs. Boris Cherny|Full thread →]]*
