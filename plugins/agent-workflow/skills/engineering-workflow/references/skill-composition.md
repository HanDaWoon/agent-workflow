# Composing external skills

Read this reference when selecting an available external engineering skill. Matt skills and Orca are installed and maintained outside this repository. This workflow owns routing, task identity, execution ownership, and completion evidence. External skills own their specialized techniques; Orca owns supervised runtime state.

## Direct reuse

Resolve the skill by name through the host's available skills and read its actual instructions before applying it. Keep workflow references independent of installation paths.

| Need | Skill | Entry condition |
| --- | --- | --- |
| Write or revise agent instructions | `writing-for-agents` | Apply its context-pointer and single-source guidance; also read its mechanics reference when editing skills |
| Design an interface or test seam | `codebase-design` | Apply to the interface being designed, not every ordinary edit |
| Resolve domain vocabulary or record a consequential decision | `domain-modeling` | Create glossary entries and ADRs only when there is an actual term or decision to record |
| Implement a behavior test-first | `tdd` | Identify the public seam and its existing user agreement before starting the loop |

For TDD, carry forward the exact seam agreement from the issue, specification, or conversation. Existing agreement satisfies confirmation; do not ask the same question again. If the seam is new or materially changed and no agreement covers it, present that specific choice before writing tests. The source skill's red → green discipline does not require tests for documentation-only changes.

Availability is not invocation, project setup, or evidence of a successful coding run. If a selected skill is unavailable, use the authorized basic workflow where possible and report the missing technique. Leave installation to the external tool-management process.

## User-invoked planning tools

`setup-matt-pocock-skills`, `to-spec`, `to-tickets`, `implement`, and `wayfinder` are user-invoked in the inspected upstream revision. Recommend an appropriate tool when useful, but do not invoke it transitively from this workflow. Preserve upstream invocation metadata, including `agents/openai.yaml` when present.

Before using upstream planning tools, resolve their project contract: `docs/agents/issue-tracker.md`, domain documentation, and the label vocabulary they require. A link to an arbitrary workflow document alone is insufficient. Reuse existing decisions about GitHub, language, and project scope. Setup must not create an unnecessary triage system.

Choose one execution owner. A user-requested upstream `implement` owns its implementation flow. This personal workflow owns execution when it is selected instead. Do not nest both execution flows or claim that a personal adaptation ran the upstream skill unchanged.

## Review with Orca

The inspected upstream `code-review` requires two parallel reviewers and a committed diff from a fixed point. Its review contract is not equivalent to self-review or review of an uncommitted workspace.

When supervised Orca review is requested, use the installed Orca contract to dispatch review-only work over a frozen target. Provide the same target snapshot to the reviewers, but separate Spec evidence from Standards evidence. Route fixes back to the implementation owner. An independent-review result grants permission to synthesize findings, not to assume ownership of edits. Recheck the target after fixes.

This Orca composition is a personal adaptation of the two-axis idea. Do not call it an unchanged invocation of upstream `code-review`. If the user explicitly chooses the original, satisfy its actual contract in an authorized environment.
