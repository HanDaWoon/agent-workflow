---
name: engineering-workflow
description: Plan or execute implementation around GitHub issues and connect verification, review, commits, and integration evidence. Use for implementation requests, task decomposition, and resuming changes. Do not apply the full workflow to simple questions or reading tasks.
---

# Engineering Workflow

Apply these workflow defaults within current user instructions and the project's agreed conditions. Using these defaults does not install this skill or change another project's entry configuration. Matt skills and Orca are external prerequisites whose installation and maintenance are outside this workflow.

Use this same skill in Codex or Claude Code. Follow the selected host's project instructions, tool contracts, and permissions; a shared workflow does not make their launch flags or model settings interchangeable.

Always clean up eligible terminals and worktrees when their work is finished, without another confirmation. Apply [Resource cleanup](references/completion.md#resource-cleanup) before reporting completion.

Write agent instructions and handoffs in English. Write user-facing explanations, review documents, issues, and completion reports in Korean. The Korean assets in this package define user-facing output.

## Entry

Carry forward the objective, acceptance criteria, and settled decisions from the request, existing issues, and handoff documents. Read project instructions and `docs/agents/workflow.md`, or existing configuration serving the same purpose. If configuration is missing, discover the needed values from the repository and CI; ask only about gaps that block the work. Do not make creating a configuration file a prerequisite for every task.

| Request or context | Route |
| --- | --- |
| Questions or reading | Read the necessary evidence and answer |
| Review proposal or design | Produce a reviewable document separating prior agreements from open decisions |
| Clear implementation | Confirm the issue, acceptance criteria, and project verification requirements, then execute |
| Uncertain implementation or task decomposition | Read [Planning](references/planning.md) and define the next executable work |
| Execution, resumption, delegation, or handoff | Read [Execution](references/execution.md) to establish role, model, and change ownership |
| Finishing changes, review, integration, or resource cleanup | Read [Completion](references/completion.md), complete eligible cleanup, and report evidence and actual status |

For interface design, domain decisions, or agent-document edits, read [Skill composition](references/skill-composition.md) and apply the relevant installed specialist. This workflow owns routing and evidence; it does not duplicate those specialists' full procedures.

Invoking this skill does not authorize external actions or agent delegation. Continue within existing authorization. When additional approval is necessary, prepare the concrete change and target before asking immediately before that action. Preserve user-only invocation restrictions on referenced external skills.

## Common implementation flow

1. **Define the work:** Read the existing GitHub issue and confirm acceptance criteria for one behavior. Create new issues according to existing tracker configuration and authorization. If publication is unavailable, prepare a local draft using the [issue template](assets/issue.md) and record that it is unpublished. Resolve publication authorization before starting implementation that requires a published issue. Design and reading work can continue.
2. **Prepare execution:** Use [Execution](references/execution.md) to select the route and model. Before the first check, verify the project runtime and locked local tools, and finish any missing dependency setup. Execute when scope, verification, and actual blockers are clear. Small tasks do not need an additional roadmap or supervised Run.
3. **Implement and verify:** For a test-first behavior change, read [Skill composition](references/skill-composition.md) and the installed `tdd` instructions before writing the first regression. Apply their loop to the agreed public seam; record an unavailable or unused specialist accurately. Change one behavior at a time and run relevant tests and type checks. Behavioral tests use public interfaces and independent expected values. Verify reversible documentation or formatting changes through relevant static checks and diff review.
4. **Finish:** Commit only the task's changes that satisfy the verification and review conditions in [Completion](references/completion.md). Integrate and deploy within project conditions and authorization, and record actual results using the [completion report template](assets/completion-report.md).

Load only references relevant to the current path. Obtain Orca commands, lifecycle rules, and recovery syntax from the installed skill when executing. If a required Orca capability is unavailable, preserve changes and report the missing capability and the work that can still proceed.
