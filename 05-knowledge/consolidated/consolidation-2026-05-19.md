---
type: "knowledge-consolidation"
domain: "integrated"
date: "2026-05-19"
consolidation_period: "2026-05-12 to 2026-05-19"
created: "2026-05-19 09:06"
sources_analyzed: 15
frameworks_updated: ["ea-effectiveness-framework", "ccotf-technology-architecture-framework", "ai-damage-assessment-strategy-framework"]
frameworks_created: ["microsoft-single-tenant-strategy-framework"]
patterns_identified: 1
tags: ["#consolidation", "#knowledge", "#frameworks"]
---

# Knowledge Consolidation — 19 May 2026

## Executive Summary

**Period Analysed:** 12 May – 19 May 2026

**Documents Processed:**
- 8 professional braindumps (May 6–18)
- 6 personal braindumps (May 5–17, some carrying over from previous period)
- 1 project braindump (Obsidian Business OS / COG, processed 18 May)

**Major Outcomes:**
- **Frameworks Updated:** 3 — EA Effectiveness (Principles 7 + 8 added), CCOTF Technology Architecture (Principles 6 + 7 added), AI Damage Assessment Strategy (Principles 5 + 6 added + AutoBolt in competitive landscape)
- **New Framework Created:** 1 — Microsoft Single Tenant Strategy
- **Patterns Identified:** 1 — Platform Activation Gap
- **Timeline Entries:** 0

**Key Insights Synthesised:**
1. **The AI case for Microsoft single tenant is now the dominant argument.** Microsoft Agent 365 and the Copilot/AOAI wave have changed the cost-benefit calculus for tenant consolidation more than any IT simplification argument has in five years. The recommendation: decide and document the architecture direction now (pre-IPO), begin execution post-IPO in 2027.
2. **Belron has a structural platform activation gap — across Informatica, Microsoft, and LeanIX.** Every new business requirement should start with "do we already have this?" before commissioning new tooling. The Informatica IDMC platform almost certainly has Data Quality, Catalog, and AI Governance modules available and unactivated — worth auditing before the EU AI Act compliance workstream buys anything new.
3. **Salesforce's acquisition of Informatica has materially changed the CCaaS platform evaluation.** Agentforce Contact Center + Informatica MDM is now a data-integrated, AI-native contact centre stack. If Belron uses Salesforce CRM, this is a structural advantage that Microsoft and Amazon cannot easily match at the data layer. The CCOTF platform evaluation must now be explicitly three-way.

---

## Processing Statistics

- **Total documents analysed:** 15
- **Date range:** 12–19 May 2026
- **Domains covered:** Professional (EA strategy, platform strategy, vendor intelligence), Personal (home, health, admin), Project (CCOTF, AI Damage Assessment, MCP Governance)
- **Frameworks updated:** 3
- **New frameworks created:** 1 (total frameworks: 10)
- **Patterns identified:** 1

---

## Major Themes This Period

### Theme 1: Microsoft Single Tenant — AI Has Changed the Equation
**Frequency:** 2 professional braindumps; 3+ daily briefs (Microsoft Agent 365 GA, IPO context)

**What emerged:**
The May 14 braindump on Microsoft single tenant is the most comprehensive strategic analysis of this period. What is new is not the question (whether Belron should consolidate tenants) but the answer to "why now": the AI and Copilot wave makes single tenant dramatically more valuable than it was 18 months ago. MCP-governed agentic AI, Copilot across the group, Azure OpenAI Service at scale — all require unified identity. The cost-benefit equation has shifted.

The May 16 CCOTF braindump corroborated the timing argument: Microsoft Agent 365 GA (May 1) is the first time there's a commercially priced product ($15/user/month) that directly rewards single-tenant topology. The IPO context adds urgency to getting the *architecture decision* on paper — even if execution must wait until 2027.

**New framework created:** [[microsoft-single-tenant-strategy-framework]]

