#!/usr/bin/env python3
"""Bounded public-source scan. Persists metadata and original decisions, not abstracts/full text.
Run: python scan_sources.py --out PATH
Live API output is not frozen and can change after retrieval.
"""
import argparse, concurrent.futures, datetime as dt, hashlib, json, pathlib, re, time
import urllib.parse, urllib.request, xml.etree.ElementTree as ET

def utc(): return dt.datetime.now(dt.timezone.utc).isoformat()
def txt(el): return ''.join(el.itertext()) if el is not None else ''
def datefields(el): return {c.tag:c.text for c in el} if el is not None else None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='.');args=ap.parse_args()
    out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    base=json.loads((out/'baseline-metadata.json').read_text())
    log={'date':'2026-10-20','started_utc':utc(),'inclusive_overlap':['2026-10-18','2026-10-20'],
         'prior_core_end_utc':base['cutoff_utc'],'retrieval_requests':[], 'pubmed':{},'preprints':[],'registry':[], 'registry_records':[]}
    def get(url,params=None,kind='json'):
        if params: url+='?'+urllib.parse.urlencode(params)
        rec={'url':url,'started_utc':utc()}
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'PublicEvidenceScan/1.0'})
            with urllib.request.urlopen(req,timeout=20) as r: raw=r.read();rec.update(status=r.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
            data=json.loads(raw) if kind=='json' else ET.fromstring(raw)
        except Exception as e:
            rec['error']=str(e);data=None
        rec['completed_utc']=utc();log['retrieval_requests'].append(rec)
        return data
    def pubmed():
        core='Tourette OR "tic disorder" OR "tic disorders"'
        syn='tics OR "chronic motor tic" OR "chronic vocal tic" OR "persistent tic"'
        queries=[('core_edat',core,'edat','2026/10/18'),('near_edat',core,'edat','2026/10/19'),('core_pdat',core,'pdat','2026/10/18'),('core_mdat',core,'mdat','2026/10/18'),('notice_edat',f'({core}) AND (retraction OR retracted OR erratum OR corrigendum OR correction)','edat','2026/10/18'),('syn_edat',syn,'edat','2026/10/18'),('syn_pdat',syn,'pdat','2026/10/18'),('burden_treatment_edat',f'({core}) AND (adult OR severe OR pain OR burden OR ADHD OR comorbid* OR cooccurring OR treatment OR adverse OR negative OR quality of life)','edat','2026/10/18')]
        qlog=[];ids=set()
        for label,term,field,start in queries:
            params=dict(db='pubmed',term=term,datetype=field,mindate=start,maxdate='2026/10/20',retmode='json',retmax=1000)
            data=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',params)
            q={'label':label,'params':params}
            if data and 'esearchresult' in data:
                r=data['esearchresult'];q.update(count=int(r['count']),ids=r['idlist'],querytranslation=r.get('querytranslation'),warnings=r.get('warninglist'),errors=r.get('errorlist'));ids.update(r['idlist'])
            qlog.append(q);time.sleep(.4)
        prev={x['pmid']:x for x in base['pubmed']};screen=[]
        if ids:
            root=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',dict(db='pubmed',id=','.join(sorted(ids)),retmode='xml'),'xml')
            if root is not None:
                for art in root.findall('PubmedArticle'):
                    m=art.find('MedlineCitation');a=m.find('Article');p=art.find('PubmedData');pmid=txt(m.find('PMID'))
                    corrections=[dict(type=x.attrib.get('RefType'),source=txt(x.find('RefSource')),pmid=txt(x.find('PMID'))) for x in m.findall('CommentsCorrectionsList/CommentsCorrections')]
                    item=dict(pmid=pmid,title=txt(a.find('ArticleTitle')),journal_pubdate=datefields(a.find('Journal/JournalIssue/PubDate')),article_dates=[dict(type=x.attrib.get('DateType'),**datefields(x)) for x in a.findall('ArticleDate')],history={x.attrib.get('PubStatus'):datefields(x) for x in p.findall('History/PubMedPubDate')},types=[txt(x) for x in a.findall('PublicationTypeList/PublicationType')],identifiers={x.attrib.get('IdType'):txt(x) for x in p.findall('ArticleIdList/ArticleId')},DateCompleted=datefields(m.find('DateCompleted')),DateRevised=datefields(m.find('DateRevised')),corrections=corrections,prior_scan_overlap=pmid in prev,source_url=f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/')
                    item['linked_notice_changed']=pmid in prev and corrections!=prev[pmid].get('corrections',[])
                    item['screening_decision']='Pending human metadata and, for new IDs, abstract review.'
                    screen.append(item)
                    if pmid not in prev and 'Case Reports' not in item['types']:
                        print('NEW_RECORD_REQUIRES_ABSTRACT_REVIEW',pmid,item['title'],flush=True)
        log['pubmed']=dict(queries=qlog,id_occurrences=sum(x.get('count',0) for x in qlog),unique_records=len(ids),date_type_correction_screen=screen,new_to_prior_scan_ids=sorted(ids-set(prev)),previous_overlap_count=len(ids&set(prev)))
        print('PUBMED_SUMMARY',json.dumps(log['pubmed']),flush=True)
    def preprints(server):
        dataout={'server':server,'interval':['2026-10-18','2026-10-20'],'pages':[],'version_index':[],'matches':[],'screen_regex':r'\btourett\w*|\btics?\b','screen_fields':'title and abstract','pagination_complete_for_observed_response':False}
        regex=re.compile(dataout['screen_regex'],re.I);cursor=0;seen=set()
        prev=next(x for x in base['preprints'] if x['server']==server);prevset={(x['doi'],x['version']) for x in prev['version_index']}
        while True:
            u=f'https://api.biorxiv.org/details/{server}/2026-10-18/2026-10-20/{cursor}'
            d=get(u)
            if not d: break
            coll=d.get('collection',[]);msg=d.get('messages',[{}])[0]
            dataout['pages'].append({'cursor':cursor,'returned':len(coll),'message':msg})
            for x in coll:
                key=(x['doi'],x['version']);seen.add(key)
                dataout['version_index'].append({k:x.get(k) for k in ('doi','version','date')})
                if regex.search(x.get('title','')+' '+x.get('abstract','')):
                    dataout['matches'].append({k:x.get(k) for k in ('doi','version','date','title','category','published')})
                    print('PREPRINT_MATCH_REQUIRES_REVIEW',server,json.dumps({k:x.get(k) for k in ('doi','version','date','title')}),flush=True)
            total=int(msg.get('total',0))
            if not coll or cursor+len(coll)>=total:
                dataout['pagination_complete_for_observed_response']=True;break
            cursor+=len(coll)
        dataout.update(total_returned=len(dataout['version_index']),unique_doi_versions=len(seen),previous_scan_overlap_doi_versions=len(seen&prevset),not_in_previous_scan_doi_versions=len(seen-prevset),reported_totals=sorted(set(int(x['message'].get('total',0)) for x in dataout['pages'])))
        log['preprints'].append(dataout);print('PREPRINT_SUMMARY',server,json.dumps({k:v for k,v in dataout.items() if k not in ('version_index','pages')}),flush=True)
    def registries():
        studies={}
        for label,key,term in [('ct_tourette','query.cond','Tourette'),('ct_tic_disorder','query.cond','tic disorder'),('ct_tics','query.cond','Tics'),('ct_ecopipam','query.term','ecopipam')]:
            params={key:term,'filter.advanced':'AREA[LastUpdatePostDate]RANGE[2026-10-18,2026-10-20]','pageSize':100,'format':'json','countTotal':'true'}
            r=get('https://clinicaltrials.gov/api/v2/studies',params);q={'label':label,'params':params}
            if r:
                q['response']={'totalCount':r.get('totalCount'),'nct_ids':[x['protocolSection']['identificationModule']['nctId'] for x in r.get('studies',[])],'nextPageToken':r.get('nextPageToken')}
                for x in r.get('studies',[]):studies[x['protocolSection']['identificationModule']['nctId']]=x
            log['registry'].append(q)
        for nct,r in sorted(studies.items()):
            p=r['protocolSection'];i=p['identificationModule'];e=p.get('eligibilityModule',{})
            # Do not persist contacts, officials, locations, or prose containing contact details.
            item={'nctId':nct,'title':i.get('briefTitle'),'status':p.get('statusModule',{}),'hasResults':r.get('hasResults'),'conditions':p.get('conditionsModule',{}).get('conditions',[]),'design':p.get('designModule',{}),'outcome_summary':('Registered two-day EEG beta-power comparison before tic events; no treatment outcome.' if nct=='NCT07137442' else 'Structured outcome interpretation requires manual review.'),'eligibility':{k:e.get(k) for k in ('healthyVolunteers','sex','minimumAge','maximumAge','stdAges')},'source_url':f'https://clinicaltrials.gov/study/{nct}','prior_scan_overlap':nct in base['registry_ids']}
            log['registry_records'].append(item)
        print('REGISTRY_SUMMARY',json.dumps({'queries':log['registry'],'records':log['registry_records']}),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        fs=[pool.submit(pubmed),pool.submit(preprints,'biorxiv'),pool.submit(preprints,'medrxiv'),pool.submit(registries)]
        for f in fs:
            try:f.result()
            except Exception as e:log.setdefault('worker_errors',[]).append(str(e))
    log['completed_utc']=utc();log['retrieval_requests'].sort(key=lambda x:x['started_utc'])
    (out/'search-log.json').write_text(json.dumps(log,indent=2)+'\n')
    print('SAVED',out/'search-log.json',flush=True)
if __name__=='__main__':main()

