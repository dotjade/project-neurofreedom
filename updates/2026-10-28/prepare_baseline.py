#!/usr/bin/env python3
"""Build selected public comparison inputs from cited source snapshot; temporary output only."""
import argparse,csv,hashlib,io,json,pathlib
BASE='7ef323818a2a808a19e367e78ba01533fc9dce58'
def build(repo):
 def read(p):return (repo/p).read_text()
 def lines(p):return [json.loads(x) for x in read(p).splitlines() if x.strip()]
 return {'cutoff_utc':json.loads(read('updates/2026-10-27/summary.json'))['core_completed_utc'],'pubmed':lines('updates/2026-10-27/pubmed-screening.jsonl'),'registry':lines('updates/2026-10-27/registry-evidence.jsonl'),'preprints':{s:list(csv.DictReader(io.StringIO(read('updates/2026-10-27/'+s+'-preprint-index.tsv')),delimiter='\t')) for s in ['biorxiv','medrxiv']}}
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--out',required=True);args=a.parse_args();repo=pathlib.Path(args.repo)
 prov=json.loads((pathlib.Path(__file__).parent/'provenance.json').read_text())
 for x in prov['sources']:
  if x.get('baseline_input'):assert hashlib.sha256((repo/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
 pathlib.Path(args.out).write_text(json.dumps(build(repo),indent=2)+'\n');print('Temporary baseline rebuilt; expected source commit',BASE)
if __name__=='__main__':main()
