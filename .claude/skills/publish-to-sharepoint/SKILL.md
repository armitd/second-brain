---
name: publish-to-sharepoint
description: Publish any vault document to a SharePoint document library so Microsoft Copilot can find and reference it
roles: [all]
integrations: []
---

# COG Publish to SharePoint Skill

## Purpose
Upload a COG vault document to a SharePoint document library so it is indexed by Microsoft Copilot Business Chat and accessible to M365 colleagues. Handles Markdown conversion, approval gate, and vault metadata update.

## When to Invoke
- User says "publish to SharePoint", "push to SharePoint", "share with Copilot", "send to M365"
- After generating a framework, project overview, or reference architecture that should be searchable in Copilot
- When a COG document needs to be accessible to M365 colleagues without a Confluence instance

## Process Flow

### 1. Get Timestamp and Check Auth

Run `date '+%Y-%m-%d %H:%M'` using Bash.

Check for a Microsoft Graph access token:

```bash
# Check environment variable first
echo $M365_GRAPH_TOKEN
```

**If token missing or not set:** Guide the user through device code authentication (see Authentication section below). Do not proceed without a valid token.

### 2. Identify the Source Document

**If user specified a file:** Read it directly.

**If user described the document:** Search vault for likely matches:
- `04-projects/*/PROJECT-OVERVIEW.md`
- `05-knowledge/consolidated/*.md`
- `05-knowledge/research/*.md`
- `01-daily/briefs/*.md`

Present candidates and let the user choose.

### 3. Configure Publishing Target

Ask (if not already provided):

```
Where should this be published in SharePoint?

- SharePoint site URL: e.g. https://belron.sharepoint.com/sites/EnterpriseArchitecture
- Library: Document library name (default: "Documents")
- Folder: Optional subfolder path (e.g. "COG/Frameworks")
- Filename: Defaults to the document's H1 heading + .html
```

**Read `MY-INTEGRATIONS.md`** — if a SharePoint integration is configured with a default site URL, use that as the default.

### 4. Convert Markdown to HTML

Convert the vault document to clean HTML for SharePoint rendering and Copilot indexing:

**Pre-processing:**
- Strip YAML frontmatter entirely
- Remove Obsidian internal links `[[...]]` — convert to plain text or skip
- Remove Obsidian task emojis `📅` if they clutter the output
- Preserve checkboxes as `☐` (incomplete) and `☑` (complete)

**HTML template:**
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
  <p class="meta">Published from COG vault | [DATE]</p>
  [CONVERTED CONTENT]
</body>
</html>
```

**Conversion rules:**
| Markdown | HTML |
|----------|------|
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
| `\| table \|` | `<table>` |
| `[[link]]` | plain text (strip brackets) |
| YAML frontmatter | strip entirely |

### 5. Approval Gate

**NEVER upload without explicit user approval.**

Present a summary:

```
Ready to publish to SharePoint:

Document: [source filename]
Title: [H1 heading]
Site: [SharePoint site URL]
Library: [library name]
Folder: [folder path or root]
Filename: [output filename].html
Estimated size: [word count] words

Content preview (first 300 chars):
[preview]

Proceed? (yes/no)
```

Wait for explicit confirmation.

### 6. Upload via Microsoft Graph API

Use the Graph API to upload the HTML file to SharePoint:

```bash
# Build the upload URL
# Format: https://graph.microsoft.com/v1.0/sites/{hostname}:{site-path}:/drive/root:/{folder}/{filename}:/content

SITE_HOSTNAME="belron.sharepoint.com"
SITE_PATH="/sites/EnterpriseArchitecture"
FOLDER="COG/Frameworks"
FILENAME="document-name.html"

UPLOAD_URL="https://graph.microsoft.com/v1.0/sites/${SITE_HOSTNAME}:${SITE_PATH}:/drive/root:/${FOLDER}/${FILENAME}:/content"

curl -X PUT "${UPLOAD_URL}" \
  -H "Authorization: Bearer ${M365_GRAPH_TOKEN}" \
  -H "Content-Type: text/html" \
  --data-binary @/tmp/cog_sharepoint_upload.html
