# Finite evidence and source integrity

This directory keeps evidence needed to inspect or reproduce the current
code. Historical bulk is accessible through [HISTORY.md](../HISTORY.md).

| File | Purpose |
| --- | --- |
| [FINITE_CHECKS.json](FINITE_CHECKS.json) | Six actual runs, scope counters, runtime, output hashes and code-comparison provenance |
| [results/](results/) | Complete outputs for singular fibres, algebra, profiles, reflections, deletions and CRT/lifts |
| [BUILD.json](BUILD.json) | Paper/code hashes, compiler and visual-review record |
| [EQUATION_BASELINE.json](EQUATION_BASELINE.json) | Frozen hashes of 51 displays, with immutable source commit and path |

[REPRODUCING.md](../REPRODUCING.md) gives commands and interpretation.
The [supplement](../review/COMPUTATIONAL_SUPPLEMENT.md) states the ranges and
limitations. Running code needs no historical checkout or private workspace.
Old receipts identify earlier byte versions and paths; they remain at the
pinned commit rather than being edited to resemble current executions.

The root [SHA256SUMS.txt](../SHA256SUMS.txt) is the current distribution
manifest. Baseline hashes check source preservation, not mathematics.
No independent or formal verification is asserted by these files.
