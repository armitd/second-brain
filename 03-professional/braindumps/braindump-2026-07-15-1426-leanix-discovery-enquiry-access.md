---
type: "braindump"
domain: "professional"
date: "2026-07-15"
created: "2026-07-15 14:26"
themes: ["leanix", "enterprise-architecture", "sap", "tooling", "licensing"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#leanix", "#eam"]
status: "consolidated"
energy_level: "medium"
emotional_tone: "curious"
confidence: "medium"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: LeanIX Discovery — Expanding Use & Non-Licensed Enquiry Access

## Raw Thoughts
LeanIX discovery. What else can we do with it? How do we give non-licenced users enquiry access.

How do we sell the LeanIX governance model to the AI group?

LeanIX as a governance tool — not just an EA inventory, but the platform of record for governing the estate.

"If you are working in LeanIX, then it makes sense to govern in LeanIX."

*(Context from daybook 2026-07-15: raised alongside "SAP / LeanIX" and "AI Governance" in the Front Office Meeting.)*

## Content Analysis

### Main Themes
1. **Tool exploitation:** Belron already has LeanIX (now SAP LeanIX) — the question is whether the platform is being used to anywhere near its full capability, or just as an application inventory.
2. **Access democratisation:** Getting architecture data in front of a wider audience (stakeholders, delivery teams, business owners) without the cost/friction of full editor licences.
3. **SAP alignment:** LeanIX is now part of SAP. Its roadmap increasingly ties to SAP transformation (RISE, S/4HANA), which is directly relevant to the "SAP / LeanIX" meeting thread.

### Supporting Ideas
- "Discovery" suggests this is a scoping/assessment exercise, not a committed roadmap yet — good moment to shape how the tool is positioned internally.
- Non-licensed access is really two questions: (a) what the LeanIX licence model allows, and (b) what alternative distribution channels exist (exports, embeds, API-fed dashboards).

### Questions Raised
- What is Belron's current SAP LeanIX contract tier, and how many editor vs viewer seats does it include?
- Are viewer/read-only seats free, capped, or chargeable under our specific contract?
- Who is the LeanIX admin / product owner internally, and who owns the SAP relationship?
- What is the actual demand — how many people want enquiry access, and for what (portfolio queries, roadmaps, tech risk)?
- Who leads the AI group, and what governance (if any) do they already have? Where's the gap the LeanIX model fills?

### Decisions Contemplated
- Whether to expand LeanIX usage into new modules/use cases vs keep it as an APM inventory.
- Whether wider access is delivered via LeanIX viewer seats or via exported/embedded reporting.

## Strategic Intelligence

### What else can we do with LeanIX? (capability landscape)

Beyond application inventory, SAP LeanIX supports:

- **Application Portfolio Management (APM):** lifecycle tracking, TIME classification (Tolerate / Invest / Migrate / Eliminate), cost and business-criticality heatmaps. Rationalisation candidate.
- **Technology Risk & Obsolescence:** tech stack catalogue with lifecycle/end-of-life data, flagging unsupported components — strong pre-IPO due-diligence and risk story.
- **Business Capability Modelling:** capability maps with heatmaps overlaying cost, risk, or strategic fit — the bridge between business and IT that lands with non-technical execs.
- **Integration / Interface Architecture:** interface catalogue and data-flow modelling — useful for the SAP transformation and Contact Centre work.
- **Transformation & Roadmap planning:** target-state architectures, roadmap fact sheets, milestone tracking.
- **SAP transformation support:** SAP LeanIX increasingly ties into RISE with SAP / S/4HANA migration planning — directly relevant to the "SAP / LeanIX" agenda item.
- **SaaS / Cloud management (SMP):** discovery of shadow SaaS and spend, if that module is licensed.
- **Surveys & Fact Sheet subscriptions:** crowdsource data quality by asking app owners to confirm/update their own fact sheets — a scalable way to keep the repository current.
- **Reporting suite:** landscape, matrix, roadmap, portfolio, data-flow reports — many shareable.
- **API & integrations:** REST/GraphQL API plus out-of-the-box connectors (ServiceNow, Signavio, etc.) to sync CMDB and process data.

### Non-licensed enquiry access (options to explore)

- **Viewer / read-only role:** LeanIX has role tiers (Admin / Member / Viewer). Whether viewers are free or chargeable depends entirely on Belron's contract — confirm with the account team.
- **Shared report links & snapshots:** reports can be shared or snapshotted for people who don't log in.
- **Exports:** PDF / Excel / PowerPoint exports distributed via SharePoint/Teams/Confluence for true zero-licence consumption.
- **API-fed dashboards:** pull data via the API into Power BI / an internal portal so non-licensed users query a downstream dashboard, never touching LeanIX itself. Most scalable if demand is high.
- **Embedded reports:** surface LeanIX reports inside an existing intranet/Confluence page.

> ⚠️ Licensing specifics (viewer seat cost, caps, API usage rights) are contract-dependent. Treat the above as options to validate, not confirmed entitlements. Confirm with the SAP LeanIX account manager / Belron's licence owner before committing to an approach.

### LeanIX as a governance tool (not just an inventory)

Reframing LeanIX from "the EA team's application catalogue" to "Belron's platform of record for governing the technology estate."

> **Guiding principle:** *"If you are working in LeanIX, then it makes sense to govern in LeanIX."* Govern where the work already lives — don't stand up a separate governance layer that duplicates the register and drifts out of sync.

The governance capabilities already in the box:

- **Data quality & completeness governance:** fact-sheet quality seals, mandatory fields, and completeness scoring keep the repository trustworthy enough to make decisions on.
- **Ownership & accountability:** every asset has a named owner and subscription roles — governance starts with someone being accountable.
- **Lifecycle governance:** lifecycle states (Plan → Phase-in → Active → Phase-out → End-of-life) turn the register into a controlled roadmap, not a static list.
- **Technology risk & obsolescence governance:** end-of-life tracking flags unsupported tech before it becomes an audit or security finding.
- **Portfolio decision governance:** TIME classification (Tolerate/Invest/Migrate/Eliminate) and heatmaps give a repeatable basis for rationalisation calls.
- **Standards & compliance:** reference architectures and policy fact sheets let you define "the standard" and measure drift against it.
- **Surveys as a control loop:** periodic owner surveys operationalise governance — data stays current because owners are prompted to re-certify.

**Why this framing matters:**
- Elevates LeanIX from a cost line to a control platform — strengthens the case for wider adoption and the enquiry-access question above.
- Establishes the single governance pattern that the AI-group pitch then extends (see below) — one model, applied consistently across apps, integrations, and AI.
- Directly supports the pre-IPO story: auditable governance over the technology estate.

> Positioning note: "governance tool" must not read as "system of control that slows delivery." Frame it as the trusted source of truth that makes faster, safer decisions possible.

### Selling the LeanIX governance model to the AI group

The pitch is not "use our tool" — it's "adopt our governance discipline for AI assets." The LeanIX governance model already solves the problems the AI group is about to hit:

- **What the model gives them:** a single authoritative register of assets, clear ownership per asset, lifecycle states, defined review/refresh cycles, and portfolio-level risk/cost visibility. Map that onto AI: an inventory of AI use cases / models / agents, each with an accountable owner, a lifecycle (PoC → pilot → production → retire), and risk classification.
- **Why it lands now:** AI governance is being stood up from scratch. It is far cheaper to inherit a proven governance pattern than to invent a parallel one. Avoids a second, disconnected AI registry.
- **The integration angle:** register AI use cases and models as fact sheets in LeanIX (or a linked object type), so the AI portfolio sits inside the same landscape as the applications and integrations it touches — dependencies become visible, not hidden.
- **Pre-IPO framing:** demonstrable, auditable governance over the AI estate is an asset in IPO due diligence. "We know every AI system, who owns it, and its risk posture" is a strong story.
- **Ties to MCP Governance:** the same governed-source-of-truth principle underpins [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]] — the AI group governance conversation and the MCP governance work should reinforce, not duplicate, each other.

