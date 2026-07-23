# Shared Project Model

UNDER CONSTRUCTION

The repository has accepted a layered
[common information architecture](information-architecture.md):

```text
Source documents
        |
        v
Knowledge Model
        |
        v
Project Model
        |
        v
Skills and generated artefacts
```

The Project Model will represent normalized project information shared by all
specialized skills. It will preserve links to supporting, qualifying, and
opposing extracted knowledge without owning source extraction, conflict
evidence, skill methodology, or generated presentation.

Its upstream evidence contract is version 0.1 of the
[Minimal Knowledge Model](../knowledge-model/README.md).

Its concepts must use the
[Canonical Domain Model](../terminology/canonical-domain-model.md), which
defines shared meaning without becoming part of the processing pipeline.

The architecture and upstream evidence model are defined. Project Model
responsibilities, normalization state, identity, relationships, validation
rules, and serialization remain TO BE DEFINED.
