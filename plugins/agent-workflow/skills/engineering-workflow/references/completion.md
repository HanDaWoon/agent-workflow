# Verification, review, and completion

## Verification evidence

Complete project-required checks and record the target, command or CI job, result, and environmental limitations. Reuse passing evidence for the same code and environment. When code, base, dependencies, or environment change, refresh affected evidence and satisfy project requirements again.

Trace changed areas to the project's conditional documentation and verification requirements. Check what an umbrella build actually includes: test files and support scripts can be excluded from its diagnostics. Run the applicable direct checker for changed files outside that coverage. Record the actual environment controls used; synthetic service variables alone do not establish isolation from environment files or inherited credentials.

For diagnostics that consume generated inputs, establish that those inputs match the final source tree, including after temporary routes or fixtures are removed. Use the project's generation command when inputs are missing or stale, then rerun the affected direct checker.

For runtime or setup changes, verify the documented entry path in the intended execution environment and state its prerequisites. An explicit runtime launcher proves that path, not automatic selection in every shell. A stripped environment is a separate scenario; do not generalize its failure to a configured host or its success to an unconfigured host.

Tests for behavior changes verify observable behavior against independent expected values. Documentation changes use relevant link, formatting, and content consistency checks. Distinguish checks not run, pre-existing failures, and failures caused by the current change.

## Review criteria and depth

Fix the base commit and target change for review. Spec review examines acceptance criteria, scope, and missing behavior. Standards review examines project instructions, design consistency, and maintainability.

State whether the target is the whole repository, a committed range, or a workspace snapshot. A committed range excludes staged, unstaged, and untracked changes. For workspace review, include the relevant files explicitly and freeze edits while independent reviewers read them, or use an interim commit clearly marked as pending review. For a whole-repository audit, inspect the tracked tree even when the branch diff is empty. Capture the selected base and target as immutable evidence rather than relying on a moving branch name.

High-risk changes require separate independent reviewers for Spec and Standards. High-risk factors include security boundaries, potential data loss, concurrency, and broad compatibility changes; assess these before considering a change's size. Otherwise, use self-review for small documentation or low-risk changes, and one independent reviewer covering both axes for other implementation. Satisfy any stronger project-required review. An independent reviewer may be another person or an agent whose delegation is authorized; the required reviewer count does not override delegation permissions.

If required independent review is unavailable, complete self-review and report independent review as pending. Do not mark review complete. An interim commit is possible after implementation and required tests are finished, but explicitly retain the pending-review status and distinguish it from issue closure or completed integration. Refresh affected verification and review evidence after review revisions.

In supervised review, send fixes back to the designated implementation owner and follow [Skill composition](skill-composition.md). Reviewers report findings; they do not edit the same target concurrently.

## Commit and integrate

Separate user changes from the task's changes in the final diff and commit only the task scope. Confirm that the commit contains the changes covered by verification and review. Do not report a work unit as complete while required verification is failing.

The default for closing an implementation issue is integration into the target branch with required verification and review evidence. A commit, PR creation, push, and Orca worker success are separate outcomes. If deployment is part of project acceptance criteria, obtain deployment evidence too. Work authorized directly on the target branch is still assessed against its actual commit and project completion conditions.

Within authorization, post the [completion report](../assets/completion-report.md) to the issue and link evidence. If external updates are unavailable, prepare the report locally and state actual progress. Supervised workers finish their delegated scope and report through the Orca contract; the role authorized to close the issue and integrate the overall work owns those actions.

## Resource cleanup

Automatically clean up completed workflow resources as soon as they are eligible and before the final completion report. No further confirmation is needed for this scoped cleanup. The session or coordinator responsible for overall completion owns any teardown that a worker cannot perform on its own terminal or checkout.

- **Terminals:** after accepted Task/Dispatch settlement, release workers with no immediate follow-up through the installed Orca contract. Inspect and close unused task shells and leftover tabs/resume records once their completed-work provenance and lack of current use are established. Preserve the active user session, unrelated resources, explicitly requested retention, and resources assigned to continuing work. Starting-inventory membership alone does not establish user ownership or a reason to retain a previous run's leftovers.
- **Worktrees:** remove a completed task checkout once its intended changes are preserved in the integration target, no unmerged work or uncommitted user changes remain, and no active owner or dependent work still needs it. For an explicitly scoped non-integrating experiment, use [Archived experiments](#archived-experiments) to establish the alternative preservation condition. Inspect untracked and ignored files; preserve unique evidence outside the checkout and verify the copy before removal. Keep the main checkout. Use Orca for managed worktree removal and its integrated-branch cleanup; do not force-discard changes. Local integration can satisfy this condition without remote push. An open issue or pending manual acceptance alone is not a retention reason when future work can resume from the preserved commits.

Before teardown, update current instructions that depend on the retiring checkout. Preserve historical evidence unchanged; document how a working copy of a path-dependent harness can be rerun from the preserved commit. For any resource that must remain, record its owner, concrete reason, and the event that makes it eligible for cleanup.

Verify the result through the execution host: terminal/process and tab inventories after release/close, and Orca/Git worktree inventories plus filesystem absence after removal. Check the final state before reporting and recheck related leftovers on resumption. A successful release receipt or a matching before/after count does not prove all eligible resources were removed or will stay absent after restart. Follow Orca's recovery contract for uncertain results; report unresolved cleanup instead of claiming it complete. This policy does not authorize an unrelated resource sweep, external publication, or installation of background automation.

## Archived experiments

Use this alternative only when the task's authorized scope includes finishing an experiment without product integration and removing its owned resources. An archive alone does not authorize discarding ordinary unmerged implementation, user changes, or a still-needed checkout. Establish completed scope, accepted worker settlement where applicable, exclusive resource ownership, and no active owner or dependent work before proceeding.

1. Capture the exact refs and commits plus tracked, untracked, and ignored contents. Preserve the experiment's intended changes and unique evidence in a designated retained archive outside disposable checkouts and temporary directories. Record its owner, retention/release condition, hashes, and restoration instructions. For incremental bundles, retain and verify the prerequisite history too, or use a self-contained bundle. State whether preservation is local-only.
2. Restore into a separate temporary repository using only the documented archive and prerequisites, without borrowing objects from the checkout being removed. Verify the expected commits and changed-file contents; compare separately preserved evidence byte-for-byte. A missing prerequisite, failed restore, unknown ownership, user change, or active dependency blocks removal. Preserve the resource and report the concrete blocker.
3. Recheck the source refs and working state immediately before teardown. A change invalidates the earlier eligibility decision. Remove the eligible managed checkout through Orca without forcing. If Orca retains an unmerged branch, delete only the exclusively owned experiment ref, conditioned on its exact archived HEAD; retain it if that condition or ownership cannot be verified. Apply the ordinary terminal, inventory, and filesystem cleanup checks above. Remove the temporary restore repository after verifying the retained archive.

Report this result as archived without product integration. Keep the archive available until its recorded release condition is met; completion of checkout cleanup alone does not make the archive disposable.
