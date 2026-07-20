---
type: "braindump"
domain: "professional"
date: "2026-07-20"
created: "2026-07-20 16:00"
themes: ["readwise", "cog-pipeline", "newsletter-ingestion", "knowledge-infrastructure", "exponential-view"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#cog", "#readwise"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Auto-save Exponential View into Readwise → COG

## Raw Thoughts
How to get my Exponential View newsletter subscription auto saved to Readwise for onward consumption in COG.

## The pipeline (what you're building)

```
Exponential View email
   → [mail auto-forward rule]
      → Readwise Reader FEED email (@feed.readwise.io)
         → Readwise → Obsidian sync
            → Readwise/ vault folder
               → /process-readwise
                  → 05-knowledge/booklets/articles/
```

This slots straight into COG's existing convention: Readwise is the primary raw-sources layer; `/process-readwise` is the bridge into the knowledge base.

## Content Analysis

### The key decision: email-forward, NOT RSS (because you're a paying subscriber)
- Exponential View is partly **paywalled**. Substack's RSS feed only serves the **public/preview** portion of paid posts, so an RSS route would truncate the very issues you pay for.
- The **email** you receive contains the **full issue**. So the right method is to get the *email* into Readwise. RSS is only the better choice if you just want free public posts.

### Readwise Reader has TWO email addresses (this trips people up)
- **Library email** (`…@readwise.io`) — for one-off "send me this, I'll read it" documents.
- **Feed email** (`…@feed.readwise.io`) — for **auto-forwarding rules and newsletter subscriptions**. This is the one you want.
- Find/personalise it in Reader: Account Settings → Email (mobile), or the "Add to Library / import options" page (web). Per Readwise's own guidance, use the *feed* email for auto-forwarding.

### Two ways to route the email
1. **Auto-forward rule (recommended — keeps your existing subscription):** create a filter in your mail client (Gmail/Outlook) that forwards anything from the Exponential View sender to your `@feed.readwise.io` address. Reader auto-clicks the confirmation link; if Gmail asks for a confirmation code, Reader emails it to your inbox to complete setup.
2. **Subscribe with the feed email directly:** re-subscribe to the newsletter using the feed email. Simpler, but you'd be managing the subscription from Readwise rather than your normal inbox — the forward rule is usually cleaner when you're already subscribed.

### The last mile into the vault (the real gotcha)
Getting it into Readwise Reader is only half the job — it then has to land in the `Readwise/` vault folder for COG to see it. The Readwise → Obsidian export historically syncs **highlights**, so a newsletter you never highlight may not appear. Two fixes:
- **Enable Reader-document sync** in the Readwise Official Obsidian plugin settings (sync documents, not just highlights), **or**
- **Highlight at least one line** in each issue in Reader, which forces it into the export.

Then `/process-readwise` files new issues into `05-knowledge/booklets/articles/`.

### Questions Raised
- Which mail client holds the Exponential View subscription — Gmail, Outlook/M365, or a personal address? (Determines the exact forward-rule steps.)
- Is your Readwise → Obsidian sync currently highlights-only, or already set to pull Reader documents? (This decides whether you need the highlight workaround.)
- Do you want **every** issue auto-ingested, or only ones you choose to save? Auto-forward = everything; manual save = curated.

### Decisions Contemplated
- Email-forward vs RSS (resolved: email, because paid content).
- Auto-forward rule vs re-subscribe with feed email (leaning: forward rule).
- Auto-ingest all issues vs curate (leaning: auto-ingest, then let `/process-readwise` + the Hive lens triage).

## Strategic Intelligence

### Key Insights
1. **The paywall is the whole reason RSS fails here.** For any *paid* newsletter, the email route is the only one that captures full content. Worth making this the default rule for all your paid subscriptions, not just Exponential View.
2. **Reader's feed-vs-library email split is the setup detail that makes or breaks auto-ingestion.** Use the feed address for the forward rule.
3. **The Readwise→Obsidian "highlights-only" default is the silent failure point.** Everything can work in Reader and still never reach COG. Fix the sync setting once and the pipeline runs itself.

### Pattern Recognition
- **Connects to the raw-sources convention** in [[llm-wiki-knowledge-infrastructure-framework]] and CLAUDE.md: external content → Readwise → `Readwise/` → COG. This is that pattern applied to a specific high-value feed.
- **Connects to the subscription-audit thread** [[braindump-2026-06-30-0914-subscriptions-alignednews]] — you're consolidating your intake into one pipeline (Readwise → COG) rather than scattered inboxes.
- **Repeatable pattern:** once this works for Exponential View, the same recipe covers any newsletter (TBD, Every.to, etc.).

### Strategic Implications
- Exponential View (Azeem Azhar: AI + exponential tech) is squarely on your interests and a strong **Hive** candidate source — once in COG, `/process-readwise` plus the Hive curation lens will surface post-worthy items automatically.
- One-time setup, then hands-off: every issue flows to the vault without manual saving.

## Action Items

### Immediate (24-48 hours)
- [ ] Grab your Readwise Reader **feed email** (`…@feed.readwise.io`) from Reader → Account Settings → Email 📅 2026-07-21
- [ ] Create a mail forward rule: from the Exponential View sender → your feed email; confirm the forward 📅 2026-07-21

### Short-term (1-2 weeks)
- [ ] Check the Readwise Official Obsidian plugin: enable **Reader-document sync** (not highlights-only) so newsletters reach `Readwise/` 📅 2026-07-27
- [ ] Wait for the next issue, confirm it lands in `Readwise/`, then run `/process-readwise` to file it into `booklets/articles/` 📅 2026-07-27
- [ ] Add Exponential View to `MY-INTERESTS.md` sources (and note the Readwise pipeline in `MY-INTEGRATIONS.md`) 📅 2026-07-27

### Strategic Considerations
- Make "forward paid newsletters to the Readwise feed email" the standard for all subscriptions worth keeping.
- If a future issue is podcast-only, note that's a separate Substack feed (the podcast RSS is distinct from the newsletter).

## Connections
- **Related Braindumps:** [[braindump-2026-06-30-0914-subscriptions-alignednews]] (subscription/tooling audit)
- **Knowledge Base:** [[llm-wiki-knowledge-infrastructure-framework]] (raw-sources layer)
- **Skill:** `/process-readwise` — files Readwise content into the knowledge base
- **Config:** [[00-inbox/MY-INTEGRATIONS]] (Readwise), [[00-inbox/MY-INTERESTS]]
- **Source:** https://www.exponentialview.co

## Domain Classification
- **Primary Domain:** Professional (90%)
- **Reasoning:** COG knowledge-pipeline / tooling setup; the content itself (AI/exponential tech) is professional interest. Minor personal-productivity overlap.
- **Privacy Level:** internal

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — practical setup task.
- **Emotional Tone:** Curious / pragmatic.

### Confidence Assessment
- **Overall Analysis:** 90% — Readwise Reader's email-newsletter mechanics are confirmed from Readwise's own docs; the paywall/RSS point is a known Substack behaviour.
- **Areas Requiring Clarification:** your specific mail client, and whether your Readwise→Obsidian sync already includes Reader documents. Also confirm your exact `@feed.readwise.io` address from your account.
- **Sources:** [Readwise — Email Newsletters](https://docs.readwise.io/reader/docs/faqs/email-newsletters) · [Readwise — Feed (RSS, Newsletters)](https://docs.readwise.io/reader/docs/faqs/feed) · [Exponential View](https://www.exponentialview.co/)

---

*Processed by COG Brain Dump Analyst*
