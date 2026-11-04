# Finite checks and repository validation

All scripts use Python 3.11+ and the standard library. Run them from the
repository root; see [REPRODUCING.md](../REPRODUCING.md) for commands.

| File | Role |
| --- | --- |
| [check_singular_fibres.py](check_singular_fibres.py) | Alternate-field finite parametrization, exceptional-fibre and lift checks |
| [check_extensions.py](check_extensions.py) | Five finite suites: algebra, profile, reflection, deletion and CRT |
| [check_repository.py](check_repository.py) | Links, checksums, source equations and recorded-output integrity |
| [limits.py](limits.py) | Fresh output directories and fixed cooperative resource limits |

The two mathematical scripts derive from the separately implemented
historical verifiers. Their mathematical test bodies are retained; standalone
argument handling, output creation, deadline checks and nonzero limit exits
were added for this public repository. Original code and exact run snapshots
remain accessible through [HISTORY.md](../HISTORY.md); the current
[finite evidence](../evidence/README.md) remains in this checkout.
This adaptation is not an independent mathematical review.
