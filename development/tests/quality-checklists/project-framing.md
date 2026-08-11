# Project Framing Test Checklist

Use the installable
[Project Framing Quality Checklist](../../../plugins/project-design/skills/project-framing/references/quality-checklist.md)
as the normative methodology contract.

During repository validation, also confirm that:

- [ ] all four permanent fixture scenarios have been reviewed;
- [ ] scenario-specific observations remain represented;
- [ ] every fixture output is a Project Canvas with all ten required sections
      present or explicitly insufficiently informed;
- [ ] fixture outputs remain usable by the applicable downstream steps while
      preserving explicit gaps;
- [ ] the manual test file contains the current test cases and bilingual
      Project Canvas criteria, result areas, and reservation areas;
- [ ] the skill and its runtime references do not depend on `development/`;
- [ ] the runtime example is fictional, does not reuse a permanent fixture,
      and is not represented as a Golden Output;
- [ ] fixture and Golden Output content is unchanged unless the iteration
      explicitly authorizes it;
- [ ] the Canonical Domain Model, Knowledge Model, Project Model, and
      localized terminology remain unchanged unless the iteration explicitly
      authorizes an architectural evolution;
- [ ] the generated framing remains within the boundaries of the installable
      quality checklist.
- [ ] the response first identifies `project-framing`, its inputs, the Project
      Canvas output, and that no document template is required;
- [ ] the opening presents all ten Canvas chapters before requesting project
      content;
- [ ] the optional Word or Google Docs output and local, Drive, or default
      template choice are resolved before requesting the initial description
      or source documents;
- [ ] the user may start from a prompt description, source documents, or both;
- [ ] question-and-answer rounds contain at most three high-value questions,
      update the Canvas progressively, avoid repetition, and preserve deferred
      unknowns;
- [ ] in a guided flow, framing starts only in `framing_iterations` and every
      round is recorded after the working Canvas is updated;
- [ ] more than three questions in one recorded round are rejected by the
      state machine;
- [ ] Canvas approval requires an explicit user confirmation and a non-empty
      `_project-design/project-canvas.md`;
- [ ] durable Markdown delivery uses `_project-design/project-canvas.md` or a
      justified qualified filename without silent overwrite.
