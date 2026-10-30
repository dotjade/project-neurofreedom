"""Independent high-precision analytic check of a SYNTHETIC Gaussian example.
No observations, sampling, paper parameters or random seed. Requires mpmath.
"""
from pathlib import Path
import json
import mpmath as m
m.mp.dps=60
P=Path(__file__).resolve().parent
result=json.loads((P.parent/'results.json').read_text())
checks=[]
def check(name,ok):
 assert ok,name
 checks.append(name)
def close(name,value,expected):check(name,abs(m.mpf(str(value))-expected)<m.mpf('1e-13'))
# Independent closed form for equal SE .2: var(delta)=.08(1-rho).
a=m.mpf('0.4'); v=m.mpf('.08');critical=m.sqrt(2)*m.erfinv(m.mpf('.95'))
expected=[]
for r in result['contrast_scenarios']:
 rho=m.mpf(str(r['estimate_correlation']));se=m.sqrt(v*(1-rho));z=a/se
 p=2*m.ncdf(-abs(z));low=a-critical*se;high=a+critical*se
 close(f'{rho}:difference',r['contrast'],a)
 close(f'{rho}:se',r['contrast_se'],se)
 close(f'{rho}:z',r['z'],z)
 close(f'{rho}:p',r['p_two_sided'],p)
 close(f'{rho}:ci lower',r['ci95'][0],low)
 close(f'{rho}:ci upper',r['ci95'][1],high)
 # Eigenvalues of equal-variance covariance matrix.
 check(f'{rho}:positive eigenvalues',m.mpf('.04')*(1-rho)>0 and m.mpf('.04')*(1+rho)>0)
 close(f'{rho}:determinant',r['covariance_determinant'],m.mpf('.0016')*(1-rho*rho))
 check(f'{rho}:decision',r['below_illustrative_alpha']==(p<m.mpf('.05')))
 expected.append({'rho':str(rho),'se':str(se),'p':str(p),'ci95':[str(low),str(high)]})
for row,z in zip(result['marginal_tests_identical_across_scenarios'],[m.mpf(3),m.mpf(1)]):
 close(row['condition']+':z',row['z'],z)
 close(row['condition']+':p',row['p_two_sided'],2*m.ncdf(-z))
# Exact model's crossing: rho > 1 - .4^2/(.08*zcrit^2).
threshold=1-a*a/(v*critical*critical)
check('threshold lies between0 and.5',0<threshold<m.mpf('.5'))
check('four illustrative decisions',[x['below_illustrative_alpha'] for x in result['contrast_scenarios']]==[False,False,True,True])
print(json.dumps({'label':'SYNTHETIC METHODS CHECK ONLY','checks_passed':len(checks),'checks':checks,'precision_decimal_digits':60,'absolute_tolerance':'1e-13','seed':None,'independent_formula':'var(delta)=.08(1-rho); high-precision normal CDF; eigenvalue PD check','illustrative_rho_decision_boundary':str(threshold),'oracle':expected},indent=2))
