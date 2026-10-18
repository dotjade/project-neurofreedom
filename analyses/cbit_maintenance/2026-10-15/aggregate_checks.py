#!/usr/bin/env python3
"""Reproduce published-count estimand audit. Standard library; no patient data."""
import argparse
from fractions import Fraction
import hashlib
import json
from math import ceil
from pathlib import Path

def rational(x):
    return {"fraction": f"{x.numerator}/{x.denominator}", "proportion": float(x), "percent": float(100*x)}

def bounds(A,O,R):
    if not all(type(x) is int for x in (A,O,R)) or not 0 <= R <= O <= A or A <= 0:
        raise ValueError("Require integer 0 <= positive <= assessed <= eligible and eligible > 0")
    return Fraction(R,A), Fraction(R+A-O,A)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default=str(Path(__file__).with_name('aggregate_inputs.json')));ap.add_argument('--output',default=str(Path(__file__).with_name('aggregate_checks.json')));a=ap.parse_args()
    path=Path(a.input);data=json.loads(path.read_text());checks=[]
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    rows=[]
    for arm,d in data['arms'].items():
        A=d['acute_responders'];N=d['randomized']
        check(arm+'_acute_partition', d['acute_completed']+d['acute_exited']==N)
        check(arm+'_analysis_order',0<A<=d['acute_completed']<=d['acute_analyzed']<=N)
        for f in d['followup']:
            O=f['assessed'];R=f['positive'];M=A-O;lo,hi=bounds(A,O,R)
            scenarios=[{'hypothetical_missing_positive':m,**rational(Fraction(R+m,A))} for m in range(M+1)]
            stem=arm+'_'+str(f['months_after_acute'])+'m'
            check(stem+'_enumerated_endpoints',scenarios[0]['fraction']==rational(lo)['fraction'] and scenarios[-1]['fraction']==rational(hi)['fraction'])
            check(stem+'_bound_width',hi-lo==Fraction(M,A))
            check(stem+'_monotone',all(scenarios[i]['proportion']<scenarios[i+1]['proportion'] for i in range(M)))
            check(stem+'_observed_inside_bounds',lo<=Fraction(R,O)<=hi)
            rows.append({'arm':arm,'months_after_acute':f['months_after_acute'],'eligible_acute_responders':A,'assessed':O,'positive':R,'unknown':M,'ascertainment':rational(Fraction(O,A)),'available_case_positive':rational(Fraction(R,O)),'documented_positive_among_acute_responders':rational(lo),'acute_responder_identification_bounds':{'lower':rational(lo),'upper':rational(hi)},'documented_acute_and_later_positive_among_randomized':rational(Fraction(R,N)),'missing_outcome_scenarios':scenarios})
    check('CBIT_3m_manual',bounds(24,15,13)==(Fraction(13,24),Fraction(11,12)))
    check('CBIT_6m_manual',bounds(24,15,12)==(Fraction(1,2),Fraction(7,8)))
    check('PST_manual',bounds(4,2,1)==(Fraction(1,4),Fraction(3,4)))
    check('no_missing_edge',bounds(10,10,7)==(Fraction(7,10),Fraction(7,10)))
    check('all_missing_edge',bounds(10,0,0)==(Fraction(0),Fraction(1)))
    check('zero_positive_edge',bounds(10,5,0)==(Fraction(0),Fraction(1,2)))
    for args in [(0,0,0),(5,6,1),(5,2,3),(5,2,-1),(5.0,2,1)]:
        raised=False
        try:bounds(*args)
        except ValueError:raised=True
        check('invalid_'+repr(args),raised)
    check('randomized_total',sum(d['randomized'] for d in data['arms'].values())==122)
    check('analyzed_total',sum(d['acute_analyzed'] for d in data['arms'].values())==113)
    check('completed_total',sum(d['acute_completed'] for d in data['arms'].values())==105)
    benchmark=Fraction(4,5);needed=min(m for m in range(10) if Fraction(12+m,24)>=benchmark)
    check('80pct_sensitivity',needed==8 and Fraction(19,24)<benchmark<=Fraction(20,24))
    rd=Fraction(24,63)-Fraction(4,59);inv=1/rd
    check('acute_RD_manual',rd==Fraction(388,1239))
    check('NNT_discrepancy',ceil(inv)==4 and ceil(inv)!=data['source_nnt_printed'])
    result={'method':'Deterministic finite-cohort missing-outcome enumeration; no MAR assumption or confidence interval','source':data['study'],'rows':rows,'CBIT_6m_80pct_benchmark':{'minimum_missing_positive':needed,'missing_count':9,'rate_at_minimum':rational(Fraction(12+needed,24)),'interpretation':'Arithmetic benchmark only; missing outcomes remain unknown'},'acute_source_arithmetic':{'CBIT_response':rational(Fraction(24,63)),'PST_response':rational(Fraction(4,59)),'unadjusted_risk_difference':rational(rd),'reciprocal_risk_difference':float(inv),'ceil_reciprocal':ceil(inv),'reported_NNT':data['source_nnt_printed'],'interpretation':'Reported NNT not reproduced by simple reciprocal of displayed response fractions; no unpublished model or corrected source value inferred'},'tests':{'passed':len(checks),'names':checks},'sha256':{'input':hashlib.sha256(path.read_bytes()).hexdigest(),'code':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'limitations':['Response-conditioned follow-up is not an all-randomized treatment contrast.','Unknown outcomes are varied, not imputed as observed failures.','No continuous remission or joint visit response is identified.','No adult-only, off-treatment, quality-of-life or disease-modification estimate.','No sampling confidence intervals or model-based efficacy recalculation.']}
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'tests_passed':len(checks),'output':str(Path(a.output)),'sha256':result['sha256']},indent=2))
if __name__=='__main__':main()