**How to sell it (tactics):**
1. Lead with their pain (shadow AI, no owner accountability, no risk view), not the tool.
2. Show a worked example — one real AI use case modelled as a LeanIX fact sheet with owner, lifecycle, and dependencies.
3. Offer a light-touch pilot: register the current AI PoCs (incl. AI Damage Assessment) rather than boiling the ocean.
4. Frame governance as an enabler of speed and trust, not a gate — this matters for adoption with an AI audience.

> Watch-out: don't let "governance" read as bureaucracy to an AI group that wants to move fast. Position it as guardrails that let them scale safely and pass IPO scrutiny.

### Key Insights
1. **The lever is usage maturity, not more tooling.** The value gap is almost certainly under-exploitation of what's already licensed — capability maps, tech-risk, roadmaps — rather than a missing feature.
2. **Access model choice hinges on demand shape.** A handful of stakeholders → viewer seats or shared reports. Broad, recurring demand → API-fed dashboard is cheaper and more durable than buying seats.
3. **Pre-IPO angle.** LeanIX tech-risk and portfolio data is a ready-made asset for IPO-grade IT due diligence and rationalisation narratives — worth framing the "what else" answer around that.

### Pattern Recognition
- **Connection to previous thinking:** ties to your EA remit and the SAP transformation thread; overlaps with MCP Governance in the general theme of "governed access to a shared source of truth."
- **Recurring pattern:** democratising access to a specialist tool without blowing licence budget — same shape recurs across enterprise tooling.

