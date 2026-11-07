"""Offline source/provenance and publication checks, not clinical validation."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = 'fbe540dd2552c07526418b407b1383be0a06a91b'
DATE = '2026-11-07'
checks = []


def check(name, value):
    assert value, name
    checks.append(name)


def base(path):
    return subprocess.check_output(['git', 'show', BASE + ':' + path], cwd=ROOT)


feed_bytes = (ROOT / 'public/research-feed.json').read_bytes()
feed = json.loads(feed_bytes)
old = json.loads(base('public/research-feed.json'))
check('schema and top-level keys preserved', feed.keys() == old.keys() and feed['schemaVersion'] == 1)
check('feed stays below transport limit', len(feed_bytes) < 64000)
check('six safe activities unchanged', feed['activities'] == old['activities'] and len(feed['activities']) == 6)
check('honest research and selection dates', feed['lastResearchDate'] == DATE and feed['activityEditionDate'] == DATE and feed['updatedAt'].startswith(DATE + 'T'))
check('write timestamp is not in future', datetime.fromisoformat(feed['updatedAt'].replace('Z', '+00:00')) <= datetime.now(timezone.utc))
check('approved activity selected', feed['featuredActivityId'] in [x['id'] for x in feed['activities']])
check('timeline preserves prior 23 entries', len(feed['timeline']) == 24 and feed['timeline'][1:] == old['timeline'][:23])
check('timeline dates ordered', [x['date'] for x in feed['timeline']] == sorted([x['date'] for x in feed['timeline']], reverse=True))
check('new research record exists', (ROOT / feed['timeline'][0]['record'].split('/blob/main/', 1)[1]).is_file())
check('no em dash in public feed copy', '\u2014' not in feed_bytes.decode())
check('collection and feedback unchanged', feed['feedback'] == old['feedback'] and not feed['feedback']['enabled'])
check('collection configuration unchanged', (ROOT / 'public/journal-source/feedback-config.json').read_bytes() == base('public/journal-source/feedback-config.json'))
check('finding source identities and claims preserved', [{k: v for k, v in x.items() if k not in ('checkedAt', 'linkState')} for x in feed['findings']] == [{k: v for k, v in x.items() if k not in ('checkedAt', 'linkState')} for x in old['findings']])
check('finding check dates current', all(x['checkedAt'] == DATE for x in feed['findings']))
status = base('STATUS.md').decode().replace('Updated 6 November 2026. Initial portfolio, twenty-nine completed daily updates', 'Updated 7 November 2026. Initial portfolio, thirty completed daily updates', 1).replace('Daily runs were completed on 9-31 October and 1-6 November 2026', 'Daily runs were completed on 9-31 October and 1-7 November 2026', 1)
check('earlier status retained', (ROOT / 'STATUS.md').read_text().startswith(status))
check('earlier evidence retained', (ROOT / 'evidence.jsonl').read_bytes().startswith(base('evidence.jsonl')))
changed = subprocess.check_output(['git', 'diff', '--name-only', BASE], cwd=ROOT).decode().splitlines()
check('no unrelated tracked changes', all(p in {'STATUS.md', 'evidence.jsonl', 'public/research-feed.json', 'public/link-checks/2026-11-07.json'} or p.startswith('updates/2026-11-07/') or p.startswith('analyses/h18_mechanism/2026-11-07/') for p in changed))
paths = [HERE, ROOT / 'analyses/h18_mechanism/2026-11-07']
for root in paths:
    for path in sorted(root.rglob('*')):
        if not path.is_file() or path.name in {'integration-validation.json', 'integration-manifest.json', 'publication-verification.json'}:
            continue
        relative = str(path.relative_to(ROOT))
        check('no paper/participant binaries: ' + relative, path.suffix.lower() not in {'.pdf', '.nii', '.gz', '.zip', '.xlsx', '.png', '.jpg', '.mp4'})
        if path.suffix == '.json':
            json.loads(path.read_text())
            check('valid JSON: ' + relative, True)
        if path.suffix == '.jsonl':
            [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
            check('valid JSONL: ' + relative, True)
check('link ledger records actual check day', json.loads((ROOT / 'public/link-checks/2026-11-07.json').read_text())['date'] == DATE)
result = {'passed': len(checks), 'checks': checks, 'scope': 'Source implementation and preservation checks, not clinical validation or rendered accessibility testing.'}
(HERE / 'integration-validation.json').write_text(json.dumps(result, indent=2) + '\n')
print(len(checks), 'checks passed')
