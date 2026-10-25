"""Conditional set arithmetic, no participant records or clinical estimation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def calculate(d):
    a=d['cohorts']['NCT02056873']; b=d['cohorts']['NCT05371041']
    m=next(r['n'] for r in d['reports'] if len(r['cohorts'])==2)
    # Pairwise overlap k has union a+b-k. Mixed report must fit in union.
    overlaps=[k for k in range(min(a,b)+1) if a+b-k>=m]
    if not overlaps: raise ValueError('Incompatible counts/containment assumptions')
    unions=[a+b-k for k in overlaps]
    allocations=[{'older_trial':x,'newer_trial':m-x} for x in range(a+1) if 0<=m-x<=b]
    return {'report_roles':len(d['reports']), 'named_trial_families':len(d['cohorts']),
            'invalid_naive_role_sum':sum(r['n'] for r in d['reports']),
            'conditional_union_bounds_no_disjointness':[min(unions),max(unions)],
            'conditional_cohort_overlap_bounds':[min(overlaps),max(overlaps)],
            'if_disjoint_union':a+b, 'if_disjoint_preprint_allocations':allocations,
            'without_preprint_and_without_disjointness_bounds':[max(a,b),a+b],
            'interpretation':'Conditional set constraints, not observed unique count, efficacy sample size, confidence interval, safety denominator or independent replication.'}

if __name__=='__main__':
    d=json.loads((ROOT/'inputs.json').read_text())
    (ROOT/'results.json').write_text(json.dumps(calculate(d),indent=2)+'\n')
