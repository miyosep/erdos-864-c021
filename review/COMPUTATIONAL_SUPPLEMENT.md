# Computational supplement

This accompanies the [current paper](../paper/main.pdf). No experimental
result is a premise of its proofs. [REPRODUCING.md](../REPRODUCING.md)
gives commands; [FINITE_CHECKS.json](../evidence/FINITE_CHECKS.json) records
executions and [evidence/results](../evidence/results/) holds complete outputs.

## Review status

The argument review is same-model/self-checking. AI assistance and separately
implemented finite tests do not establish independent expert review or formal
verification. Internal proof labels are not premises. Novelty and the general
Erdős #864 upper bound are not established.

## Exact finite scopes

| Check | Scope and qualifications |
| --- | --- |
| Alternate-field singular fibres | In F_p[X]/(X^2-X-d), all primitives and modular targets for p=3,5,7; cuts 0, floor(M/3), M-1; all possible integer lifts and rational fixed-grid geometry. 992 primitive/target cases, 452448 selectors, 775680 states, 4211 periods. Singular maxima 6,10,14; omitted maxima 13,27,39. |
| `audit` | All primitives and targets for p=3,5; first specified primitive and all targets for p=7; 272 targets. Modular first-three-coordinate enumeration, parametrization, exceptions and row sums; all row modes for p <= 5, three specified modes for p=7. |
| `limits` | First primitive in the least-nonresidue field for p=3,5,7,11,17,23,31; cuts 0, floor(M/3), M-1; 21 distributions, all integer s in [-M,3M]. Rational profile and exact counts, direct quadruples for p <= 5. |
| `reflection` | All 224 primitive/cut bases for p=3,5, every height in the mathematically sufficient finite optimization interval, direct diagonal-sensitive admissibility. |
| `deletions` | All 56 nonempty Sidon subsets of [1,7], every deletion and relevant sum; 5586 sum/deletion checks. |
| `crt_lifts` | All primitives, targets and cuts for p=3,5; exact degree-less-than-five CRT preimages for 584 retained rows; 122592 modular-witness/cut checks, including 10648 zero/one boundary cases. |

All six recorded public-code runs completed with `PASS`, one worker and no
truncation under the fixed caps. Small character-sum checks use floating
complex arithmetic with tolerance 10^-9, not certified interval arithmetic.
Finite counts do not prove asymptotics, relative boundary error, a prime
threshold, the external character estimate or priority.

## Verification evidence

The two mathematical implementations use different field models and were
written in the same model context. Standalone arguments, fresh outputs,
resource bounds and nonzero limit exits support reproducible execution.
The evidence records execution details, executed-code hashes, dependencies
and output hashes. Each result explicitly records that independent expert
review and formal verification have not been established.

The [gap audit](GAP_AUDIT.md) provides the algebra and literature comparisons.
Repository checks establish source/link/file integrity, not mathematical
correctness. Finite success does not replace checking the proof and its
stated external character estimate.