**Status:** Emerging (needs validation of Belron's actual current tenant state — the number of Entra ID tenants is the single most important unknown)

---

### Theme 2: Platform Activation Gap — Informatica as the Test Case
**Frequency:** 1 deep professional braindump + pattern across 3 platforms (Informatica, Microsoft, LeanIX)

**What emerged:**
The May 14 braindump on Informatica IDMC revealed a structural pattern: Belron has paid for enterprise platform capabilities it is not using. Informatica is the clearest current example — the IDMC platform includes Data Quality, Data Catalog, Data Governance, API Integration, and an AI Governance Catalog, all likely available under the existing MDM subscription. None appear to be activated.

This matters because:
- The EU AI Act compliance workstream needs an AI model inventory, data lineage, and risk scoring tool — Informatica IDMC already has all three
- The AI Damage Assessment PoC needs training data quality profiling — Informatica CLAIRE DQ Agent does exactly this
- The Salesforce Agentforce data layer for CCOTF is Informatica — if Belron already has the subscription, the integration story changes

The same pattern (owned but not activated) likely applies to Microsoft E5 Security and LeanIX Business Architecture features. The recommended EA contribution: run a platform audit as a proactive stakeholder engagement — it is both an EA intelligence exercise and a high-impact business case conversation.

**New pattern documented:** [[pattern-platform-activation-gap]]

**Status:** Stable pattern — expected to continue appearing; now named and documented

---

### Theme 3: Salesforce/Informatica Convergence Changes the CCOTF Evaluation
**Frequency:** 1 deep professional braindump

**What emerged:**
Salesforce acquired Informatica ($8B, closed November 2025). The strategic implication: Informatica is no longer a standalone data management vendor — it is now the trusted data foundation for Salesforce Agentforce's agentic AI stack. If Belron uses Salesforce CRM (unknown) and already has Informatica MDM (likely), then Salesforce Agentforce CC becomes the CCaaS option with the most pre-built data integration — Customer 360 master data feeding AI agents directly, without additional ETL build.

The CCOTF platform evaluation must now be explicitly three-way: Microsoft-stack vs. Salesforce-stack vs. Amazon-stack. The Informatica asset is the swing factor in the Microsoft vs. Salesforce comparison. CCOTF framework updated accordingly (Principles 6 and 7).

**Status:** Confirmed fact (acquisition closed). Belron-specific impact depends on Salesforce CRM usage — the pivotal unknown.

---

### Theme 4: EA as Innovation Enabler — Lean Startup + TOGAF Lite ADM
**Frequency:** 2 professional braindumps (Lean Startup cycle, TOGAF ADM templates)

**What emerged:**
Two braindumps this period make connected arguments: EA's role should expand from architecture review to *experiment design and governance*. The lean startup braindump frames innovation accounting as the tool — defining what "validated learning" looks like for AI PoCs before any code is written. The TOGAF ADM braindump frames the Architecture Contract as the missing governance artefact — what architecture commitments is the project team making, and what happens if they want to deviate?

Together these define a new EA role: not just governing architecture compliance but structuring how Belron learns from AI experiments and governs the architectural commitments each project team makes. EA Effectiveness Framework updated with Principles 7 and 8.

The Wizard of Oz MVP principle is directly applicable to all three active projects — run a human-in-the-loop phase before committing to model infrastructure. This is underused in enterprise AI and should become a standard recommendation.

**Status:** Working — both principles are well-grounded; application to Belron AI projects is direct but not yet validated in practice

---

### Theme 5: PoC as Internal Advocacy Vehicle for Claude at Belron
**Frequency:** 1 professional braindump (Anthropic/H&F)

**What emerged:**
The May 11 braindump is clear-eyed: H&F's relationship with Anthropic (JV investment) will not translate into Belron adopting Claude. The route is internal — build something undeniably good using Claude and let results make the case. The framing that works through governance: "Building Belron's AI platform on the safest, most enterprise-ready foundation model" — not "we prefer Anthropic."

Added to the AI Damage Assessment framework as Principle 6 — the PoC is the advocacy vehicle, and the framing and internal champion identification are the critical next steps.

**Status:** Working — requires active management of the prototype comparison (include Claude explicitly) and identification of the internal decision-maker

---

## Frameworks Updated

### EA Effectiveness Framework
**Location:** [[05-knowledge/consolidated/ea-effectiveness-framework]]

**What Changed:**
- **Principle 7 added:** EA as Experiment Design Owner — innovation accounting toolkit for Belron AI PoCs; Wizard of Oz MVP as standard first gate; pivot/persevere as governance artefact
- **Principle 8 added:** Belron Architecture Artefact Set (Lite ADM) — six templates from TOGAF; LeanIX boundary defined; Architecture Contract as highest-impact gap; IPO signal for architecture communication as investor-facing work

**New Evidence Added:**
- [[braindump-2026-05-06-0952-lean-startup-cycle]]
- [[braindump-2026-05-06-1627-togaf-adm-templates-belron-adaptation]]
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]]

