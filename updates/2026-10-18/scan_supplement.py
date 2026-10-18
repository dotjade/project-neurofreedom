#!/usr/bin/env python3
"""Read selected public metadata; never retain abstracts, paper text, case data or contacts.
Live APIs may change. Run: python scan_supplement.py --out PATH
ISRCTN queries use its linked public API specification, version 0.6.
"""
import argparse,datetime as dt,hashlib,json,pathlib,re,urllib.parse,urllib.request,xml.etree.ElementTree as ET
def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='.');a=ap.parse_args();out=pathlib.Path(a.out)
    log={'started_utc':utc(),'requests':[],'registry':[],'isrctn':[],'crossref':[],'coverage':[]}
    def get(url,kind='json'):
        rec={'url':url,'started_utc':utc()};log['requests'].append(rec)
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'}),timeout=40) as r:
                raw=r.read();rec.update(status=r.status,final_url=r.url,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
            value=json.loads(raw) if kind=='json' else ET.fromstring(raw) if kind=='xml' else raw.decode('utf-8',errors='replace')
        except Exception as e:rec['error']=str(e);value=None
        rec['completed_utc']=utc();return value,rec
    for nct in ['NCT07093541','NCT06194305']:
        d,r=get('https://clinicaltrials.gov/api/v2/studies/'+nct)
        if d:
            p=d['protocolSection'];log['registry'].append({'id':nct,'title':p['identificationModule'].get('briefTitle'),'status':p.get('statusModule'),'design':p.get('designModule'),'hasResults':d.get('hasResults'),'request':r})
    d,r=get('https://api.crossref.org/works/10.1111/jpc.70627')
    if d:log['crossref'].append({'request':r,'metadata':{k:d['message'].get(k) for k in ['DOI','title','published','published-online','published-print','created','deposited','indexed','type','relation','update-to','URL']}})
    # Documented public endpoint, bounded sequential requests only.
    for query in ['(Tourette OR tics OR "tic disorder") AND lastEdited GE 2026-10-16T00:00:00 AND lastEdited LT 2026-10-19T00:00:00']:
        url='https://www.isrctn.com/api/query/format/default?'+urllib.parse.urlencode({'q':query,'limit':50})
        d,r=get(url,'xml');entry={'query':query,'limit':50,'request':r}
        if d is not None:
            entry.update(root_tag=d.tag,root_attributes=d.attrib)
            # Retain only machine metadata plus identifiers and selected date/status/title fields.
            allowed={'total','totalResults','resultCount','count','isrctn','ISRCTN','id','title','scientificTitle','publicTitle','lastEdited','dateApplied','recruitmentStatus','trialStatus'}
            entry['selected_nodes']=[{'tag':n.tag,'text':n.text,'attributes':n.attrib} for n in d.iter() if n.tag.rsplit('}',1)[-1] in allowed]
            entry['tag_counts']={tag:sum(n.tag==tag for n in d.iter()) for tag in set(n.tag for n in d.iter())}
        log['isrctn'].append(entry)
    d,r=get('https://trialsearch.who.int/','text')
    entry={'source':'WHO ICTRP landing page','request':r}
    if d:
        entry['title']=(re.findall(r'<title[^>]*>(.*?)</title>',d,re.S|re.I) or [''])[0].strip()
        entry['listed_date_tokens']=sorted(set(re.findall(r'\b\d{1,2}\s+(?:October|September)\s+2026\b',d,re.I)))
        entry['html_received']=True
    log['coverage'].append(entry)
    log['completed_utc']=utc();(out/'supplement-selected-metadata.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log),flush=True)
if __name__=='__main__':main()
