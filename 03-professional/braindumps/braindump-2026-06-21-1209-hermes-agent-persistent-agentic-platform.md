---
type: "braindump"
domain: "professional"
date: "2026-06-21"
created: "2026-06-21 12:09"
themes: ["agentic-ai", "persistent-agents", "ai-tooling", "mcp-governance", "enterprise-ai"]
tags: ["#braindump", "#agentic-ai", "#hermes", "#persistent-agents", "#ai-literacy"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
source_readwise: "Readwise/Full Document Contents/Tweets/Hermes Agent pro tip.md"
source_author: "Prajwal Tomar (@PrajwalTomar_)"
source_url: "https://twitter.com/PrajwalTomar_/status/2066497450358272493/"
---

# Braindump: Hermes Agent — The Persistent Agent Category Is Now Real

## Raw Thoughts

Sourced from Readwise: Prajwal Tomar's breakdown of Hermes Agent (Nous Research, MIT licensed, launched February 2026, 185K GitHub stars). This is not the usual "here's a cool AI tool" thread — it describes a structurally different category of AI agent. Worth thinking through the implications.

---

## Content Analysis

### Main Themes

1. **The session-based vs. persistent agent split.** All current tools — Claude Code, Cursor, Codex, OpenClaw — are session-based: open a tab, do work, close it, start from zero next time. Hermes is the first agent in the persistent category: lives on a server, remembers everything across sessions, writes its own skill files, runs autonomously overnight, reachable via Telegram from any device. The two categories solve fundamentally different problems.

2. **Self-accumulating skill library.** After every task requiring 5+ tool calls, Hermes writes a markdown skill file: when to use it, the procedure, pitfalls, verification steps, auto-improvement notes. These accumulate as the agent's own procedural memory. A well-run Hermes agent has 100+ skill files specific to your workflows. This is the "compound interest" model for AI tooling — the longer it runs, the less explanation it needs.

3. **Org-chart profile architecture.** Multiple Hermes profiles run in parallel, each with its own identity (SOUL.md), memory, and skill library. The pattern emerging: Chief of Staff, Head of Research, Head of Content, Head of Finance. Each specialises independently. Morning brief triggers all four agents in parallel. This is an agent-as-team model, not agent-as-tool.

### Supporting Ideas

- **SOUL.md** (slot 1 in system prompt) = durable agent identity, not project-specific. Replaces the CLAUDE.md model for persistent-agent use cases. The key rule to bake in: "Never send money to anyone without explicit confirmation."
- **Model tier guidance:** GPT-5.5 for daily work, Claude Opus for `/goal` runs, Qwen 3.7 Max for long autonomous work (35-hour continuous execution, 1,000+ tool calls without context loss).
- **`/goal` for overnight runs.** Set an objective, raise `max_turns` to 20-50, walk away. The agent breaks the goal into subtasks, executes, completes while you sleep.
- **Hermes Desktop launched June 2026.** NVIDIA post-trained Nemotron Ultra specifically for Hermes. Infrastructure is now production-grade, not experimental.
- **Dashboard at localhost:9119.** Kanban board for triage; skill library viewer; per-profile browser automation (off by default).
- **When to use Hermes vs Claude Code:** Claude Code = focused coding in a known repo, best-in-class coding model. Hermes = research, documents, scheduling, business analysis, autonomous overnight runs, anything requiring memory across days/weeks. They run alongside each other, not in competition.

### Questions Raised

- Is Hermes already being used by teams at Belron or in the EA community? Or is this still developer-facing?
- How does the SOUL.md concept relate to CLAUDE.md? Are they converging on the same idea (persistent agent identity file) but for different agent frameworks?
- For the CCOTF programme or AI Damage Assessment PoC: could a Hermes-style persistent agent be the right architecture for a long-running PoC task (multi-day benchmark runs, report generation, competitive tracking)?
- What are the enterprise security implications of a persistent agent with memory accumulating over months? The Noma/NetFoundry governance layer question applies here too.

### Decisions Contemplated

- Whether to try running Hermes alongside Claude Code for the professional / EA workflow (COG parallel agent?)
- Whether the "org chart of agents" model (Chief of Staff, Head of Research) maps onto COG's existing skill architecture, or whether it's a different layer
- Whether this is relevant enough to Belron's MCP Governance programme to add Hermes/Nous Research to the agent governance vendor landscape

---

## Strategic Intelligence

### Key Insights

1. **The AI agent paradigm has formally split — and most enterprise thinking is still only on one side.** Session-based agents (Claude Code, Cursor, Codex) are the established category. Persistent agents (Hermes) are the new category. Enterprise AI governance frameworks — including Belron's MCP Governance work — are primarily designed around the session model: request → tool call → response → audit log. A persistent agent that accumulates skill files, runs overnight, and reaches the user via Telegram is a structurally different governance challenge. The Noma/NetFoundry/Microsoft Agent 365 evaluation should explicitly account for both categories.

2. **"Local models as insurance" is now the practitioner consensus response to Fable 5.** Greg Isenberg (same batch, separate item) drew the parallel explicitly: the Fable 5 ban is the "lost your Facebook traffic overnight" moment for AI. Hermes's model-agnostic architecture (swap models with `hermes model`) and Qwen 3.7 Max for long autonomous runs point toward a world where the model is a commodity and the agent framework + accumulated skill library is the durable asset. This changes the AIDA PoC vendor risk framing: the PoC should be built model-agnostic by design, not just because we're benchmarking three models.

3. **SOUL.md is the identity standard emerging for persistent agents.** CLAUDE.md (for Claude Code) and SOUL.md (for Hermes) are converging on the same architectural idea: a durable identity file that persists across sessions and defines the agent's character, style, constraints, and safety rules. This is going to become a governance artefact — the "agent identity document" — in any enterprise AI governance framework. The MCP Governance programme should be aware that agent identity management is not just about OAuth tokens and API keys; it's about the identity files that define what an agent will and won't do.

### Pattern Recognition

- **Connection to MCP Governance programme:** The Hermes skill file model (self-written, markdown-based, versioned, shareable) is a practical answer to the question "how do agents document what they did?" The combination of Hermes skill files + Noma's runtime monitoring + NetFoundry's identity layer starts to look like a complete agentic governance stack.
- **Connection to CCOTF architecture (AP-01, AI-first):** NICE's Guardian AI governance layer (NICE World, June 9) and Hermes's persistent profile model are both moving toward the same thing: a unified workspace where human and AI agents are managed by the same governance plane. The CCOTF RA's Layer ③ (Human Agent Workspace) and Layer ② (AI-First Contact Layer) are currently separate; the market is converging toward a single workspace for both.
- **Connection to AIDA PoC (model-agnostic architecture):** Hermes's model-swappable design validates the architectural principle. Build the agent framework and skill accumulation layer first; treat the model as a plug-in.

### Strategic Implications

- The MCP Governance programme vendor landscape should add Hermes/Nous Research as a reference for the "persistent agent identity and skill management" capability area — not as a CCaaS or API governance tool, but as an example of how agent memory, identity, and skill documentation work in practice
- The AIDA PoC architecture should explicitly include a model-agnostic abstraction layer — the Fable 5 ban makes this a risk mitigation requirement, not just a benchmark strategy
- COG's own architecture (skill files, CLAUDE.md, session-based execution) is on the session-based side of the split. The Hermes model is worth understanding as a reference for where agentic AI personal tooling is heading

---

## Action Items

### Immediate (24–48 hours)
- [ ] Add "persistent agent identity management (SOUL.md model)" as a governance capability to the MCP Governance programme scope documentation 📅 2026-06-23

### Short-term (1–2 weeks)
- [ ] Add Hermes/Nous Research to the competitive watchlist under "Agentic AI Platforms and Protocols" — note the session vs. persistent agent distinction 📅 2026-06-28
- [ ] Check whether Microsoft Agent 365 or Noma explicitly addresses persistent agents (vs. session-based agents only) — this is a gap if not 📅 2026-06-28

### Strategic Considerations

- The SOUL.md / CLAUDE.md convergence is worth watching as a potential standard. If enterprise AI governance frameworks start requiring "agent identity documents" as a standard artefact, that's a new deliverable category for the MCP Governance programme.
- The "compound interest" model of skill file accumulation has a governance mirror: every accumulated skill file is potentially an auditable record of what the agent learned to do. This is either a compliance asset (audit trail) or a compliance risk (undocumented capability expansion), depending on the governance framework.

---

## Connections

- **Related to:** [[03-professional/COMPETITIVE-WATCHLIST]] (add Hermes under Agentic AI)
- **Related project:** [[04-projects/contact-centre-future/architecture/ccotf-ra-vendor-agnostic]] (Agent governance Layer ②)
- **Related items:** [[05-knowledge/booklets/tweets/greg-isenberg-fable5-local-models-2026-06-21]] (companion thread — local models as insurance)
- **MCP Governance programme vendor evaluation:** [[05-knowledge/booklets/tweets/noma-mcp-governance-2026-06-03]]

---

## Domain Classification

- **Primary Domain:** Professional (100%)
- **Reasoning:** Enterprise architect interest in agentic AI platforms, MCP governance implications, and AI tooling landscape for active projects
- **Cross-Domain Elements:** Personal AI tooling (potential personal use of persistent agent workflow)
- **Privacy Level:** Internal — observations about Belron projects are internal; Hermes itself is open source

---

## Processing Notes

### Emotional Context
- **Energy Level:** Medium — curious and strategic, not immediately excited. The tool itself isn't the point; the category it represents is.
- **Emotional Tone:** Curious. The session/persistent split is a conceptual clarification that makes the current landscape more legible.

### Confidence Assessment
- **Overall Analysis:** 90% — the strategic implications are well-grounded; the specific Hermes product details are sourced
- **Domain Classification:** 100% — clearly professional
- **Strategic Insights:** 85% — the governance implications are solid; the specific "should Belron use Hermes" question is low priority
- **Areas Requiring Clarification:** Whether Microsoft Agent 365 explicitly governs persistent agents, not just session-based agents

---

*Processed by COG Brain Dump Analyst · 2026-06-21 12:09 · Source: Readwise/Full Document Contents/Tweets/Hermes Agent pro tip.md*
