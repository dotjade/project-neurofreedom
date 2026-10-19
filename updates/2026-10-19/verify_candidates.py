#!/usr/bin/env python3
"""Read public abstracts transiently; retain metadata only, not abstracts or person-level data."""
import urllib.request,xml.etree.ElementTree as E,json,datetime as dt,hashlib,pathlib
out=pathlib.Path(__file__).resolve().parent
log={'requests':[],'pubmed':[],'registry':[]}
def get(url,xml=False):
 r={'url':url,'started_utc':dt.datetime.now(dt.timezone.utc).isoformat()};log['requests'].append(r)
 try:
  with urllib.request.urlopen(url,timeout=45) as f:b=f.read();r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  return E.fromstring(b) if xml else json.loads(b)
 except Exception as e:r['error']=str(e)
 finally:r['completed_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
ids='10382139,11518480,40977255,41621322,41689912,42890800,42890894,42893364'
r=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id='+ids+'&retmode=xml',True)
if r is not None:
 for x in r.findall('PubmedArticle'):
  log['pubmed'].append({'pmid':x.findtext('.//PMID'),'abstract_available':bool(x.findall('.//AbstractText')),'abstract_retained':False,'title':''.join(x.find('.//ArticleTitle').itertext())})
for n in ['NCT05158439','NCT07137442','NCT07839377','NCT07854665','NCT06825520']:
 r=get('https://clinicaltrials.gov/api/v2/studies/'+n)
 if r:
  p=r['protocolSection'];log['registry'].append({'id':n,'title':p['identificationModule'].get('briefTitle'),'status':p.get('statusModule'),'design':p.get('designModule'),'hasResults':r.get('hasResults')})
(out/'candidate-verification.json').write_text(json.dumps(log,indent=2)+'\n')
