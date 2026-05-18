---
name: daybook
description: Create or open today's daybook file for capturing thoughts throughout the day
roles: [all]
integrations: []
---

# COG Daybook Skill

## Purpose
Create today's daybook file if it doesn't exist, or confirm it's ready if it does. Optionally append a thought directly. Daybooks are lightweight daily capture files — no structure, no friction. Run `/braindump` later to process what's in them.

## When to Invoke
- User types `/daybook`
- User wants to open or create their daily capture file
- User says "open daybook", "create daybook", "today's daybook"
- User provides content after the command to append immediately (e.g. `/daybook had a good meeting about X`)

## Process Flow

### 1. Get Current Date

Run `date '+%Y-%m-%d'` using Bash to get today's date. NEVER guess the date.

### 2. Check for Existing Daybook

Check whether `01-daily/daybooks/daybook-YYYY-MM-DD.md` already exists for today.

**If it already exists:**
- Confirm: "Your daybook for [date] is already open at `01-daily/daybooks/daybook-YYYY-MM-DD.md`."
- If the user provided content with the command, append it (see Step 4)
- If no content was provided, show the current contents of the daybook so the user can see what's in there
- Done

**If it does not exist:**
- Create it (Step 3)

### 3. Create the Daybook File

Create `01-daily/daybooks/daybook-YYYY-MM-DD.md` with this exact template:

```markdown
---
type: "daybook"
date: "YYYY-MM-DD"
created: "YYYY-MM-DD"
status: "open"
---

# Daybook — DD Month YYYY

<!-- Append thoughts here throughout the day. No structure needed. Run /braindump when back at desk. -->


```

Use the full date in the heading, e.g. `# Daybook — 17 May 2026`.

### 4. Append Content (if provided)

If the user typed content after `/daybook` (e.g. `/daybook just had a call with X about Y`), append that text to the daybook after the comment line. Preserve the blank line after the comment. Add the content as plain text on a new line.

Example result if user typed `/daybook just had a call about the PoC`:
```markdown
<!-- Append thoughts here throughout the day. No structure needed. Run /braindump when back at desk. -->

Just had a call about the PoC.
```

### 5. Confirm Completion

- If **created:** "Daybook created at `01-daily/daybooks/daybook-YYYY-MM-DD.md`. Append thoughts throughout the day — run `/braindump` when you're ready to process them."
- If **already existed + content appended:** "Appended to your daybook at `01-daily/daybooks/daybook-YYYY-MM-DD.md`."
- If **already existed + no content:** Show current contents and say "Ready to capture — just append thoughts here throughout the day."

## Notes
- Daybooks are intentionally unstructured — no headings, no analysis, no friction
- They are the raw input layer; `/braindump` is the processing layer
- The file stays in `status: open` until the user runs `/braindump` on it (braindump can set it to `processed`)
- Never create a daybook for a past date unless the user explicitly asks
