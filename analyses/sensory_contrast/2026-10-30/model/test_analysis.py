import json,math,unittest
from pathlib import Path
from analyze import compute,two_sided_p
class TestContrast(unittest.TestCase):
 def setUp(self):self.x=json.loads(Path(__file__).with_name('inputs.json').read_text());self.r=compute(self.x)
 def test_marginals(self):
  d,i=self.r['marginal_tests_identical_across_scenarios'];self.assertLess(d['p_two_sided'],.05);self.assertGreater(i['p_two_sided'],.05)
 def test_decisions_differ(self):self.assertEqual([r['below_illustrative_alpha']for r in self.r['contrast_scenarios']],[False,False,True,True])
 def test_contrast_fixed(self):
  for r in self.r['contrast_scenarios']:self.assertAlmostEqual(r['contrast'],.4)
 def test_covariance_valid(self):
  for r in self.r['contrast_scenarios']:self.assertGreater(r['covariance_determinant'],0)
 def test_independence(self):self.assertAlmostEqual(self.r['contrast_scenarios'][1]['contrast_se'],math.sqrt(.08))
 def test_ci_decisions(self):
  for r in self.r['contrast_scenarios']:self.assertEqual(r['ci95'][0]>0,r['below_illustrative_alpha'])
 def test_no_difference(self):
  x=dict(self.x);x['indirect_difference']=x['direct_difference']
  for r in compute(x)['contrast_scenarios']:self.assertEqual(r['p_two_sided'],1)
 def test_invalid_rho(self):
  x=dict(self.x);x['estimate_correlations']=[1]
  with self.assertRaises(AssertionError):compute(x)
 def test_normal_zero(self):self.assertEqual(two_sided_p(0),1)
if __name__=='__main__':unittest.main()
