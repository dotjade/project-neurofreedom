#!/usr/bin/env python3
"""Offline scan metadata/count/retention checks, not clinical validation."""
import argparse,csv,hashlib,json,pathlib
from prepare_baseline import build
ROOT=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((ROOT/n).read_text())
def lines(n):return [json.loads(x) for x in (ROOT/n).read_text().splitlines() if x.strip()]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);a=ap.parse_args();base=build(pathlib.Path(a.repo));checks=[]
 def check(n,v):assert v,n;checks.append(n)
 log=read('search-log.json');s=read('summary.json');p=lines('pubmed-screening.jsonl');r=lines('registry-evidence.jsonl');e=lines('primary-evidence.jsonl')
 check('Eight complete PubMed queries',len(log['pubmed']['queries'])==8 and all('count' in q for q in log['pubmed']['queries']))
 check('PubMed exact query counts',[q['count'] for q in log['pubmed']['queries']]==[2,2,0,19,0,2,0,2])
 check('19 unique records and 27 occurrences',len(p)==len({x['pmid']for x in p})==19 and sum(q['count'] for q in log['pubmed']['queries'])==27)
 check('All searched PubMed records fetched',{x['pmid'] for x in p}==set(i for q in log['pubmed']['queries'] for i in q['ids']))
 check('No PubMed result cap reached',all(q['count']==len(q['ids'])<q['params']['retmax'] for q in log['pubmed']['queries']))
 check('All PubMed records classified without abstract persistence',all(x['screening_decision'] and x['abstract_retained'] is False for x in p))
 check('Exactly two prior-day overlaps',sum(x['prior_scan_overlap'] for x in p)==2)
 check('Two new-to-repository primary records exactly',set(x['pmid'] for x in e)=={'42902960','42903303'} and len(e)==2)
 check('New IDs have no old repository reference matches',all(not x['historical_repository_reference_paths']for x in p if x['pmid'] in {'42902960','42903303'}))
 check('New indexing distinguished from publication',all(x['pubmed_entry_date']=='2026-10-22' and x['electronic_publication_date']<'2026-10-22' and not x['new_publication_after_prior_cutoff'] for x in e))
 check('No existing evidence ID duplicated',not any(x['id'] in (pathlib.Path(a.repo)/'evidence.jsonl').read_text() for x in e))
 check('Retraction exclusion and reciprocal notice retained',all(not x['new_notice'] and not x['selected_metadata_changes'] for x in read('integrity-recheck.json')))
 total=0;matches=0
 for q in log['preprints']:
  with (ROOT/q['index_path']).open() as f:idx=list(csv.DictReader(f,delimiter='\t'))
  keys={(x['doi'],x['version']) for x in idx};old={(x['doi'],x['version']) for x in base['preprints'][q['server']]};total+=len(idx);matches+=len(q['matches'])
  check(q['server']+' version dedup count',len(idx)==len(keys)==q['unique_doi_versions']==q['total_returned'])
  check(q['server']+' complete stable pagination',q['pagination_complete_for_observed_response'] and sum(x['returned'] for x in q['pages'])==len(idx) and q['reported_totals']==[len(idx)])
  check(q['server']+' independently recomputed overlap',len(keys&old)==q['previous_scan_overlap_doi_versions'] and len(keys-old)==q['not_in_previous_scan_doi_versions'])
  check(q['server']+' inclusive dates',all('2026-10-21'<=x['date']<='2026-10-23' for x in idx))
 check('701 all-subject preprint versions and two excluded matches',total==701 and matches==2 and all(not m['qualifying_tic_result']for q in log['preprints']for m in q['matches']))
 check('Registry query counts and pagination',[q['response']['totalCount'] for q in log['registry']]==[0,1,1,0] and all(not q['response']['nextPageToken'] for q in log['registry']))
 fields='NCTId,BriefTitle,StatusModule,DesignModule,Condition,MinimumAge,MaximumAge,StdAge,HasResults'
 check('CT.gov server-side projection is exact safe allowlist',all(q['params']['fields']==fields for q in log['registry']))
 check('Four direct controls without posted results',len(r)==len({x['id'] for x in r})==4 and all(x['hasResults'] is False for x in r))
 check('Only expected start/post/submission changes',all(not x['selected_field_changes']for x in r if x['id']!='NCT07137442') and {c['field']for x in r if x['id']=='NCT07137442'for c in x['selected_field_changes']}=={'status.startDateStruct.date','status.lastUpdatePostDateStruct.date','status.lastUpdateSubmitDate'})
 check('Negative feasibility zero enrollment retained',next(x for x in r if x['id']=='NCT05158439')['design']['enrollmentInfo']=={'count':0,'type':'ACTUAL'})
 supp=read('supplement-selected-metadata.json');check('ISRCTN negative query and positive control',supp['window']['root_attributes']['totalCount']=='0' and supp['positive_control']['root_attributes']['totalCount']=='22')
 check('WHO and CTIS gaps explicit',not supp['who_ictrp']['query_export_obtained'] and not supp['ctis']['parsed_trial_record'])
 check('41 successful core requests',len(read('request-log.json'))==41 and all(x.get('status')==200 and 'error' not in x for x in read('request-log.json')))
 check('Both primary source metadata confirmed',len(read('primary-source-checks.json'))==2 and all(x.get('status')==200 and x.get('selected_metadata',{}).get('doi') for x in read('primary-source-checks.json')))
 check('Summary agrees',s['pubmed_unique_records']==len(p) and s['preprint_doi_versions']==total and s['new_to_repository_primary_records']==len(e) and s['new_posted_trial_results']==0)
 def keys(o):
  if isinstance(o,dict):
   for k,v in o.items():yield k;yield from keys(v)
  elif isinstance(o,list):
   for x in o:yield from keys(x)
 forbidden={'resultsSection','outcomeMeasuresModule','participantFlowModule','contactsLocationsModule','centralContacts','locationContacts','overallOfficials','abstract','AbstractText'}
 check('No forbidden source-body/participant/contact fields',not (set(keys(log))|set(keys(r))|set(keys(read('primary-source-checks.json'))))&forbidden)
 check('No duplicated baseline artifact',not (ROOT/'baseline.json').exists())
 if (ROOT/'manifest.json').exists():check('Manifest file hashes and sizes',all((ROOT/x['path']).stat().st_size==x['bytes'] and hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256']for x in read('manifest.json')['files']))
 result={'status':'passed','checks_passed':len(checks),'checks':checks,'scope':'Offline saved-metadata and public-retention checks; not clinical hypothesis testing or peer review.'};(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
