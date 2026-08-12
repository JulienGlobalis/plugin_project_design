# Claude Code Integration

The Claude Code integration is defined by
`plugins/project-design/.claude-plugin/plugin.json`.

Claude Code automatically discovers `skills/*/SKILL.md` at the plugin root, so it uses the same shared skill implementation as Codex. The Claude manifest does not duplicate skills or declare a custom skills path.

No commands, agents, hooks, MCP servers, LSP servers, output styles, or
channels are included.

The repository marketplace is defined by
`.claude-plugin/marketplace.json` at the repository root. It exposes only the
isolated `plugins/project-design/` bundle and can be installed from GitHub:

```bash
claude plugin marketplace add JulienGlobalis/plugin_project_design
claude plugin install project-design@project-design
```

Claude Code must be restarted after installation or update so the plugin is
reloaded.
