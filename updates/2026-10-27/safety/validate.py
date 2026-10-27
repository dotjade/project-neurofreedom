"""Offline assertions for the dated safety/link ledgers, not clinical validation."""
import json,pathlib
P=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((P/n).read_text())
x=json.loads((P.parents[2]/'public/link-checks/2026-10-27.json').read_text())
checks=load('catalog-safety-check.json')['checks'].copy()
checks.update({
'19_timeline_targets_retrieved':sum(r['kind']=='timeline' and r['targetConfirmedRead'] for r in x['results'])==19,
'no_confirmed_broken_target':not any(r.get('establishedBroken') for r in x['results']),
'baseline_exact_bytes':all(r['matchesPinnedRepositoryBytes'] for r in x['results'] if r['kind'] in ('production','rawSource')),
'production_repository_header':any(r.get('journalSource')=='repository' for r in x['results'] if r['kind']=='production'),
'all20_source_checks_recorded':len(load('source-checks.json')['sources'])==20,
'six_queries_recorded':len(load('query-ledger.json')['queries'])==6,
'no_new_findings_claimed':load('query-ledger.json')['qualifyingNewMaterialSafetyFindings']==0,
'paper_bytes_not_retained':load('supplementary-checks.json')['paperBytesRetained'] is False})
assert all(checks.values()),checks
result={'passed':sum(checks.values()),'total':len(checks),'checks':checks}
(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
