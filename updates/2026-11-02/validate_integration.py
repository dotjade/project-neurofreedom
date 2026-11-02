"""Offline artifact/safety checks, not scientific validation."""
import json, pathlib, subprocess, hashlib
R=pathlib.Path(__file__).resolve().parents[2]; P=pathlib.Path(__file__).resolve().parent
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def base(path):return subprocess.check_output(['git','show','866c82c09c838fffdabea719dc5f44edb133eea2:'+path],cwd=R)
f=json.loads((R/'public/research-feed.json').read_text()); old=json.loads(base('public/research-feed.json'))
check('same feed schema',f.keys()==old.keys() and f['schemaVersion']==1)
check('same six catalog activities',f['activities']==old['activities'] and len(f['activities'])==6)
check('approved daily selection',f['featuredActivityId']=='hand-at-ease' and f['activityEditionDate']=='2026-11-02')
check('dated research',f['lastResearchDate']=='2026-11-02' and f['updatedAt'].startswith('2026-11-02T'))
check('timeline size',len(f['timeline'])==24)
check('timeline order',[x['date']for x in f['timeline']]==sorted([x['date']for x in f['timeline']],reverse=True))
check('prior timeline preserved',f['timeline'][1:]==old['timeline'][:23])
check('no em dash','\u2014'not in json.dumps(f,ensure_ascii=False))
check('no new activities set',set(x['id']for x in f['activities'])==set(x['id']for x in old['activities']))
check('feedback source unchanged',(R/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
s=base('STATUS.md').decode().replace('Updated 1 November 2026. Initial portfolio, twenty-four completed daily updates','Updated 2 November 2026. Initial portfolio, twenty-five completed daily updates',1).replace('Daily runs were completed on 9-31 October and 1 November 2026','Daily runs were completed on 9-31 October and 1-2 November 2026',1)
check('complete prior status retained',(R/'STATUS.md').read_text().startswith(s))
check('single new status section',(R/'STATUS.md').read_text().count('## Completed daily research update - 2 November 2026')==1)
records=[json.loads(x)for x in(R/'evidence.jsonl').read_text().splitlines()if x.strip()]; before=[json.loads(x)for x in base('evidence.jsonl').decode().splitlines()if x.strip()]
check('one historical source added',len(records)==len(before)+1)
for a,b in zip(before,records):
 if a.get('pmid')=='36878177':b=dict(b);b.pop('documentation_audit_2026_11_02')
 check('prior evidence '+str(a['id']),a==b)
a=R/'analyses/canna_documentation/2026-11-02'; x=json.loads((a/'extraction.json').read_text()); review=json.loads((a/'review/identity.json').read_text())
check('plan hash',hashlib.sha256((a/'plan.md').read_bytes()).hexdigest()==x['plan_sha256'])
check('independent identity hash',x['sources'][4]['sha256']==review['sha256'])
check('identity exclusion',x['sources'][4]['type'].startswith('mismatched'))
check('no source files',not list(a.rglob('*.pdf')) and not list(a.rglob('*.png')))
check('scan checks',json.loads((P/'scan/validation.json').read_text())['passed']==32)
check('safety checks',json.loads((P/'safety/validation.json').read_text())['passed'])
result={'passed':len(checks),'checks':checks,'scope':'Offline consistency/source-preservation checks, not clinical validation'}
(P/'integration-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'checks passed')
