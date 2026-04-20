---
type: "consolidated-knowledge"
domain: "professional"
framework: "leanix-ea-repository"
created: "2026-04-15"
last_updated: "2026-04-20"
consolidation_id: "consolidation-2026-04-20"
source_documents: 2
status: "working"
tags: ["#framework", "#consolidated", "#LeanIX", "#EA-tools", "#architecture-repository", "#APM"]
---

# LeanIX EA Repository Framework

## Framework Overview
A working model for using LeanIX as the living repository for EA work at Belron — covering the data model, prioritised use cases, data structuring principles, and strategic positioning of LeanIX as both a repository tool and a stakeholder engagement instrument.

**Status:** Working (research complete; application depends on whether Belron has an active LeanIX instance)
**Last Updated:** 2026-04-15
**Source Insights:** 1 document — LeanIX learning use cases braindump (Apr 9)

---

## Why This Matters

EA work is only as durable as its home. Capability maps, application portfolios, integration inventories, and initiative tracking produced in PowerPoint decay — they're out of date within weeks and can't be linked, filtered, or queried. LeanIX (or a comparable EAM platform) is the tooling layer that makes EA work maintainable, shareable, and credible at scale.

The business case is simple: every artefact being built — BCM, systems landscape, integration map, initiative tracking — has a natural LeanIX entry. Learning LeanIX now means building once and maintaining one place, not managing a folder of diverging documents.

---

## The LeanIX Data Model — Fact Sheet Types

The fundamental unit in LeanIX is the **Fact Sheet** — a record for any architectural entity. Nine types, each with a specific purpose:

| Fact Sheet Type | What it represents | Belron example |
|---|---|---|
| **Application** | A software system | Salesforce, Oracle EBS, Booking System |
| **Business Capability** | What the business does (independent of how) | Customer Booking, ADAS Calibration, Claims Processing |
| **IT Component** | Infrastructure, databases, middleware | Azure, MuleSoft, Salesforce platform |
| **Interface** | A connection between two applications | Salesforce ↔ EBS integration |
| **Data Object** | A significant data entity | Customer Record, Job Order, Calibration Report |
| **Process** | A business process (optional, linked to capabilities) | Windscreen Replacement Process |
| **User Group** | A group of users or stakeholders | Technicians, Contact Centre Agents, Insurance Partners |
| **Provider** | A vendor or technology provider | Salesforce, Oracle, Microsoft |
| **Initiative** | A project or programme | CCOTF, Nordics Project |

### How Fact Sheets Generate Value

A Fact Sheet with no relationships is a list entry. The value is in connections:
- **Application** → **Business Capability** it supports
- **Interface** → two **Applications** it connects
- **IT Component** → **Application** it runs
- **Initiative** → **Applications** and **Business Capabilities** it changes

These relationships enable impact analysis: "If we retire this application, which capabilities are affected? Which interfaces break? Which initiatives are at risk?" This is what most EA tools promise and few deliver at this precision.

---

## Core Principles

### Principle 1: Start with Questions, Not Inventory

**Statement:** Don't create Fact Sheets just to have them. Start by asking: "What question do I need to answer?" The question determines which Fact Sheet types to create first.

**How to apply:**
- "Which applications support ADAS Calibration?" → Create Application + Business Capability Fact Sheets first
- "What integrations break if we retire this system?" → Create Interface Fact Sheets for that system
- "Which initiatives touch the same applications?" → Create Initiative Fact Sheets and link to Application

**The failure mode:** Creating comprehensive Fact Sheets before establishing relationships produces a maintained list, not an insight engine.

**Confidence:** High

---

### Principle 2: Relationships Are the Value

**Statement:** The moment you link an Application to a Business Capability, or an Interface to two Applications, LeanIX starts to generate insight. Prioritise connections over completeness.

**Evidence:** The impact analysis capability that makes LeanIX genuinely useful to business stakeholders — "which programmes conflict?" — only emerges from relationships, not from individual record completeness.

**How to apply:** For every new Fact Sheet, ask: what should this connect to? Don't close the record until at least one relationship exists.

**Confidence:** High

---

### Principle 3: Own the Data Quality

**Statement:** LeanIX data degrades fast if no one owns it. For each Fact Sheet type, assign an owner — the EA function for technical landscape, business owners for capabilities. Without ownership, entries go stale and trust collapses.

**How to apply:** Document the owner of each Fact Sheet type on creation. For Belron: EA owns Application, IT Component, Interface, and Initiative. Business capability owners (typically Operations, CX leads) should own Business Capability Fact Sheets — or at least validate them.

