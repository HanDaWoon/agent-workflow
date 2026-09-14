# Planning and issue decomposition

Synthesize the objective already established in the conversation, issues, and ADRs. Distinguish unresolved choices affecting user intent from technical facts discoverable in the repository. Do not ask the user to explain information the agent can investigate.

## When a decision blocks implementation

Record the question that must be resolved, the costs of the options, a recommendation, and supporting evidence. Decision work is complete when it provides an evidence-backed answer and identifies remaining uncertainty. Do not expand a design request into feature development unless implementation was requested.

Keep the overall direction coarse and create detailed issues only for near-term implementation whose acceptance criteria can be stated now. Do not introduce approval steps for settled decisions. Choices requiring the user's judgment remain proposals until answered; silence does not finalize them.

## Implementation issue size

- Each issue delivers a narrow but complete behavior that can be verified independently. Describe observable outcomes rather than a list of files by technical layer.
- Connect only dependencies that actually block starting or completing work. Sharing a parent objective does not by itself require serial execution.
- If a broad mechanical change cannot pass independently, sequence it as expand → migrate → contract. If an intermediate integration branch is necessary, specify each stage's verification scope and ownership of final integration checks.
- Continue review fixes and retries under the same issue and change. Split out new work when it has different acceptance criteria.

Use the [issue template](../assets/issue.md) for drafts and fill only the fields relevant to implementation or decision work. GitHub owns requirements, dependencies, and final evidence; Orca owns detailed supervised execution logs. Follow existing labels and tracker conventions rather than adding new ones without a task need.
