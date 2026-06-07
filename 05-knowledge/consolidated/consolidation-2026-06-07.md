---
type: "knowledge-consolidation"
domain: "integrated"
date: "2026-06-07"
consolidation_period: "2026-05-20 to 2026-06-07"
created: "2026-06-07 10:49"
sources_analyzed: 18
frameworks_updated: ["agentic-ai-governance-framework", "ccotf-technology-architecture-framework"]
frameworks_created: ["architecture-operating-model-framework", "communities-of-practice-framework"]
patterns_identified: 4
tags: ["#consolidation", "#knowledge", "#frameworks"]
---

# Knowledge Consolidation — 7 June 2026

## Executive Summary

**Period:** 2026-05-20 to 2026-06-07 (18 days)

**Documents processed:**
- 12 professional braindumps
- 3 project braindumps (CCOTF ×2, MCP ×1)
- 2 personal braindumps (contextual)
- Daily briefs: June 1–7 (7 briefs)

**Major outcomes:**
- **2 new frameworks created:** Architecture Operating Model (EA/SA/TA), Communities of Practice
- **2 frameworks flagged for update:** Agentic AI Governance, CCOTF Technology Architecture
- **4 cross-cutting patterns identified**

---

## Major Themes This Period

### Theme 1: Architecture Community and Operating Model

**Frequency:** 4 documents, multiple conversation threads

**Core insight:** The EA/SA/TA split at Belron has a confirmed structural gap (no TA named roles) and a live interaction model problem (functional EAs vs. front/back office SAs don't map 1:1). A formal proposal is forming, targeted at the architecture community.

**Key sources:**
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]] — full current-state diagnosis and proposal structure
- [[braindump-2026-06-05-1739-btops-collaboration-ccotf-viva-engage]] — BT&Ops collaboration as a symptom of unclear boundary
- [[braindump-2026-05-31-communities-of-practice-notebooklm]] — CoP model as the mechanism for the architecture community

**Framework created:** [[architecture-operating-model-framework]]
**Status:** Emerging — proposal direction clear, socialisation needed

---

### Theme 2: MCP Governance Maturing into Production Reality

**Frequency:** 5+ daily briefs, 1 project braindump

**Core insight:** MCP has crossed from protocol standard into enterprise infrastructure. The governance question is no longer "whether" but "which tooling and at what layer." Three concrete options now exist: Docker MCP distribution tooling (open), Noma Agent Access Control (commercial), Microsoft Agent 365 Defender context mapping (Microsoft-stack). LeanIX has shipped an MCP server, creating a direct connection between the EA tooling and MCP governance work.

**Key sources:**
- [[daily-brief-2026-06-04]] — MCP Dev Summit: Docker tooling, AAIF security roadmap, OpenAI+Anthropic SDK convergence
- [[daily-brief-2026-06-07]] — Microsoft Agent 365 MCP context mapping arriving in Defender (June preview)
- [[daily-brief-2026-06-06]] — LeanIX MCP server: query EA data from Claude or Copilot
- [[braindump-2026-06-04-1710-mcp-ref-architecture-simplified-diagram]] — simplified diagram needed as communication artefact

**Framework to update:** [[agentic-ai-governance-framework]]

**Pending updates to agentic-ai-governance-framework:**
- Add MCP Dev Summit milestone: AAIF 170 orgs, 110M+ SDK downloads/month
- Add tooling options: Docker MCP distribution, Noma, Microsoft Agent 365 (compare at each governance layer)
- Add LeanIX MCP server as EA-tooling reference implementation
- Add Docker OCI distribution + Tasks primitive + MCP Triggers from the roadmap
- Update enterprise security landscape section with Agent 365 Defender context mapping

---

### Theme 3: CCaaS Vendor Landscape Restructured by Salesforce

**Frequency:** 3 braindumps, 2 daily briefs

**Core insight:** Salesforce has entered the CCaaS market natively (Agentforce Contact Center, GA February 2026) at the same time as Belron's Salesforce footprint (Service Cloud + Marketing Cloud) was confirmed. This changes the CCOTF vendor evaluation — Salesforce is now a first-party CCaaS option with dramatically lower switching cost given the existing estate. The 74% AI agent rollback rate (Sinch 2026) is an additional design constraint for any AI-in-CC deployment.

