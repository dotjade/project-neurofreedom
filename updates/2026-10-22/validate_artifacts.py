#!/usr/bin/env python3
"""Offline metadata and publication-boundary checks; not clinical validation."""
import argparse,csv,hashlib,json,pathlib
from prepare_baseline import build
ROOT=pathlib.Path(__file__).resolve().parent

def read(name):return json.loads((ROOT/name).read_text())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);a=ap.parse_args();base=build(pathlib.Path(a.repo));checks=[]
 def check(name,condition):assert condition,name;checks.append(name)
 log=read('search-log.json');summary=read('summary.json');pub=[json.loads(x) for x in (ROOT/'pubmed-screening.jsonl').read_text().splitlines()];reg=[json.loads(x) for x in (ROOT/'registry-evidence.jsonl').read_text().splitlines()]
 check('Eight complete PubMed queries',len(log['pubmed']['queries'])==8 and all('count' in x for x in log['pubmed']['queries']))
 check('Four unique PubMed IDs and four occurrences',len(pub)==len({x['pmid'] for x in pub})==4 and sum(q['count'] for q in log['pubmed']['queries'])==4)
 check('All ESearch IDs fetched',set(x['pmid'] for x in pub)==set(i for q in log['pubmed']['queries'] for i in q['ids']))
 check('PubMed result caps not reached',all(q['count']==len(q['ids']) and q['count']<q['params']['retmax'] for q in log['pubmed']['queries']))
 check('All records classified, no new tic outcome',all(x['screening_decision'] and not x['new_qualifying_primary_tic_result'] for x in pub))
 check('No full abstract retained',all(x['abstract_retained'] is False for x in pub))
 check('Two prior-day overlaps',sum(x['prior_scan_overlap'] for x in pub)==2)
 check('Retraction status remains explicit','Retracted Publication' in next(x for x in pub if x['pmid']=='39947542')['types'] and 'Retraction Notice' in next(x for x in pub if x['pmid']=='42527169')['types'])
 check('No new retraction claimed',all(x['new_notice'] is False for x in read('integrity-recheck.json')))
 total=0;matches=0
 for p in log['preprints']:
  with (ROOT/p['index_path']).open() as f:idx=list(csv.DictReader(f,delimiter='\t'))
  keys={(x['doi'],x['version']) for x in idx};old={(x['doi'],x['version']) for x in base['preprints'][p['server']]};n=len(idx);total+=n;matches+=len(p['matches'])
  check(p['server']+' unique version count',n==len(keys)==p['unique_doi_versions']==p['total_returned'])
  check(p['server']+' observed pages complete',p['pagination_complete_for_observed_response'] and sum(x['returned'] for x in p['pages'])==n and p['reported_totals']==[n])
  check(p['server']+' overlap independently recomputed',len(keys&old)==p['previous_scan_overlap_doi_versions'] and len(keys-old)==p['not_in_previous_scan_doi_versions'])
  check(p['server']+' all dates in inclusive interval',all('2026-10-20'<=x['date']<='2026-10-22' for x in idx))
 check('639 preprint versions and one excluded lexical match',total==639 and matches==1 and all(not m['qualifying_tic_result'] for p in log['preprints'] for m in p['matches']))
 check('Registry query counts 0,1,1,0', [q['response']['totalCount'] for q in log['registry']]==[0,1,1,0])
 check('No registry pagination token',all(not q['response']['nextPageToken'] for q in log['registry']))
 check('Server projection excludes result measurements',all('fields' in q['params'] and 'HasResults' in q['params']['fields'] and 'ResultsSection' not in q['params']['fields'] and 'OutcomeMeasure' not in q['params']['fields'] for q in log['registry']))
 check('Four direct registry controls, no results',len(reg)==len({r['id'] for r in reg})==4 and all(r['hasResults'] is False for r in reg))
 check('Only watched start/post/submission dates changed',all(not r['selected_field_changes'] for r in reg if r['id']!='NCT07137442') and {x['field'] for r in reg if r['id']=='NCT07137442' for x in r['selected_field_changes']}=={'status.startDateStruct.date','status.lastUpdatePostDateStruct.date','status.lastUpdateSubmitDate'})
 check('Withdrawn zero-enrollment counterevidence kept',next(x for x in reg if x['id']=='NCT05158439')['design']['enrollmentInfo']=={'count':0,'type':'ACTUAL'})
 check('ISRCTN negative and positive controls',read('supplement-selected-metadata.json')['window']['root_attributes']['totalCount']=='0' and read('supplement-selected-metadata.json')['positive_control']['root_attributes']['totalCount']=='22')
 check('WHO and CTIS gaps explicit',read('supplement-selected-metadata.json')['who_ictrp']['query_export_obtained'] is False and read('supplement-selected-metadata.json')['ctis']['parsed_trial_record'] is False)
 check('All core requests successful',all(x.get('status')==200 and 'error' not in x for x in read('request-log.json')))
 check('New-primary ledger deliberately empty',(ROOT/'primary-evidence.jsonl').read_bytes()==b'')
 check('Summary agrees with saved outputs',summary['pubmed_unique_records']==len(pub) and summary['preprint_doi_versions']==total and summary['new_posted_trial_results']==0)
 check('No duplicated baseline publication artifact',not (ROOT/'baseline.json').exists())
 if (ROOT/'manifest.json').exists():
  m=read('manifest.json')
  check('Manifest SHA256 hashes and sizes match',all((ROOT/x['path']).stat().st_size==x['bytes'] and hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in m['files']))
 result={'status':'passed','checks_passed':len(checks),'checks':checks,'scope':'Offline saved-metadata and boundary checks, not clinical hypothesis testing or peer review.'};(ROOT/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
