"""Local integration checks; no network or participant data."""
from pathlib import Path
import json, subprocess
ROOT=Path(__file__).resolve().parents[2]
feed=json.loads((ROOT/'public/research-feed.json').read_text())
base=json.loads(subprocess.check_output(['git','show','HEAD:public/research-feed.json'],cwd=ROOT))
assert feed['activities']==base['activities']
assert feed['feedback']==base['feedback'] and not feed['feedback']['enabled']
assert feed['lastResearchDate']=='2026-10-29'
assert feed['activityEditionDate']=='2026-10-29'
assert feed['featuredActivityId'] in {a['id'] for a in feed['activities']}
assert '\u2014' not in (ROOT/'public/research-feed.json').read_text()
assert len(feed['timeline'])<=24
assert feed['timeline'][0]['date']=='2026-10-29'
records=[json.loads(x) for x in (ROOT/'evidence.jsonl').read_text().splitlines() if x.strip()]
ids=[x['id'] for x in records]; assert len(ids)==len(set(ids))
new=[x for x in records if x.get('pmid')=='42947547'];assert len(new)==1
assert len([x for x in records if x.get('pmid')=='42680906'])==1
for folder in ['updates/2026-10-29','analyses/gene_specificity/2026-10-29']:
 for p in (ROOT/folder).rglob('*.json'):json.loads(p.read_text())
print('Catalog/collection preserved; dates/selection/schema limits valid; study IDs deduplicated; JSON parses.')
