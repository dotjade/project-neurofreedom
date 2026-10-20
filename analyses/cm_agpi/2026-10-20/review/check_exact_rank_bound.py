"""Independent rank-sum generating-function check; no research data."""
import json
import argparse
from pathlib import Path
from fractions import Fraction

# Coefficients of product(1 + x**r) count sign allocations by positive-rank sum.
def distribution(n):
    coefficients = [1]
    for rank in range(1, n + 1):
        updated = coefficients + [0] * rank
        for exponent, count in enumerate(coefficients):
            updated[exponent + rank] += count
        coefficients = updated
    return coefficients

checks=[]
for n in (5,6):
    c=distribution(n)
    total=sum(c)
    assert total==2**n
    assert c[0]==c[-1]==1
    pvalues=[min(Fraction(1),2*min(Fraction(sum(c[:i+1]),total),Fraction(sum(c[i:]),total))) for i in range(len(c)) if c[i]]
    minimum=min(pvalues)
    assert minimum==Fraction(2,2**n)
    checks.append({'n':n,'rank_sum_counts':c,'sign_patterns':total,'minimum_exact_two_sided_p':float(minimum),'fraction':str(minimum)})
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('main_output', nargs='?', type=Path,
                    default=Path(__file__).resolve().parent.parent / 'testing-unit-check.json',
                    help='Main audit diagnostic JSON; defaults to the parent audit directory.')
args=parser.parse_args()
main=json.loads(args.main_output.read_text())
assert [x['minimum_exact_two_sided_p'] for x in checks]==[x['minimum_exact_two_sided_p'] for x in main['results']]
result={'method':'independent generating-function derivation',
        'scope':'Exact two-sided doubled-tail signed-rank test under equiprobable signs, independent nonzero paired differences and distinct absolute ranks. No claim about which observations or test implementation the paper actually used.',
        'checks':checks,'matches_main_check':True}
Path(__file__).with_name('independent-testing-unit-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
