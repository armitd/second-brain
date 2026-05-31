---
type: "consolidated-knowledge"
domain: "professional"
framework: "ea-effectiveness"
created: "2026-04-09"
last_updated: "2026-05-24"
consolidation_id: "consolidation-2026-05-24"
source_documents: 34
status: "working"
tags: ["#framework", "#consolidated", "#enterprise-architecture", "#visibility", "#effectiveness", "#transition"]
---

# EA Effectiveness Framework

## Framework Overview
A working model for how an Enterprise Architect builds and sustains genuine influence — combining stakeholder visibility, business proximity, artefact design, and disciplined routines into a self-reinforcing system.

**Status:** Working (strong evidence base from first week; needs validation over 4–6 weeks of application)
**Last Updated:** 2026-04-09
**Source Insights:** 7 documents — braindumps on stakeholder visibility, architecture guide, BCM, Belron business understanding, software delivery model, EA Copilot agent, weekly check-in

---

## The Core Problem

Enterprise architects are structurally at risk of invisibility. The discipline sits between business and technology — owning neither domain fully, producing work that is abstract, and being consulted reactively rather than proactively. In this role, capability alone is not enough. **Perceived value = actual value.** An EA's impact is limited not by their knowledge but by how well that knowledge is known and trusted by the people who make decisions.

---

## Core Principles

### Principle 1: Visibility Requires a System, Not Resolve

**Statement:** Proactive stakeholder presence cannot be sustained by willpower. It requires a calendar-anchored routine that creates touchpoints before they feel necessary.

**Evidence:**
- [[braindump-2026-04-08-0937-passive-to-active-stakeholder-visibility]] — "A passive default won't be fixed by deciding to be more active — it requires a calendar-anchored system"
- [[weekly-checkin-2026-04-08]] — "Tired + meetings = passive default. Energy and environment are the root cause, not character"
- [[braindump-2026-04-07-1550-architecture-guide-update]] — "Pair the guide launch with a short communication — not just silently publishing it"

**The system (draft):**

| Cadence | Action | Time |
|---|---|---|
| Weekly (Monday) | Stakeholder radar — who haven't I spoken to? Where are decisions forming? | 15 min |
| Weekly (Friday) | Brief wins summary — 2–3 bullets sent to one stakeholder | 10 min |
| Fortnightly | Informal stakeholder coffee — one person from rotation, no agenda | 20 min |
| Monthly | EA impact narrative — one paragraph for manager/sponsor | 20 min |

**Confidence:** High — this is a well-established pattern in EA effectiveness literature and confirmed by personal diagnosis

---

### Principle 2: EA Artefacts Are Dual-Purpose — Thinking Tool AND Visibility Instrument

**Statement:** Every EA artefact produced should serve two functions simultaneously: it solves a thinking problem AND it creates a reason for stakeholder engagement. Design artefacts with both audiences in mind.

