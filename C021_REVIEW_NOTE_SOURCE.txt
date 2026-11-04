# Uniform integer-lift coverage for complete quadratic Bose–Chowla bases

Review draft. Prepared by Codex from
the existing project proof E864-C021. Review level: SELF_CHECKED only.
Neither independent correctness verification nor literature novelty has
been established. This is a scoped construction theorem submitted for
review, not a solution of Erdős #864. No experiment is used as a proof
premise. The accompanying original proof and audit are preserved.

## Statement and quantifiers

Let $p$ tend to infinity through odd primes, $K=\mathbb F_{p^2}$,
$M=p^2-1$. For a primitive $\theta\in K$ and a residue $t$ modulo $M$ let

```math
B_{p,\theta,t}
 =\{\mathrm{rep}_{[1,M]}(\log_\theta(\theta+a)+t):a\in\mathbb F_p\}.
```

Here rep selects the unique representative in {1,...,M}; in particular
residue zero is represented by M. A cut tau in the convention
rep(u) = ((u-tau) mod M)+1 corresponds to t=1-tau modulo M.
Thus all residue translations are exactly all the cuts in this convention.

For an integer set A, count unordered pairs a<=b, including the diagonal.
Call A admissible if at most one integer sum has more than one such
representation. Put m=min B, v=max B and

```math
L_{p,\theta,t}
 =\min\{S-2m+1:S\in\mathbb Z,\ S>2v,
                  \ B\cup(S-B)\text{ is admissible}\}.
```

The minimization allows an overall integer translation and uses the
inclusive interval length, not just the difference of endpoints.
The set of feasible S is nonempty, as proved below.

**Theorem (C021).** For every fixed compact nonempty J contained in
(-1,3), there exist c_J>0 and p_J such that for every odd prime
p>=p_J, every theta,t above and every integer s with s/M in J,

```math
\#\{(b_1,b_2,b_3,b_4)\in B^4:b_1+b_2+b_3-b_4=s\}
 \ge c_J p^2.
```

In particular,

```math
\lim_{\substack{p\to\infty\\p\text{ odd prime}}}
 \ \sup_{\theta,t}\left|\frac{L_{p,\theta,t}}{p^2}-3\right|=0.
```

Equivalently, for each epsilon>0 there is P_epsilon independent of
theta,t such that the displayed absolute value is below epsilon for
all odd primes p>=P_epsilon and all choices. This is stronger than a
statement only about the minimum over choices.

The hypotheses require a COMPLETE p-element base, positive lifts in
ONE period, and separated reflections S>2v. There is no assertion
here about deletion variants, overlapping reflected parts, arbitrary
Sidon bases, prime powers, an explicit prime threshold, or an error rate.

## External input

Keating and Rudnick, *The variance of the number of prime polynomials
in short intervals and in residue classes*, arXiv:1204.0708v3,
section 3.4, equations (3.31)--(3.33), printed pp.9--10:
for a nonprincipal Dirichlet character Xi modulo Q in F_p[T],

```math
\left|\sum_{f\text{ monic},\deg f=n}\Lambda(f)\Xi(f)\right|
 \le (\deg Q-1)p^{n/2}.
```

At n=1 every monic f is T+b and Lambda(f)=1. Primitivity of Xi
is not a hypothesis of (3.33). The local CRT character producing the
required sum is constructed explicitly in the proof below. The
external result is not being identified with a discrete-log theorem
without a reduction.

Source: https://arxiv.org/pdf/1204.0708v3 . The sole non-elementary
input is this proved function-field character bound. The argument
also uses the usual trigonometric approximation of continuous torus
functions and continuous approximation of boxes with null boundary.

## Elementary preliminaries

**1. Sidon property.** The p values theta+a are distinct and nonzero,
so B has exactly p elements. Equality of two pair sums modulo M
reduces, after cancelling the 2t translation, to

```math
(\theta+a)(\theta+b)=(\theta+c)(\theta+d).
```

Cancel theta^2 and compare coefficients in the basis 1,theta of
K over F_p. This gives a+b=c+d and ab=cd. Hence the roots of the
same quadratic give the same unordered pair {a,b}={c,d}, including
repeated roots. Thus B is Sidon modulo M and for integer sums.
Its nonzero integer differences have unique ordered representations:
x-y=z-w gives x+w=z+y, and Sidon uniqueness forces the same pair
when x-y is nonzero.

