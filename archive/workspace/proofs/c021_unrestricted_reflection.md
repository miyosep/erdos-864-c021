# Reflections at every integer height (E864-C056, E864-C058)

Session e864_20261105_03_extensions, cycle 3, 2026-11-05 Asia/Shanghai.
SELF_CHECKED only. Finite lemmas below are proved directly. The asymptotic
deduction uses a re-derived analytic theorem, whose complete proof and
external input are included as an appendix. No novelty claim.

## Theorem: optimal hull length with no separation assumption

For odd primes p put M=p²−1. For θ primitive in F_(p²) and t in Z/MZ let

    B={rep_[1,M](log_θ(θ+a)+t):a in F_p}.

An integer set is admissible if at most one sum has more than one
unordered representation a≤b, including a=b. For EVERY integer S define

    A_S=B∪(S−B),
    ℓ_B(S)=max(A_S)−min(A_S)+1,
    L*(B)=min {ℓ_B(S): S in Z and A_S admissible}.

Then the minimum exists and

    lim_(p→∞ through odd primes) sup_(θ,t) |L*(B)/p²−3|=0.     (8)

There is no restriction on S and no disjointness assumption. In fact,
for every ε>0, all sufficiently large p and every base choice satisfy

    A_S inadmissible for every S/M in [−1+ε,3−ε].             (9)

For all feasible S, |A_S| is between 2p−2 and 2p. Consequently the
largest attainable |A_S|/√ℓ_B(S) tends uniformly to 2/√3.
This is a theorem about this specific complete family, not arbitrary
Sidon bases or arbitrary admissible sets in Erdős #864.

## Small counterexamples to a tempting stronger finite assertion

One cannot use 'A_S admissible iff R_B(S)=0' for all S. The new exhaustive
test gives p=3, θ=1+X in X²=2, t=0, B={1,6,7}, S=2. The union
{−5,−4,1,6,7} is admissible but R_B(2)=7. Its only repeated sum is 2,
with pairs (−5,7),(−4,6),(1,1). These are exactly permitted central
collisions. Thus the separated criterion really fails after separation
is removed. It is replaced by a count of genuine off-centre collisions.

Nor are the finite minima equal: the same base has unrestricted
inclusive optimum 7, attained at S=8, whereas its separated optimum
is 15 at S=16. The asymptotic theorem does not assert equality at
small primes or an explicit threshold.

These attempts preceded the proofs below. The reflection-mode run
../runs/20261104T175850-be97a2607144487cafb7d168e3dadbdc/ passed
750850 states and all 224 primitive/cut bases for p=3,5. It checks
every S in [3min(B)−max(B)−1,3max(B)−min(B)+1]. Outside that range
the hull is already at least the explicit feasible upper bound, so
no smaller optimum is missed. It checks the separated criterion,
the hull formula, overlap≤2, and the necessary count bound below.

## Finite Sidon obstruction lemma (E864-C056)

Let C be any nonempty finite integer Sidon set of size n, including
diagonal pair sums in the definition. Write

    R_C(s)=#{(a,b,c,d) in C^4:a+b+c−d=s}.

If C∪(S−C) is admissible, for any integer S, then

    |C∩(S−C)|≤2,        R_C(S)≤6n.                          (10)

Proof. The overlap points solve x+y=S inside C. There is at most one
unordered pair, hence at most two distinct points in the overlap.
The reflected union is invariant under x↦S−x. A repeated sum u
reflects, bijectively on its unordered pairs, to a repeated sum 2S−u.
Therefore any repeated sum in an admissible reflected union must
equal S; an off-centre repeated sum makes it inadmissible.

For every quadruple counted by R_C(S) consider the unordered pairs

    P={a,b},        Q={d,S−c},       a+b=d+(S−c).

Both belong to the union. If P≠Q and a+b≠S, they are an off-centre
collision, forbidden by the previous paragraph. Every permitted
quadruple must therefore be in at least one of three classes:

1. a+b=S. Then c=d. There are at most two ordered (a,b) and n
   choices c=d, so at most 2n quadruples.