**Evidence:**
- [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — "A Wardley Map of Belron's capabilities would be a high-impact EA artefact. No one has probably done this. A map showing where Belron's capabilities sit on the evolution axis — and where they should sit — is the kind of thing that gets you in front of leadership"
- [[braindump-2026-04-08-1436-belron-software-development-model]] — "The model is a forcing function for the Belron business understanding goal... Every conversation needed to fill a gap is a stakeholder engagement"
- [[braindump-2026-04-07-1520-business-capability-modelling]] — "Start with the map, not the theory. Showing people a draft capability map of their own company creates immediate engagement"
- [[braindump-2026-04-09-0934-ea-copilot-agent]] — The Copilot agent is both a process tool AND an institutional knowledge artefact

**How to apply:** Before starting any EA artefact, ask:
1. What thinking problem does this solve?
2. Who would find this valuable to see — and why would it open a conversation?
3. What format makes it most shareable with non-EA stakeholders?

**Confidence:** High — pattern appears across all substantive braindumps this week

---

### Principle 3: Business Proximity and Stakeholder Proximity Are the Same Investment

**Statement:** Getting closer to the business *is* stakeholder management. The operational stakeholders who understand how the business works are exactly the people who most need to trust the EA function — and who EA most needs to understand.

**Evidence:**
- [[braindump-2026-04-08-1123-getting-closer-to-belron-business]] — "When you do the fortnightly stakeholder coffee rotation, weight it toward operational stakeholders first — they hold the knowledge you need"
- [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — Porter value chain analysis *is* a structured way to understand how the business works
- [[braindump-2026-04-08-1436-belron-software-development-model]] — "Every conversation needed to fill a gap in this model is a stakeholder engagement"
- [[daily-brief-2026-04-07]] — EA in 2026 is shifting from documentation to "governing autonomy, shaping decisions at scale" — which requires influence over decision-makers, which requires relationships

**How to apply:** When choosing which stakeholders to invest in, weight toward those closest to operational reality — contact centre, field ops, delivery managers — before those closest to the EA's natural technical comfort zone.

**Confidence:** High

---

### Principle 4: Lead with Business Language, Not Framework Language

**Statement:** All EA communication materials — guides, briefings, capability maps, Wardley maps — must be expressed in the business's own language. Framework vocabulary (TOGAF, ArchiMate, capability, evolution axis) is for EA practitioners; everyone else needs outcomes, scenarios, and consequences.

**Evidence:**
- [[braindump-2026-04-07-1520-business-capability-modelling]] — "Don't lead with 'enterprise architecture' or 'TOGAF.' Lead with business outcomes: 'a clearer picture of what we do, where we invest, and where there are gaps'"
- [[braindump-2026-04-07-1550-architecture-guide-update]] — "Areas I cover should be expressed in business language: 'systems and integrations,' 'data and reporting' — not 'application architecture, data architecture'"
- [[braindump-2026-04-07-1550-architecture-guide-update]] — "An architecture guide is a marketing document as much as a reference document. Scenarios beat abstractions: 'Starting a new system purchase? Talk to architecture first.'"

**Confidence:** High — consistent across all communication-focused braindumps

---

### Principle 5: EA in the Agentic Era — From Process Governance to Architectural Intent

**Statement:** As AI agents absorb the coordination layer of organisations (planning, dependency management, status tracking), EA functions whose value is framed around *process* become structurally redundant. EA's durable value proposition is *architectural intent* — defining goals clearly enough that autonomous systems can execute them well. This is the repositioning the current transition requires.

**The Byttow argument:**
David Byttow's essay "AI Absorbed the Process Layer" makes the mechanism explicit:
- Coordination overhead (sprint planning, handoff docs, alignment meetings) was always a cost, never a value — agents now bear that cost
- What remains after coordination is automated is *judgment*: goal clarity, taste, direction, ownership
- **"AI will not replace managers. It will expose the ones whose contribution was procedural rather than directional."**
- **"AI makes the gap visible"** — if you cannot articulate a goal clearly enough for an AI agent to act on it, you could not articulate it clearly enough for your team either. AI just removes the friction that previously masked the gap

**The EA repositioning:**
- From: governance as friction (review gates, standards compliance, process ownership)
- To: governance as intent-setting (defining what goals agents are authorised to pursue, with what tools, under what constraints)

This is a stronger position. As agents accelerate execution, the cost of building in the wrong direction increases. EA's role shifts from *slowing down bad decisions* to *improving the quality of goals before execution starts*.

**Evidence:**
- [[braindump-2026-04-27-0955-ai-absorbed-process-layer]] — Byttow: coordination collapse, judgment as leverage, "fast delivery of the wrong thing is worse than slow delivery"
- [[braindump-2026-04-27-0955-shopify-tobi-ai-memo]] — Tobi Lutke's Shopify memo: before asking for headcount or a new process, demonstrate why an AI-first alternative wouldn't work. EA should apply this standard to its own governance proposals
- [[daily-brief-2026-04-30]] — Amazon Connect Customer: AWS reframed agentic contact centre from "deflection" to "relationship." The goal definition is the new value — not the process wrapper around execution

**The internal framing to use:**
> *"EA's value in an agentic world is not governance of AI processes — it is architectural clarity that makes AI agent deployment safe and directional. Agents amplify whatever judgment sits at the centre. EA's job is to improve the quality of that judgment before deployment begins."*

**Confidence:** High — converging evidence from Byttow, Shopify memo, and Agarwal braindumps; framing tested across multiple sources independently

---

### Principle 6: BA-EA Fluency Multiplies the Impact of Both Functions

**Statement:** An Enterprise Architect who understands business architecture well enough to be a high-quality partner — reading a capability model critically, connecting a value stream analysis to architecture constraints, bringing an AI/technology lens into BA conversations early — is more valuable than either a pure BA or a pure EA working separately. The EA-BA handoff is where value most commonly leaks; closing it from the EA side is higher leverage than adding more EA tools.

**The key insight:** The goal is not to do BA — it is to work more effectively with BAs. TOGAF BA training gives an EA the vocabulary to engage meaningfully with existing BA artefacts: to spot what's missing, to connect a capability gap to an architecture decision, to ask "how does this capability change with AI augmentation?" These are questions only an EA with BA fluency can ask.

**All three active projects are BA in disguise:**
- **AI Damage Assessment PoC** = the "Vehicle Assessment" capability (currently human-performed) being transformed by AI. BA frames this as a capability transformation with technology as the enabler — connecting it to a board-level strategic objective rather than a technology experiment
- **Contact Centre of the Future** = the "Customer Engagement" value stream being redesigned. BA provides the value stream map to show what is being automated, augmented, or eliminated — making the investment case concrete for non-technical stakeholders
- **MCP Governance** = the "IT Governance" capability area. BA connects it to business policies, compliance requirements, and enterprise risk appetite — elevating it from a technology standards exercise to a business governance programme

**The collaboration model:** Producing a Belron capability model from scratch is less valuable than engaging with the BA team's existing artefacts and contributing an EA/technology perspective to them. The first action is to get access to what's already there, not to start over.

**Evidence:**
- [[braindump-2026-05-05-1549-togaf-ba-application]] — "The course gives you enough BA knowledge to be a high-quality consumer and partner of BA work: you can read a capability model critically, spot where a value stream analysis is missing something relevant to architecture"
- [[braindump-2026-05-05-1549-togaf-ba-application]] — "The EA-BA handoff is where value leaks... Understanding BA is how an EA closes that gap from their side"
- [[braindump-2026-05-05-1549-togaf-ba-application]] — Belron capability model inferred: Customer Acquisition → Appointment Management → Vehicle Assessment → Glass Repair/Replace → ADAS Calibration → Claims Management
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — CCOTF technology model is the technology layer that sits beneath the capability model — the missing artefact is the explicit capability-to-technology mapping

**LeanIX connection:** LeanIX has Business Architecture features (value streams, capability maps) that are likely underused. BA training knowledge maps directly to LeanIX practice — creating a two-for-one: BA fluency improves the EA-BA partnership AND improves LeanIX utilisation.

**How to apply:**
- Access the existing BA artefacts first (capability model, value stream maps) — ask the 3 BAs in the EA team what they have
- For each active project: frame it explicitly as a capability transformation story, not just a technology project
- In BA joint-working sessions: ask the question "how does this capability change with AI augmentation?" — this is the uniquely EA/technology perspective BA colleagues cannot easily provide themselves

**Confidence:** High — principle is structurally sound and grounded in a specific braindump; application to all three projects is well-evidenced

---

### Principle 7: EA as Experiment Design Owner — Innovation Accounting as Governance

**Statement:** In an organisation running AI PoCs, the EA team's highest-leverage governance contribution is not reviewing the architecture *after* a PoC has been built — it is defining *what counts as evidence* before the first sprint begins. Innovation accounting (a lean startup discipline) gives EA a structured tool for this: define the hypothesis, the leading indicator metrics, and the pivot threshold before any code is written.

**Why this matters for Belron's AI portfolio:**
In 2026, AI PoCs are proliferating faster than traditional governance can review them. The question "when does this generate value?" is no longer answered by a delivery date — it is answered by a learning milestone. EA's role is to force this definition early, creating a governance moment that is forward-looking rather than backward-looking.

**The innovation accounting toolkit:**
| Tool | EA Action |
|---|---|
| **Hypothesis definition** | Before PoC kick-off: "We believe [capability X] will [outcome Y] for [customer Z]. We will know this is true when [leading indicator]." |
| **Leading indicators** | Define the measurable outcomes that confirm value *before* revenue arrives — accuracy rate, decision quality, time-to-decision, technician confidence score |
| **Experiment design** | Recommend Wizard of Oz or Concierge MVP phases before committing to model infrastructure — test whether the *decision* is valuable when a human makes it |
| **Pivot threshold** | Pre-define the evidence level that would trigger a direction change — removes politics from the decision at the stage gate |
| **Innovation accounting review** | Monthly or per-sprint: are we learning at the rate we predicted? Are our leading indicators moving? |

**Wizard of Oz principle:** Before committing to model training, data pipelines, or MLOps infrastructure, run a human-in-the-loop pilot — a person does what the AI will eventually do. If the decision isn't valuable when a human makes it, the AI version won't be either. This is underused in enterprise AI and should be a standard first gate for any Belron AI PoC.

**The lean startup critique to hold in tension:** Lean startup optimises for *incremental* validation. For breakthrough bets (AI Damage Assessment at full deployment scale), the vision must come first — experiments validate the *path* to the vision, not the vision itself. Don't let fast feedback loops kill long-horizon bets.

**Evidence:**
- [[braindump-2026-05-06-0952-lean-startup-cycle]] — Innovation accounting as the answer to "when does this generate value?"; Wizard of Oz MVPs underused in enterprise AI; EA as experiment design owner
- [[braindump-2026-05-06-0952-lean-startup-cycle]] — "Pivot/persevere as an EA governance artefact — if EA owns the framework for defining validated learning before the PoC begins, EA is structuring the governance moment"
- [[braindump-2026-05-06-1627-togaf-adm-templates-belron-adaptation]] — BA capability maps serve as the hypothesis-definition layer for lean startup experiments

**Confidence:** High — well-sourced; the Wizard of Oz + innovation accounting application to Belron's active AI projects is directly applicable and not dependent on Belron-specific unknowns

---

### Principle 8: A Belron Architecture Artefact Set — Lite ADM, Not Full TOGAF

**Statement:** TOGAF's ADM templates were designed for formal, project-by-project architecture engagements. Belron's EA practice is smaller, faster-moving, and operating across multiple simultaneous initiatives. The right response is a curated "Belron Architecture Artefact Set" — six templates adapted from TOGAF's strongest concepts, anchored to LeanIX for data, used for narrative and governance only.

**The six artefacts worth adapting (not all at once — sequence matters):**

*Tier 1 — Adapt Now:*
1. **Architecture Principles** — 1 page per principle; covers rationale, implications, what it rules out. Belron likely has implicit principles — make them explicit and govern against them
2. **Architecture Vision** — 2–3 pages per initiative; what problem, what future state, what's in/out of scope, key risks. Aligns stakeholders before architecture work begins
3. **Stakeholder Map** — 1 page; who cares, what they care about, what they need to see

*Tier 2 — Adapt Medium-Term:*
4. **Architecture Brief** (simplified Statement of Architecture Work) — half a page; what we're committing to investigate and produce, by when, approved by whom
5. **Architecture Contract** — 1–2 pages; what architecture commitments the project team is making, who signs off, what happens if they want to deviate. **This is the biggest governance gap at Belron.**
6. **Compliance Assessment** — lightweight checklist tied to Architecture Principles; run at project gate reviews

**LeanIX boundary:** LeanIX already covers Application Portfolio (replacing Application Architecture deliverables), Technology Radar (replacing Technology Architecture inventory), and roadmap views. Any Belron template set must treat LeanIX as the system of record for data — documents are for narrative, decisions, and governance only.

**The Architecture Contract is the highest-impact gap.** Belron currently makes architecture decisions without a governance artefact that defines what commitments a project team is making. A lightweight Architecture Contract (1–2 pages) per initiative would be immediately valuable for all three active projects — and becomes an IPO-adjacent artefact as investor-grade technology governance documentation.

**IPO signal:** The ability to demonstrate coherent, documented technology architecture standards is investor-facing work as Belron approaches an H2 2026 IPO. Architecture communication is a pre-IPO deliverable, not just an internal discipline.

**Evidence:**
- [[braindump-2026-05-06-1627-togaf-adm-templates-belron-adaptation]] — Full ADM template assessment for Belron; Lite ADM proposal; LeanIX overlap mapping; Architecture Contract as biggest gap
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]] — "Showing tech standards to markets is IPO-adjacent"; architecture communication as investor-facing work
- [[braindump-2026-05-05-1549-togaf-ba-application]] — BA artefacts as the evidence base that Architecture Vision documents summarise

