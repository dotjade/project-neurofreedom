import unittest,json
from pathlib import Path
from analyze import calculate,denominators
class Audit(unittest.TestCase):
 def setUp(self):self.x=json.loads((Path(__file__).parent/'inputs.json').read_text());self.r=calculate(self.x)
 def test_denominators(self):self.assertEqual(denominators(28,71.8,43),[39]);self.assertEqual(denominators(10,52.6,21),[19])
 def test_implied(self):self.assertEqual([a['transition_implied_fit_if_same_complete_population'] for a in self.r['arms']],[30,12])
 def test_discrepancy(self):self.assertEqual([a['difference'] for a in self.r['arms']],[2,2])
 def test_crude(self):self.assertAlmostEqual(self.r['crude_difference_using_percentage_compatible_denominators'],28/39-10/19)
 def test_not_refit(self):self.assertGreater(abs(self.r['crude_minus_reported']),0.02)
 def test_hierarchy(self):self.assertTrue(self.r['reported_lower_above_margin']);self.assertFalse(self.r['primary_gate_passed']);self.assertFalse(self.r['confirmatory_noninferiority_established_under_published_hierarchy'])
 def test_interval(self):self.assertTrue(self.r['reported_interval_includes_zero']);self.assertEqual(self.r['distance_lower_to_margin'],0.24)
 def test_missingness_not_inferred(self):self.assertFalse(self.r['missingness_bounds_executed'])
 def test_boundary(self):self.assertEqual(denominators(1,100,1),[1]);self.assertEqual(denominators(2,100,1),[])
 def test_determinism(self):self.assertEqual(calculate(self.x),calculate(self.x))
if __name__=='__main__':unittest.main()
