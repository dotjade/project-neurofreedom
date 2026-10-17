import concurrent.futures, datetime, hashlib, html, json, pathlib, re, subprocess, tempfile

ROOT=pathlib.Path(__file__).resolve().parent
BASE=json.loads((ROOT/'baseline/public__research-feed.json').read_text())
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

def check(item):
    result=dict(item); result['checkedAt']=now(); result['method']='ordinary anonymous curl GET with redirects; no credentials, custom agent, security override or bypass'
    with tempfile.TemporaryDirectory() as d:
        body=pathlib.Path(d)/'body'; headers=pathlib.Path(d)/'headers'
        p=subprocess.run(['curl','--location','--silent','--show-error','--max-time','35','--output',str(body),'--dump-header',str(headers),'--write-out','%{http_code}\t%{url_effective}\t%{content_type}',item['url']],capture_output=True,text=True)
        result['curlExitCode']=p.returncode; result['error']=p.stderr.strip() or None
        fields=p.stdout.split('\t'); result['httpStatus']=int(fields[0]) if fields and fields[0].isdigit() else None
        result['finalUrl']=fields[1].split('?')[0] if len(fields)>1 else None
        result['contentType']=fields[2] if len(fields)>2 else None
        data=body.read_bytes() if body.exists() else b''; result['bytes']=len(data)
        text=data.decode('utf-8','replace'); title=re.search(r'<title[^>]*>(.*?)</title>',text,re.S|re.I)
        result['documentTitle']=html.unescape(re.sub(r'\s+',' ',title.group(1))).strip() if title else None
        result['establishedBroken']=result['httpStatus'] in (404,410)
        if item['kind']=='timeline':
            result['renderedArticlePresent']=bool(re.search(r'<article\b',text,re.I))
            expected=item['url'].split('/blob/main/')[1]
            result['targetConfirmedRead']=result['httpStatus']==200 and expected in text and result['renderedArticlePresent']
            result['status']='retrievable' if result['targetConfirmedRead'] else 'retrieval_limited_or_target_unverified'
        elif item['kind']=='finding':
            if 'PMC10863457' in item['url']:
                result['contentMatchesExpected']=all(x in text for x in ['Perspectives from Adults with Tourette Syndrome','10.2147/NDT.S442131','PMC10863457'])
                result['expectedIdentity']='Isaacs et al. 2024; Perspectives from Adults with Tourette Syndrome on Research Priorities and Registry Development; DOI 10.2147/NDT.S442131; PMCID PMC10863457'
            elif '.pdf' in item['url']:
                result['pdfMagic']=data.startswith(b'%PDF-')
                if result['pdfMagic']:
                    q=subprocess.run(['pdftotext',str(body),'-'],capture_output=True,text=True)
                    result['contentMatchesExpected']='10.1186/s44247-026-00284-7' in q.stdout and 'Ivanova' in q.stdout
                    result['expectedIdentity']='Ivanova et al.; DOI 10.1186/s44247-026-00284-7'
                else: result['contentMatchesExpected']=False
            else:
                result['contentMatchesExpected']='Long-term outcome of Tourette syndrome' in text and 'Pappert' in text
                result['expectedIdentity']='Pappert et al. 2003; DOI 10.1212/01.WNL.0000086370.10186.7C'
            result['status']='primary_content_retrievable' if result['httpStatus']==200 and result['contentMatchesExpected'] else ('limited_access_http_403' if result['httpStatus']==403 else 'retrieval_limited_or_target_unverified')
        else:
            result['bodySha256']=hashlib.sha256(data).hexdigest()
            try:
                feed=json.loads(data); result['matchesRepository']=feed==BASE
                for key in ['updatedAt','lastResearchDate','activityEditionDate','featuredActivityId']: result[key]=feed.get(key)
                result['activityIds']=[a['id'] for a in feed.get('activities',[])]
                result['feedback']=feed.get('feedback')
                (ROOT/(item['kind']+'.json')).write_text(json.dumps(feed,indent=2)+'\n')
            except Exception as e: result['parseError']=str(e)
            h=headers.read_text() if headers.exists() else ''
            for name,key in [('date','serverDate'),('x-journal-source','journalSource'),('cache-control','cacheControl')]:
                values=re.findall(r'^'+name+r':\s*(.+?)\r?$',h,re.I|re.M)
                result[key]=values[-1] if values else None
    return result

items=[dict(kind='timeline',url=x['record'],date=x['date'],title=x['title'],sourceKind=x['type']) for x in BASE['timeline']]
items += [dict(kind='finding',url=x['url'],label=x['label']) for x in BASE['findings']]
items += [dict(kind='production',url='https://tourette.fyi/api/public-feed'),dict(kind='rawSource',url='https://raw.githubusercontent.com/dotjade/project-neurofreedom/main/public/research-feed.json')]
started=now()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(check,items))
ledger={'checkedAt':started,'completedAt':now(),'checkDate':'2026-10-17','scope':'9 currently displayed repository timeline links and 3 finding sources, plus production/raw-source baseline. No publication performed.','repositoryFeedUpdatedAt':BASE['updatedAt'],'repositoryFeedLastResearchDate':BASE['lastResearchDate'],'results':results}
(ROOT/'link-ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(ledger,indent=2))
