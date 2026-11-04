# Evidence and provenance

This directory holds exact finite outputs and receipts. Read the
[computational supplement](../review/COMPUTATIONAL_SUPPLEMENT.md) for their
meaning and limitations, and [REPRODUCING.md](../REPRODUCING.md) to run checks.

| Historical check | Recorded output |
| --- | --- |
| Parametrization and exceptions | [audit.json](runs/20261104T175510-6afeb6b3f17842be9d99641ed0124910/outputs/audit.json) |
| Integer-count profiles | [limits.json](runs/20261104T175733-c6d3cbeb565d409893af79af248dcf8a/outputs/limits.json) |
| All-height reflection | [reflection.json](runs/20261104T175850-be97a2607144487cafb7d168e3dadbdc/outputs/reflection.json) |
| Deletion loss | [deletions.json](runs/20261104T175904-d73cf14c34d84b19a449bb061ff15d13/outputs/deletions.json) |
| CRT and carry boundaries | [crt_lifts.json](runs/20261104T180322-796e9a7a704040da87b2c1dbe1b4775d/outputs/crt_lifts.json) |
| Alternate-field singular fibres | [singular_uniform.json](runs/20261104T181514-4b2df1bfafdd4ddaa11e3afe0f6d3c8c/outputs/singular_uniform.json) |
| Earlier document integrity | [document_checks.json](runs/20261104T185004-55eae0993e3844abb0e74db4d7c3c560/outputs/document_checks.json) |

Each linked output has a neighbouring receipt and exact code/input snapshots
in its run directory. These are selected historical successful runs; some
superseded runs mentioned in archived guides are not distributed here.
Original user-home paths were redacted before publication; historical receipt
hash fields still identify the original local bytes. Earlier export manifests
are preserved under [archive/workspace/](../archive/workspace/README.md).

[RELOCATION.json](RELOCATION.json) maps every file from the preceding public
commit to its byte-preserved location. Frozen receipts and snapshots retain
their historical paths; consult this map rather than editing those records.
The current distribution has one checksum manifest at the repository root.
Hashes check file integrity, not mathematical correctness.

The standalone public-code adaptation was checked again during the
reorganization. [RESTRUCTURE_VALIDATION.json](RESTRUCTURE_VALIDATION.json)
records six fresh finite-suite executions, unchanged mathematical-function
comparisons and PDF checks. Their outputs are in
[restructure-2026-11-05/](restructure-2026-11-05/); [BUILD.json](BUILD.json)
records current paper and code hashes. These are separate from the historical
runs above and do not expand their mathematical scope.
