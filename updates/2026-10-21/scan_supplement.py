#!/usr/bin/env python3
"""Bounded official-source checks; save metadata, never abstracts or contact fields."""
import concurrent.futures, datetime as dt, hashlib, json, pathlib, re
import urllib.parse, urllib.request, xml.etree.ElementTree as E
OUT=pathlib.Path(__file__).resolve().parent
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def get(url,kind='json'):
    r={'url':url,'started_utc':utc()};value=None
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'})
        with urllib.request.urlopen(req,timeout=20) as f:
            b=f.read();r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
        value=json.loads(b) if kind=='json' else E.fromstring(b) if kind=='xml' else b.decode(errors='replace')
    except Exception as e:r['error']=str(e)
    r['completed_utc']=utc()
    return value,r
def registry(nct):
    d,r=get('https://clinicaltrials.gov/api/v2/studies/'+nct)
    item={'id':nct,'request':r}
    if d:
        p=d['protocolSection'];item.update(title=p['identificationModule'].get('briefTitle'),status=p.get('statusModule'),design=p.get('designModule'),hasResults=d.get('hasResults'))
    return item
def isrctn(label,query=None):
    url=('https://www.isrctn.com/api/query/format/default?'+urllib.parse.urlencode({'q':query,'limit':50 if label=='window' else 1})) if query else 'https://www.isrctn.com/api/trial/ISRCTN14910154/format/default'
    d,r=get(url,'xml');item={'label':label,'query':query,'request':r}
    if d is not None:
        item.update(root_tag=d.tag,root_attributes=d.attrib)
        allowed={'totalCount','isrctn','title','scientificTitle','publicTitle','lastEdited','recruitmentStatus','trialStatus','dateAssigned','dateUpdated'}
        item['selected_nodes']=[{'tag':n.tag,'text':n.text,'attributes':n.attrib} for n in d.iter() if n.tag.rsplit('}',1)[-1] in allowed and (n.text or '').strip() not in ['Dr','Prof','Mrs','Mr','Ms']]
    return item
def who():
    d,r=get('https://trialsearch.who.int/','text')
    item={'source':'WHO ICTRP landing page','request':r,'query_export_obtained':False}
    if d:item.update(title=(re.findall(r'<title[^>]*>(.*?)</title>',d,re.S|re.I) or [''])[0].strip(),listed_date_tokens=sorted(set(re.findall(r'\b\d{1,2}\s+(?:October|September)\s+2026\b',d,re.I))))
    return item
def main():
    log={'started_utc':utc()}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs={n:pool.submit(registry,n) for n in ['NCT05158439','NCT07093541','NCT06194305','NCT07137442']}
        jobs['isrctn_window']=pool.submit(isrctn,'window','(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-19T00:00:00 AND lastEdited LT 2026-10-22T00:00:00')
        jobs['isrctn_positive_control']=pool.submit(isrctn,'positive_control','Tourette')
        jobs['isrctn_direct_control']=pool.submit(isrctn,'direct_control')
        jobs['who']=pool.submit(who)
        # Candidate abstract review is a separate transient step after metadata screening.
        for key,f in jobs.items():
            try:log[key]=f.result()
            except Exception as e:log[key]={'error':str(e)}
    log['completed_utc']=utc()
    (OUT/'supplement-selected-metadata.json').write_text(json.dumps(log,indent=2)+'\n')
    print('SAVED',OUT/'supplement-selected-metadata.json',flush=True)
if __name__=='__main__':main()
