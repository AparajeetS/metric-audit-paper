# Governance

Marginal Baseline Evaluation is an open research project currently maintained
by Aparajeet Shadangi. The goal of this policy is to make scientific and
software decisions inspectable while the contributor community is small.

## Decision Principles

1. Reproducibility takes priority over a cleaner narrative.
2. Confirmatory and exploratory analyses must be labeled separately.
3. Protocol, target, metric, or threshold changes after results are observed
   must be versioned and disclosed.
4. Negative results and known validity failures remain available for provenance.
5. Backward compatibility is preferred for the package; breaking changes
   require a major version or a documented migration path.

## Roles

- **Maintainer:** reviews changes, manages releases, and protects credentials.
- **Contributor:** proposes code, documentation, experiments, or independent
  replications through issues and pull requests.
- **External auditor:** may report reproduction failures or methodological
  objections without contributing code.

As the project gains regular contributors, maintainers may be added based on a
record of technically sound reviews and adherence to the decision principles.

## Change Process

- Software fixes require tests when behavior changes.
- Research changes require a claim-scope note and reproduction command.
- Protocol changes require a dated document or pull request before new
  confirmatory results are inspected.
- Releases require passing tests, successful package build, `twine check`, and
  release notes.
- Material scientific disagreements should remain visible in issue or pull
  request history, with the resolution and evidence recorded.

## Continuity

The MIT license permits independent continuation. If active maintenance stops,
the code, package source, protocols, and committed artifacts remain forkable.
No proprietary service is required to execute the core CPU audit.
