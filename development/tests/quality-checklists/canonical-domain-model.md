# Canonical Domain Model Checklist

## Corpus Evidence

- [ ] Every retained concept has at least one clear corpus example.
- [ ] Every retained concept serves multiple skills or a shared-model boundary.
- [ ] All four permanent fixtures can be described without adding unsupported
      canonical concepts.

## Concept Quality

- [ ] Every concept has one clear definition and purpose.
- [ ] Aliases do not introduce competing canonical meanings.
- [ ] Relationships explain shared semantics without defining schema
      cardinality or storage.
- [ ] Overlapping concepts are merged or their distinction is justified.
- [ ] Deferred and excluded concepts are documented with reasons.

## Separation of Concerns

- [ ] The model defines vocabulary rather than project-specific instances.
- [ ] Source provenance, confidence, validation, and contradiction handling
      remain Knowledge Model responsibilities.
- [ ] Normalization status, identity, versioning, and lifecycle remain Project
      Model responsibilities.
- [ ] Skill-specific artefacts and methodology remain outside the canonical
      model.
- [ ] Serialization, schemas, runtime behavior, and platform details are not
      introduced.

## Architecture Compatibility

- [ ] The model remains outside the processing pipeline.
- [ ] Definitions are compatible with the Information Architecture ADR.
- [ ] Every future skill can reuse the vocabulary without owning it.
- [ ] Spec Kit and other integrations can map canonical concepts without
      becoming core dependencies.
- [ ] The model remains technology-independent and methodology-independent.
