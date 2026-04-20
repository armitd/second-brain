---
type: "consolidated-knowledge"
domain: "professional"
framework: "wms-field-inventory-landscape"
created: "2026-04-20"
last_updated: "2026-04-20"
consolidation_id: "consolidation-2026-04-20"
source_documents: 2
status: "emerging"
tags: ["#framework", "#consolidated", "#WMS", "#inventory", "#Oracle", "#Körber", "#field-service", "#Belron"]
---

# WMS & Field Inventory Landscape Framework

## Framework Overview
A working model of the warehouse management and field inventory software market as it applies to Belron's specific context — a mobile-first service business where "inventory" is carried in technician vans rather than managed in a fixed warehouse. Covers the Oracle vs. Körber evaluation, the van stock gap, and decision criteria for a market with unusual requirements.

**Status:** Emerging (initial market scan complete; Belron-specific decision not yet made)
**Created:** 2026-04-20
**Source Insights:** 2 documents — Oracle Mobile Inventory vs. Körber braindump (Apr 15), competitive watchlist

---

## The Context — Why This Is Hard

Standard WMS systems are designed for fixed warehouse operations: goods arrive at a dock, are stored in a location, picked for orders, and shipped. This model does not map to Belron's operational reality:

- **Technicians carry inventory in vans** — the "warehouse" is mobile and each van is effectively a micro-location
- **Van stock replenishment** is the critical logistics operation — not warehouse-to-customer, but depot-to-van
- **Job completion triggers consumption** — inventory is consumed at the customer site, not at a warehouse dispatch point
- **Real-time van-level visibility** is the operational requirement — the inventory system must know what is in each van, not just each depot

Most WMS platforms were not designed for this pattern. The van stock gap is not a minor missing feature — it is a fundamental architectural mismatch that must be addressed by any viable solution.

---

## The Market Evaluation — Oracle Mobile Inventory vs. Körber K.Motion

### Oracle Mobile Inventory
- **What it is:** A module within Oracle SCM Cloud — not a standalone WMS, but an inventory management component
- **Pricing:** Approximately $300/user/month — mid-tier SaaS pricing for enterprise software
- **Van stock support:** None confirmed. Oracle Mobile Inventory focuses on warehouse operations and mobile device support for warehouse workers, not for field technicians managing van-based inventory
- **Integration:** Native to Oracle SCM Cloud / EBS ecosystem — lowest integration friction if Belron is already Oracle-based
- **Verdict:** Potentially viable as part of a broader Oracle SCM investment, but van stock is a critical gap. Would likely require Oracle Field Service (a separate product) or a custom extension to handle van-level inventory

### Körber K.Motion WMS
- **What it is:** A standalone enterprise WMS from Körber Supply Chain, one of the tier-1 WMS vendors
- **Pricing:** Opaque — enterprise pricing model, not published. Expect significant licence + implementation cost
- **Van stock support:** Not confirmed. Körber is a traditional WMS vendor; van stock / field inventory is not a standard use case. Would require evaluation of their mobile/field service modules
- **Integration:** Standalone platform — would require integration with Belron's existing ERP and scheduling systems
- **Verdict:** Enterprise-grade capability but designed for warehouse operations. Van stock support requires dedicated investigation. The standalone nature creates integration overhead.

---

## The Critical Finding — The Van Stock Gap

Neither Oracle Mobile Inventory nor Körber K.Motion has confirmed van stock support as a standard capability. This is the pivotal finding:

| Requirement | Oracle Mobile Inventory | Körber K.Motion | Standard WMS |
|---|---|---|---|
| Fixed warehouse inventory | Partial (module within SCM) | Yes | Yes |
| Van/vehicle-level inventory | Not confirmed | Not confirmed | Not standard |
| Real-time van stock visibility | Not confirmed | Not confirmed | Not standard |
| Depot-to-van replenishment | Not confirmed | Not confirmed | Not standard |
| Job completion consumption | Not confirmed | Not confirmed | Not standard |

**The implication:** A standard WMS selection process will not solve Belron's core problem. The selection criteria must include van stock as a required capability, not a preference.

---

## The Decision Framework

### Step 1: Clarify the Requirement
Before evaluating vendors, document the van stock requirement precisely:
- How many vans? How many unique SKUs per van?
- What is the replenishment model — daily depot replenishment? On-demand? Threshold-triggered?
- What are the integration points — which system creates the job, consumes the inventory, triggers replenishment?
- Is real-time van visibility required, or is end-of-day reconciliation sufficient?

### Step 2: Apply the Van Stock Filter First
Any vendor that cannot support van-level inventory as a standard (not custom) capability should be deprioritised. The implementation risk and customisation cost of forcing a fixed-warehouse WMS into a van inventory model is typically prohibitive.

### Step 3: Evaluate Platform Coherence
The van stock solution cannot be evaluated in isolation — it must fit the broader system landscape:
- If Belron is Oracle-based (EBS/SCM): Oracle Field Service is the most coherent van stock solution. Oracle Field Service manages mobile workforce scheduling *and* parts/inventory at the van level — it is purpose-built for field service businesses.
- If Belron uses a different ERP: evaluate whether Körber or a specialist field service platform (ServiceMax, IFS Field Service) better fits the integration architecture.

