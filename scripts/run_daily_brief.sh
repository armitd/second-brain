#!/bin/bash
# Invokes the COG daily-brief skill via Claude Code CLI.
# Runs non-interactively with permissions bypassed — safe because
# daily-brief only reads web pages and writes to the vault.

source "$HOME/.zprofile" 2>/dev/null || true
source "$HOME/.zshrc" 2>/dev/null || true

VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"

cd "$VAULT"

exec "$HOME/.local/bin/claude" \
    --dangerously-skip-permissions \
    -p "Run /daily-brief" \
    >> /tmp/cog-daily-brief.log 2>&1
