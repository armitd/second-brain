---
type: "position-paper"
title: "Data Foundations for Agentic AI"
status: "draft"
version: "0.1"
created: "2026-05-21"
author: "Armo — Enterprise Architecture"
audience: "CDO / CTO / AI Programme Board"
gaps: ["Informatica license audit", "semantic governance ownership", "current tenant state", "existing data quality standards"]
tags: ["#position-paper", "#data-architecture", "#agentic-ai", "#enterprise-architecture", "#belron"]
---

# Data Foundations for Agentic AI

**Belron Enterprise Architecture — Position Paper**
**Version 0.1 — Draft for development**
**Author: Enterprise Architecture**

---

> ⚠️ **DRAFT — Gaps to fill before sharing:**
> - `[VERIFY: Informatica licence scope]` — confirm which IDMC modules are active at Belron
> - `[VERIFY: data quality standards]` — confirm whether AI-specific DQ standards exist
> - `[VERIFY: semantic governance ownership]` — confirm whether any controlled vocabulary / ontology work exists at Belron
> - `[VERIFY: Microsoft tenant state]` — confirm current opco tenant structure
> - `[STAKEHOLDER]` — confirm primary audience before finalising tone

---

## Executive Summary

Belron is deploying AI agents across its business — in customer contact, in damage assessment, in operational automation. The quality of those agents' outputs depends almost entirely on the quality of the data they are built on, not the sophistication of the models they use.

Enterprise Architecture has identified three distinct layers that must all be in place for AI agents to produce trustworthy, consistent results: **data movement** (does the data arrive efficiently?), **data quality** (is the data trustworthy?), and **data meaning** (does the data mean the same thing to every agent that reads it?).

Most enterprise AI programmes invest heavily in model selection and infrastructure, and underinvest in the governance and meaning layers. This paper argues that closing those gaps — using capabilities Belron may already own — is the highest-leverage action available to the AI programme right now.

---

## The Problem

### AI quality failures are usually data problems, not model problems

When an AI agent returns a wrong, inconsistent, or unreliable answer, the instinctive response is to upgrade the model. In most cases, this is the wrong intervention. The model is performing correctly given the data it received. The problem is in the data.

There are three ways data can fail an AI agent:

1. **It doesn't arrive efficiently** — pipeline latency, unnecessary copying, stale snapshots
2. **It isn't trustworthy** — unvalidated quality, no lineage, no provenance
3. **It doesn't mean the same thing everywhere** — different agents, teams, or opcos interpret the same term differently

The third failure is the most dangerous. An AI agent that returns a wrong answer is easily caught. Ten AI agents that each return different-but-internally-consistent answers — because they each interpret "customer", "job", or "resolution" differently — will appear to be working correctly until decisions are compared. By then, the data has been acted on.

### The risk grows as agent deployment scales

Belron is moving from single-agent experiments to multi-agent deployments across opcos and business functions. A semantic inconsistency that is invisible in a single agent becomes a structural risk across a fleet. `[EXAMPLE NEEDED: a Belron-specific example of where inconsistent definitions have caused reporting or operational problems would strengthen this section]`

---

## The Framework: Three Layers

```
Layer 3 — Meaning:    Semantic governance  — what does this data mean?
Layer 2 — Quality:    Data governance      — is this data trustworthy?
Layer 1 — Movement:   Efficient transport  — does this data arrive?
```

Each layer is a prerequisite for the next. Layer 1 without Layer 2 delivers fast, untrustworthy data. Layers 1 and 2 without Layer 3 deliver fast, clean data that different agents interpret differently.

### Layer 1 — Efficient Data Movement

Modern data architecture has largely solved Layer 1. Zero-copy principles in streaming systems (Apache Arrow, Kafka), cloud data sharing (Snowflake's zero-copy cloning), and logical-first architecture (don't move data unless you must) are established patterns.

**Belron's current position:** `[VERIFY: what data movement infrastructure exists — Informatica CDI? Azure Data Factory? Kafka? What is the current pipeline architecture?]`

**The principle to apply:** Prefer sharing data over copying it. Before building a new data pipeline for an AI use case, ask whether the data can be accessed in place.

### Layer 2 — Data Quality and Governance

Data quality for AI is a distinct discipline from operational data quality. A field that is "good enough" for reporting may be entirely unsuitable for AI training or grounding — missing values, inconsistent formats, and label noise that human analysts overlook will be learned by a model as signal.

`[STAT: Only 38% of organisations have established data quality standards specifically for AI — Informatica 2026 State of Data and AI report. Worth including if citing externally.]`

**Belron's current position:** Belron has Informatica IDMC, currently used primarily for Master Data Management. The IDMC platform includes Data Quality, Data Catalog, AI Governance Catalog, and Data Lineage modules that `[VERIFY: are these licensed? are they active?]` may be available but underused. If so, the capability to close this layer exists — it is an activation question, not a procurement question.

**The principle to apply:** Before training or grounding any AI model on Belron data, run it through a data quality assessment. Establish minimum quality thresholds as a gate for AI use.

### Layer 3 — Semantic Governance

