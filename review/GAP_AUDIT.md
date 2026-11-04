# Mathematical and literature gap audit

This same-model audit describes mathematical checkpoints and primary-source
comparison limitations. It does not constitute independent expert review
or formal verification.
See the [current paper](../paper/main.pdf) and
[computational supplement](COMPUTATIONAL_SUPPLEMENT.md).

## Mathematical checkpoints

### Singular solutions: a total bound, not a per-row bound

Write L(a)=θ+a, Δ=θ−θ̄, γ=θ^(s−2t), z=L(a)L(b)/γ. If z is real,
zL(c)=L(e) and conjugation give zΔ=Δ, so z=1. There are exactly p
solutions c=e for such a pair (a,b). But L(a)L(b)=γ has at most TWO
ordered solutions in the ENTIRE parameter plane: equality of two such
products forces equality of unordered pairs by coefficient comparison
in the basis 1,θ. Therefore total singular witnesses≤2p, uniformly
in γ, primitive θ and translation t. Counting p continuations at p²
arbitrary parameter pairs would be an incorrect bound; those pairs
are not arbitrary. Diagonal products yield at most one ordered pair.

The retained parametrization discards at most four rows. Every nonreal-z
parameter pair has exactly one continuation, so omitted non-singular
witnesses≤4p. Every omitted witness is in this class or the singular
class above: total omitted≤6p. This is a uniform full-fibre bound.

The formulas, the four exceptional-row conditions, the two irreducible
quadratics and linear factor in Q, and CRT nonprincipality all check
algebraically. The principal restriction on F_p* is harmless because
at least one of the two independently variable K* components remains
nonprincipal. The published character estimate permits imprimitive Ξ.

### Uniformity for every integer target

For each residue target the retained measure has total mass 1+O(1/p)
and uniformly vanishing coefficients at each fixed nonzero Fourier mode.
Fix a grid size K BEFORE taking the prime limit. There are K³ boxes,
and their maximum discrepancy δ_(p,K) tends uniformly to zero over
ALL θ,t,s. No continuous test or approximating polynomial depends
on these varying parameters at this stage.

For y=s/M, the exact integer selector is 0<x1+x2+x3−y≤1.
Its boundary boxes lie in two bands of width 6/K around the two
sum planes. Their total volume≤12/K for EVERY real y. Consequently

    sup_(θ,t,s in Z) |R_B(s)/p²−F(s/M)|
        ≤6/p+K³δ_(p,K)+12/K.

Let p→∞ at fixed K, then K→∞. This proves the required supremum,
including y approaching −1 or 3 and arbitrary integer carries.
It does not prove a relative error when F(y)→0 or give a rate.

The torus seam is not silently identified with the wrong integer lift.
Fixed half-open boxes are torus continuity sets with null boundary.
Alternatively any fixed coordinate value belongs to at most 2p modular
witnesses: fix a second coordinate and use modular Sidon uniqueness
for the remaining pair. Thus each coordinate seam has mass≤2/p.
The boundary x1+x2+x3−y=1 also fixes b4=M, so has mass≤2/p;
the lower boundary fixes the same residue but is excluded by the selector.
The fixed-grid proof already handles both boundaries without these
additional estimates.

### All-height and deletion deductions

For an integer Sidon C, any off-centre repeated sum in C∪(S−C)
reflects to a second repeated sum. Every R_C(S) witness must therefore
have a central pair sum or represent the same unordered pair twice
if the union is admissible. Each of the three degeneracy classes
has at most 2|C| witnesses; hence R_C(S)≤6|C|. Diagonals are included.
The overlap bound is ≤2 and the true hull is
v_C−m_C+|S−(m_C+v_C)|+1 at every integer height. These facts justify
the complete all-height reduction; the old separated-only criterion
R_C(S)=0 must not be used in the overlapping case.

The deletion incidence bound follows even more directly by fixing any
one slot and then a second slot; the remaining two elements have at
most two ordered pair-sum representations. Thus each slot has load
≤2|B| and four slots give 8|B||D|. This avoids any ambiguity over
zero differences. Arbitrary o(p) deletions preserve endpoint intervals
containing (η+o(1))p parent elements. The survivor endpoint, not the
parent endpoint, is used in the hull argument. All deductions check.

## Literature comparison

The accurate conclusion is not that three unrelated new theorems have
been discovered. The construction and character bound are established
literature; the deletion estimate is elementary; the two reflection
conclusions follow from compact-interior coverage plus elementary geometry.
The substantive analytic step to verify is the joint constrained-fibre
distribution and its integer selector. No checked primary theorem below
was identified as directly stating this exact uniform integer local limit.
This is a bounded comparison, not proof that no earlier derivation exists.

