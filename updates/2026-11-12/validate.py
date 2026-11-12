#!/usr/bin/env python3
"""Offline edition preservation and artifact checks, not clinical/source verification."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,re,subprocess
r=Path(__file__).resolve().parents[2];p=Path(__file__).resolve().parent;B='4894c40b9da2714730fb50d5730bea6e3fc92608'
def old(x):return subprocess.check_output(['git','show',f'{B}:{x}'],cwd=r)
f=json.loads((r/'public/research-feed.json').read_text());b=json.loads(old('public/research-feed.json'));cs={}
def ck(n,v):assert v,n;cs[n]=True
ck('schema',f['schemaVersion']==b['schemaVersion']==1)
ck('activities unchanged',f['activities']==b['activities'] and len(f['activities'])==6)
ck('collection off unchanged',f['feedback']==b['feedback'] and not f['feedback']['enabled'])
ck('dates',f['lastResearchDate']==f['activityEditionDate']=='2026-11-12')
ck('honest timestamp',f['updatedAt'][:10]=='2026-11-12' and datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.now(timezone.utc))
ck('24 entries and history',len(f['timeline'])==24 and f['timeline'][1:]==b['timeline'][:23])
ck('sorted',all(x['date']>=y['date'] for x,y in zip(f['timeline'],f['timeline'][1:])))
ck('daily report link',f['timeline'][0]['record'].endswith('/updates/2026-11-12/report.md'))
ck('approved selection',f['featuredActivityId']=='notice-one-thing')
ck('no em dash','\u2014' not in (r/'public/research-feed.json').read_text())
ck('partial coverage explicit','preprint coverage was partial' in f['timeline'][0]['summary'])
for a,z in zip(b['findings'],f['findings']):
 ck('finding preserved '+a['title'],{k:v for k,v in a.items() if k!='checkedAt'}=={k:v for k,v in z.items() if k!='checkedAt'} and z['checkedAt']=='2026-11-12')
for x in ['evidence.jsonl','public/journal-source/worker.js','public/journal-source/journal.js','public/journal-source/index.html','public/journal-source/feedback-config.json']:
 ck('unchanged '+x,(r/x).read_bytes()==old(x))
l=json.loads((r/'public/link-checks/2026-11-12.json').read_text());ck('48 fresh links',len(l['checks'])==48)
a=r/'analyses/correction_impact/2026-11-12';av=json.loads((a/'validation.json').read_text());ck('11 audit checks',av['all_pass'] and len(av['checks'])==11 and all(av['checks'].values()))
ck('scan report present',(p/'scan/report.md').is_file())
ck('fresh audit review',(a/'review.md').is_file())
ck('recovery disclosure','uncommitted files were lost' in (p/'report.md').read_text())
for folder in [p,a]:
 for x in folder.rglob('*'):
  if not x.is_file():continue
  if x.suffix=='.json':json.loads(x.read_text())
  if x.suffix=='.py':ast.parse(x.read_text())
ck('new JSON and Python valid',True)
for x in [p/'report.md',p/'public-review.md',a/'report.md']:
 for rel in re.findall(r'\]\(([^)]+)\)',x.read_text()):
  if rel.startswith(('https://','http://','#')):continue
  ck('relative link '+str(x.relative_to(r))+' '+rel,(x.parent/rel).exists())
result={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks_passed':len(cs),'checks':cs,'scope':'Offline preservation, dates, syntax and local link checks. Remote, CI and live checks are separate.'}
(p/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
