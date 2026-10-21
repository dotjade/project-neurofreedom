#!/usr/bin/env python3
"""Deterministic metadata/boundary checks, not statistical efficacy tests."""
import json
from pathlib import Path
from collect_registry_metadata import validate, FIELDS
root=Path(__file__).parent
m=json.loads((root/'registry-projected-metadata.json').read_text())
d=m['data']; validate(d)
x=json.loads((root/'structured-extraction.json').read_text())
p=d['protocolSection'];r=d['resultsSection'];o=r['outcomeMeasuresModule']['outcomeMeasures'][0];a=r['adverseEventsModule']
checks={
 'correct_trial':p['identificationModule']['nctId']=='NCT05371041',
 'projection_matches_saved_script':m['projection_fields']==FIELDS,
 'result_classes_not_requested':all(not any(z in f for z in ['.classes','.categories','.measurements']) for f in FIELDS),
 'eight_actual_enrollees':p['designModule']['enrollmentInfo']=={'count':8,'type':'ACTUAL'},
 'baseline_module_n8':r['baselineCharacteristicsModule']['denoms'][0]['counts'][0]['value']=='8',
 'endpoint_n8':o['denoms'][0]['counts'][0]['value']=='8',
 'baseline_100_definition':any(q.get('title')=='YGTSS Score' and 'out of 100' in q.get('description','') for q in r['baselineCharacteristicsModule']['measures']),
 'endpoint_50_definition':'(0 to 50)' in o['description'],
 'nine_month_label':o['timeFrame']=='9 months',
 'initiation_clock_preserved':'after the initiation of DBS' in o['groups'][0]['description'],
 'lead_surgery_safety_clock':'after lead implant surgery' in a['timeFrame'],
 'nonsystematic_label':set(e['assessmentType'] for e in a['seriousEvents']+a['otherEvents'])=={'NON_SYSTEMATIC_ASSESSMENT'},
 'safety_totals_preserved':[(e['deathsNumAffected'],e['seriousNumAffected'],e['otherNumAffected'],e['deathsNumAtRisk'],e['seriousNumAtRisk'],e['otherNumAtRisk']) for e in a['eventGroups']]==[(0,3,8,8,8,8)],
 'no_analysis_object_returned':'analyses' not in o,
 'no_dispersion_object_returned':'dispersionType' not in o,
 'stopping_gate_retained':x['decision']=='STOP_WITHOUT_EFFICACY_CALCULATION' and x['efficacy_calculation_performed'] is False,
 'participant_values_not_saved':x['participant_rows_saved_or_analyzed'] is False,
 'no_retained_pdf':not list(root.glob('*.pdf')),
}
assert all(checks.values()),checks
(root/'metadata-checks.json').write_text(json.dumps({'passed':sum(checks.values()),'total':len(checks),'checks':checks,'interpretation':'Metadata consistency and privacy-boundary checks only; not clinical verification or hypothesis tests.'},indent=2)+'\n')
print(json.dumps({'passed':sum(checks.values()),'total':len(checks)}))
