"""Independent SYNTHETIC arithmetic check, not human data or a clinical test.

Run from repository root:
    python updates/2026-10-31/independent_math_check.py

Uses only Python's standard library. No imports from the implementation being
checked, no network, no random sampling, no seed, and no output-file writes.
Exact rational raw moments are expanded using Gaussian even moments before
conversion to floating point for comparisons with the saved numerical artifact.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[2]

def main():
    data = json.loads((ROOT / 'analyses/force_matching/2026-10-31/synthetic-results.json').read_text())
    checks = []

    def check(label, valid):
        assert valid, label
        checks.append(label)

    def close(x, y):
        return math.isclose(float(x), float(y), rel_tol=1e-11, abs_tol=1e-11)

    for index, row in enumerate(data['memory_rows']):
        target = F(str(row['target']))
        indirect = F(1, 2) + F(2, 3) * target
        direct = F(3, 2) * indirect
        expected = [('indirect', indirect), ('direct', direct),
                    ('direct_minus_target', F(3, 4)),
                    ('direct_over_indirect', F(3, 2)),
                    ('direct_minus_indirect', indirect / 2)]
        for key, value in expected:
            check(f'row{index}:{key}', close(row[key], value))

    def normal_raw(mean, variance, order):
        value = F(0)
        for j in range(0, order + 1, 2):
            double_factorial = math.prod(range(1, j, 2)) if j else 1
            value += (math.comb(order, j) * mean ** (order-j)
                      * variance ** (j//2) * double_factorial)
        return value

    for index, row in enumerate(data['distribution_rows']):
        mean = F(row['indirect_mean'])
        indirect_raw = [normal_raw(mean, F(9, 100), n) for n in range(4)]
        factor_raw = [normal_raw(F(3, 2), F(1, 25), n) for n in range(4)]
        product_raw = [a*b for a, b in zip(indirect_raw, factor_raw)]
        variance = product_raw[2] - product_raw[1]**2
        central3 = (product_raw[3] - 3*product_raw[1]*product_raw[2]
                    + 2*product_raw[1]**3)
        skewness = float(central3) / float(variance)**1.5
        expected = [('mean', product_raw[1]), ('variance', variance),
                    ('skewness', skewness)]
        for key, value in expected:
            check(f'product{index}:{key}', close(row['divisive'][key], value))
            check(f'calibration{index}:{key}', close(row['calibration_only'][key], value))
        check(f'subtractive{index}:mean', close(row['subtractive']['mean'], mean+F(3, 4)))
        check(f'subtractive{index}:variance', close(row['subtractive']['variance'], F(13, 100)))
        check(f'subtractive{index}:skew', row['subtractive']['skewness'] == 0)

    check('no random sampling', data['seed'] is None and not data['random_sampling'])
    check('explicit synthetic label', 'NOT HUMAN OR TOURETTE DATA' in data['label'])
    receipt = json.loads((ROOT / 'updates/2026-10-31/independent-review.json').read_text())
    assert checks == receipt['independent_math']['checks'], 'receipt assertion identities differ'
    assert len(checks) == receipt['independent_math']['checks_passed'] == 59
    print(json.dumps({'checks_passed': len(checks), 'receipt_matches': True,
                      'method': 'Independent exact rational Gaussian raw moments; synthetic arithmetic only.'}, indent=2))

if __name__ == '__main__':
    main()