2. d=a and S−c=b. This implies b+c=S. There are at most two
   ordered (b,c) and n choices a=d, so at most 2n quadruples.
3. d=b and S−c=a. Again there are at most 2n quadruples.

The last two classes cover every equality P=Q, even diagonals.
Union bounding gives 6n. Overcounting intersections between these
classes is harmless. No separation assumption has been used. ∎

For completeness, the deletion-mode test also checks this lemma for
every survivor of every nonempty Sidon subset of [1,7] and all relevant
sums. It includes empty survivors, for which the bound is vacuous.

## Proof of the unrestricted optimum

The analytic theorem in the appendix proves the following uniform facts
for the displayed complete bases, without using previous status labels:

    m/M→0, v/M→1, d/M→1, where m=min B, v=max B, d=v−m;
    sup_(θ,t,s) |R_B(s)/p²−F(s/M)|→0,

where F(y)=P(y<U1+U2+U3<y+1) for independent uniform (0,1)
variables, continuous and strictly positive on (−1,3).
On any fixed compact interval J inside that open interval,
R_B(S)≥c_J p² for every S/M∈J eventually. For large p this is
greater than 6p; (10) proves (9).

For every integer S the exact hull formula is

    ℓ_B(S)=d+|S−(m+v)|+1.                                  (11)

Indeed max(A_S)=max(v,S−m), min(A_S)=min(m,S−v). If S≥m+v
these are S−m,m, and otherwise they are v,S−v. These two cases
give (11). In particular S−2m+1 is NOT the hull for arbitrary S.

There is a feasible integer S0=3v−m+1>2v. To check this without
assuming any prior criterion, the internal B+B sums are ≤2v<S0,
and the reflected internal sums are ≥2S0−2v>S0. Both have unique
unordered representations by Sidonicity. The mixed sums have the
form S0+x−y. Apart from S0 itself their representations are unique
by nonzero difference uniqueness. A collision of an internal low
sum a+b with a mixed sum S0+d−c would require
S0=a+b+c−d≤3v−m, which is impossible. A high/mixed collision
reflects to a low/mixed collision. Thus the only repeated sum is
S0 and the union is admissible. Its hull has length 3d+2, proving

    L*(B)≤3d+2=(3+o(1))M.                                 (12)

The minimum exists because feasible lengths are positive integers.
Suppose a fixed ε∈(0,1) admitted arbitrarily large bases and feasible
heights with ℓ_B(S)≤(3−ε)M. From (11) and the endpoint facts,

    |S/M−(m+v)/M|≤3−ε−d/M−1/M=2−ε+o(1).

Since (m+v)/M→1 uniformly, eventually

    S/M∈[−1+ε/2,3−ε/2].                                   (13)

This compact interval is forbidden by (9), a contradiction. Together
with (12) and M/p²→1 this proves (8). The overlap part of (10) gives
2p−2≤|A_S|≤2p; combine with the length lower bound and the explicit
upper construction to obtain the cardinality ratio. ∎

## Scope and review

The finite obstruction and hull geometry are direct combinatorial
proofs. Their application to the quadratic family is a deduction from
the included analytic theorem, whose non-elementary input is a proved
published result. Thus the family theorem is unconditional in the usual
mathematical sense, while its verification status here is SELF_CHECKED.
If that analytic input or its reduction were invalidated, the family
deduction would require re-review; the finite lemma would remain valid.

## Appendix: full local limit and foundation proofs

# Uniform integer local limit theorem (E864-C055)

Session e864_20261105_03_extensions, cycle 2, 2026-11-05 Asia/Shanghai.
Review: SELF_CHECKED, with fresh finite tests; no independent/formal review
or novelty claim. The analytic input is a proved character bound, explicitly
reduced below and in the included foundation appendix.

## Theorem

For each odd prime p put M=p²−1. For every primitive θ in K=F_(p²) and
t in Z/MZ let B consist of the representatives in {1,…,M} of
log_θ(θ+a)+t for a in F_p. For integers s let

    R_B(s) = #{(b1,b2,b3,b4) in B^4: b1+b2+b3−b4=s},

