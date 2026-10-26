"""Deterministic descriptive audit of published aggregates; not a simulation."""
import json
from decimal import Decimal
from pathlib import Path
P = Path(__file__).resolve().parent

def analyze(x):
    c = x['counts']
    fraction = lambda k: str((Decimal(c[k])*100/Decimal(c['total'])).quantize(Decimal('.000001')))
    contrasts = {k: str(Decimal(str(v))-Decimal(str(x['table1_means']['youth'][k])))
                 for k,v in x['table1_means']['adult'].items()}
    return {
        'kind': 'Deterministic published-aggregate arithmetic; not simulation or participant reanalysis',
        'seed': None,
        'partition_checks': {'age': c['youth']+c['adult']==c['total'],
            'diagnosis': sum(c[k] for k in ['tourette','chronic_motor','chronic_vocal','transient'])==c['total'],
            'sites': sum(x['site_counts'])==c['total'],
            'interview': sum(x['interview_counts'])==c['structured_interview'],
            'ascertainment': c['structured_interview']+c['best_estimate']==c['total']},
        'adult_percent': fraction('adult'),
        'structured_interview_percent': fraction('structured_interview'),
        'chronic_motor_or_vocal_percent': str((Decimal(c['chronic_motor']+c['chronic_vocal'])*100/Decimal(c['total'])).quantize(Decimal('.000001'))),
        'adult_minus_youth_printed_mean_points': contrasts,
        'limits': 'Differences use rounded reported means, not adjusted effects or equivalence tests. No reconstructed scores, confidence intervals, subgroup counts, reliability coefficients, causal effects or patient biology.'
    }

if __name__ == '__main__':
    out = analyze(json.loads((P/'inputs.json').read_text()))
    (P/'results.json').write_text(json.dumps(out,indent=2)+'\n')
