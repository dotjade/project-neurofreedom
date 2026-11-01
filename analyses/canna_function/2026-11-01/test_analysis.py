import unittest,json
from pathlib import Path
from analyze import wilson,riskdiff,audit
class Tests(unittest.TestCase):
 def setUp(self): self.a=json.loads((Path(__file__).parent/'inputs.json').read_text()); self.r=audit(self.a)
 def test_primary(self):
  self.assertAlmostEqual(self.r['primary_unadjusted']['risk_difference'],.1278409090909091)
  self.assertAlmostEqual(self.r['primary_unadjusted']['risk_ratio'],2.40625)
 def test_null_compatible(self):
  l,u=self.r['primary_unadjusted']['newcombe_wilson_95ci']; self.assertLess(l,0); self.assertGreater(u,0)
  self.assertEqual(self.r['functional_intervals_including_zero'],5)
 def test_discrepancy(self):
  self.assertEqual(self.r['functional_rounding_compatible_rows'],4)
  row=self.r['functional_audit'][1]
  self.assertEqual(row['lsm_subtraction'],'-0.83'); self.assertEqual(row['subtraction_minus_reported'],'-6.38')
 def test_exchange(self):
  d,c=riskdiff(14,64,3,33); e,k=riskdiff(3,33,14,64)
  self.assertAlmostEqual(d,-e); self.assertAlmostEqual(c[0],-k[1]); self.assertAlmostEqual(c[1],-k[0])
 def test_zero_events(self):
  l,u=wilson(0,10); self.assertAlmostEqual(l,0); self.assertGreater(u,0)
 def test_all_events(self):
  l,u=wilson(10,10); self.assertAlmostEqual(u,1); self.assertLess(l,1)
 def test_invalid(self):
  for x,n in [(11,10),(-1,10),(0,0)]:
   with self.assertRaises(ValueError): wilson(x,n)
 def test_equal_groups(self):
  d,c=riskdiff(5,10,5,10); self.assertEqual(d,0); self.assertAlmostEqual(c[0],-c[1])
 def test_denominators(self):
  self.assertEqual(sum(self.a['population']['analyzed']),97)
  self.assertEqual(sum(self.a['population']['completed_registry']),72)
  self.assertEqual(self.a['population']['randomized']-self.a['population']['excluded_untreated'],97)
 def test_deterministic(self): self.assertEqual(self.r,audit(self.a))
if __name__=='__main__': unittest.main()
