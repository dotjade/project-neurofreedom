#!/usr/bin/env python3
"""Transient publisher/metadata checks. Do not persist abstracts or full-text bodies."""
import json,pathlib,re,sys,concurrent.futures
from scan_supplement import get,utc
OUT=pathlib.Path(__file__).resolve().parent

def check(label,url,kind):
 d,r=get(url,kind);x={'label':label,'request':r,'body_retained':False}
 if d is not None:
  if kind=='json':
   m=d.get('message',{});x['selected']={k:m.get(k) for k in ['DOI','title','type','created','published','published-online','published-print','update-to','relation','is-referenced-by-count','license']}
  else:
   x['title']=(re.findall(r'<title[^>]*>(.*?)</title>',d,re.S|re.I) or [''])[0].strip()
   x['metadata']=[{'name':a,'content':b} for a,b in re.findall(r'<meta[^>]*(?:name|property)=[\"\']([^\"\']+)[\"\'][^>]*content=[\"\']([^\"\']*)[\"\']',d,re.I) if re.search(r'citation_(title|doi|date|publication_date|online_date)|dc.date|article:published_time',a,re.I)]
 return x

def main():
 jobs=[('QSM_Crossref','https://api.crossref.org/works/10.3174/ajnr.A9681','json'),('QSM_publisher','https://www.ajnr.org/content/early/2026/10/19/ajnr.A9681','text'),('QSM_DOI','https://doi.org/10.3174/ajnr.A9681','text'),('CTIS_gemlapodect','https://euclinicaltrials.eu/ctis-public/view/2023-505086-83-00','text')]
 out={'started_utc':utc(),'checks':[]}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
  for f in [p.submit(check,*x) for x in jobs]:out['checks'].append(f.result())
 out['completed_utc']=utc();(OUT/'selected-candidate-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
