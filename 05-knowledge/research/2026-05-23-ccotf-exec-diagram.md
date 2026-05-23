---
type: "exec-diagram"
domain: "enterprise-architecture"
date: "2026-05-23"
created: "2026-05-23"
title: "Contact Centre of the Future — Executive Architecture Diagram"
owner: "Armo — Enterprise Architecture, Belron"
audience: "Executive stakeholders — no prior EA context required"
status: "v0.1"
related_ra: "2026-05-23-ccotf-reference-architecture.md"
tags:
  - "contact-centre"
  - "ccotf"
  - "exec-comms"
  - "diagram"
---

# Contact Centre of the Future
## Target Architecture — Executive View

*One page. Five layers. This is what we're building.*

---

```mermaid
flowchart TB
    classDef channel fill:#dbeafe,stroke:#2563eb,color:#1e3a5f,font-weight:bold
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764,font-weight:bold
    classDef human fill:#dcfce7,stroke:#16a34a,color:#14532d,font-weight:bold
    classDef belron fill:#fef3c7,stroke:#d97706,color:#78350f,font-weight:bold
    classDef mcp fill:#f1f5f9,stroke:#475569,color:#0f172a,font-weight:bold
    classDef outcome fill:#f0fdf4,stroke:#22c55e,color:#14532d

    subgraph CH["① Customer Channels"]
        direction LR
        V["Voice / Phone"]
        W["Chat / WhatsApp"]
        E["Email / SMS"]
        VID["Video"]
        APP["App / Web Self-Service"]
    end

    subgraph AI["② AI-First Contact Layer  ·  Virtual Agent · Intelligent Routing · Proactive Outreach"]
        direction LR
        VA["LLM-Powered\nVirtual Agent"]
        IR["Intelligent Routing\nIntent → Skill → Queue"]
        PO["Proactive Outreach\nAI-triggered reminders"]
    end

    subgraph HA["③ Human Agent Workspace  ·  When AI cannot resolve"]
        direction LR
        AD["Unified Agent Desktop\n+ Real-Time AI Assist"]
        QA["Supervisor View\n+ AI Quality Assurance"]
    end

    subgraph BL["④ Belron Intelligence Layer  ·  Unique to Belron — not bought from a CCaaS vendor"]
        direction LR
        VRM["Vehicle & Glass ID\nVRM Lookup"]
        INS["Insurer Claims API\nReal-Time Authorisation"]
        ADAS["ADAS Calibration\nSpecialist Routing"]
        AIDA["AI Damage Assessment\nPoC → Production"]
    end

    subgraph MCP["⑤ Enterprise Integration  ·  MCP Gateway — governed, audited, identity-bound"]
        direction LR
        CRM["Customer & CRM\ncustomer-mcp"]
        FSM["Scheduling & Field Service\nscheduling-mcp"]
        KB["Knowledge & Policy\nknowledge-mcp"]
        SYS["Back-Office Systems\nclaims · finance · workforce"]
    end

    CH --> AI
    AI -->|"~60% resolved\nby AI"| DEF["Contact Deflected\nor Self-Served"]
    AI -->|"Escalate\nwith context"| HA
    HA <-->|"Real-time\ndata & guidance"| BL
    BL <-->|"MCP tool calls\naudit-logged"| MCP
    HA --> RES["Contact Resolved\nBack-office updated automatically"]

    class V,W,E,VID,APP channel
    class VA,IR,PO ai
    class AD,QA human
    class VRM,INS,ADAS,AIDA belron
    class CRM,FSM,KB,SYS mcp
```

---

## How to read this

| Layer | What it is | The strategic point |
|---|---|---|
| **① Customer Channels** | Every way a customer can reach Belron | Omnichannel from day one — channel doesn't determine outcome |
| **② AI-First Contact Layer** | LLM virtual agents, intelligent routing, proactive outreach | Target: ~60% of contacts resolved without a human agent |
| **③ Human Agent Workspace** | Unified desktop with real-time AI assistance | Humans handle complexity — AI handles repetition |
| **④ Belron Intelligence Layer** | VRM/glass lookup, insurer APIs, ADAS routing, AI damage assessment | **Our competitive moat.** No CCaaS vendor can sell this to us — we build it. |
| **⑤ Enterprise Integration** | MCP Gateway connecting to CRM, scheduling, knowledge, back-office | Every agent action is identity-bound, logged, and auditable. Governance not an afterthought. |

---

## The three things to take away

1. **AI-first, not AI-only.** The architecture routes to automation first. Humans are elevated to handle what AI cannot — complexity, empathy, exceptions.

2. **Belron's moat is Layer ④.** Vehicle intelligence, insurer real-time authorisation, ADAS routing, and AI damage assessment are capabilities no generic platform provides. This is where Belron differentiates.

3. **Governance is structural, not bolted on.** Every AI-to-system interaction goes through an MCP Gateway that enforces identity, audit, and policy. This is how we satisfy regulators, auditors, and the IPO process.

---

## What isn't shown (deliberately)

This diagram omits:
- CCaaS vendor selection (open decision — architecture is platform-neutral until chosen)
- Internal system names and legacy estates
- Network topology and data residency detail
- EU AI Act compliance mapping

Full architecture detail: [[2026-05-23-ccotf-reference-architecture]]

---

*EA Owner: Armo · Belron Enterprise Architecture · v0.1 · 2026-05-23*
