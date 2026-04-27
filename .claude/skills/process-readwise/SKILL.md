---
name: process-readwise
description: Scan Readwise vault for unprocessed content and file it into the second brain knowledge base
roles: [all]
integrations: []
---

# COG Process Readwise Skill

## Purpose
Ingest unprocessed Readwise content — articles, tweets, books, full document captures — and file them into the appropriate second brain location. Readwise is the primary raw sources layer; this skill is the bridge between raw capture and structured knowledge.

## When to Invoke
- User says "process readwise", "sync readwise", "file my readwise", "ingest readwise"
- User wants to process recently saved content from Readwise
- Scheduled cron run (automated weekly processing)

## Pre-Flight Check

**Get current timestamp (REQUIRED before generating any files):**
1. Run `date '+%Y-%m-%d %H:%M'` using Bash
2. Store this value for all `created:` frontmatter fields

**Read user profile:**
- Read `00-inbox/MY-PROFILE.md` for active projects and user name
- Read `00-inbox/MY-INTERESTS.md` for topics — used to assess relevance and route content
- Read `03-professional/COMPETITIVE-WATCHLIST.md` if it exists — flag any competitive intel found in Readwise content

## Process Flow

### 1. Discover Unprocessed Content

Scan all Readwise source folders for content not yet filed in `05-knowledge/`:

```
Readwise/Articles/                         → target: 05-knowledge/booklets/articles/
Readwise/Tweets/                           → target: 05-knowledge/booklets/tweets/ (or braindump if substantive)
Readwise/Full Document Contents/Tweets/    → target: 05-knowledge/booklets/tweets/
Readwise/Full Document Contents/Articles/  → supplement existing article entries
Readwise/Books/                            → target: 05-knowledge/booklets/books/
```

**Deduplication check:** For each Readwise item, check whether a corresponding file already exists in `05-knowledge/booklets/` by matching on title (fuzzy) or source URL. Skip already-processed items silently.

**Batch size:** Process up to 20 items per run to avoid overwhelming the session. If more are unprocessed, report the count and ask whether to continue or stop.

**Report to user before processing:**
```
Found [X] unprocessed items in Readwise:
- Articles: [count]
- Tweets: [count]  
- Books: [count]
- Full document captures: [count]

Processing up to 20. Continue?
```

### 2. Classify Each Item

For each unprocessed item, determine:

| Signal | Classification |
|--------|---------------|
| `Category: #articles` in metadata | Article → booklets/articles/ |
| `Category: #tweets`, single tweet or short highlights | Tweet note → booklets/tweets/ |
| `Category: #tweets`, substantive thread with ideas | Braindump candidate — flag for user |
| `Category: #books` | Book → booklets/books/ |
| Full Document Contents/Tweets/ | Thread capture → booklets/tweets/ |
| Full Document Contents/Articles/ | Supplement article entry, don't duplicate |

**Relevance scoring against MY-INTERESTS.md:**
- **High relevance** (topics match directly): Process fully, file to booklets
- **Low relevance** (no topic match): File with minimal processing — title, author, URL, one-line summary only. Don't invest in deep analysis.
- **Project relevance** (relates to active project): Note in output and add `related_projects` tag

### 3. Generate Output Files

#### Articles → `05-knowledge/booklets/articles/[slug]-YYYY-MM-DD.md`

```markdown
---
type: "readwise-article"
category: "articles"
source: "readwise"
source_readwise: "Readwise/Articles/[original-filename]"
date_processed: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
title: "[title]"
author: "[author]"
url: "[url from metadata]"
tags: ["#readwise", "#article", "#[topic-tag]"]
relevance: "[high|medium|low]"
related_projects: []
status: "processed"
---

# [Title]

## Summary
[2-3 sentence summary based on highlights and full document if available]

## Key Highlights
[Extract the most substantive highlights from the Readwise file — up to 5]
- [Highlight 1]
- [Highlight 2]
- [Highlight 3]

## Why It Matters
[1-2 sentences on relevance to interests or active projects — omit if low relevance]

## Source
- **Author:** [author]
- **Saved to Readwise:** [date if available]
- **Full text:** [[Readwise/Full Document Contents/Articles/[filename]|Full document →]] *(if exists)*

---
*Processed from Readwise by COG*
```

#### Tweets → `05-knowledge/booklets/tweets/[author-slug]-YYYY-MM-DD.md`

