# Claude Code Integration

The Claude Code integration is defined by
`plugins/project-design/.claude-plugin/plugin.json`.

Claude Code automatically discovers `skills/*/SKILL.md` at the plugin root, so it uses the same shared skill implementation as Codex. The Claude manifest does not duplicate skills or declare a custom skills path.

No commands, agents, hooks, MCP servers, LSP servers, output styles, or
channels are included. External Claude marketplace packaging remains TO BE
DEFINED.