---

### Principle 9: Working Backwards / PRFAQ — Start From the Press Release

**Statement:** Before scoping or architecting any new initiative, write the press release first. Amazon's Working Backwards method forces clarity on the customer, the problem, and the outcome before any solution work begins. For an EA function, this is the highest-leverage tool for initiative framing, stakeholder alignment, and investment case quality.

**The method:**
1. **Press Release** — Write the announcement of the finished product or capability, as if the launch day has arrived. Audience: the customer. Forces: clarity on outcome, not solution.
2. **FAQ (internal)** — What would the team ask before building? What are the hardest questions? Surfaces assumptions before they become architectural decisions.
3. **FAQ (external)** — What would a sceptic, executive, or investor ask? Stress-tests the case.
4. **Visuals/UX** — What does it look like in use? Often reveals gaps the text doesn't.
5. **Build** — Only now.

**For EA specifically:**
- The PRFAQ replaces the Architecture Vision brief as the shareable, non-technical stakeholder artefact. It is more compelling than a capability map and requires no framework literacy to read.
- Amazon's insight: *"If you can't write the press release, you don't understand the customer well enough to build for them."* EA equivalent: if you can't write the press release, you haven't understood the business problem well enough to govern the architecture.
- **"Bounded independence"** (AWS Kiro): the right framing for how EA delegates work to agentic AI tools — set the spec and boundary, let the agent execute within it. PRFAQ is the spec-definition layer.