**Confidence:** High

---

### Principle 4: Use Tags and Lifecycle Status Consistently

**Statement:** LeanIX's reporting and filtering depends on consistent lifecycle state tagging. Decide upfront on the states you'll use (e.g. Active, Retiring, Planned, Under Review) and apply them from day one. Inconsistent tagging makes the Technology Risk report useless.

**How to apply:** Before creating the first Application Fact Sheet, define the lifecycle taxonomy and write it down. Treat it as a standard. Review it once a quarter.

**Confidence:** High

---

### Principle 5: Minimum Viable Architecture First

**Statement:** A LeanIX instance with 10 well-connected Fact Sheets is more valuable than 200 incomplete ones. Ship a working APM first; layer in capabilities and interfaces over time.

**How to apply:** For Belron, the minimum viable start is: (1) top 5–10 applications, linked to (2) the Level 1 Business Capability Fact Sheets. This gives immediate APM value and a foundation for everything else.

**Confidence:** High

---

## Key Use Cases for an EA at Belron

### Use Case 1: Application Portfolio Management (APM)
**What it answers:** "What are all our applications? What do they do? Which are duplicates, end-of-life, or unsupported?"

**How to start:** Create one Application Fact Sheet per known system (Salesforce, EBS/ERP, booking system, calibration tool, contact centre platform). Link each to Business Capabilities it supports. Even a 70%-complete APM is vastly more useful than none.

**Why it matters:** Most large organisations have an undocumented application landscape. LeanIX makes it explicit and maintainable — a prerequisite for the technology risk and initiative tracking use cases.

---

### Use Case 2: Business Capability Map (BCM)
**What it answers:** "What does Belron do? Which applications support which capabilities? Where are there gaps or overlaps?"

**How to start:** Create Business Capability Fact Sheets at two levels (e.g. Level 1: Customer Booking; Level 2: Online Booking, Phone Booking, Insurance Portal Booking). Link to applications. This is where the static BCM PowerPoint becomes a live, queryable record.

**Connection:** The capability map work from April 7 has its permanent home here. Once in LeanIX, it can be updated and shared without version-control fragmentation.

---

### Use Case 3: Technology Risk and Lifecycle Management
**What it answers:** "Which technologies are approaching end-of-life? Which applications are running on unsupported infrastructure?"

**How to start:** Tag IT Component Fact Sheets with lifecycle status and end-of-support dates. Run the Technology Risk report. This surfaces tech debt that is invisible until it becomes a crisis.

**Why it matters for Belron:** Without this, technology risk enters conversations as a surprise (a system going end-of-support, an application with no vendor support) rather than a planned transition.

---

### Use Case 4: Integration and Interface Map
**What it answers:** "What connects to what? What happens if this system goes down or is replaced?"

**How to start:** Create Interface Fact Sheets for the known integrations — starting with the highest-risk ones (Salesforce ↔ EBS, booking system ↔ scheduling, claims system ↔ insurer portals). Link each to the two Applications it connects.

**Connection:** The Salesforce ↔ EBS integration question from April 8 is an Interface Fact Sheet. So is every A2A-enabled agent handoff in the emerging agentic workflow.

---

### Use Case 5: Initiative and Programme Impact Tracking
**What it answers:** "Does CCOTF conflict with Nordics? Which applications does each initiative change?"

**How to start:** Create Initiative Fact Sheets for CCOTF, Nordics, and any active programmes. Link each to the Applications and Business Capabilities they change. LeanIX then shows overlap — two initiatives touching the same application is an automatic flag.

**Why this is a business differentiator:** This kind of visibility is genuinely hard to get without a tool like LeanIX. When EA can show that two programmes conflict six months before they collide, the credibility impact is significant.

---

### Use Case 6: Wardley Map Integration (Emerging)
**What it answers:** "Where do our capabilities sit on the commodity/custom axis? What should we build vs. buy?"

**How to approach:** LeanIX lifecycle data (is this application built on commodity or custom technology?) maps to the Wardley evolution axis. If LeanIX is the system of record, Wardley Maps become derivable from data rather than hand-drawn.

**Note:** This is a more advanced use case — build Use Cases 1–2 first before attempting this integration.

---

## Strategic Positioning

### LeanIX Is a Stakeholder Engagement Tool, Not Just a Repository

