# GitHub Spec Kit Integration Boundary

GitHub Spec Kit is an optional orchestration and implementation framework. It does not own or define the `project-design` methodology.

## Standalone Mode

`project-design` must remain fully usable without Spec Kit. Users may invoke the orchestrator, any specialized skill, or any explicit subset of skills. Core skills, shared resources, templates, assets, and schemas must not require Spec Kit commands, files, templates, repository layout, or an active Spec Kit project.

## Companion Mode

The plugin may eventually prepare or enrich independent project artefacts before or alongside a Spec Kit workflow. Potential relationships with `/speckit.specify`, `/speckit.plan`, and `/speckit.tasks` are future use cases and are not implemented in version 0.1.0.

## Integration Mode

A future optional adapter may map structured `project-design` artefacts to Spec Kit artefacts:

```text
project-design methodology
        |
        v
structured project artefacts
        |
        v
optional Spec Kit adapter
        |
        v
Spec Kit workflow
```

The dependency flows only from `integrations/spec-kit/` toward Spec Kit. Core skills must never depend directly on Spec Kit structures.

Automatic command execution, installation, template modification, synchronization, and runtime artefact conversion are not included. Detailed integration behavior is TO BE DEFINED.
