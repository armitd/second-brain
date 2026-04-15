---
type: "braindump"
domain: "professional"
date: "2026-04-09"
created: "2026-04-09 10:22"
themes: ["LeanIX", "enterprise-architecture-tooling", "EA-repository", "use-cases", "learning"]
tags: ["#braindump", "#professional", "#LeanIX", "#EA-tools", "#architecture-repository"]
status: "consolidated"
consolidated_in: "consolidation-2026-04-15"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Learn LeanIX — Use Cases and Storage

## Raw Thoughts
Need to learn LeanIX. New use cases. How to store?

---

## Content Analysis

### Main Themes
1. **LeanIX as a tool to learn:** There's a knowledge gap around what LeanIX is and how to use it — this is a skill acquisition need
2. **Use cases:** The specific applications of LeanIX relevant to the EA role at Belron — not just "what is it" but "what should I use it for"
3. **Storage / data model question:** "How to store?" suggests uncertainty about how to structure data inside LeanIX — what goes in, how it's organised, and how it connects

### Supporting Ideas
- LeanIX is an EA management platform — it's the tooling layer that sits underneath the frameworks (Wardley, BCM, capability mapping) being built this week
- If Belron uses or is considering LeanIX, this becomes the repository for the capability maps, application landscapes, and technology standards being developed
- The "how to store" question is the right first instinct — LeanIX has a specific data model (Fact Sheets) and the way you structure information determines the value you can extract from it

### Questions Raised
- Does Belron already have a LeanIX instance, or is this exploratory (could we use it)?
- Is this LeanIX for personal learning/use, or for organisational rollout?
- Which EA artefacts currently being developed (BCM map, systems landscape, customer journey system overlay) would live in LeanIX?
- What does "new use cases" refer to — new to Armo, new to Belron, or new capabilities LeanIX has released?

---

## What LeanIX Is (Research Primer)

### The Core Concept
LeanIX is a **SaaS-based Enterprise Architecture Management (EAM) platform** that provides a structured, collaborative repository for architecture data — applications, capabilities, technologies, and their relationships. It is one of the leading tools in the EA tooling market alongside Ardoq, Orbus iServer, and Bizzdesign.

The fundamental unit in LeanIX is the **Fact Sheet** — a record for any architectural entity (an application, a business capability, an IT component, a data object, etc.). Fact Sheets are connected to each other to build a living map of the enterprise.

### The LeanIX Data Model — Fact Sheet Types

| Fact Sheet Type | What it represents | Belron example |
|---|---|---|
| **Application** | A software system or application | Salesforce, Oracle EBS, Booking System |
| **Business Capability** | What the business does (independent of how) | Customer Booking, ADAS Calibration, Claims Processing |
| **IT Component** | Infrastructure, databases, middleware layers | Azure, MuleSoft, Salesforce platform |
| **Interface** | A connection or integration between two applications | Salesforce ↔ EBS integration |
| **Data Object** | A significant data entity | Customer Record, Job Order, Calibration Report |
| **Process** | A business process (optional, often linked to capabilities) | Windscreen Replacement Process |
| **User Group** | A group of users or stakeholders | Technicians, Contact Centre Agents, Insurance Partners |
| **Provider** | A vendor or technology provider | Salesforce, Oracle, Microsoft |
| **Initiative** | A project or programme | CCOTF, Nordics Project |

### How Fact Sheets Connect
The power of LeanIX is not in individual Fact Sheets — it's in the **relationships** between them:
- An **Application** is mapped to the **Business Capabilities** it supports
- An **Interface** connects two **Applications**
- An **IT Component** runs an **Application**
- An **Initiative** changes or creates **Applications** or **Business Capabilities**

This gives you the impact analysis most EA tools promise but few deliver: "If we retire this application, which capabilities are affected? Which interfaces break? Which initiatives are at risk?"

---

## Key Use Cases for an EA at Belron

### Use Case 1: Application Portfolio Management (APM)
**What it is:** A complete inventory of all applications — what they do, what capability they support, who owns them, their lifecycle status (active, retiring, planned), and their technical health.

**Why it matters for Belron:** Most large organisations have a messy, partially-documented application landscape. LeanIX makes this explicit and maintainable. It answers: "What are all our applications? What do they do? Which ones are duplicates, end-of-life, or unsupported?"

