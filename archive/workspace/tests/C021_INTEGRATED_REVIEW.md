# Reproduce the integrated-manuscript review

Editorial update, 2026-11-05: the manuscript and current document checker
have since been revised for external review. Use C021_EDITORIAL_REVIEW.md
for the current document-check command and expectations. The commands and
counts below describe the earlier integrated draft; its original checker
is preserved in notes/c021_editorial_20261105/document_checker_before_revision.py
and in the historical run snapshots. Mathematical finite-check scopes below
remain historical evidence, not newly rerun results.

Session e864_20261105_04_manuscript, 5 November 2026 Asia/Shanghai.
No old theorem label is a premise. All code is newly written standard-library
Python 3.11+ and imports no historical research implementation. Exact caps
are enforced; no resource increase, seed rotation or background process.

From the workspace root:

```powershell
python tools/run_job.py --problem erdos_864 --session e864_20261105_04_manuscript --code verifiers/review_c021_singular_uniform.py --input proofs/investigation_20261105_manuscript.md --input proofs/c021_uniform_local_limit.md -- python verifiers/review_c021_singular_uniform.py
python tools/run_job.py --problem erdos_864 --session e864_20261105_04_manuscript --code verifiers/check_integrated_manuscript.py --input proofs/quadratic_bose_chowla_integer_counts.md --input proofs/audit_20261105_integrated.md -- python verifiers/check_integrated_manuscript.py
```

Reuse the logical session identifier and unchanged budgets; never rotate
identifiers to bypass accounting. Each invocation produces a fresh receipt
with code/input/output hashes and snapshots. No randomness is used; the
seed is null. State counts are declared candidate/check visits, not scalar
operations or a CPU quota. LIMIT/truncation is not a full-scope pass.

## Mathematical finite checks

Final run: ../runs/20261104T181514-4b2df1bfafdd4ddaa11e3afe0f6d3c8c/.
The field model is F_p[X]/(X²−X−d), with least d having nonsquare
discriminant. This differs from the earlier X²−d implementation.
It checks ALL primitive theta and ALL gamma for p=3,5,7: respectively
4×8, 8×24, 16×48, total 992 targets. Cuts are 0,floor(M/3),M−1;
all possible integer lifts of each residue are checked. The selector
counts total 452448; both zero and one boundaries occur 3964 times.

Direct first-three-coordinate enumeration checks the complete fibre,
the real-z singular classification, at most two z=1 parameter pairs,
at most four excluded rows, retained size and the full ≤6p complement.
Observed singular maxima are 6,10,14 and omitted maxima 13,27,39.
Rational grid geometry is checked at sizes 2,5,13 across all changes
of grid/slab combinatorial regimes. PASS: 775680 states, 4211 periods,
one worker, no truncation.

The prior run 20261104T181440-09ad3b183e394129930b72d865cbf0ad is
preserved. Its unused max_small_profile_error=0 field was removed:
this verifier does not compute a profile error. The field must not
be interpreted as exact agreement with the local limit. The real
algebra/carry checks passed again in the final replacement run.

## Document integrity checks

Final run: ../runs/20261104T183223-4238d218143d4d65b76a9729d188cca5/.
It checks 51 display expressions, 28 equation labels, inline math,
balanced braces, reviewed TeX command spelling, requested section order,
six lemma headings, three corollary headings and 14 source links.
It checks for accidental control characters and workspace-only placeholders.
This is not visual rendering, a full TeX parser, proof verification or
verification of the linked external literature.

The initial checker run 20261104T182921-a1ed8efbe7194ec798ad388150c79495
failed on its own incomplete allowlist for valid cap/mu/quad commands.
Its failure is retained; the corrected final check passed. No mathematical
claim is inferred from either document-check status.

The intermediate successful run
20261104T182954-14a687b6899d46e28970e16f0772e671 is also retained.
The final run above includes the explicit definition x_+=max(x,0) added
to the manuscript; the document checker itself is unchanged.

All finite computations remain evidence in precisely their tested scope.
They cannot prove a uniform asymptotic limit, the external character
estimate, novelty or Erdős #864. Mathematical arguments and the literature
boundary are in ../proofs/audit_20261105_integrated.md. Existing historical
extension suites and their receipts remain in C021_EXTENSIONS_TESTS.md.
