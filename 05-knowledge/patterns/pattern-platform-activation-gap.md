---
type: "pattern-analysis"
pattern: "platform-activation-gap"
created: "2026-05-19"
domains: ["professional", "enterprise-architecture"]
frequency: "medium"
tags: ["#pattern", "#analysis", "#enterprise-architecture", "#vendor-management", "#belron"]
---

# Pattern: Platform Activation Gap

## Pattern Description
Belron (and large enterprises generally) consistently pay for enterprise platform capabilities that are significantly underutilised. The licensed capability is available, the commercial commitment is made, but the features remain inactive — creating an "activation gap" between what is owned and what is used.

**Frequency:** Observed independently across two major platforms in one braindump pair (May 2026); aligns with the LeanIX usage braindump (April 2026)

**Domains:** Professional — Enterprise Architecture, Vendor Management

**Significance:** Every activation gap is a sunk-cost waste and a missed strategic opportunity. Closing activation gaps is typically higher ROI than new vendor commitments because the commercial investment is already made.

---

## Occurrences

### May 2026 — Informatica IDMC
**Context:** Research into Informatica toolkit beyond MDM.

**Manifestation:** Belron uses Informatica for MDM. The IDMC platform includes Data Quality, Data Catalog, Data Governance, API Integration, and AI Governance Catalog — likely already licensed or available under the existing subscription. These modules are almost certainly inactive at Belron.

**Outcome:** The activation gap is being treated as an audit action — find out what is licensed vs. what is active before commissioning any new tooling for EU AI Act governance or AI training data quality.

**Source:** [[braindump-2026-05-14-1444-informatica-idmc-beyond-mdm]]

---

### May 2026 — Microsoft 365 / Azure
**Context:** Microsoft single tenant strategy analysis.

**Manifestation:** The Belron Microsoft estate almost certainly includes E5 Security and Compliance features, advanced Entra ID capabilities, Defender for Cloud, and Sentinel — all potentially underactivated relative to what is licensed. The parallel question to Informatica: "what have we paid for that we're not using?"

**Outcome:** The Microsoft estate audit is framed the same way as the Informatica audit — a license discovery exercise before any new investment decisions.

**Source:** [[braindump-2026-05-14-0907-microsoft-single-tenant-strategy]]

---

### April 2026 — LeanIX
**Context:** LeanIX learning and use cases braindump.

**Manifestation:** LeanIX is in use at Belron for some functions (application portfolio, technology radar). Business Architecture features (capability maps, value streams) are likely underused. Integration features connecting to Jira, ServiceNow, and Azure may be inactive.

**Outcome:** Identified as an activation opportunity in the LeanIX framework; BA training gives EA the knowledge to activate these features meaningfully.

**Source:** [[braindump-2026-04-09-1022-leanix-learning-use-cases]]

---

## Analysis

**What Triggers This Pattern:**
- Large enterprise platforms are sold at Group level with broad licensing — features are available but no one is specifically tasked with activating them
- Teams managing day-to-day operations use the features they know; adjacent capabilities require awareness and effort to adopt
- New capabilities (e.g. Informatica AI Governance Catalog, added 2025) are added to existing platforms post-purchase without proactive notification to all clients
- EA functions that don't audit the full estate miss the gap between what is owned and what is used

**What Follows This Pattern:**
- Adjacent problems get solved with new vendor purchases — creating redundancy and additional cost
- The existing platform vendor gets displaced from strategic conversations they should be part of
- EA credibility is damaged when the "we need to buy X" recommendation turns out to be "we already have X"

**Cross-Domain Implications:**
- Applies across all enterprise platform categories: cloud (Azure), integration (Informatica CDI), data (IDMC), ITSM (ServiceNow), collaboration (M365)
- The pattern recurs because it is structural — large platform vendors bundle capabilities that most buyers don't fully explore

**Recommended Actions:**
1. **Run a periodic platform audit** — for each major enterprise vendor relationship, inventory: (a) what is licensed, (b) what is activated, (c) what is actively used
2. **Connect new requirements to existing platforms first** — before commissioning new tooling, check whether an existing platform already covers it
3. **Track vendor roadmap additions** — platforms add features regularly; an EA practice should have a mechanism to review new capabilities against current business needs
4. **Use the audit as an EA visibility moment** — presenting findings to senior stakeholders ("here is what we already own that we haven't activated") is a high-impact, low-cost EA contribution

---

## Evolution Over Time

This pattern has been present in the vault since the LeanIX braindump (April 2026). The Informatica and Microsoft braindumps in May 2026 confirmed it as a recurring, structural pattern rather than a one-off observation. The pattern is expected to continue — it is inherent to how large enterprise software is sold and adopted.

---

*Pattern identified through consolidation of May 2026 braindumps — [[braindump-2026-05-14-1444-informatica-idmc-beyond-mdm]], [[braindump-2026-05-14-0907-microsoft-single-tenant-strategy]], [[braindump-2026-04-09-1022-leanix-learning-use-cases]]*