**Direct applications:**
- **AI Damage Assessment PoC:** Write the PRFAQ *now* — "Belron customer photographs windscreen damage and receives instant repair/replace recommendation." Writing this before the next stakeholder conversation will expose assumptions and sharpen the pitch.
- **Contact Centre of the Future:** The PRFAQ for "Belron customer contacts us and their issue is resolved on first contact by an AI agent, with escalation to a human only when needed" is the vision artefact the programme needs.
- **MCP Governance:** "Belron's AI systems interoperate safely without shadow integrations or data leakage, governed by a clear access control framework" — the PRFAQ for this initiative would be the most compelling way to bring governance to non-technical leadership.

**The Working Backwards method is tool-independent:** Adopt it as an EA method regardless of whether Belron adopts AWS Kiro. It costs nothing to lift and use immediately.

**Evidence:**
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — "The Working Backwards / PRFAQ method is the most valuable takeaway regardless of Kiro itself — it's a method, not a tool, and it's lift-and-use into EA practice immediately"
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — "Writing the press release first for 'Belron customer gets damage assessed in 30 seconds via app' forces clarity on customer experience before solutioning"
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — "Spec-driven development" / "bounded independence" as the collaboration model between developer and agent

**Confidence:** High — method is well-established (Amazon internal practice for 20+ years); direct applicability to EA practice is confirmed by workshop observation; Belron-specific applications are immediate

