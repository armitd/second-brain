---
type: "braindump"
domain: "professional"
date: "2026-05-06"
created: "2026-05-06 16:27"
themes: ["TOGAF", "ADM", "architecture-governance", "Belron", "EA-practice"]
tags: ["#braindump", "#TOGAF", "#ADM", "#enterprise-architecture", "#Belron", "#governance"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-19]]"
consolidated_date: "2026-05-19"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: TOGAF ADM Document Templates — Can We Adapt to Belron?

## Raw Thoughts
look at ADM document templates from TOGAF - can we adapt to Belron?

---

## Content Analysis

### Main Themes
1. **TOGAF ADM templates as a starting point, not a destination:** The ADM defines a structured set of deliverables per phase — the question is which are worth borrowing, which need stripping back, and which don't apply at all to a business like Belron.
2. **Belron's EA maturity vs. TOGAF's assumptions:** TOGAF ADM was designed for large-scale, project-by-project architecture engagements — Belron's EA practice is smaller, faster-moving, and supporting live product teams and OpCos. The templates need to serve that reality.
3. **What TOGAF templates actually cover:** The gap between what TOGAF specifies as deliverables and what Belron actually needs to govern architecture decisions, capture architecture intent, and create alignment with stakeholders.

### Supporting Ideas
- Previous braindump (May 5) already mapped TOGAF BA concepts to Belron — this is the next layer: do the ADM *output documents* translate?
- The vault book "TOGAF Is NOT an EA Framework" highlights that the ADM is a procurement/project-oriented cycle — not a description of how EA functions day-to-day; that tension matters here
- LeanIX is already in use at Belron — it replaces or pre-empts several TOGAF template functions (application inventory, technology radar, roadmap views)
- The 3 BAs in the EA team produce their own artefacts — any ADM template adaptation needs to avoid duplicating or conflicting with what they already produce

### Questions Raised
- Which ADM phases and deliverables map to what Belron actually does vs. what TOGAF describes?
- Where is LeanIX already filling a template-shaped hole — and where does it leave gaps that a document template should cover?
- Is there value in a Belron "lite ADM" — a simplified, opinionated subset of TOGAF templates adapted for Belron's scale and context?
- What does Belron's current architecture governance documentation actually look like, and where are the gaps?

### Decisions Contemplated
- Whether to adopt TOGAF templates wholesale, adapt selectively, or use them only as inspiration to design Belron-specific artefacts
- Whether to anchor any adapted templates to the existing BA artefacts and LeanIX data rather than creating parallel documentation

---

## Strategic Intelligence

### TOGAF ADM Templates — Assessment for Belron

The TOGAF ADM phases and their primary output documents:

| ADM Phase | Key Documents | Belron Applicability |
|---|---|---|
| Preliminary | Architecture Principles, Architecture Framework | **High** — Belron needs documented principles; framework definition is underway |
| A — Architecture Vision | Architecture Vision, Statement of Architecture Work, Stakeholder Map | **High** — Vision document is immediately useful per initiative; SOA needs simplification |
| B — Business Architecture | Business Architecture deliverables (capabilities, value streams) | **High** — But BA team already owns this; EA should consume, not duplicate |
| C — Information Systems | Data Architecture, Application Architecture deliverables | **Medium** — LeanIX covers Application; Data Architecture is an emerging gap |
| D — Technology Architecture | Technology Architecture deliverables | **Medium** — LeanIX Tech Radar covers a lot; detailed tech docs still valuable |
| E — Opportunities & Solutions | Architecture Roadmap, Transition Architecture | **Medium** — Roadmap exists in some form; Transition Architecture often over-engineered |
| F — Migration Planning | Migration Plan, Architecture Roadmap (updated) | **Low-Medium** — Project-level detail; rarely needed at EA level |
| G — Implementation Governance | Architecture Contract, Compliance Assessment | **High** — This is a gap at Belron; lightweight governance docs would add value |
| H — Change Management | Architecture Change Request, Impact Assessment | **Medium** — Worth having a lightweight process; current process unclear |
| Requirements Mgmt | Architecture Requirements Specification | **Low** — Usually covered by project-level BRDs or product backlogs |

### Key Insights

1. **Six templates are directly worth adapting for Belron** — Architecture Principles, Architecture Vision, Stakeholder Map, Architecture Roadmap, Architecture Contract (lightweight), and Compliance Assessment. These fill real gaps in Belron's current EA practice and don't duplicate existing tooling.

2. **LeanIX already replaces three TOGAF template functions** — Application Portfolio (replaces Application Architecture deliverables), Technology Radar (replaces Technology Architecture inventory), and Roadmap views (partially replaces ADM Architecture Roadmap). Any Belron template set must treat LeanIX as the system of record for these, not a document.

3. **The Architecture Contract concept is the biggest gap** — TOGAF's Architecture Contract defines what is being committed to architecturally and governs how a solution is built against the architecture. Belron likely has no equivalent, meaning architecture decisions are made without a governance artefact. A lightweight Belron Architecture Contract (1-2 pages per initiative) would be immediately valuable, particularly for the three active projects.

4. **The ADM cycle doesn't match Belron's delivery rhythm** — TOGAF assumes you run a full ADM cycle per architectural engagement. Belron's reality is continuous architecture support for product teams and OpCos across multiple simultaneous initiatives. The templates should be treated as project-level documents triggered by initiative milestones, not as a sequential cycle.

