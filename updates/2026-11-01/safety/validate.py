import json,pathlib
p=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((p/n).read_text())
q=load('query-ledger.json');s=load('source-checks.json');r=load('regulatory-evidence.json');c=load('catalog-safety-check.json')
checks=dict(c['checks'])
checks.update(six_searches=len(q['queries'])==6,eleven_sources=len(s['sources'])==11,one_batch_notice=q['qualifyingNewCoreWatchCommunications']==1,exact_batch=r['batch']=='DNG1035A',dates_distinct=r['noticeDate']=='2026-11-01' and r['recallDate']=='2026-10-27',class_and_level=r['recallClass']==2 and r['recallLevel']=='Retail',no_individual_data=r['individualDataRetained'] is False,no_full_page=r['fullExternalPageRetained'] is False)
for n in ['link-check-rerun.json','homepage-link-check.json']:
 x=load(n);checks[n+'_dated']=x['checkDate']=='2026-11-01';checks[n+'_no_established_broken']=not any(z.get('establishedBroken') for z in x['results'])
checks['baseline_not_new_publication']=load('link-check-rerun.json')['repositoryFeedLastResearchDate']=='2026-10-31'
out={'checks':checks,'passed':sum(checks.values()),'total':len(checks),'allPassed':all(checks.values())};(p/'validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['allPassed']
