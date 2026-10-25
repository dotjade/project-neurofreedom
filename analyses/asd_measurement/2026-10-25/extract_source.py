#!/usr/bin/env python3
"""Read primary XML transiently; retain selected aggregate facts, never the paper or individuals."""
import datetime as dt, hashlib,json,pathlib,urllib.request,xml.etree.ElementTree as E
P=pathlib.Path(__file__).resolve().parent
URL='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13683974&retmode=xml'
def text(e):return ' '.join(''.join(e.itertext()).split()) if e is not None else ''
def main():
 start=dt.datetime.now(dt.timezone.utc).isoformat()
 with urllib.request.urlopen(URL,timeout=60) as f:b=f.read();status=f.status
 root=E.fromstring(b);a=root.find('.//article');m=a.find('front/article-meta')
 ids={x.attrib.get('pub-id-type'):text(x) for x in m.findall('article-id')};assert ids['doi']=='10.1002/mdc3.70882'
 tables={text(t.find('label')):t for t in a.findall('.//table-wrap')}
 selected={}
 wanted={'Participants','Age at time of enrolment (years)','Level 1','Level 2','Level 3','Total tic score','Impairment','Global score','Autism spectrum disorder','Age at enrollment'}
 for name,t in tables.items():
  if name=='TABLE 4':continue
  rows=[]
  for tr in t.findall('.//tr'):
   cs=[text(c) for c in list(tr) if c.tag in ['td','th']]
   if cs and cs[0] in wanted:rows.append(cs)
  selected[name]=rows
 inputs={'study':{'pmid':'42902960','pmc':'PMC13683974','doi':ids['doi'],'published':'2026-10-20'},'sample':{'total':535,'asd':49,'non_asd':486,'age_mean':15.23,'age_range':[3,72],'adult_count':None,'asd_adult_count':None,'support_level_counts':[29,17,3]},'model_counts':{'impairment':483,'tic_severity':485},'unadjusted':{'impairment':{'asd_mean':14.79,'non_asd_mean':17.85,'p':0.111},'tic_severity':{'asd_mean':21.12,'non_asd_mean':19.28,'p':0.152}},'adjusted':{'impairment':{'beta':-4.49,'ci':[-8.46,-0.51],'p':0.027},'tic_severity':{'beta':-0.31,'ci':[-2.91,2.29],'p':0.814}},'scale_ranges':{'impairment':[0,50],'tic_severity':[0,50]},'selected_source_cells':selected,'scope':'Published cohort aggregates only; Table 2 headings are group totals, not verified item-specific counts.'}
 for name in ['impairment','tic_severity']:
  assert str(inputs['adjusted'][name]['beta']).replace('-','−') in text(tables['TABLE 3'])
 (P/'inputs.json').write_text(json.dumps(inputs,ensure_ascii=False,indent=2)+'\n')
 prov={'url':URL,'start_utc':start,'completed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':status,'response_sha256':hashlib.sha256(b).hexdigest(),'response_bytes':len(b),'identifiers':ids,'tables_inspected':list(tables),'supplement_types':[text(s) for s in a.findall('.//supplementary-material')],'source_license':'CC BY-NC-ND 4.0, as stated in source; only facts and original summaries retained','paper_body_retained':False,'individual_data_accessed':False,'limits':'Main paper and supplement inventory inspected. Disclosure document not audited; participant data unavailable publicly and not requested.'}
 (P/'source-provenance.json').write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n')
 print('Primary identifiers and selected aggregate cells verified')
if __name__=='__main__':main()
