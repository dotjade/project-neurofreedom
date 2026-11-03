"""Offline preservation, schema and analysis checks, not clinical validation."""
import json,pathlib,subprocess,hashlib
R=pathlib.Path(__file__).resolve().parents[2];P=pathlib.Path(__file__).resolve().parent
BASE='5cc598196428261bc4c289f94cc7929af55c0bf0';checks=[]
def check(n,b):
 assert b,n
 checks.append(n)
def base(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R)
f=json.loads((R/'public/research-feed.json').read_text());old=json.loads(base('public/research-feed.json'))
check('schema preserved',f.keys()==old.keys() and f['schemaVersion']==1)
check('six activities identical',f['activities']==old['activities'] and len(f['activities'])==6)
check('approved selection',f['featuredActivityId']=='familiar-route' and f['activityEditionDate']=='2026-11-03')
check('actual research dates',f['lastResearchDate']=='2026-11-03' and f['updatedAt'].startswith('2026-11-03T'))
check('timeline bound/order',len(f['timeline'])==24 and [x['date'] for x in f['timeline']]==sorted([x['date'] for x in f['timeline']],reverse=True))
check('old timeline preserved',f['timeline'][1:]==old['timeline'][:23])
check('no em dash','\u2014' not in json.dumps(f,ensure_ascii=False))
check('feedback unchanged off',f['feedback']==old['feedback'] and f['feedback']['enabled'] is False)
check('config unchanged',(R/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
s=base('STATUS.md').decode().replace('Updated 2 November 2026. Initial portfolio, twenty-five completed daily updates','Updated 3 November 2026. Initial portfolio, twenty-six completed daily updates',1).replace('Daily runs were completed on 9-31 October and 1-2 November 2026','Daily runs were completed on 9-31 October and 1-3 November 2026',1)
check('all earlier status retained',(R/'STATUS.md').read_text().startswith(s))
check('old evidence unchanged',(R/'evidence.jsonl').read_bytes().startswith(base('evidence.jsonl')))
e=[json.loads(l) for l in(R/'evidence.jsonl').read_text().splitlines() if l.strip()];b=[json.loads(l) for l in base('evidence.jsonl').decode().splitlines() if l.strip()]
check('one deduplicated historical source',len(e)==len(b)+1 and sum(x.get('pmid')=='38265476' for x in e)==1)
a=R/'analyses/canna_driving/2026-11-03';x=json.loads((a/'inputs.json').read_text());out=json.loads((a/'results.json').read_text())
check('prospective plan hash',hashlib.sha256((a/'plan.md').read_bytes()).hexdigest()==x['plan_sha256'])
check('no fabricated missingness bounds',out['missingness_bounds_executed'] is False)
check('failed upstream gate',out['primary_gate_passed'] is False)
check('no clinical validation',out['confirmatory_noninferiority_established_under_published_hierarchy'] is False)
check('scan consistency',json.loads((P/'scan/validation.json').read_text())['passed']==32)
check('safety pass',json.loads((P/'safety/validation.json').read_text())['passed'] is True)
for root in [a,P]:
 for p in root.rglob('*'):
  if p.suffix in ['.json','.jsonl']:
   if p.suffix=='.json':json.loads(p.read_text())
   else:[json.loads(l) for l in p.read_text().splitlines() if l.strip()]
   check('valid '+str(p.relative_to(R)),True)
check('no full text or images',not any(p.suffix in ['.pdf','.png','.jpg'] for root in [a,P] for p in root.rglob('*')))
r={'passed':len(checks),'checks':checks,'scope':'Offline implementation and preservation checks, not clinical validation'}
(P/'integration-validation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
