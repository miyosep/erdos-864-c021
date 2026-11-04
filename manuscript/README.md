# External-review manuscript

Read the [typeset paper](MANUSCRIPT.pdf), or edit the complete
[LaTeX source](MANUSCRIPT.tex). The bibliography is embedded in that source;
no separate database is required. The [Markdown manuscript](proofs/quadratic_bose_chowla_integer_counts.md)
is also retained. This is the expanded manuscript, superseding the old
separated-reflection note for the results stated here.

Theorem 1 is the uniform integer representation estimate. Corollary 1.1
deduces sublinear deletion stability and optimal span over every integer
reflection height. The scope is the specified quadratic Bose--Chowla
construction family. This is not a resolution of general Erdős #864.
AI assistance, same-model review and the absence of established independent
or formal verification are disclosed in the paper. No novelty is claimed.

## Build the paper

From this directory, with Tectonic 0.17.0:

```text
tectonic --untrusted MANUSCRIPT.tex
```

XeLaTeX can also compile the source (two passes), with Latin Modern fonts
and the standard packages named in its preamble. Only Tectonic was tested
for this export. The source contains no shell-escape requirement or external
bibliography dependency. The TeX package bundle may need network access on
the first Tectonic build. Build-tool binaries are not redistributed here.

## Review and finite evidence

- [Computational supplement](notes/c021_editorial_20261105/COMPUTATIONAL_SUPPLEMENT.md)
- [Mathematical and literature gap audit](proofs/audit_20261105_integrated.md)
- [Editorial revision record](notes/c021_editorial_20261105/REVISION_REVIEW.md)
- [Earlier finite-suite scopes](tests/C021_EXTENSIONS_TESTS.md)
- [Alternate-field verifier](verifiers/review_c021_singular_uniform.py)
- [Export provenance and original/public hashes](PUBLIC_EXPORT.json)
- [Current byte checksums](SHA256SUMS.txt)

The `runs/` subtree contains selected successful historical runs, their
code/input snapshots and receipts. It is not a report of new executions.
Some superseded runs mentioned in the historical guides are not exported.
Local home paths in public evidence copies are replaced by `<USER_HOME>`;
receipt hash fields still identify the original local bytes. The export
manifest distinguishes those from actual public-copy hashes.

The historical guides show commands for the original full workspace and
its bounded runner, which is not bundled here. For a standalone rerun of
the alternate-field verifier, Python 3.11+ and its standard library suffice.
From this directory, the following example supplies the same caps and a
300-second foreground timeout. It writes a fresh directory and preserves
the historical outputs. Do not increase caps after a limit result.

```python
import os
from pathlib import Path
import subprocess
import sys

run = Path("local-singular-check")
run.mkdir()  # A fresh directory is required.
env = dict(os.environ, MATH_MAX_STATES="2000000",
           MATH_MAX_PERIOD_ENUMERATION="1000000",
           MATH_MAX_PARALLEL_WORKERS="1", MATH_RUN_DIR=str(run.resolve()))
subprocess.run([sys.executable, "verifiers/review_c021_singular_uniform.py"],
               env=env, check=True, timeout=300)
```

Check `status == "PASS"` and `truncated == false` in the resulting
`outputs/singular_uniform.json`; process success alone is insufficient.
The other finite-suite modes can use the same environment and timeout,
substituting `experiments/check_c021_extensions.py` followed by a mode
from the finite-suite guide. Each call needs a fresh output directory.
No finite computation proves the asymptotic theorem, priority, the cited
character estimate or the general Erdős conjecture.
