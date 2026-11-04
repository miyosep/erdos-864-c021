"""Finite consistency checks in F_p[X]/(X^2-d).

Run standalone with a mode and optional --output directory. Search states are inner candidate visits;
periods count tested cuts/targets. One worker. JSON records exact finite scope.
"""
from limits import configure, deadline_check
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import gcd, pi, sqrt
import argparse
import cmath
import json
import os
from pathlib import Path


class Cap(Exception):
    pass


class Budget:
    def __init__(self):
        self.states = self.periods = 0
        self.smax = int(os.environ['MATH_MAX_STATES'])
        self.pmax = int(os.environ['MATH_MAX_PERIOD_ENUMERATION'])
        assert int(os.environ['MATH_MAX_PARALLEL_WORKERS']) >= 1

    def tick(self, n=1):
        deadline_check(Cap)
        if self.states+n > self.smax:
            raise Cap('state cap')
        self.states += n

    def period(self):
        deadline_check(Cap)
        if self.periods+1 > self.pmax:
            raise Cap('period cap')
        self.periods += 1


class Field:
    # F_p[X]/(X^2-d), pairs (constant, X coefficient).
    def __init__(self, p):
        self.p = p
        self.d = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)

    def add(self, x, y):
        return ((x[0]+y[0]) % self.p, (x[1]+y[1]) % self.p)

    def neg(self, x):
        return (-x[0] % self.p, -x[1] % self.p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        return ((x[0]*y[0]+self.d*x[1]*y[1]) % self.p,
                (x[0]*y[1]+x[1]*y[0]) % self.p)

    def bar(self, x):
        return (x[0], -x[1] % self.p)

    def div(self, x, y):
        assert y != (0, 0)
        n = (y[0]**2-self.d*y[1]**2) % self.p
        ni = pow(n, -1, self.p)
        return self.mul(x, (y[0]*ni % self.p, -y[1]*ni % self.p))

    def table(self, theta):
        powers, logs = [], {}
        z = (1, 0)
        for i in range(self.p**2-1):
            if z in logs:
                return None
            powers.append(z)
            logs[z] = i
            z = self.mul(z, theta)
        assert z == (1, 0)
        return powers, logs

    def primitives(self, cap):
        ans = []
        for x in product(range(self.p), repeat=2):
            cap.tick()
            if x != (0, 0) and self.table(x) is not None:
                ans.append(x)
        return ans


def hist(B, cap):
    """Three-sum histogram then one negative slot, exact ordered integers."""
    triple = Counter()
    for a, b, c in product(B, repeat=3):
        cap.tick()
        triple[a+b+c] += 1
    result = Counter()
    for s, n in triple.items():
        for d in B:
            cap.tick()
            result[s-d] += n
    return result


def direct_hist(B, cap):
    ans = Counter()
    for a, b, c, d in product(B, repeat=4):
        cap.tick()
        ans[a+b+c-d] += 1
    return ans


def admissible(A, cap):
    sums = Counter()
    for a, b in combinations_with_replacement(sorted(A), 2):
        cap.tick()
        sums[a+b] += 1
    return sum(v > 1 for v in sums.values()) <= 1


def profile(y):
    def cdf(z):
        return sum((-1)**j * (1, 3, 3, 1)[j] * max(z-j, Fraction(0))**3
                   for j in range(4))/Fraction(6)
    return cdf(y+1)-cdf(y)


def audit(cap):
    summary = []
    for p in (3, 5, 7):
        f = Field(p)
        primitives = f.primitives(cap)
        if p == 7:
            primitives = primitives[:1]
        maxbad = maxomitted = 0
        totalkept = targets = 0
        maxrowratio = 0.0
        for theta in primitives:
            powers, logs = f.table(theta)
            L = [f.add(theta, (a, 0)) for a in range(p)]
            index = {x: a for a, x in enumerate(L)}
            D = f.sub(theta, f.bar(theta))
            for gamma in powers:
                cap.period()
                targets += 1
                actual = set()
                # Brute first three field coordinates, direct lookup of fourth.
                for a, b, c in product(range(p), repeat=3):
                    cap.tick()
                    evalue = f.div(f.mul(f.mul(L[a], L[b]), L[c]), gamma)
                    if evalue in index:
                        actual.add((a, b, c, index[evalue]))
                kept = set()
                bad = 0
                z1pairs = 0
                for a in range(p):
                    cap.tick()
                    k = f.div(L[a], gamma)
                    w = f.sub(f.div(f.bar(gamma), f.bar(L[a])), f.bar(theta))
                    excluded = (k == f.bar(k) or w == f.bar(w)
                                or w == f.neg(theta) or w == f.neg(f.bar(theta)))
                    assert w != f.neg(f.bar(theta))
                    if excluded:
                        bad += 1
                    rows = []
                    for b in range(p):
                        cap.tick()
                        z = f.mul(k, L[b])
                        if z == (1, 0):
                            z1pairs += 1
                        fibre = [q for q in actual if q[0:2] == (a, b)]
                        if z == f.bar(z):
                            assert len(fibre) == (p if z == (1, 0) else 0)
                            continue
                        C = f.div(f.mul(D, f.sub((1, 0), f.bar(z))), f.sub(z, f.bar(z)))
                        E = f.mul(z, C)
                        assert C in index and E in index
                        q = (a, b, index[C], index[E])
                        assert fibre == [q]
                        if not excluded:
                            r = f.div(f.neg(f.sub(f.mul(k, theta), f.mul(f.bar(k), f.bar(theta)))),
                                      f.sub(k, f.bar(k)))
                            assert r[1] == 0
                            lam = f.div(f.neg(f.mul(D, f.bar(k))), f.sub(k, f.bar(k)))
                            assert C == f.mul(lam, f.div(f.sub((b, 0), w), f.sub((b, 0), r)))
                            kept.add(q)
                            rows.append((b, C, w, r))
                    if not excluded:
                        assert len(rows) == p-1
                        # Direct finite local-character sums, all (j,h) for p<=5;
                        # selected nonzero modes for p=7. No CRT code is reused.
                        modes = product(range(p*p-1), repeat=2) if p <= 5 else ((1, 0), (0, 1), (1, -1))
                        for j, h in modes:
                            if j == h == 0:
                                continue
                            val = 0j
                            for b, C, w, r in rows:
                                cap.tick()
                                # Equation (C), using actual field multiplication.
                                exponent = (j*logs[L[b]] + h*logs[f.sub((b, 0), w)]
                                            - h*logs[f.sub((b, 0), r)])
                                val += cmath.exp(2j*pi*(exponent % (p*p-1))/(p*p-1))
                            assert abs(val) <= 4*sqrt(p)+1e-9
                            maxrowratio = max(maxrowratio, abs(val)/sqrt(p))
                assert bad <= 4 and z1pairs <= 2
                assert kept <= actual and len(actual-kept) <= 6*p
                assert len(kept) == (p-bad)*(p-1)
                maxbad = max(maxbad, bad)
                maxomitted = max(maxomitted, len(actual-kept))
                totalkept += len(kept)
        summary.append(dict(p=p, primitive_count=len(primitives), targets=targets,
                            max_excluded_rows=maxbad, max_omitted=maxomitted,
                            retained_witnesses=totalkept, max_row_sum_over_sqrt_p=maxrowratio))
    return summary


def limits(cap):
    results = []
    finite_warning = None
    for p in (3, 5, 7, 11, 17, 23, 31):
        f = Field(p)
        theta = f.primitives(cap)[0]
        _, logs = f.table(theta)
        M = p*p-1
        for t in sorted({0, M//3, M-1}):
            cap.period()
            B = sorted((logs[f.add(theta, (a, 0))]+t-1) % M+1 for a in range(p))
            R = hist(B, cap)
            if p <= 5:
                assert R == direct_hist(B, cap)
            errors = []
            for s in range(-M, 3*M+1):
                cap.tick()
                target = profile(Fraction(s, M))
                errors.append((abs(Fraction(R[s], p*p)-target), s))
                if finite_warning is None and R[s] == 0 and -1 < Fraction(s, M) < 3:
                    finite_warning = dict(p=p, theta=theta, t=t, B=B, s=s,
                                          profile=str(target), note='Finite interior coverage fails; asymptotic theorem only.')
            err, at = max(errors)
            results.append(dict(p=p, theta=theta, t=t, max_absolute_error=float(err),
                                exact_error=str(err), maximizing_s=at,
                                total_ordered_witnesses=sum(R.values())))
            assert sum(R.values()) == p**4
    return dict(distributions=results, finite_interior_hole=finite_warning)


def reflection(cap):
    cases = []
    overlap_example = None
    for p in (3, 5):
        f = Field(p)
        for theta in f.primitives(cap):
            _, logs = f.table(theta)
            M = p*p-1
            for t in range(M):
                cap.period()
                B = sorted((logs[f.add(theta, (a, 0))]+t-1) % M+1 for a in range(p))
                R = hist(B, cap)
                m, v = B[0], B[-1]
                feasible = []
                sep = []
                # Contains every possible improvement over the explicit upper
                # height: outside this range the hull is already >= upper bound.
                lo, hi = 3*m-v-1, 3*v-m+1
                for S in range(lo, hi+1):
                    cap.tick()
                    A = set(B) | {S-b for b in B}
                    assert len(set(B) & {S-b for b in B}) <= 2
                    span = max(A)-min(A)+1
                    assert span == v-m+abs(S-(m+v))+1
                    ok = admissible(A, cap)
                    if S > 2*v:
                        assert ok == (R[S] == 0)
                    if ok:
                        assert R[S] <= 6*p
                        feasible.append((span, S))
                        if S > 2*v:
                            sep.append((span, S))
                        if R[S] and S <= 2*v and overlap_example is None:
                            overlap_example = dict(p=p, theta=theta, t=t, B=B, S=S,
                                                   A=sorted(A), R=R[S], span=span)
                assert feasible and sep
                cases.append(dict(p=p, theta=theta, t=t, unrestricted=min(feasible), separated=min(sep)))
    return dict(cases=cases, positive_R_admissible_example=overlap_example)


def deletions(cap):
    checked = sidon_count = 0
    # All nonempty Sidon subsets of [1,7], all deletions, all relevant sums.
    for mask in range(1, 1 << 7):
        cap.tick()
        B = [a+1 for a in range(7) if mask >> a & 1]
        sums = [a+b for a, b in combinations_with_replacement(B, 2)]
        if len(sums) != len(set(sums)):
            continue
        sidon_count += 1
        p = len(B)
        R = direct_hist(B, cap)
        for dm in range(1 << p):
            cap.period()
            C = [b for i, b in enumerate(B) if not dm >> i & 1]
            d = p-len(C)
            RC = direct_hist(C, cap)
            for s in range(3*min(B)-max(B), 3*max(B)-min(B)+1):
                cap.tick()
                assert RC[s] >= R[s]-8*p*d
                if admissible(set(C) | {s-c for c in C}, cap):
                    assert RC[s] <= 6*len(C)
                checked += 1
    return dict(ambient_interval=[1, 7], sidon_sets=sidon_count, sum_deletion_checks=checked)


def crt_lifts(cap):
    def evaluate(f, coeff, x):
        z = (0, 0)
        for v in reversed(coeff):
            z = f.add(f.mul(z, x), (v, 0))
        return z

    def interpolate(f, x, y, z, desired):
        # Solve the five F_p evaluation coordinates for a degree<5 polynomial.
        powers = []
        for point in (x, y, z):
            row = [(1, 0)]
            for _ in range(4):
                row.append(f.mul(row[-1], point))
            powers.append(row)
        matrix = [[q[k] for q in powers[i]] for i, k in ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0))]
        rhs = [desired[0][0], desired[0][1], desired[1][0], desired[1][1], desired[2][0]]
        rows = [row+[v] for row, v in zip(matrix, rhs)]
        for j in range(5):
            cap.tick()
            pivot = next(i for i in range(j, 5) if rows[i][j] % f.p)
            rows[j], rows[pivot] = rows[pivot], rows[j]
            inv = pow(rows[j][j], -1, f.p)
            rows[j] = [v*inv % f.p for v in rows[j]]
            for i in range(5):
                if i != j:
                    factor = rows[i][j]
                    rows[i] = [(a-factor*b) % f.p for a, b in zip(rows[i], rows[j])]
        coeff = [rows[i][-1] for i in range(5)]
        assert tuple(evaluate(f, coeff, u) for u in (x, y, z)) == desired
        return coeff

    counts = Counter()
    for p in (3, 5):
        f = Field(p)
        M = p*p-1
        for theta in f.primitives(cap):
            powers, logs = f.table(theta)
            L = [f.add(theta, (a, 0)) for a in range(p)]
            index = {v: a for a, v in enumerate(L)}
            for gamma in powers:
                for a in range(p):
                    cap.tick()
                    k = f.div(L[a], gamma)
                    w = f.sub(f.div(f.bar(gamma), f.bar(L[a])), f.bar(theta))
                    if k == f.bar(k) or w == f.bar(w) or w in (f.neg(theta), f.neg(f.bar(theta))):
                        continue
                    r = f.div(f.neg(f.sub(f.mul(k, theta), f.mul(f.bar(k), f.bar(theta)))), f.sub(k, f.bar(k)))
                    for desired in ((theta, (1, 0), (1, 0)), ((1, 0), theta, (1, 0))):
                        interpolate(f, theta, f.neg(w), f.neg(r), desired)
                    # The two unit polynomials isolate the full-order character
                    # in each quadratic component, establishing finite
                    # nonprincipality for every nonzero (j,h).
                    counts['retained_rows_with_explicit_CRT_preimages'] += 1
                actual = []
                for a, b, c in product(range(p), repeat=3):
                    cap.tick()
                    evalue = f.div(f.mul(f.mul(L[a], L[b]), L[c]), gamma)
                    if evalue in index:
                        actual.append((a, b, c, index[evalue]))
                for t in range(M):
                    cap.period()
                    beta = [(logs[v]+t-1) % M+1 for v in L]
                    residue = (logs[gamma]+2*t) % M
                    for a, b, c, e in actual:
                        value = beta[a]+beta[b]+beta[c]-beta[e]
                        assert value % M == residue
                        for carry in range(-2, 4):
                            cap.tick()
                            s = residue+carry*M
                            numerator = beta[a]+beta[b]+beta[c]-s
                            assert (value == s) == (0 < numerator <= M)
                            if numerator in (0, M):
                                counts['zero_or_one_boundary_cases'] += 1
                        counts['modular_witness_cut_checks'] += 1
    return dict(counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('part', choices=['audit', 'limits', 'reflection', 'deletions', 'crt_lifts'])
    parser.add_argument('--output')
    args = parser.parse_args()
    configure(args.output, args.part)
    cap = Budget()
    result = dict(part=args.part, seed=os.environ.get('MATH_SEED'),
                  independent_expert_review=False, formal_verification=False)
    try:
        result['data'] = globals()[args.part](cap)
        result['status'] = 'PASS'
        result['truncated'] = False
    except Cap as ex:
        result.update(status='LIMIT', truncated=True, reason=str(ex))
    except Exception as ex:
        result.update(status='FAIL', truncated=False, reason=repr(ex))
        raise
    finally:
        result.update(states=cap.states, periods=cap.periods, workers=1,
                      limits=dict(states=cap.smax, periods=cap.pmax, workers=1))
        out = Path(os.environ['MATH_RUN_DIR'])/'outputs'
        out.mkdir(exist_ok=True)
        (out/(args.part+'.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print(json.dumps({k: v for k, v in result.items() if k != 'data'}))

    if result['status'] != 'PASS':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
