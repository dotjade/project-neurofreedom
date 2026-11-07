"""Resume the two failed API cursors once, retaining failures and exact provenance."""
import concurrent.futures,datetime as dt,hashlib,json,pathlib,re,time,urllib.request
P=pathlib.Path(__file__).parent
s=json.loads((P/'search-log.json').read_text());b=json.loads((P/'baseline.json').read_text());pat=re.compile(r'\btourett\w*|\btics?\b',re.I)
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def run(d):
 cursor=d['total_returned'];prev={(x['doi'],x['version']) for x in b['preprints'][d['server']]}
 while not d['pagination_complete_for_observed_response']:
  url=f"https://api.biorxiv.org/details/{d['server']}/2026-11-04/2026-11-07/{cursor}";r={'url':url,'started_utc':utc(),'resume_after_transient_503':True}
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as q: raw=q.read();r.update(status=q.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
   data=json.loads(raw)
  except Exception as e:r['error']=str(e);data=None
  r['completed_utc']=utc();s['retrieval_requests'].append(r)
  if not data:break
  coll=data.get('collection',[]);msg=data.get('messages',[{}])[0];d['pages'].append({'cursor':cursor,'returned':len(coll),'message':msg})
  for x in coll:
   d['version_index'].append({k:x.get(k) for k in ('doi','version','date')})
   if pat.search(x.get('title','')+' '+x.get('abstract','')):
    d['matches'].append({k:x.get(k) for k in ('doi','version','date','title','category','published')});print('MATCH',d['server'],x['doi'],x.get('title'),flush=True)
  total=int(msg.get('total',0))
  if not coll or cursor+len(coll)>=total:d['pagination_complete_for_observed_response']=True;break
  cursor+=len(coll)
 seen={(x['doi'],x['version']) for x in d['version_index']}
 d.update(total_returned=len(d['version_index']),unique_doi_versions=len(seen),previous_scan_overlap_doi_versions=len(seen&prev),not_in_previous_scan_doi_versions=len(seen-prev),reported_totals=sorted(set(int(x['message'].get('total',0)) for x in d['pages'])))
 print('DONE',d['server'],d['total_returned'],d['pagination_complete_for_observed_response'],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(run,s['preprints']))
s['initial_core_completed_utc']=s['completed_utc'];s['completed_utc']=utc();s['retrieval_requests'].sort(key=lambda x:x['started_utc']);(P/'search-log.json').write_text(json.dumps(s,indent=2)+'\n')
