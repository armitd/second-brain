---
name: publish-to-sharepoint
description: Publish a vault document to SharePoint via OneDrive file drop — converts markdown to HTML and drops to OneDrive; Power Automate uploads to SharePoint
roles: [all]
integrations: ["sharepoint"]
---

# COG Publish to SharePoint Skill

## Purpose
Convert a COG vault document to clean HTML and publish it to a SharePoint document library via OneDrive drop. Power Automate picks up the file and uploads it to SharePoint automatically. No Graph API token required.

## When to Invoke
- User says "publish to SharePoint", "push to SharePoint", "share this", "send to SharePoint"
- After generating a knowledge article, daily brief, braindump, or framework document worth sharing

## Drop Folder
```
~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/
```
Power Automate watches this folder. Files dropped here are uploaded to SharePoint and then deleted.

---

## Process Flow

### Step 1: Get Timestamp
Run `date '+%Y-%m-%d %H:%M'` to get the current timestamp.

### Step 2: Identify the Document

**If user specified a file path:** read it directly.

**If user described the document** (e.g. "the Composio braindump", "today's brief"):
Search these locations for likely matches:
- `01-daily/briefs/`
- `04-projects/*/braindumps/`
- `05-knowledge/`
- `03-professional/braindumps/`
- `02-personal/braindumps/`

Present up to 5 candidates and let the user choose. Read the chosen file.

### Step 3: Derive Output Filename

Generate a filename from the document's H1 heading:
- Lowercase, spaces to hyphens, strip special characters
- Append the date: `title-slug-YYYY-MM-DD.html`
- Example: `composio-agent-infrastructure-2026-06-14.html`

### Step 4: Approval Gate

**Never drop a file without explicit confirmation.**

Show:
```
Ready to publish to SharePoint:

  Document: [source vault path]
  Title:    [H1 heading]
  Filename: [output filename].html
  Via:      OneDrive → COG-Publish → SharePoint (PA flow)

Content preview:
[first 200 characters of body content, stripped of markdown]

Publish? (yes/no)
```

Wait for explicit confirmation. If no, stop.

### Step 5: Convert Markdown to HTML

Strip YAML frontmatter entirely. Convert the body using these rules:

| Markdown | HTML |
|---|---|
| `# H1` | `<h1>` |
| `## H2` | `<h2>` |
| `### H3` | `<h3>` |
| `**bold**` | `<strong>` |
| `*italic*` | `<em>` |
| `- item` | `<ul><li>` |
| `1. item` | `<ol><li>` |
| `- [ ] task` | `<li>☐ task</li>` |
| `- [x] task` | `<li>☑ task</li>` |
| `[text](url)` | `<a href="url">text</a>` |
| `` `code` `` | `<code>` |
| ```` ```block``` ```` | `<pre><code>` |
| `> quote` | `<blockquote>` |
| `---` | `<hr>` |
| `\| table \|` | `<table>` with `<th>` first row |
| `[[link]]` | plain text (strip brackets) |
| `📅 YYYY-MM-DD` | strip (task date emojis) |
| `#tag` | strip |

Wrap in this template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>[H1 HEADING]</title>
  <style>
    body { font-family: Segoe UI, sans-serif; max-width: 900px; margin: 2rem auto; line-height: 1.6; color: #323130; }
    h1 { font-size: 2rem; border-bottom: 2px solid #0078d4; padding-bottom: 0.5rem; }
    h2 { font-size: 1.4rem; color: #0078d4; margin-top: 2rem; }
    h3 { font-size: 1.1rem; }
    table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
    th { background: #0078d4; color: white; padding: 8px 12px; text-align: left; }
    td { border: 1px solid #edebe9; padding: 8px 12px; }
    tr:nth-child(even) { background: #f3f2f1; }
    code { background: #f3f2f1; padding: 2px 6px; border-radius: 3px; font-family: Consolas, monospace; }
    pre { background: #f3f2f1; padding: 1rem; border-radius: 4px; overflow-x: auto; }
    blockquote { border-left: 4px solid #0078d4; margin: 0; padding: 0.5rem 1rem; background: #f3f2f1; }
    .meta { color: #605e5c; font-size: 0.85rem; margin-bottom: 1.5rem; }
  </style>
</head>
<body>
  <p class="meta">Published from COG vault · [DATE]</p>
  [CONVERTED CONTENT]
</body>
</html>
```

### Step 6: Write to Drop Folder

Write the HTML file to:
```
~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/[filename].html
```

Verify the file was written:
```bash
ls -lh ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/
```

### Step 7: Update Vault Frontmatter

Add to the source file's frontmatter:
```yaml
sharepoint_published_at: "YYYY-MM-DD HH:MM"
sharepoint_filename: "[filename].html"
```

### Step 8: Confirm

```
Published to SharePoint drop folder.

  File: [filename].html
  Size: [size]

Power Automate will upload to SharePoint in ~1–2 minutes.
Vault updated with publish timestamp.
```

---

## Error Handling

| Situation | Response |
|---|---|
| Drop folder missing | Create with `mkdir -p ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/`, then proceed |
| File already exists in drop folder | Warn: PA may not have processed a previous file yet. Proceed anyway? |
| Source file not found | List candidate files and ask user to choose |
| User says no at approval gate | Stop. Do not write any files. |

---

## Notes
- The converted HTML is styled with Segoe UI and Microsoft blue (#0078d4) to match M365 visual conventions
- PA deletes the file from COG-Publish after uploading to SharePoint — if the file persists, check the PA flow run history
- The skill does not know the final SharePoint URL; only the filename is recorded in vault frontmatter
- See `05-knowledge/integrations/publish-to-sharepoint-pa-flow.md` for the PA setup guide
