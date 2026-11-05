"""Offline checks of provenance, publication safety and preservation; not clinical validation."""
from pathlib import Path
import json,subprocess,hashlib
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
BASE='d5450986a0df8b6c9d29344a6c576ae6bf922a05'; checks=[]
def check(n,b):
 assert b,n
 checks.append(n)
def base(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R)
f=json.loads((R/'public/research-feed.json').read_text());old=json.loads(base('public/research-feed.json'))
check('feed schema unchanged',f.keys()==old.keys() and f['schemaVersion']==1)
check('six safe activities unchanged',f['activities']==old['activities'] and len(f['activities'])==6)
check('honest dates',f['lastResearchDate']=='2026-11-05' and f['updatedAt'].startswith('2026-11-05T') and f['activityEditionDate']=='2026-11-05')
check('approved selection',f['featuredActivityId'] in [a['id'] for a in f['activities']])
check('timeline preserves prior entries',len(f['timeline'])==24 and f['timeline'][1:]==old['timeline'][:23])
check('public copy no em dash','\u2014' not in json.dumps(f,ensure_ascii=False))
check('feedback stays disabled',f['feedback']==old['feedback'] and not f['feedback']['enabled'])
check('collection config unchanged',(R/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
s=base('STATUS.md').decode().replace('Updated 4 November 2026. Initial portfolio, twenty-seven completed daily updates','Updated 5 November 2026. Initial portfolio, twenty-eight completed daily updates',1).replace('Daily runs were completed on 9-31 October and 1-4 November 2026','Daily runs were completed on 9-31 October and 1-5 November 2026',1)
check('earlier status preserved',(R/'STATUS.md').read_text().startswith(s))
check('earlier evidence preserved',(R/'evidence.jsonl').read_bytes().startswith(base('evidence.jsonl')))
for root in [P,R/'analyses/network_provenance/2026-11-05']:
 for p in root.rglob('*'):
  if p.suffix=='.json':json.loads(p.read_text());check('json '+str(p.relative_to(R)),True)
  if p.suffix=='.jsonl':[json.loads(x) for x in p.read_text().splitlines() if x.strip()];check('jsonl '+str(p.relative_to(R)),True)
  check('no papers/maps/archives '+str(p.relative_to(R)),p.suffix not in ['.pdf','.nii','.zip','.xlsx'])
(P/'integration-validation.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'scope':'Implementation checks, not clinical validation'},indent=2)+'\n');print(len(checks),'checks passed')
