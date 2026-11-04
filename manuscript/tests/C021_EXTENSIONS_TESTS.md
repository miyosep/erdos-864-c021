# Reproducible finite checks for the C021 extensions

Code: ../experiments/check_c021_extensions.py, Python 3.11+ standard
library only, deterministic, no imported historical research code or
third-party source code. No independent mathematician/formal review.

From the workspace root use the bounded runner, reusing this logical
session's identifier; do not enlarge its budgets or rotate session IDs
to avoid accounting. Each invocation creates a new receipt directory.

```powershell
python tools/run_job.py --problem erdos_864 --session e864_20261105_03_extensions --code experiments/check_c021_extensions.py --input proofs/investigation_20261105_extensions.md -- python experiments/check_c021_extensions.py audit
python tools/run_job.py --problem erdos_864 --session e864_20261105_03_extensions --code experiments/check_c021_extensions.py --input proofs/investigation_20261105_extensions.md -- python experiments/check_c021_extensions.py limits
python tools/run_job.py --problem erdos_864 --session e864_20261105_03_extensions --code experiments/check_c021_extensions.py --input proofs/investigation_20261105_extensions.md -- python experiments/check_c021_extensions.py reflection
python tools/run_job.py --problem erdos_864 --session e864_20261105_03_extensions --code experiments/check_c021_extensions.py --input proofs/investigation_20261105_extensions.md -- python experiments/check_c021_extensions.py deletions
python tools/run_job.py --problem erdos_864 --session e864_20261105_03_extensions --code experiments/check_c021_extensions.py --input proofs/investigation_20261105_extensions.md -- python experiments/check_c021_extensions.py crt_lifts
```

The script requires the runner's MATH_* limits and output directory.
One worker; caps are checked before candidate-state/cut expansion.
The seed is null because no randomness is used. State counts measure
declared inner candidate visits, not every scalar field operation.
An explicit LIMIT result records truncation; it cannot prove completion
of the declared scope. A FAIL result raises an error and retains the
partial output. An assertion failure or process timeout is not a pass.

## Final successful runs

| Mode | Run directory under ../runs/ | Exact finite scope |
| --- | --- | --- |
| audit | 20261104T175510-6afeb6b3f17842be9d99641ed0124910 | All primitive θ and all targets γ for p=3,5; first lexicographic primitive and all γ for p=7; 272 targets. Brute modular first-three-coordinate enumeration, rational formula/exception/singular-fibre/omitted bound; all row modes for p≤5, three specified modes for p=7. |
| limits | 20261104T175733-c6d3cbeb565d409893af79af248dcf8a | p=3,5,7,11,17,23,31; first primitive in least-nonresidue field; t=0,floor(M/3),M−1, 21 distributions, all integer s∈[−M,3M]. Rational profile and exact counts, direct quadruples p≤5. |
| reflection | 20261104T175850-be97a2607144487cafb7d168e3dadbdc | All 224 primitive/cut bases for p=3,5; every height in the mathematically sufficient finite optimization interval; diagonal-sensitive direct admissibility. |
| deletions | 20261104T175904-d73cf14c34d84b19a449bb061ff15d13 | All 56 nonempty Sidon subsets of [1,7], every deletion subset, every relevant sum; 5586 sum/deletion checks. |
| crt_lifts | 20261104T180322-796e9a7a704040da87b2c1dbe1b4775d | p=3,5, all primitive θ, all γ and t; exact degree<5 CRT polynomial preimages for 584 retained rows; 122592 modular-witness/cut checks, including 10648 zero/one boundary cases. |

Each outputs/<mode>.json records status, exact scope, state and period
counts and truncation; receipt.json has actual runtime, versions, command,
code/input snapshots and hashes. Historical revisions are preserved:
20261104T175706-e8b5e54f963443cfa49d191481cf1598 (profile calculation
partly floating) and 20261104T180257-edd87a296b3640acaf8c1b86a1541a33
(CRT supplement before removing redundant assertions). Use the final
replacements above. The audit code snapshot predates the profile fix,
which does not affect audit mode; its receipt identifies exact code.

These tests check finite algebra, code paths and examples. The
small-character-sum calculations use floating complex arithmetic with
10^−9 tolerance, not certified interval arithmetic. They do not prove
the published character theorem, any asymptotic statement, an error
rate, a threshold, novelty, or the general Erdős conjecture.
