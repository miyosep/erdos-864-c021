"""Exact new verifier in F_p[X]/(X^2-X-d); no historical-code imports."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import os
from pathlib import Path


class Limit(Exception):
    pass


states = periods = 0
smax = int(os.environ['MATH_MAX_STATES'])
pmax = int(os.environ['MATH_MAX_PERIOD_ENUMERATION'])
assert int(os.environ['MATH_MAX_PARALLEL_WORKERS']) >= 1


def tick(n=1):
    global states
    if states+n > smax:
        raise Limit('state cap')
    states += n


def period():
    global periods
    if periods+1 > pmax:
        raise Limit('period cap')
    periods += 1


def check_prime(p):
    # X^2=X+d has nonsquare discriminant. Coordinates are in 1,X.
    d = next(d for d in range(p) if pow((1+4*d) % p, (p-1)//2, p) == p-1)
    M = p*p-1

    def add(x, y):
        return ((x[0]+y[0]) % p, (x[1]+y[1]) % p)

    def neg(x):
        return (-x[0] % p, -x[1] % p)

    def sub(x, y):
        return add(x, neg(y))

    def mul(x, y):
        return ((x[0]*y[0]+d*x[1]*y[1]) % p,
                (x[0]*y[1]+x[1]*y[0]+x[1]*y[1]) % p)

    def bar(x):
        return ((x[0]+x[1]) % p, -x[1] % p)

    def div(x, y):
        assert y != (0, 0)
        norm = mul(y, bar(y))
        assert norm[1] == 0 and norm[0]
        a = pow(norm[0], -1, p)
        return mul(x, mul((a, 0), bar(y)))

    result = dict(p=p, polynomial_d=d, primitives=0, targets=0,
                  singular_max=0, omitted_max=0, max_excluded_rows=0,
                  selectors=0, upper_boundary=0, lower_boundary=0)
    for theta in product(range(p), repeat=2):
        tick()
        if theta == (0, 0):
            continue
        powers = []
        z = (1, 0)
        while z not in powers:
            tick()
            powers.append(z)
            z = mul(z, theta)
        if len(powers) != M:
            continue
        result['primitives'] += 1
        log = {z: i for i, z in enumerate(powers)}
        L = [add(theta, (a, 0)) for a in range(p)]
        # Full enumeration of (a,b,c) with e read off from actual product.
        index = {v: a for a, v in enumerate(L)}
        for gamma in powers:
            period()
            result['targets'] += 1
            full, good = [], []
            excluded = set()
            for a in range(p):
                tick()
                k = div(L[a], gamma)
                w = sub(div(bar(gamma), bar(L[a])), bar(theta))
                if k[1] == 0 or w[1] == 0 or w in (neg(theta), neg(bar(theta))):
                    excluded.add(a)
            singular = 0
            singular_pairs = 0
            for a, b in product(range(p), repeat=2):
                z = div(mul(L[a], L[b]), gamma)
                fibre = []
                for c in range(p):
                    tick()
                    E = mul(z, L[c])
                    if E in index:
                        fibre.append((a, b, c, index[E]))
                if z[1] == 0:
                    assert len(fibre) == (p if z == (1, 0) else 0)
                    if fibre:
                        singular_pairs += 1
                        assert all(q[2] == q[3] for q in fibre)
                    singular += len(fibre)
                else:
                    assert len(fibre) == 1
                    if a not in excluded:
                        good.extend(fibre)
                full.extend(fibre)
            assert singular_pairs <= 2 and singular <= 2*p
            assert len(excluded) <= 4
            assert len(good) == (p-len(excluded))*(p-1)
            assert len(full)-len(good) <= 6*p
            result['singular_max'] = max(result['singular_max'], singular)
            result['omitted_max'] = max(result['omitted_max'], len(full)-len(good))
            result['max_excluded_rows'] = max(result['max_excluded_rows'], len(excluded))
            for t in sorted({0, M//3, M-1}):
                period()
                beta = [(log[x]+t-1) % M+1 for x in L]
                residue = (log[gamma]+2*t) % M
                exact = Counter(beta[a]+beta[b]+beta[c]-beta[e] for a,b,c,e in full)
                selected = Counter(beta[a]+beta[b]+beta[c]-beta[e] for a,b,c,e in good)
                assert all((v-residue) % M == 0 for v in exact)
                # Every possible nonzero integer lift of this residue lies here;
                # outside [-M,3M] counts and F vanish identically.
                for carry in range(-2, 4):
                    tick()
                    s = residue+carry*M
                    count = 0
                    for a,b,c,e in good:
                        tick()
                        u = beta[a]+beta[b]+beta[c]-s
                        assert (u == beta[e]) == (0 < u <= M)
                        count += (0 < u <= M)
                        result['upper_boundary'] += (u == M)
                        result['lower_boundary'] += (u == 0)
                    assert count == selected[s]
                    assert 0 <= exact[s]-selected[s] <= 6*p
                    result['selectors'] += len(good)
    return result


def geometry():
    records = []
    for K in (2, 5, 13):
        bysum = Counter()
        for a,b,c in product(range(1, K+1), repeat=3):
            tick()
            bysum[a+b+c] += 1
        maximum = Fraction(0)
        for j in range(-4*K, 8*K+1):
            period()
            y = Fraction(j, 2*K)
            low = high = 0
            for tot, n in bysum.items():
                tick()
                left, right = Fraction(tot-3, K), Fraction(tot, K)
                low += n*(left >= y and right <= y+1)
                high += n*(right > y and left < y+1)
            gap = Fraction(high-low, K**3)
            assert 0 <= gap <= Fraction(12, K)
            maximum = max(maximum, gap)
        records.append(dict(K=K, max_boundary_box_volume=str(maximum),
                            proved_upper=str(Fraction(12, K)),
                            targets='j/(2K), -4K<=j<=8K, all grid combinatorial regimes'))
    return records


out = dict(seed=os.environ.get('MATH_SEED'), workers=1,
           independent_implementation_of_historical_code=True,
           independent_reviewer_or_formal_proof=False,
           note='Finite checks do not verify the asymptotic limit or external character theorem.')
try:
    out['prime_checks'] = [check_prime(p) for p in (3, 5, 7)]
    out['geometry'] = geometry()
    out.update(status='PASS', truncated=False)
except Limit as ex:
    out.update(status='LIMIT', truncated=True, reason=str(ex))
except Exception as ex:
    out.update(status='FAIL', truncated=False, reason=repr(ex))
    raise
finally:
    out.update(states=states, periods=periods,
               limits=dict(states=smax, periods=pmax, workers=1))
    target = Path(os.environ['MATH_RUN_DIR'])/'outputs'
    target.mkdir(exist_ok=True)
    (target/'singular_uniform.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('prime_checks','geometry')}))
