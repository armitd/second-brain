---
type: "memory-hygiene-report"
date: "2026-07-18"
created: "2026-07-18 08:20"
sweep_scope: "agent-memory (empty) + 05-knowledge (targeted: environment-heavy notes + structural scan)"
tags: ["#memory-hygiene", "#trust-sweep", "#cog"]
status: "resolved"
---

> **Resolution (2026-07-18): all four fixes applied + memory store seeded.**
> 1. ✅ Restored `publish-to-sharepoint-pa-flow.md` to `05-knowledge/integrations/` — broken link now resolves.
> 2. ✅ Corrected Readwise counts in `MY-INTEGRATIONS.md` (articles 21, books 79, threads 190).
> 3. ✅ Archived 21 iCloud conflict files to `05-knowledge/archive/icloud-conflicts-2026-07-18/` (all verified identical or older-subset; none hard-deleted). The `integrations 2/sync-tasks` copy was an older subset of the canonical note — archived.
> 4. ✅ Removed the empty `integrations 2/` folder. Zero conflict files/dirs remain.
> 5. ✅ Seeded the previously-empty agent memory store with 4 entries (2 feedback, 1 project, 1 reference) + `MEMORY.md` index.

# Memory Hygiene Sweep — 18 July 2026

First sweep since installing the `memory-hygiene` skill (v3.7.1). Nothing has been auto-changed: this run is **report + proposals only**, because every proposed action is a file move, archive, or config edit — all of which are hard-stop / propose-only under COG's rules.

## 1. What persists?

| Store | State |
|---|---|
| **Agent memory** (`~/.claude/projects/.../memory/`) | **Empty — does not exist yet.** No memories have been saved. Nothing to verify. |
| **Durable knowledge** (`05-knowledge/**`) | 348 markdown notes. This sweep targeted the **environment-dependent** notes (setup + integration flows) and ran a **structural duplicate scan** across all of them. The bulk (patterns, consolidations, research, booklets) are judgment/strategy notes carrying few environment claims, so they were not individually stamped this pass. |

## 2. What updated?

**Nothing auto-applied.** All corrections are proposed below and await your go-ahead (see §5).

## 3. What is measured? (scorecard)

| Metric | Count |
|---|---|
| Environment claims verified clean | 3 (OneDrive `COG-Publish/`, OneDrive `COG-Tasks/`, `sync-tasks-pa-flow.md` link) |
| **Drifted (verified wrong)** | **4** (3 Readwise counts + 1 broken setup-guide link) |
| **Structural drift — iCloud conflict duplicates** | **20 `" 2.md"` files + 1 `integrations 2/` folder** |
| Propose-archive | 20 duplicate files (2 confirmed identical, rest pending per-file diff) |
| Propose-restore | 1 file (only copy sits in a conflict folder) |

*No previous sweep exists, so no trend delta yet. This report is the baseline; the next sweep will diff against it.*

## Findings in detail

### 🔴 Drift A — Readwise counts are stale (stale-but-confident)
`00-inbox/MY-INTEGRATIONS.md` states counts that no longer match the vault:

| Claim in file | Actual now | Delta |
|---|---|---|
| "20 saved articles" | **21** | +1 |
| "66 books" | **79** | +13 |
| "75 threads" | **190** | +115 |

The thread count is badly out of date. These are exactly the descriptions an agent would quote confidently while being wrong. *(Note: this file lives in `00-inbox/`, outside the sweep's core scope, so I'm flagging rather than editing.)*

### 🔴 Drift B — broken setup-guide link + orphaned unique file
`MY-INTEGRATIONS.md` links `[[05-knowledge/integrations/publish-to-sharepoint-pa-flow]]`, but that file **does not exist** at the canonical path. Its **only copy** lives in the iCloud conflict folder `05-knowledge/integrations 2/publish-to-sharepoint-pa-flow.md`. So the link is dead and the real content is stranded in a conflict folder. This one must be **restored**, not deleted.

### 🟠 Structural drift — 20 iCloud conflict duplicates
20 `"<name> 2.md"` files across `05-knowledge/` (setup notes, one consolidation, one framework, and ~16 booklets). Sampled two (`how-i-work-with-cog`, `cog-setup-overview`) — **byte-identical** to their originals and ~15 min newer (classic iCloud sync fork). Safe to archive after a per-file identical-check.

### 🟢 Verified clean
- OneDrive drop-folders `COG-Publish/` and `COG-Tasks/` both exist.
- `sync-tasks-pa-flow.md` exists at its canonical linked path.

## 4. What is auditable?
This report is the audit trail for the sweep (the memory store isn't Git-tracked in the usual way, and the vault's auto-backup bundles changes into generic commits). Every proposed change is listed here with its evidence.

## 5. Propose — waiting on you

I will not touch anything until you confirm. Options, in priority order:

1. **Restore the stranded file** — move `integrations 2/publish-to-sharepoint-pa-flow.md` → `integrations/publish-to-sharepoint-pa-flow.md` (fixes the broken link). *Recommended.*
2. **Fix the Readwise counts** in `MY-INTEGRATIONS.md` (articles 21, books 79, threads 190). Low-risk factual correction.
3. **Archive the 20 duplicate `" 2.md"` files** — I'd diff each against its original first; identical ones move to an `archive/` folder (never hard-deleted), any that differ get surfaced to you individually.
4. **Remove the now-empty `integrations 2/` folder** after (1) and (3).

**Waiting on you:** which of 1–4 should I action? "All" is fine, or pick a subset.
