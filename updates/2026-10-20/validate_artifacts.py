#!/usr/bin/env python3
"""Offline validation of this observed scan; no network calls."""
import csv, hashlib, json, pathlib
P=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((P/n).read_text())
def main():
    s=read('summary.json');log=read('search-log.json')
    assert s['pubmed_unique_records']==8
    pm=[json.loads(x) for x in (P/'pubmed-screening.jsonl').read_text().splitlines()]
    assert len(pm)==len({x['pmid'] for x in pm})==8
    assert sum(x['prior_scan_overlap'] for x in pm)==5
    assert not any(x['linked_notice_changed'] for x in pm)
    for server,expected in [('biorxiv',357),('medrxiv',95)]:
        rows=list(csv.DictReader((P/(server+'-preprint-index.tsv')).open(),delimiter='\t'))
        assert len(rows)==len({(x['doi'],x['version']) for x in rows})==expected
        info=next(x for x in log['preprints'] if x['server']==server)
        assert sum(x['returned'] for x in info['pages'])==expected
        assert not info['matches'] and info['pagination_complete_for_observed_response']
    reg=[json.loads(x) for x in (P/'registry-evidence.jsonl').read_text().splitlines()]
    assert len(reg)==4 and all(not x['current']['hasResults'] for x in reg)
    current=next(x for x in reg if x['id']=='NCT07137442')
    changes={x['field']:(x['previous'],x['current']) for x in current['selected_field_changes']}
    assert changes=={
      'status.lastUpdatePostDateStruct.date':('2026-10-16','2026-10-19'),
      'status.lastUpdateSubmitDate':('2026-10-15','2026-10-16'),
      'status.startDateStruct.date':('2026-10-21','2026-10-22')
    },changes
    assert all(not x['selected_field_changes'] for x in reg if x['id']!='NCT07137442')
    assert (P/'primary-evidence.jsonl').read_bytes()==b''
    for r in read('manifest.json')['files']:
        data=(P/r['path']).read_bytes()
        assert len(data)==r['bytes']
        assert hashlib.sha256(data).hexdigest()==r['sha256']
    print('PASS: observed counts, identifier uniqueness, registry diffs, empty primary ledger and all manifest hashes.')
if __name__=='__main__':main()
