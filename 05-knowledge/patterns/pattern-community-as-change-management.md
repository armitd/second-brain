---
type: "pattern-analysis"
pattern: "community-as-change-management"
created: "2026-06-19"
domains: ["professional", "project-ccotf"]
frequency: "medium"
tags: ["#pattern", "#analysis", "#community", "#change-management", "#ccotf"]
---

# Pattern: Community Is the Change Management Plan

## Pattern Description

Building a community of practitioners *before* the architecture decision is made — not to inform the decision, but to make those practitioners co-authors of it — is a more durable change management strategy than any communications plan deployed after the fact.

**Frequency:** Appeared in 3+ documents across June 2026, most clearly in CCOTF programme context

**Domains:** Project (CCOTF), Professional (EA practice)

**Significance:** Applies to any pan-organisational programme that will eventually affect practitioners who are currently outside the design team

---

## Occurrences

### June 19, 2026 — [[braindump-2026-06-19-1652-hive-ccotf-community]]
**Context:** CCOTF programme — deciding whether to build a Hive community for contact centre practitioners across Belron's opcos

**Manifestation:** "The community IS the change management plan. CCOTF is a pan-Belron programme that will eventually affect every contact centre agent and manager across 35 countries. Building a community now — before the platform decision — means the people most affected are shaping the direction, not being told about it post-fact."

**Outcome:** Decision to explore building a CCOTF Hive community using the Signals feature for structured ground-level intelligence gathering

---

### June 5, 2026 — [[braindump-2026-06-05-1739-btops-collaboration-ccotf-viva-engage]]
**Context:** BT&Ops collaboration friction — question of where CCOTF should live as a community (Teams channel vs. Viva Engage vs. Hive)

**Manifestation:** Recognised that CCOTF needed a community home before it needed a communications plan — the conversation would happen in informal channels regardless

**Outcome:** Platform question remained open; the need for a structured community home was confirmed

---

### June 3, 2026 — [[braindump-2026-06-03-1009-ccotf-qualtrics-genesys-ops]]
**Context:** Cross-market intelligence gap — EA team doesn't have visibility into what contact centre platforms and pain points exist in each opco

**Manifestation:** Stakeholder loops (Jamie/Joakim/Heidi) identified as the current workaround for a problem that a community would solve structurally — ground-level intelligence is trapped in bilateral relationships rather than flowing to the programme team

**Outcome:** Identified the intelligence gap as a structural problem; individual stakeholder loops as the workaround

---

## Analysis

**What Triggers This Pattern:**
- A programme team building architecture or strategy that will affect people who have no voice in the design
- Intelligence that only exists at the practitioner level (current platform pain points, workflow quirks, cross-opco differences)
- A programme that will require adoption across organisations the programme team doesn't directly control

**What Follows When the Pattern Is Applied:**
- Practitioners who contribute to the programme become natural early adopters and internal advocates
- Architecture open issues (specifically: what's the current platform? what are the real pain points?) can be resolved through community signals rather than formal workshops
- The programme has a visible home — not just a PowerPoint in someone's inbox

**What Follows When the Pattern Is Ignored:**
- Change management becomes a separate workstream that starts after the architecture is done
- Adoption resistance is higher because practitioners feel the architecture was done *to* them
- Programme team remains blind to operational realities that practitioners know but never had a channel to share

**Cross-Domain Implications:**
This pattern applies anywhere EA produces architecture that affects practitioners at a distance:
- MCP Governance: the developers building agent tools are the practitioners; a governance community would reduce "governance as friction" perception
- Any group-level standard applied to opcos: the opco leads are the practitioners; community involvement precedes adoption

**Potential Actions:**
- For CCOTF: establish the Hive community before the CCaaS platform decision — so the practitioners shape the requirements, not just receive the result
- For MCP Governance: consider a developer/architect community as the adoption vehicle for the governance framework — not just a policy document

---

## Structural Pattern: The Three Roles

In any programme-level community applied to change management, three roles are needed:

| Role | Purpose | Risk if absent |
|---|---|---|
| **Founding members** | Credibility anchors — respected practitioners who join early and signal to peers that this is worth engaging with | Community never reaches critical mass |
| **Signal contributors** | Practitioners who submit observations, pain points, market intelligence | Community becomes top-down broadcast rather than intelligence engine |
| **Programme liaisons** | Programme team members who visibly act on community input | Practitioners stop contributing if they see no impact from their signals |

The pattern fails when communities are built as communication channels (broadcast only) rather than intelligence channels (input → action loop). The key signal that the pattern is working: an architectural decision visibly changed because of community input.

---

## Evolution Over Time

This pattern has not historically been used explicitly in EA practice — architecture frameworks are usually designed by architects and communicated to stakeholders. The shift is the recognition that:
1. Pan-organisational programmes (30+ countries, 30,000+ people) cannot be governed by a small EA team producing documents
2. The practitioners at the edge often have information the centre does not (current platform, local contracts, operational workarounds)
3. Adoption is cheaper when people co-own the direction than when they receive it

The Hive Signals concept (CCOTF, June 2026) is the first concrete implementation attempt at Belron.

---

*Pattern identified through consolidation of 3+ sources from June 2026 | Status: Emerging — first articulation; no confirmed outcomes yet*
