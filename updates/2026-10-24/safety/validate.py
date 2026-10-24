"""Offline documentation/boundary checks. No network or clinical validation."""
import datetime, json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text())
daily_path=ROOT/'2026-10-24.json'
if not daily_path.exists(): daily_path=ROOT.parents[2]/'public/link-checks/2026-10-24.json'
daily=json.loads(daily_path.read_text())
queries=read('query-ledger.json')
sources=read('source-checks.json')
catalog=read('catalog-safety-check.json')
provenance=read('repository-provenance.json')
supplement=read('supplementary-checks.json')
counts={kind:sum(x['kind']==kind for x in daily['results']) for kind in ['timeline','finding','homepageResearch','production','rawSource','feedbackConfig','homepage']}
baseline=[x for x in daily['results'] if x['kind'] in ('production','rawSource')]
pappert=next(x for x in supplement['results'] if x['label']=='Pappert institutional primary alternative')
checks={
 'pinned_base':daily['baseCommit']==provenance['baseCommit']=='275d4cbb7386f41dc275395a11acad3a479c5a95',
 'correct_daily_date':daily['checkDate']=='2026-10-24',
 'link_counts':counts=={'timeline':16,'finding':3,'homepageResearch':9,'production':1,'rawSource':1,'feedbackConfig':1,'homepage':1},
 'no_established_broken_target':not any(x['establishedBroken'] for x in daily['results']),
 'timeline_targets_confirmed':all(x['targetConfirmedRead'] for x in daily['results'] if x['kind']=='timeline'),
 'baseline_feed_bytes':all(x['httpStatus']==200 and x['matchesPinnedRepositoryBytes'] and x['matchesRepository'] for x in baseline),
 'baseline_old_not_new_edition':all(x['updatedAt']=='2026-10-23T03:57:38Z' and x['lastResearchDate']=='2026-10-23' for x in baseline),
 'production_header':next(x for x in baseline if x['kind']=='production')['journalSource']=='repository',
 'baseline_feedback_disabled':all(x['feedback']['enabled'] is False and x['feedback']['sampleSize']==0 for x in baseline),
 'canonical_challenge_not_broken':any(x['label']=='Pappert and colleagues, 2003' and x['httpStatus']==403 and not x['establishedBroken'] for x in daily['results'] if x['kind']=='finding'),
 'attributed_primary_alternative':pappert['httpStatus']==200 and pappert['expectedIdentityConfirmed'] and 'rcpsych.ac.uk' in pappert['url'],
 'supplementary_paper_bytes_removed':supplement['paperBytesRetained'] is False,
 'source_check_count':len(sources['checks'])==22,
 'source_strict_cutoff_matches':sources['windowStart']==queries['windowStart']=='2026-10-23T03:01:22Z' and sources['windowEnd']==queries['windowEnd']=='2026-10-24T02:46:04Z',
 'queries_distinct_six':len(set(q for b in queries['batches'] for q in b['queries']))==queries['queryCount']==6,
 'captured_card_count':sum(len(b['screenedCards']) for b in queries['batches'])==queries['resultCardsScreened']==27,
 'every_card_has_disposition':all(x['decision'] and x['url'].startswith('https://') for b in queries['batches'] for x in b['screenedCards']),
 'known_access_limit_retained':any(x['title']=='NICE NG127' and x['status']=='access_limited_http_403' for x in sources['checks']) and any(x['title']=='EMA COMP minutes September 8-10' and x['status']=='reader_error_not_screened' for x in sources['checks']),
 'catalog_and_source_checks_pass':len(catalog['checks'])==14 and catalog['allPassed'] and all(catalog['checks'].values()),
 'no_publication_claim':provenance['publishedByThisCheck'] is False and provenance['repositoryModifiedByThisCheck'] is False,
 'no_full_papers_in_delivery':not any(p.suffix.lower() in {'.pdf','.html','.xml'} for p in ROOT.rglob('*') if p.is_file()),
 'report_limitations_present':all(t in (ROOT/'report.md').read_text() for t in ['not proof that no new risk exists','not verification of the later October 24 publication','No access restriction was bypassed','No individual narratives, participant data']),
}
result={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'checkCount':len(checks),'allPassed':all(checks.values()),'scope':'Offline documentation/software checks, not clinical validation or independent clinical peer review.'}
(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(0 if result['allPassed'] else 1)
