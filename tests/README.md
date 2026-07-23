# Validation and Tests

Version 0.1.0 uses structural validation only:

- Validate `.codex-plugin/plugin.json` with the installed Codex plugin validator.
- Validate `.claude-plugin/plugin.json` with the installed Claude Code CLI in strict mode.
- Validate every `skills/*/SKILL.md` with the skill-creator validator.
- Check for unresolved scaffold placeholders.
- Check that core skills contain no Spec Kit runtime dependency.
- Check that no runtime package, hook, command, custom agent, or MCP server is present.

Detailed methodology tests, fixtures, forward tests, and integration tests are TO BE DEFINED.
