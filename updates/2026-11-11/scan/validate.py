#!/usr/bin/env python3
"""Offline consistency checks of the saved scan; not clinical peer review."""
import json,pathlib,re
p=pathlib.Path(__file__).resolve().parent
d=json.loads((p/'search-log.json').read_text());s=json.loads((p/'summary.json').read_text());sup=json.loads((p/'supplement-registry.json').read_text());checks={}
checks['pubmed_counts_match']=d['pubmed']['id_occurrences']==sum(x['count'] for x in d['pubmed']['queries'])==25
checks['pubmed_unique_match']=len({z for x in d['pubmed']['queries'] for z in x['ids']})==25==len(d['pubmed']['date_type_correction_screen'])
checks['pubmed_no_new_entry_or_pdat']=all(x['count']==0 for x in d['pubmed']['queries'] if x['label']!='core_mdat')
checks['no_errors']=not s['request_errors'] and not s['worker_errors'] and all('error' not in x for x in sup)
checks['all_core_requests_200']=len(d['retrieval_requests'])==45 and all(x['status']==200 for x in d['retrieval_requests'])
checks['preprint_totals']=sum(x['total_returned'] for x in d['preprints'])==721 and all(x['total_returned']==x['unique_doi_versions']==len(x['version_index']) for x in d['preprints'])
regex=re.compile(r'\btourett\w*|\btics?\b',re.I)
checks['preprint_lexical_controls']=bool(regex.search('Tourette syndrome')) and bool(regex.search('chronic motor tics')) and not bool(regex.search('statistics'))
checks['preprint_no_matches']=all(not x['matches'] for x in d['preprints'])
checks['preprint_overlap']=sum(x['previous_scan_overlap_doi_versions'] for x in d['preprints'])==400 and sum(x['not_in_previous_scan_doi_versions'] for x in d['preprints'])==321
checks['no_posted_ctgov_results']=all(x['hasResults'] is False for x in d['registry_records']) and all(x['record']['hasResults'] is False for x in sup)
checks['ctgov_distinct_count']=len({x['nctId'] for x in d['registry_records']}|{x['nctId'] for x in sup})==13
checks['no_selected_change_except_07137442']=all(not v for k,v in s['registry_changes'].items() if k!='NCT07137442') and set(s['registry_changes']['NCT07137442'])=={'status'}
checks['web_query_count']=len(json.loads((p/'web-query-provenance.json').read_text())['exact_queries'])==14
def badkeys(x):
 if isinstance(x,dict): return [k for k in x if k.lower() in ['abstract','contacts','contactslocationsmodule','locations','resultssection','officials']] + sum((badkeys(v) for v in x.values()),[])
 if isinstance(x,list):return sum((badkeys(v) for v in x),[])
 return []
checks['metadata_only_json']=all(not badkeys(json.loads(f.read_text())) for f in p.glob('*.json') if f.name not in ['publication-files.json','validation.json'])
r={'checks':checks,'all_pass':all(checks.values()),'limitations':'Consistency checks of saved metadata, not independent source verification or clinical peer review.'}
(p/'validation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));assert r['all_pass']
