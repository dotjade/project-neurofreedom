#!/usr/bin/env python3
"""Offline metadata review, consistency checks and publication hashes. No network calls."""
import pathlib,json,hashlib,re,datetime
p=pathlib.Path(__file__).resolve().parent
x=json.loads((p/'scan.json').read_text());tails=json.loads((p/'tail-probes.json').read_text())
decisions={}
for r in x['pubmed']['records']:
 pid=r['pmid']
 if pid in ['41678466','41818248','42889785','43008481']:d='Unrelated lexical/acronym hit; not tic evidence.'
 elif pid=='43014332':d='New-window secondary OCD systematic review/network meta-analysis; no new primary tic experiment or verified TS-subgroup benefit.'
 elif pid in ['38688785','42667351']:d='Historical secondary synthesis; not new primary evidence.'
 elif pid=='41830597':d='Historical qualitative functional-tic study; distinct from neurodevelopmental TS.'
 elif pid=='39177336':d='Historical diagnosis-policy study; not a tic-treatment result.'
 else:d='Historical primary publication; electronic date before surveillance window.'
 decisions[pid]=d
review={'checked_date_utc':'2026-11-12','decisions':decisions,'new_primary_evidence_addition':False,'gate_reopening_input_verified':False,'new_secondary_context':['43014332'],'scope_note':'Date/type/abstract screening only; older full texts not resynthesized.'}
(p/'review.json').write_text(json.dumps(review,indent=2)+'\n')
checks=[]
def ck(n,v):checks.append({'check':n,'pass':bool(v)})
ck('13 unique metadata IDs and screening decisions',len(x['pubmed']['records'])==13==len(decisions)==len(set(x['pubmed']['unique_ids'])))
ck('PubMed main query fully retrieved',x['pubmed']['queries'][0]['count']==len(x['pubmed']['records']))
ck('Core query/refinement IDs deduplicated',set(x['pubmed']['unique_ids'])==set().union(*(set(q.get('ids',[])) for q in x['pubmed']['queries'])))
ck('Core 20 requests succeeded',len(x['requests'])==20 and all(r['exit_code']==0 for r in x['requests']))
ck('Core worker errors absent',not x.get('errors'))
ck('Ten unique CT snapshots',len({r['nctId'] for r in x['registry']['records']})==10)
ck('Seven watched selected-field comparisons unchanged',len(x['registry']['selected_field_diffs'])==7 and not any(x['registry']['selected_field_diffs'].values()))
ck('Registry date query fully paginated',not x['registry']['query'].get('nextPageToken'))
counts={}
for server in ['medrxiv','biorxiv']:
 a=x['preprints'][server];b=next(r for r in tails if r['server']==server);rows=a['index']+b.get('index',[]);u={tuple(r[:2]) for r in rows};tot=int(a['pages'][-1]['total'])
 counts[server]={'inspected_unique_versions':len(u),'reported_total':tot,'uninspected_versions':tot-len(u),'matches':a['matches']+b.get('matches',[]),'complete':False,'tail_exit_code':b['exit_code']}
 ck(server+' unique inspected versions',len(u)==len(rows))
 ck(server+' declared incomplete',len(u)<tot and not a['complete'])
ck('bioRxiv tail timeout preserved',counts['biorxiv']['tail_exit_code']==28)
ck('Lexical positive/negative controls',bool(re.search(r'\btourett\w*|\btics?\b','TOURETTE and chronic tics',re.I)) and not re.search(r'\btourett\w*|\btics?\b','statistics',re.I))
summary={'date':'2026-11-12','edition':'Fresh bounded rebuild after local archive loss','prior_cutoff_utc':x['prior_cutoff_utc'],'core_started_utc':x['started_utc'],'core_completed_utc':x['completed_utc'],'last_source_attempt_utc':max(z['completed_utc'] for z in tails),'pubmed_unique_records':13,'new_secondary_context_pmid':'43014332','new_qualifying_primary':0,'registry_unique_records':10,'watched_registry_changes':0,'new_trial_result_verified':False,'new_window_warning_verified':False,'preprints':counts,'gate_reopened':False}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(p/'validation.json').write_text(json.dumps({'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Saved metadata and honest partial-coverage consistency, not complete surveillance or clinical validation.','checks':checks,'all_pass':all(c['pass'] for c in checks)},indent=2)+'\n')
names=['scan.py','scan.json','tail_probes.py','tail-probes.json','discovery-access.json','web-sources.json','review_validate.py','review.json','summary.json','validation.json','report.md']
rows=[]
for name in names:
 b=(p/name).read_bytes();assert (b'/' + b'workspace' + b'/') not in b and (b'/' + b'tmp' + b'/') not in b,name
 rows.append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
obj={'allowlist':rows,'excluded':['run.log','baseline sources','raw responses','full abstracts'],'payload_bytes':sum(r['bytes'] for r in rows)}
(p/'allowlist.json').write_text(json.dumps(obj,indent=2)+'\n')
total=sum(r['bytes'] for r in rows)+(p/'allowlist.json').stat().st_size
assert total<=80000,total
print(json.dumps({'checks':len(checks),'all_pass':all(c['pass'] for c in checks),'package_bytes_including_allowlist':total,'summary':summary},indent=2))

