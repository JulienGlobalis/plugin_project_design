# Functional Design Artefact Structure

Use this structure for `_project-design/functional-design.md`. Preserve the
business meaning and stable identifiers when adapting labels or omitting a
meaningless hierarchy level.

## Evolution Controls

Start with concise artefact controls before the numbered business sections:

- project and artefact title;
- current artefact version or baseline when supplied;
- artefact review status when supplied;
- last validated change date when known;
- applicable Project Canvas or Project View baseline;
- change history.

Do not invent a version, owner, approval, or date. The change history uses:

| Date | Affected IDs | Change type | Reason or source | Decision status |
| --- | --- | --- | --- | --- |

Allowed change types are `Addition`, `Clarification`, `Correction`,
`Deprecation`, and `Replacement`, localized naturally when needed. Use a
project-provided vocabulary instead when one already exists.

The current body describes the current applicable design. The change history
records why it evolved; it does not duplicate the complete evidence trail.

## 1. Actors and Roles

Describe functional participation rather than project governance. Keep Actors
distinct from Stakeholders.

Recommended table when several actors share comparison dimensions:

| Actor ID | Actor or role | Responsibilities | Main interactions | Known rights or limits | Status |
| --- | --- | --- | --- | --- | --- |

Do not invent permissions. Link personas to an Actor rather than creating a
separate identity when they describe the same functional role.

## 2. General Specifications

### 2.1 Global Processes

Describe target end-to-end Processes at a level that connects actors,
features, rules, and outcomes. Give each represented process a stable ID.

For every process, capture when known:

- trigger and objective;
- participating actors;
- main stages and outcome;
- related features and global rules;
- unresolved decisions or variants.

Keep Existing and Transition processes separate when they materially qualify
the target design.

### 2.2 Product, Module, and Feature Inventory

Use a table as the navigation and coverage index:

| Feature ID | Product | Module | Feature | Objective | Target actors | Scope or maturity | Dependencies | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

The `Detail` cell links to the feature section. Use only hierarchy levels that
carry project meaning. This table is not a prioritized backlog and contains no
effort, sprint, implementation task, or unsupported sequencing.

Every listed feature must have one detailed section or an explicit justified
deferral. Every detailed section must occur in the inventory.

### 2.3 Global Business Rules

Centralize rules that apply across several Processes, modules, or features:

| Rule ID | Rule | Applies to | Status | Decision or evidence reference |
| --- | --- | --- | --- | --- |

Feature-specific rules remain in their feature section. A feature references
a global Rule ID instead of restating it.

## 3. Detailed Functional Specifications

Create one subsection per inventory feature, headed by its stable ID and name.

### 3.x `<Feature ID>` — `<Feature name>`

#### General Information

| Property | Value |
| --- | --- |
| Stable ID | |
| Name | |
| Product / module | |
| Functional maturity | |
| Objective | |
| Target actors | |
| Prerequisites | |
| Postconditions | |
| Dependencies | |
| Applicable global rules | |
| Traceability | |

Use `To be defined` for unsupported but structurally necessary values. Do not
use a missing value as a reason to invent a question.

#### Nominal Scenario

Use ordered observable steps. Each step names the acting Actor or solution
behavior, the action, and the resulting functional state. Avoid technical
mechanisms.

#### Alternative Valid Scenarios

Describe supported variations that still achieve a valid outcome. Do not
classify these as errors merely because they differ from the nominal path.

#### Errors and Exceptions

Use a table when several cases share the same dimensions:

| Case ID | Trigger or condition | Expected handling | Resulting state | Visible feedback | Related message |
| --- | --- | --- | --- | --- | --- |

Keep business rejection, validation error, unavailable dependency, user
cancellation, and exceptional recovery distinct when the project evidence
does so.

#### Acceptance Criteria

Give each criterion a stable ID related to the feature. Express observable
conditions and outcomes. Prefer a clear `Given / When / Then` form only when
it improves testability; do not force it for declarative rules.

Do not invent values, thresholds, performance targets, priorities, or test
data. Link criteria to the scenario, rule, interface, field, or message they
verify.

#### Questions and Required Decisions

Retain only questions that materially affect the feature or downstream use.
Identify the expected authority when known. Never hide a conflict inside a
provisional behavior.

#### Interfaces and Fields

Describe each user-facing or functional interface with a stable Interface ID,
purpose, target actors, entry conditions, expected actions, outcomes, and
states. A screen, form, report, import surface, or externally visible
interaction may be an interface; do not prescribe its technical delivery.

For field-level behavior, use:

| Field ID | Label or information | Expected value / format | Required | Editable | Visibility | Default or source | Validation and behavior | Rule refs | Message refs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Record only supported properties. Keep business format and validation distinct
from database types or implementation widgets. Describe conditional display,
editability, calculation, and cross-field validation when materially known.

#### Feature-Specific Business Rules

| Rule ID | Rule | Applies when | Result | Status | Decision or evidence reference |
| --- | --- | --- | --- | --- | --- |

Do not duplicate a global rule. Reference it and state only the feature-local
qualification.

#### Messages

List the message references used by the feature:

| Message ID | Trigger | Channel | Recipient or audience | Purpose |
| --- | --- | --- | --- | --- |

The full message definition belongs to the annex catalog.

## 4. Annexes

### 4.1 Global Message Catalog

Define each transactional e-mail, SMS, notification, or in-application message
once:

| Message ID | Name | Channel | Trigger | Recipient or audience | Functional content or exact approved wording | Dynamic information | Conditions | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Do not invent marketing or legal wording. When exact wording is not approved,
state the required information and mark the wording as unresolved.

### 4.2 Optional Shared Annexes

Add only when they reduce ambiguity or duplication:

- functional glossary;
- shared functional data dictionary;
- cross-reference index for rules, features, interfaces, and messages;
- explicitly requested traceability matrix.

Do not add a technical data model, API contract, architecture diagram,
backlog, release plan, or document-format instructions.

## Downstream Readiness

After the numbered sections, qualify technical-design and backlog-preparation
readiness separately. Identify blockers and non-blocking reservations from the
current artefact. Do not calculate a percentage or claim universal
completeness.

