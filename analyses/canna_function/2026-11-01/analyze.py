"""Deterministic public-aggregate audit; no participant data or RNG.
Newcombe independent-proportions hybrid Wilson interval, no continuity correction.
Not the published center-stratified model. Python standard library only.
"""
import json, math
from decimal import Decimal
from pathlib import Path
from statistics import NormalDist
BASE=Path(__file__).resolve().parent

def wilson(x,n,z=NormalDist().inv_cdf(.975)):
    if not 0<=x<=n or n<=0: raise ValueError('Invalid binomial counts')
    p=x/n; d=1+z*z/n
    c=(p+z*z/(2*n))/d
    h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return c-h,c+h

def riskdiff(x1,n1,x0,n0):
    p1,p0=x1/n1,x0/n0
    l1,u1=wilson(x1,n1); l0,u0=wilson(x0,n0)
    d=p1-p0
    return d,[d-math.hypot(p1-l1,u0-p0),d+math.hypot(u1-p1,p0-l0)]

def audit(a):
    x1,x0=a['primary']['responders']; n1,n0=a['primary']['n']
    rd,ci=riskdiff(x1,n1,x0,n0)
    rr=(x1/n1)/(x0/n0)
    se=math.sqrt(1/x1-1/n1+1/x0-1/n0)
    z=NormalDist().inv_cdf(.975)
    rows=[]
    for r in a['functional_rows']:
        dec=lambda k:Decimal(str(r[k]))
        diff=dec('arm_lsm_nabiximols')-dec('arm_lsm_placebo')
        discrepancy=diff-dec('reported_contrast')
        # Conditional conventional rounding +/- .005 for each two-decimal LSM/contrast.
        rows.append({'endpoint':r['endpoint'],'reported_contrast':r['reported_contrast'],'ci95':[r['ci95_lower'],r['ci95_upper']],
                     'interval_contains_zero':r['ci95_lower']<=0<=r['ci95_upper'],
                     'lsm_subtraction':str(diff),'subtraction_minus_reported':str(discrepancy),
                     'compatible_under_two_decimal_rounding':abs(discrepancy)<=Decimal('.015'),
                     'reported_p':r['reported_p']})
    return {'classification':'Exploratory deterministic published-aggregate audit, not simulation or clinical validation',
            'seed':None,'primary_unadjusted':{'direction':'nabiximols minus placebo',
            'response_proportions':[x1/n1,x0/n0],'risk_difference':rd,'newcombe_wilson_95ci':ci,
            'risk_ratio':rr,'log_wald_rr_95ci':[math.exp(math.log(rr)-z*se),math.exp(math.log(rr)+z*se)],
            'limitations':'Independent unadjusted binary estimates do not reconstruct center-stratified Mantel-Haenszel analysis. Missing primary outcomes classified nonresponse as in source. RR interval is approximate and small event counts limit precision.'},
            'functional_audit':rows,'functional_intervals_including_zero':sum(r['interval_contains_zero'] for r in rows),
            'functional_rounding_compatible_rows':sum(r['compatible_under_two_decimal_rounding'] for r in rows),
            'ae_descriptive_proportions':[a['harms']['any_ae_people'][i]/a['harms']['exposed'][i] for i in range(2)],
            'ae_discontinuation_proportions':[a['harms']['ae_discontinuations_registry'][i]/a['harms']['exposed'][i] for i in range(2)],
            'no_new_functional_sampling_estimate':'Use reported ANCOVA contrasts/CI unchanged. No pooling, multiplicity claim, equivalence margin, clinical threshold or reconstructed covariance.'}

if __name__=='__main__':
    a=json.loads((BASE/'inputs.json').read_text())
    (BASE/'results.json').write_text(json.dumps(audit(a),indent=2)+'\n')
