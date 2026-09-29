# Claude Code Integration

The Claude Code integration is defined by
`plugins/project-design/.claude-plugin/plugin.json`.

Claude Code automatically discovers `skills/*/SKILL.md` at the plugin root, so it uses the same shared skill implementation as Codex. The Claude manifest does not duplicate skills or declare a custom skills path.

No commands, agents, hooks, MCP servers, LSP servers, output styles, or
channels are included.

The repository marketplace is defined by
`.claude-plugin/marketplace.json` at the repository root. It exposes only the
isolated `plugins/project-design/` bundle and can be installed from the
private GitLab repository (access to the `globalis-ms` group required):

```bash
claude plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
claude plugin install project-design@project-design
```

To update, refresh the marketplace before the plugin:

```bash
claude plugin marketplace update project-design
claude plugin update project-design@project-design
```

Claude Code must be restarted after installation or update so the plugin is
reloaded.
