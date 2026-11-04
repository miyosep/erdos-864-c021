# C021: complete quadratic Bose–Chowla reflections

Research review draft and finite verification material related to Erdős problem #864.

**Review status: SELF_CHECKED only. Independent mathematical verification and
literature novelty remain unresolved. This repository does not claim a solution
of Erdős #864.** The proof exposition and code were prepared with Codex; the
stored internal `PROVED` label is not an independent correctness certificate.

## Read the proof

- [Standalone proof note](C021_REVIEW_NOTE.md), including all elementary premises.
- [Editable LaTeX source](C021_REVIEW_NOTE_SOURCE.txt).
- [C021 proof (display-safe copy)](proofs/bose_integer_carries.md).
- [Detailed same-model audit](proofs/audit_20261105_c021.md).
- [Download code, inputs and historical evidence](C021_review_packet.zip).
- [Finite package recheck](validation/finite_recheck.json).
- [Public-export provenance](PUBLIC_EXPORT.json) and [SHA-256 checksums](SHA256SUMS.txt).

For odd primes $p$, let $B_{p,\theta,t}$ be the **complete** $p$-element
degree-two Bose–Chowla logarithm base, with a primitive element $\theta$,
residue translation $t$, and representatives in $[1,p^2-1]$. Let
$L_{p,\theta,t}$ be the least inclusive interval length of an admissible
$B\cup(S-B)$ with integer $S>2\max B$, allowing an overall translation.
An admissible set has at most one repeated unordered pair sum, with diagonal
pairs included. The submitted claim is

![Uniform reflection-length limit](assets/equations/eq-04-light.svg#gh-light-mode-only)

![Uniform reflection-length limit](assets/equations/eq-04-dark.svg#gh-dark-mode-only)

The key intermediate claim is uniform coverage of every fixed compact interior
range of integer $3B-B$ heights, with at least $c_Jp^2$ ordered witnesses.
The note spells out the reduction from these discrete-log witnesses to a
nonprincipal polynomial Dirichlet character and then to the integer lift.

The scope is one-period positive representatives, complete prime degree-two
bases, and **separated** reflections. It does not cover arbitrary Sidon sets,
overlapping reflections, deletions, or prime powers. There is no explicit
prime threshold or asymptotic error rate.

## Reproduce the finite check

Download and extract the ZIP. It contains the original Python standard-library
verifier, its configuration, and historical data for only
$p=2,3,5,7,11,17,23,31$. From the extracted directory, with Python 3.11+:

```python
import os
from pathlib import Path
import subprocess
import sys
import tempfile

destination = Path(tempfile.mkdtemp(prefix="c021-check-"))
(destination / "outputs").mkdir()
environment = os.environ.copy()
environment.update(
    MATH_MAX_STATES="2000000",
    MATH_MAX_PERIOD_ENUMERATION="1000000",
    MATH_MAX_PARALLEL_WORKERS="1",
    MATH_RUN_DIR=str(destination),
)
subprocess.run(
    [sys.executable, "verifiers/check_bose_support.py",
     "experiments/session2_cycle3_verify.json"],
    env=environment, check=True, timeout=300,
)
print(destination / "outputs" / "support_verification.json")
```

The distributed packet was actually extracted and its bundled verifier rerun:
all eight archived cases passed, using 174895 counted states, one worker and
no truncation. These finite checks do **not** prove the asymptotic theorem or
provide independent mathematical review. Checksums establish file integrity.

## Sources and provenance

The exact character input is Keating–Rudnick,
[arXiv:1204.0708v3](https://arxiv.org/pdf/1204.0708v3), §3.4,
(3.31)–(3.33), applied at degree one to an explicitly constructed character.
The full source comparison, including Ortega–Prendiville (2023) and
Carter–O’Bryant–Tao, [arXiv:2610.36207v1](https://arxiv.org/abs/2610.36207v1),
is in the note and the ZIP's `SOURCES.md`. No novelty clearance is claimed.

The public ZIP is derived from the local review packet: local user-home paths
are replaced by `<USER_HOME>`, manifests are recalculated, and the standalone
note uses static SVG equations with a separate LaTeX source. Historical receipt hashes refer to the
original local files; changed public copies and original/public hashes are
identified in the export manifest. Third-party PDFs and external code are not
included. The original local research records are preserved. The ZIP also retains
byte-exact original proof/audit text in `archive/original_proofs/`; the
readable copies quote literal stars to avoid Markdown emphasis.

Publication does not change the mathematical review or novelty status.

Display equations are pre-rendered SVG assets for consistent layout, with light/dark variants. The original LaTeX is provided separately. Renderer provenance and license are in [assets/equations](assets/equations/RENDERING.md).
