# Computational supplement and verification record

This supplement belongs to the external-review draft
[Uniform integer representation counts and reflected spans for quadratic
Bose–Chowla sets](../../proofs/quadratic_bose_chowla_integer_counts.md).
No numerical result is a premise of its proofs.

## Verification status

The project records C054–C059 as PROVED / SELF_CHECKED with novelty
NOT_CHECKED. These are internal research-management labels, not independent
refereeing or formal proof certification. The mathematical argument and the
precisely stated external character theorem must be checked directly.
The manuscript was prepared with AI assistance; no independent expert
review or formal verification has been established by these records.

## Locally executed checks

The first independently written implementation of the field formulas used
F_p[X]/(X²−d); an alternate verifier used F_p[X]/(X²−X−d) and imported
no historical research code. Both were written in the same model context,
so implementation independence does not imply an independent reviewer.

The alternate verifier tests every primitive element and every modular
target for p=3,5,7, selected translations 0,floor(M/3),M−1, every possible
integer lift, and rational fixed-grid boundary geometry. The successful
final run checked 992 primitive/target cases and 452448 witness/cut/lift
selectors. Singular maxima were 2p; omitted maxima were 13,27,39.
There were 775680 declared state visits, 4211 periods, one worker and
no truncation. These numbers describe only that finite computation.

Exact final run and code:

* [Alternate-field output](../../runs/20261104T181514-4b2df1bfafdd4ddaa11e3afe0f6d3c8c/outputs/singular_uniform.json)
* [Receipt](../../runs/20261104T181514-4b2df1bfafdd4ddaa11e3afe0f6d3c8c/receipt.json)
* [Verifier](../../verifiers/review_c021_singular_uniform.py)
* [Reproduction and full scope](../../tests/C021_INTEGRATED_REVIEW.md)

Earlier checks include direct integer histograms, small quadruple
enumeration, all small primitive/cut reflected unions, every deletion of
small Sidon subsets, and explicit CRT preimages. Their distinct scopes,
actual receipts and superseded checker revisions are retained in the
[original extension test guide](../../tests/C021_EXTENSIONS_TESTS.md).
They are not merged into a misleading single search bound or total.

## Feedback-reported tests not adopted as verified evidence

The user supplied a review reporting 1568 modular fibres and 520576
integer selectors, including some p=11,13 choices, and a ZIP link from
an external sandbox. This session has not read or executed that artifact.
Those figures are recorded as feedback reports only. They are not added
to the locally executed totals, described as reproduced, or treated as
independent mathematical verification. No code was imported from the
unexamined ZIP and no licensing assumption was made for it.

## Detailed audit and document checks

The [full mathematical and literature audit](../../proofs/audit_20261105_integrated.md)
records the singular-fibre, CRT, fixed-grid and integer-carry arguments,
source access levels and independent-review limitations. The
[editorial change record](REVISION_REVIEW.md) distinguishes the present
expository revision from new mathematical work. Historical receipts and
original code/input/output hashes are preserved.

Document-integrity checks validate equation source, numbering, grouping,
references and section order. Workspace tests validate infrastructure.
Neither validates the mathematics. No finite table proves the uniform
asymptotic theorem, the external character estimate, a prime threshold,
literature priority or the general Erdős #864 conjecture.