**Sequencing:** Start with Architecture Principles and Architecture Vision (lightest, most universally useful) before tackling Architecture Contract (most impactful but requires buy-in from delivery teams). Run the pilot on CCOTF — largest scope, most stakeholders.

**Confidence:** High — TOGAF ADM structure is well-established; Belron-specific applicability is inferred from project context but solidly grounded

---

## Applications & Use Cases

### Use Case 1: Establishing EA Presence in a New Role
**When to apply:** Joining a new organisation or function where EA is not well understood
**How to apply:**
1. Build the stakeholder radar (list + last contact date) in week 1
2. Draft the architecture guide (scope + engagement model) as the "front door"
3. Identify one visible artefact that solves a real business problem (capability map, customer journey map)
4. Set up the weekly/fortnightly routine before it feels needed

**Expected outcomes:** After 90 days — stakeholders know what EA is and when to engage; EA is in the conversation on at least one active decision

### Use Case 2: Recovering from Passive Mode
**When to apply:** Self-diagnosis of reactive behaviour — waiting for problems rather than seeking them
**How to apply:**
1. Diagnose the root cause: tiredness? Calendar fragmentation? Unclear mandate?
2. If calendar: protect one 90-minute morning block per day for EA work
3. Start with one action: book the first stakeholder coffee (this week, not "next week")
4. Use a visible artefact as the conversation opener — never go to a stakeholder empty-handed

**Expected outcomes:** Within 2–3 weeks — at least one proactive stakeholder connection made; at least one decision influenced before it was finalised

### Use Case 3: Turning a Learning Exercise into Visibility
**When to apply:** Any time you're building knowledge about the business (reading, researching, mapping)
**How to apply:**
1. Create a shareable output from the learning (one-page, diagram, briefing note)
2. Share it with a stakeholder and ask for their reaction: "Does this match your understanding?"
3. The conversation that follows is the visibility moment — the document is the opener

### Use Case 4: Owning Emerging Technology Governance
**When to apply:** When a new technology wave is forming (currently: agentic AI / MCP / A2A) and business units will start building without governance
**How to apply:**
1. Research the technology deeply — build genuine expertise, not summary knowledge
2. Create a briefing that explains it in business language: "What this means for Belron"
3. Use an external trigger (milestone, industry announcement) as the hook to go to leadership: "Here's what just happened. Here's what we need to decide."
4. Propose a formal governance mechanism (e.g. Agentic AI Architecture Review) — this creates ongoing EA ownership, not a one-time briefing

