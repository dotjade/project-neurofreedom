import unittest,json,copy
from decimal import Decimal as D
from pathlib import Path
from analyze import analyze
P=Path(__file__).resolve().parent
class Tests(unittest.TestCase):
 def setUp(self):self.x=json.loads((P/'inputs.json').read_text());self.r=analyze(self.x)
 def test_counts(self):
  t=self.r['assessment_table'];self.assertEqual([t[k] for k in t if k!='reference'],[507,129,67,752])
 def test_partitions(self):self.assertTrue(all(self.r['checks'].values()))
 def test_discordance(self):self.assertEqual(self.r['discordant_assessments'],196)
 def test_complements(self):self.assertEqual(D(self.r['category_agreement_percent'])+D(self.r['category_disagreement_percent']),D(100))
 def test_missing_counts(self):self.assertEqual((self.r['unpaired_parent_assessments'],self.r['patients_not_in_paired_analysis']),(1901,67))
 def test_published_rounding(self):
  for k in ['sensitivity_percent','specificity_percent']:self.assertEqual(D(self.r[k]).quantize(D('.1')),D(self.x['published'][k]))
 def test_absolute_bounds(self):
  a=self.r['difference_additivity_audit'];self.assertEqual((a['mean_absolute_sum_lower_bound'],a['mean_absolute_sum_upper_bound']),('0.01','4.81'));self.assertTrue(a['entire_within_conditional_absolute_bounds'])
 def test_not_signed_additive(self):self.assertEqual(self.r['difference_additivity_audit']['entire_minus_component_sum'],'-0.66')
 def test_absolute_bound_reject(self):
  x=copy.deepcopy(self.x);x['mean_difference_points']['entire']='5.00';self.assertFalse(analyze(x)['difference_additivity_audit']['entire_within_conditional_absolute_bounds'])
 def test_fellow_pairing(self):self.assertEqual(self.r['unpaired_fellow_assessments'],67)
 def test_reproduce(self):self.assertEqual(self.r,json.loads((P/'results.json').read_text()))
if __name__=='__main__':unittest.main()
