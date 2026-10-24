#!/usr/bin/env python3
"""Read official primary XML transiently; save only allowlisted aggregate facts and provenance.
No paper body, figures, participant examples, supplementary datasets or personal data saved.
"""
import datetime as dt,hashlib,json,pathlib,re,urllib.request,xml.etree.ElementTree as E
OUT=pathlib.Path(__file__).resolve().parent
URL='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13680449&retmode=xml'
def txt(e):return ' '.join(''.join(e.itertext()).split()) if e is not None else ''
def main():
 start=dt.datetime.now(dt.timezone.utc).isoformat()
 with urllib.request.urlopen(URL,timeout=60) as f: b=f.read(); status=f.status
 root=E.fromstring(b); a=root.find('.//article') if root.tag!='article' else root
 meta=a.find('front/article-meta'); ids={e.attrib.get('pub-id-type'):txt(e) for e in meta.findall('article-id')}
 assert ids['doi']=='10.3389/fpsyt.2026.1948693'
 mapping={'Sex':'male','Race':'white','Ethnicity':'non_hispanic','Current tic medication status':'current_medication','Tic disorder family history':'family_history','OCD status':'ocd','ADHD status':'adhd','Significant life event':'life_event'}
 rows=[]
 for tr in a.findall('.//table-wrap[@id="T1"]/table/tbody/tr'):
  cs=[txt(c) for c in tr.findall('td')]
  if cs[0] in mapping:
   m=re.search(r'(\d+) \(([\d.]+)%\)',cs[1]); assert m,cs
   rows.append({'field':mapping[cs[0]],'count':int(m[1]),'percent':m[2],'source_locator':'Table 1'})
 out={'study':{'doi':ids['doi'],'pmid':'42903303','pmc':'PMC13680449','published':'2026-10-06','title':txt(meta.find('title-group/article-title'))},'stages':{'invited':758,'responded':334,'complete_tic_items':292,'retained':258,'current_tics':247,'current_as_adult_worst':50},'table1_percentages':rows,'source_locator_stages':'Sections 2.1, 2.2.1 and 3.1','rounding_assumption':'nearest 0.1 percentage point, half-up; all denominators at most 258','model_counts':{'adult_worst_tts':None,'adult_worst_impairment':None},'model_count_status':'not located in inspected main-text methods/Tables 1–5; no individual reconstruction','source_license':'CC BY 4.0; facts only retained'}
 (OUT/'inputs.json').write_text(json.dumps(out,indent=2)+'\n')
 p={'url':URL,'started_utc':start,'completed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':status,'response_sha256':hashlib.sha256(b).hexdigest(),'response_bytes':len(b),'identifiers':ids,'license_url':txt(meta.find('.//{http://www.niso.org/schemas/ali/1.0/}license_ref')),'full_text_retained':False,'supplementary_material_elements':len(a.findall('.//supplementary-material')),'tables_inspected':['T1','T2','T3','T4','T5'],'limitations':'Main paper and public metadata only. No private/author-supplied data, contact, participant plots or narratives. No absent worldwide correction claim.'}
 (OUT/'source-provenance.json').write_text(json.dumps(p,indent=2)+'\n')
 print(json.dumps({'rows':len(rows),'status':status,'sha256':p['response_sha256']}))
if __name__=='__main__':main()
