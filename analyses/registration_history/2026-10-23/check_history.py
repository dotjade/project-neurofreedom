#!/usr/bin/env python3
"""Deterministic documentation checks, no patient data or clinical estimates."""
import json,hashlib
from pathlib import Path
root=Path(__file__).parent
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    assert value,name
versions={n:json.loads((root/f'version-{n}-metadata.json').read_text()) for n in [1,7,8,13,23,24,25]}
def sec(n,name): return next(s['text'] for s in versions[n]['sections'] if s['heading']==name)
for n,v in versions.items():
    check(f'version_{n}_identity',v['version']==n and f'&a={n}#' in v['url'])
    check(f'version_{n}_only_metadata',len(v['sections'])==4 and {s['heading'] for s in v['sections']}=={'Study Status','Study Design','Outcome Measures','Document Section'})
    check(f'version_{n}_no_result_rows',all(x not in json.dumps(v['sections']) for x in ['Overall Number of Participants Analyzed','Statistical Analysis 1','Name Simone','measurements','categories']))
history=versions[1]['history']
check('history_index_has_25_versions',len(history)==25)
check('outcome_change_index_only_version25',[i+1 for i,r in enumerate(history) if 'Outcome Measures' in r['text']]==[25])
for n in [7,8,13,23,24]: check(f'outcomes_v{n}_equal_v1',sec(n,'Outcome Measures')==sec(1,'Outcome Measures'))
check('v1_four_primary_windows',sec(1,'Outcome Measures').count('[Time Frame:')==4)
check('v1_no_40_percent', '40%' not in sec(1,'Outcome Measures'))
check('v25_one_primary_window',sec(25,'Outcome Measures').count('[Time Frame:')==1)
check('v25_40_percent_total', '40%' in sec(25,'Outcome Measures') and 'Total Tics' in sec(25,'Outcome Measures'))
check('masking_boundary','Double' in sec(7,'Study Design') and 'None (Open Label)' in sec(8,'Study Design'))
check('enrollment_20_then_10','20 [Estimated]' in sec(13,'Study Design') and '10 [Actual]' in sec(23,'Study Design'))
check('latest_nonrandomized_sequential','Sequential Assignment' in sec(25,'Study Design') and 'Non-Randomized' in sec(25,'Study Design'))
check('first_submission_distinct_from_qc','2014-02-03' in sec(1,'Study Status') and '2014-02-04' in sec(1,'Study Status'))
check('protocol_date_before_upload','2019-09-23' in sec(25,'Document Section') and '2023-10-10 12:40' in sec(25,'Document Section'))
check('old_document_section_empty',sec(24,'Document Section')=='Document Section')
output={'kind':'Offline documentation checks, not clinical hypothesis tests','checks':checks,'passed':len(checks),'seed':None,'simulation':False,'participant_data_analyzed':False,'input_sha256':{f'version-{n}-metadata.json':hashlib.sha256((root/f'version-{n}-metadata.json').read_bytes()).hexdigest() for n in versions}}
(root/'checks.json').write_text(json.dumps(output,indent=2)+'\n'); print(f'{len(checks)} checks passed')
