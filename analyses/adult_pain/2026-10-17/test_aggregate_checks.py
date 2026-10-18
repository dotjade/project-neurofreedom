import json
from decimal import Decimal
from pathlib import Path
import unittest

from aggregate_checks import analyze, compatible_counts, interval_overlap, pct, weighted

class AggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = json.loads(Path(__file__).with_name('aggregate_inputs.json').read_text())
        cls.result = analyze(cls.inputs)

    def test_pain_partition(self):
        c = self.inputs['counts']
        self.assertEqual(c['men_pain'] + c['women_pain'], c['pain'])
        self.assertEqual(c['men_all'] + c['women_all'], c['all'])

    def test_pain_percentage(self):
        self.assertAlmostEqual(self.result['sample_pain']['percent'], 73.6842105263158)

    def test_help_count_sum(self):
        self.assertEqual(self.result['help_seeking']['printed_count_sum'], 50)
        self.assertAlmostEqual(self.result['help_seeking']['count_sum_percent_of_pain'], 89.2857142857143)

    def test_rounding_candidate_is_conditional(self):
        self.assertEqual(compatible_counts(86, 56), [48])
        self.assertIsNone(self.result['help_seeking']['accepted_corrected_denominator'])

    def test_impossible_subset(self):
        self.assertTrue(self.result['help_seeking']['reported_women_help_exceeds_women_pain'])

    def test_relief_count(self):
        self.assertEqual(self.result['relief']['printed_count_sum'], 10)

    def test_relief_scenarios(self):
        r = {x['denominator']: x['relief_percent'] for x in self.result['relief']['conditional_denominator_scenarios']}
        for denominator, expected in [(76, 13.1578947368421), (56, 17.8571428571429), (50, 20), (48, 20.8333333333333)]:
            self.assertAlmostEqual(r[denominator], expected)

    def test_no_causal_or_corrected_rates(self):
        self.assertTrue(all(not x['is_established_treated_response_rate'] for x in self.result['relief']['conditional_denominator_scenarios']))
        self.assertFalse(self.result['relief']['all_nonpositive_as_failure_allowed'])

    def test_conditional_vas(self):
        v = self.result['vas_conditional_displayed_aggregate']
        self.assertEqual((v['present_weighted_mean'], v['worst_weighted_mean'], v['worst_minus_present']), (2.925, 4.3, 1.375))
        self.assertEqual(v['exact_gap_from_displayed_means'], '11/8')

    def test_rounding_ranges_not_ci(self):
        v = self.result['vas_conditional_displayed_aggregate']
        self.assertEqual(v['gap_rounding_range'], [1.275, 1.475])
        self.assertNotIn('confidence_interval', v)

    def test_partition_consistency(self):
        flags = {(x['gender'], x['window']): x['compatible_under_one_decimal_rounding'] for x in self.result['vas_partition_consistency']}
        self.assertEqual(flags, {('men', 'present'): True, ('men', 'worst'): True, ('women', 'present'): True, ('women', 'worst'): False})

    def test_female_conflict(self):
        x = next(x for x in self.result['vas_partition_consistency'] if x['gender'] == 'women' and x['window'] == 'worst')
        self.assertAlmostEqual(x['diagnosis_weighted_displayed_mean'], 67/15)
        self.assertGreater(x['strata_rounding_range'][0], x['total_rounding_range'][1])
        self.assertIsNone(x['corrected_estimate'])

    def test_rounding_edge(self):
        self.assertEqual(compatible_counts(50, 2), [1])
        self.assertEqual(compatible_counts(30.3, 56, 1), [])

    def test_percentage_invalid(self):
        for a, b in [(-1, 10), (11, 10), (0, 0)]:
            with self.assertRaises(ValueError):
                pct(a, b)

    def test_weighted_invalid(self):
        for v, n in [([], []), ([1], [0]), ([1], [1, 2])]:
            with self.assertRaises(ValueError):
                weighted(v, n)

    def test_weighted_exact(self):
        self.assertEqual(weighted(['2', '4'], [1, 3]), Decimal('3.5'))

    def test_interval_boundaries(self):
        self.assertTrue(interval_overlap([0, 1], [1, 2]))
        self.assertFalse(interval_overlap([0, 1], [2, 3]))

    def test_determinism(self):
        self.assertEqual(analyze(self.inputs), analyze(self.inputs))

if __name__ == '__main__':
    unittest.main(verbosity=2)
