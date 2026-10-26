#!/usr/bin/env python3
"""Offline scan consistency and data-minimization checks, not clinical validation."""
import argparse,csv,hashlib,json,pathlib,subprocess
from prepare_baseline import build
ROOT=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((ROOT/n).read_text())
def lines(n):return [json.loads(x)for x in(ROOT/n).read_text().splitlines()if x.strip()]
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);args=a.parse_args();repo=pathlib.Path(args.repo);base=build(repo);c=[]
 def check(n,v):assert v,n;c.append(n)
 s=read('summary.json');log=read('search-log.json');p=lines('pubmed-screening.jsonl');r=lines('registry-evidence.jsonl');e=lines('primary-evidence.jsonl')
 check('Exact baseline cutoff',log['prior_core_end_utc']==base['cutoff_utc']=='2026-10-25T02:46:02.904884+00:00')
 check('Eight reviewed query counts',[q['count']for q in log['pubmed']['queries']]==[1,1,1,9,0,1,0,1])
 check('Ten unique records and14 occurrences',len(p)==len({x['pmid']for x in p})==10 and sum(q['count']for q in log['pubmed']['queries'])==14)
 check('All search IDs fetched',{x['pmid']for x in p}=={i for q in log['pubmed']['queries']for i in q['ids']})
 check('Caps not reached',all(q['count']==len(q['ids'])<1000 for q in log['pubmed']['queries']))
 check('Current query dates',all(q['params']['maxdate']=='2026/10/26'and q['params']['mindate']in['2026/10/24','2026/10/25']for q in log['pubmed']['queries']))
 check('All records classified without abstracts',all('Pending'not in x['screening_decision']and not x['abstract_retained']for x in p))
 check('Four prior overlaps',sum(x['prior_scan_overlap']for x in p)==4)
 check('One original primary addition',len(e)==1 and e[0]['pmid']=='42925937'and sum(x['new_to_repository_primary_record']for x in p)==1)
 check('No prior primary identifier reference',not next(x for x in p if x['pmid']=='42925937')['historical_repository_reference_paths'])
 check('Preclinical dates and limits retained',e[0]['electronic_publication_date']=='2026-10-24'and not e[0]['newly_indexed_after_prior_cutoff_verified']and 'rat' in e[0]['population']and 'causality unresolved' in e[0]['mechanism'])
 check('Known retraction unchanged',all(not x['new_notice']and not x['selected_metadata_changes']for x in read('integrity-recheck.json')))
 total=0
 for q in log['preprints']:
  with(ROOT/q['index_path']).open()as f:idx=list(csv.DictReader(f,delimiter='\t'))
  k={(x['doi'],x['version'])for x in idx};old={(x['doi'],x['version'])for x in base['preprints'][q['server']]};total+=len(idx)
  check(q['server']+' unique count',len(idx)==len(k)==q['unique_doi_versions']==q['total_returned'])
  check(q['server']+' complete stable pagination',q['pagination_complete_for_observed_response']and sum(x['returned']for x in q['pages'])==len(idx)and q['reported_totals']==[len(idx)])
  check(q['server']+' overlap recomputed',len(k&old)==q['previous_scan_overlap_doi_versions']and len(k-old)==q['not_in_previous_scan_doi_versions'])
  check(q['server']+' dates and no hits',all('2026-10-24'<=x['date']<='2026-10-26'for x in idx)and not q['matches'])
 check('321 DOI versions',total==321)
 check('Registry query counts',[q['response']['totalCount']for q in log['registry']]==[0,0,0,0]and all(not q['response']['nextPageToken']for q in log['registry']))
 check('Four unchanged no-result controls',len(r)==4 and all(not x['selected_field_changes']and not x['hasResults']for x in r))
 check('Negative feasibility retained',next(x for x in r if x['id']=='NCT05158439')['design']['enrollmentInfo']=={'count':0,'type':'ACTUAL'})
 supp=read('supplement-selected-metadata.json');check('ISRCTN zero and control',supp['window']['root_attributes']['totalCount']=='0'and supp['positive_control']['root_attributes']['totalCount']=='22')
 check('WHO/CTIS limits explicit',not supp['who_ictrp']['query_export_obtained']and not supp['ctis']['parsed_trial_record'])
 check('29 successful core requests',len(read('request-log.json'))==29 and all(x.get('status')==200 and 'error'not in x for x in read('request-log.json')))
 check('Summary agrees',s['pubmed_unique_records']==len(p)and s['preprint_doi_versions']==total and s['new_to_repository_primary_records']==len(e))
 def keys(o):
  if isinstance(o,dict):
   for k,v in o.items():yield k;yield from keys(v)
  elif isinstance(o,list):
   for x in o:yield from keys(x)
 forbidden={'resultsSection','outcomeMeasuresModule','participantFlowModule','contactsLocationsModule','centralContacts','overallOfficials','abstract','AbstractText','__VIEWSTATE','__EVENTVALIDATION'}
 check('No source-body/participant/contact/session fields',not(set(k for f in ROOT.glob('*.json')for k in keys(json.loads(f.read_text())))|set(keys(p))|set(keys(r))|set(keys(e)))&forbidden)
 check('Source hashes match',all(hashlib.sha256(subprocess.check_output(['git','show',read('provenance.json')['baseline_commit']+':'+x['path']],cwd=repo)).hexdigest()==x['sha256']for x in read('provenance.json')['sources']))
 result={'status':'passed','checks_passed':len(c),'checks':c,'scope':'Saved metadata/count/date/privacy-boundary consistency only, not clinical validation.'};(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
