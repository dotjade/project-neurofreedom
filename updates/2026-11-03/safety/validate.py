import json,pathlib
R=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((R/n).read_text())
a=load('link-check-rerun.json');b=load('homepage-link-check.json');s=load('catalog-safety-check.json');c=load('source-checks.json');q=load('query-ledger.json');checks={}
checks['dated']=a['checkDate']==b['checkDate']=='2026-11-03'
checks['twenty_four_timeline']=sum(x['kind']=='timeline' for x in a['results'])==24
checks['all_baseline_timeline_verified']=all(x['targetConfirmedRead'] for x in a['results'] if x['kind']=='timeline')
checks['none_established_broken']=not any(x['establishedBroken'] for x in a['results']+b['results'])
checks['raw_api_match']=all(x['matchesRepository'] for x in a['results'] if x['kind'] in ('production','rawSource'))
checks['all_additional_research_status_recorded']=all(x.get('targetConfirmedRead',x.get('contentMatchesExpected')) or (x['httpStatus']==203 and x['status']=='access_limited_or_target_unverified') for x in b['results'] if x['kind'] in ('timeline','homepageResearch'))
checks['source_count']=len(c['sources'])==11
checks['queries']=len(q['queries'])==6
checks['no_new_notice']=q['qualifyingNewCoreWatchCommunications']==0
checks['catalog_checks']=all(s['checks'].values())
result={'checks':checks,'passed':all(checks.values()),'count':len(checks)}
(R/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert result['passed']
