# Spec Kit Compatibility

## Compatibility Contract

- Spec Kit is optional.
- Standalone project-design behavior must remain complete.
- Shared skills must not read or write Spec Kit-specific files directly.
- Spec Kit-specific logic must remain under `integrations/spec-kit/`.
- Integration failures must not prevent standalone use.
- Mapping must preserve provenance and distinguish assumptions from decisions.

## Version 0.1.0

Compatibility is architectural and documentary only. No Spec Kit version is required, detected, installed, or supported through executable behavior.

Supported versions, artefact formats, conflict handling, and migration rules are TO BE DEFINED.
