import unittest
from analyze import classify,run
class Checks(unittest.TestCase):
 def test_below_hc(self):self.assertEqual(classify('.099999999',0),'high_confidence')
 def test_hc_boundary_probable(self):self.assertEqual(classify('.1',2),'probable')
 def test_probable_requires_count(self):self.assertEqual(classify('.1',1),'neither')
 def test_upper_probable_boundary(self):self.assertEqual(classify('.3',2),'neither')
 def test_zero_dn_hc_allowed(self):self.assertEqual(classify('.027300673732677999',0),'high_confidence')
 def test_map(self):
  r=run();self.assertEqual(list(r['group_counts'].values()),[3,7,9,17])
  self.assertEqual(r['groups']['both_disorder_hc'],['DNAH9','QRICH1','SETD1A'])
  self.assertEqual([x['gene']for x in r['combined_not_hc']],['CELSR3','WWC1'])
if __name__=='__main__':unittest.main()
