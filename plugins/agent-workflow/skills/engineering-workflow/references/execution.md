# Execution roles and change ownership

## Select the route

An ordinary user session performs work directly. Use the installed `orchestration` skill when supervision, monitoring, or DAG coordination is requested. A worker receiving a valid Task/Dispatch preamble follows that execution contract. A handoff transferring ownership to a new user session uses `orca-cli` and creates no supervised Run, Task, or Dispatch. Historical IDs in handoff documents are not current execution authority.

Agent delegation, including independent review, requires authorization from the current request and applicable instructions. Do not substitute another subagent tool for Orca supervised execution.

## Select the model

Establish the agent host first: Codex or Claude Code, as selected by the user or project. Keep that host for the task unless a switch is authorized. Resolve specialist skills and tools in that host's available capabilities; an installation visible to the other host does not prove availability here.

Judge the required reasoning depth by uncertainty, change impact, and recovery cost. Favor short implementation and verification cycles for clear local changes, strengthen boundary review for changes spanning modules, and allocate deeper reasoning and independent review to security, concurrency, and complex design work.

Do not assume a permanent performance ranking of models. Read the execution environment's catalog and launcher configuration to select an actually supported model ID and effort. Resolve or disclose differences between requested and applied values. If the current session cannot change its model, report the verifiable settings and limitations without claiming to have switched it.

Record: `agent host / role / selection rationale / requested model and effort / applied model and effort / evidence`. Use the selected host's supported controls; Codex reasoning effort and Claude effort are not an equivalence scale. Record an unavailable control as not applicable and an unverifiable applied value as unconfirmed. If a requested value is unsupported, compare supported alternatives against existing user constraints; hold that execution only when no alternative meets a material constraint. Render this record in Korean when reporting to the user.

In supervised execution, the coordinator owns this record from the launch receipt. A worker cites supplied launch evidence or leaves those fields unconfirmed and points to the coordinator's record; a generic agent self-description does not establish the launched model or whether explicit options were supplied.

## Worktrees and concurrency

For single-agent implementation, inspect existing changes and ownership in the current checkout. Use an Orca worktree when other work would conflict or the project requires separation. Supervised implementation uses a separate worktree for each issue; connect the actual issue to the exact returned worktree ID.

The default for supervised execution is at most two independent implementations. Reduce that number when project resource limits or review throughput are lower. Coordinate ownership or order tasks whose resources or change scopes overlap. Schedule reviews within the available total capacity rather than multiplying workers through nested review teams. Record throughput and conflict evidence before increasing concurrency.

The coordinator owns resource visibility, including when project configuration omits it. Create checkouts when execution or preparation needs them. For each retained checkout, record its owner, actual stage, waiting reason when applicable, and next transition at creation, ownership changes, and execution/review checkpoints. Use the installed Orca contract's supported status/comment fields and read back the result; if unavailable, report the state and limitation in the current progress record. Count running workers, open terminals, and checkouts separately. A displayed completed status does not replace [eligible cleanup](completion.md#resource-cleanup).

Before starting, verify the project's base ref and the actual starting commit. Orca parent relationships do not establish the Git base. Work depending on earlier changes must use a ref containing them. Follow project configuration for shared caches and isolation of databases, ports, build outputs, and test artifacts.

Before running checks, resolve the package directory, required runtime, package manager and dependency setup from project instructions, manifests and CI. Verify the applied runtime and that the lockfile's local tools exist; use the project's setup command when dependencies are missing. Package executors that fetch a missing tool can silently test with a different version. Prefer an already available supported runtime over adapting checks to an unsupported one, and report a missing runtime as an environment limitation. Separate setup failures from a behavioral RED.

Worker launch readiness and a requested setup hook do not prove dependency readiness. The coordinator records the actual setup outcome; the package's execution owner verifies local tools before checks. Let a running setup finish before another install or check uses the same package. If no hook is configured, the execution owner completes the documented package setup.

## Resume and recover

For an active issue, start with the diff and last verification state of the same branch and worktree. If its completed worktree was already removed, start from the verified integration target containing the prior work. Continue failed-test fixes and review revisions from the existing change, updating affected evidence. Preserve user changes.

Reuse a worker terminal for immediate follow-up only after its Dispatch settles and the installed Orca contract transfers ownership to a fresh Dispatch. Check that its existing model and effort suit the next task. A previous coordinator binding is a separate role transition: resolve it through the runtime's binding/recovery contract, or start a fresh worker terminal. An old Run's empty inbox is not evidence about the current attempt.

Keep coordinator and worker commands distinct and preserve the live worker preamble. When inbox reads return a replayable Delivery, process and acknowledge it through the runtime contract before expecting later follow-ups; repeated reads of the same Delivery do not check newer messages. Treat enqueue, receipt, and completed action as separate evidence. Keep one actionable coordinator wait active and resume that wait rather than opening another.

If the runtime reports fencing, follow its stop and recovery contract. A later successful command does not prove that continuing after the rejection was valid.

When an Orca execution result is uncertain, read the installed skill's recovery guidance and the actual receipt. Do not infer worker exit or execution failure from a communication error or empty response and launch a duplicate worker. Follow the Orca contract for Task/Dispatch settlement and resource cleanup. Ordinary user sessions send no supervised lifecycle messages.
