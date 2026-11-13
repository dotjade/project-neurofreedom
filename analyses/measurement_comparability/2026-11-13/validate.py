"""Deterministic aggregate extraction audit, not patient-data reanalysis."""
import json, subprocess
from pathlib import Path
p=Path(__file__).resolve().parent
repo=p.parents[2]
rows=json.loads((p/'evidence-matrix.json').read_text())
assert len({r['id'] for r in rows})==3
assert rows[1]['n']['Minnesota_CBIT_TMS']+rows[1]['n']['TeleCBIT']==69
assert rows[2]['n']['longitudinal_participants']<=rows[2]['n']['participants']
assert rows[2]['n']['longitudinal_visits']<=rows[2]['n']['all_assessments']
assert rows[0]['estimates']['ci95'][0]<0<rows[0]['estimates']['ci95'][1]
# A published beta and SE rounded to two decimals permit this magnitude range.
beta_lo,beta_hi=.225,.235
se_lo,se_hi=.035,.045
ratio_min,ratio_max=beta_lo/se_hi,beta_hi/se_lo
reported=abs(rows[2]['estimates']['time_only_reported_t'])
assert not ratio_min<=reported<=ratio_max
pattern=r'\b40762700\b|\b41180850\b|\b42076920\b|s00787-025-02818-2|CPJ.0000000000200554|10.1002/mds.70342'
r=subprocess.run(['git','grep','-l','-E',pattern,'df5cc76'],cwd=repo,text=True,capture_output=True)
assert r.returncode in [0,1],r.stderr
out={'analysis_type':'deterministic reporting/eligibility audit, not clinical effect estimation','seed':None,'source_count':3,'prior_identifier_matches':r.stdout.splitlines(),'baseline':'df5cc76','rounding_check':{'permitted_abs_beta_div_SE':[ratio_min,ratio_max],'reported_abs_t':reported,'compatible':False},'pooling_permitted':False,'h18_reopened':False}
(p/'validation-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
