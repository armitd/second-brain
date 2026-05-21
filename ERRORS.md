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
