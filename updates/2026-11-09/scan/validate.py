#!/usr/bin/env python3
"""Offline bookkeeping checks; not independent scientific review."""
import csv,hashlib,json,pathlib,re
p=pathlib.Path(__file__).resolve().parent;checks=[]
def ck(name,value):checks.append({'check':name,'passed':bool(value)});assert value,name
def read(name):return json.loads((p/name).read_text())
s=read('summary.json');j=read('search-log.json');r=read('preprint-recovery.json');b=read('baseline.json')
rows=[json.loads(x) for x in (p/'pubmed-screening.jsonl').read_text().splitlines()]
ck('35 unique query records',len(rows)==len({x['pmid'] for x in rows})==35)
ck('40 id occurrences',sum(q['count'] for q in j['pubmed']['queries'])==40)
ck('query ID union matches metadata',set().union(*(set(q['ids']) for q in j['pubmed']['queries']))=={x['pmid'] for x in rows})
for q in j['pubmed']['queries']:ck(q['label']+' no truncation',q['count']==len(q['ids'])<int(q['params']['retmax']))
ck('all screening complete',all('Pending' not in x['screening_decision'] for x in rows))
ck('no new primary additions',not any(x['new_primary_evidence'] for x in rows) and s['new_primary_evidence_records_proposed']==0)
ck('historical classes accounted',sum(x['screening_class']=='historical metadata update' for x in rows)==29)
ck('date intervals',j['inclusive_overlap']==['2026-11-07','2026-11-09'])
ck('cutoff matches baseline',s['prior_core_cutoff_utc']==b['cutoff_utc'])
total=0
for x in s['preprints']:
 v=list(csv.DictReader((p/(x['server']+'-preprint-index.tsv')).open(),delimiter='\t'));keys={(y['doi'],y['version']) for y in v};total+=len(keys)
 ck(x['server']+' unique index',len(keys)==len(v)==x['unique_doi_versions'])
 ck(x['server']+' stable total',x['reported_totals']==[len(v)])
 ck(x['server']+' complete',x['pagination_complete_for_observed_response'])
 ck(x['server']+' overlap accounting',x['previous_scan_overlap_doi_versions']+x['not_in_previous_scan_doi_versions']==len(v))
 ck(x['server']+' no lexical match',x['matches']==[])
 ck(x['server']+' date bounds',all('2026-11-06'<=y['date']<='2026-11-09' for y in v))
ck('485 versions',total==s['preprint_versions']==485)
rx=re.compile(r'\btourett\w*|\btics?\b',re.I);ck('lexical positive controls',all(rx.search(x) for x in ['Tourette syndrome','chronic motor tics','tic disorder']));ck('lexical negative control',not rx.search('statistics'))
ck('single 503 retained',len(s['initial_failed_requests'])==1 and '503' in s['initial_failed_requests'][0]['error'])
ck('recovered same failed page',r['requests'][0]['url']==s['initial_failed_requests'][0]['url'] and r['requests'][0]['status']==200)
ck('recovery complete without error',r['complete'] and all(x.get('status')==200 for x in r['requests']))
ck('39 core and recovery requests',len(read('request-log.json'))==36+3)
regs=[json.loads(x) for x in (p/'registry-evidence.jsonl').read_text().splitlines()]
ck('seven comparable registry watches',len(regs)==7 and all(x['prior_scan_overlap'] for x in regs))
for x in regs:ck(x['nctId']+' unchanged/no results',x['hasResults'] is False and x['selected_field_changes']==[])
ck('four window queries zero',len(j['registry'])==4 and all(x['response']['totalCount']==0 and not x['response'].get('nextPageToken') for x in j['registry']))
sup=read('supplement-registry.json');ck('eighth registry historical/no results',sup['status']==200 and sup['snapshot']['hasResults'] is False and sup['snapshot']['protocolSection']['statusModule']['studyFirstPostDateStruct']['date']=='2026-09-24')
pm=read('supplement-pubmed.json');ck('directed paper old and unchanged',pm['metadata']['pmid']=='42947547' and pm['metadata']['linked_notices']==[] and pm['sha256']=='f5a23a7c589c386419d937ca8cdab30bb8ba46916391b103fb1c6698ff71365a')
ck('36 distinct PubMed IDs',s['distinct_pubmed_ids_including_directed']==len({x['pmid'] for x in rows}|{pm['metadata']['pmid']}))
ck('eight source hashes verified',len(read('baseline-verification.json')['sources'])==8 and all(x['match'] for x in read('baseline-verification.json')['sources']))
ck('four safety queries/nine pages',len(read('safety-query-log.json')['queries'])==4 and len(read('safety-review.json')['sources'])==9)
ck('no positive safety assertion',read('safety-review.json')['new_watched_treatment_warning_verified'] is False)
ck('sensory supplement unavailable not inferred',read('incidental-sensory-check.json')['participant_files_accessed'] is False and '403' in read('incidental-sensory-check.json')['access_result'])
(p/'validation.json').write_text(json.dumps({'passed':len(checks),'failed':0,'scope':'Offline accounting and source consistency; not independent clinical/scientific validation.','checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
