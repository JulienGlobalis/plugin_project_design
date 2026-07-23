# Technical Assumptions

## Identity and Access

The organizational identity service supplies employee accounts and department
membership. Partner identities are not available through that service and are
outside the planned authentication design.

The delivery team expects department membership to identify the approving
manager. The identity team has not confirmed that manager relationships are
available.

## Interfaces

The reporting team expects a live query interface for operational dashboards.
The technical estimate assumes a nightly flat-file export.

## Data

The storage estimate covers two years of requests and attachments. Automated
deletion is included in the estimate.

## Cutover

The technical estimate assumes a single cutover with no parallel operation of
the shared mailbox.
