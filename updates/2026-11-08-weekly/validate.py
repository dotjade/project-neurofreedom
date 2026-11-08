#!/usr/bin/env python3
"""Offline publication checks; not clinical validation. Run from any directory."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlparse
R = Path(__file__).resolve().parents[2]
W = Path(__file__).resolve().parent
checks = []
def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
def sha(data):
    return hashlib.sha256(data).hexdigest()
def git(*args):
    return subprocess.check_output(['git', '-C', str(R), *args])
M = json.loads((W/'source-manifest.json').read_text())
BASE = M['baseline_commit']
for path, digest in M['files'].items():
    check('baseline:'+path, sha(git('show', BASE+':'+path)) == digest)
    if path != 'STATUS.md':
        check('unchanged_source:'+path, sha((R/path).read_bytes()) == digest)
I = json.loads((W/'source-inventory.json').read_text())
A = json.loads((W/'computation-audit/audit-results.json').read_text())
check('inventory_base', I['reviewed_ref'] == BASE)
check('inventory_daily_count', len(I['daily_records']) == 8)
check('baseline_separate', 'Prior weekly/monthly baseline' in I['november_1_handling'])
check('source_ledger_count', len([x for x in (R/'evidence.jsonl').read_text().splitlines() if x.strip()]) == I['main_evidence_ledger_records'])
check('audit_pass', A['checks_passed'] == A['checks_total'] == 352 and A['all_passed'])
check('audit_is_verification', A['full_simulation_rerun'] is False)
check('audit_base', A['repository_commit'] == BASE)
check('audit_source_unchanged', sha((R/A['source_directory']/'results.json').read_bytes()) == A['source_results_sha256'])
check('original_checks_recorded', '261/261' in A['original_second_calculation_reexecuted_separately'])
S = R/'updates/2026-11-08-weekly-synthesis.md'
text = S.read_text()
for value in ('352/352', '261/261', 'H18 remains', 'No numerical or code correction', 'November 1', '90 minutes', 'six primary reports'):
    check('report_term:'+value, value in text)
check('no_placeholders', not any(t in text for t in ('RESULTS_TO_INSERT', 'NEXT_TO_INSERT', 'SOURCE_TO_INSERT', 'TODO')))
for path in [S, W/'computation-audit/report.md']:
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if link.startswith('https://github.com/dotjade/project-neurofreedom/blob/'+BASE+'/'):
            rel = unquote(urlparse(link).path.split('/blob/'+BASE+'/', 1)[1])
            check('pinned_link:'+rel, (R/rel).exists())
        elif not re.match(r'https?://|#', link):
            check('local_link:'+link, (path.parent/link.split('#')[0]).resolve().exists())
for path in W.rglob('*.json'):
    if path.name in ('validation.json', 'publication-verification.json'):
        continue
    json.loads(path.read_text())
    check('valid_json:'+str(path.relative_to(R)), True)
check('no_full_text_media', not any(p.suffix.lower() in ('.pdf','.png','.jpg','.nii','.gz','.csv') for p in W.rglob('*') if p.is_file()))
base_status=git('show',BASE+':STATUS.md').decode()
expected_start=base_status.replace('four completed weekly syntheses','five completed weekly syntheses',1).replace('weekly syntheses were completed on 11, 18 and 25 October and 1 November;','weekly syntheses were completed on 11, 18 and 25 October and 1 and 8 November;',1)
check('prior_status_preserved', (R/'STATUS.md').read_text().startswith(expected_start))
check('one_weekly_status', (R/'STATUS.md').read_text().count('## Completed weekly synthesis - 8 November 2026') == 1)
base_paths=git('ls-tree','-r','--name-only',BASE).decode().splitlines()
unchanged=0
for path in base_paths:
    if path == 'STATUS.md': continue
    expected=git('rev-parse',BASE+':'+path).decode().strip()
    actual=git('hash-object',str(R/path)).decode().strip()
    if actual != expected:
        check('unrelated_file:'+path,False)
    else: unchanged+=1
check('all_unrelated_files_preserved', unchanged == len(base_paths)-1)
result={'baseline_commit':BASE,'checks_passed':sum(c['passed'] for c in checks),'checks_total':len(checks),'all_passed':all(c['passed'] for c in checks),'unrelated_baseline_files_preserved':unchanged,'feed_unchanged':sha((R/'public/research-feed.json').read_bytes())==M['files']['public/research-feed.json'],'scope':'Offline provenance, structure, audit values, links and preservation. Not clinical validation or fresh external-link, deployment or accessibility testing.','checks':checks}
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['all_passed'] else 1)
