#!/usr/bin/env python3
"""Validate scan accounting, deduplication, retained fields and local deliverable links."""
import ast,datetime as dt,hashlib,json,pathlib,re
p=pathlib.Path(__file__).resolve().parent
load=lambda n:json.loads((p/n).read_text())
r=load('search-log.json');s=load('summary.json');supp=load('supplement-selected-metadata.json');c=load('isrctn-control.json')
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value:raise AssertionError(name)
queries=r['pubmed']['queries'];ids=set(i for q in queries for i in q['ids'])
check('Eight successful PubMed queries',len(queries)==8 and all('count' in q for q in queries))
check('All PubMed result IDs retrieved below cap',all(len(q['ids'])==q['count'] and q['count']<q['params']['retmax'] for q in queries))
check('Twelve occurrences and six unique PubMed IDs',sum(q['count'] for q in queries)==12 and len(ids)==6)
check('Metadata screen matches ID union',ids==set(x['pmid'] for x in r['pubmed']['date_type_correction_screen']))
check('All screening decisions assigned',all('Pending' not in x['screening_decision'] for x in r['pubmed']['date_type_correction_screen']))
check('Only new PubMed ID is explicitly secondary',r['pubmed']['new_to_prior_scan_ids']==['42888480'] and 'Review' in next(x for x in r['pubmed']['date_type_correction_screen'] if x['pmid']=='42888480')['types'])
check('No changed linked notice among overlaps',not any(x['linked_notice_changed'] for x in r['pubmed']['date_type_correction_screen']))
for x in r['preprints']:
    pairs={(y['doi'],y['version']) for y in x['version_index']}
    check(x['server']+' complete unique pagination',x['pagination_complete_for_observed_response'] and len(pairs)==x['total_returned']==x['unique_doi_versions']==x['reported_totals'][0] and len(x['reported_totals'])==1)
    check(x['server']+' no lexical match',not x['matches'])
check('541 DOI/version records',sum(x['unique_doi_versions'] for x in r['preprints'])==541)
check('All direct core requests successful',all(x.get('status')==200 and 'error' not in x for x in r['retrieval_requests']) and not r.get('worker_errors'))
check('CTgov query counts complete',all(q['response']['totalCount']==len(q['response']['nct_ids']) and q['response']['nextPageToken'] is None for q in r['registry']))
check('Three unique CTgov window records',len(r['registry_records'])==3 and all(x['prior_scan_overlap'] for x in r['registry_records']))
regs=[json.loads(l) for l in (p/'registry-evidence.jsonl').read_text().splitlines()]
check('No changed fields in four previously monitored registry records',all(not x['changes'] for x in regs if x['prior_snapshot']))
check('Registry results not inferred',all(x['has_results'] is False and x['new_result'] is False for x in regs))
check('ISRCTN zero bounded result and nonempty positive control',supp['isrctn'][0]['root_attributes']['totalCount']=='0' and c[0]['root_attributes']['totalCount']=='22')
check('Empty new-primary ledger is intentional',(p/'primary-evidence.jsonl').read_text()=='' and s['primary_evidence_additions']==0)
for f in p.glob('*.py'):ast.parse(f.read_text())
check('Python syntax validated',True)
for f in p.glob('*.json'):json.loads(f.read_text())
for f in p.glob('*.jsonl'):
    for line in f.read_text().splitlines():json.loads(line)
check('JSON and JSONL parse',True)
targets=re.findall(r'\]\(([^)]+)\)',(p/'report.md').read_text())
missing=[x for x in targets if not x.startswith('http') and x not in ['validation.json'] and not (p/x).is_file()]
check('All report local links resolve',not missing)
check('No saved raw source documents',not any(f.suffix.lower() in ['.xml','.html','.pdf'] for f in p.iterdir()))
out={'checked_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'checks':checks,'checks_passed':len(checks),'checks_failed':0,'limits':'Accounting and file validation only; not independent scientific review or complete source/history audit.'}
(p/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
files=[]
for f in sorted(p.iterdir()):
    if f.is_file() and f.name!='manifest.json':files.append({'path':f.name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(p/'manifest.json').write_text(json.dumps({'date':'2026-10-18','root_files':files,'baseline_directory':'baseline/ is a local read-only comparison snapshot, not a new research addition.','primary_additions':0},indent=2)+'\n')
print(json.dumps(out,indent=2))
