# Product review

Read this reference when the request reviews how a feature, a flow, or the whole product behaves for its users.

## Target

Fix the flows, user roles, locales, viewports, and the build or environment under review. Use the verification environments the project approves; production or live data needs authorization that covers it.

## Method

Walk each flow as each role would:

- entry points, the main path, and completion
- empty, loading, error, and permission-denied states
- retry, double submission, back navigation, and reload persistence
- keyboard use, labels, focus, and contrast
- every supported locale and a narrow mobile viewport

For a question about how something should look or behave, build a throwaway comparison with the installed `prototype` skill instead of filing a guess.

## Evidence

Record reproduction steps with the environment, the observed and expected behavior, and screenshots kept in the project's ignored evidence location. Describe screenshots in the issue rather than linking private files.

Keep two kinds of findings apart. A defect contradicts stated or documented behavior and becomes an implementation issue. A proposal is a judgment about a better experience; one with open choices becomes a decision issue.

The review is done when every flow in scope has been walked for every role, locale, and viewport in scope, and each finding is classified as a defect or a proposal.
