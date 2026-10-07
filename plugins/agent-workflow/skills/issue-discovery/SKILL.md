---
name: issue-discovery
description: Investigate code, product behavior, or feature ideas and turn verified findings into GitHub issues the engineering-workflow project manager can delegate. Use for code reviews, feature or UX reviews, new-feature research, and idea development that should become tracked work. Publishes only issues the user approves. Pre-merge review of a work unit stays with engineering-workflow.
---

# Issue Discovery

Run the investigation the user asks for and end with issues a worker can execute without rediscovery. Approved, published issues are the deliverable. This skill changes no product code; prototypes and other investigation artifacts stay in an ignored location, such as the project's scratch directory.

Read the project instructions, its workflow configuration, and its issue-tracker and label docs, such as `docs/agents/issue-tracker.md` and `docs/agents/triage-labels.md`, before investigating. Write agent-facing notes in English. Write drafts, issues, and reports to the user in Korean.

## Route

| Request | Read |
| --- | --- |
| Code review of a repository, an area, or a change range | [Code review](references/code-review.md) |
| Feature, flow, or UX review of product behavior | [Product review](references/product-review.md) |
| New-feature research or idea development | [Feature research](references/feature-research.md) |

A request spanning modes applies each relevant reference to its part.

## Flow

1. **Scope:** fix the mode, the target, and the base commit that evidence pins to. Ask the user only when readings of the target would lead to different investigations.
2. **Investigate:** follow the mode reference. Delegating parts of the investigation to other agents requires existing delegation authority; launch them from the [launch defaults](../engineering-workflow/references/execution.md#select-the-model).
3. **Verify:** every finding ends verified, marked as a hypothesis, or dropped with a reason. Check each against existing behavior, open and closed issues, recorded decisions, and out-of-scope records before it becomes an issue.
4. **Shape:** turn findings into drafts under [Issue authoring](references/issue-authoring.md).
5. **Approve:** present the draft table from Issue authoring and wait for the user's explicit approval. Approval covers exactly the listed repository, issues, labels, and changes to existing issues.
6. **Publish:** publish the approved issues, verify their relations and labels, and report the URLs. The parent issue is the handoff: the user can give it to the engineering-workflow project manager.

When one of the user-invoked tools in [Skill composition](../engineering-workflow/references/skill-composition.md#user-invoked-planning-tools) fits better, recommend it to the user: `to-spec` or `to-tickets` for spec-driven slicing, `triage` for incoming issues, `wayfinder` for ideas too vague to slice, `improve-codebase-architecture` for architecture deepening, and `setup-matt-pocock-skills` when the tracker docs are missing.