**Why this works:** Emerging technology governance is inherently EA territory — capability, integration, risk, and governance all in one. Most business units welcome governance on unfamiliar territory. Arriving early with clarity is more influential than arriving late with rules.

**Evidence:** [[braindump-2026-04-09-1322-emerging-technology-topic]] — the three-part deliverable (paper, presentation, briefing) is exactly this playbook. [[daily-brief-2026-04-10]] — A2A 1-year milestone is the external trigger for the MCP/A2A briefing.

### Use Case 6: Shaping a Leadership Transition
**When to apply:** When a leadership vacuum opens — a manager leaves, a function restructures, a new remit is forming
**How to apply:**
1. Recognise the shift: watching a transition is fundamentally different from shaping it. Move from observer to contributor by having a point of view, not just observations
2. Be visible where decisions are forming — existing meetings, office presence, the spaces where transition conversations happen informally
3. Have a deliverable in flight that demonstrates strategic intent: an exam booked, a document in progress, a briefing prepared. These signal "this person is positioning themselves" to the people watching
4. The question to answer privately: if you were designing the EA team's remit from scratch, what would you want it to be? Having a clear internal answer prepares you for the moment you're asked
5. Make one contribution in the relevant meetings that signals intent rather than presence — not just "I was there" but "I had a point of view"

**Why timing matters:** Leadership vacuums create a brief window during which the future structure is genuinely uncertain. Visibility and clear positioning during this window carries disproportionate weight. Miss the window and the structure solidifies without you.

**Evidence:** [[weekly-checkin-2026-04-20]] — "currently watching, need to move to shaping." Head of EA retiring + departmental change in motion = transition moment live. Nordics delivery, Steve Paisley collaboration, CIO-level document are exactly the visible outputs that build the case for someone who should be shaping the transition.

**Confidence:** Medium-High — principle is well-established in career development literature; personal application is emerging

---

### Use Case 5: Connecting Artefact Work to Budget Cycles
**When to apply:** When a budget cycle is approaching and EA work needs to be funded
**How to apply:**
1. Identify the budget deadline and work backwards — roadmaps must be ready 4–6 weeks before budget submission
2. Frame roadmap initiatives in capability language, not technology language ("enable AI-assisted damage assessment" not "implement a machine vision API")
3. Use the capability map as the spine — initiatives that can't be connected to a capability don't get funded
4. Present the roadmap to a sponsor before budget review begins — use it as a proactive stakeholder touchpoint, not just a document to submit

**Hard deadline:** Belron budgeting starts July 2026. Roadmaps needed by mid-June. That's the forcing function for completing Phase 1 of the Belron Business Understanding Framework by end of April.

**Evidence:** [[braindump-2026-04-09-1418-budgeting-roadmaps]]

---

## Boundaries & Limitations

**This framework works when:**
- The EA practitioner has genuine domain knowledge to offer
- There is organisational appetite for EA involvement (even if not yet activated)
- Stakeholder relationships can be built informally (not in highly political or siloed environments)

**This framework does NOT work when:**
- EA has no mandate or sponsorship from leadership
- The organisation actively resists architecture governance
- All available time is consumed by delivery/project work with no space for EA practice

**Common Pitfalls:**
- Over-investing in artefacts at the expense of conversations — a perfect diagram that no one has seen is worthless
- Treating the stakeholder routine as optional when energy is low — this is exactly when it matters most
- Using framework language in materials intended for a business audience
- Assuming structural clarity is a prerequisite for EA contribution — the April 13 check-in confirmed that personal reputation builds independently of team remit ambiguity. Don't wait for the structure to be resolved; keep building relationships and producing artefacts while the structural conversation is initiated in parallel.
- Trusting the internal read over the external evidence — three consecutive check-ins have now confirmed that the internal critic runs hotter than the evidence warrants. The Nordics work landed well despite anticipated resistance. Personal reputation was strong despite structural uncertainty. The external read is consistently better than the internal one. Treat this as a known calibration error and adjust accordingly.

---

## Evolution & History

### April 6–9, 2026: Initial Development
**What Emerged:** The EA visibility problem crystallised as structural (role design) rather than personal (character). The dual-purpose artefact principle emerged from noticing that the most impactful EA work was always framed as both a thinking tool and a stakeholder opportunity.

