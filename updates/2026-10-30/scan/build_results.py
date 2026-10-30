#!/usr/bin/env python3
"""Normalize reviewed Oct30 public metadata. Refuse new unreviewed identifiers."""
import argparse,csv,json,pathlib,re,subprocess
from prepare_baseline import build

def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def flat(x,p=''):
 o={}
 if isinstance(x,dict):
  for k,v in x.items():o.update(flat(v,p+'.'+k if p else k))
 else:o[p]=x
 return o

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=pathlib.Path(a.repo);out=pathlib.Path(a.out);out.mkdir(exist_ok=True,parents=True);raw=json.loads(pathlib.Path(a.raw).read_text());base=build(repo)
 known={'33959852', '42949677', '42856611', '35567613', '41618542', '42943225', '42947547', '35467133', '42952789', '35859051', '42467078', '41693549', '33944988', '35654996', '33966152', '35838898', '35723689', '32560953', '42934522', '42412229', '42941499', '42951691'}
 pub=raw['pubmed'].pop('date_type_correction_screen');assert {x['pmid'] for x in pub}==known,'Identifiers need review'
 decisions={
 '32560953':('historical_adjacent_primary','2020 pediatric trichotillomania study; not new tic-treatment evidence.'),
 '35467133':('historical_primary','2022 Taiwan population incidence/prevalence report; revision is not a new publication.'),
 '35654996':('historical_other_condition','2022 neurosurgical outcome-measure proposal; not primary tic evidence.'),
 '35723689':('historical_secondary','2022 diagnostic classification review; not new empirical tic evidence.'),
 '35838898':('historical_secondary','2022 DBS technology review; not independent clinical trial.'),
 '42947547':('newly_retrieved_october28_primary','October 28 adult force-matching study newly retrieved. Calendar-date publication verified; exact time after previous early-day cutoff unknown. Preserve indirect-condition null, absent precision and correlation-versus-causation distinction.'),
 '42949677':('older_newly_indexed_review','July 8 network-informed DBS perspective newly indexed; secondary hypothesis, not new trial or established target.'),

 '40927925':('historical_primary_metadata_revision','September 2025 pregnancy/outcome association study; not a new-window publication. No individual data or causal treatment inference.'),
 '41025609':('historical_secondary_metadata_revision','September 2025 vagus-nerve-stimulation review, not new primary efficacy evidence.'),
 '41204680':('historical_other_condition_primary_metadata_revision','November 2025 laryngeal dystonia study, not a new Tourette trial.'),
 '41334637':('historical_secondary_metadata_revision','December 2025 complementary-medicine review; methodological limitations prohibit blanket treatment recommendations.'),
 '41518128':('historical_primary_metadata_revision','January 2026 adult registry psychiatric-burden study; current revision is not new publication. Shared registry cohort is not independent replication.'),
 '42818614':('prior_deferred_exploratory_primary','September food-IgG study already deferred October 9. Retrospective association rules do not diagnose allergy or establish dietary tic treatment. No new extraction.'),
 '42934522':('older_primary_new_to_repository','Previously extracted July 30 qualitative GP-TiCS care-experience paper. Preserve publisher-version caveat and indexing-time uncertainty. Aggregate roles/themes only, no interview narratives.'),
 '42935160':('irrelevant_acronym_collision','TICs means toxic industrial chemicals, not tic disorders.'),
 '42938876':('irrelevant_acronym_collision','TICs means MRI time-intensity curves, not tic disorders.'),
 '42941499':('adjacent_primary_not_tic_specific','October 15 pediatric misophonia study, not a tic-treatment study. No family narratives extracted.'),
 '42943225':('older_preclinical_new_to_repository','Previously extracted September 26 rat/cell study with October 27 indexing. Experimental phenotype changes do not establish human efficacy, safety or disease modification.'),

 '41059647':('historical_primary_metadata_revision','October 2025 functional tic-like behavior follow-up, not a new primary Tourette publication. No identifying narratives retained.'),
 '41392858':('historical_secondary_metadata_revision','December 2025 trial-representation meta-analysis, not new independent trial results.'),
 '42189206':('historical_primary_metadata_revision','May 2026 pediatric tic/functional-tic comparison; revision is not new research. No family-level descriptions extracted.'),
 '42391199':('historical_primary_metadata_revision','July 2026 rage-attacks study; October revision is not a new publication. Burden remains relevant without equating rage and tics.'),
 '42412229':('historical_primary_metadata_revision','July 2026 developmental cohort study, not new-window evidence or adult-specific prediction.'),
 '42467078':('historical_primary_metadata_revision','July 2026 pediatric EMTICS treatment-pattern report; medication-use associations are not randomized treatment effects.'),
 '42525239':('historical_letter_metadata_revision','July 2026 care-pathway letter, not new controlled treatment evidence.'),
 '42910671':('prior_case_report_metadata_only','Prior case report; exact publication date unknown. Citation metadata only, no narrative retained.'),
 '42919181':('prior_primary_overlap','Previously extracted CHD/Tourette study. Null overall estimate and table/prose contradiction retained; revision is not new research.'),
 '42921162':('case_series_citation_metadata_only','October 23 case series already screened. Citation metadata only; not controlled Tourette treatment evidence.'),
 '42925937':('prior_preclinical_primary_overlap','October 24 rat-model paper already extracted. Preserve unresolved causality, abstract-only access and absent human efficacy/safety evidence.')}
 decisions.update({'33944988': ('historical_primary_revision', '2021 EMTICS sex/age clinical-presentation study; not new publication. Pediatric cross-sectional age differences do not prove individual trajectory.'), '33959852': ('historical_pilot_revision', '2021 oral-orthotic pilot in 13 youth. Initial difference was not reproduced during follow-up; no intervention recommendation.'), '33966152': ('historical_primary_revision', '2021 Iranian pediatric prevalence/comorbidity survey; not new-window evidence.'), '35567613': ('historical_primary_revision', '2022 dystonic tic clinical characterization; not new-window publication. No video or individual narrative accessed.'), '35859051': ('historical_secondary_revision', '2022 cannabis-based medicines systematic review, not new trial evidence.'), '41618542': ('historical_biographical_revision', 'January 2026 historical tribute, not primary clinical evidence.'), '41693549': ('other_condition_revision', 'February 2026 Parkinson disease urinary-infection study, not Tourette evidence.'), '42856611': ('prior_primary_revision', 'October 1 TMS plus CBIT trial already extracted October 12. No duplication or relabeling as new publication.'), '42951691': ('adjacent_primary_older_than_cutoff', 'October 28 Iceland ADHD clinical sample; tic/Tourette prevalence reported similar across presentations. Not a tic-specific causal or treatment study; no equivalent prevalence proof from nonsignificance.'), '42952789': ('older_primary_newly_retrieved', 'October 14 pediatric cross-sectional CD4/vitamin association, indexed October 29. YGTSS global includes impairment; vitamin correlations fail primary FDR correction. No immune mechanism or supplementation effect established.'), '42947547': ('prior_primary_overlap', 'Adult force-matching paper already extracted October 29; indirect null and absent interaction/precision remain. Current study is not prospective prediction.')})
 for x in pub:
  pm=x['pmid'];doi=x['identifiers'].get('doi');matches=set()
  for term in [pm,doi]:
   if term:
    r=subprocess.run(['git','grep','-l','-F',term,'e324b6d369652b9a280faf8b318d9321fd2d4dcb','--','*.md','*.json','*.jsonl','*.tsv'],cwd=repo,text=True,capture_output=True)
    matches.update(t.split(':',1)[1] for t in r.stdout.splitlines())
  typ,decision=decisions[pm]
  x.update(historical_repository_reference_paths=sorted(matches),abstract_retained=False,new_to_repository_primary_record=pm=='42952789',new_publication_since_prior_cutoff=False,evidence_class=typ,screening_decision=decision)
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n'for x in pub))
 prior={x['id']:{k:x[k]for k in ['status','design','hasResults']}for x in base['registry']};reg=[]
 interpretations={'NCT07854665':'October 28 update of an October 2 protocol, not yet recruiting, planned 124 ages 6–18, randomized/triple-masked taVNS design, no results. Unchanged selected snapshot; not an adult persistent-severe efficacy finding.','NCT07898592':'New October 27 protocol, not yet recruiting, estimated 50 parents in broad neurodevelopmental supportive-care single-group study; motor tic disorders are one listed condition. No results or Tourette-specific efficacy established.','NCT01019343':'October 26 metadata posting for a historical mixed-movement-disorder basic-science study completed in 2020, actual enrollment 1273 across diagnoses, no results. This is not a new completed trial or 1273 Tourette participants.','NCT07137442':'October 29 posting moves estimated start from November 2 to November 3; planned 75 and no results unchanged. Planned dates do not establish actual recruitment or efficacy.','NCT05158439':'Unchanged withdrawal for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy.','NCT07093541':'Expanded access remains no longer available, unchanged from prior snapshot. No reason, safety cause or efficacy inferred; no results.','NCT06194305':'Pediatric CBIT study remains recruiting without results; selected metadata unchanged.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];assert n in interpretations,'New registry needs review';b=flat({k:x[k]for k in ['status','design','hasResults']});p=flat(prior.get(n,{}));changes=[{'field':k,'previous':p.get(k),'current':b.get(k)}for k in sorted(set(p)|set(b))if p.get(k)!=b.get(k)];assert n in ['NCT07137442'] or not changes,'Changes need review';x.update(id=n,evidence_class='registry_status_control',previous_day_comparison_available=n in prior,selected_field_changes=changes if n in prior else [],comparison_scope='Selected status/design/hasResults versus previous day only; new-to-day record lacks a previous-day snapshot. Not full amendment history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');p['index_path']=p['server']+'-preprint-index.tsv'
  with(out/p['index_path']).open('w')as f:w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  assert not p['matches'],'New lexical hit needs review'
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw.update(request_log_path='request-log.json',scope='Selected public metadata and original summaries only. No source abstracts/full papers, participant rows, contacts or private narratives retained.');write(out/'search-log.json',raw)
 s={'date':'2026-10-30','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'new_to_previous_scan_records':10,'new_to_repository_primary_records':1,'verified_new_primary_publications_since_prior_cutoff':0,'verified_newly_entered_pubmed_since_prior_cutoff':0,'unknown_exact_publication_date_records':0,'preprint_doi_versions':sum(x['unique_doi_versions']for x in raw['preprints']),'preprint_lexical_matches':0,'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry']for i in q.get('response',{}).get('nct_ids',[]))),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error'in x for x in requests),'decision':'Older October 14 pediatric immune/vitamin association newly retrieved, not a new-window first publication or treatment result. One registry planned-start date changed. No new posted trial result or qualifying preprint verified within recorded limits.'};write(out/'summary.json',s);print(json.dumps(s,indent=2))
if __name__=='__main__':main()
