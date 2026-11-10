import json,csv,pathlib,hashlib
p=pathlib.Path(__file__).parent
d=json.loads((p/'search-log.json').read_text());base=json.loads((p/'baseline.json').read_text())
rows=d['pubmed']['date_type_correction_screen']
for x in rows:
 y=int((x.get('article_dates') or [x.get('journal_pubdate') or {}])[0].get('Year',0))
 if x['pmid'] in ['42995839','42997792','42997938']:why='Unrelated acronym match, not tic-disorder evidence.'
 elif x['pmid']=='42996864':why='Historical pediatric NLRP3 review, electronic publication October 23, already screened November 9; not new primary evidence.'
 elif x['pmid']=='42997457':why='Historical broad cannabis systematic review/meta-analysis, electronic publication October 29, already screened November 9; not a new tic trial.'
 elif y<2026:why='Historical publication retrieved by metadata modification; not a new scientific finding.'
 else:why='Needs review'
 x['screening_decision']=why
(p/'pubmed-screening.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
regs=[]
for x in d['registry_records']:
 old=next(z for z in base['registry'] if z['id']==x['nctId']);x['selected_field_changes']=[k for k in ['title','status','hasResults','conditions','design','eligibility'] if x.get(k)!=old.get(k)];regs.append(x)
(p/'registry-evidence.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in regs))
pp=[]
for x in d['preprints']:
 old=list(csv.DictReader((p/('prior-'+x['server']+'-preprint-index.tsv')).open(),delimiter='\t'));prev={(z['doi'],str(z['version'])) for z in old};cur={(z['doi'],str(z['version'])) for z in x['version_index']};x['corrected_previous_overlap']=len(cur&prev);x['corrected_not_in_prior_index']=len(cur-prev)
 pp.append({k:v for k,v in x.items() if k not in ['version_index','pages']})
 with (p/(x['server']+'-preprint-index.tsv')).open('w') as f:
  w=csv.DictWriter(f,fieldnames=['doi','version','date'],delimiter='\t');w.writeheader();w.writerows(x['version_index'])
summary={'started_utc':d['started_utc'],'completed_utc':d['completed_utc'],'query_counts':[(x['label'],x.get('count')) for x in d['pubmed']['queries']],'unique_pubmed_records':len(rows),'preprints':pp,'registry_query_results':d['registry'],'watched_registry_changes':{x['nctId']:x['selected_field_changes'] for x in regs},'request_errors':[x for x in d['retrieval_requests'] if 'error'in x],'worker_errors':d.get('worker_errors',[]),'remaining_screening':[x['pmid'] for x in rows if x['screening_decision']=='Needs review']}
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
