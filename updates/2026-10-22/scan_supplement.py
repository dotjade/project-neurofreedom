#!/usr/bin/env python3
"""Bounded official registry supplements. Retain only selected public metadata."""
import concurrent.futures,datetime as dt,hashlib,json,pathlib,re,urllib.parse,urllib.request,xml.etree.ElementTree as E
OUT=pathlib.Path(__file__).resolve().parent
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def get(url,kind='xml'):
 rec={'url':url,'started_utc':utc()};data=None
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=60) as f:b=f.read();rec.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  data=E.fromstring(b) if kind=='xml' else b.decode(errors='replace')
 except Exception as e:rec['error']=str(e)
 rec['completed_utc']=utc();return data,rec
def isrctn(label,query):
 u='https://www.isrctn.com/api/query/format/default?'+urllib.parse.urlencode({'q':query,'limit':50 if label=='window' else 1});d,r=get(u);out={'query':query,'request':r}
 if d is not None:
  allowed={'totalCount','isrctn','scientificTitle','publicTitle','lastEdited','recruitmentStatus','trialStatus','dateAssigned','dateUpdated'}
  out.update(root_tag=d.tag,root_attributes=d.attrib,selected_nodes=[{'tag':n.tag,'text':n.text,'attributes':n.attrib} for n in d.iter() if n.tag.rsplit('}',1)[-1] in allowed])
 return label,out
def who():
 d,r=get('https://trialsearch.who.int/','text');o={'request':r,'query_export_obtained':False}
 if d:o['listed_date_tokens']=sorted(set(re.findall(r'\b\d{1,2}\s+(?:October|September)\s+2026\b',d,re.I)))
 return 'who_ictrp',o
def ctis():
 d,r=get('https://euclinicaltrials.eu/ctis-public/view/2023-505086-83-00','text');return 'ctis',{'request':r,'parsed_trial_record':False,'interpretation':'HTML application shell retrieval does not establish current trial status.'}
def main():
 log={'started_utc':utc()}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
  fs=[p.submit(isrctn,'window','(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-20T00:00:00 AND lastEdited LT 2026-10-23T00:00:00'),p.submit(isrctn,'positive_control','Tourette'),p.submit(who),p.submit(ctis)]
  for f in fs:k,v=f.result();log[k]=v
 log['completed_utc']=utc();(OUT/'supplement-selected-metadata.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log,indent=2))
if __name__=='__main__':main()
