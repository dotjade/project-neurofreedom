"""Independent source-workbook audit, aggregate gene sets only. No random seed.
Run: python independent_source_checks.py /tmp/nf-aggregate-fig2.xlsx
The source is temporary and not redistributed. Requires openpyxl.
"""
import hashlib,json,sys
from pathlib import Path
from openpyxl import load_workbook
p=Path(sys.argv[1]); w=load_workbook(p,read_only=True,data_only=True)
a=list(w['Fig2d'].values)
o,t,c=[{r[i] for r in a[1:] if r[i]} for i in range(3)]
r=[x for x in list(w['Fig2c'].values)[1:] if isinstance(x[1],(int,float))]
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
check('source set counts',[len(o),len(t),len(c),len(o|t|c)]==[12,10,34,36])
check('both separate analyses',o&t=={'DNAH9','QRICH1','SETD1A'})
check('exclusive classification counts',[len(t-o),len(o-t),len(c-(o|t))]==[7,9,17])
check('outside combined',(o|t)-c=={'CELSR3','WWC1'})
check('numeric q rows excludes trailing dictionary',len(r)==18111)
check('unique gene rows',len({x[0] for x in r})==len(r))
check('all union genes have q',(o|t|c)<={x[0] for x in r})
check('all q within unit interval',all(0<=x[1]<=1 for x in r))
check('all hc flags match',all((x[1]<.1)==bool(x[6]) for x in r))
check('all probable flags match',all((.1<=x[1]<.3 and x[5]>=2)==bool(x[7]) for x in r))
check('hc set matches table',{x[0] for x in r if x[1]<.1}==c)
check('probable numeric q alone overcounts',sum(.1<=x[1]<.3 for x in r)==88 and sum(bool(x[7]) for x in r)==20)
check('two outside combined satisfy probable',all(.1<=x[1]<.3 and x[5]>=2 for x in r if x[0] in {'CELSR3','WWC1'}))
check('hc does not require dnDam2',any(x[0]=='CCDC168' and x[5]==0 and x[6] for x in r))
inputs=json.loads((Path(__file__).resolve().parent.parent/'inputs.json').read_text())['records']
source={x[0]:x for x in r}
for row in inputs:
 g=row['gene']; z=source[g]
 check('input source match '+g,
  [row['hcOCD'],row['hcCTD'],row['hcOCDCTD']]==[g in s for s in [o,t,c]]
  and float(row['combined_q'])==z[1]
  and row['combined_dnDam_count']==z[5]
  and row['published_combined_hc']==z[6]
  and row['published_combined_probable']==z[7])
print(json.dumps({'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks_passed':len(checks),'checks':checks,'source_numeric_q_rows':len(r),'q_band_0_1_to_0_3':88,'probable_with_damaging_count_requirement':20,'intersection_both':sorted(o&t),'ctd_hc_not_ocd_hc':sorted(t-o),'ocd_hc_not_ctd_hc':sorted(o-t),'combined_only_hc':sorted(c-(o|t))},indent=2))
