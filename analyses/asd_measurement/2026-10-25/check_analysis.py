#!/usr/bin/env python3
import json,pathlib,subprocess,sys,hashlib
P=pathlib.Path(__file__).resolve().parent
x=json.loads((P/'inputs.json').read_text());r=json.loads((P/'results.json').read_text());checks=[]
def ck(name,condition):checks.append({'check':name,'passed':bool(condition)});assert condition,name
ck('cohort partition',x['sample']['asd']+x['sample']['non_asd']==535)
ck('ASD support partition',sum(x['sample']['support_level_counts'])==49)
for k,n in x['model_counts'].items():
 ck(k+' subset',0<n<=535)
 ck(k+' excluded arithmetic',r['model_coverage'][k]['not_in_model']==535-n)
 ck(k+' coverage',r['model_coverage'][k]['fraction_of_total']==n/535)
 c=r['comparisons'][k];lo,hi=x['adjusted'][k]['ci'];ck(k+' interval order',lo<=c['adjusted_asd_coefficient']<=hi)
 ck(k+' source beta',c['adjusted_asd_coefficient']==x['adjusted'][k]['beta'])
 ck(k+' source p',c['adjusted_p']==x['adjusted'][k]['p'])
 ck(k+' no causal decomposition',c['difference_between_coefficients_not_causal_decomposition'])
ck('overlap lower',r['model_overlap_bounds']['minimum']==433)
ck('overlap upper',r['model_overlap_bounds']['maximum']==483)
ck('impairment contrast',r['comparisons']['impairment']['unadjusted_asd_minus_non_asd']==-3.06)
ck('severity contrast',r['comparisons']['tic_severity']['unadjusted_asd_minus_non_asd']==1.84)
ck('severity interval includes zero',r['comparisons']['tic_severity']['adjusted_ci_contains_zero'])
ck('adult count unknown',x['sample']['adult_count'] is None and x['sample']['asd_adult_count'] is None)
ck('not adult estimate',not r['adult_specific_estimate_identified'])
ck('not mechanism validation',not r['measurement_mechanism_test_identified'])
ck('no random seed',r['seed'] is None)
b=(P/'results.json').read_bytes();subprocess.run([sys.executable,str(P/'analyze.py')],check=True,capture_output=True);ck('byte reproducibility',b==(P/'results.json').read_bytes())
for f in ['prediction.md','report.md','source-provenance.json']:ck(f+' present',(P/f).exists())
ck('paper not retained',not json.loads((P/'source-provenance.json').read_text())['paper_body_retained'])
(P/'checks.json').write_text(json.dumps({'passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