**Key sources:**
- [[daily-brief-2026-06-06]] — Salesforce Agentforce CC: first-party CCaaS for Belron
- [[braindump-2026-06-04-1523-salesforce-data-360]] — Data Cloud as the unification layer for Service Cloud + Marketing Cloud
- [[braindump-2026-05-30-0958-agentforce-contact-center-belron-fit]] — (CCOTF project) Agentforce fit assessment
- [[daily-brief-2026-06-04]] — 74% chatbot rollback rate as design constraint

**Framework to update:** [[ccotf-technology-architecture-framework]]

**Pending updates to ccotf-technology-architecture-framework:**
- Add Salesforce Agentforce Contact Center as a first-party CCaaS option (given Service Cloud footprint)
- Add the Genesys-Salesforce "frenemies" dynamic
- Add the 74% AI agent rollback rate as a design constraint in Domain 4 (AI & Automation)
- Add the Viva Engage vs. Teams community platform decision (Contact Centre Hive)
- Update vendor landscape: Zoom, Genesys, Microsoft, Salesforce (Agentforce CC), Vonage

---

### Theme 4: Communities of Practice as an Organisational Enabler

**Frequency:** 2 braindumps (May 31 — CoP guidebook synthesis + BCM NotebookLM)

**Core insight:** The CoP model (Domain + Community + Practice) is the right organisational design for the EA practice at Belron — both as a learning architecture for EA practitioners and as a mechanism for spreading capability-based thinking. The Contact Centre Hive concept emerging from CCOTF maps naturally to a CoP. The BT&Ops collaboration question may also be addressable through a cross-functional community design rather than a structural intervention.

**Key sources:**
- [[braindump-2026-05-31-communities-of-practice-notebooklm]] — full CoP framework synthesis
- [[braindump-2026-05-31-business-capability-mapping-notebooklm]] — BCM as a CoP output/workstream
- [[braindump-2026-06-05-1739-btops-collaboration-ccotf-viva-engage]] — Contact Centre Hive as CCOTF CoP

**Framework created:** [[communities-of-practice-framework]]
**Status:** Emerging — research strong; Belron application to design

---

## New Frameworks Created

### 1. Architecture Operating Model Framework
**Location:** [[05-knowledge/consolidated/architecture-operating-model-framework]]

**Core principles:**
1. EA / SA / TA operate at different altitudes, not different ranks
2. The EA→SA interface is the live gap at Belron (functional vs. front/back office mismatch)
3. TA is the structural gap — named TA roles are the proposal's core deliverable
4. Four known failure modes — diagnose before prescribing

**Primary use case:** Drafting the best practice proposal for the architecture community

**Status:** Emerging — needs socialisation with Lead EA and SAs

---

### 2. Communities of Practice Framework
**Location:** [[05-knowledge/consolidated/communities-of-practice-framework]]

**Core principles:**
1. CoPs are defined by domain, not task — the three-element diagnostic (Domain + Community + Practice)
2. CoPs fail when treated as a service to the organisation
3. "News from the future" is the highest-value output — lead with this argument to sponsors
4. Sponsorship legitimises without controlling — three levels needed
5. The "non-launch" is often better than a formal launch event

**Applications at Belron:**
- EA CoP (architecture community)
- Contact Centre Hive (CCOTF cross-opco community)
- Data Architecture CoP (emerging)

**Status:** Emerging — research strong; Belron design not yet started

---

## Cross-Cutting Patterns

### Pattern 1: Governance Infrastructure Is Converging on EA-Owned Layers

The MCP governance tooling (Docker distribution, Noma, Agent 365), the LeanIX MCP server, and the EA/SA/TA operating model proposal all point to the same underlying pattern: the EA function is being handed new infrastructure governance responsibilities (AI agents, MCP servers, agentic workflows) at the same time as it's trying to establish its own operating model. The risk is that EA takes on governance of the new without fixing the operating model for the old.

**Implication:** The EA/SA/TA operating model proposal should be fast-tracked — it's the structural foundation for everything the EA function is being asked to govern.

---

### Pattern 2: Salesforce Is Becoming Belron's Default Customer Engagement Platform

