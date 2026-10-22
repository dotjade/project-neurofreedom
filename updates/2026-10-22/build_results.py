#!/usr/bin/env python3
"""Normalize the recorded scan and append original screening decisions.
python build_results.py --raw RAW_SCAN --repo BASE_CHECKOUT --out DIR
RAW_SCAN is temporary output of scan_sources.py. Only selected public metadata is retained.
"""
import argparse,csv,hashlib,json,pathlib
from prepare_baseline import build

def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def flat(x,p=''):
 out={}
 if isinstance(x,dict):
  for k,v in x.items():out.update(flat(v,p+'.'+k if p else k))
 else:out[p]=x
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();out=pathlib.Path(args.out);raw=json.loads(pathlib.Path(args.raw).read_text());base=build(pathlib.Path(args.repo))
 decisions={
 '39947542':('historical_retracted_preclinical','February 2025 preclinical paper, previously excluded on October 17. October 21 metadata revision does not rehabilitate its claims. Retraction link remains explicit. Exclude from positive mechanism/efficacy evidence.'),
 '42527169':('historical_retraction_notice','July 29 electronic retraction notice with October issue date, previously encountered October 17. October 21 revision is not a new retraction. No reason for retraction independently verified.'),
 '41220182':('historical_preclinical_overlap','November 2025 rat-model intervention study screened October 21. October 20 metadata revision is not a new clinical/preclinical result. Animal stereotypy cannot establish human efficacy.'),
 '41794658':('historical_secondary_overlap','March 7 scoping review of functional-tic comorbidity, already screened October 21. Functional tic-like presentations remain distinct from primary chronic tic disorders. No new primary outcome.')}
 pub=raw['pubmed'].pop('date_type_correction_screen');prior_int={x['pmid']:x for x in base['historical_integrity']};integrity=[]
 for x in pub:
  typ,decision=decisions[x['pmid']];x.update(evidence_class=typ,screening_decision=decision,new_qualifying_primary_tic_result=False,abstract_retained=False)
  if x['pmid'] in prior_int:
   old=prior_int[x['pmid']];x['historical_repository_overlap']=True
   delta={k:{'previous':old.get(k),'current':x.get(k)} for k in ['types','corrections','DateRevised'] if old.get(k)!=x.get(k)}
   integrity.append({'id':x['pmid'],'source_url':x['source_url'],'compared_to':'updates/2026-10-18/search-log.json','selected_metadata_changes':delta,'interpretation':'Duplicate erratum cross-links no longer returned; notice is Journal Article plus Retraction Notice rather than Published Erratum plus Retraction Notice. RetractionIn/RetractionOf remain. This is changed metadata, not a new retraction or reinstatement.','new_notice':False})
 (out/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in pub));write(out/'integrity-recheck.json',integrity)
 prior={x['id']:x['current'] for x in base['registry']};reg=[]
 interpretations={'NCT07137442':'Estimated start October 25 to October 26, posting October 20 to October 21, submission October 19 to October 20. Recruiting, observational design, planned enrollment 75 and no-results flag unchanged. No recruitment event or treatment result established.','NCT05158439':'Withdrawn for inability to recruit, actual enrollment zero, no results. Negative feasibility, not negative efficacy or evidence of cell administration.','NCT07093541':'Expanded access remains temporarily unavailable; no results. No new suspension or reason inferred.','NCT06194305':'Pediatric CBIT study remains recruiting with no results. Selected metadata unchanged, not a new treatment result.'}
 for x in raw.pop('registry_records'):
  n=x['nctId'];new={k:x[k] for k in ['status','design','hasResults']};a,b=flat(prior[n]),flat(new);changes=[{'field':k,'previous':a.get(k),'current':b.get(k)} for k in sorted(set(a)|set(b)) if a.get(k)!=b.get(k)]
  x.update(id=n,evidence_class='registry_protocol_update_without_results' if changes else 'registry_status_control',selected_field_changes=changes,comparison_scope='Selected status/design/hasResults fields only; not a full version history.',interpretation=interpretations[n]);reg.append(x)
 (out/'registry-evidence.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in reg))
 for p in raw['preprints']:
  idx=p.pop('version_index');s=p['server'];p['index_path']=s+'-preprint-index.tsv'
  with (out/p['index_path']).open('w') as f:
   w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(idx)
  for m in p['matches']:m.update(screening_decision='Excluded lexical false positive: TICs means thermodynamically infeasible cycles in prostate-cancer metabolic modeling, not tics/Tourette syndrome.',qualifying_tic_result=False)
 requests=raw.pop('retrieval_requests');write(out/'request-log.json',requests);raw['request_log_path']='request-log.json';raw['scope']='Public selected metadata only. No full abstracts, full papers, individual measurements, contacts or community narratives retained.';write(out/'search-log.json',raw)
 (out/'primary-evidence.jsonl').write_text('')
 summary={'date':'2026-10-22','strict_prior_cutoff_utc':base['cutoff_utc'],'core_started_utc':raw['started_utc'],'core_completed_utc':raw['completed_utc'],'pubmed_unique_records':len(pub),'pubmed_id_occurrences':raw['pubmed']['id_occurrences'],'pubmed_previous_day_overlap':raw['pubmed']['previous_overlap_count'],'pubmed_historical_repository_overlap':4,'new_qualifying_primary_tic_results':0,'preprint_doi_versions':sum(x['unique_doi_versions'] for x in raw['preprints']),'preprint_lexical_matches':sum(len(x['matches']) for x in raw['preprints']),'qualifying_preprints':0,'registry_update_window_unique_ids':sorted(set(i for q in raw['registry'] for i in q['response']['nct_ids'])),'new_posted_trial_results':0,'new_retractions':0,'api_request_errors':sum('error' in x for x in requests),'decision':'No new-window result changes the separately scoped Okun 2024 clinical/function estimand audit. Preserve the historical retraction exclusion and unchanged negative registry evidence.'};write(out/'summary.json',summary)
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
