# Project workflow configuration template — v1

Configuration template for the adopted v1 workflow. Link existing project documents that already own the information. Fill `<...>` fields from actual evidence when applying the template; blank fields are neither authorization nor proof of passing verification. Applying this template to another project requires scope covering that change.

## Entry and requirements

- Scope: `<repository or subdirectory>`
- Agent hosts: `<Codex, Claude Code, or both; installing both does not launch both>`
- Instruction sources: `<AGENTS.md for Codex; CLAUDE.md for Claude Code, importing shared AGENTS.md when appropriate; preserve existing instructions>`
- GitHub tracker: `<owner/repo and existing tracker configuration link>`
- Domain and ADRs: `<existing documentation links>`
- Upstream skill compatibility, when those skills are used: `<docs/agents/issue-tracker.md, docs/agents/domain.md, and required label vocabulary; link existing sources and provide the exact entry files expected by the selected skills>`
- Execution skill entry: `<discoverable personal skill or verified source SKILL.md link; record whether entry is explicit-only or enabled for the authorized scope>`
- Project instruction pointer, when entry is enabled: `For implementation, resumption, and work-planning requests, read <execution skill entry> and docs/agents/workflow.md. For questions and reading requests, answer directly.`
- Language: agent instructions and handoffs in English; user-facing review documents, issues, and completion reports in Korean.

## Execution baseline

- Default branch/ref source: `<repository configuration or documentation link>`
- Base selection for dependent work: `<how to verify prerequisite changes are included>`
- Runtime and setup sources: `<supported runtime, package manager, lockfile and setup command sources, including execution directory; verify applied values using Execution in the personal skill>`
- Session execution conditions: `<observed sandbox, approval and network capabilities of fresh sessions; record required operator intervention rather than assuming the coordinator's environment is inherited>`
- Relevant check selection: `<evidence connecting affected areas to checks>`
- Agreed public test seams: `<interface, covered behavior, and user agreement in the issue/spec/conversation; reuse that agreement until the seam materially changes>`
- Required completion checks: `<CI job/script links and passing conditions>`
- Verification environment: `<approved synthetic/local/live paths, environment loading controls, fixture or harness source, and what each can prove; link evidence rather than embedding credentials>`
- Integration conditions: `<target branch, required review/CI, merge method>`
- Review ownership and target: `<implementation owner, reviewer, integration owner, and frozen commit or workspace snapshot>`
- Is deployment required for issue closure: `<yes/no and existing agreement>`

## Resources and concurrency

- Per-worktree isolation: `<ports, database/schema, build/test outputs, cleanup owner>`
- Cleanup inputs: `<integration target proving preservation, or explicit non-integrating experiment scope; retained evidence/archive location, owner and release condition, restoration prerequisites, path-dependent harnesses, and current resource owners; apply the personal skill's Completion reference>`
- Resource status location: `<project-specific progress record or supported Orca status/comment fields; the personal skill's Execution reference owns update responsibility and checkpoints>`
- Shareable caches: `<stores/images and sharing conditions>`
- Dependency directory sharing: `<evidence about concurrent changes and platform constraints; otherwise install separately>`
- Concurrent supervised implementation limit: `<value based on resources and review throughput>`
- Conflicting change scopes: `<ownership coordination for shared files, migrations, etc.>`

## Authorization and completion evidence

- Continuing authorization evidence: `<user instruction/project agreement and its scope>`
- External publication/push/merge/deployment scope: `<already authorized scope or unresolved>`
- Other-project changes: `<authorization evidence or out of scope>`
- Completion evidence location: `<issue/PR/verification-log linking convention>`
- Project model constraints: `<actual restrictions, such as allowed models or cost; omit if none>`

This file does not grant authority. Configure it from actual user authorization and tool permissions. Reference command sources rather than copying them; keep secret values and execution logs out of this configuration.

When validating runtime entry, use fresh ordinary sessions with task prompts that omit the skill name and path, and check the actual skill read before execution. Cover implementation, resumption, and planning branches and a reading-only bypass. A pointer restricted to explicit invocation does not establish automatic entry. Record which branches were actually exercised. Keep experimental pointers in pilot checkouts until project activation is authorized; preserve the evidence and remove the experiment during cleanup.
