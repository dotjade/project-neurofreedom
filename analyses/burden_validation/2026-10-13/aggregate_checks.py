#!/usr/bin/env python3
"""Reproduce published-aggregate response agreement; Python standard library only."""
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
Z = 1.959963984540054

def wilson(k, n):
    if not isinstance(k, int) or not isinstance(n, int) or n <= 0 or not 0 <= k <= n:
        raise ValueError('Require integers 0 <= k <= n, n > 0')
    p = k / n
    den = 1 + Z * Z / n
    center = (p + Z * Z / (2 * n)) / den
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return [0.0 if k == 0 else max(0.0, center - half),
            1.0 if k == n else min(1.0, center + half)]

def stat(k, n):
    return {'numerator': k, 'denominator': n, 'fraction': str(Fraction(k,n)),
            'estimate': k / n, 'wilson_ci95': wilson(k,n)}

def analyze(d):
    n=d['total']; pos=d['reference_positive_n']; neg=d['reference_negative_n']
    assert pos + neg == n
    tp=sum(a['reference_positive_n'] for a in d['arms_index_positive'].values())
    index_pos=sum(a['n'] for a in d['arms_index_positive'].values())
    fp=index_pos-tp; fn=pos-tp; tn=neg-fp
    assert min(tp,fp,fn,tn)>=0 and tp+fp+fn+tn==n
    po=Fraction(tp+tn,n)
    pe=Fraction((tp+fp)*(tp+fn)+(fn+tn)*(fp+tn),n*n)
    kappa=(po-pe)/(1-pe)
    return {
        'source':d['source'],
        'confusion': {'true_positive':tp,'false_positive':fp,'false_negative':fn,'true_negative':tn},
        'sensitivity':stat(tp,pos), 'specificity':stat(tn,neg),
        'positive_predictive_value':stat(tp,index_pos),
        'negative_predictive_value':stat(tn,n-index_pos),
        'agreement':stat(tp+tn,n), 'discordance':stat(fp+fn,n),
        'kappa': {'exact':str(kappa),'estimate':float(kappa),'ci95':None},
        'conditional_arm_positive_predictive_values': {
            name:stat(a['reference_positive_n'],a['n']) for name,a in d['arms_index_positive'].items()},
        'interpretation':'Within-sample descriptive classification concordance. No QoL outcome, adult-only accuracy, external validation, causal treatment contrast or surrogate validation.',
        'uncertainty':d['ci_method']
    }

def checks(d,r):
    tests=[]
    def check(name,truth):
        assert truth,name
        tests.append(name)
    check('reference margins',d['reference_positive_n']+d['reference_negative_n']==232)
    check('confusion exact',r['confusion']=={'true_positive':63,'false_positive':25,'false_negative':9,'true_negative':135})
    check('index positive margin',63+25==60+28)
    check('reference positive margin',63+9==72)
    check('sensitivity exact',r['sensitivity']['fraction']=='7/8')
    check('specificity exact',r['specificity']['fraction']=='27/32')
    check('ppv exact',r['positive_predictive_value']['fraction']=='63/88')
    check('npv exact',r['negative_predictive_value']['fraction']=='15/16')
    check('agreement+discordance',abs(r['agreement']['estimate']+r['discordance']['estimate']-1)<1e-15)
    check('kappa hand arithmetic',Fraction(r['kappa']['exact'])==Fraction(1035,1528))
    check('kappa source rounds',round(r['kappa']['estimate'],2)==d['printed_kappa'])
    check('source sensitivity within integer percentage rounding precision',abs(r['sensitivity']['estimate']-d['printed_rounded_sensitivity'])<=.01)
    check('source specificity within integer percentage rounding precision',abs(r['specificity']['estimate']-d['printed_rounded_specificity'])<=.01)
    for name in ['sensitivity','specificity','positive_predictive_value','negative_predictive_value','agreement','discordance']:
        s=r[name]; lo,hi=s['wilson_ci95']
        check('interval contains estimate '+name,0<=lo<=s['estimate']<=hi<=1)
    check('Wilson zero endpoint',wilson(0,10)[0]==0)
    check('Wilson complete endpoint',wilson(10,10)[1]==1)
    check('Wilson complement symmetry',all(abs(a-b)<1e-14 for a,b in zip(wilson(3,10),[1-wilson(7,10)[1],1-wilson(7,10)[0]])))
    for k,n in [(-1,2),(3,2),(0,0),(1.0,2)]:
        try: wilson(k,n)
        except ValueError: tests.append('invalid input rejected '+str((k,n)))
        else: raise AssertionError('invalid input accepted')
    return tests

if __name__=='__main__':
    d=json.loads((HERE/'aggregate_inputs.json').read_text())
    r=analyze(d)
    passed=checks(d,r)
    r['verification']={'passed_checks':len(passed),'checks':passed}
    (HERE/'aggregate_checks.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