---

### CCOTF Technology Architecture Framework
**Location:** [[05-knowledge/consolidated/ccotf-technology-architecture-framework]]

**What Changed:**
- **Principle 6 added:** Salesforce/Informatica convergence as a new CCaaS platform evaluation dimension — the Informatica asset as a swing factor in the Microsoft vs. Salesforce comparison
- **Principle 7 added:** Vendor EBC scepticism principle — treat EBC content as a hypothesis requiring reference customer validation; architecture representation should make vendor ownership and data proximity explicit

**New Evidence Added:**
- [[braindump-2026-05-14-1444-informatica-idmc-beyond-mdm]]
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]]

---

### AI Damage Assessment Strategy Framework
**Location:** [[05-knowledge/consolidated/ai-damage-assessment-strategy-framework]]

**What Changed:**
- **Principle 5 added:** Use Informatica DQ (CLAIRE) to validate training data before model training — specific profiling steps, EU AI Act compliance value, audit action to confirm licensing
- **Principle 6 added:** PoC as advocacy vehicle for Claude — internal framing, evidence-based approach, IPO angle, back-channel option with Anthropic enterprise services
- **Competitive landscape updated:** AutoBolt added — VIN/plate-based glass part identification SaaS; 99.8% accuracy; ADAS calibration data (89% of MY2023+ vehicles need calibration after windshield replacement); relevant to Belron's UK/EU operations if plate lookup is confirmed

**New Evidence Added:**
- [[braindump-2026-05-14-1444-informatica-idmc-beyond-mdm]]
- [[braindump-2026-05-11-1200-getting-belron-onto-anthropic]]
- [[braindump-2026-05-16-0037-autobolt-glass-part-identification]]

---

## New Frameworks Created

### Microsoft Single Tenant Strategy Framework
**Location:** [[05-knowledge/consolidated/microsoft-single-tenant-strategy-framework]]

**Created:** Based on 3 sources; primary: [[braindump-2026-05-14-0907-microsoft-single-tenant-strategy]]

**Core Principles:**
1. Pre-IPO is the right time to decide, not to execute
2. The AI case is now the primary driver (Copilot, MCP, AOAI)
3. Four architectural options: A (do nothing/decide), B (M365 first), C (Lighthouse), D (full consolidation)
4. Governance design precedes technical consolidation
5. M365 and Azure consolidation are separable programmes

**Status:** Emerging — requires validation of Belron's actual tenant state (number of Entra ID tenants is the pivotal unknown)

---

## Patterns Identified

### Platform Activation Gap
**Frequency:** Medium — confirmed across 3 platforms (Informatica, Microsoft, LeanIX)

**Description:** Large enterprise platforms are licensed at Group level but significantly underutilised. Features are available but not activated — creating a gap between what is owned and what is used. New requirements get solved with new vendor purchases, creating redundancy.

**Implications:** EA should run periodic platform audits and connect new requirements to existing platforms before recommending new tooling.

**Documentation:** [[05-knowledge/patterns/pattern-platform-activation-gap]]

---

## Cross-Cutting Insights

**Connections Across Domains:**
- The AI case links tenant strategy (Microsoft single tenant → unified identity for MCP) to CCOTF (Copilot agents across the group) to AI Damage Assessment (unified Azure estate for model governance)
- The Informatica platform spans CCOTF (Agentforce data layer), AI Damage Assessment (training data quality), and EU AI Act compliance (AI Governance Catalog) — a single vendor relationship touches all three active projects
- The Architecture Contract (EA Effectiveness Principle 8) is directly applicable to all three active projects as the missing governance artefact

