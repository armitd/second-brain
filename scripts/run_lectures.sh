#!/bin/bash
SCRIPTS="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/scripts"
source "$HOME/.zprofile" 2>/dev/null || true
source "$HOME/.zshrc" 2>/dev/null || true
source "$SCRIPTS/.venv/bin/activate"
exec python3 "$SCRIPTS/lecture_processor.py" >> /tmp/cog-lectures.log 2>&1
