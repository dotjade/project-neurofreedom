#!/usr/bin/env python3
"""Deterministic aggregate arithmetic only. Python standard library; no network."""
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import hashlib
import json

getcontext().prec = 40
HERE = Path(__file__).resolve().parent

def dec(x):
    return Decimal(str(x))

def pct(n, d):
    if d <= 0 or n < 0 or n > d:
        raise ValueError("Expected 0 <= numerator <= positive denominator")
    return dec(n) * 100 / dec(d)

def weighted(values, counts):
    if len(values) != len(counts) or not values or any(n <= 0 for n in counts):
        raise ValueError("Need matching values and positive counts")
    return sum(dec(v) * n for v, n in zip(values, counts)) / sum(counts)

def compatible_counts(displayed_percent, denominator, decimals=0):
    """Conservative inclusive rounding interval, not observed counts."""
    if denominator <= 0 or decimals < 0:
        raise ValueError("Invalid denominator or precision")
    half = dec(5) * dec(10) ** (-decimals - 1)
    target = dec(displayed_percent)
    return [n for n in range(denominator + 1)
            if target - half <= pct(n, denominator) <= target + half]

def interval_overlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

def as_json(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, dict):
        return {k: as_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [as_json(v) for v in obj]
    return obj

def analyze(data):
    c, v = data['counts'], data['vas']
    n_help = c['men_help_reported'] + c['women_help_reported']
    n_relief = c['men_relief_reported'] + c['women_relief_reported']
    compatible = compatible_counts(data['percentages']['help'], c['pain'])
    rates = [
        {'denominator_description': 'All survey respondents', 'denominator': c['all'],
         'relief_percent': pct(n_relief, c['all']), 'is_established_treated_response_rate': False},
        {'denominator_description': 'Past-or-present pain subgroup', 'denominator': c['pain'],
         'relief_percent': pct(n_relief, c['pain']), 'is_established_treated_response_rate': False},
        {'denominator_description': 'Sum of inconsistent printed help-seeking sex counts',
         'denominator': n_help, 'relief_percent': pct(n_relief, n_help),
         'is_established_treated_response_rate': False}]
    for n in compatible:
        rates.append({'denominator_description': 'Hypothetical count compatible with rounded 86% of 56; not a correction',
                      'denominator': n, 'relief_percent': pct(n_relief, n),
                      'is_established_treated_response_rate': False})
    weights = [v[g]['n'] for g in ['men', 'women']]
    present = weighted([v[g]['present'] for g in ['men', 'women']], weights)
    worst = weighted([v[g]['worst'] for g in ['men', 'women']], weights)
    half = dec(data['vas_rounding_half_unit'])
    consistency = []
    for gender in ['men', 'women']:
        row = v[gender]
        for window in ['present', 'worst']:
            from_strata = weighted([row['GTS_' + window], row['CMTD_' + window]],
                                   [row['GTS_n'], row['CMTD_n']])
            overall = dec(row[window])
            overall_range = [overall - half, overall + half]
            strata_range = [from_strata - half, from_strata + half]
            consistency.append({'gender': gender, 'window': window,
                'printed_total_mean': overall, 'diagnosis_weighted_displayed_mean': from_strata,
                'total_rounding_range': overall_range, 'strata_rounding_range': strata_range,
                'compatible_under_one_decimal_rounding': interval_overlap(overall_range, strata_range),
                'corrected_estimate': None})
    return as_json({
        'analysis_type': 'Deterministic published-aggregate arithmetic and consistency checks; no simulation or participant records',
        'sample_pain': {'n': c['pain'], 'denominator': c['all'],
                        'percent': pct(c['pain'], c['all']),
                        'timeframe': 'Past or present, not current prevalence'},
        'help_seeking': {'reported_percent': dec(data['percentages']['help']),
                        'printed_count_sum': n_help, 'count_sum_percent_of_pain': pct(n_help, c['pain']),
                        'counts_compatible_with_rounded_reported_percent': compatible,
                        'reported_women_help_exceeds_women_pain': c['women_help_reported'] > c['women_pain'],
                        'accepted_corrected_denominator': None},
        'relief': {'printed_count_sum': n_relief, 'reported_percent': dec(data['percentages']['relief']),
                   'conditional_denominator_scenarios': rates,
                   'all_nonpositive_as_failure_allowed': False,
                   'reason': 'Questionnaire permits uncertain responses; treatment receipt and response-category counts unresolved'},
        'vas_conditional_displayed_aggregate': {'present_weighted_mean': present, 'worst_weighted_mean': worst,
                   'worst_minus_present': worst - present,
                   'exact_gap_from_displayed_means': str(Fraction(worst - present)),
                   'present_rounding_range': [present - half, present + half],
                   'worst_rounding_range': [worst - half, worst + half],
                   'gap_rounding_range': [worst - present - 2 * half, worst - present + 2 * half],
                   'status': 'Conditional on sex-total rows; female worst mean conflicts with diagnosis strata. Not a corrected or inferential estimate.',
                   'interpretation': 'Different recalled quantities, not longitudinal change, treatment benefit, or clinically important difference; no confidence interval computed'},
        'vas_partition_consistency': consistency,
        'limits': ['No sampling interval or general population estimate',
                   'No correction to contradictory source reporting',
                   'No paired covariance, significance test, meaningful-change threshold or causal effect',
                   'Rounding ranges are deterministic arithmetic compatibility ranges, not confidence intervals']})

def main():
    raw = (HERE / 'aggregate_inputs.json').read_bytes()
    result = analyze(json.loads(raw))
    result['input_sha256'] = hashlib.sha256(raw).hexdigest()
    result['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE / 'aggregate_checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('Saved aggregate_checks.json; no clinical inference or corrected denominator.')

if __name__ == '__main__':
    main()
