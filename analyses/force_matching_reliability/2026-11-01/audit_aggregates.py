#!/usr/bin/env python3
"""Published aggregate arithmetic, not simulation or participant reanalysis."""
import json, math
from pathlib import Path
P=Path(__file__).resolve().parent
x=json.loads((P/'aggregate-inputs.json').read_text())
checks=0
def check(v):
 global checks
 assert v
 checks+=1
m=x['table4_mean_error_N']; windows=[]
for i,w in enumerate(x['windows_s']):
 d=sum(r[i] for r in m['direct'])/4;s=sum(r[i] for r in m['slider'])/4
 windows.append({'window_s':w,'direct_error_N':d,'slider_error_N':s,'direct_minus_slider_N':d-s})
a,b=windows[2:]
delta=b['direct_minus_slider_N']-a['direct_minus_slider_N']
check(math.isclose(a['direct_minus_slider_N'],.8925));check(math.isclose(b['direct_minus_slider_N'],.7725));check(math.isclose(delta,-.12))
per_force=[]
for f,d,s in zip(x['force_N'],m['direct'],m['slider']):
 e=d[2]-s[2];l=d[3]-s[3]
 per_force.append({'target_N':f,'earlier_contrast_N':e,'later_contrast_N':l,'change_N':l-e})
 check(l<e);check(s[3]>s[2]);check(d[3]<d[2])
check(math.isclose(sum(r['change_N'] for r in per_force)/4,delta))
reliability=[]
for c,rs in x['split_half_spearman_brown'].items():
 check(all(0<r<1 for r in rs));check(all(a<b for a,b in zip(rs,rs[1:])))
 reliability.append({'condition':c,'eight_minus_two_replications_coefficient':rs[-1]-rs[0],'scope':'same-session split-half; not retest or contrast reliability'})
rep=x['table2_two_and_eight_replication_means_N'];rep_results={}
for n in [2,8]:rep_results[str(n)]=sum(rep[f'direct_{n}'])/4-sum(rep[f'slider_{n}'])/4
check(math.isclose(rep_results['2'],.755));check(math.isclose(rep_results['8'],.7625))
check(abs(rep_results['2']-rep_results['8'])<.01)
out={'analysis_type':'deterministic arithmetic of rounded published aggregate means; not simulation','random_seed':None,'n':x['n'],'equal_force_window_estimates':windows,'per_force_last_window_change':per_force,'later_minus_earlier_contrast_N':delta,'relative_change_percent':100*delta/a['direct_minus_slider_N'],'decomposition_N':{'direct_change':b['direct_error_N']-a['direct_error_N'],'slider_change':b['slider_error_N']-a['slider_error_N']},'rounded_input_worst_case_bound_for_change_N':.02,'table2_equal_force_contrast_N':rep_results,'split_half_change':reliability,'confidence_interval':None,'uncertainty_reason':'Rounded aggregate inputs; within-participant cross-condition and cross-window covariances unavailable. No new significance/equivalence claim.','checks_passed':checks}
(P/'aggregate-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
