"""Local integration assertions. No network requests or participant data."""
from pathlib import Path
import datetime, hashlib, json, subprocess
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
def base(path):return subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT)
f=json.loads((ROOT/'public/research-feed.json').read_text()); b=json.loads(base('public/research-feed.json'))
check('catalog exactly preserved',f['activities']==b['activities'])
check('feedback exactly preserved and disabled',f['feedback']==b['feedback'] and not f['feedback']['enabled'])
check('research date',f['lastResearchDate']=='2026-10-31')
check('activity date',f['activityEditionDate']=='2026-10-31')
check('approved feature',f['featuredActivityId']=='small-silly-mark' and any(a['id']==f['featuredActivityId'] for a in f['activities']))
check('timeline bounded and dated',len(f['timeline'])<=24 and f['timeline'][0]['date']=='2026-10-31')
check('retained timeline exactly preserved',f['timeline'][1:]==b['timeline'][:23])
check('public copy no em dash','\u2014' not in (ROOT/'public/research-feed.json').read_text())
check('true nonfuture content write timestamp',datetime.datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.datetime.now(datetime.timezone.utc))
old=base('evidence.jsonl'); new=(ROOT/'evidence.jsonl').read_bytes()
check('existing evidence bytes preserved',new.startswith(old))
records=[json.loads(l) for l in new.decode().splitlines() if l.strip()]
check('evidence ids unique',len({r['id'] for r in records})==len(records))
check('model evidence one record',sum(r.get('pmid')=='40531356' for r in records)==1)
check('histamine evidence one record',sum(r.get('pmid')=='42956657' for r in records)==1)
check('exactly two primary additions',len(new.splitlines())-len(old.splitlines())==2)
for folder in ['updates/2026-10-31','analyses/force_matching/2026-10-31']:
    for p in (ROOT/folder).rglob('*.json'):json.loads(p.read_text())
check('all authored JSON parses',True)
check('synthetic assertions',json.loads((ROOT/'analyses/force_matching/2026-10-31/synthetic-results.json').read_text())['checks_passed']==30)
for field in ['record']:
    for e in f['timeline']:
        url=e[field]; prefix='https://github.com/dotjade/project-neurofreedom/blob/main/'
        if url.startswith(prefix):check('timeline path exists '+url[len(prefix):],(ROOT/url[len(prefix):]).is_file())
check('feedback static unchanged', (ROOT/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
result={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checksPassed':len(checks),'checks':checks,'scope':'Source, feed and artifact integration only; not clinical, rendered or publication verification.'}
(ROOT/'updates/2026-10-31/integration-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'{len(checks)} integration assertions passed')