with ordered coordinates and all repetitions permitted. If U1,U2,U3 are
independent uniform variables on (0,1), define

    F(y) = P(y<U1+U2+U3<y+1).

Then

    lim_(p→∞ through odd primes) sup_(θ,t) sup_(s in Z)
        |R_B(s)/p² − F(s/M)| = 0.                             (LLT)

This is an absolute local limit, uniform even at moving endpoints and
outside the support. It gives no relative error when F(s/M)→0, no
shrinking-scale estimate, and no explicit rate or prime threshold.

The profile has the explicit formula

    G(z) = (z_+³ −3(z−1)_+³ +3(z−2)_+³ −(z−3)_+³)/6,
    F(y) = G(y+1)−G(y),      x_+=max(x,0).                   (4)

It is continuous, zero outside [−1,3], strictly positive inside (−1,3),
and F(y)=F(2−y). In particular F(1)=2/3 and F(0)=F(2)=1/6.
For every compact nonempty J⊂(−1,3), (LLT) implies
R_B(s)≥(min_J F/2)p² for all s/M∈J and all sufficiently large p,
uniformly in all base choices. This recovers the coverage part of C021
without taking its stored status as a premise.

## Counterexample attempts before the proof

The limits-mode test first enumerated all integer counts for p=3,5,7,11,
17,23,31, the first lexicographic primitive in F_p[X]/(X²−d), least
quadratic nonresidue d, and t=0,floor(M/3),M−1. It checked all s in
[−M,3M]. Outside this range both the count and limiting profile vanish.
Direct ordered quadruples independently checked the histogram for p≤5.
No asymptotic assertion follows from these finite samples.

The finite assertion of positivity at EVERY interior s is false: for
p=3, θ=1+X, X²=2, t=0, B={1,6,7}, R_B(−7)=0 while F(−7/8)=1/3072>0.
This is compatible with (LLT). Errors are substantial and not monotone
in the sample. At p=31 the maximum absolute errors for the three cuts
are approximately 0.1564, 0.1978, 0.1795; no rate was fitted.

The initial run 20261104T175706-e8b5e54f963443cfa49d191481cf1598 used
floating zero in part of the supposedly exact profile calculation. That
numerical-type issue was corrected to rational zero and rational division.
Use the replacement exact-arithmetic run
../runs/20261104T175733-c6d3cbeb565d409893af79af248dcf8a/:
PASS, 462653 states, 21 cuts, one worker, no truncation. The old evidence
is retained and is superseded only for its exact-arithmetic description.

## Proof: from the full modular fibre to a moving integer slab

For the modular fibre at s, the foundation theorem, proved in the appendix,
constructs a retained measure μ_s of mass 1+O(1/p) on the normalized
first three coordinates in (0,1]³, with uniform weak convergence to
Lebesgue measure. Importantly, the entire omitted modular fibre has at
most 6p points. The proof of that bound includes z=1 singular fibres;
one cannot infer it just by counting excluded (a,b) parameter pairs.

Put y=s/M. For any retained modular witness let xi=bi/M, i=1,2,3.
Its fourth representative b4 is the unique number in {1,…,M}
congruent to b1+b2+b3−s modulo M. Thus the INTEGER equality holds
if and only if

    0 < x1+x2+x3−y ≤ 1.                                    (5)

The weak upper endpoint is essential: the value 1 represents residue
zero, whereas 0 does not. Let H_y⊂(0,1]³ be the half-open slab in (5).
For every integer s, exactly

    0 ≤ R_B(s)/p² − μ_s(H_y) ≤ 6/p.                         (6)

It remains to justify convergence uniformly for all moving y; fixed-box
weak convergence alone must not be asserted to do this without a step.

Fix a positive integer K0. Partition (0,1] into K0 half-open intervals
((j−1)/K0,j/K0], and partition the cube into K0³ resulting boxes Q.
Each fixed box is a continuity set for torus Lebesgue measure; hence

    δ_(p,K0) = sup_(θ,t,s) max_Q |μ_s(Q)−vol(Q)| → 0

