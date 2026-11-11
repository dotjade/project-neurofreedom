import urllib.request,urllib.parse,json,datetime,hashlib,pathlib,xml.etree.ElementTree as ET
import argparse
ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(pathlib.Path(__file__).resolve().parent));args=ap.parse_args()
out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
records=[]
fields='NCTId,BriefTitle,StatusModule,DesignModule,Condition,MinimumAge,MaximumAge,StdAge,HasResults'
for id in ['NCT07839377','NCT06825520','NCT05942716','NCT05558566','NCT06909656','NCT07854665']:
 u='https://clinicaltrials.gov/api/v2/studies/'+id+'?'+urllib.parse.urlencode({'fields':fields});rec={'nctId':id,'url':u,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(u,timeout=45);raw=r.read();d=json.loads(raw);rec.update(http_status=r.status,sha256=hashlib.sha256(raw).hexdigest(),record=d)
 except Exception as e:rec['error']=str(e)
 rec['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();records.append(rec)
(out/'supplement-registry.json').write_text(json.dumps(records,indent=2)+'\n')
u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42767894&retmode=xml';r=urllib.request.urlopen(u,timeout=45);raw=r.read();d=ET.fromstring(raw)
a=d.find('PubmedArticle');m=a.find('MedlineCitation');p=a.find('PubmedData');art=m.find('Article')
rec={'url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(raw).hexdigest(),'pmid':m.findtext('PMID'),'title':''.join(art.find('ArticleTitle').itertext()),'types':[x.text for x in art.findall('PublicationTypeList/PublicationType')],'identifiers':{x.attrib.get('IdType'):x.text for x in p.findall('ArticleIdList/ArticleId')},'article_dates':[dict(type=x.attrib.get('DateType'),**{c.tag:c.text for c in x}) for x in art.findall('ArticleDate')],'corrections':[dict(type=x.attrib.get('RefType'),pmid=x.findtext('PMID')) for x in m.findall('CommentsCorrectionsList/CommentsCorrections')]}
(out/'historical-correction-check.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps({'registry':[(x['nctId'],x.get('record',{}).get('protocolSection',{}).get('statusModule'),x.get('record',{}).get('hasResults')) for x in records],'correction':rec},indent=2))
