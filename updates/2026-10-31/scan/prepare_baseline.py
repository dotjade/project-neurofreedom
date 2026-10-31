#!/usr/bin/env python3
"""Recreate prior selected metadata input from versioned public snapshots."""
import argparse,csv,io,json,pathlib,hashlib,subprocess
BASE='8b9fd54ff445e8f5e74ffffa48f49a80ad36990b'
def build(repo):
 p=repo/'updates/2026-10-30/scan'
 return {'cutoff_utc':json.loads((p/'summary.json').read_text())['core_completed_utc'],'pubmed':[json.loads(x)for x in(p/'pubmed-screening.jsonl').read_text().splitlines()],'registry':[json.loads(x)for x in(p/'registry-evidence.jsonl').read_text().splitlines()],'preprints':{s:list(csv.DictReader(io.StringIO((p/(s+'-preprint-index.tsv')).read_text()),delimiter='\t'))for s in ['biorxiv','medrxiv']}}
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--out',required=True);args=a.parse_args();repo=pathlib.Path(args.repo)
 for path in ['summary.json','pubmed-screening.jsonl','registry-evidence.jsonl','biorxiv-preprint-index.tsv','medrxiv-preprint-index.tsv']:
  p='updates/2026-10-30/scan/'+path;expected=subprocess.check_output(['git','show',BASE+':'+p],cwd=repo);assert (repo/p).read_bytes()==expected,p
 pathlib.Path(args.out).write_text(json.dumps(build(repo),indent=2)+'\n')
if __name__=='__main__':main()
