#!/usr/bin/env python3
"""Build original screening decisions from captured metadata; no external requests."""
import json,pathlib,hashlib,csv,datetime as dt
OUT=pathlib.Path(__file__).resolve().parent
load=lambda name:json.loads((OUT/name).read_text())
def write(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
def jsonl(name,items): (OUT/name).write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in items))
def flatten(x,p=''):
 if isinstance(x,dict):
  out={}
  for k,v in x.items():out.update(flatten(v,p+'.'+k if p else k))
  return out
 return {p:x}
def main():
 s=load('search-log.json');base=load('baseline-metadata.json');sup=load('supplement-selected-metadata.json');rbase={x['id']:x for x in load('baseline-registry.json')}
 prior={x['pmid']:x for x in base['pubmed']};screen=s['pubmed']['date_type_correction_screen']
 decisions={
 '41220182':'Historical November 2025 rat model intervention study; October 20 metadata revision is not a new clinical or preclinical result. Retained separately as preclinical historical context; no human efficacy inferred.',
 '41794658':'March 2026 scoping review of functional tics; October 20 metadata revision is not new primary evidence. Functional tic-like presentations remain distinct from primary tic disorders.',
 '42896917':'Newly encountered adjacent technical primary study; no Tourette cohort or tic clinical outcome. PubMed/Crossref date October 19 precedes strict prior cutoff, with publisher metadata also showing October 15. Within overlap-query window but not verified newly published since cutoff.'}
 for x in screen:
  x['screening_decision']=decisions.get(x['pmid'],prior.get(x['pmid'],{}).get('screening_decision','Historical/secondary overlap; no newly verified result.'))
  x['abstract_review_today']=x['pmid'] in decisions;x['abstract_retained']=False
  x['new_qualifying_primary_tic_result']=False
 jsonl('pubmed-screening.jsonl',screen)
 jsonl('primary-evidence.jsonl',[])
 c={x['pmid']:x for x in load('candidate-verification.json')['records']}
 technical={
  'id':'pmid:42896917','pmid':'42896917','doi':'10.3174/ajnr.A9681','title':c['42896917']['title'],'authors':c['42896917']['authors'],'year':2026,
  'source_urls':['https://pubmed.ncbi.nlm.nih.gov/42896917/','https://doi.org/10.3174/ajnr.A9681'],
  'evidence_class':'adjacent_technical_primary_evidence_newly_encountered_not_since_cutoff',
  'discovery_date':'2026-10-21','pubmed_electronic_date':'2026-10-19','pubmed_entry_date':'2026-10-19T20:54 (database time zone unspecified)',
  'date_conflict':'PubMed and Crossref date October 19; publisher DC.Date October 19 but citation_publication_date/article:published_time October 15. Both precede prior scan cutoff. Do not choose a resolved first-publication date.',
  'study_type':'Retrospective MRI-sequence comparison across separate cohorts.',
  'population':'Cerebral cavernous malformations not involving thalamus, epilepsy and healthy comparison cohorts; no Tourette cohort described. Ages and severe-adult applicability unverified.',
  'sample_counts':{'QSM_cavernous_malformation':24,'WMn_epilepsy':16,'MP2RAGE_healthy':24},
  'comparator':'Indirect comparison across independent cohorts, not within-person sequence comparison.',
  'exposure':'QSM, white-matter-null and MP2RAGE MRI sequences; no therapeutic intervention tested.',
  'outcomes':'Centromedian-nucleus contrast, contrast-to-noise and signal-to-noise metrics; prospective specification unverified.',
  'result':'Abstract reports better lateral thalamic contrast on QSM but lower overall signal-to-noise. Complementary targeting utility remains a proposal.',
  'followup':'Imaging-methods comparison, not clinical benefit follow-up.',
  'uncertainty':'Sequence and cohort differences are confounded; full-methods bias/precision assessment not completed.',
  'adverse_events':'No treatment safety inference.', 'attrition':'Flow/exclusions not verified from abstract.',
  'conflicts_funding':'Not established in this bounded extraction.',
  'cohort_deduplication':'No matching DOI/PMID in prior bounded baseline. Relationship to other imaging cohorts not resolved; not counted as independent tic-treatment evidence.',
  'claim_supported':'Adjacent imaging-methods lead only.','claim_not_supported':'Accurate individual targeting, prospective tic prediction, clinical efficacy, durable disease modification or cure.',
  'retrieval_status':'Official PubMed abstract reviewed transiently; publisher metadata accessible; full methods not audited.',
  'correction_retraction_check':'No PubMed linked notice or Crossref update-to relation returned; not comprehensive clearance.',
  'next_verification_task':'No expansion of current aggregate registry task; revisit only for a focused imaging question with full methods.'}
 jsonl('adjacent-evidence.jsonl',[technical])
 historical=[{'id':'pmid:41220182','doi':'10.1002/brb3.71041','title':c['41220182']['title'],'source_url':'https://pubmed.ncbi.nlm.nih.gov/41220182/','class':'historical_preclinical_primary','published':'2025-11','metadata_revised':'2026-10-20','design':'IDPN-induced rat model comparing jujuboside A, tiapride and combination groups with model/normal controls.','original_summary':'Abstract reports changes in striatal glutamate/GABA and stereotyped behavior; sample sizes, numerical precision and risk of bias were not extracted. Animal stereotypy is not validated human tic benefit or a treatment recommendation.','retrieval_status':'Abstract-only review; no source text retained.','decision':'Exclude from new-window count; preserve as historical preclinical context without therapeutic promotion.'}]
 jsonl('historical-preclinical.jsonl',historical)
 jsonl('secondary-screening.jsonl',[x for x in screen if x['pmid'] not in ['41220182','42896917']])
 reg=[]
 for nct in ['NCT07137442','NCT05158439','NCT07093541','NCT06194305']:
  now=sup[nct];cur={k:now[k] for k in ['status','design','hasResults']};old={k:rbase[nct]['current'][k] for k in cur};a,b=flatten(old),flatten(cur)
  diff=[{'field':k,'previous':a.get(k),'current':b.get(k)} for k in sorted(set(a)|set(b)) if a.get(k)!=b.get(k)]
  note={'NCT07137442':'Estimated start October 22 to October 25; posting October 19 to October 20; submission October 16 to October 19. Recruiting status, observational design, estimated enrollment 75 and no results unchanged. No verified recruitment event or efficacy result.', 'NCT05158439':'Withdrawn for inability to recruit; actual enrollment zero, no results. Negative feasibility, not negative efficacy or evidence of cell administration.','NCT07093541':'Temporarily unavailable expanded access remains unchanged. No new suspension or its cause inferred.','NCT06194305':'Recruiting pediatric CBIT study; unchanged selected status/design/results fields. No trial result inferred.'}[nct]
  reg.append({'id':nct,'title':now['title'],'source_url':'https://clinicaltrials.gov/study/'+nct,'evidence_class':'newly_observed_registry_protocol_posting_without_results' if diff else 'prior_registry_status_control','current':cur,'selected_field_changes':diff,'interpretation':note,'comparison_scope':'Selected status/design/hasResults fields only; not full version history.'})
 jsonl('registry-evidence.jsonl',reg)
 pp=load('preprint-resume-log.json')['preprints']
 for p in pp:
  with (OUT/(p['server']+'-preprint-index.tsv')).open('w') as f:
   w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t');w.writeheader();w.writerows(p['version_index'])
 end=max(s['completed_utc'],sup['completed_utc'],load('preprint-resume-log.json')['completed_utc'],load('selected-candidate-checks.json')['completed_utc'],load('publisher-date-check.json')['completed_utc'])
 summary={'date':'2026-10-21','prior_cutoff_utc':base['cutoff_utc'],'overlap_inclusive':['2026-10-19','2026-10-21'],'api_started_utc':s['started_utc'],'final_main_api_cutoff_utc':end,'web_discovery_end_bracket_utc':'2026-10-21T02:53:54Z','pubmed_id_occurrences':s['pubmed']['id_occurrences'],'pubmed_unique_records':len(screen),'pubmed_prior_overlap':sum(x['prior_scan_overlap'] for x in screen),'new_qualifying_primary_tic_study_outcomes':0,'adjacent_primary_studies_newly_encountered':1,'historical_preclinical_studies_newly_encountered':1,'preprint_doi_version_records':sum(x['unique_doi_versions'] for x in pp),'preprint_lexical_matches':sum(len(x['matches']) for x in pp),'preprint_complete_observed_totals':all(x['pagination_complete_for_observed_response'] for x in pp),'ctgov_query_occurrences':sum(x['response']['totalCount'] for x in s['registry']),'ctgov_unique_window_records':len(s['registry_records']),'new_registry_postings':1,'new_registry_results':0,'isrctn_window_total':int(sup['isrctn_window']['root_attributes']['totalCount']),'isrctn_positive_control_total':int(sup['isrctn_positive_control']['root_attributes']['totalCount']),'preprint_recovery':'Initial baseline version_index KeyError prevented feed requests. TSV baseline restored; first feed pass timed out at cursor 60 for both; resume uses longer timeout and logs every attempt.','limitations':['Early-day overlapping surveillance, not continuous or exhaustive.','No age/severity restriction; explicit adult severe burden/comorbidity/negative-result query. No result means evidence gap, not absence of burden or efficacy.','PubMed publication/entry/modification and registry posting dates differ; newly encountered does not mean newly published.','Preprint lexical screen can miss synonyms; other servers not comprehensively enumerated.','WHO query export unavailable; CTIS SPA returns no interpreted protocol record; national/worldwide registry coverage incomplete.','Full registry history and comprehensive publisher/Crossmark clearance not performed.','No participant data, stories, full abstracts or papers retained; original summaries and public metadata only.']}
 write('summary.json',summary)
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
