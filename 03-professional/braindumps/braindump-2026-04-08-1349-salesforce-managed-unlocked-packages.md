---
type: "braindump"
domain: "professional"
date: "2026-04-08"
created: "2026-04-08 13:49"
themes: ["Salesforce", "packages", "managed packages", "unlocked packages", "DevOps", "enterprise architecture"]
tags: ["#braindump", "#professional", "#Salesforce", "#packages", "#DevOps", "#EA"]
status: "researched"
energy_level: "medium"
emotional_tone: "curious/investigative"
confidence: "high"
---

# Braindump: Salesforce Managed vs Unlocked Packages

## Raw Thoughts
Look at managed / unlocked packages in Salesforce.

---

## Research Primer

Salesforce has three main package types. Understanding the distinction is important for any EA governing a Salesforce environment.

---

### The Three Package Types

| | Unmanaged | Managed | Unlocked |
|---|---|---|---|
| **Purpose** | One-time install, open code | AppExchange distribution | Internal org development |
| **Code visible?** | Yes | No (locked) | Yes |
| **Editable after install?** | Yes | No | Yes |
| **Source-control driven?** | No | No | Yes (Salesforce DX) |
| **Versioned?** | No | Yes | Yes |
| **Upgradeable?** | No | Yes (by publisher) | Yes (by your team) |
| **Who uses it** | Quick installs, templates | ISVs, AppExchange vendors | Enterprise development teams |

---

### Managed Packages

**What they are:** The traditional packaging model. Code and configuration are bundled, versioned, and distributed — but the internals are locked. Purchasers/installers cannot see or edit the underlying Apex, components, or logic.

**Use case:** Building a product to sell or distribute on AppExchange. ISVs (Independent Software Vendors) use managed packages to protect IP and push controlled upgrades to customers.

**EA implication:** If your company buys solutions from AppExchange (e.g., a document generation tool, a telephony integration), those arrive as managed packages. You can configure them but not modify them. Any gaps between what the package does and what you need require either customisation around the edges or a different product.

**Key constraint:** Components inside a managed package cannot be modified. If a managed package creates a custom object or field, you cannot change its core behaviour — only extend around it.

---

### Unlocked Packages

**What they are:** The modern, source-control-driven development model for teams building Salesforce solutions *for their own org*. Introduced with Salesforce DX (2nd Generation Packaging / 2GP). Metadata is version-controlled in Git, packages are deployed via Salesforce CLI, and the code remains fully visible and editable.

**Use case:** Internal enterprise development. Breaking a large, complex Salesforce org into modular, independently deployable units — each as an unlocked package.

**Why it matters for enterprise orgs:**
- Large Salesforce orgs that have grown organically over years ("org soup") have tangled, untestable metadata. Unlocked packages let you start modularising incrementally without needing to untangle everything at once
- Each package has a defined dependency chain, making change impact clearer
- Enables proper CI/CD pipelines: test → package → deploy → release, like modern software
- Teams can work independently on different packages without stepping on each other

**Org-dependent unlocked packages:** A variant that allows packages to depend on metadata that lives directly in the org (rather than in another package). Useful for large legacy orgs where untangling all dependencies upfront is impractical — you can start packaging the new work while leaving legacy metadata in place.

---

### The EA Lens: Which Applies Here?

**For Belron/your company's Salesforce org, the relevant question is:**

1. **Are you buying solutions?** → You're dealing with managed packages (AppExchange). Understand what's locked and what can be configured; design around the edges carefully.

2. **Are you building internal solutions?** → Unlocked packages are the right model. If your org is still being deployed via change sets or metadata API without source control, migrating to unlocked packages is a significant but worthwhile architectural investment.

3. **Is there a mix?** → Almost certainly yes. The architecture question is: which capabilities live in managed packages (bought), which in unlocked packages (built internally), and where are the integration points?

---

## Strategic Intelligence

### Key Insights

1. **Unlocked packages are the enterprise standard for Salesforce development in 2026.** Change sets are legacy. If your Salesforce team is still deploying via change sets, moving to unlocked packages + source control is the single highest-leverage technical improvement available.

2. **Managed vs unlocked is a buy-vs-build decision in disguise.** Managed = buy (or use as-is). Unlocked = build and own. This maps directly to the Wardley Mapping framework from this morning — understand where each capability sits on the evolution axis before deciding which model to use.

3. **Governance of the package landscape is an EA responsibility.** In large orgs, you can end up with multiple teams building unlocked packages with unclear dependencies, naming conflicts, and no overall architecture. The EA role is to own the package architecture — what packages exist, what they contain, how they depend on each other, and who owns each.

### Questions to Investigate
- Does your company use Salesforce? If so, what's the current deployment model — change sets, managed packages, unlocked packages, or a mix?
- Is there a package architecture in place, or is it "org soup"?
- Are there AppExchange managed packages in use, and are they creating constraints on your architecture?
- Is the Salesforce team using source control (Git) for their metadata?

---

## Action Items

### Immediate (24–48 hours)
- [ ] Find out what deployment model your Salesforce team currently uses (change sets / metadata API / unlocked packages) 📅 2026-04-10
- [ ] Identify which AppExchange managed packages are installed in your org and what they own 📅 2026-04-10

### Short-term (1–2 weeks)
- [ ] Read the Salesforce DX / unlocked packages documentation to understand the package development model in depth 📅 2026-04-18
- [ ] If the org uses change sets: assess the effort and benefit of migrating to unlocked packages — this is a significant but impactful EA recommendation 📅 2026-04-22

### Strategic Considerations
- Package architecture in Salesforce is the same problem as capability ownership across the enterprise — it just happens to have a technical implementation. The EA lens (who owns what, where are the boundaries, what depends on what) applies directly
- This connects to the CCOTF/front-office capability overlap braindump — if both CCOTF and front-office touch Salesforce, understanding the package boundaries tells you a lot about where the capability overlap lives technically

---

## Key Resources
- [Salesforce Ben — Unlocked Packages: Comprehensive Guide](https://www.salesforceben.com/unlocked-packages-in-salesforce-a-comprehensive-guide-for-developers/)
- [Salesforce Developers — Unlocked Packages official docs](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)
- [Metazoa — Breaking Your Org Into Packages](https://www.metazoa.com/best-practices-breaking-your-org-into-packages/)
- [DevOps Launchpad — Bringing DevOps to Salesforce with package development](https://devopslaunchpad.com/blog/bringing-devops-to-salesforce-with-package-development/)
- [Noltic — Managed and Unmanaged Packages guide](https://noltic.com/stories/managed-and-unmanaged-packages-in-salesforce)

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — if Salesforce spans both CCOTF and front-office, package boundaries reveal the technical shape of the capability overlap
- **Related braindump:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — managed vs unlocked is a buy-vs-build decision; Wardley Mapping is the framework to make it

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** private

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 91% — well-sourced from Salesforce official docs and community
- **Package type definitions:** 97% — standard Salesforce documentation
- **Company-specific application:** 70% — depends on how Salesforce is actually used at Belron; needs investigation

---

*Processed by COG Braindump Analyst*
