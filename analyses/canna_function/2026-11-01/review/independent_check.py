"""Independent implementation: invert quadratic score inequality, integer cents.
Does not import author's analyze.py. No participant data or RNG.
"""
import json, math, hashlib
from pathlib import Path
B=Path(__file__).resolve().parents[1]
a=json.loads((B/'inputs.json').read_text()); published=json.loads((B/'results.json').read_text())
z=1.959963984540054
checks=[]
def check(label,value):
 checks.append({'check':label,'pass':bool(value)})
 assert value,label
# Solve n*(p_obs-p)^2 <= z^2*p*(1-p) for candidate true p.
def score_interval(x,n):
 p=x/n; A=n+z*z; b=-(2*n*p+z*z); c=n*p*p
 delta=b*b-4*A*c
 return ((-b-math.sqrt(delta))/(2*A),(-b+math.sqrt(delta))/(2*A))
x,y=14,3;n,m=64,33
p,q=x/n,y/m
lp,up=score_interval(x,n);lq,uq=score_interval(y,m)
rd=p-q
newcombe=[rd-math.sqrt((p-lp)**2+(uq-q)**2),rd+math.sqrt((up-p)**2+(q-lq)**2)]
rr=(x*m)/(y*n)
# Variance independently expressed with binomial non-event counts.
v=(n-x)/(n*x)+(m-y)/(m*y)
ratio_ci=[rr*math.exp(-z*math.sqrt(v)),rr*math.exp(z*math.sqrt(v))]
actual=published['primary_unadjusted']
for label,value,target in [('risk difference',rd,actual['risk_difference']),('risk ratio',rr,actual['risk_ratio'])]:
 check(label,abs(value-target)<1e-12)
for i in range(2):
 check('Newcombe bound '+str(i),abs(newcombe[i]-actual['newcombe_wilson_95ci'][i])<1e-12)
 check('RR bound '+str(i),abs(ratio_ci[i]-actual['log_wald_rr_95ci'][i])<1e-12)
nulls=rounding=0
for i,row in enumerate(a['functional_rows']):
 check(row['endpoint']+' interval order',row['ci95_lower']<=row['ci95_upper'])
 nulls+=row['ci95_lower']<=0<=row['ci95_upper']
 # Integer cents represent printed values; max compatible discrepancy 1.5 cents.
 diffc=round(row['arm_lsm_nabiximols']*100)-round(row['arm_lsm_placebo']*100)
 discc=diffc-round(row['reported_contrast']*100)
 compatible=abs(discc)<=1.5;rounding+=compatible
 check(row['endpoint']+' rounding',compatible==published['functional_audit'][i]['compatible_under_two_decimal_rounding'])
 check(row['endpoint']+' subtraction',abs(diffc/100-float(published['functional_audit'][i]['lsm_subtraction']))<1e-12)
check('All five intervals contain zero',nulls==5)
check('Four of five rounding compatible',rounding==4)
check('Source paper CI untouched',a['primary']['paper_ci95']==[-.28,.01])
check('Registry CI untouched',a['primary']['registry_ci95']==[-.2688,.0131])
for i in range(2):
 check('AE proportion '+str(i),abs(a['harms']['any_ae_people'][i]/a['harms']['exposed'][i]-published['ae_descriptive_proportions'][i])<1e-12)
 check('AE discontinuation '+str(i),abs(a['harms']['ae_discontinuations_registry'][i]/a['harms']['exposed'][i]-published['ae_discontinuation_proportions'][i])<1e-12)
r={'method':'Independent score-quadratic inversion, binomial non-event RR variance, integer-cent subtraction; no import of analysis implementation','input_sha256':hashlib.sha256((B/'inputs.json').read_bytes()).hexdigest(),'results_sha256':hashlib.sha256((B/'results.json').read_bytes()).hexdigest(),'independent_estimates':{'rd':rd,'newcombe_ci95':newcombe,'rr':rr,'rr_ci95':ratio_ci},'checks':checks,'passed':len(checks),'failed':0}
(B/'review'/'independent-results.json').write_text(json.dumps(r,indent=2)+'\n')
print(f'{len(checks)} independent checks passed')