**2. Uniform base endpoints.** We include the elementary dense-Sidon
distribution argument to avoid relying on workspace-only claim IDs.
For ANY integer Sidon B subset [1,L], write b=|B| and j=|B intersect
[1,x]|, where 1<=x<L. Take an integer h>=1, a=x+h-1,
d=L-x+h-1 and T=a+d. For the two pieces B_1,B_2 define

```math
g_i(y)=\#\{u\in B_i:0\le y-u<h\}.
```

Their supports have lengths at most a,d. Cauchy gives
sum_y g_1(y)^2>=h^2 j^2/a and the corresponding lower bound
h^2(b-j)^2/d for g_2. For g=g_1+g_2, nonnegativity and uniqueness
of positive differences give

```math
\sum_y g(y)^2=hb+2\sum_{\substack{r>0\\r\in B-B}}(h-r)_+\le hb+h(h-1).
```

Consequently

```math
\begin{aligned}
\frac{j^2}{a}+\frac{(b-j)^2}{d}&\le 1+\frac{b-1}{h},\\
\left|\frac jb-\frac aT\right|^2&\le\frac{ad}{Tb^2}\left(1+\frac{b-1}{h}-\frac{b^2}{T}\right).
\end{aligned}
```

The second formula follows by completing the square; its last bracket
is nonnegative by the first inequality. For the present bases take
b=p, L=M, h=ceil(M^(3/4)). The bracket tends to zero, the prefactor
is at most T/(4p^2)=O(1), and a/T-x/M tends uniformly to zero.
Thus j/p-x/M tends uniformly to zero in x and all base choices.
Every fixed positive relative interval at either endpoint therefore
contains base points for large p, uniformly. Hence

```math
\frac mM\longrightarrow0,\qquad\frac vM\longrightarrow1,\qquad\frac{v-m}{M}\longrightarrow1.
```

uniformly in theta,t.

**3. Exact reflection criterion.** If S>2v the two parts B and S-B
are disjoint. The unordered sum families are B+B, 2S-(B+B), and
S+(B-B). The first is below S, the second above S. Their internal
uniqueness follows from the Sidon property; the mixed family is
unique away from S by difference uniqueness. At S there are exactly
p mixed unordered pairs. A low/mixed collision is exactly

```math
b_1+b_2=S+b_4-b_3\quad\Longleftrightarrow\quad b_1+b_2+b_3-b_4=S.
```

Such a collision also reflects to a different sum above S, violating
admissibility. Conversely the absence of these collisions leaves only
the permitted repeated sum S. Thus admissibility is equivalent to
S not in 3B-B. After translating the minimum m to 1, the maximum
is S-2m+1, giving the exact length in the statement.

## Main proof: joint character control and the integer lift

The next three sections reproduce the explicit derivation from the
accompanying audit. Their labels (A)--(C) are local equations, not
unproved lemmas or outside dependencies.

## 1. Target, parametrization, and discarded rows

Write q=p here only in the external theorem; in the local proof use p.
Let bar denote p-th power, D=theta-bar(theta), L(a)=theta+a and
gamma=theta^(s-2t). All L(a), gamma and D are nonzero. The exponent
s-2t is correct: translating FOUR logs with signs +,+,+,- adds 2t.
The modular equation is L(a)L(b)L(c)=gamma L(e).

Fix a, set k=L(a)/gamma and z=k L(b). If z!=bar(z), solving
z(theta+c)=theta+e together with its conjugate gives

```math
L(c)=\frac{D(1-\overline z)}{z-\overline z}.\tag{A}
```

Indeed conjugating the right side and subtracting gives exactly D;
thus L(c)-theta is in F_p. Likewise
z L(c)-bar(z) bar(L(c))=D, so z L(c)-theta is in F_p.
The resulting e is valid and unique. L(c) cannot be zero because its
anti-invariant part is D. The factors z and z L(c) are also nonzero.

An explicit absolute bound for the excluded a is FOUR:

* k in F_p occurs at most once. If two a worked, their nonzero
  difference divided by gamma would be in F_p, forcing gamma in F_p;
  then L(a)/gamma cannot be in F_p at all.
