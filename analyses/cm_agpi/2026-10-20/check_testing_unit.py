"""Original combinatorial audit only; no participant data or effect reconstruction.

Post-reading diagnostic plan (not preregistered): enumerate all equally likely sign allocations for five distinct nonzero
paired differences under the exact signed-rank null, then obtain the minimum
standard doubled-tail p value. The all-positive/all-negative outcomes are each
one of 2**n allocations. This checks a possible interpretation of a published
method, not which method implementation the authors actually used.
"""
from itertools import product
import json
from pathlib import Path

def check(n):
    sums = [sum(rank for rank, sign in zip(range(1,n+1), signs) if sign)
            for signs in product((False, True), repeat=n)]
    total=n*(n+1)//2
    two_sided=[]
    for s in sums:
        lower=sum(t <= s for t in sums)/len(sums)
        upper=sum(t >= s for t in sums)/len(sums)
        two_sided.append(min(1., 2*min(lower,upper)))
    return {"n_independent_nonzero_pairs":n,"sign_configurations":len(sums),
            "minimum_exact_two_sided_p":min(two_sided),
            "closed_form_minimum":2**(1-n),"total_rank_sum":total}

out={"scope":"post-reading mathematical compatibility diagnostic, not preregistered; no study-data analysis",
     "prediction":"Under the stated exact signed-rank assumptions, minimum two-sided p for five independent pairs is 2/32 = 0.0625.",
     "assumptions":["five independent participant-level paired differences", "no zero differences", "distinct absolute ranks", "exact symmetric sign-flip null", "standard doubled-tail two-sided p value"],
     "results":[check(5),check(6)],
     "conclusion":"Reported very small p values cannot be interpreted as exact signed-rank tests of five paired participant summaries. This does not establish an author error: the testing unit or implementation may differ and is unresolved. This check cannot select between participant, time, frequency or epoch units, or identify an asymptotic implementation."}
assert out['results'][0]['minimum_exact_two_sided_p'] == 0.0625
assert out['results'][1]['minimum_exact_two_sided_p'] == 0.03125
assert all(x['minimum_exact_two_sided_p']==x['closed_form_minimum'] for x in out['results'])
Path(__file__).with_name('testing-unit-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
