# Finite checks and repository validation

All scripts use Python 3.11+ and the standard library. Run them from the
repository root; see [REPRODUCING.md](../REPRODUCING.md) for commands.

| File | Role |
| --- | --- |
| [check_singular_fibres.py](check_singular_fibres.py) | Alternate-field finite parametrization, exceptional-fibre and lift checks |
| [check_extensions.py](check_extensions.py) | Five finite suites: algebra, profile, reflection, deletion and CRT |
| [check_repository.py](check_repository.py) | Links, checksums, source equations and recorded-output integrity |
| [limits.py](limits.py) | Fresh output directories and fixed cooperative resource limits |

The two mathematical scripts use different field models and share bounded
output/resource handling. The [finite evidence](../evidence/README.md) records
the executed scopes, outputs and provenance. Separately implemented code does
not constitute independent mathematical review.
