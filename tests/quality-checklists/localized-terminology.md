# Localized Terminology Checklist

## Canonical Integrity

- [ ] Every localized canonical entry maps to one exact Canonical Domain Model
      concept.
- [ ] All 22 canonical concepts are covered exactly once.
- [ ] Localized labels do not add, remove, merge, split, or redefine concepts.
- [ ] The English Canonical Domain Model remains the normative semantic source.
- [ ] Knowledge Model and Project Model labels are clearly identified as
      non-canonical.

## Language Quality

- [ ] Every canonical concept has one preferred localized label.
- [ ] Allowed variants preserve canonical meaning.
- [ ] Usage notes identify high-risk translation collisions.
- [ ] Stakeholder and Actor remain distinguishable.
- [ ] Need and Requirement remain distinguishable.
- [ ] Option and Decision remain distinguishable.
- [ ] Risk and Issue remain distinguishable.
- [ ] Project-specific Domain Terms are not translated without source or
      glossary authority.

## Resolution and Fallback

- [ ] The resource follows `<asset-name>.<language-code>.<extension>`.
- [ ] Exact regional language resolves before the base language.
- [ ] Missing localized terminology is explicit.
- [ ] English fallback requires an explicit rule or user acceptance when a
      language was requested.
- [ ] No unrelated localized language is selected silently.

## Architecture Compatibility

- [ ] Localized terminology remains outside the information-processing
      pipeline.
- [ ] Canonical English names remain stable reference keys.
- [ ] Skills may use localized labels without changing normalized meaning.
- [ ] The Canonical Domain Model, Knowledge Model, and Project Model remain
      unchanged.
