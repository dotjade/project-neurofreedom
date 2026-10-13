#!/usr/bin/env python3
"""Independent public-aggregate audit. No source full text or person-level data.
Run: python review/independent_checks.py
SciPy is used solely for integer feasibility of severe-cell bounds.
"""
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from statistics import NormalDist

import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
WORKER = HERE.parent
d = json.loads((HERE/'reviewer_inputs.json').read_text())

# Independent score-test inversion: solve its quadratic boundary directly.
def score_interval(k, n):
    z = NormalDist().inv_cdf(.975)
    a = n + z*z
    b = -(2*k + z*z)
    c = k*k/n
    root = math.sqrt(b*b-4*a*c)
    return [(-b-root)/(2*a),(-b+root)/(2*a)]

j = d['jeon']
tp = j['overlap_cbit']+j['overlap_pst']
ip = j['index_positive_cbit']+j['index_positive_pst']
fp = ip-tp
fn = j['reference_positive']-tp
tn = j['reference_negative']-fp
assert [tp,fp,fn,tn]==[63,25,9,135]
n=j['n']
po=Fraction(tp+tn,n)
pe=Fraction(ip*j['reference_positive']+(n-ip)*j['reference_negative'],n*n)
kappa=(po-pe)/(1-pe)
metrics={
    'sensitivity':(tp,j['reference_positive']),
    'specificity':(tn,j['reference_negative']),
    'positive_predictive_value':(tp,ip),
    'negative_predictive_value':(tn,n-ip),
    'agreement':(tp+tn,n), 'discordance':(fp+fn,n),
}
independent={name:{'numerator':k,'denominator':n,'estimate':k/n,
                   'score_ci95':score_interval(k,n)} for name,(k,n) in metrics.items()}
prior=json.loads((WORKER/'aggregate_checks.json').read_text())
for name,r in independent.items():
    assert r['estimate']==prior[name]['estimate']
    assert max(abs(a-b) for a,b in zip(r['score_ci95'],prior[name]['wilson_ci95']))<1e-12
assert float(kappa)==prior['kappa']['estimate']

# Re-execute supplied analyze/checks functions without main's write side effect.
spec=importlib.util.spec_from_file_location('worker_checks',WORKER/'aggregate_checks.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
winputs=json.loads((WORKER/'aggregate_inputs.json').read_text())
rerun=m.analyze(winputs);passed=m.checks(winputs,rerun)
rerun['verification']={'passed_checks':len(passed),'checks':passed}
assert rerun==prior

# Optimize only an unknown aggregate severe/severe cell. Feasible tables are
# mathematical witnesses, not estimated actual tables, and are never saved.
def sharp_severe_bounds(row, col, matches):
    size=len(row); a=[];rhs=[]
    for i in range(size):
        v=np.zeros((size,size));v[i,:]=1;a.append(v.ravel());rhs.append(row[i])
    for i in range(size):
        v=np.zeros((size,size));v[:,i]=1;a.append(v.ravel());rhs.append(col[i])
    a.append(np.eye(size).ravel());rhs.append(matches)
    a=np.asarray(a); rhs=np.asarray(rhs)
    c=np.zeros(size*size);c[5*size+5]=1
    results=[]
    for direction in (1,-1):
        r=milp(c*direction, integrality=np.ones(size*size),
               bounds=Bounds(np.zeros(size*size),np.full(size*size,sum(row))),
               constraints=LinearConstraint(a,rhs,rhs))
        assert r.success
        x=np.rint(r.x).astype(int)
        assert np.max(abs(r.x-x))<1e-6 and np.array_equal(a@x,rhs)
        results.append(int(x[5*size+5]))
    return results

mc=d['mcguire']; rr=mc['cgi_counts']; results={}
for name,model in mc['models'].items():
    cc=model['counts'];n=mc['n'];assert sum(rr)==sum(cc)==n
    po=Fraction(model['matches'],n)
    pe=Fraction(sum(r*c for r,c in zip(rr,cc)),n*n)
    bounds=sharp_severe_bounds(rr,cc,model['matches'])
    frechet=[max(0,rr[5]+cc[5]-n),min(rr[5],cc[5])]
    assert bounds==frechet
    results[name]={'agreement':float(po),'kappa':float((po-pe)/(1-pe)),
                  'severe_TP_sharp_integer_bounds':bounds,
                  'severe_sensitivity_bounds':[x/rr[5] for x in bounds],
                  'minimum_missed_reference_severe':rr[5]-bounds[1]}

out={
 'audit_date':'2026-10-13',
 'worker_rerun_exact_output_match':True,
 'worker_tests_passed':len(passed),
 'independent_jeon':{'table':{'tp':tp,'fp':fp,'fn':fn,'tn':tn},
                     'metrics':independent,'kappa_exact':str(kappa),'kappa':float(kappa)},
 'mcguire_partial_identification':results,
 'bound_interpretation':'Conditional on the published pooled model labels and margins. Identification bounds, not confidence intervals. No unknown table or person-level record inferred. Does not resolve the printed score-43 overlap, validate a new cutoff, or identify adult/diagnosis-specific performance.',
 'versions':{'python':sys.version.split()[0],'scipy':scipy.__version__},
 'worker_sha256':{f:hashlib.sha256((WORKER/f).read_bytes()).hexdigest() for f in
                  ['aggregate_checks.py','aggregate_inputs.json','aggregate_checks.json','extraction.json','report.md','prespecified_question.md']}
}
(HERE/'independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
