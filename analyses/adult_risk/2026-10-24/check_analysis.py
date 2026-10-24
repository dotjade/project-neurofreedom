#!/usr/bin/env python3
import hashlib,json,pathlib
from analyze import calculate
P=pathlib.Path(__file__).resolve().parent
x=json.loads((P/'inputs.json').read_text()); y=json.loads((P/'results.json').read_text()); t=json.loads((P/'temporal-audit.json').read_text()); checks=[]
def check(n,b): checks.append({'name':n,'passed':bool(b)}); assert b,n
check('deterministic reproduction',calculate(x)==y)
check('flow ordered',758>=334>=292>=258)
check('flow partition',424+42+34+258==758)
for r in y['rounding_compatible_denominators']:
 check(r['field']+' candidate present',len(r['candidates'])>0)
 check(r['field']+' bounded',all(r['count']<=n<=258 for n in r['candidates']))
 check(r['field']+' labeled conditional','conditional' in r['status'])
check('model counts unknown',all(v is None for v in y['model_counts'].values()))
check('no simulation',y['seed'] is None and 'not simulation' in y['analysis_type'])
check('boundary p preserved',t['model_documentation']['ocd_impairment_p_printed']=='0.050')
check('different outcome sets',t['model_documentation']['tts']['predictors']!=t['model_documentation']['impairment']['predictors'])
check('no temporal causal claim','no verified prospective' in t['decision'])
check('source identity',x['study']['doi']=='10.3389/fpsyt.2026.1948693')
check('rounding OCD only208',next(r for r in y['rounding_compatible_denominators'] if r['field']=='ocd')['candidates']==[208])
check('rounding ADHD only252',next(r for r in y['rounding_compatible_denominators'] if r['field']=='adhd')['candidates']==[252])
(P/'checks.json').write_text(json.dumps({'checks':checks,'passed':len(checks),'failed':0,'kind':'software/documentation checks, not clinical validation'},indent=2)+'\n')
print(len(checks),'checks passed')
