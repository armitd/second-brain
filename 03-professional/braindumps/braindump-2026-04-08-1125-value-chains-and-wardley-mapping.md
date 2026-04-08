---
type: "braindump"
domain: "professional"
date: "2026-04-08"
created: "2026-04-08 11:25"
themes: ["value chains", "Wardley mapping", "Porter", "enterprise architecture", "strategic tools", "business understanding"]
tags: ["#braindump", "#professional", "#value-chain", "#Wardley", "#Porter", "#EA-tools"]
status: "researched"
energy_level: "high"
emotional_tone: "curious/learning"
confidence: "high"
---

# Braindump: Value Chains and Value Chain Mapping

## Raw Thoughts
I need to learn about value chains and value chain mapping.

---

## Research Primer

There are two distinct but related tools here. You need both, and they serve different purposes.

---

### Tool 1: Porter's Value Chain (1985)
*Use this to understand how a business creates value*

**What it is:** A framework that breaks a company's activities into the steps that collectively create value for the customer and profit for the business. Michael Porter introduced it in *Competitive Advantage* (1985). Every business activity is either a *primary activity* (directly creating the product/service) or a *support activity* (enabling the primary activities to work).

**Primary Activities** (the value-creating sequence):
1. **Inbound Logistics** — receiving, storing, and handling inputs (for Belron: glass, parts, adhesives arriving at fitting centres)
2. **Operations** — turning inputs into the product/service (for Belron: the technician repairing or replacing the windscreen)
3. **Outbound Logistics** — getting the product/service to the customer (for Belron: mobile van dispatch; the technician going to the customer)
4. **Marketing & Sales** — how customers find and choose you (for Belron: insurance partnerships, direct booking, brand)
5. **Service** — post-sale support (for Belron: ADAS calibration, warranty, customer satisfaction follow-up)

**Support Activities** (enabling the primary activities):
- **Firm Infrastructure** — finance, legal, management, EA (your function)
- **Human Resource Management** — recruitment, training, technician upskilling
- **Technology Development** — systems, tools, R&D (scheduling systems, calibration equipment)
- **Procurement** — buying the inputs (glass, adhesives, tools)

**The insight:** Profit (or "margin") is the difference between what the customer pays and the total cost of all these activities. Value chain analysis asks: *where in this chain are we adding genuine value, where are we wasting cost, and where is competitive advantage being built or eroded?*

**For Belron:** The value chain is actually interesting because Belron's business is not manufacturing — it's a service chain where the Operations step (the technician) happens at the customer's location. That inverts the usual outbound logistics model. Understanding this is foundational EA context.

---

### Tool 2: Wardley Mapping (2005–present)
*Use this to make strategic architecture decisions*

**What it is:** Created by Simon Wardley, a Wardley Map plots business components (capabilities, services, systems) on two axes to reveal where to invest, what to commoditise, what to build vs. buy, and where disruption is likely. It is the most powerful strategic tool available to enterprise architects today.

**The two axes:**
- **Y axis (Value Chain):** Vertical position = visibility to the end user. At the top: things the user directly experiences (the booking, the repair, the invoice). At the bottom: invisible infrastructure that enables those things (servers, databases, protocols).
- **X axis (Evolution):** Horizontal position = how mature the component is.
  - **Genesis** (left): Novel, uncertain, no standards, high differentiation
  - **Custom Build** → **Product/Rental** → **Commodity/Utility** (right): Increasingly standardised, cheaper, interchangeable

**What this tells you:**
- Components on the left (Genesis/Custom) are where you *invest* because they are differentiating
- Components on the right (Commodity) are where you *minimise cost* — you buy or outsource them; building them yourself is waste
- Everything moves left to right over time — nothing stays custom forever
- The map reveals **where evolution pressure is heading** before it arrives

**A simple Belron example:**

| Component | Value Chain Position | Evolution Stage | Implication |
|---|---|---|---|
| Technician repair skill | High (customer-facing) | Custom/Product | Core capability — invest in training |
| ADAS calibration | High (customer-facing) | Custom (moving to Product) | Growing differentiator — build now |
| Booking system | Mid (enables service) | Product | Buy, don't build |
| Glass supply chain | Low (invisible) | Commodity | Minimise cost, use standard suppliers |
| Cloud infrastructure | Very low (invisible) | Utility | Pure commodity — use AWS/Azure |
| AI scheduling optimiser | Mid (enables service) | Genesis/Custom | Early-stage differentiator — watch or invest |

**The strategic power:** A Wardley Map shows you that building a custom booking system is waste (it's a commodity), but investing in ADAS calibration capability is smart (it's still custom/product and becoming more valuable as the vehicle fleet evolves). This is exactly the kind of decision-making that EA should be driving.

**2026 relevance:** A 2026 article specifically applies Wardley Mapping to build-vs-buy decisions in agentic AI — directly relevant to the A2A/MCP braindump. As AI components evolve rapidly from Genesis toward Product, Wardley Maps help you decide which AI capabilities to build now vs. wait for them to commoditise.

---

### How They Relate

Porter tells you *what* activities create value.
Wardley tells you *where* those activities sit strategically and *how* to invest in them.

Use Porter to understand the Belron business model.
Use Wardley to make architecture and investment decisions within it.

---

## Strategic Intelligence

### Key Insights