LeanIX's dashboards, reports, and Fact Sheet views are designed to be shared with non-EA stakeholders. A well-maintained LeanIX instance makes EA work visible and credible in a way that a folder of PowerPoints cannot. For an EA function building its reputation, this matters enormously — a stakeholder who can log into LeanIX and see the impact analysis for their initiative is experiencing EA value directly.

**Connection to EA Effectiveness:** LeanIX is the definitive dual-purpose artefact instrument — it is simultaneously the EA repository AND the stakeholder-facing visibility tool. Both purposes are served by the same dataset.

### The Recommendation Opportunity

If Belron does not currently use LeanIX (or uses it poorly), proposing and implementing an EA repository is a high-visibility, lasting initiative. It creates a permanent, queryable record of EA work that leadership can see and use. The five use cases above constitute the business case — each answers a question that leadership currently cannot answer reliably.

---

## Applications & Decision Path

### If Belron Has an Active LeanIX Instance
1. Get access and audit the current state of Fact Sheets and relationships
2. Identify the highest-value gap — typically APM completeness or capability linkage
3. Run a "LeanIX revival" mini-initiative: clean data, add relationships, train stakeholders
4. High-visibility, tangible contribution; builds on existing investment

### If Belron Does Not Have LeanIX
1. Build a one-page business case: APM + BCM + initiative tracking use cases justify a tool like LeanIX for a business of Belron's scale
2. Access the LeanIX free trial / community edition to test the data model
3. Complete LeanIX Academy introductory path (free, online)
4. Propose the tool with a concrete implementation approach (not just "we should get this")

---

## Boundaries & Limitations

**This framework works when:**
- The EA function has the mandate and access to create and maintain the repository
- Business capability owners can be identified and engaged to validate their Fact Sheets
- There is appetite for a formal EA tooling investment (or LeanIX is already available)

**This framework does NOT work when:**
- No one owns data quality — entries go stale within months
- EA is under-resourced and cannot maintain relationships alongside project work
- Stakeholders have no access to or interest in the repository outputs

**Common Failure Mode:** The Fact Sheet graveyard — entries created during an initial burst, not maintained, not connected, eventually abandoned. Prevented by: starting with questions (not inventory), assigning ownership, starting small.

---

## Evolution & History

### April 9, 2026: Research and Use Case Mapping
LeanIX researched from first principles. The Fact Sheet data model understood. Five Belron-specific use cases mapped. Data structuring principles identified (start with questions, relationships are the value, own the data quality, consistent tagging, minimum viable first).

Key insight: "LeanIX is the tooling layer for everything being built this week" — the BCM, systems landscape, integration map, and initiative tracking artefacts from the Belron Business Understanding Framework all have a natural LeanIX home.

**Source:** [[braindump-2026-04-09-1022-leanix-learning-use-cases]]

---

## Related Frameworks
- [[ea-effectiveness-framework]] — LeanIX is the definitive dual-purpose artefact: EA repository AND stakeholder visibility tool (Principle 2)
- [[belron-business-understanding-framework]] — Layers 4 (Systems Landscape) and 5 (Capability Map) both live in LeanIX; LeanIX makes these layers maintainable
- [[agentic-ai-governance-framework]] — The MCP Server registry and A2A workflow design both have natural LeanIX entries (Interface and Initiative Fact Sheets)

---

## Future Development

**Unanswered questions:**
- Does Belron already have a LeanIX instance? (Determines whether this is a "use it" or "propose it" path)
- If yes: what is the current state of the data — APM complete? Capabilities linked? Or a Fact Sheet graveyard?
- If no: what EAM tools (if any) are currently in use? This shapes the TCO argument for LeanIX

**Immediate actions:**
- [ ] Confirm whether Belron has LeanIX — ask manager or check with IT procurement 📅 2026-04-24
- [ ] If no instance: access LeanIX free trial and complete the introductory Academy path 📅 2026-04-27
- [ ] If instance exists: request access and audit the APM completeness 📅 2026-04-27

**Engagement opportunity:**
- **SAP LeanIX London Tour — April 30, 2026.** In-person SAP LeanIX event in London. Valuable for: (1) seeing the current product roadmap (LeanIX has been integrating with SAP Signavio for process + architecture combined views — relevant to Belron's business understanding work), (2) networking with other EA practitioners using LeanIX in regulated or complex businesses, (3) demonstrating to Belron leadership that the EA function is actively investing in the tooling conversation. If Belron is evaluating LeanIX, attending this event strengthens the internal business case.

---

*Consolidated from 1 source | First version: April 15, 2026 | Status: Working*
