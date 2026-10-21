#!/usr/bin/env python3
"""Offline bookkeeping checks; not independent scientific peer review."""
import pathlib,json,hashlib,csv,datetime as dt,argparse,ast
P=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((P/n).read_text())
rows=lambda n:[json.loads(x) for x in (P/n).read_text().splitlines() if x]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--check-manifest',action='store_true');args=ap.parse_args();checks=[]
 def check(name,v):
  assert v,name
  checks.append(name)
 s=load('summary.json');q=load('search-log.json');pm=rows('pubmed-screening.jsonl');r=rows('registry-evidence.jsonl');pp=load('preprint-resume-log.json')['preprints']
 check('eight_unique_pubmed_records',len(pm)==len({x['pmid'] for x in pm})==8)
 check('eleven_pubmed_id_occurrences',sum(x['count'] for x in q['pubmed']['queries'])==s['pubmed_id_occurrences']==11)
 check('all_pubmed_ids_fetched',set(x['pmid'] for x in pm)==set(y for x in q['pubmed']['queries'] for y in x['ids']))
 check('five_prior_overlaps',sum(x['prior_scan_overlap'] for x in pm)==5)
 check('zero_new_qualifying_primary_tic_outcomes',not rows('primary-evidence.jsonl') and s['new_qualifying_primary_tic_study_outcomes']==0)
 check('adjacent_primary_not_misclassified',len(rows('adjacent-evidence.jsonl'))==1 and 'not_since_cutoff' in rows('adjacent-evidence.jsonl')[0]['evidence_class'])
 check('preprints_no_duplicates_all_observed_pages',all(x['total_returned']==x['unique_doi_versions']==len({(y['doi'],y['version']) for y in x['version_index']}) and x['pagination_complete_for_observed_response'] and x['reported_totals']==[x['total_returned']] for x in pp))
 check('652_preprints_zero_matches',sum(x['total_returned'] for x in pp)==652 and sum(len(x['matches']) for x in pp)==0)
 check('preprint_dates_within_overlap',all('2026-10-19'<=y['date']<='2026-10-21' for x in pp for y in x['version_index']))
 check('tsv_indexes_match_logs',all(list(csv.DictReader((P/(x['server']+'-preprint-index.tsv')).open(),delimiter='\t'))==x['version_index'] for x in pp))
 check('three_exact_registry_date_diffs',len(r[0]['selected_field_changes'])==3 and {x['field'] for x in r[0]['selected_field_changes']}=={'status.startDateStruct.date','status.lastUpdateSubmitDate','status.lastUpdatePostDateStruct.date'})
 check('registry_controls_unchanged',all(not x['selected_field_changes'] for x in r[1:]))
 check('registry_no_results',all(x['current']['hasResults'] is False for x in r))
 check('negative_feasibility_preserved',r[1]['current']['status']['overallStatus']=='WITHDRAWN' and r[1]['current']['design']['enrollmentInfo']=={'count':0,'type':'ACTUAL'})
 check('isrctn_zero_with_positive_control',s['isrctn_window_total']==0 and s['isrctn_positive_control_total']==22)
 check('known_recoveries_documented',q['worker_errors']==["'version_index'","'version_index'"] and len([x for x in load('preprint-search-log.json')['retrieval_requests'] if 'error' in x])==2 and not any('error' in x for x in load('preprint-resume-log.json')['retrieval_requests']))
 for path in P.glob('*.py'):ast.parse(path.read_text(),filename=str(path))
 check('python_sources_parse',True)
 if args.check_manifest:
  manifest=load('manifest.json')
  for x in manifest['files']:
   b=(P/x['path']).read_bytes();check('manifest_'+x['path'],hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes'])
  check('allowlist_excludes_caches_source_bodies',all('__pycache__' not in x['path'] and not x['path'].endswith(('.html','.xml','.pdf','.pyc')) for x in manifest['files']))
 result={'validated_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'status':'passed','checks_passed':len(checks),'checks':checks,'scope':'Offline consistency checks, not independent scientific peer review.'}
 if args.write:(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
