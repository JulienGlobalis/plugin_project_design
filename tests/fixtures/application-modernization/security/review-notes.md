# Security Review Notes

The following observations came from a preliminary review:

- Some support actions use a shared privileged service account.
- Team administrators can grant profiles broader than their own.
- Attachment types are restricted by filename extension only.
- Sensitive notes are visible to all members of the assigned team.
- Audit entries record the action time but not always the acting user.
- Dormant accounts remain in local team tables after directory access is
  removed.
- Session timeout behavior differs between the main screen and the reporting
  screen.

The information classification of cases and attachments has not been agreed.
No current threat model, penetration-test report, or formal security
acceptance was supplied.
