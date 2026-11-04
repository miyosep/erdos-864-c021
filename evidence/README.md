# Finite evidence and source integrity

This directory keeps evidence needed to inspect or reproduce the current code.

| File | Purpose |
| --- | --- |
| [FINITE_CHECKS.json](FINITE_CHECKS.json) | Six actual runs, scope counters, runtime, executed-code hashes and output hashes |
| [results/](results/) | Complete outputs for singular fibres, algebra, profiles, reflections, deletions and CRT/lifts |
| [BUILD.json](BUILD.json) | Paper/code hashes, compiler and visual-review record |
| [EQUATION_BASELINE.json](EQUATION_BASELINE.json) | Frozen hashes of 51 displays, with immutable source commit and path |

[REPRODUCING.md](../REPRODUCING.md) gives commands and interpretation.
The [supplement](../review/COMPUTATIONAL_SUPPLEMENT.md) states the ranges and
limitations. The included code and results suffice for the documented checks.

The root [SHA256SUMS.txt](../SHA256SUMS.txt) is the current distribution
manifest. Baseline hashes check source preservation, not mathematics.
No independent or formal verification is asserted by these files.