```

**Build the upload steps:**
1. Write converted HTML to `/tmp/cog_sharepoint_upload.html` using Bash
2. Construct the Graph API URL from the site URL, library, folder, and filename
3. Run the curl upload command
4. Parse the response for the file `webUrl`

**Handle the site URL parsing:**
- Input: `https://belron.sharepoint.com/sites/EnterpriseArchitecture`
- Hostname: `belron.sharepoint.com`
- Site path: `/sites/EnterpriseArchitecture`

### 7. Confirm and Update Vault

After successful upload:

**Confirm to user:**
```
Published to SharePoint!

File: [filename].html
URL: [webUrl from Graph API response]
Library: [library]
Copilot: This document is now indexed and searchable in Copilot Business Chat.
```

**Update the source vault file's frontmatter:**
```yaml
sharepoint_url: "[webUrl]"
sharepoint_site: "[site URL]"
sharepoint_published_at: "[timestamp]"
```

---

## Authentication Setup

### First-Time Setup (Device Code Flow)

If `M365_GRAPH_TOKEN` is not set, guide the user through one-time setup:

**Step 1 — Get a device code:**
```bash
curl -X POST "https://login.microsoftonline.com/common/oauth2/v2.0/devicecode" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=14d82eec-204b-4c2f-b7e8-296a70dab67e&scope=https://graph.microsoft.com/Files.ReadWrite.All https://graph.microsoft.com/Sites.ReadWrite.All"
```

*Note: `14d82eec-204b-4c2f-b7e8-296a70dab67e` is Microsoft's public Graph Explorer client ID — no app registration needed.*

**Step 2 — User action:**
```
Open this URL in your browser: https://microsoft.com/devicelogin
Enter this code: [user_code from response]
Sign in with your Belron Microsoft account.
```

**Step 3 — Poll for the token:**
```bash
curl -X POST "https://login.microsoftonline.com/common/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=urn:ietf:params:oauth2:grant-type:device_code&client_id=14d82eec-204b-4c2f-b7e8-296a70dab67e&device_code=[device_code]"
```

**Step 4 — Store the token:**
Instruct the user to add to their shell profile (`~/.zshrc`):
```bash
export M365_GRAPH_TOKEN="[access_token]"
```

**Token expiry:** Microsoft Graph tokens expire after ~1 hour. For a longer-lived solution, suggest setting up `/update-config` to store refresh token handling, or re-authenticate when needed.

### Adding SharePoint to MY-INTEGRATIONS.md

After first successful publish, suggest adding to `MY-INTEGRATIONS.md`:

```markdown
**SharePoint / Microsoft Graph**
- Default site: https://belron.sharepoint.com/sites/EnterpriseArchitecture
- Default library: Documents
- Default folder: COG
- Auth: Bearer token via env var `M365_GRAPH_TOKEN`
```

---

## Fallback Behaviour

| Scenario | Action |
|----------|--------|
| No Graph token | Guide through device code auth before proceeding |
| Upload fails (403) | User may lack write permission to the library — check site permissions |
| Upload fails (404) | Site URL, library, or folder path may be wrong — verify and retry |
| Token expired | Re-run device code flow; remind user to update `~/.zshrc` |
| Very large file (>4MB) | Use Graph API chunked upload session instead |
| No SharePoint configured | Ask user for site URL; offer to save to MY-INTEGRATIONS.md |

---

## Design Principles

- **Approval gate is mandatory** — never upload without explicit confirmation
- **COG is source of truth** — SharePoint is a read layer for Copilot; always update from COG, never the reverse
- **Clean HTML for Copilot** — HTML is better indexed by Copilot than raw Markdown; the styling matches M365 visual conventions
- **Update vault frontmatter** — the SharePoint URL in the vault file closes the loop: you know what's published and where
- **One-time auth, then invisible** — after the first device code setup, publishing should be a single command with no friction

## Integration with Other Skills

- **Runs after:** `/knowledge-consolidation`, `/generate-prd`, `/generate-release-notes` — any skill that produces a shareable document
- **Pairs with:** `/publish-to-confluence` — use SharePoint for M365 environments, Confluence for Atlassian environments
- **Updates:** `MY-INTEGRATIONS.md` on first successful use