1. **Value chain analysis of Belron would directly answer the "getting closer to the business" question.** Building a Porter value chain for Belron — even a rough one — forces you to understand every step from glass procurement to post-repair customer satisfaction. It's a learning tool as much as a strategy tool.

2. **A Wardley Map of Belron's capabilities would be a high-impact EA artefact.** No one has probably done this. A map showing where Belron's capabilities sit on the evolution axis — and where they *should* sit — is the kind of thing that gets you in front of leadership. It connects directly to the stakeholder visibility goal.

3. **These two tools together answer the questions EA is supposed to answer.** What does the business do, where does value flow, where should we invest, what should we buy, where is disruption coming? With Porter + Wardley, you have a systematic way to answer all of these.

### Connection to This Week's Themes

This braindump connects everything from this week:
- **Getting closer to Belron** → Porter value chain analysis *is* the structured way to understand how Belron works
- **Stakeholder visibility** → A Wardley Map of Belron's capabilities is a concrete, high-visibility EA artefact
- **A2A/MCP strategy** → Wardley Mapping is exactly how you decide where AI agents and protocols sit on the evolution axis and whether to build or buy
- **EA effectiveness** → Value chain + Wardley gives you the strategic vocabulary to have boardroom-level conversations

---

## Learning Path

### Week 1 — Foundations
- [ ] Read the Wikipedia entry on Wardley Maps — 20 minutes, gives you the vocabulary 📅 2026-04-10
- [ ] Read the CIO introduction to Wardley Value Chain Mapping (short, practical) 📅 2026-04-10
- [ ] Sketch a rough Porter value chain for Belron from memory — note the gaps, which are your learning agenda 📅 2026-04-12

### Week 2 — Go Deeper
- [ ] Read Simon Wardley's free online book: *Wardley Maps* (available at learnwardleymapping.com) — focus on chapters 1–3 first 📅 2026-04-18
- [ ] Try the Wardley Maps for Enterprise Architects resource at wardleymaps.com/ea 📅 2026-04-18
- [ ] Draft a first Wardley Map of one Belron capability area (e.g. booking and dispatch) 📅 2026-04-20

### Week 3 — Apply
- [ ] Refine the Belron Wardley Map with input from operational stakeholders (connects to the stakeholder coffee rotation) 📅 2026-04-25
- [ ] Use the 2026 Medium article on Wardley Mapping + agentic AI (build-vs-buy) to apply the map to the A2A/MCP decisions 📅 2026-04-25

### Longer-term
- [ ] Consider creating a living Wardley Map for Belron as a standing EA artefact — review and update quarterly 📅 2026-05-31
- [ ] Present a value chain/Wardley insight to a stakeholder — turns a learning exercise into a visibility moment

---

## Action Items

### Immediate (24–48 hours)
- [ ] Bookmark: wardleymaps.com/ea — Wardley Mapping specifically for enterprise architects 📅 2026-04-09
- [ ] Sketch the Belron Porter value chain from memory (rough is fine) — gaps reveal your learning priorities 📅 2026-04-10

### Short-term (1–2 weeks)
- [ ] Work through Wardley Maps chapters 1–3 (free online) 📅 2026-04-18
- [ ] Draft a Wardley Map for the Belron booking-to-dispatch capability 📅 2026-04-20

### Strategic Considerations
- A finished Wardley Map of Belron's key capabilities — even a draft one — is the kind of artefact that could anchor a conversation with your manager about EA priorities
- The combination of Porter (business understanding) + Wardley (strategic positioning) is a complete toolkit for an enterprise architect. Most EAs only know one or neither.

---

## Key Resources

- [wardleymaps.com/ea — Wardley Mapping for Enterprise Architects](https://www.wardleymaps.com/ea)
- [CIO — Introduction to Wardley Value Chain Mapping](https://www.cio.com/article/196094/an-introduction-to-wardley-value-chain-mapping.html)
- [BMC — Wardley Value Chain Mapping guide](https://www.bmc.com/blogs/wardley-value-chain-mapping/)
- [Medium — Build vs Buy in 2026: Using Wardley Mapping for Agentic AI](https://medium.com/@haberlah/build-vs-buy-in-2026-using-wardley-mapping-to-navigate-the-agentic-ai-shift-be24d534b054)
- [Open Practice Library — Wardley Mapping](https://openpracticelibrary.com/practice/wardley-mapping/)
- [Porter's Value Chain — Toolshero](https://www.toolshero.com/management/value-chain-analysis-porter/)

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1123-getting-closer-to-belron-business]] — Porter value chain analysis *is* the structured way to understand how Belron works
- **Related braindump:** [[braindump-2026-04-08-0937-passive-to-active-stakeholder-visibility]] — Wardley Map is a high-visibility EA artefact
- **Related braindump:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — Wardley Mapping applies directly to build-vs-buy decisions for A2A/MCP

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** private

## Processing Notes
### Emotional Context
- **Energy Level:** High — strong learning intent; this is a foundational capability gap being addressed proactively
- **Emotional Tone:** Curious and motivated — the right posture for skill acquisition

### Confidence Assessment
- **Overall Analysis:** 94%
- **Framework descriptions:** 97% — Porter and Wardley are well-established; descriptions verified against authoritative sources
- **Belron-specific applications:** 82% — logical extrapolations; actual map needs validation with operational knowledge

---

*Processed by COG Braindump Analyst*
