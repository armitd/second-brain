---
type: "braindump"
domain: "professional"
date: "2026-04-08"
created: "2026-04-08 13:52"
themes: ["EBS", "Oracle E-Business Suite", "Salesforce", "ERP", "CRM", "integration", "enterprise architecture"]
tags: ["#braindump", "#professional", "#EBS", "#Oracle", "#Salesforce", "#ERP", "#integration", "#EA"]
status: "researched"
energy_level: "medium"
emotional_tone: "investigative"
confidence: "high"
---

# Braindump: What Is EBS in the Salesforce World?

## Raw Thoughts
What is EBS in Salesforce world?

---

## Answer

**EBS = Oracle E-Business Suite** — Oracle's on-premise ERP (Enterprise Resource Planning) system.

In the context of Salesforce, EBS almost always refers to integrating Salesforce (front-office CRM) with Oracle EBS (back-office ERP). It is one of the most common enterprise integration patterns: the two systems hold different but overlapping data about customers, orders, and financials — and organisations need them to talk to each other.

---

## What Each System Does

| System | Type | Domain | Typical Data |
|---|---|---|---|
| **Salesforce** | CRM | Front-office | Leads, opportunities, contacts, accounts, service cases, customer interactions |
| **Oracle EBS** | ERP | Back-office | Orders, invoices, inventory, financials, HR, procurement, supply chain |

**The overlap and the problem:** A customer exists in both. A sales opportunity in Salesforce becomes an order in EBS. An invoice raised in EBS relates to an account in Salesforce. Without integration, data is duplicated, manual re-entry happens, and the two systems tell different stories about the same customer.

---

## Why Integration Is Non-Trivial

Oracle EBS is an older, complex, on-premise system with its own data model. Salesforce is a cloud CRM with a very different architecture. Bridging them requires:

- **Middleware / integration platform** — typically MuleSoft (owned by Salesforce), WSO2, or similar. MuleSoft has pre-built connectors for Oracle EBS which reduces the integration effort significantly.
- **Data mapping** — the customer/account/order models are not the same across the two systems; translation logic is needed
- **Sync direction decisions** — which system is the master of record for which data? (e.g., account name in Salesforce vs. customer name in EBS — who wins when they conflict?)
- **Trigger events** — what causes data to flow? (e.g., when an opportunity is marked Closed Won in Salesforce, does it automatically create an order in EBS?)

---

## Common Integration Patterns (Salesforce ↔ EBS)

1. **Opportunity-to-Order:** When a deal closes in Salesforce, create/update an order in EBS
2. **Account-Customer sync:** Keep customer master data consistent between CRM and ERP
3. **Invoice visibility in Salesforce:** Surface EBS invoice and payment status inside Salesforce so sales/service teams can see financial position without logging into EBS
4. **Product/Price synchronisation:** EBS holds the product catalogue and pricing; sync into Salesforce for accurate quoting
5. **Inventory/availability:** Pull stock availability from EBS into Salesforce for sales teams making commitments

---

## The EA Lens

EBS ↔ Salesforce integration is a classic **front-office/back-office boundary problem** — which is exactly the kind of architectural boundary that EA should own.

Key questions for your context:
- Does Belron use Oracle EBS as its ERP, or a different system (SAP, Microsoft Dynamics, etc.)?
- If yes, is there a live integration between Salesforce and EBS already, or is data still being moved manually?
- What is the middleware layer — MuleSoft, custom APIs, something else?
- Who owns the integration — IT, Salesforce team, or an integration team?

**Note:** This also connects directly to the MCP braindump — MCP servers could eventually sit in front of EBS and Salesforce, allowing AI agents to query both systems without bespoke integrations. That's the future state architecture.

---

## Action Items

### Immediate
- [ ] Confirm: does Belron use Oracle EBS, or a different ERP? 📅 2026-04-10
- [ ] If yes: find out whether a Salesforce-EBS integration exists and what the middleware layer is 📅 2026-04-10

### Short-term
- [ ] If integration exists: understand what data flows, in which direction, and what the known gaps are 📅 2026-04-17
- [ ] If no integration or partial integration: this is a significant EA gap worth documenting 📅 2026-04-17

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1349-salesforce-managed-unlocked-packages]] — Salesforce architecture context
- **Related braindump:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — MCP could sit in front of both EBS and Salesforce as a unified data access layer for AI agents
- **Related braindump:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — front-office/back-office boundary is exactly where EBS ↔ Salesforce integration lives

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** private

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 88%
- **EBS definition:** 97% — Oracle E-Business Suite is the standard meaning in enterprise/Salesforce contexts
- **Belron-specific relevance:** 65% — depends on whether Belron actually uses Oracle EBS; needs verification

---

*Processed by COG Braindump Analyst*