```markdown
---
type: "readwise-tweet"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Tweets/[original-filename]"
date_processed: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
author: "[twitter handle]"
tags: ["#readwise", "#tweet", "#[topic-tag]"]
relevance: "[high|medium|low]"
related_projects: []
status: "processed"
---

# Tweets: [Author Name]

## Highlights
[Each saved tweet highlight as a bullet]
- [Tweet text] ([View Tweet](url))
- [Tweet text] ([View Tweet](url))

## Why These Were Saved
[One sentence on the apparent pattern or theme across these saves — omit if single tweet]

---
*Processed from Readwise by COG*
```

For **full thread captures** (`Full Document Contents/Tweets/`):

```markdown
---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/[filename]"
date_processed: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
title: "[thread topic]"
author: "[author]"
tags: ["#readwise", "#thread", "#[topic-tag]"]
relevance: "[high|medium|low]"
related_projects: []
status: "processed"
---

# Thread: [Title/Topic]

## Summary
[2-3 sentence summary of the thread's argument or content]

## Key Points
- [Point 1]
- [Point 2]
- [Point 3]

## Why It Matters
[Relevance to interests or projects]

## Full Thread
[[Readwise/Full Document Contents/Tweets/[filename]|Full thread →]]

---
*Processed from Readwise by COG*
```

#### Books → `05-knowledge/booklets/books/[slug]-YYYY-MM-DD.md`

```markdown
---
type: "readwise-book"
category: "books"
source: "readwise"
source_readwise: "Readwise/Books/[original-filename]"
date_processed: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
title: "[title]"
author: "[author]"
tags: ["#readwise", "#book", "#[topic-tag]"]
relevance: "[high|medium|low]"
related_projects: []
status: "processed"
---

# [Book Title] — [Author]

## What It's About
[1-2 sentence description]

## Key Highlights
[Up to 7 most substantive highlights from the Readwise file]
- [Highlight 1]
- [Highlight 2]

## Why It Matters
[Relevance to interests or active projects — omit if low relevance]

## Full highlights
[[Readwise/Books/[filename]|All highlights →]]

---
*Processed from Readwise by COG*
```

### 4. Competitive Intelligence Check

If `COMPETITIVE-WATCHLIST.md` exists:
- Scan each processed item for mentions of tracked companies or people
- If found, note it in the output file's frontmatter: `competitive_intel: true`
- Report to user: "Found competitive intel mentions in [X] items — review flagged files"

### 5. Braindump Candidates

Some Readwise content — particularly substantive tweet threads with original ideas — is better captured as a professional braindump than a filed tweet note. Flag these rather than auto-filing:

```
[Thread title] by [author] looks substantive enough to braindump rather than just file.
Want me to process it as a braindump instead? (y/n)
```

Criteria for flagging as braindump candidate:
- Full thread capture with >500 words of original thinking
- Content directly relevant to an active project
- Contains a framework, model, or structured argument (not just news)

### 6. Report Completion

After processing, report:

```
Readwise processing complete.

Filed:
- [X] articles → 05-knowledge/booklets/articles/
- [X] tweet notes → 05-knowledge/booklets/tweets/  
- [X] thread captures → 05-knowledge/booklets/tweets/
- [X] books → 05-knowledge/booklets/books/

Flagged:
- [X] braindump candidates (substantive threads)
- [X] competitive intel mentions

Skipped:
- [X] already processed
- [X] low relevance (filed with minimal processing)

[If more items remain:]
[Y] items remain unprocessed. Run again to continue.
```

## Scheduling (Optional)

To run automatically, use `CronCreate` to schedule this skill weekly:
- Suggested cadence: Sunday morning, before or after the weekly check-in
- The cron prompt should be: "Run the process-readwise skill — scan Readwise/ for unprocessed content and file to 05-knowledge/booklets/"

## YAML Formatting Requirements

All frontmatter must use Obsidian-compatible formatting:
- All string values quoted with double quotes
- Arrays use quoted strings: `["item1", "item2"]`
- Boolean values unquoted: `true` or `false`

## Design Principles

- **Don't over-process low-relevance content.** A tweet from someone you follow about an unrelated topic gets a minimal entry — title, author, URL. Not every Readwise save deserves deep analysis.
- **Preserve the link back to Readwise.** Always include `source_readwise` frontmatter so the original is traceable.
- **Flag, don't decide.** When something could be a braindump, ask rather than auto-file in the wrong place.
- **Batch deliberately.** 20 items per run keeps sessions manageable. Quality over quantity.
- **Never delete from Readwise/.** These are immutable raw sources. COG only reads them, never modifies or removes them.

---
*COG Process Readwise Skill — bridges raw Readwise capture to structured second brain knowledge*