### Strategic Implications
- Positions LeanIX as an enterprise decision-support asset (esp. for SAP transformation and IPO readiness), not just an EA team repository.
- Access strategy has direct cost implications — worth a quick options/cost comparison before any seat purchase.

## Action Items

### Immediate (24-48 hours)
- [ ] Identify Belron's LeanIX admin / product owner and the SAP LeanIX account contact 📅 2026-07-16
- [ ] Pull the current LeanIX contract to check tier, seat counts, and viewer-seat terms 📅 2026-07-16

### Short-term (1-2 weeks)
- [ ] Scope the actual demand for enquiry access — who wants it and for what queries 📅 2026-07-22
- [ ] Ask the LeanIX account manager to confirm viewer-seat cost/caps and API usage rights 📅 2026-07-22
- [ ] Run a short internal "what are we not using?" audit against the module list above 📅 2026-07-22
- [ ] Draft a one-slide pitch for the AI group: LeanIX governance model applied to AI assets (register PoCs as fact sheets) 📅 2026-07-22

### Strategic Considerations
- Consider a one-page LeanIX value/roadmap paper tying capabilities to SAP transformation + IPO due diligence.
- Decide the access pattern (viewer seats vs API-fed dashboard vs exports) based on demand shape before spending.

## Connections
- **Related Braindumps:** *(none yet — first LeanIX capture)*
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]] (governed access theme), [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]] (integration architecture)
- **Knowledge Base:** *(candidate for a future EA-tooling reference note)*
- **Source:** [[01-daily/daybooks/daybook-2026-07-15|Daybook 2026-07-15]]

## Domain Classification
- **Primary Domain:** professional (90%)
- **Reasoning:** EA tooling strategy in your Belron role; not tied to a single named active project.
- **Cross-Domain Elements:** touches MCP Governance and SAP transformation.
- **Privacy Level:** confidential (internal Belron tooling/licensing)

## Processing Notes
### Emotional Context
- **Energy Level:** medium
- **Emotional Tone:** curious / exploratory ("discovery")
- **Implications:** early-stage scoping — good time to shape positioning before decisions harden.

### Confidence Assessment
- **Overall Analysis:** 80% — questions are clear; capability landscape is well understood.
- **Domain Classification:** 90% — clearly professional.
- **Strategic Insights:** 75% — sound in general, but the access answer depends on Belron's specific contract terms, which I can't see.
- **Areas Requiring Clarification:** current contract tier, seat model, and real demand volume.

---

*Processed by COG Brain Dump Analyst*
