---
type: "braindump"
domain: "professional"
date: "2026-06-30"
created: "2026-06-30 08:18"
themes: ["cog-maintenance", "launchd", "api-key"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#cog-maintenance"]
status: "consolidated"
energy_level: "medium"
emotional_tone: "neutral"
confidence: "high"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: COG launchd fixes pending

## Raw Thoughts

Two fixes needed for the COG launchd automation once corporate Anthropic API key is provisioned:

1. Corp Anthropic API key not yet available — waiting on provisioning. Once received, add it to the launchd shell scripts that run Python-based COG jobs. Affected scripts: `~/.cog/run_vault_review.sh`, `~/.cog/run_articles.sh`, `~/.cog/run_lectures.sh` — all use `ANTHROPIC_API_KEY` env var which launchd doesn't inherit from the shell.

2. "Operation not permitted" errors on `Second Brain/scripts/run_*.sh` — duplicate copies of the runner scripts exist inside the vault. Something is attempting to execute them but failing, likely missing execute permissions. Need to investigate what's calling them and either grant execute permissions or remove the duplicates if they're vestigial.

## Action Items

### Immediate (once corp key arrives)
- [ ] Export `ANTHROPIC_API_KEY` in `~/.cog/run_vault_review.sh`, `run_articles.sh`, and `run_lectures.sh` 📅 2026-07-07

### Short-term
- [ ] Investigate what is calling `Second Brain/scripts/run_*.sh` and fix "Operation not permitted" — either `chmod +x` those scripts or remove them if vestigial 📅 2026-07-07

## Context
- Vault-review launchd job (`com.cog.vault-review`) currently exits with code 1 — ANTHROPIC_API_KEY not set
- Daily-brief is running fine (ran at 08:14 on 2026-06-30)
- Scripts in `Second Brain/scripts/` appear to be duplicates of `~/.cog/` runner scripts

## Connections
- **Related Projects:** COG maintenance

---

*Processed by COG Brain Dump Analyst*
