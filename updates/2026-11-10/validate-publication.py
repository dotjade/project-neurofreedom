#!/usr/bin/env python3
"""Offline consistency checks; not clinical validation or an exhaustive source review."""
from pathlib import Path
import json,subprocess,datetime
root=Path(__file__).resolve().parents[2]; day=Path(__file__).resolve().parent
feed=json.loads((root/'public/research-feed.json').read_text()); baseline=json.loads(subprocess.check_output(['git','show','095c568b21ba8171867c7324f24548d0ee8617bc:public/research-feed.json'],cwd=root));checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
check('schema preserved',feed['schemaVersion']==baseline['schemaVersion']==1)
check('six unchanged activities',feed['activities']==baseline['activities'] and len(feed['activities'])==6)
check('feedback unchanged disabled',feed['feedback']==baseline['feedback'] and not feed['feedback']['enabled'])
check('dates truthful',feed['lastResearchDate']==feed['activityEditionDate']=='2026-11-10' and feed['updatedAt'][:10]=='2026-11-10')
check('timestamps not future',datetime.datetime.fromisoformat(feed['updatedAt'].replace('Z','+00:00'))<=datetime.datetime.now(datetime.timezone.utc))
check('24 timeline entries',len(feed['timeline'])==24)
check('timeline history preserved',feed['timeline'][1:]==baseline['timeline'][:23])
check('new report exists',(root/'updates/2026-11-10/report.md').exists())
check('ordered dates',all(a['date']>=b['date'] for a,b in zip(feed['timeline'],feed['timeline'][1:])))
check('allowed activity',feed['featuredActivityId'] in {x['id'] for x in baseline['activities']})
check('no em dash','\u2014' not in (root/'public/research-feed.json').read_text())
gates=json.loads((day/'analysis-gates.json').read_text());check('three explicit gates',len(gates['rows'])==3)
for g in gates['rows']:
 check(g['gate']+' prior exists',(root/g['prior_report']).exists())
 check(g['gate']+' inputs explicit',len(g['required_inputs'])>=3)
check('no computation claim','No new literature reanalysis or numerical computation was performed' in (day/'analysis-feasibility.md').read_text())
scan=json.loads((day/'scan/summary.json').read_text());check('49 PubMed',scan['unique_pubmed_records']==49);check('812 preprint versions',sum(x['unique_doi_versions'] for x in scan['preprints'])==812)
for p in day.rglob('*.json'):json.loads(p.read_text())
check('all JSON parses',True)
result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_passed':len(checks),'checks':checks,'scope':'Offline content/accounting checks; not independent source verification or clinical validation.'}
(day/'publication-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
