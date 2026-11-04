# Quadratic Bose–Chowla integer counts and reflected spans

**Sage Kim · Peking University**

**[Read the paper (PDF)](paper/main.pdf)** · [LaTeX source](paper/main.tex) · [Markdown](paper/main.md)

This repository accompanies *Uniform integer representation counts and
reflected spans for quadratic Bose–Chowla sets*. Theorem 1 estimates the
number of ordered integer solutions to $b_1+b_2+b_3-b_4=s$, uniformly over
the specified complete quadratic bases and every integer target. Corollary
1.1 applies this estimate to sublinear deletions and to reflected unions
at every integer reflection height, including overlapping pieces.
An admissible union has at most one sum with multiple unordered
representations, including diagonals. The least inclusive span in this
construction family is $(3+o(1))p^2$, also after $o(p)$ base deletions.

Start with the PDF for the complete argument. To check its critical steps,
continue with the review guide; to run the finite tests, use the reproduction
guide. The early separated-reflection note is historical material.

| Your goal | Start here |
| --- | --- |
| Read or build the current paper | [paper/](paper/README.md) |
| Examine proof obligations and review limitations | [review/](review/README.md) |
| Reproduce finite checks | [REPRODUCING.md](REPRODUCING.md) |
| Inspect exact outputs, receipts and provenance | [evidence/](evidence/README.md) |
| Consult earlier drafts and the original C021 packet | [archive/](archive/README.md) |

The results concern the stated quadratic construction family and its
sublinear deletions. They do not resolve the general Erdős #864 upper-bound
problem. Independent expert/formal verification and literature priority
have not been established; see the [review record](review/README.md).

Python checks use only the standard library (Python 3.11+).
[SHA256SUMS.txt](SHA256SUMS.txt) records the distributed file bytes.
