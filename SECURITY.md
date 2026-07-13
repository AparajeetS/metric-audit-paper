# Security Policy

## Supported Versions

Security fixes are applied to the latest released `mbe-eval` version. Older
versions may receive fixes when the change is low risk and backward compatible.

## Reporting A Vulnerability

Do not include credentials, private data, or an unpatched exploit in a public
issue. Use GitHub's private vulnerability reporting for this repository. If that
feature is unavailable, contact the maintainer using the email listed in the
package metadata.

Include the affected version, reproduction steps, impact, and any proposed
mitigation. Acknowledgement is targeted within seven days. Publication timing
will be coordinated after a fix or mitigation is available.

## Scope

The package reads user-supplied CSV files and can write Markdown reports. It
does not execute code from those files or require network access for the core
audit. Training scripts and third-party notebook environments have separate
dependency and credential risks.

Never commit Kaggle, PyPI, cloud, or GitHub tokens. Revoke any credential that
has appeared in a notebook, terminal transcript, issue, or chat.
