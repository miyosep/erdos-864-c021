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
