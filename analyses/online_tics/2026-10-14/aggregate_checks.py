#!/usr/bin/env python3
"""Deterministic published-aggregate audit; standard library only; no participant data."""
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

D = Decimal
ROOT = Path(__file__).resolve().parent


def p_envelope(printed):
    if printed.startswith('<'):
        return D('0'), D(printed[1:])
    p = D(printed)
    return max(D('0'), p - D('0.0005')), min(D('1'), p + D('0.0005'))


def bonferroni(pvals):
    m = len(pvals)
    return [min(D('1'), p * m) for p in pvals]


def holm(pvals):
    m = len(pvals)
    order = sorted(range(m), key=lambda i: (pvals[i], i))
    adjusted = [D('0')] * m
    running = D('0')
    for rank, i in enumerate(order):
        running = max(running, min(D('1'), (m - rank) * pvals[i]))
        adjusted[i] = running
    return adjusted


def holm_stepdown(pvals, alpha):
    """Independent decision implementation using original critical thresholds."""
    order = sorted(range(len(pvals)), key=lambda i: (pvals[i], i))
    reject = [False] * len(pvals)
    for rank, i in enumerate(order):
        if pvals[i] > alpha / (len(pvals) - rank):
            break
        reject[i] = True
    return reject


def compatible_counts(n, printed_percent):
    target = D(printed_percent)
    return [k for k in range(n + 1)
            if (D(100) * k / n).quantize(D('0.1'), rounding=ROUND_HALF_UP) == target]