### Step 4: Field Service vs. WMS — The Right Framing
Van stock management sits at the intersection of:
- **WMS** (inventory management, stock levels, replenishment)
- **Field Service Management** (technician scheduling, job dispatch, mobile workforce)

This intersection is a distinct product category — **Field Service Management (FSM)** platforms natively cover van inventory as part of their scope. Key vendors:
- **Oracle Field Service** (formerly TOA Technologies) — strongest if already Oracle-invested
- **IFS Field Service Management** — strong in engineering/technical field service
- **ServiceMax** (Salesforce ecosystem) — strongest if Salesforce-invested
- **ClickSoftware / Salesforce Field Service** — alternative if Salesforce is the CRM platform

**The reframe:** Rather than asking "which WMS handles van stock?" ask "does Belron need a Field Service Management platform, and which one fits the existing system landscape?"

---

## Belron-Specific Considerations

### The Mobile-First Service Model
Belron's value chain is fundamentally mobile — the technician's van is the primary operational unit. The "inventory system" is in service of the technician, not the warehouse. Any system evaluation must start from the technician experience, not the depot manager experience.

### Oracle Investment Path
If Belron uses Oracle EBS (as suspected from the systems landscape analysis), the Oracle path has strong coherence:
- Oracle EBS → Oracle SCM Cloud → Oracle Mobile Inventory → Oracle Field Service
- Single vendor, integrated data model, native integration
- The van stock gap may be addressable within the Oracle product family without going to market for a separate WMS

### The Salesforce Angle
Salesforce is confirmed in Belron's landscape. Salesforce Field Service (the Salesforce FSM product) integrates natively with the Salesforce CRM. If customer-facing processes (booking, case management) run in Salesforce, extending into Salesforce Field Service for technician dispatch and van inventory has architectural coherence.

---

## Applications & Use Cases

### Use Case 1: Van Stock Gap Assessment
**Objective:** Confirm whether the van stock gap is real and unaddressed in Belron's current landscape
**How:**
1. Ask: does Belron currently have real-time van-level inventory visibility? If yes — what system provides it?
2. If not: quantify the operational impact — how does this affect stock-outs, excess van inventory, and replenishment efficiency?
3. This question may reveal that Belron has already solved it with a proprietary or specialist solution — confirming the systems landscape is the first step

### Use Case 2: Oracle Field Service Evaluation
**Objective:** Assess Oracle Field Service as the van stock solution if Belron is Oracle-invested
**How:**
1. Confirm Belron's Oracle investment depth: EBS only? SCM Cloud? Oracle Cloud broadly?
2. Request Oracle Field Service demo focused specifically on van/technician inventory management
3. Assess integration complexity with existing booking and scheduling systems
4. Compare TCO: Oracle Field Service licence vs. standalone WMS + integration cost

### Use Case 3: Market Scoping for RFI/RFP
**Objective:** If a formal procurement process is required, frame the requirements correctly
**Key inclusion criteria:**
- Van/field inventory management as a *standard* capability (not custom)
- Real-time mobile visibility for technicians
- Depot-to-van replenishment workflow support
- Integration with Belron's CRM (Salesforce) and ERP (Oracle/EBS)
- UK/EU deployment with GDPR-compliant data handling

---

## Boundaries & Limitations

**This framework applies when:**
- Evaluating inventory management solutions for a field service / mobile workforce business
- The inventory is primarily carried in vehicles rather than managed in fixed locations

**This framework does NOT apply when:**
- The primary inventory challenge is depot/warehouse management (use a standard WMS)
- The van stock problem is already solved by an existing specialist tool

---

## Evolution & History

### April 15, 2026: Initial Market Scan
Oracle Mobile Inventory and Körber K.Motion researched in depth. Critical finding: van stock is not a standard capability in either platform. Oracle Field Service identified as the most coherent van stock solution in an Oracle-invested landscape. Field Service Management reframed as the correct product category.

**Source:** [[braindump-2026-04-15-1133-oracle-mobile-inventory-vs-korber]]

---

## Related Frameworks

- [[belron-business-understanding-framework]] — Layer 4 (Systems Landscape) is where the van stock solution question surfaces; Layer 3 (Customer Journey) Stage 3 (Pre-Visit/Parts Check) is the process point this addresses
- [[agentic-ai-governance-framework]] — van stock could be an MCP server candidate: a Parts agent that checks van inventory and triggers replenishment is a natural agentic workflow in the Belron application map

---

## Future Development

**Key questions to resolve:**
- Does Belron currently have van-level real-time inventory visibility? If so, which system provides it?
- What is Belron's Oracle investment depth — EBS only, or broader Oracle Cloud?
- Has the WMS/van stock question been evaluated previously and if so, what was the conclusion?

**Next actions:**
- [ ] Ask a relevant stakeholder (operations/IT): "How do we currently manage van stock — do we have real-time visibility by van?" 📅 2026-04-30
- [ ] If the answer is "no" or "manually": assess Oracle Field Service as the first candidate 📅 2026-05-07

---

*Consolidated from 2 sources | Created: April 20, 2026 | Status: Emerging — van stock gap identified; Oracle Field Service as probable path if Oracle-invested; field service management reframe is the key insight*
