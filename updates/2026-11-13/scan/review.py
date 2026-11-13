import json, pathlib, datetime, sys
P=pathlib.Path(__file__).parent
x=json.load(open(P/'scan.json'))
b=json.load(open(sys.argv[1]))
oldids={str(a['pmid']) for a in b['pubmed']['records']}
diffs={}
for old in b['registry']['records']:
 i=old['nctId'];raw=x['registry']['records'][i];p=raw['protocolSection'];new={'nctId':i,'title':p['identificationModule']['briefTitle'],'status':p['statusModule'],'conditions':p.get('conditionsModule',{}).get('conditions'), 'ages':p.get('eligibilityModule',{}),'studyType':p['designModule'].get('studyType'),'enrollment':p['designModule'].get('enrollmentInfo'),'hasResults':raw.get('hasResults')}
 diffs[i]={k:{'old':old.get(k),'new':new.get(k)} for k in old if old.get(k)!=new.get(k)}
r={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prior_scan_completed_utc':b['completed_utc'],'pubmed_overlap':sorted(oldids&set(x['pubmed']['unique_returned_ids'])),'pubmed_new_to_query':sorted(set(x['pubmed']['unique_returned_ids'])-oldids),'registry_selected_diffs':diffs,'scope':'Selected metadata comparison, not full-record history; administrative changes do not prove results.'}
(P/'review.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2)[:7000])
