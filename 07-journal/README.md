---
type: "index"
tags: ["#journal", "#index"]
---

# 07 Journal

Capture-only musings, thoughts, and reflections. Titled notes I keep and refer back to — **not** actionable, **not** processed.

## What goes here
- Reflections, musings, half-formed thoughts, things I want to remember thinking
- Usually captured via **speech-to-text** straight into a new note (iPhone / iPad / Mac)
- Each note has a **title** so I can find it again later

## What does NOT go here
- Actionable capture → that belongs in the **Daybook** (`01-daily/daybooks/`), which `/braindump` processes into tasks
- Journal notes are deliberately **outside the action pipeline**: `/braindump`, `/process-daybook`, and `/sync-tasks` never touch this folder

## Convention
- **Filename:** `YYYY-MM-DD-short-title-slug.md` (date prefix sorts them; title makes them findable)
- **Frontmatter:** `title`, `date`, `type: journal`, optional `tags`
- Copy `_template.md` for a new entry, or just dictate into a fresh note and give it a title

## Sources feeding this folder
- **`/create-journal`** — dictate/type a musing straight in
- **Day One import** — export from Day One (Markdown/JSON) into `00-inbox/raw/dayone-import/`, then ask COG to "process my Day One export". Entries land here date-stamped by their **original entry date** with `source: "dayone"`. See [[00-inbox/raw/dayone-import/README]].

## Later — optional, my choice
- `/vault-review` can resurface old journal entries for reflection
- `/knowledge-consolidation` can surface themes across them — only if I explicitly ask

*This is a keep-and-reflect layer, not a to-do layer. Nothing here implies an action.*
