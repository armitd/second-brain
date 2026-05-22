---
type: "reference-architecture-summary"
artefact_class: "Simplified Architecture Model (one-view companion)"
domain: "enterprise-architecture"
date: "2026-05-22"
created: "2026-05-22"
title: "MCP Architecture — Simplified Model"
owner: "Armo — Enterprise Architecture, Belron"
status: "v0.1"
related_projects: ["mcp-governance", "ai-damage-assessment-poc", "contact-centre-future"]
related_research: ["2026-05-22-mcp-agentic-reference-architecture.md", "2026-05-06-mcp-strategy-belron.md"]
tags:
  - "reference-architecture"
  - "mcp"
  - "agentic-ai"
  - "diagram"
  - "exec-brief"
confidence: "high"
---

# MCP Architecture — Simplified Model

*A one-view companion to [[2026-05-22-mcp-agentic-reference-architecture]]. Use for exec briefings, ACR kickoffs, and onboarding new project teams to the MCP governance model.*

> The full reference architecture defines the conformance surface (20 ABBs, 10 patterns, four phases). This document defines the **mental model** — what every Belron architect, BA, and engineer should be able to draw on a whiteboard.

---

## The Diagram

```
                   ┌──────────────────────┐
                   │   CHANNELS / USERS   │   Voice · Chat · Web · Mobile · Email
                   └──────────┬───────────┘
                              │
                   ┌──────────▼───────────┐
                   │       AGENTS         │   LangGraph · Copilot Studio
                   │  Reasoning · Memory  │   Bedrock · Vertex · Custom
                   └──────────┬───────────┘
                              │  MCP  +  A2A
              ┌───────────────▼───────────────┐
              │        MCP GATEWAY            │   ◄── The single control point
              │  Identity · Policy · Audit    │
              │  DLP · HITL · Tool Registry   │
              └───────────────┬───────────────┘
                              │  MCP
              ┌───────────────▼───────────────┐
              │       MCP SERVERS             │   customer · vehicle · scheduling
              │ (one per business capability) │   claims · workforce · finance
              │                               │   itsm · knowledge
              └───────────────┬───────────────┘
                              │  APIs
              ┌───────────────▼───────────────┐
              │  INTEGRATION + SOURCE         │   MuleSoft · SnapLogic
              │  SYSTEMS                      │   Salesforce · ServiceNow
              │                               │   Workday · Oracle · M365
              └───────────────────────────────┘

  ━━━━━━━━  CROSS-CUTTING PLANES (touch every layer)  ━━━━━━━━
   Identity       Entra ID · OAuth 2.1 + PKCE
   Semantic       Ontology · Business Glossary · Knowledge Graph
   Observability  OpenTelemetry → Dynatrace + Elastic
   Audit          Immutable WORM · 7-year retention
```

---

## Five Components, One Line Each

| # | Component | What it is |
|---|---|---|
| 1 | **Agents** | AI actors that reason, plan, and call tools. Vendor-mixed by design. |
| 2 | **Gateway** | The only path between agents and tools. Where identity, policy, audit, DLP, and HITL live. |
| 3 | **MCP Servers** | Tool bundles organised by business capability, not by source system. |
| 4 | **Integration + Source Systems** | Existing APIs and systems of record, wrapped — not replaced. |
| 5 | **Cross-cutting planes** | Identity, semantic meaning, observability, audit — applied uniformly to every layer. |

---

## Two Protocols

| Protocol | What it connects | Why it exists |
|---|---|---|
| **MCP** (Model Context Protocol) | Agent → Tool | Standardises how agents discover and call tools |
| **A2A** (Agent2Agent) | Agent → Agent | Standardises how agents delegate work to other agents |

They are **orthogonal** — every multi-agent workflow uses both (see RP-04 in the full RA).

---

## The One Insight

> **The Gateway is the architecture.**
>
> Everything *above* it is interchangeable (any agent framework, any model provider).
> Everything *below* it is interchangeable (any MCP server, any source system).
>
> The Gateway is what makes the whole estate provider-portable, governable, and IPO-defensible.

This is why **AP-03** ("all agent-to-tool traffic transits a Belron-controlled gateway") is the load-bearing principle of the entire reference architecture. Lose the Gateway and you lose vendor neutrality, audit, identity propagation, and EU AI Act conformance in one move.

---

## How to Use This Model

- **Exec briefings** — one slide; the diagram is the slide
- **ACR kickoffs** — orient a project team before walking them through the full RA
- **Vendor conversations** — show where the vendor sits and what they don't get to own
- **BA capability mapping** — point to the MCP Server layer; that's where business capabilities map to machine-callable surface

For conformance detail (ABBs, SBBs, patterns, principles), go to the full RA: [[2026-05-22-mcp-agentic-reference-architecture]].
For adoption sequencing (what to deploy, in what order), go to the strategy doc: [[2026-05-06-mcp-strategy-belron]].

---

*v0.1 — 2026-05-22. Companion to the full reference architecture; not a substitute.*
