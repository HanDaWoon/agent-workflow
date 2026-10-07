# Issue authoring

The engineering-workflow project manager pastes an issue body into its worker's Task spec. So the body must carry everything specific to that issue that a worker needs; project-wide rules stay in project configuration and are linked, not restated.

## Shape

- **One behavior:** each issue delivers one independently verifiable behavior that fits one worker context. Split criteria that cover separate concerns, such as permissions, concurrency, time zones, and data provenance, into separate issues with real ordering. Bundled concerns multiply review rounds.
- **Order:** preparatory refactoring comes first, and broad mechanical changes follow expand, migrate, contract, as [Planning](../../engineering-workflow/references/planning.md) describes.
- **Decisions first:** a user-owned choice becomes a decision issue with options, a recommendation, and evidence. Implementation issues cite the settled decision and treat it as closed.
- **Depth:** near-term work gets full issues. Later candidates stay as a backlog list in the parent.
- **Parent:** one parent per run groups the children as native sub-issues. Its ordering table uses real issue numbers only.

## Fields

Fill the [issue template](../../engineering-workflow/assets/issue.md) and the [parent template](../../engineering-workflow/assets/parent-issue.md). Each field carries content specific to the issue or is deleted. Repeating a project-wide rule gives the worker nothing new.

- **Evidence:** a reproduction or permalinks pinned to the base commit. A hypothesis is marked as one.
- **Dependency contract:** for each blocker, the interface or behavior this issue relies on, so its worker can start from the blocker's result.
- **Change and conflict areas:** name modules, interfaces, and shared resources, such as message catalogs, the migration sequence, and shared fixtures. The manager uses conflict areas to decide which ready issues may run in parallel.
- **Schema or migration:** yes, no, or undecided with the reason. Every schema change is declared, because migrations must be sequenced across branches.
- **Verification:** the regression to add and its public seam, the flows to check, checks that already fail at the base, and traps that appear only in a clean checkout.

Public issue text excludes local paths, credentials, and private session evidence.

## Execution recommendation

Assess depth, size, and risk from the investigation:

- **Risk:** assess with the high-risk factors in [Completion](../../engineering-workflow/references/completion.md#review-criteria-and-depth), even when the visible change is small; they also decide the manager's reviewer split.
- **Agent, model, effort:** start from the [launch defaults](../../engineering-workflow/references/execution.md#select-the-model) and adjust under their rule. Name the deep-work model only for the deepest work, and choose only among the agent hosts the project configures.

Record the recommendation with its reasons in the issue's execution section. It is the manager's starting point, not an applied value.

## Labels

Mirror the recommendation in namespaced labels so the manager can filter issues:

| Label | Meaning |
| --- | --- |
| `agent:codex`, `agent:claude` | Recommended agent host |
| `effort:<level>` | Recommended effort level, in that host's level names |
| `model:deep` | Deep-work model recommended; absent means the default model |
| `risk:low`, `risk:medium`, `risk:high` | Risk level |

Labels name classes, never model IDs; the body holds the reasons. Also apply the project's own category and triage-state labels from its label docs, using a ready-for-agent state only for a fully specified issue. A label missing from the repository goes into the approval table with its description and color, and is created only after approval.

## Approval

Write the drafts to an ignored local location, together with the run's slug: a short, non-private name such as the date and target that stays the same across retries. Show the user the target `owner/repo` and one table with each issue's title, kind, parent, blockers, risk, recommended agent, model, and effort, and labels. Also list the labels to create and every change to an existing issue: a reused issue added as a sub-issue, labeled, or linked as a blocker. An issue can have only one parent, so a reused issue that already has one is cited in the new issues' bodies instead and left unchanged. Provide full bodies on request.

Publish only what the user explicitly approves. An edit returns to the table. Silence, or approval of a different list, is not approval.

## Publish

1. Create the approved missing labels with `gh label create`, without overwriting existing labels.
2. Create the parent with its ordering and pending-decision sections marked as pending, then the children in dependency order so every blocker exists first. Use `gh issue create` with `--parent`, `--blocked-by`, `--label`, and `--body-file`. End each body with a hidden marker, `<!-- issue-discovery:<run>:<finding> -->`. Before each create, look for the marker in the repository's issues of every state, fetched with `gh issue list --state all --limit <more than the repository's issue count> --json number,body` and matched locally; search indexing lags, so a quick retry could miss an issue it just created.
3. Apply the approved changes to existing issues.
4. Read back every issue with `gh issue view --json parent,blockedBy,labels` and repair any difference.
5. Fill the parent's ordering table and pending decisions with the real numbers, and report the URLs to the user as a table.

Publishing is done when every approved issue exists with its parent, blockers, and labels verified. After publication, a change to acceptance criteria goes into the issue body, not only a comment, so the body stays the worker's spec.
