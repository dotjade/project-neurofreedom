"""Offline integration/preservation checks, not clinical validation."""
import pathlib,json,subprocess,hashlib
R=pathlib.Path(__file__).resolve().parents[2];P=pathlib.Path(__file__).resolve().parent;BASE='c0a9b5b10049b0714e432386d73c1933a6058c93';checks=[]
def check(n,b):
 assert b,n
 checks.append(n)
def base(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R)
f=json.loads((R/'public/research-feed.json').read_text());old=json.loads(base('public/research-feed.json'))
check('schema preserved',f.keys()==old.keys() and f['schemaVersion']==1)
check('six activities identical',f['activities']==old['activities'] and len(f['activities'])==6)
check('approved dated selection',f['featuredActivityId']=='hand-at-ease' and f['activityEditionDate']=='2026-11-04')
check('honest content dates',f['lastResearchDate']=='2026-11-04' and f['updatedAt'].startswith('2026-11-04T'))
check('bounded ordered timeline',len(f['timeline'])==24 and f['timeline'][1:]==old['timeline'][:23])
check('no em dash','\u2014' not in json.dumps(f,ensure_ascii=False))
check('feedback unchanged off',f['feedback']==old['feedback'] and f['feedback']['enabled'] is False)
check('config preserved',(R/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
s=base('STATUS.md').decode().replace('Updated 3 November 2026. Initial portfolio, twenty-six completed daily updates','Updated 4 November 2026. Initial portfolio, twenty-seven completed daily updates',1).replace('Daily runs were completed on 9-31 October and 1-3 November 2026','Daily runs were completed on 9-31 October and 1-4 November 2026',1)
check('earlier status retained',(R/'STATUS.md').read_text().startswith(s))
check('earlier evidence retained',(R/'evidence.jsonl').read_bytes().startswith(base('evidence.jsonl')))
e=[json.loads(x) for x in (R/'evidence.jsonl').read_text().splitlines() if x.strip()]
check('historical source deduplicated',sum(x.get('pmid')=='39681552' for x in e)==1)
a=R/'analyses/network_feasibility/2026-11-04';i=json.loads((a/'inputs.json').read_text());o=json.loads((a/'results.json').read_text())
check('prospective plan fixed',hashlib.sha256((a/'plan.md').read_bytes()).hexdigest()==i['plan_sha256'])
check('metadata gate',i['public'] and i['license']['name']=='CC0 1.0 Universal' and len(i['files'])==4 and i['pagination_next'] is None)
check('three group maps',len(o['maps'])==3 and o['same_header_grid'])
check('no clinical replication',not o['full_published_pipeline_gate_passed'] and not o['spatial_specificity_test_executed'] and not o['clinical_target_validation'])
check('independent numerical pass',json.loads((a/'independent-review.json').read_text())['passed']==55)
check('scan pass',json.loads((P/'scan/validation.json').read_text())['passed']==32)
check('preprint recovery complete',json.loads((P/'scan/summary.json').read_text())['preprint_pagination_complete'])
check('safety pass',json.loads((P/'safety/validation.json').read_text())['passed'])
for root in [P,a]:
 for p in root.rglob('*'):
  if p.suffix=='.json':json.loads(p.read_text());check('valid '+str(p.relative_to(R)),True)
  if p.suffix=='.jsonl':[json.loads(x) for x in p.read_text().splitlines() if x.strip()];check('valid '+str(p.relative_to(R)),True)
check('no paper, maps or archives published',not any(p.suffix in ['.pdf','.nii','.zip','.xlsx'] for root in [P,a] for p in root.rglob('*')))
(P/'integration-validation.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'scope':'Implementation/preservation verification, not clinical validation'},indent=2)+'\n');print(len(checks),'passed')
