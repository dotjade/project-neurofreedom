#!/usr/bin/env python3
"""Reconstruct permitted input metadata and reproduce seven normalized outputs offline."""
import argparse,copy,csv,hashlib,json,pathlib,subprocess,sys,tempfile
ROOT=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((ROOT/n).read_text())
def lines(n):return [json.loads(x)for x in(ROOT/n).read_text().splitlines()if x.strip()]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);a=ap.parse_args();raw=copy.deepcopy(load('search-log.json'));raw.pop('request_log_path');raw.pop('scope');raw['retrieval_requests']=load('request-log.json');raw['pubmed']['date_type_correction_screen']=lines('pubmed-screening.jsonl');raw['registry_records']=lines('registry-evidence.jsonl')
 for q in raw['preprints']:
  with(ROOT/q['index_path']).open()as f:q['version_index']=list(csv.DictReader(f,delimiter='\t'))
 names=['search-log.json','request-log.json','pubmed-screening.jsonl','registry-evidence.jsonl','biorxiv-preprint-index.tsv','medrxiv-preprint-index.tsv','summary.json']
 with tempfile.TemporaryDirectory(prefix='neurofreedom-oct29-repro-')as d:
  p=pathlib.Path(d);(p/'raw.json').write_text(json.dumps(raw));subprocess.run([sys.executable,str(ROOT/'build_results.py'),'--raw',str(p/'raw.json'),'--repo',a.repo,'--out',str(p/'out')],check=True,capture_output=True,text=True)
  checks=[{'path':n,'byte_identical':(ROOT/n).read_bytes()==(p/'out'/n).read_bytes(),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()}for n in names];assert all(x['byte_identical']for x in checks)
 result={'status':'passed','reproduced_files':len(checks),'checks':checks,'scope':'Saved selected metadata only, no new live queries or clinical recalculation.'};(ROOT/'reproduction-check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