* Put w=bar(gamma)/(bar(theta)+a)-bar(theta). The equation w=bar(w),
  after multiplying the nonzero denominators, is

  ```math
  \overline\gamma(\theta+a)-\gamma(\overline\theta+a)+D(\theta+a)(\overline\theta+a)=0.
  ```

  Its leading coefficient is D, so it has at most two roots a in F_p.
* w=-theta means bar(gamma)=-D(bar(theta)+a), with at most one solution.
  w=-bar(theta) is impossible since gamma!=0.

On each retained row k is nonreal. The affine function

```math
z-\overline z=(k-\overline k)b+k\theta-\overline k\,\overline\theta
```

has a unique root r in F_p: the ratio of its two anti-invariant
coefficients is fixed by conjugation. For all b!=r, (A) becomes

```math
L(c)=\lambda\frac{b-w}{b-r},\qquad\lambda=-\frac{D\overline k}{k-\overline k}\ne0.\tag{B}
```

There are p-1 retained columns per retained row. The resulting
quadruples are distinct because their first two coordinates a,b are
distinct. Hence this is a genuine subset of at least (p-4)(p-1)
ordered modular witnesses. All singular columns and rows are discarded;
their possible large fibres are never estimated by an unjustified
square-root bound or subtracted from the claimed lower count.

## 2. The character modulus and the external theorem

Let chi(theta)=exp(2 pi i/M) have exact order M. For a Fourier mode
(i,j,h), the varying part of a retained b-row, apart from constants
of modulus one, is

```math
\chi^j(b+\theta)\,\chi^h(b-w)\,\chi^{-h}(b-r).\tag{C}
```

Use polynomial variable T and

```math
Q(T)=m_\theta(T)\,m_{-w}(T)\,(T+r).
```

Both minimal polynomials are irreducible quadratics. They are distinct
because w is nonreal and w is neither -theta nor -bar(theta). The
linear factor is different from both. Thus Q is squarefree of degree 5.
The evaluation points are theta, -w, -r; in particular evaluating
T+b produces b+theta, b-w, b-r with the displayed signs.

On the three residue fields put the local characters chi^j, chi^h,
and chi^(-h) restricted to F_p^*. The Chinese remainder theorem
constructs their product Dirichlet character Xi modulo Q, extended by
zero at nonunits. If (j,h)!=(0,0) modulo M, at least one QUADRATIC
component is nonprincipal on its full field K^*. CRT allows that
component to vary independently, so Xi is nonprincipal. A trivial
linear component still omits b=r correctly. No primitivity assertion
for Xi is required.

Keating--Rudnick, arXiv:1204.0708v3, printed pp.9--10, section 3.4,
(3.31)--(3.33), gives

```math
\left|\sum_{\substack{f\text{ monic}\\\deg f=n}}\Lambda(f)\Xi(f)\right|\le(\deg Q-1)p^{n/2},\qquad\Xi\text{ nonprincipal}.
```

At n=1 every monic linear has von Mangoldt weight one. Therefore
the modulus of (C) summed over b!=r is at most 4sqrt(p).
The primitive-character assumption introduced in section 3.5 belongs
to the cleaner Frobenius formulation there, not to (3.33). The
function-field Riemann hypothesis used here is a proved external
theorem, not a conditional appeal to number-field GRH.

For modes with j=h=0 and i nonzero modulo M, each retained a has
exactly p-1 columns. The same bound with modulus m_theta of degree 2
gives |sum_a chi^i(L(a))|<=sqrt(p). Removing at most four a adds at
most four, giving a total at most (p-1)(sqrt(p)+4).
For all other nonzero modes the total is at most 4p sqrt(p).
The zero mode is (p-O(1))(p-1)=p^2+O(p).
All constants are independent of theta,t,s and the frequencies
modulo M. A coordinate translation multiplies the Fourier coefficient
by a constant of modulus one and does not alter these bounds.

## 3. Why this proves the desired INTEGER count uniformly

