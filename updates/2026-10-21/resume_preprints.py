#!/usr/bin/env python3
"""Resume incomplete feeds once with longer timeout; metadata retained, abstracts transient."""
import json,pathlib,urllib.request,datetime as dt,hashlib,re,concurrent.futures,time
OUT=pathlib.Path(__file__).resolve().parent
utc=lambda:dt.datetime.now(dt.timezone.utc).isoformat()
def main():
 prior=json.loads((OUT/'preprint-search-log.json').read_text());logs={'started_utc':utc(),'input':'preprint-search-log.json','retrieval_requests':[],'preprints':[]}
 baseline=json.loads((OUT/'baseline-metadata.json').read_text())
 def run(s):
  d=next(x for x in prior['preprints'] if x['server']==s);cursor=d['total_returned'];regex=re.compile(d['screen_regex'],re.I)
  while not d['pagination_complete_for_observed_response']:
   url=f'https://api.biorxiv.org/details/{s}/2026-10-19/2026-10-21/{cursor}';data=None
   for attempt in range(1,4):
    rec={'url':url,'started_utc':utc(),'attempt':attempt,'timeout_seconds':60}
    try:
     with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as r:
      raw=r.read();rec.update(status=r.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest());data=json.loads(raw)
    except Exception as e:rec['error']=str(e)
    rec['completed_utc']=utc();logs['retrieval_requests'].append(rec)
    if data is not None:break
    time.sleep(1)
   if data is None:break
   coll=data.get('collection',[]);msg=data.get('messages',[{}])[0];d['pages'].append({'cursor':cursor,'returned':len(coll),'message':msg})
   for x in coll:
    d['version_index'].append({k:x.get(k) for k in ['doi','version','date']})
    if regex.search(x.get('title','')+' '+x.get('abstract','')):d['matches'].append({k:x.get(k) for k in ['doi','version','date','title','category','published']})
   total=int(msg.get('total',0));cursor+=len(coll)
   if not coll or cursor>=total:d['pagination_complete_for_observed_response']=True
  current={(x['doi'],x['version']) for x in d['version_index']};old={(x['doi'],x['version']) for x in next(x for x in baseline['preprints'] if x['server']==s)['version_index']}
  d.update(total_returned=len(d['version_index']),unique_doi_versions=len(current),previous_scan_overlap_doi_versions=len(current&old),not_in_previous_scan_doi_versions=len(current-old),reported_totals=sorted(set(int(x['message'].get('total',0)) for x in d['pages'])))
  return d
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:
  for d in p.map(run,['biorxiv','medrxiv']):logs['preprints'].append(d);print(json.dumps({k:v for k,v in d.items() if k not in ['pages','version_index']}),flush=True)
 logs['completed_utc']=utc();(OUT/'preprint-resume-log.json').write_text(json.dumps(logs,indent=2)+'\n')
if __name__=='__main__':main()
