# Repository review and migration

5 November 2026. Editorial and reproducibility review; no new mathematical
claim, independent referee report or literature-priority assessment.

## Findings in the previous public layout

The top README introduced both the expanded paper and a second “Read the
proof” route for the old separated-only note. The latter's scope exclusions
could be mistaken for limits of the current theorem. The `manuscript/`
directory also mixed paper formats, preliminary proofs, workspace notes,
verifiers, receipts and export metadata. Several reproduction instructions
called `tools/run_job.py`, which was not distributed in this repository.
Multiple checksum/provenance files described different exports without an
obvious current entry point. A dated audit still described presentation
text that had subsequently been removed at the author's request.

## Changes

| Previous location | Current role/location |
| --- | --- |
| `manuscript/MANUSCRIPT.*` and integrated Markdown | [paper/](../paper/README.md), one current paper in three formats |
| Nested supplement and integrated audit | [review/](README.md), with the audit explicitly identified as historical |
| Workspace-dependent verifier entry points | [code/](../code/README.md), standalone bounded Python commands |
| `manuscript/runs/` | [evidence/runs](../evidence/README.md), unchanged historical public bytes |
| Initial C021 note, SVG assets and ZIP | [archive/c021-original](../archive/c021-original/C021_REVIEW_NOTE.md) |
| Preliminary proofs, workspace instructions and older manifests | [archive/](../archive/README.md) |
| Competing root guides and checksum manifests | A short root README, [REPRODUCING.md](../REPRODUCING.md), and one current [checksum manifest](../SHA256SUMS.txt) |

Every previously tracked file is preserved byte-for-byte at a location in
[RELOCATION.json](../evidence/RELOCATION.json). Current reader-facing files
are derived copies with working navigation. Frozen archive documents can
retain obsolete workspace paths; they are explicitly distinguished from
current instructions. Old URLs on `main` follow the path migration; the
preceding Git commit remains an immutable record of the original layout.

The paper retains Sage Kim, Peking University, and the requested removal
of its AI-assistance paragraph. Its mathematics is unchanged. Only its
supplement hyperlink destination changed during this reorganization.
Separate review history and limitations remain intact.

## Validation

The [restructuring validation](../evidence/RESTRUCTURE_VALIDATION.json)
records comparison of unchanged mathematical test functions against the
archived originals, six fresh finite-suite runs, and PDF checks. Current
repository validation checks links, checksums, every preserved historical
file, displayed mathematics, labels and author/source metadata. All 11 PDF
pages were rendered for visual inspection after recompilation.

Resource/output handling was adapted for standalone execution. These
changes do not add an asymptotic rate, extend a finite search range or
establish independent mathematical verification. Historical run records
were moved without rewriting their fields. New finite results and build
provenance are recorded separately from those historical receipts.
