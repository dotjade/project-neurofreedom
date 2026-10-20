#!/usr/bin/env python3
"""Derive compact metadata/decision artifacts from observed public API responses.
Run after scan_sources.py and scan_supplement.py. Live API reruns may differ.
No participant data, abstracts or full papers are written.
"""
import datetime as dt, hashlib, json, pathlib
P=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((P/n).read_text())
def write(n,v): (P/n).write_text(json.dumps(v,ensure_ascii=False,separators=(',',':'))+'\n')
def lines(n,v): (P/n).write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in v))
def diff(a,b,path=''):
    if isinstance(a,dict) and isinstance(b,dict):
        return sum((diff(a.get(k),b.get(k),path+'.'+k if path else k) for k in sorted(set(a)|set(b))),[])
    return [] if a==b else [{'field':path,'previous':a,'current':b}]
def main():
    log=read('search-log.json');supp=read('supplement-selected-metadata.json');baseline=read('baseline-metadata.json');prev=read('baseline-registry.json')
    decisions={
      '41621322':('historical_primary_overlap','January 27 pediatric obsessive-compulsive-symptom genetic study. Already screened yesterday; UpdateOf PMID 40799755 links the preprint, not independent replication. No new tic-treatment evidence.'),
      '41633747':('secondary_review','Review/chapter of functional tics, PubMed entry February 2026. October 19 metadata modification is not new publication. No new primary result; functional tic-like behaviors remain distinct from primary chronic tic disorders.'),
      '41689912':('secondary_review_overlap','February 5 systematic review of gambling cognition, already screened yesterday and outside the publication window.'),
      '41779259':('secondary_review','March 4 review of tic pathophysiology and management. October 19 metadata revision is not a new drug/stimulation result; treatment-development summaries do not establish efficacy.'),
      '42726672':('historical_biography','September 11 biographical/historical article, not a new clinical experiment or tic-treatment result. October 19 metadata revision triggered retrieval.'),
      '42890800':('conceptual_overlap','October 2 hypothesis/theory article, already classified from its publisher yesterday. Generic Journal Article indexing does not turn diagnostic proposals into primary validation.'),
      '42890894':('secondary_review_overlap','October 2 systematic review of functional tic-like behaviors, already screened yesterday; overlapping reports are not independent cohorts.'),
      '42893364':('secondary_review_overlap','May 30 pediatric PANDAS narrative review entered into PubMed October 18; already screened yesterday. No new primary chronic-tic treatment result.')
    }
    for x in log['pubmed']['date_type_correction_screen']:
        x['evidence_class'],x['screening_decision']=decisions[x['pmid']]
    lines('pubmed-screening.jsonl',log['pubmed']['date_type_correction_screen'])
    lines('secondary-screening.jsonl',[x for x in log['pubmed']['date_type_correction_screen'] if x['evidence_class']!='historical_primary_overlap'])
    lines('primary-evidence.jsonl',[])
    for x in log['preprints']:
        if 'version_index' in x:
            values=x.pop('version_index')
            file=x['server']+'-preprint-index.tsv'
            (P/file).write_text('doi\tversion\tdate\n'+''.join(f"{a['doi']}\t{a['version']}\t{a['date']}\n" for a in values))
            x['version_index_file']=file
    previous={x['id']:x for x in prev}
    records=[]
    for x in log['registry_records']:
        x['previously_checked_in_prior_direct_metadata']=x['nctId'] in previous
        x['prior_scan_overlap_definition']='Original flag refers only to prior in-window query records; direct prior checks are separately resolved here.'
        item={'id':x['nctId'],'title':x['title'],'source_url':x['source_url'],'evidence_class':'registry_protocol_update_without_results','current':{k:x[k] for k in ['status','design','hasResults','conditions','eligibility']}}
        p=previous[x['nctId']]
        item['selected_field_changes']=diff({k:p[k] for k in ['status','design','hasResults']},{k:x[k] for k in ['status','design','hasResults']})
        item['interpretation']='Estimated start changed from October 21 to October 22. Posting/submission dates changed. Recruiting status, observational design, planned enrollment 75 and absence of results are unchanged. No full version-history comparison or recruitment event is established.'
        records.append(item)
    for n in ['NCT05158439','NCT07093541','NCT06194305']:
        x=supp[n];p=previous[n]
        current={k:x[k] for k in ['status','design','hasResults']}
        records.append({'id':n,'title':x['title'],'source_url':'https://clinicaltrials.gov/study/'+n,'evidence_class':'prior_registry_status_control','current':current,'selected_field_changes':diff({k:p[k] for k in current},current),'interpretation':('Withdrawn for inability to recruit; actual enrollment zero and no results. Negative feasibility evidence, not negative efficacy or evidence of cell administration.' if n=='NCT05158439' else 'Selected status/design/results fields unchanged; posting is outside the current window. No treatment or safety result is inferred.')})
    lines('registry-evidence.jsonl',records)
    summary={
      'date':'2026-10-20','prior_cutoff_utc':'2026-10-19T03:09:45Z',
      'api_started_utc':log['started_utc'],'core_api_completed_utc':log['completed_utc'],
      'final_api_cutoff_utc':supp['completed_utc'],'web_check_end_bracket_utc':'2026-10-20T02:53:17Z',
      'cutoff_note':'Final API cutoff is machine-timestamped. Web tool supplemental checks occurred within recorded brackets, not second-precision source API timestamps.',
      'pubmed_id_occurrences':log['pubmed']['id_occurrences'],'pubmed_unique_records':log['pubmed']['unique_records'],'pubmed_prior_overlap':log['pubmed']['previous_overlap_count'],'pubmed_new_to_prior_bounded_scan':log['pubmed']['new_to_prior_scan_ids'],
      'preprint_doi_version_records':sum(x['unique_doi_versions'] for x in log['preprints']),
      'preprint_title_abstract_lexical_matches':sum(len(x['matches']) for x in log['preprints']),
      'ctgov_query_id_occurrences':sum(x['response']['totalCount'] for x in log['registry']),
      'ctgov_unique_window_records':len(log['registry_records']),
      'new_primary_study_results_verified':0,'new_registry_results_verified':0,
      'isrctn_window_total':int(supp['isrctn_window']['root_attributes']['totalCount']),
      'isrctn_positive_control_total':int(supp['isrctn_positive_control']['root_attributes']['totalCount']),
      'limitations':['Early-day overlapping rather than continuous surveillance.','Publication, indexing, modification, preprint and registry posting dates are different.','PubMed filters and preprint lexical screen may miss records; other preprint servers not enumerated.','No full registry version-history audit, worldwide registry census, usable WHO query export or systematic CTIS enumeration.','No newly retrieved primary clinical result; no cure or disease-modification inference.']
    }
    write('summary.json',summary)
    write('search-log.json',log)
    write('baseline-metadata.json',baseline)
    write('baseline-registry.json',prev)
    write('supplement-selected-metadata.json',supp)
    checks={
      'pubmed_ids_complete':sum(q['count'] for q in log['pubmed']['queries'])==8 and len(log['pubmed']['date_type_correction_screen'])==8,
      'pubmed_no_truncation':all(q['count']==len(q['ids']) and q['count']<q['params']['retmax'] for q in log['pubmed']['queries']),
      'all_pubmed_decisions_done':all('Pending' not in x['screening_decision'] for x in log['pubmed']['date_type_correction_screen']),
      'preprint_count':summary['preprint_doi_version_records']==452,
      'preprint_pages_complete':all(x['pagination_complete_for_observed_response'] for x in log['preprints']),
      'ctgov_one_deduplicated_window_record':summary['ctgov_query_id_occurrences']==2 and summary['ctgov_unique_window_records']==1,
      'ctgov_no_next_page':all(not x['response']['nextPageToken'] for x in log['registry']),
      'registry_known_controls_unchanged':all(not r['selected_field_changes'] for r in records if r['evidence_class']=='prior_registry_status_control'),
      'registry_no_results':all(not r['current']['hasResults'] for r in records),
      'empty_primary_ledger':(P/'primary-evidence.jsonl').stat().st_size==0,
      'no_core_api_errors':not any('error' in r for r in log['retrieval_requests'])
    }
    assert all(checks.values()),checks
    write('validation.json',{'checked_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'checks':checks,'passed':True})
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
