"""Fresh public metadata only; overwrites dated snapshots if explicitly rerun."""
import urllib.request,json,datetime,pathlib
p=pathlib.Path(__file__).resolve().parent
ids=['NCT05615220','NCT01727700','NCT03452943','NCT03571256','NCT01647269','NCT00478842','NCT04731714','NCT04007991']
a=[]
for n in ids:
 u='https://clinicaltrials.gov/api/v2/studies/'+n
 row={'id':n,'url':u,'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  response=urllib.request.urlopen(u,timeout=40);d=json.load(response);q=d['protocolSection'];s=q['statusModule'];e=q['eligibilityModule']
  row.update(httpStatus=response.status,title=q['identificationModule']['briefTitle'],status=s['overallStatus'],lastUpdatePostDate=s.get('lastUpdatePostDateStruct'),enrollment=q['designModule'].get('enrollmentInfo'),minimumAge=e.get('minimumAge'),maximumAge=e.get('maximumAge'),primaryOutcomeNames=[v['measure'] for v in q['outcomesModule']['primaryOutcomes']],hasResults=d.get('hasResults'),evidenceType='official registry metadata, not independent trial replication')
 except Exception as exc:row['error']=str(exc)
 a.append(row)
(p/'registry-checks.json').write_text(json.dumps(a,indent=2)+'\n')
