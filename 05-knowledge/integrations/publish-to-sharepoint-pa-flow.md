---
type: "integration-guide"
created: "2026-06-14"
integration: "COG → SharePoint via OneDrive file drop"
skill: "publish-to-sharepoint"
tags: ["#integration", "#power-automate", "#sharepoint", "#publishing", "#onedrive"]
---

# COG → SharePoint Publish: Power Automate Setup Guide

**Approach:** COG converts a vault document to HTML and drops it in OneDrive. PA watches the folder, uploads the file to SharePoint, and deletes it.
**PA licence required:** Standard (free connectors — OneDrive + SharePoint)
**Setup time:** ~10 minutes

---

## Before You Start

- [ ] Know your SharePoint staging site URL (e.g. `https://belron.sharepoint.com/sites/YourSite`)
- [ ] Know which document library and folder to publish into (e.g. `Documents/COG`)
- [ ] OneDrive for Business (BelronGlobal) installed and syncing on your Mac
- [ ] The `COG-Publish` folder already created in your OneDrive (done automatically when the skill was set up)

---

## Step 1: Create the Flow

1. Go to **make.powerautomate.com** (sign in with your Belron account)
2. Click **+ Create** → **Automated cloud flow**
3. Name it: `COG SharePoint Publish`
4. Search for trigger: **"When a file is created"** (OneDrive for Business)
5. Click **Create**

---

## Step 2: Configure the Trigger

In the **"When a file is created"** trigger:

- **Folder**: Browse to and select `/COG-Publish`

---

## Step 3: Get File Content

Click **+ New step** → search **OneDrive for Business** → **Get file content**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename this step: `Get file content`

---

## Step 4: Upload to SharePoint

Click **+ New step** → search **SharePoint** → **Create file**.

Configure:
- **Site Address**: your SharePoint staging site URL (e.g. `https://belron.sharepoint.com/sites/YourSite`)
- **Folder Path**: the library and folder path (e.g. `/Documents/COG`)
- **File Name**: select `Name` from the trigger dynamic content
- **File Content**: select `File content` from the **Get file content** step

Rename this step: `Upload to SharePoint`

---

## Step 5: Delete the Processed File

Click **+ New step** → search **OneDrive for Business** → **Delete file**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename this step: `Delete processed file`

---

## Step 6: Save the Flow

Click **Save**. The flow is now active.

---

## Flow Summary

```
Trigger: File created in OneDrive /COG-Publish
  └── Get file content (OneDrive)
  └── Upload to SharePoint (Create file — site, folder, name, content)
  └── Delete processed file (OneDrive)
```

Three steps — the simplest PA flow in COG.

---

## Step 7: Test It

1. Create a test HTML file:
   ```html
   <html><body><h1>COG publish test</h1><p>If you can see this, the flow works.</p></body></html>
   ```
2. Save as `cog-publish-test.html` and drop into `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/`
3. Wait ~1–2 minutes
4. Check your SharePoint site — `cog-publish-test.html` should appear in the target folder
5. The file should disappear from COG-Publish

---

## Using the Skill

Once the PA flow is set up, publishing from COG is:

```
/publish-to-sharepoint
```

COG will:
1. Ask which document (or accept a file path)
2. Show a preview and ask for confirmation
3. Convert markdown → HTML (M365-styled)
4. Drop the HTML file into COG-Publish
5. Update the vault file with a publish timestamp

The file appears in SharePoint within ~1–2 minutes.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| File sits in COG-Publish unprocessed | PA flow not triggered | Check flow is on; OneDrive trigger can take 1–3 min |
| SharePoint "Create file" shows permission error | Insufficient access to the site/library | Confirm you have Contribute access to the target library |
| File uploaded but in wrong folder | Folder path misconfigured | Check Folder Path in Step 4 — must match library + subfolder exactly |
| File not deleted after upload | Delete step failed | Verify Delete file step uses trigger `Id`, not the SharePoint file ID |
| HTML looks unstyled in SharePoint | Browser previewing raw HTML | Open the file from SharePoint — it should render correctly |

---

## Updating the SharePoint Destination

The target site and folder are hard-coded in the PA flow (Step 4). To change destination:
- Edit the flow and update the Site Address and Folder Path in the Create file step
- Or create a second flow watching the same folder with a different destination and use filename prefixes to route (e.g. `ea-` prefix → EA site, `cog-` prefix → staging site)

---

*Set up: 2026-06-14 | Skill: /publish-to-sharepoint | Drop folder: ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/*
