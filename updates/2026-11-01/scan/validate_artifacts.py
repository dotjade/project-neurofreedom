#!/usr/bin/env python3
"""Consistency and data-minimization checks, not clinical validation."""
import json,csv,pathlib,hashlib,subprocess,datetime,re,ast
p=pathlib.Path(__file__).resolve().parent; repo=p.parents[2];checks=[]
def check(label,test):
 assert test,label
 checks.append(label)
def js(n):return json.loads((p/n).read_text())
def jl(n):return [json.loads(x)for x in(p/n).read_text().splitlines()]
s=js('search-log.json');summary=js('summary.json');pub=jl('pubmed-screening.jsonl');reg=jl('registry-evidence.jsonl');req=js('request-log.json')
check('correct scan date',s['date']=='2026-11-01')
check('prior cutoff matches October31',s['prior_core_end_utc']==json.loads((repo/'updates/2026-10-31/scan/summary.json').read_text())['core_completed_utc'])
check('times ordered',s['prior_core_end_utc']<s['started_utc']<s['completed_utc'])
check('eight query families',len(s['pubmed']['queries'])==8)
check('query IDs match fetched',set().union(*(set(x.get('ids',[]))for x in s['pubmed']['queries']))=={x['pmid']for x in pub})
check('fetch count matches summary',len(pub)==summary['pubmed_unique_records'])
check('unique PMIDs',len(pub)==len({x['pmid']for x in pub}))
check('all IDs explicitly screened',all(x['screening_decision']and 'Pending' not in x['screening_decision']for x in pub))
check('no abstracts retained',all(x['abstract_retained']==False and 'abstract'not in x for x in pub))
check('no new publication falsely claimed',not any(x['new_publication_since_prior_cutoff']for x in pub))
check('error count',summary['api_request_errors']==sum('error'in r for r in req))
check('no unknown worker errors',not s.get('worker_errors'))
for x in s['preprints']:
 ix=list(csv.DictReader((p/x['index_path']).open(),delimiter='\t'));server=x['server']
 check(server+' unique count',len({(a['doi'],a['version'])for a in ix})==x['unique_doi_versions'])
 check(server+' index count',len(ix)==x['total_returned'])
 check(server+' citation only',all(set(a)=={'doi','version','date'}for a in ix))
 check(server+' lexical screen no matches',not x['matches'])
 check(server+' regex positive TS control',bool(re.search(x['screen_regex'],'Tourette syndrome',re.I)))
 check(server+' regex positive tic control',bool(re.search(x['screen_regex'],'persistent motor tics',re.I)))
 check(server+' regex negative control',not re.search(x['screen_regex'],'statistics',re.I))
 check(server+' observed pages complete',x['pagination_complete_for_observed_response'])
 check(server+' total stable',len(x['reported_totals'])==1)
check('preprint combined count',summary['preprint_doi_versions']==sum(x['unique_doi_versions']for x in s['preprints']))
check('unique registry IDs',len(reg)==len({x['id']for x in reg}))
check('registry selected fields unchanged',not any(x['selected_field_changes']for x in reg))
check('no result posts',not any(x['hasResults']for x in reg))
check('all registry results below cap',all(not q.get('response',{}).get('nextPageToken')for q in s['registry']))
check('retractions unchanged',all(not x['selected_metadata_changed_fields']for x in js('integrity-recheck.json')))
check('WHO not overstated',js('supplement-selected-metadata.json')['who_ictrp']['query_export_obtained']==False)
check('CTIS not overstated',js('supplement-selected-metadata.json')['ctis']['parsed_trial_record']==False)
check('older papers not new',all(x['new_window_publication']==False for x in js('older-evidence.json')['records']))
for f in p.rglob('*'):
 if f.is_file()and f.suffix in {'.json','.jsonl','.tsv','.md'}:
  check(f.name+' no private collection fields',not any(t in f.read_text() for t in ['"contactsLocationsModule"','"patient_id"','"participant_id"','"emailAddress"']))
(p/'validation.json').write_text(json.dumps({'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_passed':len(checks),'checks':checks,'scope':'Metadata consistency and minimization, not proof of comprehensive coverage or clinical validity.'},indent=2)+'\n')
print(len(checks),'checks passed')
if __name__=='__main__':pass
