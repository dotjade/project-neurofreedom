"""Offline integration checks for the 28 October public research edition."""
import datetime, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path(__file__).resolve().parents[2]
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
f=json.loads((ROOT/'public/research-feed.json').read_text())
b=json.loads(subprocess.check_output(['git','show','7ef323818a2a808a19e367e78ba01533fc9dce58:public/research-feed.json'],cwd=ROOT))
check('schema preserved',f['schemaVersion']==b['schemaVersion']==1)
check('six approved activities unchanged',f['activities']==b['activities'] and len(f['activities'])==6)
check('feedback unchanged and off',f['feedback']==b['feedback'] and f['feedback']['enabled'] is False)
check('new edition date',f['lastResearchDate']==f['activityEditionDate']=='2026-10-28')
check('write timestamp not future',datetime.datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.datetime.now(datetime.timezone.utc))
check('existing timeline preserved',f['timeline'][1:]==b['timeline'])
check('timeline within renderer cap',len(f['timeline'])<=24)
check('new journal links actual report',f['timeline'][0]['record'].endswith('/analyses/informant_agreement/2026-10-28/report.md') and (ROOT/'analyses/informant_agreement/2026-10-28/report.md').exists())
check('no em dash in visible feed',chr(8212) not in json.dumps(f,ensure_ascii=False))
check('approved activity selection',f['featuredActivityId'] in {a['id'] for a in b['activities']})
records=[json.loads(l) for l in (ROOT/'evidence.jsonl').read_text().splitlines() if l.strip()]
for key in ['id','doi','pmid']:
    vals=[str(d[key]).lower() for d in records if d.get(key)]
    check('evidence unique '+key,len(vals)==len(set(vals)))
for directory in ['analyses/informant_agreement/2026-10-28','updates/2026-10-28']:
    for p in (ROOT/directory).rglob('*.json'):json.loads(p.read_text())
check('new JSON parses',True)
for finding in f['findings']:check('finding checked today '+finding['label'],finding['checkedAt']=='2026-10-28')
check('live collection config disabled',json.loads((ROOT/'public/journal-source/feedback-config.json').read_text())==json.loads(subprocess.check_output(['git','show','7ef323818a2a808a19e367e78ba01533fc9dce58:public/journal-source/feedback-config.json'],cwd=ROOT)))
result={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':len(checks),'checks':checks,'feed_sha256':hashlib.sha256((ROOT/'public/research-feed.json').read_bytes()).hexdigest(),'scope':'Offline schema, safety, preservation and evidence identity checks; not clinical validation or production verification.'}
(ROOT/'updates/2026-10-28/integration-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
