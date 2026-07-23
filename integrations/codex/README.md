# Codex Integration

The Codex integration is defined by `.codex-plugin/plugin.json`. The manifest explicitly references the shared root `skills/` directory and adds no runtime dependency.

The shared `SKILL.md` files use only the cross-platform `name` and `description` front-matter fields. Codex-specific UI metadata is intentionally not embedded inside those skill directories in version 0.1.0 so the skill implementation remains platform-independent.

Plugin marketplace distribution, installation policy, product gating, icons, screenshots, and hosted metadata are TO BE DEFINED. No personal or repository marketplace entry is created in this iteration.
