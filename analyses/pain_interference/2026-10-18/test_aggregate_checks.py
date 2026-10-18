import copy,json,unittest
from pathlib import Path
from decimal import Decimal as D
from aggregate_checks import audit,rounding_envelope,percent,display

class AggregateChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((Path(__file__).parent/'aggregate_inputs.json').read_text())
        cls.out=audit(cls.data)
    def test_domains(self):self.assertEqual(len(self.out['domain_results']),13)
    def test_all_reported_gaps_positive(self):self.assertEqual(self.out['domains_with_positive_reported_gap'],13)
    def test_rounding_does_not_reverse_signs(self):self.assertEqual(self.out['domains_positive_under_rounding'],13)
    def test_smallest_gap(self):self.assertEqual(self.out['minimum_reported_gap']['difference_of_reported_means_tic_minus_pain'],'0.0500')
    def test_largest_gap(self):self.assertEqual(self.out['maximum_reported_gap']['difference_of_reported_means_tic_minus_pain'],'1.1200')
    def test_pain_ranking(self):self.assertEqual(self.out['highest_pain_mean_domains'],['Mood','Sleep','General enjoyment of life'])
    def test_tic_ranking(self):self.assertEqual(self.out['highest_tic_mean_domain'],'Social situations')
    def test_rounding_one_decimal(self):self.assertEqual(rounding_envelope('2.9'),(D('2.85'),D('2.95')))
    def test_rounding_two_decimal(self):self.assertEqual(rounding_envelope('3.09'),(D('3.085'),D('3.095')))
    def test_general_activity_envelope(self):self.assertEqual(self.out['domain_results'][0]['rounding_only_envelope'],['0.2850','0.3950'])
    def test_age_counts(self):self.assertEqual([self.out['age_accounting'][k] for k in ('all_age_bands_sum','aged_19plus','aged_16_to_18')],[181,140,41])
    def test_adult_not_imputed(self):self.assertIsNone(self.out['age_accounting']['aged_18plus_n']);self.assertIsNone(self.out['age_accounting']['adult_interference_estimates'])
    def test_item_denominators_not_imputed(self):self.assertTrue(all(r['tic_n'] is None and r['pain_n'] is None and r['paired_n'] is None for r in self.data['interference']))
    def test_help_partition(self):self.assertEqual(self.out['help_seeking']['table_category_sum'],181);self.assertEqual(self.out['help_seeking']['table_derived_seekers'],117)
    def test_help_conflict(self):self.assertNotEqual(self.out['help_seeking']['table_derived_seekers'],self.out['help_seeking']['prose_seekers']);self.assertIsNone(self.out['help_seeking']['adopted_corrected_seeker_count'])
    def test_help_percent(self):self.assertEqual(display(percent(117,181),1),'64.6');self.assertEqual(display(percent(118,181),1),'65.2')
    def test_receipt_percent(self):self.assertEqual(display(percent(71,117),1),'60.7');self.assertEqual(display(percent(71,118),1),'60.2')
    def test_provider_percentages(self):self.assertTrue(all(x['table_count_matches_printed_pct_at_one_decimal'] for x in self.out['help_seeking']['provider_checks']))
    def test_deterministic(self):self.assertEqual(audit(self.data),audit(copy.deepcopy(self.data)))
    def test_invalid_denominator(self):
        with self.assertRaises(ValueError):percent(2,0)
    def test_invalid_count(self):
        with self.assertRaises(ValueError):percent(3,2)
    def test_invalid_mean(self):
        d=copy.deepcopy(self.data);d['interference'][0]['pain_mean']='5.01'
        with self.assertRaises(ValueError):audit(d)
    def test_nonfinite_mean(self):
        d=copy.deepcopy(self.data);d['interference'][0]['pain_mean']='NaN'
        with self.assertRaises(ValueError):audit(d)
    def test_duplicate_domain(self):
        d=copy.deepcopy(self.data);d['interference'][1]['domain']=d['interference'][0]['domain']
        with self.assertRaises(ValueError):audit(d)
    def test_no_clinical_estimate(self):self.assertTrue(self.out['no_new_significance_tests'] and self.out['no_participant_records'] and self.out['no_composite_interference_score'])

if __name__=='__main__':unittest.main()