**Catalysts:**
- [[braindump-2026-04-08-0937-passive-to-active-stakeholder-visibility]] — explicit self-diagnosis
- [[weekly-checkin-2026-04-08]] — honest assessment of a fragmented, depleted week
- [[braindump-2026-04-08-1436-belron-software-development-model]] — recognition that the artefact building process IS the stakeholder engagement

### April 10, 2026: Second Consolidation — Two New Use Cases Added
**What Emerged:** Two new use cases from the week's subsequent work: owning emerging technology governance (MCP/A2A as the concrete instance) and connecting artefact work to budget cycles (July 2026 budgeting deadline as the forcing function).

**New evidence:**
- [[braindump-2026-04-09-1322-emerging-technology-topic]] — the three-part deliverable set (paper, presentation, briefing) as the EA's playbook for emerging tech ownership
- [[braindump-2026-04-09-1418-budgeting-roadmaps]] — budgeting starts July 2026; roadmaps needed by mid-June; capability map is the spine

**Status at April 10, 2026:** Working. Framework is holding up across a second week of application. Budget deadline creates concrete pressure to complete the Belron Business Understanding Framework Phase 1 by end of April.

### April 20–30, 2026: Fifth Consolidation — Agentic Repositioning

**What Emerged:** The period produced a cluster of three professionally-interconnected braindumps (Byttow, Shopify memo, Agarwal) that together define a new strategic layer for EA in the agentic era. This is not an additive update — it shifts the framework's underlying premise.

**The structural argument now complete:**
- Byttow describes *what is happening organisationally*: coordination is being absorbed by agents, judgment becomes the scarce resource
- Shopify describes *what the best companies are requiring*: AI as baseline expectation, "hire an AI before a human," measurement built in
- Agarwal describes *what happens at the individual level*: craft abundance, builder's disposition as the new signal, constraints dissolving for those with clarity

Together they define the repositioning EA must make: from process governance to architectural intent. Principle 5 added.

**Sources:** [[braindump-2026-04-27-0955-ai-absorbed-process-layer]], [[braindump-2026-04-27-0955-shopify-tobi-ai-memo]], [[braindump-2026-04-27-0955-life-work-becomes-free-agarwal]]

**Status at April 30, 2026:** Working. Five principles; six use cases. Principle 5 is the most important addition since the initial framework and significantly changes how EA effectiveness is framed.

---

### April 20, 2026: Fourth Consolidation — Transition Moment Live

**What Emerged:** The week of April 14–20 produced a significant shift in the professional context and three new framework-relevant observations:

**1. The transition moment is live — watching must become shaping.**
The Head of EA is retiring. Departmental change is in motion. The team remit ambiguity that was an unresolved structural question is now likely to get resolved *through* the transition rather than as a standalone conversation. This context shifts the framework's focus from "building presence while the structure is unclear" to "actively positioning during a live restructure." Use Case 6 (Shaping a Leadership Transition) added in response.

**2. Collaboration as a visible amplifier — the Steve Paisley model.**
The Nordics delivery this week was collaborative (Steve Paisley partnership), not solo. The outcome — a document taken to the global CIO — is a higher-visibility output than solo EA work would have produced. Pattern: the best EA outputs this period have consistently come from partnerships, not individual effort. The collaboration *is* the visibility mechanism. Find the next opportunity to activate a similar partnership rather than defaulting to solo work.

**3. External reception consistently better than internal expectation — now a confirmed pattern (third data point).**
- April 8: Personal reputation building despite a fragmented, depleted week
- April 13: Personal reputation landing well despite structural ambiguity  
- April 20: Nordics work landing well with global CIO despite internal resistance anticipated

This is no longer an observation — it is a calibration pattern. The internal critic consistently underestimates external reception. Treat it as a known systematic error and give the external read more weight in decisions about whether to proceed or hold back.

**4. TOGAF exam as a professional intent signal — timing matters.**
Booking the TOGAF exam during a live transition moment is not just about certification. It is a signal of professional intent at exactly the moment a leadership vacuum is opening. The *timing* of visible professional investment (exams, high-profile deliverables) carries weight in transition contexts. TOGAF completion signals "this person is investing in their capability at the moment others are deciding what comes next."

**New evidence:**
- [[weekly-checkin-2026-04-20]] — transition moment recognition; Steve Paisley collaboration; external reception pattern; watching→shaping shift; TOGAF as intent signal

**Status at April 20, 2026:** Working. New use case (Transition Shaping) added. Common pitfall updated with calibration error insight. Framework now spans five principles and six use cases.

