"""Transient official PDF keyword screen. No source PDF/text retained."""
import datetime,hashlib,json,pathlib,re,subprocess,tempfile
P=pathlib.Path(__file__).resolve().parent
url='https://www.ema.europa.eu/en/documents/agenda/agenda-prac-meeting-26-29-october-2026_en.pdf'
terms=['ecopipam','aripiprazole','risperidone','pimozide','haloperidol','clonidine','guanfacine','valbenazine','deutetrabenazine','tetrabenazine','Neupulse','median nerve','NeuroStar','deep brain','topiramate','botulinum','tiapride','methylphenidate','atomoxetine','lisdexamfetamine','fluvoxamine','sertraline','antidepressant']
x={'url':url,'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'terms':terms,'method':'ordinary anonymous curl then pdftotext, case-insensitive substring screen'}
with tempfile.TemporaryDirectory() as d:
 f=pathlib.Path(d)/'agenda.pdf'; q=subprocess.run(['curl','-L','-sS','--max-time','35','-o',str(f),'-w','%{http_code}',url],capture_output=True,text=True);x.update(httpStatus=q.stdout,curlExitCode=q.returncode)
 b=f.read_bytes() if f.exists() else b'';x['sha256']=hashlib.sha256(b).hexdigest();x['pdfMagic']=b.startswith(b'%PDF')
 if x['pdfMagic']:
  t=subprocess.run(['pdftotext',str(f),'-'],capture_output=True,text=True).stdout;x['matches']={term:len(re.findall(re.escape(term),t,re.I)) for term in terms};x['totalMatches']=sum(x['matches'].values())
x['paperBytesRetained']=False;x['scope']='Lexical agenda screen, not outcomes or completed regulatory decisions; wording and other medicines may be missed.'
(P/'prac-agenda-check.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x))
