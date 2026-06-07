---
type: "consolidated-knowledge"
domain: "professional"
framework: "architecture-operating-model"
created: "2026-06-07"
last_updated: "2026-06-07"
consolidation_id: "consolidation-2026-06-07"
source_documents: 3
status: "emerging"
tags: ["#framework", "#consolidated", "#enterprise-architecture", "#operating-model", "#EA", "#SA", "#TA"]
---

# Architecture Operating Model Framework (EA / SA / TA)

## Framework Overview
A working model for how Enterprise Architecture, Solution Architecture, and Technical Architecture roles should be defined, differentiated, and structured to work together effectively — anchored to Belron's current architecture structure and pre-IPO governance context.

**Status:** Emerging (current state confirmed; proposal direction clear; final model not yet socialised)
**Last Updated:** 2026-06-07
**Source Insights:** 3 documents — [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]], conversation context (June 4–5 2026)

---

## Belron Current State (as of June 2026)

```
Lead EA (Chief / Head of Enterprise Architecture)
 ├── Functional EAs — split by domain
 │    ├── Customer EA
 │    ├── Operations EA
 │    ├── Finance EA
 │    ├── Data EA          ← inside EA function
 │    └── Security EA      ← inside EA function
 │
Solution Architects — split by Front Office / Back Office
 ├── Front Office SAs
 └── Back Office SAs

Technical Architecture — no named roles (gap)
```

**Confirmed facts:**
- ✅ Lead EA exists above the functional EAs — cross-cutting direction available
- ✅ Data and Security architecture sit inside EA as functional domains
- ✅ SAs split by Front/Back Office
- ❌ TA: no named roles — functional gap

**Audience for the proposal:** Architecture community

---

## Core Principles

### Principle 1: The Three Levels Operate at Different Altitudes — Not Different Ranks

**Statement:** EA, SA, and TA are not a seniority hierarchy — they are different operating altitudes, each answering a different question at a different time horizon.

| Level | Horizon | Question it answers | Primary stakeholders |
|---|---|---|---|
| **EA** | 3–5 years | Are we investing in the right things, the right way? | CxO, business domain leads |
| **SA** | 6–18 months | How do we build this specific thing in a way that fits the enterprise? | Programme managers, product owners, delivery leads |
| **TA** | Sprint to quarter | How exactly do we build this component, within what constraints? | Engineering leads, DevOps, security engineering |

**Implication:** An EA who drops into SA-level work is not "helping" — they are doing the wrong job. Clear altitude discipline is a governance requirement, not a preference.

**Evidence:**
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]] — "The split only works if the handoff points are explicit"

**Confidence:** High — consistent with TOGAF ADM and industry EA practice

---

### Principle 2: The EA → SA Interface Is the Live Gap at Belron

**Statement:** Functional EAs (by domain) and SAs (by Front/Back Office) do not map 1:1. A Front Office SA regularly spans multiple EA domains simultaneously. Without a defined interaction model, the EA→SA joint is where standards get ignored and decisions fall between the cracks.

**The mismatch:**
```
Front Office SA ──── Customer EA    (primary)
                └─── Digital EA     (secondary)
                └─── Data EA        (cross-cutting)

Back Office SA  ──── Finance EA     (primary)
                └─── Operations EA  (secondary)
                └─── Data EA        (cross-cutting)
```

**Proposed interaction model:**
- **Primary EA per SA:** Each SA programme has one named EA as the primary engagement point, based on the dominant domain of the programme
- **Cross-domain arbitration:** When a programme spans multiple EA domains, the Lead EA is the tiebreaker
- **Published domain map:** A simple matrix showing which functional EA owns which domain space — SA engagement guide

**Evidence:**
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]] — "The proposal needs a primary-EA-per-programme rule and an escalation path to Lead EA for cross-domain conflicts"

**Confidence:** High — the structural mismatch is confirmed; the interaction model is proposed, not yet validated

---

### Principle 3: TA Is the Structural Gap — Formalising It Is the Proposal's Core Deliverable

**Statement:** Without named Technical Architects, technical architecture decisions are either being made by SAs (too high / too abstract), by senior engineers in delivery (uncoordinated, inconsistent), or not being made at all (risk). Introducing named TA roles is the proposal's most impactful recommendation.

**Two options for the proposal:**

