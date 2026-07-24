# Shared Quality Rules

## Status

IMPLEMENTED - common verification contract version 0.1.

This directory defines common quality principles and traceability rules.
Skill-specific criteria remain in each implemented skill and will expand as
the remaining methodologies are defined.

Under the accepted
[common information architecture](../project-model/information-architecture.md),
the Knowledge Model distinguishes:

- Fact
- Interpretation
- Assumption
- Proposal
- Decision
- Open Question

Version 0.1 of these responsibilities, including provenance, confidence,
uncertainty, validation, and assertion relationships, is defined in the
[Minimal Knowledge Model](../knowledge-model/README.md).

The shared models and future methodologies must prohibit unsupported
invention, preserve source traceability, and prevent unresolved assumptions
from being represented as validated decisions.

Version 0.1 of the
[Minimal Normalized Project Model](../project-model/README.md) distinguishes
Established, Provisional, and Unresolved project information; Existing,
Target, and Transition perspectives; and Supporting, Qualifying, and Opposing
Knowledge Basis links.

Canonical meanings for Assumption, Option, Decision, and Open Question are
defined in the
[Canonical Domain Model](../terminology/canonical-domain-model.md). Fact,
Interpretation, and epistemic Proposal classification remain Knowledge Model
responsibilities.

## Common Verification Contract

Every installable methodology must:

- support material statements with source evidence or an explicit Knowledge
  Basis;
- preserve provenance and material opposing evidence;
- keep Established, Provisional, and Unresolved information distinct;
- keep Existing, Target, and Transition perspectives distinct;
- preserve unresolved contradictions until sufficient evidence and authority
  support a resolution;
- keep canonical distinctions such as Assumption, Option, Decision, Risk,
  Issue, Need, Requirement, Stakeholder, and Actor;
- avoid inventing owners, dates, measures, priorities, Constraints,
  Requirements, Business Rules, or Decisions;
- make missing information and uncertainty visible without treating source
  absence as proof that information does not exist;
- keep generated statements traceable through normalized project information
  and extracted knowledge to source artefacts;
- remain within the responsibility and downstream boundaries of the invoked
  skill.

Localized outputs must use the preferred terminology for the requested
language while preserving canonical distinctions. The initial mapping and
fallback rules are defined by the
[French terminology companion](../terminology/canonical-terms.fr.md).

Each implemented skill must keep its methodology-level quality contract inside
its installable directory. Development tests validate these contracts but are
not runtime dependencies.