**How to start:** Create one Application Fact Sheet per known system (Salesforce, EBS, booking system, etc.) and link each to the Business Capabilities it supports. Even a 70%-complete APM is vastly more useful than none.

**Connects to:** [[braindump-2026-04-08-1436-belron-software-development-model]] — the software delivery model analysis maps directly to APM data

---

### Use Case 2: Business Capability Map (BCM)
**What it is:** The capability map built in LeanIX using Business Capability Fact Sheets — hierarchical, connected to the applications that support each capability.

**Why it matters:** This is where the capability modelling work from April 7 gets a permanent, shareable home. Instead of a static diagram in PowerPoint, it becomes a live record that can be updated and linked to real applications.

**How to start:** Create Business Capability Fact Sheets at two levels (e.g., Level 1: Customer Booking; Level 2: Online Booking, Phone Booking, Insurance Portal Booking). Link each to the applications that support it.

**Connects to:** [[braindump-2026-04-07-1520-business-capability-modelling]], [[belron-business-understanding-framework]]

---

### Use Case 3: Technology Risk and Lifecycle Management
**What it is:** Tracking the lifecycle status of technologies and IT components — which are current standard, which are approaching end-of-life, which are unsupported.

**Why it matters:** Without this, tech debt is invisible until it becomes a crisis. LeanIX surfaces it systematically — "we have 4 applications running on a database version that goes end-of-support in 12 months."

**How to start:** Tag IT Component Fact Sheets with lifecycle status and end-of-support dates. Run the Technology Risk report.

---

### Use Case 4: Integration and Interface Map
**What it is:** A map of all the integrations between applications — what connects to what, via what mechanism, and in which direction data flows.

**Why it matters:** Integration landscapes are almost always undocumented. LeanIX Interface Fact Sheets give you a governed record that makes impact analysis possible. Directly relevant to the Salesforce ↔ EBS integration question.

**Connects to:** [[braindump-2026-04-08-1352-ebs-salesforce]]

---

### Use Case 5: Initiative / Programme Impact Tracking
**What it is:** Mapping programmes (CCOTF, Nordics) to the Applications and Business Capabilities they change — showing what each initiative touches and whether there are conflicts or dependencies.

**Why it matters:** This is where LeanIX becomes genuinely useful to the business (not just EA). It answers: "Is the CCOTF programme touching the same applications as the Nordics initiative? Do they conflict?" This kind of visibility is very hard to get without a tool like LeanIX.

**Connects to:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]]

---

### Use Case 6: Wardley Map Integration (Emerging)
**What it is:** Some EA teams use LeanIX data to inform Wardley Maps — the lifecycle/maturity data in LeanIX (is this application built on commodity or custom technology?) maps to the evolution axis.

**Why it matters:** If LeanIX is the system of record, Wardley Maps become derivable from data rather than hand-drawn. This is a more advanced use case.

**Connects to:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]]

---

## "How to Store?" — Data Structuring Principles

The most common LeanIX failure mode is creating a Fact Sheet graveyard — entries that aren't maintained, aren't connected, and don't answer any real question. The right framing:

### Principle 1: Start with Questions, Not Inventory
Don't create Fact Sheets just to have them. Start by asking: *"What question do I need to answer?"*
- "Which applications support ADAS Calibration capability?" → Create those Application and Business Capability Fact Sheets first
- "What integrations are at risk if we retire this system?" → Create Interface Fact Sheets for that system

### Principle 2: Relationships Are the Value
A Fact Sheet with no relationships is a list entry. The moment you link an Application to a Business Capability, or an Interface to two Applications, LeanIX starts to generate insight. Prioritise connections over completeness.

### Principle 3: Own the Data Quality
LeanIX data degrades fast if no one owns it. For each Fact Sheet type, assign an owner — either the EA function (for technical landscape) or a business owner (for capabilities). Without ownership, entries go stale.

### Principle 4: Use Tags and Lifecycle Status Consistently
LeanIX's reporting and filtering depends on consistent tagging. Decide upfront on the lifecycle states you'll use (e.g. Active, Retiring, Planned, Under Review) and apply them consistently from day one.

### Principle 5: Minimum Viable Architecture First
Don't try to model everything before sharing anything. A LeanIX instance with 10 well-connected Fact Sheets is more valuable than 200 incomplete ones. Ship a working APM first; layer in capabilities and interfaces over time.

