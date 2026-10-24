#!/usr/bin/env python3
"""Offline Oct24 metadata and privacy-boundary checks, not clinical validation."""
import argparse,csv,hashlib,json,pathlib
from prepare_baseline import build
ROOT=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((ROOT/n).read_text())
def lines(n):return [json.loads(x)for x in(ROOT/n).read_text().splitlines()if x.strip()]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);a=ap.parse_args();repo=pathlib.Path(a.repo);base=build(repo);checks=[]
 def check(n,v):assert v,n;checks.append(n)
 log=read('search-log.json');s=read('summary.json');p=lines('pubmed-screening.jsonl');r=lines('registry-evidence.jsonl');e=lines('primary-evidence.jsonl')
 check('Exact baseline cutoff',log['prior_core_end_utc']==base['cutoff_utc']=='2026-10-23T02:57:07.490048+00:00')
 check('Eight PubMed queries with reviewed counts',[q['count']for q in log['pubmed']['queries']]==[3,1,0,18,0,4,0,2])
 check('19 unique records and 28 occurrences',len(p)==len({x['pmid']for x in p})==19 and sum(q['count']for q in log['pubmed']['queries'])==28)
 check('All searched PubMed records fetched',{x['pmid']for x in p}==set(i for q in log['pubmed']['queries']for i in q['ids']))
 check('No PubMed cap reached',all(q['count']==len(q['ids'])<q['params']['retmax']for q in log['pubmed']['queries']))
 check('Current PubMed interval',all(q['params']['maxdate']=='2026/10/24'and q['params']['mindate']in['2026/10/22','2026/10/23']for q in log['pubmed']['queries']))
 check('All PubMed classified without abstracts',all('Pending'not in x['screening_decision']and x['abstract_retained']is False for x in p))
 check('13 prior-scan overlaps',sum(x['prior_scan_overlap']for x in p)==13)
 check('Exactly one primary addition',len(e)==1 and e[0]['pmid']=='42908833'and sum(x['new_to_repository_primary_record']for x in p)==1)
 check('Primary DOI/PMID not previously referenced',not next(x for x in p if x['pmid']=='42908833')['historical_repository_reference_paths'])
 check('New primary not duplicate evidence',e[0]['id']not in(repo/'evidence.jsonl').read_text())
 check('Indexing distinct from publication',e[0]['electronic_publication_date']=='2026-10-07'and e[0]['pubmed_entry_date']=='2026-10-23'and not e[0]['new_publication_after_prior_cutoff'])
 check('Case exact publication timing unknown',next(x for x in p if x['pmid']=='42910671')['new_publication_since_prior_cutoff']is None)
 check('Person/files/decisions denominators explicit',e[0]['sample']['development_unique_people']==25 and e[0]['sample']['development_labeled_video_derived_files']==125 and e[0]['sample']['external_heldout_people']==7 and e[0]['sample']['heldout_phenotype_decisions']==56)
 check('Tic-positive denominator is zero not sensitivity estimate',e[0]['sample']['heldout_consensus_positive_tics']==0 and 'not estimable'in e[0]['tic_specific_result'])
 check('Selected known-retraction metadata unchanged',len(read('integrity-recheck.json'))==2 and all(not x['new_notice']and not x['selected_metadata_changes']for x in read('integrity-recheck.json')))
 total=matches=0
 for q in log['preprints']:
  with(ROOT/q['index_path']).open()as f:idx=list(csv.DictReader(f,delimiter='\t'))
  keys={(x['doi'],x['version'])for x in idx};old={(x['doi'],x['version'])for x in base['preprints'][q['server']]};total+=len(idx);matches+=len(q['matches'])
  check(q['server']+' unique version counts',len(idx)==len(keys)==q['unique_doi_versions']==q['total_returned'])
  check(q['server']+' complete stable pagination',q['pagination_complete_for_observed_response']and sum(x['returned']for x in q['pages'])==len(idx)and q['reported_totals']==[len(idx)])
  check(q['server']+' independently recomputed overlap',len(keys&old)==q['previous_scan_overlap_doi_versions']and len(keys-old)==q['not_in_previous_scan_doi_versions'])
  check(q['server']+' current dates',all('2026-10-22'<=x['date']<='2026-10-24'for x in idx))
 check('597 versions and one excluded lexical hit',total==597 and matches==1 and all(not m['qualifying_tic_result']for q in log['preprints']for m in q['matches']))
 check('Registry counts and pagination',[q['response']['totalCount']for q in log['registry']]==[0,1,1,0]and all(not q['response']['nextPageToken']for q in log['registry']))
 fields='NCTId,BriefTitle,StatusModule,DesignModule,Condition,MinimumAge,MaximumAge,StdAge,HasResults'
 check('Safe exact CT.gov server projection',all(q['params']['fields']==fields for q in log['registry']))
 check('Four controls without results',len(r)==len({x['id']for x in r})==4 and all(x['hasResults']is False for x in r))
 check('Only start/post/submission changes',all(not x['selected_field_changes']for x in r if x['id']!='NCT07137442')and {c['field']for x in r if x['id']=='NCT07137442'for c in x['selected_field_changes']}=={'status.startDateStruct.date','status.lastUpdatePostDateStruct.date','status.lastUpdateSubmitDate'})
 check('Changed estimated start not actual',next(x for x in r if x['id']=='NCT07137442')['status']['startDateStruct']=={'date':'2026-10-28','type':'ESTIMATED'})
 check('Zero enrollment negative feasibility retained',next(x for x in r if x['id']=='NCT05158439')['design']['enrollmentInfo']=={'count':0,'type':'ACTUAL'})
 supp=read('supplement-selected-metadata.json');check('ISRCTN zero and positive control',supp['window']['root_attributes']['totalCount']=='0'and supp['positive_control']['root_attributes']['totalCount']=='22')
 check('WHO and CTIS unverified coverage explicit',not supp['who_ictrp']['query_export_obtained']and not supp['ctis']['parsed_trial_record'])
 check('38 successful core API requests',len(read('request-log.json'))==38 and all(x.get('status')==200 and 'error'not in x for x in read('request-log.json')))
 check('One source metadata confirmation',len(read('primary-source-checks.json'))==1 and read('primary-source-checks.json')[0]['selected_metadata']['doi']==e[0]['doi'])
 check('Summary agrees',s['pubmed_unique_records']==len(p)and s['preprint_doi_versions']==total and s['new_to_repository_primary_records']==len(e)and s['new_posted_trial_results']==0)
 def keys(o):
  if isinstance(o,dict):
   for k,v in o.items():yield k;yield from keys(v)
  elif isinstance(o,list):
   for x in o:yield from keys(x)
 forbidden={'resultsSection','outcomeMeasuresModule','participantFlowModule','contactsLocationsModule','centralContacts','locationContacts','overallOfficials','abstract','AbstractText','__VIEWSTATE','__EVENTVALIDATION'}
 check('No source body/participant/contact/session fields',not set(k for f in ROOT.glob('*.json')for k in keys(json.loads(f.read_text())))&forbidden and not(set(keys(r))|set(keys(p))|set(keys(e)))&forbidden)
 check('No baseline duplicate artifact',not(ROOT/'baseline.json').exists())
 check('Source hashes still match',all(hashlib.sha256((repo/x['path']).read_bytes()).hexdigest()==x['sha256']for x in read('provenance.json')['sources']))
 if(ROOT/'manifest.json').exists():check('Manifest file sizes and hashes',all((ROOT/x['path']).stat().st_size==x['bytes']and hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256']for x in read('manifest.json')['files']))
 result={'status':'passed','checks_passed':len(checks),'checks':checks,'scope':'Offline saved-metadata/count/date/deduplication/retention checks; not clinical validation or peer review.'};(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
