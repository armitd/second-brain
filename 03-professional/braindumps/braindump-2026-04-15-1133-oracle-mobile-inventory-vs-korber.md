---
type: "braindump"
domain: "professional"
date: "2026-04-15"
created: "2026-04-15 11:33"
last_updated: "2026-04-15 11:45"
themes: ["warehouse-management", "mobile-inventory", "vendor-comparison", "licensing"]
tags: ["#braindump", "#research", "#oracle", "#korber", "#wms", "#mobile-inventory"]
status: "researched"
energy_level: "medium"
emotional_tone: "curious"
confidence: "medium"
---

# Braindump: Oracle Mobile Inventory vs Körber — Research Findings

## Raw Thoughts
Need to find out more about Oracle Mobile Inventory product capabilities vs Körber, including licensing. Use case: both warehouse/parts inventory and technician van stock, for a small market (likely 10–30 users).

---

## Research Findings

### Oracle Mobile Inventory

#### What It Is
Oracle Mobile Inventory is **not a standalone product** — it is a module within **Oracle Fusion Cloud SCM** (Supply Chain Management). You cannot buy it independently; it requires an Oracle SCM Cloud subscription.

#### Core Mobile Capabilities (native, no third-party needed)
- Cycle counting and physical inventory counts
- Receiving (Purchase Orders, Transfer Orders, multi-line)
- Put away (with suggested putaway logic)
- Pick confirm (Sales Orders, Transfer Orders, Wave, Directed, Consolidated, Locator Sequence, Partial)
- Ship confirmation
- Subinventory and inter-/intra-org transfers
- Stock issues and stocking inquiries
- PAR (Periodic Automatic Replenishment) counts
- Inventory inquiry and visibility
- Packing operations
- Barcode scanning (camera or device scanner) and label printing
- **Offline mode** — PAR counts cached locally, synced when reconnected

#### UI & Device Support
- Built on Oracle's Redwood UX — native mobile pages, browser-based
- Works on any device with a browser; no separate app install required
- Role-based access: Warehouse Manager, Inventory Manager, Warehouse Operator, Receiving Agent

#### Third-Party Extenders (add cost)
- **RF-SMART** — extends Oracle Cloud with richer RF/barcode workflows
- **RFgen** — adds flexibility for high-volume environments
- **Propel Apps** — claims licence-free on-premise mode
- These are relevant if Oracle's native mobile flows are insufficient

#### Van Stock / Field Inventory
⚠️ **Not explicitly supported.** Oracle Mobile Inventory is designed for fixed warehouse operations. There is no native "van stock" or field technician mobile inventory module in the standard product. This would likely require customisation, a third-party extender, or a different Oracle product (e.g., Oracle Field Service, formerly TOA Technologies).

#### Licensing Model
- **Per user / per month** subscription, bundled into Oracle SCM Cloud
- **Starting price: ~$300/user/month** (published estimates — Oracle does not publicly disclose official pricing)
- Indicative costs at small market scale:
  - 10 users: ~$2,500–$7,000/month (~$30,000–$84,000/year in licensing alone)
  - First year including implementation/onboarding: **$60,000–$168,000**
  - Implementation costs alone can double the first-year licence cost
- No separate "mobile inventory" licence — it is included in the SCM Cloud subscription
- Additional costs: transaction volume overages, premium support, storage

#### Small Market Fit
⚠️ **Potentially uneconomical.** At $300/user/month, even 15 users = $54,000/year before implementation. Oracle SCM Cloud is designed for enterprise scale. The per-user model does not reduce meaningfully at low user counts.

---

### Körber K.Motion WMS

#### What It Is
Körber K.Motion WMS is a **full warehouse management system** — a standalone product, not tied to an ERP. Formerly known as HighJump WMS. Part of the Körber Supply Chain software portfolio.

#### Core Capabilities
- Receiving and put-away
- Slotting and location management
- Warehouse transfers and inventory differentiation
- Cross-docking
- Order and wave management
- Picking and packing (RF, voice-directed, paper)
- Advanced shipping and staging
- Load and route optimisation
- Returns management (built-in)
- Resource and labour management
- Integration with automation: AS/RS, AMRs, AGVs, conveyors, robotics
- Real-time inventory visibility with ML/AI analytics
- Multi-client support (relevant for 3PLs, less so here)

#### UI & Device Support
- **Fully mobile-enabled** — Android, iPad, iPhone
- **HTML5 browser interface** — any device, any browser, no app install
- Supports RF scanners, voice-directed operations, IoT sensors

#### Deployment
- Cloud (Körber Cloud) or on-premises — customer choice

#### Van Stock / Field Inventory
⚠️ **Not explicitly mentioned.** Körber is a warehouse-focused WMS. No van stock or field technician inventory module was found in product documentation. Same gap as Oracle — this is a warehouse tool, not a field mobility tool.