---

## Strategic Intelligence

### Key Insights

1. **LeanIX is the tooling layer for everything being built this week.** The capability map, systems landscape, integration map, and initiative tracking from the Belron Business Understanding Framework all have a natural LeanIX home. Learning LeanIX now means the artefacts being built have a durable, maintainable location — not just a PowerPoint file.

2. **The "how to store" question is the right first instinct.** Data model design in LeanIX determines whether the tool becomes genuinely useful or a graveyard. The answer: start with the questions you need to answer, not with comprehensive inventory.

3. **LeanIX is a stakeholder engagement tool, not just an EA repository.** LeanIX's dashboards, reports, and Fact Sheet views are designed to be shared with non-EA stakeholders. A well-maintained LeanIX instance makes EA work visible and credible in a way that a folder of PowerPoints cannot.

4. **If Belron doesn't use LeanIX today, learning it positions you to recommend and implement it.** Many EA functions lack a proper repository. Proposing LeanIX (or a comparable tool) — with a concrete implementation approach — is a significant EA contribution with visible, lasting impact.

### Strategic Implications
- LeanIX learning compounds with everything else being built — every artefact from the Belron Business Understanding Framework has a natural LeanIX entry
- Understanding LeanIX's data model makes BCM, APM, and integration architecture work faster and more consistent
- A LeanIX implementation is a high-visibility initiative — it creates a permanent, shareable artefact of EA work that leadership can see and use

---

## Action Items

### Immediate (24–48 hours)
- [ ] Confirm: does Belron already have a LeanIX instance? If yes, get access 📅 2026-04-10
- [ ] If no: access the LeanIX free trial / community edition to start learning the data model 📅 2026-04-10

### Short-term (1–2 weeks)
- [ ] Complete the LeanIX Academy introductory path (free online — covers Fact Sheets, relationships, reports) 📅 2026-04-18
- [ ] Map the top 5 Belron applications into LeanIX Fact Sheets (Salesforce, EBS or ERP, booking system, calibration tool, contact centre platform) and link to Business Capabilities 📅 2026-04-22
- [ ] Identify the "new use cases" referenced — are these new LeanIX product features or new EA applications? Review LeanIX's 2026 release notes 📅 2026-04-16

### Strategic Considerations
- If Belron doesn't have LeanIX: prepare a short business case — cost, use cases, time to value. The capability map and APM use cases alone justify it for a business of Belron's scale
- If Belron has LeanIX but it's underused: a "LeanIX revival" initiative (cleaning data, adding relationships, training stakeholders) is a high-visibility, tangible EA contribution

---

## Connections
- **Related framework:** [[belron-business-understanding-framework]] — Layers 4 (Systems Landscape) and 5 (Capability Map) both live in LeanIX
- **Related braindump:** [[braindump-2026-04-07-1520-business-capability-modelling]] — the BCM work needs a tool like LeanIX to be maintained long-term
- **Related braindump:** [[braindump-2026-04-08-1436-belron-software-development-model]] — the software delivery model maps to LeanIX Application and Initiative Fact Sheets
- **Related braindump:** [[braindump-2026-04-08-1352-ebs-salesforce]] — integration between EBS and Salesforce is a LeanIX Interface Fact Sheet
- **Related:** [[ea-effectiveness-framework]] — LeanIX is a dual-purpose artefact instrument: EA repository AND stakeholder-facing visibility tool

---

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Reasoning:** EA tooling, directly relevant to the role and to the Belron artefact-building work underway
- **Privacy Level:** Professional (internal)

## Processing Notes

### Emotional Context
- **Energy Level:** Medium — practical tool-learning intent; part of a broader structured morning of EA work
- **Emotional Tone:** Curious — the question is open-ended, investigative, not urgent

### Confidence Assessment
- **Overall Analysis:** 88% — LeanIX is well-documented; Belron-specific relevance (whether they use it, which use cases apply) is the unknown
- **LeanIX data model:** 92% — standard platform documentation
- **Use case applicability:** 82% — depends on whether Belron has the tool and what EA maturity looks like
- **Areas requiring clarification:** Does Belron have LeanIX? What does "new use cases" mean specifically?

---

*Processed by COG Braindump Analyst*
