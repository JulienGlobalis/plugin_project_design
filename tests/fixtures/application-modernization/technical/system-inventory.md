# Current System Inventory

## Application

- Server-rendered Java application using an unsupported application-server
  release.
- Shared modules for web screens, business rules, scheduled work, and data
  access.
- JavaScript helpers added incrementally without a common component model.
- Build process dependent on a workstation configuration known by two
  engineers.

## Data

- Relational database with approximately 180 tables.
- Business rules implemented across application code, database procedures, and
  scheduled jobs.
- Attachment metadata stored in the database; files stored on a network share.
- Duplicate person records and inconsistent category values exist.

## Quality and Operations

- Automated tests cover authentication and a small part of case creation.
- Deployment requires manual configuration steps.
- Monitoring checks server availability but not queue processing or scheduled
  jobs.
- Four scheduled jobs have no current technical owner.
- Development and production configuration use different naming conventions.

No complete component diagram or current data dictionary was found.
