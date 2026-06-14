---
name: publish-to-sharepoint
description: Publish a vault document to SharePoint as a PDF via OneDrive file drop — converts markdown to PDF and drops to OneDrive; Power Automate uploads to SharePoint
roles: [all]
integrations: ["sharepoint"]
---

# COG Publish to SharePoint Skill

## Purpose
Convert a COG vault document to PDF and publish it to SharePoint via OneDrive drop. Power Automate picks up the file and uploads it to SharePoint. The SharePoint link can then be shared via Teams or email.

## When to Invoke
- User says "publish to SharePoint", "push to SharePoint", "share this", "send to SharePoint"
- After generating a knowledge article, daily brief, braindump, or framework worth sharing

## Drop Folder
```
~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/
```

## Dependency
PDF conversion requires `md-to-pdf` (Node.js tool using headless Chrome).

**Check if installed:**
```bash
which md-to-pdf
```

**If not installed** — tell the user:
```
md-to-pdf is required for PDF generation. Install it once with:

  npm install -g md-to-pdf

Then re-run /publish-to-sharepoint.
```
Stop until installed.

---

## Process Flow

### Step 1: Get Timestamp
```bash
date '+%Y-%m-%d %H:%M'
```

### Step 2: Check Dependency
```bash
which md-to-pdf || echo "NOT FOUND"
```
If not found, show install instruction above and stop.

### Step 3: Check Drop Folder
```bash
ls ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/ 2>/dev/null || mkdir -p ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/
```

### Step 4: Identify the Document

**If user specified a file path:** use it directly.

**If user described the document** (e.g. "the Composio braindump", "today's brief"):
Search these locations:
- `01-daily/briefs/`
- `04-projects/*/braindumps/`
- `05-knowledge/`
- `03-professional/braindumps/`
- `02-personal/braindumps/`

Present up to 5 candidates and let the user choose.

### Step 5: Derive Output Filename

From the document's H1 heading:
- Lowercase, spaces to hyphens, strip special characters
- Append the date: `title-slug-YYYY-MM-DD.pdf`
- Example: `composio-agent-infrastructure-2026-06-14.pdf`

### Step 6: Approval Gate

**Never proceed without explicit confirmation.**

```
Ready to publish to SharePoint:

  Document: [source vault path]
  Title:    [H1 heading]
  Output:   [filename].pdf
  Via:      OneDrive → COG-Publish → SharePoint (PA flow)

Publish? (yes/no)
```

Wait for explicit confirmation. If no, stop.

### Step 7: Convert to PDF

`md-to-pdf` writes the PDF next to the source file. To keep the vault clean, copy the source to `/tmp` first, convert there, then move the PDF to OneDrive:

```bash
mkdir -p /tmp/cog-publish
cp "[full path to source .md file]" /tmp/cog-publish/[source-filename].md
cd /tmp/cog-publish && md-to-pdf [source-filename].md --highlight-style github
```

This creates `/tmp/cog-publish/[source-filename].pdf`.

Verify the PDF was created:
```bash
ls -lh /tmp/cog-publish/
```

If the command fails, report the error output to the user and stop.

### Step 8: Copy to Drop Folder

```bash
cp /tmp/cog-publish/[source-filename].pdf \
   ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/[output-filename].pdf
```

Verify:
```bash
ls -lh ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/
```

### Step 9: Update Vault Frontmatter

Add to the source file's frontmatter:
```yaml
sharepoint_published_at: "YYYY-MM-DD HH:MM"
sharepoint_filename: "[filename].pdf"
```

### Step 10: Confirm

```
✅ Published to SharePoint drop folder.

  File: [filename].pdf
  Size: [size]

Power Automate will upload to SharePoint in ~1–2 minutes.
Share the SharePoint link via Teams or email once it appears.
```

---

## Error Handling

| Situation | Response |
|---|---|
| `md-to-pdf` not installed | Show install command, stop |
| Drop folder missing | Create with `mkdir -p`, then proceed |
| PDF conversion fails | Show error output, do not copy to drop folder |
| File already exists in drop folder | Warn that PA may not have processed a previous file; ask to proceed |
| Source file not found | List candidate files and ask user to choose |

---

## Notes
- `md-to-pdf` strips YAML frontmatter automatically — no pre-processing needed
- The PDF is generated from the raw markdown; Obsidian `[[links]]` appear as plain text
- PA deletes the file from COG-Publish after uploading to SharePoint — if it persists, check PA flow run history
- The skill records the filename but not the SharePoint URL (PA knows the final URL)
- See `05-knowledge/integrations/publish-to-sharepoint-pa-flow.md` for the PA setup guide