| Primary source and checked location | What is available | Deduction assessment |
| --- | --- | --- |
| Keating–Rudnick, arXiv:1204.0708v3, §3.4 (3.31)–(3.33), pp.9–10 | Nonprincipal polynomial Dirichlet-character bound. | The local limit follows after explicitly proving our degree-five CRT reduction and exceptional-fibre accounting, then elementary approximation. It uses no new character-sum theorem. |
| Nathanson, arXiv:2104.12711v3, §2 Theorem 1 and proof, pp.3–4 | Classical Bose–Chowla construction and modular Sidon uniqueness. | These premises are reproductions. The result does not itself specify joint integer-lift counts. |
| Ortega–Prendiville, JTNB 35 (2023), Theorems 1.2, 6.3 and 1.15; §5 (5.4), pp.126–127 | Ordinary Fourier discrepancy; counting/partition regularity for at least five variables. | The displayed theorem is not directly applicable to a prescribed four-variable integer target. The quantitative four-factor check below fails to give the necessary o(M) error. Other deductions are not ruled out. |
| Pikhurko, Discrete Math. 306 (2006), §2 proof of Theorem 4 (7), p.2100; §6 Lemma 10; §7 reflected/randomized intersections | Interval/residue distribution, macroscopic triple-sum densities, averaged reflected intersections. | Such averaging does not furnish positivity/equality at every prescribed integer S. No proof of that stronger implication was established. |
| Carter–O'Bryant–Tao, arXiv:2610.36207v1, Theorems 2.3–2.5, pp.6–7 | Diameter, ordered positions, gaps. | Supplies endpoint information, not the constrained joint fibre. Statements/surrounding passages checked, not all proofs or code. |
| Forey–Fresán–Kowalski, arXiv:2301.12878v3, introduction/Remark 2, §3 pp.4–6, §5 pp.9–10 | Symmetric Sidon terminology, algebraic realization of Bose sets, exponential-sum equidistribution discussion. | Confirms the symmetry framework and classical algebraic setting are prior. Its discussed exponential sums vary over character parameters; no exact positive-integer-lift theorem was extracted. Referenced broader monograph was not audited. |
| Yuchen Ding, arXiv:2606.15041v2, Theorems 1 and 4, §2.1 | Weighted distribution on arithmetic progressions. | One-coordinate distribution, not a prescribed four-coordinate local count. The current v2 title is Dense finite Sidon sets on arithmetic progressions, differing from the v1 title in search summaries. |

Only these selected passages were checked; no full-paper correctness review
of all seven sources is claimed. The external bound actually used is
[Keating–Rudnick](https://arxiv.org/pdf/1204.0708v3); the directly relevant
Fourier comparison is
[Ortega–Prendiville](https://www.numdam.org/item/10.5802/jtnb.1239.pdf).

### Quantitative four-factor Fourier check

This calculation is derived here, rather than attributed as a theorem to
another paper. Set f=1_B and g=(p/M)1_[1,M], use Fourier transforms on
R/Z and let Δ=||f̂−ĝ||_∞. Parseval and the Sidon property give

    ||f̂||_2²=p,       ||f̂||_4⁴=2p²−p,
    ||ĝ||_2=O(1),     ||ĝ||_4⁴=O(M).

By telescoping f̂³ overline(f̂)−ĝ³ overline(ĝ), and using Cauchy–Schwarz
on each remaining three-factor product,

    sup_s |R_f(s)−R_g(s)| = O(Δ M^(3/4)).

For example ∫|f̂|³≤||f̂||_2||f̂||_4²=O(M^(3/4)); the mixed terms
have the same or smaller bound. At p~√M the improved published
discrepancy bound is Δ=O(M^(3/8)), which only gives O(M^(9/8)).
The local-limit main scale is p²~M, so this certificate does not prove
an o(M) error. More basically

    Δ≥||f̂−ĝ||_2=√(p−p²/M)~M^(1/4).

Thus even replacing the discrepancy estimate by its best possible order
cannot make this particular absolute-value three-factor bound o(M).
This rejects this certificate, not Fourier methods generally. The present
CRT proof controls Fourier modes of the actual constrained witnesses,
which is additional information.

### Direct consequences and limits of the priority finding

Given any family of p-element Sidon sets in [1,M], M~p², with uniform
endpoint occupancy and R_B(s)≥c_J p² on every compact J⊂(−1,3), the
same elementary proofs give all-height optimum 3p² and o(p)-deletion
stability. Full local-limit equality is not even required for those
consequences. The manuscript makes this dependence explicit; it should
not advertise the three conclusions as independent analytic advances.

Ruzsa's Sumsets of Sidon sets (1996) full PDF was located at
https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7744.pdf but access returned
403; only the searchable opening statement was available. The
Erdős–Freud (1991) publisher page likewise returned 403. No additional
unread theorem from either is claimed checked. Author-hosted FFK PDF
timed out, then its primary arXiv v3 was read. No inference of novelty
is drawn from these failures. Broader priority, including the cited
arithmetic-Fourier-transform monograph and original older literature,
remains unestablished.

