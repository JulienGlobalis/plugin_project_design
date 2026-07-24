# Codex Integration

The Codex integration is defined by
`plugins/project-design/.codex-plugin/plugin.json`. The manifest references
the `skills/` directory inside the isolated plugin bundle and adds no external
runtime dependency.

The shared `SKILL.md` files use only the cross-platform `name` and `description` front-matter fields. Codex-specific UI metadata is intentionally not embedded inside those skill directories in version 0.1.0 so the skill implementation remains platform-independent.

The repository marketplace entry is defined in
`.agents/plugins/marketplace.json` and points only to
`plugins/project-design/`. External publication, product gating, icons,
screenshots, and hosted metadata remain TO BE DEFINED.
