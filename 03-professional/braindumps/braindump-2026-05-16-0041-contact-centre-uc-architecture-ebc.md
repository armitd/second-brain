---
type: "braindump"
domain: "mixed"
date: "2026-05-16"
created: "2026-05-16 00:41"
themes: ["contact-centre-architecture", "uc-ccaas-representation", "single-tenant-microsoft", "ebc-observations", "architecture-communication"]
tags: ["#braindump", "#contact-centre", "#architecture", "#microsoft", "#uc", "#ccaas", "#belron-ipo"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-19]]"
consolidated_date: "2026-05-19"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
related_projects: ["contact-centre-future", "mcp-governance"]
---

# Braindump: Contact Centre Architecture, EBC Visit, and the Single Tenant Question

## Raw Thoughts
*(from daybook-2026-05-15)*

Think about contact centre architecture. How to express as a standard model of components - this exists as another knowledge article in COG.

EBC. They are solving the problems that we were solving at HSBC but they're still problems. Also streamdeck for controlling AV. Whatever happened to Crestron and AV control hardware vendors.

How to show architecture structure for UC and CCaaS. Difficulty of which vendor owns which bit. Representing proximity to data / knowledge. Vendor lock-in / vendor buy-in. See OneNote Notes.

Importance of being able to show tech standards to markets.

Continue with business case for single Microsoft tenant. Copilot across all orgs. Has this moved the needle on the value of single tenant.

## Content Analysis

