# I want to debunk the claim that I see a...

![rw-book-cover](https://pbs.twimg.com/profile_images/1527701676521672707/YXvJP3ac.jpg)

## Metadata
- Author: [[Tiago Forte]]
- Full Title: I want to debunk the claim that I see a...
- Category: #tweets
- Summary: I want to debunk the claim that I see a lot around here that Obsidian is "just plain text markdown files" which means "you can take them anywhere and open them with any app"

That simply isn't true

Yes, maybe the raw text of the notes is markdown, but many other parts cannot be moved elsewhere and opened by other apps:

1. The .obsidian/ directory contains your JSON config with plugins, settings, hotkeys, workspace state, link format, attachment paths – those can't be moved elsewhere

2. Plugin state files – Readwise's path-to-ID map, Templater's settings, Tasks plugin's database, Excalidraw's drawing data – even if plugins can be recreated, these settings cannot

3. .canvas files – JSON, not markdown. They reference notes by path and won't survive a move

4. .base files – JSON-based database/views over your notes. Same path-fragility

5. .excalidraw.md files – markdown wrapper around an Excalidraw JSON blob. Looks like markdown, isn't really

6. The link graph itself – backlinks, graph view, "linked mentions" – all computed from filenames and link references. They survive because the references are in the markdown, but they require Obsidian (or an Obsidian-aware tool) to materialize

7. Plugin-managed folders – Readwise output, Web Clipper output, Daily Notes location, Templates folder. Each is a folder whose contents are owned by an external system tracked in plugin state

8. Sync state – Obsidian Sync, iCloud, Dropbox, Google Drive each maintain their own state about what's where and what's been resolved. Move operations interfere with this state

9. Embedded query results – Dataview queries, Tasks queries, Bases queries. The query is in the markdown; the result is computed live and never persisted

So technically you CAN move your files elsewhere, but you'd destroy most of what makes them valuable – the graph, the plugin state, the canvases, the embedded queries, the sync state, and any structural intent encoded in folder placement

Which means you're just a...
- URL: https://twitter.com/fortelabs/status/2050536278798533103/?rw_tt_thread=True

## Full Document
I want to debunk the claim that I see a lot around here that Obsidian is "just plain text markdown files" which means "you can take them anywhere and open them with any app"

That simply isn't true

Yes, maybe the raw text of the notes is markdown, but many other parts cannot be moved elsewhere and opened by other apps:

1. The .obsidian/ directory contains your JSON config with plugins, settings, hotkeys, workspace state, link format, attachment paths – those can't be moved elsewhere
2. Plugin state files – Readwise's path-to-ID map, Templater's settings, Tasks plugin's database, Excalidraw's drawing data – even if plugins can be recreated, these settings cannot
3. .canvas files – JSON, not markdown. They reference notes by path and won't survive a move
4. .base files – JSON-based database/views over your notes. Same path-fragility
5. .excalidraw.md files – markdown wrapper around an Excalidraw JSON blob. Looks like markdown, isn't really
6. The link graph itself – backlinks, graph view, "linked mentions" – all computed from filenames and link references. They survive because the references are in the markdown, but they require Obsidian (or an Obsidian-aware tool) to materialize
7. Plugin-managed folders – Readwise output, Web Clipper output, Daily Notes location, Templates folder. Each is a folder whose contents are owned by an external system tracked in plugin state
8. Sync state – Obsidian Sync, iCloud, Dropbox, Google Drive each maintain their own state about what's where and what's been resolved. Move operations interfere with this state
9. Embedded query results – Dataview queries, Tasks queries, Bases queries. The query is in the markdown; the result is computed live and never persisted

So technically you CAN move your files elsewhere, but you'd destroy most of what makes them valuable – the graph, the plugin state, the canvases, the embedded queries, the sync state, and any structural intent encoded in folder placement

Which means you're just as locked in to Obsidian as any other "proprietary" app, it's just a hidden lock-in that's obscured by inaccurate marketing

Saying "Obsidian is just markdown files" is like saying "your house is just bricks" 

The bricks are real and moveable – but the architecture, plumbing, and wiring aren't bricks, and those are most of what makes the house function
