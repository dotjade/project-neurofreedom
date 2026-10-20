"""Read the named official registry, retaining selected non-participant metadata only.
No individual outcome rows, narratives, contact details or source copies are saved.
"""
import urllib.request, json, hashlib, datetime
from pathlib import Path
u='https://clinicaltrials.gov/api/v2/studies/NCT05371041'
with urllib.request.urlopen(u,timeout=30) as r:
    status=r.status
    data=r.read()
raw=json.loads(data)
p=raw['protocolSection']; r=raw.get('resultsSection',{}); a=r.get('adverseEventsModule',{})
flow=r.get('participantFlowModule',{})
out={
 'source_url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'http_status':status,'source_sha256':hashlib.sha256(data).hexdigest(),
 'retention':'Selected metadata and published cohort aggregates only; no individual results, narratives or source body retained.',
 'nct_id':p['identificationModule']['nctId'],
 'status':p['statusModule'],
 'design':p['designModule'],
 'eligibility_age':{k:p['eligibilityModule'].get(k) for k in ('minimumAge','maximumAge','stdAges')},
 'previous_neurosurgery_exclusion_verified': 'Any previous neurosurgical intervention' in p['eligibilityModule']['eligibilityCriteria'],
 'ipd_sharing':p.get('ipdSharingStatementModule'),
 'has_results':raw['hasResults'],
 'primary_outcome_titles_timeframes':[{'measure':x['measure'],'timeFrame':x['timeFrame']} for x in p['outcomesModule']['primaryOutcomes']],
 'participant_flow':[{'period':x['title'],'milestones':[{'type':m['type'],'subjects':[y['numSubjects'] for y in m['achievements']]} for m in x['milestones']]} for x in flow.get('periods',[])],
 'ae_timeframe':a.get('timeFrame'),
 'ae_frequency_threshold':a.get('frequencyThreshold'),
 'ae_totals':[{k:x.get(k) for k in ['deathsNumAffected','deathsNumAtRisk','seriousNumAffected','seriousNumAtRisk','otherNumAffected','otherNumAtRisk']} for x in a.get('eventGroups',[])],
 'ae_assessment_types':sorted({x['assessmentType'] for kind in ['seriousEvents','otherEvents'] for x in a.get(kind,[])}),
 'documents':raw.get('documentSection',{}).get('largeDocumentModule',{}).get('largeDocs',[])
}
Path(__file__).with_name('registry-selected-metadata.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