5. **The Statement of Architecture Work needs radical simplification** — in TOGAF, this is a formal contract-like document. For Belron, an "Architecture Brief" (half a page: what we're trying to achieve, what's in/out of scope architecturally, who the stakeholders are, what we'll produce) would serve the same purpose without the overhead.

### Pattern Recognition
- **Connection to previous braindump (May 5):** The BA application braindump mapped TOGAF BA *concepts* to Belron — this braindump is the logical next step: what do the *output documents* look like in practice for Belron?
- **Connection to LeanIX:** The LeanIX braindump (April 9) noted that LeanIX features were underused. A Belron ADM template set would define what *doesn't* go in LeanIX — the narrative, decision, and governance layer that sits above the data.
- **Connection to architecture governance:** The passive-to-active stakeholder visibility braindump (April 8) identified a need to make EA more visible. Architecture Vision and Architecture Contract documents are the mechanism for doing that — they create a paper trail of architectural intent that stakeholders can see and challenge.

### The "TOGAF Is NOT an EA Framework" Perspective
The book in the vault argues that TOGAF ADM is a procurement/project methodology, not a description of how EA actually functions. That's directly relevant here: the templates were designed to produce documents for a formal architecture engagement, not to run a living EA practice. The adaptation task is therefore:
- Take the *concept* behind each template (what it's trying to capture)
- Design a Belron version that fits the EA team's actual workflow
- Anchor to LeanIX for data, use documents only for narrative, decisions, and governance

### Strategic Implications
- A "Belron Architecture Artefact Set" — a lightweight, opinionated subset of TOGAF templates adapted for Belron — would give the EA team a consistent language and document set to work from
- The three active projects (AI Damage Assessment PoC, CCOTF, MCP Governance) are the ideal test cases for piloting adapted templates — real initiatives, real stakeholders, real governance needs
- Starting with Architecture Principles and Architecture Vision (the lightest and most universally useful) before tackling Architecture Contract (the most impactful but most effort) is the pragmatic sequence

---

## Proposed Belron Architecture Artefact Set (Lite ADM)

### Tier 1 — Adapt Now (High Value, Relatively Low Effort)
1. **Architecture Principles** — 1 page per principle; covers rationality, implications, what it rules out. Belron probably has some implicit principles — make them explicit.
2. **Architecture Vision** — 2-3 pages per initiative; what problem, what future state, what's in/out of scope, key risks. Used to align stakeholders before architecture work begins.
3. **Stakeholder Map** — 1 page; who cares, what they care about, what they need to see. Derived from TOGAF but already familiar.

### Tier 2 — Adapt Medium-Term (High Value, More Effort)
4. **Architecture Brief** (simplified Statement of Architecture Work) — half a page; what we're committing to investigate and produce, by when, approved by whom.
5. **Architecture Contract** — 1-2 pages; what architecture commitments the project team is making, who signs off, what happens if they want to deviate. This is the governance mechanism.
6. **Compliance Assessment** — lightweight checklist tied to Architecture Principles; run at project gate reviews.

### Tier 3 — Reference Only (Use as Inspiration)
7. **Architecture Roadmap** — LeanIX covers most of this; supplement with a narrative layer if needed.
8. **Architecture Change Request** — simple form for when a project wants to deviate from agreed architecture.

---

## Action Items

### Immediate (This Week)
- [ ] Pull the actual TOGAF ADM template list from The Open Group documentation — get the official template names and structures 📅 2026-05-09
- [ ] Check what architecture documents already exist at Belron — ask the BA lead or EA team lead what templates, if any, are currently in use 📅 2026-05-09

### Short-term (2 Weeks)
- [ ] Draft a Belron Architecture Principles document — even 5-6 principles to start; test against the three active projects 📅 2026-05-20
- [ ] Draft a lightweight Architecture Vision template and pilot it on one of the three active projects (CCOTF is the best candidate — largest scope, most stakeholders) 📅 2026-05-20
- [ ] Map what LeanIX already covers vs. what document templates would need to fill — avoid duplication 📅 2026-05-16

### Strategic Considerations
- The adaptation exercise could itself be an EA team artefact — a "Belron EA Playbook" that defines what documents we produce, when, and what they look like. That would create consistency across the team and make EA work visible to the organisation.
- The Architecture Contract is the highest-impact template if governance is the gap — but it requires buy-in from delivery teams and leadership. Start with Vision and Principles to build familiarity with EA artefacts before introducing a governance contract.

---

## Connections
- **Related Braindumps:** [[braindump-2026-05-05-1549-togaf-ba-application]] (TOGAF BA application to Belron — the concepts layer; this is the documents layer), [[braindump-2026-04-09-1022-leanix-learning-use-cases]] (LeanIX covers some template functions), [[braindump-2026-04-08-0937-passive-to-active-stakeholder-visibility]] (EA visibility — Architecture Vision is the mechanism)
- **Relevant Projects:** [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW|AI Damage Assessment PoC]], [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]]
- **Readwise:** [[TOGAF Is NOT an EA Framework]] — relevant perspective on ADM as procurement methodology vs. living EA practice

## Domain Classification
- **Primary Domain:** Professional (98%)
- **Reasoning:** Pure EA practice question, directly connected to the Belron role and three active projects
- **Cross-Domain Elements:** None
- **Privacy Level:** confidential

## Processing Notes

### Emotional Context
- **Energy Level:** Medium — exploratory, analytical; not urgent but practically motivated
- **Emotional Tone:** Curious — framed as a genuine question ("can we?") rather than a commitment

### Confidence Assessment
- **Overall Analysis:** 88% — solid grounding in TOGAF ADM structure and Belron context from prior braindumps; specific Belron document gaps inferred rather than confirmed from internal knowledge
- **Domain Classification:** 98% — unambiguously professional EA practice
- **Strategic Insights:** 85% — the LeanIX overlap and Architecture Contract gap are inferred; actual current state of Belron documentation unknown
- **Areas Requiring Clarification:** What EA governance documents already exist at Belron; what LeanIX modules are currently active and in use

---

*Processed by COG Brain Dump Analyst*
