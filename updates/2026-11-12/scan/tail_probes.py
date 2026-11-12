#!/usr/bin/env python3
"""Two bounded latest-page metadata probes after first-page samples proved baseline overlaps."""
import argparse,datetime,hashlib,json,pathlib,re,subprocess,concurrent.futures
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
ap=argparse.ArgumentParser();ap.add_argument('--baseline',required=True);ap.add_argument('--out',default='.');a=ap.parse_args();p=pathlib.Path(a.out);scan=json.loads((p/'scan.json').read_text());base=json.loads(pathlib.Path(a.baseline).read_text());regex=re.compile(r'\btourett\w*|\btics?\b',re.I)
def one(server):
 src=scan['preprints'][server];total=int(src['pages'][-1]['total']);cursor=max(0,total-30);url=f'https://api.biorxiv.org/details/{server}/2026-11-08/2026-11-12/{cursor}'
 r={'server':server,'url':url,'started_utc':utc(),'reason':'First bounded pages were all prior-index overlaps; inspect final observed page for later versions. This remains a partial non-contiguous sample.','cursor':cursor}
 q=subprocess.run(['curl','-fLsS','--max-time','18',url],capture_output=True,timeout=22);r.update(completed_utc=utc(),exit_code=q.returncode)
 if q.returncode:r['error']=q.stderr.decode(errors='replace')[:300];return r
 r['sha256']=hashlib.sha256(q.stdout).hexdigest();d=json.loads(q.stdout);r['reported_total']=d.get('messages',[{}])[0].get('total');r['index']=[];r['matches']=[]
 for z in d.get('collection',[]):
  r['index'].append([z.get('doi'),z.get('version'),z.get('date')])
  if regex.search(z.get('title','')+' '+z.get('abstract','')):r['matches'].append({k:z.get(k) for k in ['doi','version','date','title']})
 prior={tuple([z['doi'],z['version']]) for z in next(x for x in base['preprints'] if x['server']==server)['version_index']}
 r['previous_overlap']=len({tuple(z[:2]) for z in r['index']}&prior);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:rs=list(e.map(one,['medrxiv','biorxiv']))
(p/'tail-probes.json').write_text(json.dumps(rs,separators=(',',':'))+'\n')
print(json.dumps([{k:v for k,v in r.items() if k!='index'} for r in rs],indent=2))

