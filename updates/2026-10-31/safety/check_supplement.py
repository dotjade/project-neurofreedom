"""Bounded public metadata checks; no retained external paper bytes.
Run: python check_supplement.py /path/to/repository
Rerunning observes current availability, not the historical check date.
"""
import datetime, hashlib, json, pathlib, re, subprocess, sys, tempfile
from html.parser import HTMLParser

OUT = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(sys.argv[1]).resolve()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(name, value): (OUT/name).write_text(json.dumps(value, indent=2)+'\n')
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.forms=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href','').startswith('https://'): self.links.append(a['href'])
        if tag in ('form','input','textarea'): self.forms.append(tag)

urls=[
 ('homepage','https://tourette.fyi/','public/journal-source/index.html'),
 ('script','https://tourette.fyi/journal.js','public/journal-source/journal.js'),
 ('Pappert institutional primary alternative','https://www.rcpsych.ac.uk/docs/default-source/members/devolved-nations/rcpsych-in-wales/wales-cap-objective-assess-longit-outcomes.pdf?sfvrsn=d52dec25_2',None),
]
results=[]
for label,url,local in urls:
    result={'label':label,'url':url,'checkedAt':now(),'method':'ordinary anonymous curl GET with redirects; no credentials, custom agent or access bypass'}
    with tempfile.TemporaryDirectory(dir=OUT) as d:
        body=pathlib.Path(d)/'body'
        p=subprocess.run(['curl','--location','--silent','--show-error','--max-time','35','--output',str(body),'--write-out','%{http_code}\t%{url_effective}\t%{content_type}',url],capture_output=True,text=True)
        f=p.stdout.split('\t'); data=body.read_bytes() if body.exists() else b''
        result.update(curlExitCode=p.returncode,error=p.stderr.strip() or None,httpStatus=int(f[0]) if f[0].isdigit() else None,finalUrl=f[1] if len(f)>1 else None,contentType=f[2] if len(f)>2 else None,bytes=len(data),bodySha256=sha(data))
        if local:
            result['matchesPinnedRepositoryBytes']=data==(REPO/local).read_bytes()
            if label=='homepage':
                parser=Links();parser.feed(data.decode('utf8','replace'))
                result.update(externalLinks=list(dict.fromkeys(parser.links)),formInputTextareaTags=parser.forms)
        else:
            result['pdfMagic']=data.startswith(b'%PDF-')
            if result['pdfMagic']:
                t=subprocess.run(['pdftotext',str(body),'-'],capture_output=True,text=True).stdout
                result['expectedIdentityConfirmed']=all(s in t for s in ['10.1212/01.WNL.0000086370.10186.7C','Pappert','Objective assessments of longitudinal'])
                result['identity']='Pappert et al. 2003; DOI 10.1212/01.WNL.0000086370.10186.7C'
            else: result['expectedIdentityConfirmed']=False
        result['completedAt']=now()
    results.append(result)
dump('supplementary-checks.json',{'results':results,'paperBytesRetained':False})

feed=json.loads((REPO/'public/research-feed.json').read_text())
bundled=json.loads((REPO/'public/journal-source/research-feed.json').read_text())
js=(REPO/'public/journal-source/journal.js').read_text()
html=(REPO/'public/journal-source/index.html').read_text()
config=json.loads((REPO/'public/journal-source/feedback-config.json').read_text())
parser=Links();parser.feed(html)
checked=json.loads((OUT/'link-check-rerun.json').read_text())['results']+json.loads((OUT/'homepage-link-check.json').read_text())['results']
checked_urls={x['url'] for x in checked}
research_urls={u for u in parser.links if not u.startswith('https://tourette.fyi') and u not in ['https://github.com/dotjade/project-neurofreedom','https://github.com/dotjade/project-neurofreedom/issues/new?template=contribution.md']}
ids=['hand-at-ease','familiar-route','notice-one-thing','music-or-silence','small-silly-mark','rest-or-leave']
checks={
 'six_activity_ids_unchanged':[a['id'] for a in feed['activities']]==ids,
 'all_activity_content_matches_bundled_approved_catalog':feed['activities']==bundled['activities'],
 'no_food_field':all('food' not in a for a in feed['activities']),
 'feedback_disabled':feed['feedback']['enabled'] is False,
 'zero_vote_aggregates':feed['feedback']['sampleSize']==0 and feed['feedback']['aggregates']==[] and feed['feedback']['trend']==[],
 'source_feedback_disabled_with_null_origin':config['enabled'] is False and config['apiOrigin'] is None and config['verifiedAt'] is None,
 'vote_setup_returns_before_external_requests':js.index("if(config.enabled!==true||!config.apiOrigin||!config.verifiedAt)return") < js.index("fetch(api+'/api/summary'"),
 'no_html_form_input_or_textarea':not parser.forms,
 'no_browser_storage_api':not re.search(r'localStorage|sessionStorage|indexedDB',js),
 'reflection_clear_on_pagehide':"window.addEventListener('pagehide',()=>{byId('reflection').value='';" in js,
 'activity_optional_stop_message':html.count('Optional. Rest or skip equally. Stop if uncomfortable.')==6 and 'These ordinary leisure ideas are not proven tic or ADHD treatments.' in html,
 'all_static_research_citations_in_checked_set':research_urls <= checked_urls,
 'live_homepage_and_script_match_pinned_source':all(x.get('matchesPinnedRepositoryBytes') for x in results if x['label'] in ('homepage','script')),
 'live_feedback_disabled':any(x.get('config')==config and x.get('httpStatus')==200 for x in checked if x['kind']=='feedbackConfig'),
}
dump('catalog-safety-check.json',{'checkedAt':now(),'checks':checks,'allPassed':all(checks.values()),'activityIds':ids,'staticResearchCitationCount':len(research_urls),'scope':'Source/config safeguards and ordinary live GETs only. Reflection is an unsent page-memory select. Latent vote code is gated off. No rendered, keyboard, mobile, zoom, narration, provider-log or clinical-safety certification.'})
readfiles=['README.md','RESEARCH_PROTOCOL.md','STATUS.md','public/journal-source/README.md','public/UPDATE_WORKFLOW.md','updates/2026-10-30/safety/report.md','public/link-checks/2026-10-30.json','public/research-feed.json','public/journal-source/index.html','public/journal-source/journal.js','public/journal-source/feedback-config.json']
dump('repository-provenance.json',{'checkedAt':now(),'baseCommit':subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip(),'gitStatus':subprocess.check_output(['git','-C',str(REPO),'status','--porcelain'],text=True),'readFiles':{p:sha((REPO/p).read_bytes()) for p in readfiles},'readScopeNote':'Checks hash listed instruction and source files; hashing is not full human review. Dated source/check ledgers document actual review.','repositoryModifiedByThisCheck':False,'publishedByThisCheck':False})
print(json.dumps({'networkChecks':len(results),'sourceChecks':checks,'allPassed':all(checks.values())},indent=2))