#### Licensing Model
- **Not publicly disclosed.** Körber requires direct vendor engagement for pricing.
- Modular — customers can select specific application modules
- Typical enterprise WMS pricing models: per-user, per-site, or transaction-based (unknown which Körber uses)
- Known characteristics: **15–20 year system lifespans** at customers; **99% retention rate** — suggests significant switching costs and long-term commitments
- Steep learning curve noted in user reviews — losing key staff creates operational risk

#### Small Market Fit
⚠️ **Uncertain.** Körber claims to serve small and medium warehouses with a "best-of-breed out-of-the-box" tier. However, the complexity and implementation investment typical of a full WMS may be disproportionate for a small market with 10–30 users. No minimum user count published. Pricing opaque — requires a quote.

---

## Head-to-Head Comparison

| Dimension | Oracle Mobile Inventory | Körber K.Motion WMS |
|---|---|---|
| **Product type** | SCM Cloud module (not standalone) | Standalone WMS |
| **ERP dependency** | Requires Oracle SCM Cloud | ERP-agnostic (integrates with most) |
| **Warehouse pick/pack/receive** | ✅ Native | ✅ Native (more comprehensive) |
| **Cycle counting** | ✅ Native | ✅ Native |
| **Offline mobile** | ✅ (PAR counts) | ✅ (full offline claimed) |
| **Van stock / field inventory** | ❌ Not supported | ❌ Not explicitly supported |
| **Technician mobile use case** | ❌ Not designed for this | ❌ Not designed for this |
| **Device support** | Any browser/device | Android, iOS, HTML5 browser |
| **Voice-directed ops** | ❌ (via third party only) | ✅ Native |
| **Automation integration** | Limited | ✅ Extensive |
| **Licensing transparency** | Partial (~$300/user/month) | None (contact vendor) |
| **Small market economics** | ⚠️ Expensive at low user counts | ⚠️ Unknown — needs quote |
| **Implementation complexity** | High (can double licence cost) | High (steep learning curve) |
| **Standalone deployment** | ❌ No | ✅ Yes |

---

## Critical Gap: Van Stock / Field Inventory

**Neither product is designed for technician van stock management.** Both are warehouse-focused. The field technician use case — a mobile worker managing parts inventory in a service van, issuing stock at a job site, triggering replenishment — is a different product category:

- **Oracle Field Service** (formerly TOA Technologies) — Oracle's field service management product. May have inventory capabilities for field technicians. Worth investigating separately.
- **ServiceMax / IFS Field Service Management** — purpose-built for field technician inventory
- **SAP Field Service Management** — if Belron is SAP-based
- A simpler option: a lightweight **van stock / consignment inventory app** that integrates with the core WMS/ERP, rather than trying to make a WMS serve both use cases

This may be the wrong framing — rather than "one product for both warehouse and van stock," the better architecture may be **best-of-breed per use case** with integration between them.

---

## Unanswered Questions (Still Need Vendor Engagement)

- [ ] Does Oracle have a minimum user commitment for SCM Cloud? What is the entry-level deal size?
- [ ] What does Körber actually cost for a small deployment (10–20 warehouse users)?
- [ ] Does Körber have a van stock / field inventory module that wasn't surfaced in public docs?
- [ ] What ERP does the target small market opco run — Oracle, SAP, or other? This may determine the path of least resistance.
- [ ] Is Oracle Field Service the right product for the van stock use case, and does it integrate with Oracle Mobile Inventory?
- [ ] Are there lighter-weight WMS alternatives better suited to small market scale (e.g., Deposco, Fishbowl, inFlow, Cin7)?

---

## Action Items

### Immediate
- [ ] Contact Oracle: request SCM Cloud pricing for 10–20 users and confirm whether Mobile Inventory is included 📅 2026-04-17
- [ ] Contact Körber: request demo and indicative pricing for small warehouse (10–20 users, single site) 📅 2026-04-17
- [ ] Investigate Oracle Field Service for the van stock / technician use case 📅 2026-04-18

### Short-term
- [ ] Confirm ERP landscape of the target small market opco — determines which product is native fit 📅 2026-04-22
- [ ] Consider whether a lightweight standalone WMS (Deposco / Cin7 / inFlow) is a better fit than Oracle or Körber at this scale 📅 2026-04-22
- [ ] Build a decision matrix once Körber pricing is known 📅 2026-04-25

---

## Connections
- **Relevant Context:** Enterprise Architect at windscreen repair/replace company — evaluating for both warehouse/parts inventory and technician van stock, small market (10–30 users)
- **Related:** [[COMPETITIVE-WATCHLIST]]

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Privacy Level:** confidential

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** Medium — public sources give a reasonable picture of capabilities; pricing for Körber is genuinely opaque and requires vendor engagement. Van stock gap is a significant finding that reframes the evaluation.
- **Key uncertainty:** Neither product explicitly covers the van stock use case. This may mean the comparison needs a third option added, or the use cases need to be split across two products.

---

*Processed by COG Brain Dump Analyst — updated with research findings 2026-04-15*
