# Code review

Read this reference when the request reviews code: a whole repository, an area, or a change range.

## Target

Fix the target before reading: the repository, named modules or directories, or a commit range, plus the base commit every permalink pins to. For a change range with delegation authority, the installed `code-review` skill fits; keep its Spec and Standards reports separate. For a repository or area audit, apply the same two axes as a technique and say that the skill itself did not run.

## Lenses

Read in order of consequence:

1. Security and authorization boundaries
2. Data loss and integrity
3. Concurrency, retries, and idempotency
4. Correctness against documented behavior, decisions, and domain rules
5. Compatibility: schema and migrations, public APIs, message catalogs
6. Tests and maintainability

Project instructions, ADRs, and domain docs define correct behavior. A smell with no violated rule and no observable cost is a judgment call; label it as one, and file it only as a proposal.

## Evidence

Each finding carries a reproduction, a failing or missing test at a named public seam, or a permalink pinned to the base commit together with the rule or spec line it violates. Confirm a root cause by tracing the actual code path or reproducing it. An unconfirmed cause stays a hypothesis and becomes a decision issue that names what must be confirmed, never an implementation issue that asserts it.

Have an independent reviewer re-check high-risk findings before they become issues, within delegation authority. Record which findings were independently checked.

The review is done when every lens has been applied to the whole target and each finding is verified, a labeled hypothesis, or dropped with a reason.
