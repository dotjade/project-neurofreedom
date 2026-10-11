#!/usr/bin/env python3
"""Independent exact-arithmetic checks of the saved aggregate calculations.
Does not import the producer's code, read participant data, or modify producer files.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json
root = Path('/workspace/shared/neurofreedom_mns_attrition')
r = json.loads((root/'results.json').read_text())
checks = 0

def eq(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def saved(v):
    return F(v['exact_fraction'])

N = 41
B = F(1862,100)
pooled = (36 * F(1883,100) + 5 * 19)/41
eq(saved(r['baseline_consistency']['pooled_subgroup_mean']),pooled)
eq(saved(r['baseline_consistency']['discrepancy']),F(473,2050))
for branch,base in zip(r['branches'],[B,pooled]):
    for row,(n,y,br) in zip(branch['timepoints'],[(36,F(1625,100),F(1883,100)),(15,F(1533,100),F(1873,100))]):
        m = N-n
        observed_total = n*y
        retained_baseline_total = n*br
        baseline_total = N*base
        missing_baseline = (baseline_total - retained_baseline_total)/m
        threshold = (baseline_total-observed_total)/m
        eq(saved(row['full_change_lower']),(observed_total-baseline_total)/N)
        eq(saved(row['full_change_upper']),(observed_total+25*m-baseline_total)/N)
        eq(saved(row['returnee_paired_change']),y-br)
        eq(saved(row['implied_missing_baseline']),missing_baseline)
        eq(saved(row['tipping_missing_followup']),threshold)
        eq(saved(row['tipping_missing_change']),threshold-missing_baseline)
        eq(observed_total + m*threshold,baseline_total)
        for scenario in row['scenarios']:
            missing=saved(scenario['missing_mean'])
            change=(observed_total + m*missing-baseline_total)/N
            eq(saved(scenario['full_change']),change)
            eq(saved(scenario['missing_mean_change']),missing-missing_baseline)
            eq(scenario['feasible'],0 <= missing <= 25)
        # Check all interval corners of baseline, observed, and returnee baseline.
        # For the pooled branch these are conservative because subgroup variables
        # overlap; all actually correlated cases lie within this larger box.
        eps=F(5,1000)
        base_interval=([B-eps,B+eps] if base==B else [(36*(F(1883,100)-eps)+5*F('18.95'))/41,(36*(F(1883,100)+eps)+5*F('19.05'))/41])
        env=row['rounding_envelope_not_ci']
        for bv,yv,brv in product(base_interval,[y-eps,y+eps],[br-eps,br+eps]):
            lower=(n*yv-N*bv)/N
            upper=(n*yv+25*m-N*bv)/N
            tip=(N*bv-n*yv)/m
            tipchange=n*(brv-yv)/m
            assert saved(env['full_change_lower']) <= lower
            assert upper <= saved(env['full_change_upper'])
            assert saved(env['tipping_missing_followup_lower']) <= tip <= saved(env['tipping_missing_followup_upper'])
            assert saved(env['tipping_missing_change_lower']) <= tipchange <= saved(env['tipping_missing_change_upper'])
            checks+=4
# Direct cancellation calculation independently establishes the main threshold.
eq(15*(F('18.73')-F('15.33')),F(51))
eq(F(51,26),F(1)+F(25,26))
eq((26*F(2)-51)/41,F(1,41))
# The +2 missing-mean worsening result remains positive across paired rounding.
assert (26*2-15*F('3.41'))/41 > 0
checks+=1
metadata=json.loads((root/'run_metadata.json').read_text())
for path,expected in metadata['sha256'].items():
    eq(hashlib.sha256((root/path).read_bytes()).hexdigest(),expected)
print(f'PASS: {checks} independent exact and corner-envelope checks, including run-metadata hashes.')
print('No main-worker files modified. Source verification: publisher Results motor paragraphs and Methods Outcome measures.')
