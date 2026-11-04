# Integer carries of a complete Bose–Chowla base (C021)

Let p tend to infinity through odd primes, K=F_(p²), M=p²-1. Let theta
be any primitive element of K. Take all p logs to base theta of theta+a
(a in F_p), translate by any common residue t, and take representatives
in [1,M], obtaining B. For any fixed compact J inside (-1,3), every integer
s with s/M in J belongs to 3B-B once p is sufficiently large, uniformly
in theta and t. In fact each such s has at least c(J)p² ordered witnesses.

## Parametrize a subset of the modular witnesses

Write L(a)=theta+a, bar for p-th power, and gamma=theta^(s-2t).
The modular witness condition is L(a)L(b)L(c)=gamma L(e). For fixed a let
k=L(a)/gamma and z=k L(b). Whenever z differs from its conjugate the
equation L(e)=z L(c) has a unique solution c,e in F_p. Subtract its
conjugate and solve to get

    L(c)=(theta-bar(theta))(1-bar(z))/(z-bar(z)).

Indeed c=L(c)-theta is fixed by conjugation, and z L(c)-theta is likewise
fixed. Neither field factor vanishes. We may discard the entire singular
part; we seek a lower bound for the number of witnesses.

Except for O(1) choices of a, k is nonreal (outside F_p), and

    w=1/bar(k)-bar(theta)=bar(gamma)/(bar(theta)+a)-bar(theta)

is nonreal and differs from -theta and -bar(theta). Here and below all
O(1) constants are absolute. For k real, the affine line theta+F_p meets
gamma F_p in at most one point: parallel lines in this case are disjoint.
For w real, clear the two nonzero denominators in w=bar(w); the quadratic
coefficient is theta-bar(theta), nonzero. Equality to -bar(theta) is
impossible and equality to -theta gives at most one a. Thus discarding
these rows costs only O(1) rows, for every gamma.

For each retained a, z-bar(z) has exactly one root r in F_p as an affine
function of b (its leading and constant coefficients are anti-invariant).
On b unequal to r the displayed formula becomes

    L(c)=lambda (b-w)/(b-r)

with nonzero row-dependent lambda. Take just the resulting (p-O(1))(p-1)
ordered, distinct parametrized witnesses. We never need cancellation on
discarded rows, even when z=1 admits p solutions.

## Three log coordinates on this parameter set are equidistributed

Let chi be the full-order multiplicative character defined by
chi(theta)=exp(2 pi i/M). A Fourier mode (i,j,h) on the three coordinates
(log L(a), log L(b), log L(c))/M has summand
chi^i(L(a)) chi^j(L(b)) chi^h(L(c)). Translating the coordinates only
multiplies a mode by a constant of modulus one.

For (j,h) nonzero modulo M the row sum over b is O(sqrt(p)).
To see this, up to constants of modulus one, its summand is

    chi^j(b+theta) chi^h(b-w) chi^(-h)(b-r).

Apply the degree-one Dirichlet character bound to monic polynomials T+b
over F_p. Use squarefree modulus Q with roots theta, -w and -r together
with their conjugates. These are two distinct quadratic factors and one
linear factor by the exclusions above. On its three residue fields take
respectively evaluation at theta with chi^j, at -w with chi^h, and at
-r with chi^(-h) restricted to `F_p^*`. The Chinese remainder theorem
makes this a character modulo Q, extended by zero at nonunits. It is
nonprincipal because evaluation on either quadratic factor is onto K and
at least one of j,h is nonzero modulo M. Even a trivial linear component
correctly omits b=r. The degree is 5, so the row sum has modulus at most
4 sqrt(p). The external input is Keating–Rudnick, §3.4, (3.33) with n=1
(S11); all monic linears have von Mangoldt weight 1.

If only i is nonzero, each retained a occurs p-1 times. The full sum of
chi^i(theta+a) over a is bounded by sqrt(p) by the same theorem with the
minimal polynomial of theta, of degree two. Deleting O(1) rows inside this
one-dimensional sum adds O(1). Thus every nonconstant mode is O(p^(3/2))
even uniformly over the frequencies modulo M. The zero mode is p²+O(p).

Normalized by p², the empirical measures of the three translated log
coordinates converge to Haar probability on the three-torus, for *every*
sequence of parameters. This follows first for trigonometric polynomials,
then for continuous functions by uniform approximation, and then for a
fixed open rectangular box by approximating its indicator at its null
boundary. Representatives in [1,M] put the residue zero at 1 after
scaling, which has no effect on boxes strictly inside the cube.

## Recover the particular integer lift

For any sequence s/M tending to y in (-1,3), choose an open box Q0 with
closure in (0,1)^3 on which 0 < x1+x2+x3-y < 1 holds with a fixed margin.
Such a box exists since (0,3) intersects (y,y+1); take three equal interior
coordinates with sum in the intersection and a small neighborhood.
The fourth representative divided by M is congruent modulo 1 to
x1+x2+x3-s/M. For all large p the latter lies strictly between 0 and 1
on the box. Thus the three representatives and the fourth give exactly s
as an integer. The box receives (vol(Q0)+o(1))p² parametrized witnesses.
If the asserted uniform positive lower bound on any compact J failed,
a sequence with counts/p² tending to zero would have a subsequence with
s/M tending to some y in J, contradicting this box argument.

## Consequence for C016

C012 gives N_min=3D+1-d and, for d>=0, a missing s=3v-m-d with
2v<s<=3v-m, where v=max B, m=min B and D=v-m. C014's uniform span
estimate gives D/M -> 1, hence v/M -> 1 and m/M -> 0 since B is in [1,M].
If d/M>=epsilon infinitely often (we may take epsilon<1), this missing s
would have s/M in [3/2,3-epsilon/2] eventually. This contradicts the
compact-interior result. Since d>=-1, d=o(p²) and N_min/p² -> 3.
The canonical positive-limsup alternative C016 therefore fails. This includes
all primitive choices and all cyclic cuts, and gives the limiting normalized
size 2/sqrt(3) for the optimal reflection of these full bases. Optional
addition of the center changes size by at most one.

Scope: no bound here on the size of an arbitrary admissible set or on the
holes at submacroscopic distance from the endpoints. No formal or independent
review. The novelty of this application of the character estimate is unknown.
