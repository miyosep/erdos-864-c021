# Reproducing the paper and finite checks

Run the commands below from the repository root. Python 3.11+ and its
standard library are sufficient for the checks; no private workspace,
package installation or unbundled research runner is needed.

## Check the repository

```text
python code/check_repository.py
```

This checks current local links, distribution checksums, recorded finite
outputs, author metadata in the TeX source, all 51 displayed expressions and
equation labels (1)–(28). It does not verify the mathematical proofs.

## Check singular fibres and integer lifts

```text
python code/check_singular_fibres.py
```

This uses the alternate field model $X^2-X-d$ and checks all primitive
elements and modular targets for $p=3,5,7$, the three stated cuts, integer
carry selection and fixed-grid geometry. Exact scope and recorded counts
are in the [computational supplement](review/COMPUTATIONAL_SUPPLEMENT.md).
The new output is `results/singular-fibres/outputs/singular_uniform.json`.

## Run the other finite suites

```text
python code/check_extensions.py audit
python code/check_extensions.py limits
python code/check_extensions.py reflection
python code/check_extensions.py deletions
python code/check_extensions.py crt_lifts
```

| Mode | What it checks | Declared finite scope |
| --- | --- | --- |
| `audit` | Modular parametrization, exceptions and row character sums | All primitives for $p=3,5$; one specified primitive for $p=7$ |
| `limits` | Exact integer counts against the proposed limiting profile | Specified bases/cuts for $p=3,5,7,11,17,23,31$ |
| `reflection` | Direct admissibility and optimization over integer heights | All primitive/cut bases for $p=3,5$ |
| `deletions` | The deletion-loss inequality | Every nonempty Sidon subset of $[1,7]$, every deletion and relevant sum |
| `crt_lifts` | CRT preimages and exact carry boundaries | All primitives, targets and cuts for $p=3,5$ |

Detailed qualifications, including floating arithmetic used in the small
character-sum checks, are in the [computational supplement](review/COMPUTATIONAL_SUPPLEMENT.md).
New outputs go to `results/<mode>/outputs/<mode>.json`.

Each command uses one worker, at most 2,000,000 declared state visits,
1,000,000 periods and a cooperative 300-second deadline. These bounds are
checked inside the scripts; no machine-wide memory or CPU quota is claimed.
Existing `MATH_*` bounds may be lower, but cannot exceed these caps.

Output directories must be fresh. For another run, choose a new path:

```text
python code/check_singular_fibres.py --output results/singular-repeat
python code/check_extensions.py audit --output results/audit-repeat
```

Require `status: "PASS"` and `truncated: false` in the JSON output.
`LIMIT`, a timeout, an exception or a nonzero exit is not a completed check.
Results are finite consistency evidence, not proofs of the asymptotic limit,
the external character theorem, novelty or general Erdős #864.

## Build the PDF

From `paper/`, with Tectonic 0.17.0:

```text
tectonic --untrusted main.tex
```

The first build may download standard TeX packages. All document sources,
including the bibliography, are in `main.tex`; no Pandoc step is required.
The distributed PDF is built with Tectonic. XeLaTeX is a possible alternative
but was not used for this export. Local builds can produce different PDF
bytes (for example, timestamps); distribution checksums refer to the shipped
files, not every subsequent local build.