Put mass p^(-2) at the three translated, positively represented log
coordinates divided by M for each retained witness. For each fixed
nonzero integer Fourier vector, its residues are nonzero for all
sufficiently large p and the coefficient tends to zero uniformly in
all parameters; the total mass tends to one uniformly. Approximation
by a fixed trigonometric polynomial proves uniform convergence for
every fixed continuous torus test. Continuous upper/lower
approximations then prove uniform convergence on any fixed open box
whose closure is inside (0,1)^3. No approximation with growing
frequency or shrinking boxes is used.

For every y in J choose a box V_y with positive volume and closure
inside the cube such that, throughout the box,

```math
0<x_1+x_2+x_3-y<1,
```

with strict positive margins. Such a box exists because
(0,3) intersects (y,y+1) for every -1<y<3. The same inequalities
hold when y is replaced by any y' in a small neighborhood U_y.
Choose finitely many U_y covering the compact J. For all sufficiently
large p every corresponding fixed box contains at least half its
volume times p^2 retained witnesses, uniformly in theta,t,s.
The minimum of these finitely many positive half-volumes supplies c_J.

For a witness in the chosen box with y'=s/M, its fourth positive
representative divided by M is congruent to x1+x2+x3-y' modulo 1.
The latter is strictly between 0 and 1, so it is precisely that
representative, not another carry. Thus b1+b2+b3-b4=s as an INTEGER.
The convention that residue zero is represented by M cannot affect
this argument. This proves the stated uniform compact-interior lower
bound without confusing marginal uniformity with joint uniformity.

## Completion: uniform minimum length

All 3B-B values are at most 3v-m, so S=3v-m+1 is feasible and
S>2v. This gives

```math
L_{p,\theta,t}\le3(v-m)+2=(3+o(1))M.
```

uniformly, by elementary preliminary 2. Suppose a fixed epsilon
in (0,1) and arbitrarily large p allowed choices with
L_(p,theta,t)<=(3-epsilon)M. For the minimizing S, the exact formula
S=L_(p,theta,t)+2m-1 and S>2v put S/M eventually in the fixed
compact interval [3/2,3-epsilon/2] inside (-1,3). The integer coverage
just proved gives S in 3B-B, contradicting preliminary 3. Hence the
uniform lower bound also holds. Since M/p^2 tends to one, the
supremum statement follows. This completes the proof submitted for review.

At the optimizing height the size is exactly 2p, so the normalized
size tends uniformly to 2/sqrt(3). Larger feasible heights cannot
improve that asymptotic ratio. An optional admissible center changes
the size by at most one. No general Erdős #864 upper bound follows.

## Literature and validation boundary

Ortega--Prendiville (2023), Theorems 1.2 and 6.3, provide Fourier
uniformity for Sidon sets; their Theorem 1.15 is a five-or-more-variable
partition-regularity theorem. The audit explains why one particular
supremum-norm four-factor counting estimate fails, not why every use
of their results would fail. Source:
https://www.numdam.org/item/10.5802/jtnb.1239.pdf .

Carter--O'Bryant--Tao, *On the diameter and distribution of Sidon sets*,
arXiv:2610.36207v1 (26 October 2026), Theorems 2.3--2.5, was checked
at the level of its statements and the opening distribution argument.
Their diameter, ordered-position and largest-gap conclusions are
relevant to the base endpoints, not a stated joint distribution of
the modular 3B-B witness coordinates or a prescribed integer-lift
coverage result. No deduction of the latter from those statements
has been established here. This does not certify novelty or rule out
a different short deduction. Source:
https://arxiv.org/abs/2610.36207v1 . The HTML rendering drops some
theorem macros/numbers; the PDF's numbering was used.

The proof uses no numerical data. The attached original code and
historical outputs cover only p=2,3,5,7,11,17,23,31 for the canonical
examples, with an originally separate triple-sum verification.
They check those finite examples, not an asymptotic threshold or
the character bound. For p=31 the first absent integer lift S=2388
has modular residue 468 modulo 960; the other lifts have counts
25,390,547 (total 962). This is compatible with eventual coverage
and illustrates why the integer selector is indispensable.

Review request: check the row exceptions, CRT nonprincipality,
n=1 application of (3.33), parameter-uniform approximation, and
integer selector directly, without treating the stored PROVED label
or a previous self-review as correctness evidence. Literature
priority and independent mathematical verification remain open.
