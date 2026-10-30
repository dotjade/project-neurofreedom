"""Synthetic known-covariance Gaussian contrast; no sampling or fitted clinical model."""
from pathlib import Path
import json, math
P=Path(__file__).resolve().parent

def two_sided_p(z): return math.erfc(abs(z)/math.sqrt(2))
def compute(x):
 d,i=x['direct_difference'],x['indirect_difference']; sd,si=x['direct_standard_error'],x['indirect_standard_error']
 marginal=[{'condition':name,'difference':v,'se':s,'z':v/s,'p_two_sided':two_sided_p(v/s)} for name,v,s in [('direct',d,sd),('indirect',i,si)]]
 rows=[]
 for rho in x['estimate_correlations']:
  assert -1<rho<1
  cov=rho*sd*si; determinant=sd**2*si**2-cov**2
  variance=sd**2+si**2-2*cov;se=math.sqrt(variance);delta=d-i;z=delta/se;p=two_sided_p(z)
  assert determinant>0 and variance>0
  rows.append({'estimate_correlation':rho,'covariance':cov,'covariance_determinant':determinant,'contrast':delta,'contrast_se':se,'z':z,'p_two_sided':p,'ci95':[delta-x['normal_critical_95']*se,delta+x['normal_critical_95']*se],'below_illustrative_alpha':p<x['alpha']})
 return {'label':x['label'],'method':'Analytic Gaussian formulas evaluated numerically under analyst-chosen known covariance, not clinical estimation','seed':None,'marginal_tests_identical_across_scenarios':marginal,'contrast_scenarios':rows,'conclusion':'Marginal results alone do not identify the contrast precision or statistical decision.'}
if __name__=='__main__':
 r=compute(json.loads((P/'inputs.json').read_text()));(P/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