This is the layer most enterprise AI programmes skip entirely — and the layer most responsible for multi-agent inconsistency.

The semantic layer is not a tool that can be purchased. The tooling (ontology management platforms, data catalogs, dbt semantic layer) can be procured. The *meaning* — what "customer" means at Belron, what "job" means, what "resolution" means, what counts as an "active account" — must be defined and governed by the business itself.

Without it, each AI agent that Belron deploys will independently construct its own interpretation of these terms from whatever training data or context it receives. At small scale this is manageable. At the scale Belron operates — `[VERIFY: number of opcos, number of AI deployments planned]` — it is a structural governance risk.

**Belron's current position:** `[VERIFY: does any enterprise ontology or controlled vocabulary work exist at Belron? Is there a data glossary? Is there a Master Data Management programme that has defined canonical business objects? Who owns this — Group Data, a specific opco, EA?]`

**The principle to apply:** Define a controlled vocabulary for the 20-30 business objects that appear most frequently across AI use cases. Start with the terms that appear in multiple projects simultaneously: customer, job, technician, SLA, resolution, escalation, damage, calibration. Assign an owner to each definition. That is the minimum viable semantic layer.

---

## Where Belron Stands Today

| Layer | Capability | Status | Gap |
|---|---|---|---|
| **Layer 1 — Movement** | Informatica CDI, `[VERIFY: other pipelines]` | `[VERIFY]` | `[VERIFY: identify unnecessary data copying in AI pipelines]` |
| **Layer 2 — Quality** | Informatica IDMC (DQ, Catalog, Lineage modules) | `[VERIFY: licensed? active?]` | Likely underactivated — audit required |
| **Layer 3 — Meaning** | `[VERIFY: any existing ontology or vocabulary work?]` | Likely absent | Semantic governance programme not yet initiated |

**The gap that matters most:** Layer 3 is almost certainly missing. It is also the layer with no existing platform capability to activate — it requires a programme decision and an owner.

---

## Recommendations

### Immediate

1. **Audit the Informatica IDMC licence** — establish exactly which modules are licensed and which are active. Specifically: Data Quality, Data Catalog, Data Lineage, and AI Governance Catalog. This is a commercial and technical audit, not a project. Timebox to two weeks.

2. **Define the AI data quality gate** — before any AI model is trained or grounded on Belron data, it passes a data quality assessment. Use Informatica DQ if available; define minimum thresholds as a standard. This is a one-time standards definition exercise.

### Short-term (1-3 months)

3. **Initiate a semantic governance scoping exercise** — identify who at Belron has authority to define canonical business object definitions. Map the 20-30 most frequently used terms across active AI projects. Assign provisional owners. This does not require a platform purchase — it requires a working group and a decision.

4. **Apply the three-layer diagnostic to each active AI project** — for AI Damage Assessment PoC, MCP Governance, and Contact Centre of the Future, identify which layers are present and which are gaps. Use this as a programme risk register.

### Strategic

5. **Establish semantic governance as a first-class programme** — parallel to, and upstream of, agent deployment. The right owner is `[VERIFY: CDO? Group Data Governance? EA?]`, not the technology team. This is a business definitions problem.

---

## Connection to Active Belron AI Initiatives

| Initiative | Layer 1 | Layer 2 | Layer 3 |
|---|---|---|---|
| **AI Damage Assessment PoC** | `[VERIFY]` | Training data quality validation needed | Damage assessment vocabulary (damage types, severity classifications) |
| **MCP Governance** | Covered by MCP transport layer | Data provenance for tool outputs | What does the data returned by MCP tools mean? |
| **Contact Centre of the Future** | `[VERIFY: contact centre data pipelines]` | `[VERIFY]` | Resolution, escalation, SLA, satisfaction — definitions needed before agents are deployed |

---

## Why This Is an EA Responsibility

Enterprise Architecture is the function with visibility across all three layers and across all active AI projects simultaneously. No single project team sees the cross-cutting risk.

The argument for EA ownership is not procedural — it is not about governance gates or review processes. It is about providing the architectural clarity that makes AI agent deployment safe and directional. An EA function that can say "Layer 3 is missing across three of your four AI initiatives, and here is the minimum viable programme to close it" is providing directional value, not process overhead.

---

## Appendix: Key Terms

**Semantic layer:** The combination of controlled vocabulary, ontology, and evaluation rules that ensures different systems interpret data consistently. Not a specific product — a governed capability.

**Controlled vocabulary:** A curated list of canonical definitions for business terms. The minimum viable semantic layer.

**Ontology:** A structured representation of business concepts and their relationships — more sophisticated than a vocabulary, but built on the same foundation.

**Zero-copy architecture:** Data transport patterns that minimise unnecessary data copying between systems. Reduces latency and pipeline complexity for AI applications.

**Data lineage:** The traceable history of a data item from source to consumption. Required for EU AI Act compliance and for understanding why an AI model produced a specific output.

---

*Belron Enterprise Architecture — Draft v0.1, May 2026*
*Developed from knowledge base synthesis — see [[05-knowledge/patterns/pattern-three-layer-data-architecture-agentic-ai|Three-Layer Data Architecture Pattern]]*
