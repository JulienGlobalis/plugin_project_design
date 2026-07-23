# Shared Terminology

The [Canonical Domain Model](canonical-domain-model.md) defines version 0.1 of
the common business vocabulary shared by the Knowledge Model, Project Model,
and every future skill.

The canonical model is conceptual and technology-independent. It does not
define project instances, schemas, serialization, provenance, confidence,
validation state, or methodology.

## Localized Terminology

The English canonical names and definitions remain the normative semantic
contract. Localized terminology companions provide presentation labels,
allowed variants, and usage guidance without changing canonical meaning.

Available companions:

- [French canonical terminology](canonical-terms.fr.md)

Localized terminology follows:

```text
canonical-terms.<language-code>.md
canonical-terms.<regional-language-code>.md
```

Resolution prefers an exact regional language and then its base language. If
no requested-language resource exists, the missing localization must be
explicit. English is the default when no output language is requested and may
be used as a requested-language fallback only through an explicit rule or
user acceptance. Never silently select an unrelated localized language.

Project-specific Domain Terms remain governed by source material and an
approved project glossary. A canonical terminology companion must not
translate them automatically.

Stable implementation identifiers and conflict-resolution policy remain TO
BE DEFINED.