def audit(inputs):
    tests = []
    def check(name, predicate):
        if not predicate:
            raise AssertionError(name)
        tests.append(name)

    family = inputs['focal_family']
    alpha = D(str(inputs['alpha']))
    p_lo, p_hi = zip(*(p_envelope(row['p_printed']) for row in family))
    b_lo, b_hi = bonferroni(p_lo), bonferroni(p_hi)
    h_lo, h_hi = holm(p_lo), holm(p_hi)
    printed_upper = [D(row['p_printed'].lstrip('<')) for row in family]
    b_central, h_central = bonferroni(printed_upper), holm(printed_upper)
    check('nine_unique_focal_contrasts', len(family) == 9 == len({r['id'] for r in family}))
    check('three_outcomes_three_visits', len({r['outcome'] for r in family}) == 3 and all(sum(r['outcome'] == o for r in family) == 3 for o in {r['outcome'] for r in family}))
    check('exactly_one_primary', sum(r['hierarchy'] == 'primary' for r in family) == 1)
    check('p_envelopes_ordered', all(D('0') <= lo <= hi <= D('1') for lo,hi in zip(p_lo,p_hi)))
    check('reported_p_within_envelope', all(lo <= p <= hi for lo,p,hi in zip(p_lo,printed_upper,p_hi)))
    check('all_estimates_within_ci', all(r['lower'] <= r['estimate'] <= r['upper'] for r in family))
    check('nominal_ci_p_agreement', all((r['upper'] < 0) == (p < alpha) for r,p in zip(family, printed_upper)))
    check('six_nominal_positive_contrasts', sum(p < alpha for p in printed_upper) == 6)
    check('bonferroni_monotone_envelope', all(a <= b <= c for a,b,c in zip(b_lo,b_central,b_hi)))
    check('holm_monotone_envelope', all(a <= b <= c for a,b,c in zip(h_lo,h_central,h_hi)))
    check('holm_no_larger_than_bonferroni', all(h <= b for h,b in zip(h_central,b_central)))
    check('holm_decision_matches_stepdown', [p <= alpha for p in h_central] == holm_stepdown(printed_upper, alpha))
    check('holm_decision_matches_stepdown_lower', [p <= alpha for p in h_lo] == holm_stepdown(p_lo, alpha))
    check('holm_decision_matches_stepdown_upper', [p <= alpha for p in h_hi] == holm_stepdown(p_hi, alpha))
    check('holm_zero_one_edge_case', holm([D('0'),D('1')]) == [D('0'),D('1')])
    check('holm_equal_p_edge_case', holm([D('.01')]*3) == [D('.03')]*3)
    check('holm_singleton', holm([D('.03')]) == [D('.03')])
    check('bonferroni_caps_at_one', bonferroni([D('.8'),D('.9')]) == [D('1'),D('1')])
    check('holm_permutation_equivariance', holm(list(reversed(printed_upper))) == list(reversed(h_central)))
    check('adjusted_decisions_robust_to_printed_precision', all((lo <= alpha) == (hi <= alpha) for lo,hi in zip(b_lo,b_hi)) and all((lo <= alpha) == (hi <= alpha) for lo,hi in zip(h_lo,h_hi)))
    retained = {family[i]['id'] for i,p in enumerate(h_hi) if p <= alpha}
    expected = {'tts_v4','tts_v5','impairment_v5','qol_v4'}
    check('four_retained_by_holm', retained == expected)
    check('same_four_by_bonferroni', {family[i]['id'] for i,p in enumerate(b_hi) if p <= alpha} == expected)
    primary = next(r for r in family if r['hierarchy'] == 'primary')
    primary_passes = primary['upper'] < 0
    ni = inputs['noninferiority']
    ni_numeric_condition = ni['upper'] < ni['margin']
    check('primary_gate_fails', not primary_passes and D(primary['p_printed']) > alpha)
    check('ni_numeric_condition_passes', ni_numeric_condition)
    check('ni_margin_gap_exact', D(str(ni['margin']))-D(str(ni['upper'])) == D('.04'))
    check('confirmatory_ni_gate_closed', not(primary_passes and ni_numeric_condition))
    counts = []
    for arm in inputs['noncompliance']['arms']:
        candidates = compatible_counts(arm['randomized'], arm['noncompliant_percent_printed'])
        check('unique_compliance_count_' + arm['arm'], len(candidates) == 1)
        k = candidates[0]
        counts.append({**arm,'derived_noncompliant_n':k,'derived_compliant_n':arm['randomized']-k,'noncompliant_fraction':float(D(k)/arm['randomized'])})
    ncomp=inputs['noncompliance']
    check('randomized_totals_match', sum(x['randomized'] for x in counts) == ncomp['randomized_total'])
    check('compliant_total_matches', sum(x['derived_compliant_n'] for x in counts) == ncomp['compliant_until_v3_total'])
    check('noncompliance_reasons_arithmetic', sum(x['derived_noncompliant_n'] for x in counts) == ncomp['missing_clinic_visits_until_v3_reported_n'] + ncomp['insufficient_sessions_reported_n'])
    check('noncompliance_counts_expected', [x['derived_noncompliant_n'] for x in counts] == [27,16,10])
    rows=[]
    for i,row in enumerate(family):
        rows.append({'id':row['id'],'p_printed':row['p_printed'],'p_precision_envelope':[str(p_lo[i]),str(p_hi[i])], 'nominal_ci_excludes_zero_in_favorable_direction':row['upper']<0,'bonferroni_adjusted_using_printed_p_or_censor_upper':str(b_central[i]),'holm_adjusted_using_printed_p_or_censor_upper':str(h_central[i]),'bonferroni_adjusted_precision_envelope':[str(b_lo[i]),str(b_hi[i])],'holm_adjusted_precision_envelope':[str(h_lo[i]),str(h_hi[i])],'passes_both_sensitivities_throughout_precision_envelope':h_hi[i]<=alpha and b_hi[i]<=alpha})
    return {'analysis_id':inputs['analysis_id'],'method':'Post hoc nine-contrast multiplicity/reporting-precision sensitivity, original gatekeeping logic, and compliance arithmetic','not_a_claim':'Not a participant-data reanalysis, replacement multiplicity plan, endpoint-effect comparison, attrition-adjusted efficacy estimate or clinical recommendation','focal_family_size':9,'nominal_alpha':str(alpha),'bonferroni_threshold':str(alpha/9),'primary_superiority_demonstrated':primary_passes,'noninferiority_numeric_interval_condition':ni_numeric_condition,'confirmatory_noninferiority_permitted_by_original_gate':primary_passes and ni_numeric_condition,'ni_upper_margin_gap':str(D(str(ni['margin']))-D(str(ni['upper']))),'nominal_favorable_contrast_count':6,'retained_under_both_restricted_sensitivities':sorted(retained),'results':rows,'compliance_arithmetic':counts,'noncompliance_total':sum(x['derived_noncompliant_n'] for x in counts),'noncompliance_total_percent':float(D(100)*(ncomp['randomized_total']-ncomp['compliant_until_v3_total'])/ncomp['randomized_total']),'endpoint_specific_missing_counts_identified':False,'tests_passed':len(tests),'test_names':tests}


def main():
    input_path = ROOT / 'aggregate_inputs.json'
    result = audit(json.loads(input_path.read_text()))
    result['input_sha256'] = hashlib.sha256(input_path.read_bytes()).hexdigest()
    result['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT / 'aggregate_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'tests_passed':result['tests_passed'],'retained':result['retained_under_both_restricted_sensitivities'],'primary_passes':result['primary_superiority_demonstrated'],'confirmatory_NI_allowed':result['confirmatory_noninferiority_permitted_by_original_gate'],'compliance_counts':[r['derived_noncompliant_n'] for r in result['compliance_arithmetic']]},indent=2))

if __name__ == '__main__':
    main()
