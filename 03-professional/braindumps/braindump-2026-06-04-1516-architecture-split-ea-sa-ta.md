---
type: "braindump"
domain: "professional"
date: "2026-06-04"
created: "2026-06-04 15:16"
themes: ["enterprise architecture", "architecture operating model", "EA SA TA split", "best practice proposal"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#enterprise-architecture", "#operating-model"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-06-14]]"
consolidated_date: "2026-06-14"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Architecture Role Split — EA, SA, TA Best Practice Proposal

## Raw Thoughts

need to look at the split of architecture - EA, SA, TA - put together a proposal for best practice

---

## Content Analysis

### Main Themes
1. **Role clarity:** The three architecture disciplines (EA, SA, TA) likely have unclear or overlapping boundaries at Belron — this is the problem to diagnose.
2. **Best practice proposal:** The output is a document/proposal — not just analysis but a recommendation that can be socialised and actioned.
3. **Operating model design:** This is fundamentally about how architecture work is organised, governed, and handed off across levels.

### Questions Raised
- What is the current state at Belron — do all three roles formally exist, or are some missing/collapsed?
- Where are the current pain points? (EA too abstract? SA missing? TA overlapping with engineering?)
- Who is the audience for the proposal — CTO, CIO, architecture community, delivery teams?
- Is this about defining roles for a hiring plan, or clarifying boundaries for existing people?
- Does this apply to the central EA function only, or should it cover opco/local architecture too?

### Decisions Contemplated
- Scope: central Belron architecture only, or including opco architects?
- Format: position paper, RACI, role profiles, or all three?
- Governance: should the proposal include how EA, SA, TA interact with delivery (e.g. Architecture Review Board, design authority)?

---

## Strategic Intelligence

### Key Insights

1. **The EA/SA/TA split is a classic enterprise tension.** EA tends to operate at 3-5 year horizons and gets accused of being disconnected from delivery. SA is the critical bridge layer — often the most under-resourced or most unclear role. TA overlaps with principal engineers and can be hard to distinguish from senior development leadership. Getting the split right is about altitude, not just titles.

2. **The split only works if the handoff points are explicit.** The most common failure is that each level produces artefacts the next level ignores. EA produces principles nobody reads. SA produces SADs that delivery teams bypass. TA produces specs that get overridden in sprint. The proposal needs to define not just the roles but the governance gates between them.

3. **Belron's pre-IPO context raises the stakes.** An architecture operating model proposal made now will be read against IPO readiness — investors and auditors want to see that IT governance is mature. A clear EA/SA/TA model with defined accountability is a governance maturity signal, not just an internal process improvement.

### The Three Levels — Working Definitions

**Enterprise Architecture (EA)**
- Horizon: 3-5 years
- Focus: Strategic alignment between business capability and technology. Portfolio-level decisions. Principles, standards, reference architectures, technology radar.
- Artefacts: Business Capability Map, Application Portfolio, Architecture Principles, Technology Radar, Reference Architecture patterns
- Stakeholders: CxO, business domain leads, programme sponsors
- Key question it answers: *Are we investing in the right things, in the right way, for the right reasons?*

**Solution Architecture (SA)**
- Horizon: 6-18 months (programme/project level)
- Focus: Translating business requirements into a coherent technical design that complies with EA standards. Cross-system integration, data flows, non-functional requirements.
- Artefacts: Solution Architecture Document (SAD), integration design, data model, non-functional requirements, risk log
- Stakeholders: Programme managers, product owners, delivery leads, security, data
- Key question it answers: *How do we build this specific thing in a way that fits the enterprise?*

**Technical Architecture (TA)**
- Horizon: Sprint to quarter (component/system level)
- Focus: Deep technical design — infrastructure, platform choices, API contracts, security controls, performance, deployment patterns. Often embedded in a delivery team.
- Artefacts: Infrastructure diagrams, API specifications, deployment architecture, technical spike outputs, ADRs (Architecture Decision Records)
- Stakeholders: Engineering leads, DevOps/platform, security engineering, product teams
- Key question it answers: *How exactly do we build this component, and what are the technical constraints?*

### Current State at Belron (2026-06-04)

- **EA:** Structured by **functional area** (domain-aligned EAs — e.g. Customer, Operations, Finance, etc.)
- **SA:** Structured by **Front Office / Back Office** split
- **TA:** Not yet confirmed — likely the gap to define
- **Audience for proposal:** Architecture community

**Structural tension this creates:**

The EA functional split and the SA front/back split don't map neatly onto each other. A Front Office SA will interact with multiple functional EAs (Customer EA, Digital EA, etc.). A Back Office SA will interact with Finance EA, HR EA, Operations EA. Without a clear interaction model, the joints between EA and SA become ambiguous — SAs aren't sure which EA owns which standard, and EAs aren't sure which SA is accountable for which programme.

**Confirmed current state (2026-06-04):**
- ✅ Lead/Chief EA exists above the functional EAs — cross-cutting direction is available
- ✅ Security and Data architecture sit inside EA as functional domains — not a gap
- ❌ TA: no named roles anywhere — this is the primary gap the proposal needs to address

**Current-state structure:**
```
Lead EA
 ├── Functional EAs (Customer, Operations, Finance, Data, Security, etc.)
 └── [interface unclear] ↕
Solution Architects
 ├── Front Office SAs
 └── Back Office SAs
[TA layer: absent]
```

---

### Proposal Shape — What the Architecture Community Needs

Given the confirmed current state, the proposal has three distinct jobs:

**1. Affirm and clarify the EA structure (working well, needs documenting)**
- The Lead EA + functional EA model is sound — this is domain-aligned federated EA
- The security and data EA domains inside the function are the right call
- What's missing is a published map of which functional EA owns which domain, so SAs know who to engage

**2. Define the EA ↔ SA interaction model (the live gap)**
- Functional EAs (domain) and SAs (front/back office) don't map 1:1
- A Front Office SA will regularly span Customer EA, Digital EA, and possibly Data EA simultaneously
- Proposal needs a clear primary-EA-per-programme rule, plus an escalation path to Lead EA for cross-domain conflicts
- Suggested pattern: SA engagement matrix — which EA domain is primary for which type of programme, with Lead EA as tiebreaker

**3. Introduce TA as a named role (the structural gap)**
- Currently absent — technical architecture decisions are either being made by SAs (too high) or by senior engineers in delivery (too low, uncoordinated)
- Two viable models to propose:
  - **Option A — Named Technical Architects:** Defined TA roles, aligned to delivery programmes, accountable to the SA for their programme and to the architecture community for standards
  - **Option B — Principal Engineers with architecture accountability:** Formalise existing senior delivery people as TAs within the community framework — lower cost, faster to implement, but relies on engineering culture
- For Belron's scale and IPO context, Option A is the more defensible governance model

### Common Failure Patterns to Address in the Proposal

- **EA without SA:** EA produces strategy, but there's no translation layer into projects — delivery teams invent their own patterns and EA standards are ignored.
- **SA without authority:** SA produces documents but can't enforce compliance — becomes a tick-box exercise.
- **TA/Engineering blur:** Technical architects get absorbed into delivery teams and effectively become senior engineers — strategic technical thinking disappears.
- **No Review Board:** Without a defined Architecture Review Board or Design Authority, there's no enforcement mechanism and no learning loop back to EA.

### Strategic Implications
- This proposal positions the EA function at Belron as mature and delivery-connected — directly relevant to IPO governance optics
- Defining the split clearly helps make the case for headcount at each level (important if Belron needs to scale the architecture function post-IPO)
- A clean EA/SA/TA model also enables opco architects to understand where they fit in the global model

---

## Action Items

### Immediate (24-48 hours)
- [ ] Sketch the current-state picture: which of EA, SA, TA roles formally exist at Belron today, and where the gaps/overlaps are 📅 2026-06-05

### Short-term (1-2 weeks)
- [ ] Draft the best practice proposal — cover: role definitions, altitude model, handoff points, artefact ownership, governance gates (ARB/Design Authority) 📅 2026-06-11
- [ ] Identify who the proposal is for and what decision it needs to enable — hiring plan, governance improvement, or operating model design? 📅 2026-06-11

### Strategic Considerations
- Consider referencing TOGAF ADM phase alignment (each phase maps naturally to EA/SA/TA levels) to give the proposal external credibility
- The proposal could become the foundation for an Architecture Community of Practice charter at Belron
- Worth benchmarking against how a comparable enterprise (similar scale, pre-IPO or recently listed) structures their architecture function

---

## Connections
- **Related Braindumps:** (none yet — this is the seed thought)
- **Relevant Context:** Armo is Enterprise Architect at Belron, pre-IPO context (H2 2026 target)
- **Frameworks:** TOGAF ADM, ArchiMate, Architecture Review Board patterns

---

## Domain Classification
- **Primary Domain:** Professional (97%)
- **Reasoning:** Core EA operating model work, directly relevant to Armo's role at Belron.
- **Cross-Domain Elements:** None
- **Privacy Level:** confidential — internal Belron organisational design

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — this is a considered strategic thought, not urgent reactive capture
- **Emotional Tone:** Curious / purposeful — a topic Armo is ready to develop further
- **Implications:** This has the makings of a significant deliverable. Worth scheduling dedicated thinking time.

### Confidence Assessment
- **Overall Analysis:** 88% — the thought is clear but the Belron-specific context (current state of roles) is unknown and will shape the proposal significantly.
- **Areas Requiring Clarification:** What is the current role structure at Belron? Who would approve/receive this proposal?

---

*Processed by COG Brain Dump Analyst*
