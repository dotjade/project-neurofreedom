#!/usr/bin/env python3
"""Apply original dated screening decisions to public metadata. No external writes."""
import json,pathlib,datetime as dt
p=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((p/n).read_text())
def save(n,x):(p/n).write_text(json.dumps(x,indent=2)+'\n')
def jl(n,x):(p/n).write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n' for v in x))
r=read('search-log.json')
decisions={
'10382139':'Historical 1999 comparative executive-function report; October 17 metadata revision is not a new study. No abstract available in EFetch; no new extraction or efficacy claim.',
'11055462':'Historical 2000 letter/comment with case-report classification. No individual case details reviewed or retained; not new primary evidence.',
'11518480':'Historical 2001 autism working-memory comparison includes a Tourette comparator. Abstract reports no between-group working-memory differences. Not a new publication or tic-treatment result.',
'40977255':'Historical September 2025 electronic publication with October 17 metadata revision. Small repeated intracranial-recording study, not a new-window study or treatment-effect trial. Preserve as historical mechanistic follow-up lead.',
'41621322':'Historical January 2026 pediatric OCS genetic analysis; tic-disorder polygenic scores do not establish a new TS-specific causal treatment target. Linked UpdateOf preprint PMID 40799755 is the same work, not independent replication.',
'41689912':'Historical February 2026 systematic review of gambling cognition; secondary and outside the new-publication window.',
'42888480':'October 16 pediatric abdominal-tic narrative review already screened October 18. No new cohort or validated diagnostic-accuracy estimate.',
'42889367':'Sepsis editorial; unrelated lexical return, excluded.',
'42889785':'Palladium nanocatalyst study; unrelated lexical return, excluded.',
'42890800':'October 2 hypothesis/theory article, newly encountered in PubMed. A conceptual classification proposal, not primary diagnostic-validation evidence; do not infer functional etiology from coprolalia alone.',
'42890894':'October 2 systematic review of functional tic-like behaviors, newly encountered in PubMed. Secondary synthesis, with overlapping cohorts explicitly acknowledged; do not add its included studies as independent new cohorts.',
'42893364':'May 30 pediatric PANDAS narrative review newly indexed in October; secondary synthesis, not new chronic-tic immune-treatment evidence or adult efficacy.'}
for x in r['pubmed']['date_type_correction_screen']:x['screening_decision']=decisions[x['pmid']]
save('search-log.json',r)
jl('primary-evidence.jsonl',[])
secondary=[]
for x in r['pubmed']['date_type_correction_screen']:
 if x['pmid'] in ['42890800','42890894','42893364','41689912','42888480']:
  secondary.append({'date_checked':'2026-10-19','id':'pmid:'+x['pmid'],'evidence_type':'hypothesis_theory' if x['pmid']=='42890800' else 'secondary_review_screening','title':x['title'],'doi':x['identifiers']['doi'],'source_url':x['source_url'],'article_dates':x['article_dates'],'decision':decisions[x['pmid']],'new_primary_cohort':False,'source_access':'Public abstract/metadata; no full-text extraction. Frontiers publisher classifications independently inspected for PMID 42890800 and 42890894.'})
jl('secondary-screening.jsonl',secondary)
x=next(x for x in r['pubmed']['date_type_correction_screen'] if x['pmid']=='40977255')
jl('historical-leads.jsonl',[{'date_checked':'2026-10-19','id':'pmid:40977255','doi':'10.1002/mds.70043','title':x['title'],'source_urls':[x['source_url'],'https://doi.org/10.1002/mds.70043'],'evidence_type':'historical_primary_mechanistic_lead','publication_date':'2025-09-22','design':'Repeated CM and aGPi intracranial recordings, six TS participants with severe treatment-resistant tics, nine monthly visits; no stimulation during recordings.','original_summary':'Low-frequency power and pallido-thalamic coherence differed between tic and symptom-free recording states. Within-person association identifies a candidate signal; it does not demonstrate causal tic generation, reliable clinical prediction, treatment benefit or disease modification.','population_limit':'Age distribution not verified; do not label an adult-only cohort or extrapolate across severity. Six implanted participants are not nine independent cohorts or repeated-visit sample sizes.','full_text_status':'Abstract only; public metadata and abstract inspected transiently.','cohort_deduplication':'Absent from main ledger and exact-PMID GitHub code search. Same-participant overlap with other DBS reports remains unresolved; do not pool as an independent cohort.','correction_check':'No linked correction/retraction in this EFetch snapshot; not full Crossmark clearance.','next_verification':'Check licensed full-text eligibility, ages, clinical-trial identifiers and overlap with prior DBS cohorts before a bounded mechanism analysis.','new_window_evidence':False}])
old={x['id']:x for x in read('baseline-supplement.json')['registry']};reg=[]
for x in read('supplement-selected-metadata.json')['registry']:
 keys=['status','design','hasResults'];reg.append({'date_checked':'2026-10-19','id':'nct:'+x['id'],'evidence_type':'registry_recheck_not_new_evidence','source_url':'https://clinicaltrials.gov/study/'+x['id'],'compared_fields':keys,'changes':{k:{'before':old[x['id']].get(k),'after':x.get(k)} for k in keys if old[x['id']].get(k)!=x.get(k)},'status':x['status'],'has_results':x['hasResults'],'new_result':False})
jl('registry-evidence.jsonl',reg)
s={'date':'2026-10-19','prior_cutoff_utc':'2026-10-18T02:41:39Z','core_started_utc':r['started_utc'],'core_completed_utc':r['completed_utc'],'inclusive_overlap':['2026-10-17','2026-10-19'],'pubmed_unique':r['pubmed']['unique_records'],'pubmed_occurrences':r['pubmed']['id_occurrences'],'pubmed_new_to_prior_scan_ids':r['pubmed']['new_to_prior_scan_ids'],'new_window_primary_additions':0,'historical_primary_leads':1,'preprint_doi_versions':sum(x['unique_doi_versions'] for x in r['preprints']),'preprint_matches':sum(len(x['matches']) for x in r['preprints']),'ctgov_in_window_records':len(r['registry_records']),'ctgov_new_results':0,'isrctn_window_count':int(read('supplement-selected-metadata.json')['isrctn'][0]['root_attributes']['totalCount']),'conclusion':'No new-window qualifying primary tic result or newly posted relevant registry result verified. Newly encountered PubMed IDs are not synonymous with newly published studies.'}
save('summary.json',s)
assert len(decisions)==len(r['pubmed']['date_type_correction_screen'])==12
assert r['pubmed']['id_occurrences']==21
assert not [x for x in r['retrieval_requests'] if x.get('error')]
print(json.dumps(s,indent=2))
