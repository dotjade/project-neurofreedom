"""Resume failed public metadata pagination once after transient HTTP503; preserve initial request."""
import datetime as dt,hashlib,json,pathlib,re,urllib.request
p=pathlib.Path(__file__).resolve().parent;s=json.loads((p/'search-log.json').read_text());b=json.loads((p/'baseline.json').read_text());x=next(x for x in s['preprints'] if x['server']=='medrxiv');regex=re.compile(x['screen_regex'],re.I)
if x['pagination_complete_for_observed_response']:
 print('Pagination already complete; no requests or files changed.');raise SystemExit(0)
while not x['pagination_complete_for_observed_response']:
 cursor=len(x['version_index']);u=f'https://api.biorxiv.org/details/medrxiv/2026-11-01/2026-11-04/{cursor}';r={'url':u,'started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'retry_reason':'Resume after transient HTTP503, no access denial'}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as resp:raw=resp.read();r.update(status=resp.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  d=json.loads(raw);coll=d.get('collection',[]);msg=d.get('messages',[{}])[0];x['pages'].append({'cursor':cursor,'returned':len(coll),'message':msg})
  for item in coll:
   x['version_index'].append({k:item.get(k)for k in ['doi','version','date']})
   if regex.search(item.get('title','')+' '+item.get('abstract','')):x['matches'].append({k:item.get(k)for k in ['doi','version','date','title','category','published']})
  if not coll or cursor+len(coll)>=int(msg.get('total',0)):x['pagination_complete_for_observed_response']=True
 except Exception as e:r['error']=str(e)
 r['completed_utc']=dt.datetime.now(dt.timezone.utc).isoformat();s['retrieval_requests'].append(r)
 if 'error'in r:break
seen={(a['doi'],a['version'])for a in x['version_index']};prev={(a['doi'],a['version'])for a in b['preprints']['medrxiv']};x.update(total_returned=len(x['version_index']),unique_doi_versions=len(seen),previous_scan_overlap_doi_versions=len(seen&prev),not_in_previous_scan_doi_versions=len(seen-prev),reported_totals=sorted(set(int(a['message'].get('total',0))for a in x['pages'])));s['initial_core_completed_utc']=s['completed_utc'];s['completed_utc']=dt.datetime.now(dt.timezone.utc).isoformat();(p/'search-log.json').write_text(json.dumps(s,indent=2)+'\n');print({k:v for k,v in x.items()if k not in ['version_index','pages']})
