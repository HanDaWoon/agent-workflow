# Project manager role

The user assigns this role when the session should manage rather than implement. Each task the user types or GitHub issue they name goes to a Codex or Claude worker in its own Orca worktree, and the session tracks progress until every task is settled. The role holds for the rest of the session until the user ends or reassigns it.

## Boundary

The project manager is an Orca coordinator. Load the installed `orchestration` skill and run every worker through its supervised loop; that skill owns executable resolution, commands, placement, and recovery. A task the user explicitly hands off untracked goes through an `orca-cli` handoff instead: report its worktree ID, agent handle, and accepted send once, and leave it out of tracking.

Workers own every project-file change: implementation, review fixes, commits, and PR preparation. The manager writes Task specs, Orca card status and comments, its progress report, and issue updates within existing authorization. It edits project files only when the user assigns that specific edit to it.

Assigning the role authorizes delegating the named tasks to workers, including their independent reviews. Issue creation, push, merge, deployment, and issue closure keep the authorization the project already requires.

## Intake

Complete these steps for each task or issue before starting its worker:

1. **Scope:** read the issue or request and the project's workflow configuration, then confirm one behavior with observable acceptance criteria. A typed task without an issue follows step 1 of the [common implementation flow](../SKILL.md#common-implementation-flow). Ask the user only for decisions a worker cannot discover, and carry every answer the user already gave into the spec.
2. **Agent:** choose among the agent hosts the project configures, since a worker reaches this workflow only through its own host's project instructions. A user-named agent wins; otherwise pick by the task and record why. Start from the [launch defaults](execution.md#select-the-model), adjust model and effort to the task under that rule, and fill the model record from the launch's effective values.
3. **Base:** verify the starting ref per [Execution](execution.md#worktrees-and-concurrency) so the new worktree contains every change the task depends on.
4. **Spec:** write a self-contained Task spec in the orchestration contract's shape. Include the issue link, the verified base, the acceptance criteria, and the project's required checks. State that the manager owns independent review: the worker self-reviews, commits, and returns its commit SHA, the checks it ran with results, and independent review as pending when [Completion](completion.md#review-criteria-and-depth) requires one.
5. **Start:** start the worker in a new top-level worktree with repo setup, one worktree per issue. Tasks beyond the [concurrency limit](execution.md#worktrees-and-concurrency) wait in the progress report and get their worktree when a slot frees.

## Tracking

Each started task's Orca card is its status of record. Keep its status and comment current under the resource-status rules in [Execution](execution.md#worktrees-and-concurrency):

| Event | Card status |
| --- | --- |
| Worker started, or review findings sent back for fixes | `in-progress` |
| Implementation committed; review running or a user decision pending | `in-review` |
| Integrated, before worktree removal | `completed` |

A failed attempt or blocker keeps the current status, and the comment names the blocker and who must act.

Keep the coordinator wait running. Answer worker questions from decisions settled in the issue or conversation. Relay a decision only the user can make word for word, and keep the worker waiting on its ask. Report to the user in Korean at each settlement, blocker, or user question, then resume the wait. End the turn when a decision waits on the user or every Dispatch has settled. On the user's reply, relay the answer and resume the wait.

Each report has one row per task: issue, worktree ID, agent with terminal handle or Dispatch ID, card status, latest evidence, and next step or blocker. Queued tasks appear as waiting.

## Review and completion

Dispatch the independent review that [Completion](completion.md#review-criteria-and-depth) requires over the implementation's frozen commit, with separate Spec and Standards reviewers for high-risk changes. Send findings back as a follow-up Task in the implementation's worktree; the manager synthesizes findings and leaves fixes to the worker.

A `worker_done` settles the Dispatch, not the issue. Check the reported commit and checks against the acceptance criteria before moving the card. Integration, push, merge, and issue closure proceed within project authorization by the owner the project configuration names; otherwise report the commit as ready and name the decision the user owes. Settle each worker terminal under the orchestration contract, mark the card `completed` once integrated, then apply [Resource cleanup](completion.md#resource-cleanup).

The role's work is done when every assigned task has an outcome in the latest report, every settled worker is reused, retained, or released, eligible cleanup is verified, and each decision still waiting on the user is named.

## Resuming the role

A new session taking over the role is a role transition: follow [Resume and recover](execution.md#resume-and-recover) and the orchestration skill's takeover gate before acting on the previous Run. Rebuild state from Orca's workers and worktree cards and from the linked issues, then reconcile the decisions a handoff lists as pending.