### Main Themes
1. **Contact centre architecture as a reusable model** — the need for a standard component-level representation of how contact centre and UC architecture fits together; an existing COG article to link to
2. **EBC visit** — attended what appears to be an Executive Briefing Centre (likely a vendor's EBC, given the AV control observations). Key observation: same problems from HSBC days remain unsolved — these aren't new problems, they're persistent ones
3. **Architecture representation challenge** — how to draw UC/CCaaS in a way that honestly represents vendor ownership, data proximity, and the lock-in vs. buy-in tradeoff
4. **Tech standards as market signal** — ability to demonstrate architectural standards matters to an audience beyond the internal team (investors / IPO context)
5. **Single Microsoft tenant business case** — the Copilot/Agent 365 wave has potentially strengthened the case for consolidating Belron onto a single M365 tenant

### Supporting Ideas
- StreamDeck (Elgato) referenced as the modern replacement for what Crestron used to own — AV and meeting room control has fragmented away from dedicated hardware vendors
- Crestron's decline as a signal: proprietary AV control hardware is being replaced by software-defined solutions; relevant to anyone specifying meeting room or contact centre environments
- "See OneNote Notes" — architecture thinking is split across COG and OneNote; consolidation opportunity
- The EBC problems being "still problems" suggests that vendor briefings are offering polish over genuine resolution — worth holding vendors to account on this

### Questions Raised
- What is the existing COG knowledge article on contact centre architecture components? (referenced as already existing — find and link it)
- The EBC was with **Zoom** — specifically pitching their **AI add-ons to CCaaS** (agent assist, AI summaries, virtual agent, conversation analytics). "They're still problems" means the underlying CCaaS problems from HSBC haven't been solved — they've just had AI layered on top of them
- What specifically are the problems that were being solved at HSBC that remain unsolved? This is a key institutional memory worth capturing
- Has the Microsoft Agent 365 / Copilot wave actually changed the single-tenant value calculation, or does it just add one more reason to a case that was already strong?
- Is there an existing single-tenant business case document in COG or elsewhere?

### Decisions Contemplated
- **Architecture representation format:** How to visualise UC + CCaaS honestly — vendor-agnostic component model vs. vendor-specific mapping. Decision affects what gets shown to stakeholders and how vendor conversations are framed.
- **Single tenant business case:** Whether to formally write this up or continue informally. If IPO is H2 2026, tech standards maturity has a deadline.

## Strategic Intelligence

### Key Insights

1. **The EBC pattern is a warning sign.** "Solving the problems we were solving at HSBC but they're still problems" is a crisp observation: vendors brief against the same pain points across every client, every year, because those pain points are structurally persistent — not because they have genuinely solved them. This should calibrate how much weight Belron places on vendor briefing content vs. reference customer evidence.

2. **Architecture representation is a power tool, not just documentation.** The difficulty of showing "which vendor owns which bit" and "proximity to data/knowledge" is actually the point. An honest architecture diagram forces the question of vendor lock-in into the open — it's a tool for having a better conversation with stakeholders and vendors, not just a deliverable.

3. **The single-tenant question has a new catalyst.** Microsoft Agent 365 ($15/user/month, GA May 1) and Copilot Studio's cross-org capability directly reward single-tenant topology. This is the first time there's been a concrete, commercially priced reason to consolidate beyond IT simplification. The business case has a new hook.

4. **"Showing tech standards to markets" is IPO-adjacent.** With Belron IPO targeting H2 2026, demonstrating that the organisation has coherent, documented technology architecture standards is investor-facing work. Architecture communication becomes a pre-IPO deliverable, not just an internal discipline.

5. **OneNote is a COG debt.** Architecture thinking referenced as living in OneNote rather than COG. This is a recurring pattern — institutional knowledge fragmented across tools. Worth doing a structured OneNote-to-COG migration for the UC/CCaaS notes specifically.

### Pattern Recognition
- **Connection to Contact Centre of the Future project:** The UC/CCaaS architecture representation question is directly in scope for that project.
- **Connection to MCP Governance:** Single-tenant Microsoft consolidation affects where Agent 365 sits and how MCP governance is structured across Belron opcos.
- **Connection to Belron IPO (May 15 brief):** "Tech standards to markets" aligns with IPO preparation — investor-grade technology governance documentation.
- **HSBC pattern:** Second reference to HSBC experience as a benchmark for comparison. Armo's HSBC background provides institutional context for large-org architecture decisions.

### Strategic Implications
- The Contact Centre of the Future project needs a component model architecture document — not just vendor analysis but a vendor-agnostic reference architecture
- The single-tenant business case, if written up properly, becomes a pre-IPO governance artefact as much as a cost/capability case
- Vendor EBC content should be treated as marketing until validated against reference customers — build this scepticism into how EBC outputs are processed in COG

## Action Items

### Immediate (24-48 hours)
- [ ] Find the existing COG knowledge article on contact centre architecture and link it to the Contact Centre of the Future project 📅 2026-05-17
- [ ] Note the specific problems Zoom presented against at the EBC that "are still problems" from the HSBC days — capture before context fades 📅 2026-05-17

### Short-term (1-2 weeks)
- [ ] Pull the UC/CCaaS architecture notes out of OneNote and into COG — even rough notes are better than content that can't be surfaced 📅 2026-05-23
- [ ] Draft the architecture representation framework for UC + CCaaS: component model, vendor ownership layer, data proximity layer, lock-in/buy-in spectrum 📅 2026-05-23
- [ ] Revisit the single Microsoft tenant business case with Agent 365 and Copilot as new inputs — does the economics change meaningfully? 📅 2026-05-23

### Strategic Considerations
- Architecture communication (standards to markets) becomes more urgent as IPO H2 2026 approaches — start thinking about what an investor-grade technology architecture narrative looks like for Belron
- The EBC observation about persistent problems is worth documenting as a vendor evaluation principle: require reference customer validation, not just EBC demos

## Connections
- **Related Braindumps:** [[braindump-2026-05-11-0842-servicenow-perception-gap]] (vendor perception gap pattern)
- **Relevant Projects:** [[04-projects/contact-centre-future/PROJECT-OVERVIEW]], [[04-projects/mcp-governance/PROJECT-OVERVIEW]]
- **Relevant Briefs:** [[daily-brief-2026-05-11]] (Microsoft Agent 365 GA), [[daily-brief-2026-05-15]] (Belron IPO context)
- **OneNote:** UC and CCaaS architecture notes (to be migrated)
- **Source:** [[00-inbox/daybook-2026-05-15]]

## Domain Classification
- **Primary Domain:** Mixed — Professional + Project (Contact Centre of the Future, MCP Governance)
- **Reasoning:** Spans architecture thinking (professional discipline), a specific project (Contact Centre of the Future), and a strategic business decision (single-tenant Microsoft). IPO angle adds a cross-cutting professional dimension.
- **Privacy Level:** internal

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — captured on the move, brief notes rather than extended reflection
- **Emotional Tone:** Curious with a thread of mild frustration ("still problems") — suggests constructive scepticism rather than cynicism

### Confidence Assessment
- **Overall Analysis:** 80% — solid interpretation of sparse notes; some context gaps (which EBC, which specific HSBC problems)
- **Domain Classification:** 90% — clearly professional/project
- **Areas Requiring Clarification:** Which vendor's EBC? What were the specific persistent problems from HSBC days?

---

*Processed by COG Brain Dump Analyst*
