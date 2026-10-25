#!/usr/bin/env python3
"""Deterministic published-aggregate audit, not simulation or participant reanalysis."""
import json,pathlib
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
x=json.loads((P/'inputs.json').read_text());N=x['sample']['total'];a=x['model_counts']['impairment'];b=x['model_counts']['tic_severity']
out={'analysis_type':'Deterministic arithmetic on published aggregates, not a simulation','seed':None,'seed_reason':'No random sampling','model_coverage':{k:{'analyzed':n,'not_in_model':N-n,'fraction_of_total':n/N} for k,n in x['model_counts'].items()},'model_overlap_bounds':{'minimum':max(0,a+b-N),'maximum':min(a,b),'assumption':'Both reported model samples are subsets of the same 535-person cohort. Bounds are mathematical, not observed overlap.'},'comparisons':{},'adult_specific_estimate_identified':False,'measurement_mechanism_test_identified':False}
for k,u in x['unadjusted'].items():
 d=float(Decimal(str(u['asd_mean']))-Decimal(str(u['non_asd_mean'])))
 out['comparisons'][k]={'unadjusted_asd_minus_non_asd':d,'unadjusted_p':u['p'],'adjusted_asd_coefficient':x['adjusted'][k]['beta'],'adjusted_ci':x['adjusted'][k]['ci'],'adjusted_p':x['adjusted'][k]['p'],'adjusted_ci_contains_zero':x['adjusted'][k]['ci'][0]<=0<=x['adjusted'][k]['ci'][1],'difference_between_coefficients_not_causal_decomposition':True}
out['support_level3_fraction_of_asd']=x['sample']['support_level_counts'][2]/x['sample']['asd']
(P/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
