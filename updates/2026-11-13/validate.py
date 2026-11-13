#!/usr/bin/env python3
"""Reproduce edition consistency checks; not clinical or independent source validation."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,re,subprocess
r=Path(__file__).resolve().parents[2];p=Path(__file__).resolve().parent
B='df5cc768a484a85096c78c5c4ce4b0fc187bbc66'
def old(x):return subprocess.check_output(['git','show',f'{B}:{x}'],cwd=r)
f=json.loads((r/'public/research-feed.json').read_text());b=json.loads(old('public/research-feed.json'));cs={}
def ck(n,v):
 assert v,n
 cs[n]=True
ck('schema retained',f['schemaVersion']==b['schemaVersion']==1)
ck('six activities unchanged',f['activities']==b['activities'] and len(f['activities'])==6)
ck('collection unchanged and off',f['feedback']==b['feedback'] and not f['feedback']['enabled'])
ck('dates',f['lastResearchDate']==f['activityEditionDate']=='2026-11-13')
ck('honest write timestamp',f['updatedAt'][:10]=='2026-11-13' and datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.now(timezone.utc))
ck('24 entries preserved order',len(f['timeline'])==24 and f['timeline'][1:]==b['timeline'][:23])
ck('sorted',all(x['date']>=y['date'] for x,y in zip(f['timeline'],f['timeline'][1:])))
ck('new report link',f['timeline'][0]['record'].endswith('/updates/2026-11-13/report.md'))
ck('safe selection',f['featuredActivityId']=='music-or-silence')
ck('no public em dash','\u2014' not in (r/'public/research-feed.json').read_text())
ck('size limit',(r/'public/research-feed.json').stat().st_size<64000)
for a,z in zip(b['findings'],f['findings']):
 ck('finding preserved '+a['title'],{k:v for k,v in a.items() if k not in ['checkedAt','linkState']}=={k:v for k,v in z.items() if k not in ['checkedAt','linkState']} and z['checkedAt']=='2026-11-13')
ck('finding count preserved',len(f['findings'])==len(b['findings']))
for x in ['public/journal-source/worker.js','public/journal-source/journal.js','public/journal-source/index.html','public/journal-source/feedback-config.json']:
 ck('runtime unchanged '+x,(r/x).read_bytes()==old(x))
be=old('evidence.jsonl');ne=(r/'evidence.jsonl').read_bytes()
ck('prior evidence bytes preserved',ne.startswith(be))
records=[json.loads(x) for x in ne.decode().splitlines() if x.strip()]
ck('evidence IDs unique',len({x['id'] for x in records})==len(records))
ck('new comparison present',(r/'analyses/measurement_comparability/2026-11-13/report.md').is_file())
ck('scan report present',(p/'scan/report.md').is_file())
ck('link checks present',(r/'public/link-checks/2026-11-13.json').is_file())
for folder in [p,r/'analyses/measurement_comparability/2026-11-13']:
 for x in folder.rglob('*'):
  if not x.is_file():continue
  if x.suffix=='.json':json.loads(x.read_text())
  if x.suffix=='.py':ast.parse(x.read_text())
ck('JSON and Python valid',True)
for x in [p/'report.md',r/'analyses/measurement_comparability/2026-11-13/report.md']:
 for rel in re.findall(r'\]\(([^)]+)\)',x.read_text()):
  if rel.startswith(('https://','http://','#')):continue
  ck('relative link '+str(x.relative_to(r))+' '+rel,(x.parent/rel).exists())
result={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks_passed':len(cs),'checks':cs,'scope':'Offline preservation, consistency, dates, syntax and local link checks; independent sources, remote, CI and live verification separate.'}
(p/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