| | Option A: Named Technical Architects | Option B: Formalise Principal Engineers |
|---|---|---|
| **What** | Defined TA roles, aligned to delivery programmes | Recognise existing senior engineers as TAs within the architecture community |
| **Accountable to** | SA (for programme) + architecture community (for standards) | Delivery lead (primary) + architecture community (secondary) |
| **Governance** | Cleaner — formal accountability for standards | Lighter — depends on engineering culture |
| **Speed to implement** | Slower — may require hiring or role redesign | Faster — works with existing people |
| **IPO appropriateness** | More defensible — clear named accountability | Softer — harder to demonstrate to auditors |
| **Recommendation** | Preferred for Belron's pre-IPO context | Fallback if Option A faces headcount resistance |

**Evidence:**
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]] — "For Belron's scale and IPO context, Option A is the more defensible governance model"

**Confidence:** High on the gap; Medium on the preferred option (depends on headcount and culture)

---

### Principle 4: Common Failure Modes — Diagnose Before Prescribing

**Statement:** The three most common EA/SA/TA failure modes are known. The proposal should explicitly name which ones apply at Belron and how the proposed model prevents them.

| Failure Mode | Description | Prevention |
|---|---|---|
| **EA without SA** | EA produces strategy, delivery teams invent their own patterns | The SA layer + EA engagement matrix |
| **SA without authority** | SA produces documents, delivery teams bypass them | Architecture Review Board / Design Authority with teeth |
| **TA/Engineering blur** | TAs absorbed into delivery, standards disappear | Named TA roles accountable to the architecture community |
| **No Review Board** | No enforcement mechanism, no learning loop | Formal ARB or Design Authority as part of the proposal |

---

## Applications & Use Cases

### Use Case 1: Designing the Proposal for the Architecture Community

**When to apply:** When drafting the EA/SA/TA best practice proposal

**Structure:**
1. **Section 1:** Affirm and document the EA structure (Lead EA + functional EAs + domain map)
2. **Section 2:** Define the EA↔SA interaction model (primary EA per programme, escalation to Lead EA)
3. **Section 3:** Introduce TA (Option A: Named TAs, Option B: Formalised Principal Engineers)
4. **Section 4:** Define the governance mechanism (Architecture Review Board / Design Authority)
5. **Section 5:** Define artefact ownership at each level

**Artefact ownership by level:**

| Level | Artefact |
|---|---|
| EA | Business Capability Map, Application Portfolio, Architecture Principles, Technology Radar, Reference Architectures |
| SA | Solution Architecture Document (SAD), Integration Design, Data Model, NFRs, Risk Log |
| TA | Infrastructure Diagrams, API Specs, Deployment Architecture, ADRs (Architecture Decision Records) |

### Use Case 2: Evaluating Whether a Decision Is Being Made at the Right Altitude

**When to apply:** During a project when it's unclear who should make a particular architecture decision

**Test:** 
- Who is affected over what timeframe? → Enterprise (EA) / Programme (SA) / Component (TA)?
- Is the decision about principles/standards, or about how to implement within known standards?
- If the decision were wrong, who would be impacted and for how long?

---

## Boundaries & Limitations

**This framework works when:**
- The architecture function is large enough to have distinct EA, SA, and TA roles
- Leadership understands and supports role separation (not just "everyone is an architect")
- There is a governance mechanism (ARB or equivalent) to give the framework teeth

**This framework does NOT work when:**
- The organisation is too small for the three levels to be distinct people
- EA is purely advisory with no authority — the altitude model requires authority at each level to be effective
- The operating model changes frequently (e.g., major restructure imminent) — wait for stability before formalising

---

## Future Development

**Questions for deeper exploration:**
- How does the TA role interact with Platform Engineering / DevOps squads? There's a risk of overlap with technical leads embedded in stream-aligned teams
- Should the Architecture Review Board be positioned as EA-chaired or chaired by the Lead EA? Who has veto power?
- How does the model extend to opco architects (if Belron has local architecture resource in opcos)?

**Next steps for the proposal:**
- [ ] Draft the interaction model as a visual (1-page diagram) 📅 2026-06-14
- [ ] Socialise with the Lead EA and one or two SAs to validate the current-state diagnosis 📅 2026-06-14
- [ ] Present to the architecture community as a working draft 📅 2026-06-21

---

## Related Frameworks

- [[ea-effectiveness-framework]] — The effectiveness model that sits alongside this operating model
- [[communities-of-practice-framework]] — The EA CoP model that supports the architecture community this proposal is being built for
- [[agentic-ai-governance-framework]] — The MCP governance work that demonstrates TA-level architecture in practice

---

*Consolidated from 3 sources | Confidence: High on diagnosis, Medium on proposed options | Status: Emerging*
*Created: 2026-06-07 | Consolidation: [[consolidation-2026-06-07]]*