as p→∞ with K0 fixed. There are finitely many boxes, so the maximum
is legitimate. The union of boxes wholly inside H_y is a lower
approximation; the union of boxes meeting H_y is an upper approximation.
Any box in the difference has closure meeting one of the planes
x1+x2+x3=y or y+1. The sum of coordinates varies by at most 3/K0
within a box. Therefore the difference lies in the union of bands

    |x1+x2+x3−y|≤3/K0,   |x1+x2+x3−(y+1)|≤3/K0.

Each band has volume at most 6/K0: fix x1,x2 and integrate the possible
x3 interval, whose length is at most 6/K0. Their union has volume at
most 12/K0, uniformly for every real y. This argument also covers
boxes touching the planes only at an endpoint and the representative
seam at coordinate 1. Summing the discrepancy over at most K0³ boxes
gives, for all θ,t,s and all real y,

    |μ_s(H_y)−vol(H_y)| ≤ K0³ δ_(p,K0)+12/K0.                (7)

First let p→∞, holding K0 fixed, and then let K0→∞. Equations
(6)–(7) prove the uniform limit, since vol(H_y)=F(y); the two planes
have zero Lebesgue measure. There is no exchange of an unproved
shrinking-box estimate with the prime limit.

For (4), the volume of {x1+x2+x3≤z} in [0,1]³ is the simplex volume
z_+³/6, with the portions xi>1 subtracted by inclusion-exclusion.
This gives G. Subtraction gives F, and the reflection xi↦1−xi proves
F(y)=F(2−y). Positivity for −1<y<3 follows by choosing a small open
box inside the cube with its sum in (y,y+1). Continuity and compactness
give the stated uniform positive minimum. This completes the proof.

## Literature boundary

