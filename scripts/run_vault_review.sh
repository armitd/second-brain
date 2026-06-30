#!/bin/bash
# Wrapper for launchd — sources shell profile so ANTHROPIC_API_KEY is available,
# activates the venv, and runs vault_review.py.

set -e

SCRIPTS="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/scripts"
VENV="$SCRIPTS/.venv"

# Source shell profile for env vars (ANTHROPIC_API_KEY lives here)
# shellcheck disable=SC1091
source "$HOME/.zprofile" 2>/dev/null || true
source "$HOME/.zshrc" 2>/dev/null || true

# Activate virtual environment
source "$VENV/bin/activate"

# Run the loop
exec python3 "$SCRIPTS/vault_review.py" >> /tmp/cog-vault-review.log 2>&1
