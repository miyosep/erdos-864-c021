# Repository structure and retention review

5 November 2026. Reader-facing editorial/reproducibility review; no new
mathematical result, independent referee report or priority assessment.

## Findings and structure

The old README offered both the expanded paper and a second “Read the proof”
route for the separated-only C021 note. Paper formats, preliminary proofs,
verifiers, session notes, raw run trees and metadata were mixed. Some commands
called an unbundled private-workspace runner. Several manifests described
different historical distributions.

The current README leads to one paper. `paper/` holds its three formats;
`review/` holds substantive review; `code/` has standalone bounded scripts;
`evidence/` contains current results and provenance. There is one current
checksum manifest and a reproduction guide.

## Are historical files needed in the checkout?

| Material | Decision and reason |
| --- | --- |
| Current PDF, TeX and Markdown | Keep: reading, editing and source inspection |
| Critical proof/literature audit and finite scope | Keep substantive content: assessing the argument and limitations |
| Verifiers and six full outputs with provenance | Keep: offline inspection and reproduction |
| Initial C021 note, SVG equations and original ZIP | Git history: superseded narrower exposition |
| Repeated preliminary proofs | Git history: integrated into the current paper |
| Plans, session logs, status labels and old manifests | Git history: bookkeeping rather than reader prerequisites |
| Historical run trees with repeated code/input snapshots | Git history: not required to run current deterministic checks |
| Entire old paper solely for equation comparison | Replace with 51 frozen equation hashes and immutable source reference |

The first reorganization conservatively archived every file. After the user's
request to assess necessity, that bulk was removed from the current tree.
The preceding commit preserves every original byte and is linked from
[HISTORY.md](../HISTORY.md). A separate local backup was retained. Git history
was not force-rewritten and review status was not promoted.

## Validation and limits

Six public finite suites passed under unchanged caps. Mathematical functions
were compared with the prior code before pruning; the pinned context and exact
outputs are in [FINITE_CHECKS.json](../evidence/FINITE_CHECKS.json). Pruning did
not change mathematical verifier code or test bounds.

Repository validation checks links, full checksum coverage, six recorded
outputs, 51 displays against the frozen baseline, 28 tags and author/source
metadata. Sage Kim, Peking University, and the requested manuscript presentation
are retained. All 11 PDF pages were inspected after updating its supplement link.

Current reading and checks require no old archive. Historical forensic
reconstruction requires the pinned Git snapshot, where complete old receipts
and failures remain available. This retention decision does not certify
mathematical correctness or literature priority.