Service Cloud (confirmed) + Marketing Cloud (confirmed) + Data Cloud (Front Office Guild — under discussion) + Agentforce Contact Center (CCOTF candidate) = a full customer engagement stack within one vendor. This is a strategic pattern, not a series of independent technology decisions.

**Implication:** A Salesforce ecosystem strategy for Belron (what we buy, what we don't, where we draw the line) should be a formal EA deliverable — before individual business units make incremental Salesforce decisions without a portfolio view.

---

### Pattern 3: The Pre-IPO Governance Window Is Closing

Multiple conversations this period touched the IPO context: the EA/SA/TA proposal ("IPO governance optics"), the MCP governance project ("governance maturity signal"), the EU AI Act (August 2 deadline — 56 days). With H2 2026 as the IPO target, June and July are likely the last months to formalise governance frameworks before due diligence begins. Any framework in "emerging" status should be expedited.

**Implication:** Prioritise the EA/SA/TA proposal and MCP Governance deliverables ahead of any analytical or exploratory work for the remainder of Q2.

---

### Pattern 4: Open-Loop Stakeholder Threads Are Accumulating

Multiple daybooks and braindumps this period contain named stakeholder threads with no confirmed close: Jamie (Qualtrics cross-market), Joakim (Genesys spreadsheet), Heidi (Seen.io + AI doc), Alex Jones (Sam Swift evaluation), Chris Dilts (Architecture Forum new ideas). These are decision-enabling conversations that are stalling discovery and project progress.

**Implication:** A stakeholder engagement tracker for active open loops is needed — this is a recurring operational pattern, not a one-off capture failure.

---

## Frameworks Requiring Updates (Not Yet Done)

| Framework | Update needed | Priority |
|---|---|---|
| [[agentic-ai-governance-framework]] | Add MCP Dev Summit data, Docker/Noma/Agent 365 tooling comparison, LeanIX MCP server | High |
| [[ccotf-technology-architecture-framework]] | Add Salesforce Agentforce CC, 74% rollback rate, vendor landscape update, Contact Centre Hive | High |

---

## Knowledge Base Maintenance

### New frameworks created this session
- ✅ `architecture-operating-model-framework.md`
- ✅ `communities-of-practice-framework.md`

### Braindumps to mark as consolidated
The following braindumps were fully incorporated into this consolidation and can be marked `status: "consolidated"`:
- `braindump-2026-06-04-1516-architecture-split-ea-sa-ta.md`
- `braindump-2026-05-31-communities-of-practice-notebooklm.md`
- `braindump-2026-06-04-1523-salesforce-data-360.md` (partially — Salesforce ecosystem pattern)
- `braindump-2026-06-05-1739-btops-collaboration-ccotf-viva-engage.md`

### Braindumps still active (not yet consolidated)
- `braindump-2026-06-04-1710-mcp-ref-architecture-simplified-diagram.md` — action item in flight
- `braindump-2026-06-05-1739-alex-jones-sam-swift-evaluation-followup.md` — open stakeholder thread
- `braindump-2026-06-05-1739-arch-forum-chris-dilts-new-ideas.md` — follow-up pending

---

## Next Steps

### Immediate
- [ ] Update `agentic-ai-governance-framework.md` with MCP Dev Summit findings and tooling comparison 📅 2026-06-09
- [ ] Update `ccotf-technology-architecture-framework.md` with Salesforce Agentforce CC and 74% rollback stat 📅 2026-06-09

### Short-term
- [ ] Draft EA/SA/TA proposal for the architecture community — use the new framework as the outline 📅 2026-06-14
- [ ] Draft EA CoP one-pager — use communities-of-practice-framework as the guide 📅 2026-06-14
- [ ] Build a stakeholder engagement tracker for active open loops (Jamie, Joakim, Heidi, Chris Dilts) 📅 2026-06-09

### Next consolidation
- **Suggested:** 2026-06-21 (two weeks)
- **Focus:** Validate emerging frameworks with real-world application; update agentic-ai-governance with live tooling evaluation

---

*Consolidation completed: 2026-06-07 | 18 documents processed | 2 frameworks created | 2 frameworks flagged for update | 4 patterns identified*
