# mbe-eval v0.3.1

This maintenance release aligns the Python package with the renamed public
repository and clarifies the boundary between the stable MBE v1 audit and the
MBE 2.0 research program.

## Changes

- update all package, citation, documentation, and issue URLs to
  `AparajeetS/marginal-baseline-eval`;
- expose `mbe_eval.__version__` and `--version` in both command-line tools;
- add continuous integration across Python 3.9, 3.11, 3.13, and 3.14;
- add package build and metadata validation in CI;
- add explicit open-research, governance, security, and evidence-status docs;
- clarify that the 680-row v1 ledger is exploratory legacy evidence;
- publish the MBE 2.0 technical program and gated JMLR roadmap.

## Compatibility

There are no API-breaking changes from v0.3.0.
