# ERRORS.md — COG Failure Log

A running log of approaches that didn't work and what succeeded instead. Check before retrying a previously-attempted operation.

---

## Data Sources & Fetching

### LinkedIn posts — images not retrievable via WebFetch
- **What failed:** Attempting to retrieve embedded images or diagrams from LinkedIn post URLs via WebFetch
- **Why:** LinkedIn's page structure doesn't expose image assets to unauthenticated web fetch. The post text is usually retrievable; images are not.
- **What works:** Fetch the post text via WebFetch (usually succeeds for public posts). Note in the output that images must be added manually, and include a direct link to the original post.
- **First encountered:** 2026-05-21

### DZone articles — 403 Forbidden
- **What failed:** WebFetch on DZone article URLs returns HTTP 403 Forbidden
- **Why:** DZone blocks automated fetching
- **What works:** Search for the same content on Medium, the author's personal blog, or via WebSearch for a cached/alternative source
- **First encountered:** 2026-05-21

### AlignedNews stories — attribution error
- **What failed:** AlignedNews-sourced stories were attributed to their underlying Twitter/X source URLs rather than labeled as "AlignedNews (Tier 2)"
- **Why:** The AlignedNews MCP tool returns stories with underlying source URLs; it's easy to pass these through directly rather than noting the AlignedNews layer
- **What works:** When using `mcp__aligned-news__get_stories`, explicitly label each story as "AlignedNews (Tier 2) — [date]" in the Sources section of the brief. The underlying URL is supplementary, not the primary attribution.
- **First encountered:** 2026-05-21

---

## Vault Operations

### Readwise deduplication — file modification timestamps unreliable
- **What failed:** Using `ls -lt` modification timestamps on Readwise/ files to identify "new since last run" content
- **Why:** iCloud sync can update modification timestamps on files that haven't actually changed. A file synced after a previous session may appear newer than it is.
- **What works:** Cross-reference against the `date_processed` field in existing booklet frontmatter, or check the Readwise file's internal highlight dates, rather than relying solely on filesystem timestamps.
- **First encountered:** 2026-05-21

### Git errors — iCloud creates duplicate files inside .git/
- **What failed:** Git throwing errors / clutter from files like `.git/index 26`, `.git/index 21`, `.git/ORIG_HEAD 2` — dozens of them (76 found on 2026-07-21).
- **Why:** The vault lives in iCloud Drive **and** is a git repo, so iCloud syncs the `.git/` folder. When git rewrites `.git/index` (every commit) mid-sync, or two Macs touch it near-simultaneously, iCloud can't merge the binary file and makes conflict copies (a space + number suffix). They accumulate until git trips.
- **What works:** Delete the conflict copies — git never uses spaces in internal filenames, so any space-named file in `.git/` is an iCloud artifact and safe to remove:
  ```
  find .git -name "* *" -type f -delete
  ```
  Then verify: `git status`, `git fsck --connectivity-only`, `git log --oneline -1`. The real `.git/index`, `.git/HEAD`, `.git/ORIG_HEAD` are untouched.
- **Prevention:** Don't run git / Obsidian Git / Claude Code on two Macs at the same moment (concurrent `.git` writes are the trigger). Permanent fix would be moving `.git` out of iCloud (repo content stays synced, git internals live outside) — more involved, not yet done.
- **First encountered:** 2026-07-21

---

## Format

When adding a new entry:

```
### [Short description of what failed]
- **What failed:** [what was attempted]
- **Why:** [root cause if known]
- **What works:** [the approach that succeeded instead]
- **First encountered:** [YYYY-MM-DD]
```

---

*Maintained by COG — add entries whenever an approach fails and a working alternative is found*
