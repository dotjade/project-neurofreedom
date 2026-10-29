"""Deterministic audit of published gene aggregates, not genetic risk prediction."""
import json,csv
from pathlib import Path
from decimal import Decimal
P=Path(__file__).parent

def classify(q,n):
    q=Decimal(q)
    return 'high_confidence' if q<Decimal('.1') else ('probable' if q<Decimal('.3') and n>=2 else 'neither')

def run():
    rows=json.loads((P/'inputs.json').read_text())['records']
    assert len(rows)==len({r['gene'] for r in rows})==36
    groups={k:[] for k in ['both_disorder_hc','CTD_hc_not_OCD_hc','OCD_hc_not_CTD_hc','neither_disorder_hc_combined_hc']}
    for r in rows:
        a,b=r['hcCTD'],r['hcOCD']
        k='both_disorder_hc' if a and b else 'CTD_hc_not_OCD_hc' if a else 'OCD_hc_not_CTD_hc' if b else 'neither_disorder_hc_combined_hc'
        groups[k].append(r['gene'])
        c=classify(r['combined_q'],r['combined_dnDam_count'])
        assert (c=='high_confidence')==bool(r['published_combined_hc'])==r['hcOCDCTD']
        assert (c=='probable')==bool(r['published_combined_probable'])
        r['membership_group']=k;r['combined_classification']=c
    results={'method':'Published-membership partition and Decimal threshold verification. Not re-estimated FDR or diagnostic specificity.', 'groups':groups,'group_counts':{k:len(v) for k,v in groups.items()},'combined_not_hc':[{k:r[k] for k in ['gene','combined_q','combined_dnDam_count','combined_classification']}for r in rows if not r['hcOCDCTD']], 'separate_disorder_q_available':False,'independent_replication_tested':False,'seed':None}
    (P/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    with (P/'gene-map.csv').open('w')as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    return results
if __name__=='__main__':print(json.dumps(run(),indent=2))