**Strategic Implications:**
- Before any new tooling investment for EU AI Act compliance, AI training data quality, or CCaaS data integration — audit the Informatica IDMC subscription
- Before any new Microsoft platform investment — understand the current tenant state and what E5/M365 capabilities are already available
- The Obsidian Business OS braindump (processed 18 May, not re-consolidated here) provides the structural architecture for COG itself — the QUEUE/GENERATED pattern and three-layer model may be worth implementing as the knowledge management system scales

---

## Knowledge Base Maintenance

### Updates Made
- ✅ Updated framework: EA Effectiveness (Principles 7 + 8)
- ✅ Updated framework: CCOTF Technology Architecture (Principles 6 + 7)
- ✅ Updated framework: AI Damage Assessment Strategy (Principles 5 + 6 + AutoBolt)
- ✅ Created new framework: Microsoft Single Tenant Strategy
- ✅ Documented pattern: Platform Activation Gap
- ✅ Updated braindump statuses (see Archive Actions)

### Archive Actions
**Braindumps marked consolidated:**
- `braindump-2026-05-06-0952-lean-startup-cycle.md` → status: consolidated
- `braindump-2026-05-06-1627-togaf-adm-templates-belron-adaptation.md` → status: consolidated
- `braindump-2026-05-11-1200-getting-belron-onto-anthropic.md` → status: consolidated
- `braindump-2026-05-14-0907-microsoft-single-tenant-strategy.md` → status: consolidated
- `braindump-2026-05-14-1444-informatica-idmc-beyond-mdm.md` → status: consolidated
- `braindump-2026-05-16-0037-autobolt-glass-part-identification.md` → status: consolidated
- `braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc.md` → status: consolidated
- `braindump-2026-05-18-0821-obsidian-business-os-claude-mcp-n8n.md` → status: consolidated
- `braindump-2026-05-06-1006-beard-trimming.md` → status: consolidated (personal, low content)
- `braindump-2026-05-06-1913-concert-ticket-wall-art-framing.md` → status: consolidated (already in May 12 report)
- `braindump-2026-05-17-1524-do-expenses.md` → status: consolidated (personal admin task)
- `braindump-2026-05-05-1158-running-plan-build-up.md` → status: consolidated (already in May 12 report)
- `braindump-2026-05-06-1917-smash-burgers-tonight.md` → status: consolidated (already in May 12 report)
- `braindump-2026-05-06-1010-ultrawide-monitor.md` → status: consolidated (already in May 12 report)

---

## Future Consolidation Needs

### Ready for Framework Creation
- [ ] **Obsidian Business OS + COG architecture** — the QUEUE/GENERATED pattern and three-layer model from the 18 May braindump could evolve into a COG system design framework. Needs more evidence and practical application first — revisit in June.

### Monitoring Required
- [ ] **Platform Activation Gap** — watch for further instances as platform audits are conducted (Informatica, Microsoft E5, LeanIX)
- [ ] **Vendor EBC scepticism** — does the pattern hold across future EBC visits? Capture EBC visit outputs systematically in COG.

### Key Unknowns to Resolve
- How many Microsoft Entra ID tenants does Belron currently operate? (Changes entire tenant strategy recommendation)
- Does Belron use Salesforce CRM? (Changes CCOTF platform evaluation weighting significantly)
- What Informatica IDMC modules are currently licensed and active? (Determines EU AI Act and AI PoC data quality approach)

---

## Next Steps

**Immediate Actions:**
1. Audit Informatica IDMC licence — what modules are active vs. available 📅 2026-05-30
2. Confirm current Microsoft tenant count at Group level 📅 2026-05-30
3. Draft one-page options paper (Microsoft tenant Options A–D) for Group EA 📅 2026-06-15
4. Include Claude explicitly in AI Damage Assessment prototype model comparison

**Future Consolidation:**
- **Next Consolidation:** Suggested 2026-05-26 (end of week)
- **Focus Areas:** Microsoft tenant state (if confirmed), Informatica audit results, CCOTF platform evaluation progress

---

*Consolidation completed: 2026-05-19 | Processed 15 documents | Updated 3 frameworks, created 1 new framework, documented 1 pattern*
