# Bounded anonymous displayed-link checker. Requires Python 3, curl and pdftotext.
# Run: python check_homepage_links.py /path/to/repository
# Writes a new local rerun ledger, never modifies the published historical ledger.
import sys, concurrent.futures, datetime, hashlib, html, json, pathlib, re, subprocess, tempfile

ROOT=pathlib.Path(__file__).resolve().parent
REPO=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT.parents[2]
# Re-running checks current network state, not historical availability.
BASE=json.loads((REPO/'public/research-feed.json').read_text())
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

def check(item):
    result=dict(item); result['checkedAt']=now(); result['method']='ordinary anonymous curl GET with redirects; no credentials, custom agent, security override or bypass'
    with tempfile.TemporaryDirectory(dir=ROOT) as d:
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
        elif item['kind']=='homepageResearch':
            if item.get('pmid'):
                result['contentMatchesExpected']=item['pmid'] in text and ('<title' in text) and 'PubMed' in (result['documentTitle'] or '') and 'Checking' not in (result['documentTitle'] or '')
            else:
                result['contentMatchesExpected']=item['expect'].lower() in (result['documentTitle'] or '').lower()
            result['status']='target_metadata_retrievable' if result['httpStatus']==200 and result['contentMatchesExpected'] else 'access_limited_or_target_unverified'
        elif item['kind']=='feedbackConfig':
            try:
                result['config']=json.loads(data)
                result['status']='retrievable'
            except Exception as e: result['parseError']=str(e)
        elif item['kind']=='homepage':
            result['containsExplainerAnchor']='id="what-is-tourette"' in text
            result['containsCommentForm']='<form' in text.lower()
            result['status']='retrievable' if result['httpStatus']==200 and result['containsExplainerAnchor'] else 'access_limited_or_target_unverified'
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
                result['contentMatchesExpected']='Objective assessments of longitudinal outcome' in text and 'Pappert' in text
                result['expectedIdentity']='Pappert et al. 2003; DOI 10.1212/01.WNL.0000086370.10186.7C'
            result['status']='primary_content_retrievable' if result['httpStatus']==200 and result['contentMatchesExpected'] else ('bot_challenge_http_403' if result['documentTitle']=='Just a moment...' else 'limited_access_http_403' if result['httpStatus']==403 else 'browser_challenge_http_203' if result['httpStatus']==203 and any(x in text.lower() for x in ['checking your browser','recaptcha']) else 'retrieval_limited_or_target_unverified')
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

items=[dict(kind='homepageResearch',url='https://www.cdc.gov/tourette-syndrome/about/index.html',expect='Tourette'),dict(kind='homepageResearch',url='https://medlineplus.gov/genetics/condition/tourette-syndrome/',expect='Tourette')]
items += [dict(kind='homepageResearch',url='https://pubmed.ncbi.nlm.nih.gov/'+pmid+'/',pmid=pmid) for pmid in ['21955933','16520330','17987065','25264251','25044024','26041822']]
items += [dict(kind='homepageResearch',url='https://www.mdpi.com/2077-0383/11/1/250',expect='ONLINE-TICS'),dict(kind='feedbackConfig',url='https://tourette.fyi/feedback-config.json'),dict(kind='homepage',url='https://tourette.fyi/')]
started=now()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(check,items))
ledger={'checkedAt':started,'completedAt':now(),'checkDate':now()[:10],'scope':'Nine additional source-displayed homepage research and guidance links, production homepage and feedback configuration; HTTP/content check not rendered browser QA.','results':results}
(ROOT/'homepage-link-check.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(ledger,indent=2))
