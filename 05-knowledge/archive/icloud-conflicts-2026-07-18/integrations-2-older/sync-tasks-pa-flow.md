---
type: "integration-guide"
created: "2026-06-14"
integration: "COG → Microsoft To Do via OneDrive file drop"
skill: "sync-tasks"
tags: ["#integration", "#power-automate", "#todo", "#tasks", "#onedrive"]
---

# COG → To Do Sync: Power Automate Setup Guide

**Approach:** COG writes a JSON file to OneDrive. PA watches the folder, reads the file, creates tasks in Microsoft To Do, deletes the file.
**PA licence required:** Standard (free connectors only — OneDrive + Microsoft To Do)
**Setup time:** ~10 minutes

> Tasks land in a dedicated To Do list. Move them to your Project plan from there if they need project tracking — everything aggregates in My Tasks in the new Planner anyway.

---

## Before You Start

- [ ] Create a list in Microsoft To Do called **COG** (or any name you prefer — just note it for Step 4)
- [ ] OneDrive for Business (BelronGlobal) installed and syncing on your Mac
- [ ] The `COG-Tasks` folder already created in your OneDrive (done automatically when the skill was set up)

---

## Step 1: Create the Flow

1. Go to **make.powerautomate.com** (sign in with your Belron account)
2. Click **+ Create** → **Automated cloud flow**
3. Name it: `COG Task Sync`
4. Search for trigger: **"When a file is created"** (OneDrive for Business)
5. Click **Create**

---

## Step 2: Configure the Trigger

In the **"When a file is created"** trigger:

- **Folder**: Browse to and select `/COG-Tasks`

---

## Step 3: Get File Content

Click **+ New step** → search **OneDrive for Business** → **Get file content**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename this step: `Get file content`

---

## Step 4: Parse the JSON

Click **+ New step** → search **Data Operation** → **Parse JSON**.

Configure:
- **Content**: select `File content` from the **Get file content** step
- **Schema**: paste this:

```json
{
  "type": "object",
  "properties": {
    "sent_at": {
      "type": "string"
    },
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "due_date": {
            "type": "string"
          },
          "bucket": {
            "type": "string"
          },
          "notes": {
            "type": "string"
          }
        }
      }
    }
  }
}
```

Rename this step: `Parse task JSON`

---

## Step 5: Add "Apply to each" Loop

Click **+ New step** → **Control** → **Apply to each**.

- **Select output from previous steps**: select `tasks` from the **Parse task JSON** dynamic content

Rename this step: `For each task`

Inside the loop, add one action:

---

### Step 5a: Create To Do Task

Inside the loop → **+ Add an action** → search **Microsoft To Do (Business)** → **Add a to-do (V3)**.

Configure:
- **List id**: select your **COG** list from the dropdown
- **Title**: select `title` from **Parse task JSON** (current item)
- **Due date time**: click the Expression tab and enter:
  ```
  if(empty(items('For_each_task')?['due_date']), null, concat(items('For_each_task')?['due_date'], 'T12:00:00Z'))
  ```
- **Body content**: click the Expression tab and enter:
  ```
  concat('[', items('For_each_task')?['bucket'], '] ', items('For_each_task')?['notes'])
  ```
  This puts `[Bucket] source file path` in the task notes so you know where it came from.

Rename: `Create To Do task`

---

## Step 6: Delete the Processed File

After the loop (outside it) → **+ New step** → **OneDrive for Business** → **Delete file**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename: `Delete processed file`

---

## Step 7: Save the Flow

Click **Save**. The flow is now active and watching the COG-Tasks folder.

---

## Step 8: Test It

1. Copy this JSON and save it as `test.json`
2. Drop it into `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/`
3. Wait ~1–2 minutes
4. Check your COG list in To Do — "COG sync test" should appear with notes `[Inbox] Test task — delete me`
5. The file should disappear from COG-Tasks

```json
{
  "sent_at": "2026-06-14T12:00:00",
  "tasks": [
    {
      "title": "COG sync test",
      "due_date": "2026-06-21",
      "bucket": "Inbox",
      "notes": "Test task — delete me"
    }
  ]
}
```

---

## Flow Summary

```
Trigger: File created in OneDrive /COG-Tasks
  └── Get file content (OneDrive)
  └── Parse task JSON (Data Operation)
  └── For each task:
        └── Add a to-do (Microsoft To Do — title, due date, bucket + source in notes)
  └── Delete processed file (OneDrive)
```

Four steps. No bucket routing logic needed — tasks land in your COG list and you promote to Project from there.

---

## Workflow After Sync

1. `/sync-tasks` in COG → tasks appear in your **COG** To Do list within ~2 minutes
2. Review in To Do (or in **My Tasks** in the new Planner, which aggregates everything)
3. For anything needing project tracking → drag/move it into your Project plan from My Tasks

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| File sits in COG-Tasks unprocessed | PA flow not triggered | Check flow is turned on; OneDrive trigger can take 1–3 min |
| "Microsoft To Do (Business)" not visible | Using personal account | Ensure you're signed into PA with your Belron M365 account |
| COG list not appearing in dropdown | List not created yet | Create the list in To Do first, then refresh PA |
| Task created with no due date | `due_date` field empty in JSON | Expected — task created without a due date |
| File not deleted after processing | Delete step is inside the loop | Move the Delete file step outside (after) the Apply to each loop |

---

*Set up: 2026-06-14 | Skill: /sync-tasks | Drop folder: ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/*
Can you 