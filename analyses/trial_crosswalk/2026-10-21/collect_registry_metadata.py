#!/usr/bin/env python3
"""Fetch only explicit metadata/aggregate fields; never request result classes.
No participant outcome rows, event descriptions, or full registry body are fetched.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

BASE = 'https://clinicaltrials.gov/api/v2/studies/NCT05371041'
FIELDS = [
 'protocolSection.identificationModule',
 'protocolSection.statusModule',
 'protocolSection.designModule',
 'protocolSection.outcomesModule',
 'protocolSection.referencesModule',
 'protocolSection.ipdSharingStatementModule',
 'documentSection', 'hasResults',
 'resultsSection.participantFlowModule.groups',
 'resultsSection.participantFlowModule.periods.title',
 'resultsSection.participantFlowModule.periods.milestones',
 'resultsSection.baselineCharacteristicsModule.groups',
 'resultsSection.baselineCharacteristicsModule.denoms',
 'resultsSection.baselineCharacteristicsModule.populationDescription',
 'resultsSection.baselineCharacteristicsModule.measures.title',
 'resultsSection.baselineCharacteristicsModule.measures.description',
 'resultsSection.baselineCharacteristicsModule.measures.paramType',
 'resultsSection.baselineCharacteristicsModule.measures.unitOfMeasure',
 'resultsSection.baselineCharacteristicsModule.measures.denoms',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.type',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.title',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.description',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.timeFrame',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.paramType',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.dispersionType',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.unitOfMeasure',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.denoms',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.groups',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.analyses',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.populationDescription',
 'resultsSection.outcomeMeasuresModule.outcomeMeasures.reportingStatus',
 'resultsSection.adverseEventsModule.timeFrame',
 'resultsSection.adverseEventsModule.frequencyThreshold',
 'resultsSection.adverseEventsModule.eventGroups',
 'resultsSection.adverseEventsModule.seriousEvents.assessmentType',
 'resultsSection.adverseEventsModule.otherEvents.assessmentType',
]

def validate(data):
    def visit(x):
        if isinstance(x, dict):
            assert not ({'classes','categories','measurements'} & set(x)), 'Unexpected measurement payload; do not save.'
            for value in x.values(): visit(value)
        elif isinstance(x, list):
            for value in x: visit(value)
    visit(data)
    assert data['protocolSection']['identificationModule']['nctId'] == 'NCT05371041'
    for event in data['resultsSection']['adverseEventsModule'].get('seriousEvents', []) + data['resultsSection']['adverseEventsModule'].get('otherEvents', []):
        assert set(event) <= {'assessmentType'}


def main():
    assert all('.classes' not in f and '.categories' not in f and '.measurements' not in f for f in FIELDS)
    url = BASE + '?' + urllib.parse.urlencode({'fields': ','.join(FIELDS)})
    with urllib.request.urlopen(url, timeout=60) as response:
        body = response.read()
        status = response.status
    data = json.loads(body)
    validate(data)
    record = {
      'source_url': BASE,
      'request_url': url,
      'retrieved_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
      'http_status': status,
      'projected_response_sha256': hashlib.sha256(body).hexdigest(),
      'projection_fields': FIELDS,
      'retention': 'Server-projected definitions, study metadata, denominators and published whole-cohort safety totals only. No result classes or individual rows requested or saved.',
      'data': data,
    }
    output = Path(__file__).parent / 'registry-projected-metadata.json'
    output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'output': str(output), 'http_status':status, 'retrieved_utc':record['retrieved_utc'], 'projected_response_sha256':record['projected_response_sha256']}))

if __name__ == '__main__': main()
