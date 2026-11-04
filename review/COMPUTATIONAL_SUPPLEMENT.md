# Computational supplement

This accompanies the [current paper](../paper/main.pdf). No experimental
result is a premise of its proofs. [REPRODUCING.md](../REPRODUCING.md)
gives commands; [FINITE_CHECKS.json](../evidence/FINITE_CHECKS.json) records
executions and [evidence/results](../evidence/results/) holds complete outputs.

## Review status

The argument review is same-model/self-checking. AI assistance and separately
implemented finite tests do not establish independent expert review or formal
verification. Internal proof labels are not premises. Novelty and the general
Erdős #864 upper bound are not established. Original review history remains
accessible through [HISTORY.md](../HISTORY.md).

## Exact finite scopes

| Check | Scope and qualifications |
| --- | --- |
| Alternate-field singular fibres | In $F_p[X]/(X^2-X-d)$, all primitives and all modular targets for $p=3,5,7$; cuts $0,lfloor M/3
floor,M-1$; all possible integer lifts and rational fixed-grid geometry. 992 primitive/target cases, 452448 selectors, 775680 states, 4211 periods. Singular maxima $6,10,14$; omitted maxima $13,27,39$. |
| `audit` | All primitives and targets for $p=3,5$; first specified primitive and all targets for $p=7$; 272 targets. Modular first-three-coordinate enumeration, parametrization, exceptions and row sums; all row modes for $ple5$, three specified modes for $p=7$. |
| `limits` | First primitive in the least-nonresidue field for $p=3,5,7,11,17,23,31$; cuts $0,lfloor M/3
floor,M-1$; 21 distributions, all integer $sin[-M,3M]$. Rational profile and exact counts, direct quadruples for $ple5$. |
| `reflection` | All 224 primitive/cut bases for $p=3,5$, every height in the mathematically sufficient finite optimization interval, direct diagonal-sensitive admissibility. |
| `deletions` | All 56 nonempty Sidon subsets of $[1,7]$, every deletion and relevant sum; 5586 sum/deletion checks. |
| `crt_lifts` | All primitives, targets and cuts for $p=3,5$; exact degree-less-than-five CRT preimages for 584 retained rows; 122592 modular-witness/cut checks, including 10648 zero/one boundary cases. |

All six recorded public-code runs completed with `PASS`, one worker and no
truncation under the fixed caps. Small character-sum checks use floating
complex arithmetic with tolerance $10^{-9}$, not certified interval arithmetic.
Finite counts do not prove asymptotics, relative boundary error, a prime
threshold, the external character estimate or priority.

## Provenance

The original mathematical implementations used different field models; both
were written in the same model context. The public adaptation adds standalone
arguments, fresh outputs, bounded resource handling and nonzero limit exits.
Mathematical-function comparisons with the original code were recorded before
archival pruning. Their exact immutable snapshot is linked in the finite-check
provenance. Inherited implementation-independence flags refer to the original
implementation history, not to a new independent reviewer.

This checkout retains code, six complete outputs, execution details and hashes.
Older receipts, code/input snapshots, failures and manifests remain in Git
history. They were not rewritten as new successful checks or silently combined
with fresh results. Unexamined feedback-reported tests are not adopted evidence.

The [gap audit](GAP_AUDIT.md) retains substantive algebra and literature
comparisons. Repository checks establish source/link/file integrity, not
mathematical correctness. Neither finite success nor old labels replace
checking the proof and its stated external character estimate.
