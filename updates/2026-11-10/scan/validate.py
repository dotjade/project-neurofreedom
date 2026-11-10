import json,pathlib,csv
p=pathlib.Path(__file__).parent;d=json.loads((p/'search-log.json').read_text());s=json.loads((p/'summary.json').read_text());n=0
def check(v):
 global n
 assert v;n+=1
check(len(d['pubmed']['queries'])==8)
check(d['pubmed']['id_occurrences']==54)
rows=[json.loads(x) for x in (p/'pubmed-screening.jsonl').read_text().splitlines()]
check(len(rows)==49);check(len({x['pmid'] for x in rows})==49);check(not s['remaining_screening'])
check(not s['request_errors']);check(not s['worker_errors'])
for x in s['preprints']:
 check(x['pagination_complete_for_observed_response']);check(x['matches']==[])
 idx=list(csv.DictReader((p/(x['server']+'-preprint-index.tsv')).open(),delimiter='\t'))
 check(len(idx)==x['total_returned']);check(len({(z['doi'],z['version']) for z in idx})==len(idx))
check(sum(x['total_returned'] for x in s['preprints'])==812)
rs=[json.loads(x) for x in (p/'registry-evidence.jsonl').read_text().splitlines()]
check(len(rs)==7);check(all(x['hasResults']==False for x in rs));check([x['nctId'] for x in rs if x['selected_field_changes']]==['NCT01019343','NCT07137442'])
check([x['response']['totalCount'] for x in d['registry']]==[1,2,2,0])
check(len(json.loads((p/'supplement-registry.json').read_text()))==2)
print(json.dumps({'checks_passed':n,'scope':'Metadata accounting and selected-field consistency, not search completeness or clinical validity.'},indent=2))