The proof uses the published nonprincipal character estimate of
[Keating–Rudnick, (3.33)](https://arxiv.org/pdf/1204.0708v3).
The elementary grid argument and the singular-fibre accounting are
derived here. The same model's new derivation is still self-review.
No known theorem is being claimed as novel. A search including
Ortega–Prendiville's Fourier and five-variable theorems, Nathanson's
Bose–Chowla reproduction and Pikhurko's macroscopic triple-sum
distribution has not established priority for (LLT); details and limits
are in c021_extensions_gap_audit.md and SOURCES.md.

## Appendix: full proof of the analytic foundation

# Reconstructed finite-field foundation (E864-C054)

Session e864_20261105_03_extensions, cycle 1, 2026-11-05 Asia/Shanghai.
This proof was checked from equations and a fresh implementation, without
using any stored PROVED label. It is a reproduction/self-review, not review
by an independent mathematician or a formal proof. Novelty is not assessed.

## Definitions and theorem

Let p be an odd prime, K=F_(p²), M=p²−1, θ a generator of K*, and t in Z/MZ.
Let β(a) be the unique integer in [1,M] congruent to log_θ(θ+a)+t, a in F_p,
and put B={β(a):a in F_p}. For any integer s define the ordered modular fibre

    T_s = {(a,b,c,e) in F_p^4: β(a)+β(b)+β(c)−β(e) ≡ s (mod M)}.

There is a subset G_s of T_s with

    |G_s| = (p−e_s)(p−1),   0≤e_s≤4,   |T_s\G_s|≤6p.             (1)

Give each point (β(a)/M,β(b)/M,β(c)/M), for (a,b,c,e) in G_s,
mass p^−2. The resulting measure μ_s on the three-dimensional torus
has total mass 1+O(1/p). For every integer mode (i,j,h) nonzero modulo M,
its unnormalized Fourier sum has absolute value at most

    4p√p                         if (j,h)≠(0,0) modulo M,
    (p−1)(√p+4)                 otherwise.                      (2)

Constants and conclusions are uniform in θ,t,s. In particular μ_s tends
uniformly to Lebesgue probability for every fixed continuous torus test
and every fixed box with null boundary (using representatives in (0,1]).
The base measures p^−1 sum_(b in B) δ_(b/M) also tend uniformly to
Lebesgue measure on [0,1]. Thus min(B)/M→0 and max(B)/M→1 uniformly.

## Sole non-elementary input

We use the proved function-field Dirichlet-character estimate

    |sum_(f monic, deg f=1) Ξ(f)| ≤ (deg Q−1)√p                (3)

for every nonprincipal Dirichlet character Ξ modulo Q in F_p[T], extended
by zero on nonunits, deg Q≥2. This is the n=1 case of Keating–Rudnick,
[arXiv:1204.0708v3, §3.4, (3.31)–(3.33), pp.9–10](https://arxiv.org/pdf/1204.0708v3).
The von Mangoldt weight of each monic linear polynomial is one. The bound
allows imprimitive characters; §3.5 introduces primitivity for a subsequent
matrix formulation. This published estimate rests on the proved
function-field Riemann hypothesis. It is used as an external theorem,
not re-proved here. There are no conjectural analytic inputs.

## Sidon property, including diagonals

Write L(a)=θ+a. These are distinct and nonzero. If two pair sums of the
β values agree modulo M then L(a)L(b)=L(c)L(d). Comparing the coefficients
of 1,θ after cancelling θ² gives a+b=c+d and ab=cd. The two unordered
pairs of roots, with multiplicity, coincide. Hence B has p elements and
is Sidon modulo M and over the integers, including diagonal pair sums.
For a nonzero integer or residue u, x−y=u has at most one ordered
solution in B: equality of two such differences is an equality of pair
sums, and the alternative swapping forces the zero difference.

## Reconstruct the parametrization and exceptions

Conjugation is x↦x^p; put Δ=θ−θ̄≠0 and γ=θ^(s−2t). The modular equation is

    L(a)L(b)L(c)=γL(e).                                      (4)

The translation contributes t+t+t−t=2t, explaining the exponent.
Fix a, let k=L(a)/γ and z=kL(b). When z≠z̄ the equation and its conjugate
are equivalent to zL(c)−z̄ L(c)̄=Δ with L(c)−L(c)̄=Δ. Eliminating gives

    L(c)=Δ(1−z̄)/(z−z̄).                                    (5)

For this value, direct conjugation shows L(c)−L(c)̄=Δ and
zL(c)−z̄ L(c)̄=Δ. Thus c=L(c)−θ and e=zL(c)−θ are in F_p and are unique.
Neither L(c) nor zL(c) is zero, because its conjugate difference is Δ.

Define w=γ̄/(θ̄+a)−θ̄. Discard a row if k is real, w is real,
or w is −θ or −θ̄. There are at most four discarded rows:

* If k were real at two distinct a, subtraction would imply 1/γ in F_p;
  then L(a)/γ could not be real at any a. Hence at most one such row.
* Multiplying the nonzero denominators in w=w̄ gives

      γ̄(θ+a)−γ(θ̄+a)+Δ(θ+a)(θ̄+a)=0.

  Its quadratic leading coefficient is Δ, so there are at most two a.
* w=−θ forces γ̄=−Δ(θ̄+a), at most one a.
  w=−θ̄ would force γ̄=0 and is impossible.

On a retained row k≠k̄. The unique zero of z−z̄, as a function of b, is

    r=−(kθ−k̄θ̄)/(k−k̄) in F_p.

The ratio is fixed by conjugation, proving the stated field membership.
For b≠r equation (5) factors as

    L(c)=λ(b−w)/(b−r),   λ=−Δk̄/(k−k̄)≠0.                  (6)

Every such b produces one quadruple. Define G_s to be precisely these
quadruples. The map is injective because it retains its a,b coordinates,
and each retained row has p−1 of them, proving the first part of (1).

## Bound ALL omitted witnesses, including large singular fibres

This step is needed for equality limits, beyond the original lower-bound
argument. If z=z̄, equation zL(c)=L(e) implies zΔ=Δ. Thus there are
no solutions for real z≠1. When z=1, all p choices c=e are solutions.
The equation z=1 is L(a)L(b)=γ. The Sidon argument above, before taking
logs or translates, shows it has at most two ordered solutions (a,b).
All singular fibres together therefore contribute at most 2p witnesses.

For every other (a,b) there is exactly one witness, by (5). Non-singular
witnesses in discarded rows number at most 4p. All other non-singular
witnesses belong to G_s. Consequently |T_s\G_s|≤4p+2p=6p. There is
no subtraction of an uncontrolled singular fibre and no assumption that
every omitted (a,b) has just one continuation.

## CRT character: signs, fields, nonprincipality

Let χ:K*→C* have χ(θ)=exp(2πi/M). Fix a Fourier mode (i,j,h), with
indices reduced modulo M. Up to unit constants independent of b, a
retained row of its Fourier sum is

    sum_(b≠r) χ^j(b+θ) χ^h(b−w) χ^(−h)(b−r).               (7)

Let m_α(T)=(T−α)(T−ᾱ) for nonreal α, and set

    Q(T)=m_θ(T)m_(−w)(T)(T+r).

The first two factors are distinct irreducible quadratics: equality
would mean −w=θ or θ̄, exactly the excluded cases. The last is linear,
so Q is squarefree of degree five. Evaluation at θ,−w,−r gives a ring
isomorphism

    F_p[T]/Q ≅ K × K × F_p.

Define Ξ on units by Ξ(f)=χ^j(f(θ))χ^h(f(−w))χ^(−h)(f(−r)),
with the last character restricted to F_p*, and set Ξ=0 on nonunits.
Then Ξ(T+b) is exactly the summand (7), and is zero when b=r,
even if the linear component is a principal character. If (j,h)≠(0,0)
modulo M at least one quadratic component is nonprincipal on K*.
CRT permits that component to vary independently of the others; Ξ is
therefore nonprincipal. Possible cancellation after restricting χ to
F_p* does not change this reasoning. Equation (3) now bounds (7)
by 4√p. Summing at most p rows proves the first bound in (2).

When j=h=0 and i≠0, each retained row has p−1 columns. The degree-two
modulus m_θ and character f↦χ^i(f(θ)) give
|sum_a χ^i(L(a))|≤√p by (3). Discarding at most four rows changes the
sum by at most four. Multiplication by p−1 gives the second bound.
Translating all log coordinates contributes only a constant phase.

## Uniform distribution and endpoints

After division by p², (2) tends uniformly to zero for each fixed nonzero
integer frequency. For large p that fixed frequency is nonzero modulo M.
The zero frequency tends to one by (1). Approximate any fixed continuous
torus function uniformly by a fixed trigonometric polynomial. Its
finitely many coefficients obey these uniform limits, while the uniform
approximation error is bounded by its sup norm times the bounded total
mass. This proves uniform weak convergence. Upper and lower continuous
approximations give convergence for fixed boxes, including boxes meeting
the representative seam: their torus boundaries have Lebesgue measure
zero. In particular the seam itself has uniformly vanishing mass.

The same degree-two estimate gives all nonzero fixed Fourier coefficients
of the one-dimensional base measure O(p^−1/2). Repeat the approximation
argument for any fixed interval. For any ε>0, both (0,ε) and (1−ε,1)
contain (ε+o(1))p points uniformly, proving the endpoint assertions.

## Tests before the proof and review limit

Fresh code: ../experiments/check_c021_extensions.py, audit mode. The actual
run is ../runs/20261104T175510-6afeb6b3f17842be9d99641ed0124910/.
It passed 1,345,551 states and 272 primitive/target instances, untruncated:
all primitive θ and all γ for p=3,5; first lexicographic primitive and all
γ for p=7, in K=F_p[X]/(X²−d) with least quadratic nonresidue d.
All field identities, real singular fibres, four-row bound, and 6p bound
were checked against direct first-three-coordinate enumeration. Finite
row sums use floating complex arithmetic, tolerance 10^−9, and are only
diagnostics: they do not prove the character estimate. All modular modes
(j,h) were tested for p≤5 and three specified modes for p=7.

The original C021 compact-interior integer coverage and separated optimum
will be recovered from this foundation in the next proofs, with exact
half-open carry selection. No unresolved algebraic gap was found here.


