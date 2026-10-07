# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## Commands

Python 3 standard library only; there is no dependency install or build step. `__pycache__/` is not gitignored, so suppress bytecode when running tests.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests                                         # all tests
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_connect.ConnectTests.test_preview_writes_nothing  # one test
claude plugin validate .                         # Claude marketplace manifest
claude plugin validate plugins/agent-workflow    # Claude plugin manifest
python3 scripts/connect.py --project <git-root> --agent claude|codex|both   # preview; add --apply to write
```

## Architecture

The product is a Markdown skill; the only code is the development connection script.

- **Package:** `plugins/agent-workflow/` is the sole shipped unit. Its Codex and Claude manifests share one `skills/engineering-workflow/` tree. Bump `version` in both `plugin.json` files together when releasing package changes. The root marketplaces (`.claude-plugin/`, `.agents/plugins/`) point at the package path and never copy skill content.
- **Skill as router:** `SKILL.md` holds the Entry table that sends each request type to one owning reference (`planning`, `execution`, `completion`, `project-manager`, `skill-composition`). Edit a policy in its owning reference, then check the Korean summaries in `docs/workflow.md` and `README.md` for consistency. `assets/` holds the Korean user-facing output templates.
- **Adopter templates:** `templates/` sits outside the package. It is copied into adopting projects by hand and is not installed with the plugin.
- **Root `skills` symlink:** it points to `plugins/agent-workflow/skills` and preserves legacy absolute-path pointers. `scripts/connect.py` and the tests resolve the skill through it, so keep it a relative symlink.
- **Live propagation:** projects connected with `connect.py` or a hand-written absolute pointer to `SKILL.md` read this checkout directly, so skill edits reach them on their next read. Plugin installs see changes only after a version bump and update.
- **`connect.py` contract:** it previews by default and appends a managed block between `agent-workflow:begin`/`agent-workflow:end` markers. On any conflict it refuses instead of merging: a different existing link, a modified block, a symlinked or hardlinked instruction file, `AGENTS.override.md`, or an existing `engineering-workflow` mention. Blocks carrying an earlier release's entry wording are accepted unchanged with a notice; when changing the block wording, move the old entry into `EARLIER_ENTRIES` so connected projects stay valid. It validates every path before the first write and re-plans after `--apply` to verify. Its messages are Korean.
- **Tests:** `tests/test_connect.py` runs the script as a subprocess against disposable Git repos and asserts that refused runs leave every file byte-identical. Add a test for each new refusal case.
