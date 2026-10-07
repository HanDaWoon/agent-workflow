# Feature research

Read this reference when the request explores a new feature or develops an idea toward something buildable.

1. **Need:** state the user's problem and the outcome they expect. Search the codebase by domain concept, the open and closed issues, and recorded decisions for what already exists or was rejected.
2. **Facts:** gather external facts, such as APIs, libraries, platform policies, and comparable products, with the installed `research` skill when delegation authority covers it. Keep its output in an ignored location and cite it.
3. **Decisions:** resolve user-owned choices one at a time with the installed `grilling` skill, each with a recommendation. Use `domain-modeling` for new terms and `codebase-design` for interfaces and seams. Record each settled choice durably, as a decision issue closed with the answer or an ADR, so implementation issues can cite it. A choice the user has not made becomes an open decision issue with options, a recommendation, and evidence; silence does not settle it.
4. **Shape:** slice the settled parts into behaviors under [Issue authoring](issue-authoring.md). When the idea is still too open for near-term slices, file a parent with its open questions and recommend `wayfinder` or `to-spec` to the user.

The research is done when every choice is decided, filed as a decision issue, or listed as open in the parent.
