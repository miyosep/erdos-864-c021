# Validate the external-review revision

The latest manuscript is proofs/quadratic_bose_chowla_integer_counts.md.
The preceding manuscript/checker are preserved in
notes/c021_editorial_20261105/. Mathematical results and all 51 displayed
expressions are unchanged; the main theorem/application hierarchy, history
and verification presentation were revised.

From the workspace root, using the current logical session and unchanged
caps:

```powershell
python tools/run_job.py --problem erdos_864 --session e864_20261105_07_editorial --code verifiers/check_integrated_manuscript.py --input proofs/quadratic_bose_chowla_integer_counts.md --input proofs/investigation_20261105_editorial.md --input notes/c021_editorial_20261105/manuscript_before_revision.md --input notes/c021_editorial_20261105/COMPUTATIONAL_SUPPLEMENT.md -- python verifiers/check_integrated_manuscript.py
```

Actual successful run:
../runs/20261104T185004-55eae0993e3844abb0e74db4d7c3c560/.
Its output is outputs/document_checks.json; its receipt preserves the exact
code, manuscript, mathematical before-snapshot, supplement and limits.

The checker verifies 51 display expressions and 28 sequential equation
labels, all display-math expressions unchanged modulo whitespace, revised
headings, the analytic theorem/application corollary distinction, local
supplement link, 18 external links and explicit verification/priority limits.
It also checks brace/delimiter/command spelling and excludes internal
status codes and unadopted feedback statistics from the manuscript.
These are document integrity checks, not proof or visual-render validation.

Prior finite mathematical tests were not rerun for this expository change.
Their actual scopes/receipts remain in C021_EXTENSIONS_TESTS.md and
C021_INTEGRATED_REVIEW.md and the computational supplement. To reproduce
historical checker behavior use its saved code snapshot, not the current
checker with its changed document expectations. No new reported external
sandbox tests have been imported, executed or certified.
