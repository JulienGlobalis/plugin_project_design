# Short Fictional Project Canvas Example

This example demonstrates structure and status handling only. It is not a
Golden Output, fixture result, or source of reusable project facts.

## Project Canvas — Community Room Booking

### 1. Business Context

The fictional North Quay Community Centre currently accepts room requests by
email. Staff manually reconcile availability, which causes confirmed double
bookings. The current handling is **Established (Existing)** from the supplied
operations note.

### 2. Objectives and Expected Value

- **Established:** reduce confirmed double bookings.
- **Provisional:** give community groups visibility of request status.
- No approved baseline or numeric target was supplied.

### 3. Project Stakeholders

| Party | Role or authority | Status |
| --- | --- | --- |
| Centre manager | Sponsor and scope authority | Established |
| Facilities team | Maintains rooms and closures | Established |
| Data-protection contact | Required contributor; person not identified | Unresolved |

### 4. Users

- Community coordinators submit booking requests.
- Reception staff review requests and record decisions.
- The needs of occasional external organizers are not sufficiently described.

### 5. Functional Scope

#### MVP

- **Provisional:** request submission, availability review, staff decision,
  and status visibility.

#### Outside MVP

- **Established exclusion:** online payments.
- **Future Option:** automated access-code delivery.

#### Unresolved Scope

- Recurring bookings require a decision before functional design.

### 6. Technical Constraints

- **Established:** staff sign-in must use the existing organizational identity
  service.
- Hosting and integration constraints were not supplied.

### 7. Risks

- **Risk:** incorrect room data could continue to permit conflicting bookings.
- **Confirmed Issue:** double bookings already occur; this is not a Risk.

### 8. Decisions

- Online payments are excluded from the MVP by the centre manager.
- No architecture or technology Decision has been made.

### 9. Questions

| Question | Why it matters | Classification |
| --- | --- | --- |
| Are recurring bookings included? | Changes Processes and Scope | Required before functional design |
| What room system, if any, must be integrated? | Changes technical feasibility | Required before technical design |
| Who approves retention rules? | Required for responsible delivery | Blocking further progress |

### 10. Success Criteria

- Fewer confirmed double bookings is the source-supported success direction.
- Baseline, measure, and target are **Unresolved** and must not be invented.

## Downstream Readiness

The Canvas can start functional discussion of the established booking flow,
but recurring-booking Scope remains unresolved. Technical design should wait
for the existing-system question. Backlog preparation is not yet responsible
because the MVP boundary is incomplete.
