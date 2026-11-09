#!/usr/bin/env python3
"""Deterministic consistency checks; not clinical or independent source validation."""
import json,pathlib
p=pathlib.Path(__file__).resolve().parent
m=json.loads((p/'measurement-adequacy.json').read_text())
l=json.loads((p/'search-ledger.json').read_text())
e=[json.loads(x) for x in (p/'evidence-additions.jsonl').read_text().splitlines() if x]
checks=[]
def ck(name,test):
 checks.append({'name':name,'passed':bool(test)})
ck('Exactly six primary reports',len(m['records'])==m['source_count']==m['report_cap']==6)
ck('Unique identifiers',len({r['id'] for r in m['records']})==6)
ck('Unique DOIs',len({r['doi'] for r in m['records']})==6)
ck('All historical',m['all_sources_historical'] is True)
ck('No clinical discovery claim',m['new_clinical_discovery'] is False)
ck('No participant data',m['participant_data_accessed'] is False)
required=['population','construct','comparator','result','reliability_type','repeated_session','invariance','temporal_order','clustering','missingness','transfer_estimand','alternative_explanation','anchor_decision','access','source_locations','study_type','outcomes_analysis_status','prespecification','harms','funding','conflicts','reviewer','numeric_extraction']
for r in m['records']:
 ck(r['id']+' completeness',all(r.get(k) for k in required))
 ck(r['id']+' source URL',r['url'].startswith('https://'))
 ck(r['id']+' no promoted anchor',r['anchor_decision']=='insufficient')
ck('No fabricated total hit count',l['total_search_hits_screened'] is None)
ck('Search ledger six focal reports',l['focal_reports_screened_and_extracted']==6)
ck('Source access rows',len(l['source_access'])==6)
ck('Evidence append count',len(e)==6)
ck('Evidence identifiers match',[x['doi'] for x in e]==[x['doi'] for x in m['records']])
R={r['id']:r for r in m['records']}
num=lambda key:R[key]['numeric_extraction']
u=num('mcguire2016_iputs')
ck('I-PUTS count ordering',u['second_rater_assessments']<=u['usable_iputs']<=u['participants'])
ck('I-PUTS missingness accounting',u['usable_iputs']+u['missing_iputs']==u['participants'])
b=num('baumung2020_putsr')
ck('Pooled age counts',b['adults']+b['minors']==b['participants'])
g=num('langelage2022_temporal')
ck('Temporal association counts',g['positive_logistic']+g['nonsignificant_logistic']+g['negative_logistic']==g['analyzed'])
ck('Excluded acquisition counts',g['excluded_video']+g['excluded_urge']+g['excluded_task']==g['excluded_total'])
c=num('brandt2016_convergence')
ck('Monitor samples per participant',(c['task_seconds']-c['excluded_seconds'])*c['samples_per_second']==c['retained_samples_per_participant'])
z=num('matsuda2026_monitoring')
ck('Matsuda consent and analysis flow',z['eligible_consenting']-z['experimental_exclusions']==z['analyzed']<=z['referred'])
ck('Matsuda paired degrees of freedom',z['paired_df']==z['analyzed']-1)
ck('Matsuda event trajectory accounting',z['trajectory_trial_contributors']+z['no_qualifying_episode']==z['analyzed'])
intervals=u['icc']+z['contrasts']
ck('Intervals include extracted point estimates',all(x['ci95'][0]<x['estimate']<x['ci95'][1] for x in intervals))
monitor=next(x for x in z['contrasts'] if x['outcome']=='mean urge monitor')
ck('Mean-monitor contrast uncertain',monitor['ci95'][0]<0<monitor['ci95'][1])
ck('Reviewer role recorded',bool(m.get('reviewer')) and all(x.get('reviewer') for x in e))
ck('Search time limitation explicit','not retained' in l['search_timestamp_status'])
ck('Subsequent main-text verification recorded',sum('subsequent_review' in x for x in l['source_access'])==3)
report=(p/'report.md').read_text()
ck('Explicit no inference boundary','Keep H18\'s latent mechanism unidentified' in report)
ck('Explicit transfer definitions',all(x in report for x in ['Context transfer','Tic transfer','Transfer gap','Durable functional benefit']))
ck('No generic equivalence claim','A nonsignificant gap does not establish equivalent transfer' in report)
result={'scope':'Authored schema and structured-extraction arithmetic only; no automated paper comparison, independent transcription verification or clinical validation','checks':checks,'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)}
(p/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
raise SystemExit(0 if result['failed']==0 else 1)
