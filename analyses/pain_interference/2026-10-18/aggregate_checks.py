"""Deterministic published-summary audit; no individual records or inference.

Run from this directory: python aggregate_checks.py
Python standard library only. Rounding envelopes are NOT confidence intervals.
"""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import json

D = Decimal

def decimal_value(value):
    d = D(value)
    if not d.is_finite():
        raise ValueError('A finite decimal is required')
    return d

def rounding_envelope(value):
    """Closed conservative envelope for ordinary rounding at displayed precision."""
    d = decimal_value(value)
    half_unit = D(10) ** d.as_tuple().exponent / 2
    return d - half_unit, d + half_unit

def percent(n, denominator):
    if not isinstance(n, int) or not isinstance(denominator, int):
        raise ValueError('Counts must be integers')
    if denominator <= 0 or n < 0 or n > denominator:
        raise ValueError('Invalid count or denominator')
    return D(n) * 100 / D(denominator)

def display(d, places=4):
    return format(d.quantize(D(10) ** -places, rounding=ROUND_HALF_UP), 'f')

def audit(data):
    if data['sample_n'] <= 0:
        raise ValueError('Invalid sample size')
    rows=data['interference']
    if len(rows)!=13 or len({r['domain'] for r in rows})!=13:
        raise ValueError('Expected 13 unique domains')
    results=[]
    for row in rows:
        t,p = decimal_value(row['tic_mean']),decimal_value(row['pain_mean'])
        if not (1<=t<=5 and 1<=p<=5):
            raise ValueError('Mean outside adapted 1–5 scale')
        if any(decimal_value(row[k])<0 for k in ('tic_sd','pain_sd')):
            raise ValueError('Negative SD')
        tl,tu=rounding_envelope(row['tic_mean'])
        pl,pu=rounding_envelope(row['pain_mean'])
        results.append({'domain':row['domain'],'difference_of_reported_means_tic_minus_pain':display(t-p),
                        'rounding_only_envelope':[display(tl-pu),display(tu-pl)],
                        'strictly_positive_throughout_rounding_envelope':tl-pu>0})
    h=data['help_seeking']; c=h['table_categories']
    seekers=c['received_help']+c['sought_but_no_help']
    provider=[]
    for k,n in h['provider_table'].items():
        provider.append({'provider':k,'table_count':n,'prose_count':h['provider_prose'][k],
                         'table_count_pct_of_table_denominator':display(percent(n,h['table_provider_denominator'])),
                         'printed_pct':h['provider_pct'][k],
                         'table_count_matches_printed_pct_at_one_decimal':display(percent(n,h['table_provider_denominator']),1)==h['provider_pct'][k]})
    return {'analysis_type':'Deterministic public aggregate reporting audit; no adult-specific estimate',
            'inference_limit':'Different N/A patterns may imply different item samples. Differences of published means are not established paired mean differences, clinical effects, prevalence, or statistical tests.',
            'rounding_assumption':'Ordinary nearest rounding at each displayed decimal precision; closed envelopes are conservative and are not confidence intervals.',
            'domain_results':results,
            'domains_with_positive_reported_gap':sum(decimal_value(r['difference_of_reported_means_tic_minus_pain'])>0 for r in results),
            'domains_positive_under_rounding':sum(r['strictly_positive_throughout_rounding_envelope'] for r in results),
            'minimum_reported_gap':min(results,key=lambda r:decimal_value(r['difference_of_reported_means_tic_minus_pain'])),
            'maximum_reported_gap':max(results,key=lambda r:decimal_value(r['difference_of_reported_means_tic_minus_pain'])),
            'highest_pain_mean_domains':[r['domain'] for r in sorted(rows,key=lambda r:decimal_value(r['pain_mean']),reverse=True)[:3]],
            'highest_tic_mean_domain':max(rows,key=lambda r:decimal_value(r['tic_mean']))['domain'],
            'age_accounting':{'all_age_bands_sum':sum(x['n'] for x in data['age_bands']),
                              'aged_19plus':sum(x['n'] for x in data['age_bands'][1:]),
                              'aged_16_to_18':data['age_bands'][0]['n'],
                              'aged_18plus_n':None,'adult_interference_estimates':None,
                              'missing_prerequisite':'Separate ages16–17 from age18 and publish age≥18 item-level valid n/N/A counts, means and dispersion; paired analysis also needs common-observation n and covariance/difference dispersion.'},
            'help_seeking':{'table_category_sum':sum(c.values()),'table_derived_seekers':seekers,
                            'prose_seekers':h['prose_sought_help'],
                            'table_derived_seekers_pct':display(percent(seekers,data['sample_n'])),
                            'prose_count_seekers_pct':display(percent(h['prose_sought_help'],data['sample_n'])),
                            'printed_seekers_pct':h['prose_sought_pct'],
                            'received_among_table_derived_seekers_pct':display(percent(c['received_help'],seekers)),
                            'received_among_prose_seekers_pct':display(percent(c['received_help'],h['prose_sought_help'])),
                            'printed_received_pct':h['prose_received_pct'],
                            'adopted_corrected_seeker_count':None,
                            'provider_checks':provider},
            'no_new_significance_tests':True,'no_participant_records':True,'no_composite_interference_score':True}

if __name__=='__main__':
    root=Path(__file__).parent
    data=json.loads((root/'aggregate_inputs.json').read_text())
    (root/'aggregate_checks.json').write_text(json.dumps(audit(data),indent=2,ensure_ascii=False)+'\n')
    print('Wrote aggregate_checks.json: 13 domain summaries; adult estimation remains unavailable.')
