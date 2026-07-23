# Knowledge Model Checklist

## Model Boundary

- [ ] Assertions preserve extracted or explicitly interpreted knowledge
      without establishing normalized project truth.
- [ ] Project normalization, conflict resolution, generated artefacts, skill
      methodology, schemas, persistence, and runtime behavior remain outside
      the model.
- [ ] Every Knowledge Model construction is clearly distinguished from the
      Canonical Domain Model vocabulary.

## Assertions and Canonical References

- [ ] Every assertion preserves one independently qualifiable meaning.
- [ ] Every assertion references only applicable canonical concepts using
      their exact version 0.1 meaning.
- [ ] Multiple canonical references are justified by the assertion content.
- [ ] Unmapped source language is retained or raised as a recommendation
      rather than converted into a new canonical concept.

## Provenance and Epistemic State

- [ ] Every assertion cites a source artefact and precise location, or a
      clearly bounded reviewed-corpus scope.
- [ ] Source date, version, role, authority, and context are preserved when
      known and remain unknown when unavailable.
- [ ] Nature distinguishes Fact, Interpretation, Assumption, Proposal,
      Decision, and Open Question.
- [ ] Confidence assesses extraction or interpretation and includes a
      rationale; it is not treated as probability of truth.
- [ ] Uncertainty is explicit and does not invent missing information.
- [ ] Validation status remains distinct from confidence, source authority,
      and truth.

## Coexistence and Evolution

- [ ] Materially different assertions about the same concern coexist.
- [ ] Assertion Groups support comparison without selecting a winner or
      creating a Project Model instance.
- [ ] Supports, Contradicts, Equivalent, Refines, and Supersedes relationships
      are explicit and context-qualified.
- [ ] Contradictions preserve every side and are not resolved automatically.
- [ ] Supersession is supported by evidence rather than inferred from recency
      alone.
- [ ] Rejected and superseded assertions retain provenance and history.
- [ ] Absence from supplied material is expressed as a corpus-scoped
      interpretation, not as a universal fact.

## Architecture and Corpus Compatibility

- [ ] All four permanent fixtures can represent incomplete, conflicting,
      uncertain, evolving, and unknown information without premature
      resolution.
- [ ] End-to-end traceability can continue from a future Project Model element
      through assertions to source locations.
- [ ] The model remains technology-independent, storage-independent,
      methodology-independent, and platform-independent.
- [ ] Spec Kit remains an optional downstream integration.
- [ ] No Canonical Domain Model concept or definition is added, removed, or
      modified.
