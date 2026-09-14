# Repository instructions

## Language

Write agent instructions, skill frontmatter and bodies, references, and instruction templates in English. Write user-facing conversation, README, product documentation, and issue/report output templates in Korean. Preserve code identifiers, commands, paths, and source titles as needed.

## Workflow

Read [README](README.md) for the product and [workflow design](docs/workflow.md) when changing its policy or composition. For implementation, resumption, and work-planning requests, read [Engineering Workflow](plugins/agent-workflow/skills/engineering-workflow/SKILL.md) and follow the applicable route. For questions and reading requests, answer from the necessary evidence.

Use GitHub issues for public product changes; describe reusable behavior and acceptance criteria. Private session work uses an ignored local task record under the publication boundary below. During supervision, isolate implementation issues in separate Orca worktrees. Select model and supported effort by task difficulty, verify applied settings, and run relevant checks before committing completed work. Apply the skill's review and completion requirements.

Always complete eligible terminal and worktree cleanup under [Resource cleanup](plugins/agent-workflow/skills/engineering-workflow/references/completion.md#resource-cleanup). Preserve active user resources, unrelated work, and unique evidence. Establish execution authority from the current request and valid runtime context; reading this repository does not create a supervised Task or Dispatch.

## Publication boundary

Keep the tracked tree focused on reusable workflow instructions, templates, implementation, tests, and installation/use documentation. Keep session progress, pilot reports, project-specific paths and identifiers, authorization history, and execution evidence in ignored `.local/` or `.scratch/` storage. Apply the same boundary to public issues, comments, commit messages, and release notes. Prepare a local task record when public tracking would expose private context.

When resuming work in a maintainer checkout, read `.local/workflow/context.md` if it exists and consult its linked local records for continuing agreements. This optional context is not shipped with the plugin and is not required for users to install or run it. Keep new progress in local records rather than adding it to README or product documentation.

## External tools and authorization

Matt Pocock skills and Orca are installed and maintained separately. This repository owns workflow policy, invocation conditions, role ownership, project contracts, and completion evidence. Use external tools through their current contracts; leave their installations, updates, sources, and inventories to their own management process.

Continue within the user's current request and valid continuing authorization. Publishing, global installation, history rewrites, deployment, and other-project changes require scope covering the actual action. A prior pilot, local commit, or available credential does not expand that scope.
