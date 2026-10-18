"""Verify the saved scan's internal counts and classifications, without network calls.

This is a metadata consistency check, not independent clinical peer review or
proof that live source databases will return the same records later.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent
d = json.loads((p / 'search-log.json').read_text())
q = d['pubmed']['queries']
ids = {pmid for query in q for pmid in query['ids']}
assert len(ids) == d['pubmed']['unique_records'] == 27
assert sum(query['count'] for query in q) == d['pubmed']['id_occurrences'] == 29
assert all(query['count'] == len(query['ids']) for query in q)
assert {r['pmid'] for r in d['pubmed']['date_type_correction_screen']} == ids
assert all(r['screening_decision'] for r in d['pubmed']['date_type_correction_screen'])
assert len(d['pubmed']['new_to_prior_scan_ids']) == 6
assert d['pubmed']['previous_overlap_count'] == 21
assert not d['pubmed']['linked_notice_screen']['overlap_link_changes']
assert len(d['retrieval_requests']) == 36
assert all(r['http_status'] == 200 and r['finished_utc'] >= r['started_utc'] for r in d['retrieval_requests'])
for feed in d['preprints']:
    pairs = {(r['doi'], r['version']) for r in feed['version_index']}
    assert len(pairs) == len(feed['version_index']) == feed['total_returned'] == feed['unique_doi_versions']
    assert feed['reported_totals'] == [feed['total_returned']]
    assert sum(page['returned'] for page in feed['pages']) == feed['total_returned']
    assert not feed['matches']
assert sum(len(feed['pages']) for feed in d['preprints']) == 23
assert sum(feed['unique_doi_versions'] for feed in d['preprints']) == 632
assert sum(r['response']['totalCount'] for r in d['registry']) == 2
assert {nct for r in d['registry'] for nct in r['response']['nct_ids']} == {'NCT07137442'}
assert all(not r['response']['nextPageToken'] for r in d['registry'])
r = json.loads((p / 'registry-evidence.jsonl').read_text())
assert r['id'] == 'nct:NCT07137442' and r['has_results'] is False
reg = [json.loads(line) for line in (p / 'safety/regulatory-evidence.jsonl').read_text().splitlines()]
assert len(reg) == 2
assert reg[0]['publication_date'] == '2026-10-13'
assert reg[1]['date_posted'] == '2026-10-09'
assert reg[1]['event_window_classification'] == 'newly_discovered_older_notice_outside_incremental_window'
print('PASS: saved PubMed, preprint, registry and regulatory count/date/identifier assertions.')
