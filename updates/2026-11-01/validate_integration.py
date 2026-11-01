"""Source-only integration checks, not clinical or deployment validation."""
from pathlib import Path
import datetime, json, subprocess
ROOT=Path(__file__).resolve().parents[2]
BASE='de5f1e43230840aa430f66b5c06443df128deff1'
checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
def base(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)
f=json.loads((ROOT/'public/research-feed.json').read_text()); b=json.loads(base('public/research-feed.json'))
check('schema fields preserved',set(f)==set(b) and f['schemaVersion']==1)
check('six catalog activities exactly preserved',len(f['activities'])==6 and f['activities']==b['activities'])
check('feedback exactly preserved and disabled',f['feedback']==b['feedback'] and not f['feedback']['enabled'])
check('research date',f['lastResearchDate']=='2026-11-01')
check('activity date',f['activityEditionDate']=='2026-11-01')
check('approved optional rest feature',f['featuredActivityId']=='rest-or-leave')
check('timeline bounded and dated',len(f['timeline'])<=24 and f['timeline'][0]['date']=='2026-11-01')
check('retained timeline exactly preserved',f['timeline'][1:]==b['timeline'][:23])
check('public copy no em dash','\u2014' not in (ROOT/'public/research-feed.json').read_text())
check('true nonfuture content write timestamp',datetime.datetime.fromisoformat(f['updatedAt'].replace('Z','+00:00'))<=datetime.datetime.now(datetime.timezone.utc))
check('findings retain inclusive source content',all({k:v for k,v in a.items() if k not in ['checkedAt','linkState']}=={k:v for k,v in c.items() if k not in ['checkedAt','linkState']} for a,c in zip(f['findings'],b['findings'])) and len(f['findings'])==len(b['findings']))
old=base('evidence.jsonl'); new=(ROOT/'evidence.jsonl').read_bytes()
check('existing evidence bytes preserved',new.startswith(old))
records=[json.loads(l) for l in new.decode().splitlines() if l.strip()]
check('evidence ids unique',len({r['id'] for r in records})==len(records))
for key in ['pmid','doi']:
    values=[str(r[key]).lower() for r in records if r.get(key)]
    check(key+' identifiers unique',len(set(values))==len(values))
for folder in ['updates/2026-11-01','analyses/force_matching_reliability/2026-11-01']:
    for p in (ROOT/folder).rglob('*.json'):json.loads(p.read_text())
check('all authored JSON parses',True)
for e in f['timeline']:
    url=e['record']; prefix='https://github.com/dotjade/project-neurofreedom/blob/main/'
    if url.startswith(prefix):check('timeline path exists '+url[len(prefix):],(ROOT/url[len(prefix):]).is_file())
check('feedback static unchanged',(ROOT/'public/journal-source/feedback-config.json').read_bytes()==base('public/journal-source/feedback-config.json'))
check('homepage application source unchanged',not subprocess.check_output(['git','diff',BASE,'--','public/journal-source'],cwd=ROOT).strip())
result={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baselineCommit':BASE,'checksPassed':len(checks),'checks':checks,'scope':'Source/feed integration, not clinical evidence, rendered accessibility or publication verification.'}
(ROOT/'updates/2026-11-01/integration-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'{len(checks)} integration assertions passed')
