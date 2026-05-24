---
type: "braindump"
domain: "professional"
project: ""
date: "2026-05-17"
created: "2026-05-20 13:52"
source_daybook: "01-daily/daybooks/daybook-2026-05-17.md"
themes: ["microsoft-copilot", "m365", "data-placement", "notebooks", "governance"]
tags: ["#braindump", "#raw-thoughts", "#microsoft", "#copilot", "#m365", "#governance", "#data-residency"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-24]]"
consolidated_date: "2026-05-24"
energy_level: "low"
emotional_tone: "curious"
confidence: "medium"
---

# Braindump: Where Does M365 Copilot Put Notebooks?

## Raw Thoughts
Understand where Copilot 265 is putting Notebooks.

*(Note: "Copilot 265" = Microsoft 365 Copilot — voice/daybook capture artefact)*

---

## Content Analysis

### Main Themes
1. **Copilot artifact placement**: Where do Copilot-generated pages, notebooks, and outputs land in the M365 topology (SharePoint, OneDrive, Loop)?
2. **Governance implications**: Artifact placement determines who can see it, whether it's covered by retention policies, and how eDiscovery works
3. **Single tenant context**: This question is sharper in a multi-tenant world — cross-tenant Copilot artifacts are harder to govern than intra-tenant ones

### Supporting Ideas
- Microsoft 365 Copilot creates several types of persistent artifacts: Copilot Pages (shared BizChat outputs), meeting recaps (stored in OneDrive), Loop components, and potentially named Notebooks in Copilot Notebook (preview feature)
- The storage location varies by product surface: Teams meeting recap → initiator's OneDrive; BizChat / Copilot Pages → SharePoint or shared OneDrive depending on sharing action; Loop → Loop workspaces backed by SharePoint
- From a governance perspective, "where it puts things" matters for: retention labels applying automatically, DLP policies triggering on sensitive content, eDiscovery coverage, and Multi-Geo data residency compliance
- This question likely surfaced because of an observed behaviour — Copilot put something somewhere unexpected, or a user asked where their Copilot outputs went

### Questions Raised
- Which specific "Notebooks" surface triggered this question? (Copilot Notebook feature? OneNote integration? Loop Notebooks? Teams meeting notebook?)
- Are Copilot-created artifacts being picked up by existing retention and DLP policies, or are they falling outside them?
- In a multi-tenant Belron environment, can Copilot Pages be shared across tenant boundaries — and if so, where does the shared copy live?
- Is there a Microsoft documentation source that maps each Copilot surface to its backing storage location?

### Decisions Contemplated
- Whether to formally audit which Copilot artifact types are in use and map their storage destinations before any tenant consolidation work begins
- Whether existing M365 retention policies need updating to explicitly cover Copilot-generated content types

---

## Strategic Intelligence

### Key Insights

1. **Copilot artifact placement is an unresolved governance gap for most M365 organisations.** Microsoft introduced several Copilot surfaces (BizChat, Teams Copilot, Copilot Pages, Loop) with different backing stores. Most organisations' retention and DLP policies predate Copilot and do not explicitly cover these content types. This is a governance risk — especially if Copilot is being used in meetings where sensitive business information is discussed.

2. **This question directly extends the single tenant strategy work.** The May 14 analysis concluded that a single tenant unlocks full Copilot intelligence across the group. But "where does Copilot put things" is the governance complement to that architectural question — you need to know the storage topology before you can confidently say your compliance controls cover Copilot outputs.

3. **The answer is surface-specific, not uniform.** There is no single answer to "where does Copilot put notebooks" — it depends on which surface was used. A systematic mapping (surface → backing store → retention policy coverage) would be a useful one-page reference for the EA function.

### Pattern Recognition
- **Connection to Previous Thinking:** The Microsoft Single Tenant braindump ([[braindump-2026-05-14-0907-microsoft-single-tenant-strategy]]) identified Copilot governance as a benefit of single tenant. This thought is the next step: before governing Copilot output, you need to know where it lives.
- **Recurring Patterns:** The "where does it put things" question appears repeatedly in enterprise AI adoption — it was the same question for Teams chat retention (is Teams chat covered by Exchange retention?), and now repeats for Copilot artifacts.
- **Evolution:** The AI governance surface area is expanding faster than existing policy frameworks. Copilot content needs to be treated as a new content class, not assumed to be covered by SharePoint or Exchange policies.

### Strategic Implications
- Any work on the Microsoft tenant strategy (whether pre-IPO decision or post-IPO programme) should include a Copilot content governance workstream
- If Belron is already rolling out M365 Copilot to any opco, a quick audit of artifact placement and retention coverage should happen before broader rollout
- The answer to this question should feed into the architecture options paper (due 2026-05-21 from the single tenant braindump action items)

---

## Action Items

### Immediate (24-48 hours)
- [ ] Look up the Microsoft documentation mapping each Copilot surface to its backing storage location (SharePoint, OneDrive, Loop, Exchange) 📅 2026-05-21

### Short-term (1-2 weeks)
- [ ] Check whether current Belron M365 retention and DLP policies explicitly cover Copilot content types (Copilot Pages, Loop components, Teams meeting recaps) 📅 2026-05-27
- [ ] Add a "Copilot artifact placement and retention" section to the architecture options paper 📅 2026-05-27

### Strategic Considerations
- This is a pre-work item for any Copilot rollout — answer the placement question before more users create ungoverned AI-generated content
- Worth a short conversation with the M365 admin team (or Microsoft TAM if Belron has one) to understand current retention policy coverage

---

## Connections
- **Related Braindumps:** [[braindump-2026-05-14-0907-microsoft-single-tenant-strategy]], [[braindump-2026-04-09-0934-ea-copilot-agent]]
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW]]
- **Knowledge Base:** [[03-professional/COMPETITIVE-WATCHLIST|Microsoft AI (Azure OpenAI + Copilot)]]

---

## Domain Classification
- **Primary Domain:** Professional (90%)
- **Reasoning:** M365 governance question directly relevant to Belron EA function and active Microsoft tenant strategy work
- **Cross-Domain Elements:** None
- **Privacy Level:** Internal

## Processing Notes

### Emotional Context
- **Energy Level:** Low — a fleeting observation captured in a daybook, not a sustained reflection
- **Emotional Tone:** Curious — a question surfaced by something observed or heard, not a decision under pressure
- **Implications:** Something prompted this question — either a user complaint, a demo, or reading about Copilot features. Worth a short investigation before the single tenant architecture paper is due

### Confidence Assessment
- **Overall Analysis:** 70% — the storage topology assessment is directionally correct based on public Microsoft documentation, but Belron's specific configuration and current Copilot rollout state are unknown
- **Domain Classification:** 90% — unambiguously professional EA and M365 governance
- **Strategic Insights:** 75% — the governance gap insight is well-grounded; specifics depend on what Microsoft has shipped since the knowledge cutoff
- **Areas Requiring Clarification:** Which specific Copilot Notebooks surface triggered the daybook note; current state of Copilot rollout at Belron

---

*Processed by COG Brain Dump Analyst*
