#!/usr/bin/env python3
"""Offline publication consistency, not source verification or clinical validation."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import subprocess

root = Path(__file__).resolve().parents[2]
day = Path(__file__).resolve().parent
baseline_commit = 'f6391480c4ac6249e8a9efc03ceb792e604f6299'
def prior(path):
    return subprocess.check_output(['git', 'show', f'{baseline_commit}:{path}'], cwd=root)
feed = json.loads((root / 'public/research-feed.json').read_text())
baseline = json.loads(prior('public/research-feed.json'))
checks = []
def check(name, value):
    assert value, name
    checks.append(name)

check('schema one', feed['schemaVersion'] == baseline['schemaVersion'] == 1)
check('six unchanged activities', feed['activities'] == baseline['activities'] and len(feed['activities']) == 6)
check('feedback unchanged and off', feed['feedback'] == baseline['feedback'] and not feed['feedback']['enabled'])
check('dated edition', feed['lastResearchDate'] == feed['activityEditionDate'] == '2026-11-11')
check('honest timestamp', feed['updatedAt'][:10] == '2026-11-11' and dt.datetime.fromisoformat(feed['updatedAt'].replace('Z', '+00:00')) <= dt.datetime.now(dt.timezone.utc))
check('24 timeline entries', len(feed['timeline']) == 24)
check('history preserved', feed['timeline'][1:] == baseline['timeline'][:23])
check('timeline ordered', all(a['date'] >= b['date'] for a, b in zip(feed['timeline'], feed['timeline'][1:])))
check('new report target', feed['timeline'][0]['record'] == 'https://github.com/dotjade/project-neurofreedom/blob/main/updates/2026-11-11/report.md')
check('selected approved activity', feed['featuredActivityId'] == 'familiar-route')
check('no em dash in public feed', '\u2014' not in (root / 'public/research-feed.json').read_text())
for old, new in zip(baseline['findings'], feed['findings']):
    check('finding claims preserved: ' + old['title'], {k: v for k, v in old.items() if k not in ['checkedAt', 'linkState']} == {k: v for k, v in new.items() if k not in ['checkedAt', 'linkState']})
    check('finding link checked: ' + old['title'], new['checkedAt'] == '2026-11-11')
check('empirical evidence unchanged', (root / 'evidence.jsonl').read_bytes() == prior('evidence.jsonl'))
check('source configuration unchanged', (root / 'public/journal-source/feedback-config.json').read_bytes() == prior('public/journal-source/feedback-config.json'))
gates = json.loads((day / 'analysis-gates.json').read_text())
check('three reopening branches', len(gates['rows']) == 3)
for row in gates['rows']:
    check('prior source exists: ' + row['gate'], (root / row['prior_report']).is_file())
    check('exact prerequisites: ' + row['gate'], len(row['required_inputs']) >= 3)
    check('no branch reopened: ' + row['gate'], row['reopened'] is False)
check('no invented computation', 'No new literature reanalysis or numerical computation was performed.' in (day / 'analysis-feasibility.md').read_text())
check('bounded scan present', (day / 'scan/report.md').is_file() and (day / 'scan/summary.json').is_file())
scan = json.loads((day / 'scan/summary.json').read_text())
pubmed = [json.loads(line) for line in (day / 'scan/pubmed-screening.jsonl').read_text().splitlines() if line.strip()]
check('PubMed unique count reconciles', len({row['pmid'] for row in pubmed}) == len(pubmed) == scan['unique_pubmed_records'] == 25)
check('no qualifying new primary result', scan['qualifying_new_primary_studies'] == 0 and scan['qualifying_relevant_preprints'] == 0 and scan['new_posted_registry_results'] == 0)
for preprint in scan['preprints']:
    pattern = re.compile(preprint['screen_regex'], re.IGNORECASE)
    check('lexical positive/negative controls: ' + preprint['server'], bool(pattern.search('Tourette syndrome')) and bool(pattern.search('chronic motor tics')) and not bool(pattern.search('statistics')))
    index = (day / 'scan' / (preprint['server'] + '-preprint-index.tsv')).read_text().splitlines()
    check('preprint index reconciles: ' + preprint['server'], len(index) - 1 == preprint['unique_doi_versions'])
check('721 DOI/version records', sum(item['unique_doi_versions'] for item in scan['preprints']) == 721)
check('one administrative registry change', [key for key, value in scan['registry_changes'].items() if value] == ['NCT07137442'])
for path in day.rglob('*.json'):
    json.loads(path.read_text())
check('all daily JSON parses', True)
for filename in ['analysis-plan.md', 'analysis-feasibility.md', 'report.md', 'public-review.md']:
    check('nonempty ' + filename, (day / filename).stat().st_size > 100)
result = {
    'checked_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'checks_passed': len(checks), 'checks': checks,
    'scope': 'Offline content/preservation checks, not independent source verification or clinical validation.'
}
(day / 'publication-checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
