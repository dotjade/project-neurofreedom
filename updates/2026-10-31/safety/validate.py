"""Offline integrity checks for the dated safety/link records, not clinical validation."""
import json,pathlib
P=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((P/n).read_text())
x=json.loads((P.parents[2]/'public/link-checks/2026-10-31.json').read_text())
r=load('regulatory-evidence.json')
checks=load('catalog-safety-check.json')['checks'].copy()
checks.update({
 '24_timeline_targets_retrieved':sum(t['kind']=='timeline' and t['targetConfirmedRead'] for t in x['results'])==24,
 'nine_extra_research_links_checked':sum(t['kind']=='homepageResearch' for t in x['results'])==9,
 'three_findings_checked':sum(t['kind']=='finding' for t in x['results'])==3,
 'no_confirmed_broken_target':not any(t.get('establishedBroken') for t in x['results']),
 'baseline_exact_bytes':all(t['matchesPinnedRepositoryBytes'] for t in x['results'] if t['kind'] in ('production','rawSource')),
 'production_repository_header':any(t.get('journalSource')=='repository' for t in x['results'] if t['kind']=='production'),
 'eighteen_source_checks':len(load('source-checks.json')['sources'])==18,
 'six_queries_recorded':len(load('query-ledger.json')['queries'])==6,
 'core_and_adjacent_distinguished':load('query-ledger.json')['qualifyingNewCoreWatchFindings']==0 and load('query-ledger.json')['newAdjacentRegulatoryCommunications']==1,
 'publication_not_initiation':r['publicationDate']=='2026-10-30' and r['proseInitiationDate']=='2026-10-16' and r['keyFactsProcedureStartDate']=='2026-10-29',
 'monotherapy_exclusion_preserved':'Flupentixol-only' in r['originalSummary'],
 'paper_bytes_not_retained':load('supplementary-checks.json')['paperBytesRetained'] is False,
 'no_snapshot_duplicates':not any((P/f).exists() for f in ['production.json','rawSource.json']),
 'baseline_only':x['repositoryFeedLastResearchDate']=='2026-10-30'
})
assert all(checks.values()), checks
result={'passed':sum(checks.values()),'total':len(checks),'checks':checks}
(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
