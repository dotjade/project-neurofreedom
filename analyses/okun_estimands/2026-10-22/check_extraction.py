#!/usr/bin/env python3
"""Offline checks of source metadata and inference boundaries, not efficacy tests."""
import json,hashlib,datetime,sys
from pathlib import Path
from collect_registry_metadata import validate
P=Path(__file__).parent
x=json.loads((P/'structured-extraction.json').read_text())
r=json.loads((P/'registry-projected-metadata.json').read_text())['data']
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
validate(r); check('registry contains no result classes/categories/measurement rows',True)
check('identity NCT02056873',r['protocolSection']['identificationModule']['nctId']==x['study']['nct'])
check('actual enrollment ten',r['protocolSection']['designModule']['enrollmentInfo']['count']==x['study']['enrolled']==10)
check('chronic treatment not randomized',r['protocolSection']['designModule']['designInfo']['allocation']=='NON_RANDOMIZED')
check('registry completed',r['protocolSection']['statusModule']['overallStatus']=='COMPLETED')
check('results date historical',r['protocolSection']['statusModule']['resultsFirstPostDateStruct']['date']==x['registry']['results_first_posted']=='2024-09-05')
check('completion-date discrepancy preserved',r['protocolSection']['statusModule']['completionDateStruct']['date']==x['registry']['completion_date']!=x['registry']['paper_completion_date'])
o=r['resultsSection']['outcomeMeasuresModule']['outcomeMeasures']
check('one posted primary endpoint',len(o)==1 and o[0]['type']=='PRIMARY')
check('registry forty percent continuous endpoint', '40%' in o[0]['title'] and 'CDBS' in o[0]['title'])
check('registry six-month clock',o[0]['timeFrame']==x['registry']['primary_timeframe'])
check('registry endpoint denominator ten',o[0]['denoms'][0]['counts'][0]['value']==str(x['registry']['primary_denominator']))
check('no functional endpoint in projected outcome definitions',not any(any(t in z['title'].lower() for t in ['mos','sf-36','quality of life']) for z in o))
period=r['resultsSection']['participantFlowModule']['periods'][1]
m={z['type']:int(z['achievements'][0]['numSubjects']) for z in period['milestones']}
check('responsive period starts eight completes five',m['STARTED']==x['registry']['responsive_period_started']==8 and m['COMPLETED']==x['registry']['responsive_period_completed']==5)
a=r['resultsSection']['adverseEventsModule']
check('safety separate three-year window',a['timeFrame']==x['safety']['registry_window']=='3 years')
check('safety ascertainment systematic',all(z['assessmentType']==x['safety']['assessment'] for z in a['seriousEvents']+a['otherEvents']))
check('other event threshold one percent',a['frequencyThreshold']=='1')
for i,g in enumerate(x['safety']['groups']):
 raw=a['eventGroups'][i]
 check('safety published group totals '+str(i),raw['seriousNumAffected']==g['serious_affected'] and raw['otherNumAffected']==g['other_affected'] and raw['deathsNumAffected']==g['deaths'] and raw['seriousNumAtRisk']==g['at_risk'])
check('Cagle same-trial reference',any(z['pmid']=='36094652' for z in r['protocolSection']['referencesModule']['references']))
f=x['estimands'][2]
check('functional missing quantities not invented',all(f[z] is None for z in ['instrument_version','recall_window','scoring_algorithm','paired_denominator','aggregate_paired_mean_change','paired_change_sd','confidence_interval','adjusted_p_values','multiplicity_method']))
check('nonsignificance not equivalence',f['nonsignificance_is_equivalence'] is False)
check('functional calculation stopped',x['decision']['clinical_effect_calculated'] is False and x['decision']['compatible_functional_effect_identified'] is False)
check('no patient or synthetic clinical inference',x['decision']['participant_data_analyzed'] is False and x['decision']['simulation_performed'] is False)
check('planned days not actual within-day claim',x['protocol']['planned_video_test_days']==3 and x['protocol']['same_day_assessment_assumed'] is False)
# A deliberately fabricated malformed metadata object checks the parser boundary only.
try:
 validate({'protocolSection':{'identificationModule':{'nctId':'NCT02056873'}},'measurements':[]})
except AssertionError: rejected=True
else: rejected=False
check('synthetic malformed measurement payload rejected',rejected)
out={'executed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':len(checks),'failed':0,'checks':checks,'interpretation':'Documentation consistency and privacy-boundary tests only; not statistical tests, independent efficacy replication or clinical validation.','input_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['structured-extraction.json','registry-projected-metadata.json']}}
if '--no-write' not in sys.argv:
 (P/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