---

### April 13, 2026: Third Consolidation — Three New Evidence Points

**What Emerged:** The week of April 7–13 produced three new, significant observations that strengthen and extend the framework:

**1. Meeting drain as a recurring structural pattern (not a one-off).**
Two consecutive weekly check-ins both cited meetings as the primary energy drain and focus-disrupter. Week of April 8: "work focus fragmented by team meetings." Week of April 13 (rated 1/5): three-day team meeting, "content and dynamic both draining." This is no longer a personal observation — it is a structural diagnosis. The EA effectiveness routine (protected deep-work blocks, stakeholder coffee rotation) is the structural counter-pattern. It must be defended most actively when calendar pressure is highest.

**2. Personal reputation compounds independently of structural clarity.**
The April 13 check-in surfaced something important: Armo's individual standing with colleagues is strong ("personal reputation landing — both in how colleagues engaged and things they said directly") even though the team's collective remit is unresolved. This decoupling is strategically significant. EA effectiveness does not require structural clarity as a prerequisite — individual relationship-building and artefact delivery build credibility that persists and survives structural ambiguity. Build the reputation while the structural conversation is in progress.

**3. Team remit ambiguity as an active structural risk — distinct from personal effectiveness.**
The team's scope, ownership, and deliverables are "all unclear, and it hasn't been named openly yet." This is not a personal effectiveness failure — it is a structural gap that requires a managed conversation with the manager. The framing that works: collaborative, not accusatory — "I want to make sure I understand what success looks like for us as a team." Naming it early converts latent tension into a resolvable problem.

**New evidence:**
- [[weekly-checkin-2026-04-13]] — team remit as unspoken shared problem; personal reputation as decoupled asset; meeting drain second week running; individual conversations as the highest-energy channel

**Status at April 15, 2026:** Working. Three evidence points strengthen the framework without requiring new principles. The structural risk section is updated to reflect that "EA mandate" ambiguity can be specific to *team* remit, not just organisational appetite.

---

## Related Frameworks
- [[belron-business-understanding-framework]] — business proximity is a core input into this effectiveness framework; Phase 1 completion by end of April is a hard prerequisite for June roadmaps
- [[agentic-ai-governance-framework]] — MCP/A2A briefing is a concrete example of Principle 2 (dual-purpose artefact) and Use Case 4 (emerging tech governance ownership)
- [[ai-damage-assessment-strategy-framework]] — damage assessment paper/presentation is the Use Case 4 playbook applied to Option B emerging technology topic

---

## Future Development
**Questions for deeper exploration:**
- Which routine elements work in practice vs. which get squeezed when calendar pressure builds?
- What does the "EA brand" look like — what do stakeholders think of when they think of Armo in this role?

**Watch for:**
- After 4 weeks of applying the stakeholder routine: which touchpoints generated the most decision influence?
- After 8 weeks: has business proximity increased measurably (i.e., are you being consulted earlier in decisions)?

---

### May 22–23, 2026: Two Formal Reference Architectures Completed

**What Emerged:** In a single session, two full TOGAF Architecture Definition Documents were produced from accumulated braindumps: the MCP Agentic Reference Architecture ([[2026-05-22-mcp-agentic-reference-architecture]]) and the CCOTF Reference Architecture ([[2026-05-23-ccotf-reference-architecture]]). Both follow TOGAF 10 ADM Phases A–D with ArchiMate 3.2 notation, architecture principles, ABBs, standards information bases, and governance sections.

This represents a significant velocity step: converting several months of accumulated braindumps and research into formal governance artefacts in one session. The dual-purpose artefact principle (Principle 2) is now validated at this scale — the same session that produced internal thinking also produced stakeholder-ready documents (including the exec diagram [[2026-05-23-ccotf-exec-diagram]]).

**Pattern confirmed:** The TOGAF ADM template work (Principle 8) is paying off at speed. Having a clear artefact template in mind accelerates the translation from idea to governance document substantially.

**Sources:** [[2026-05-22-mcp-agentic-reference-architecture]], [[2026-05-23-ccotf-reference-architecture]]

**Status at May 24, 2026:** The EA artefact machine is running. Two reference architectures produced. The frontier now is social validation — getting these documents in front of stakeholders who can test, challenge, and endorse them.

---

*Consolidated from 34 sources | Confidence: High | Status: Working — fifth consolidation May 24; six use cases; two RAs complete; transition moment live*
