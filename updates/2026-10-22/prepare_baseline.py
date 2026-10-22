#!/usr/bin/env python3
"""Rebuild temporary comparison inputs from the cited repository snapshot, not patient data.
Use a checkout of c9314ae695c3b5624f5049a3d819fef922ebe14b. Output is not a publication artifact.
"""
import argparse,csv,hashlib,io,json,pathlib
BASE='c9314ae695c3b5624f5049a3d819fef922ebe14b'
def build(repo):
 def read(p):return (repo/p).read_text()
 def lines(p):return [json.loads(x) for x in read(p).splitlines() if x.strip()]
 return {'cutoff_utc':'2026-10-21T02:57:34.629924Z','pubmed':lines('updates/2026-10-21/pubmed-screening.jsonl'),'registry':lines('updates/2026-10-21/registry-evidence.jsonl'),'preprints':{s:list(csv.DictReader(io.StringIO(read('updates/2026-10-21/'+s+'-preprint-index.tsv')),delimiter='\t')) for s in ['biorxiv','medrxiv']},'historical_integrity':[x for x in json.loads(read('updates/2026-10-18/search-log.json'))['pubmed']['date_type_correction_screen'] if x['pmid'] in ['39947542','42527169']]}
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--out',required=True);args=a.parse_args();repo=pathlib.Path(args.repo)
 prov=json.loads((pathlib.Path(__file__).parent/'provenance.json').read_text())
 for x in prov['sources']:
  if x.get('baseline_input'):assert hashlib.sha256((repo/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
 pathlib.Path(args.out).write_text(json.dumps(build(repo),indent=2)+'\n');print('Temporary baseline rebuilt; expected source commit',BASE)
if __name__=='__main__':main()
