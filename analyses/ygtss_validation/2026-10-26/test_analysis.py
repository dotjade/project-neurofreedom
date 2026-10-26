import json,unittest
from decimal import Decimal
from pathlib import Path
from analyze import analyze
P=Path(__file__).resolve().parent
class AggregateTests(unittest.TestCase):
 def setUp(self):
  self.x=json.loads((P/'inputs.json').read_text()); self.r=analyze(self.x)
 def test_partitions(self):
  for k,v in self.r['partition_checks'].items():
   with self.subTest(k=k): self.assertTrue(v)
 def test_fractions(self):
  for k,n in [('adult_percent',101),('structured_interview_percent',410),('chronic_motor_or_vocal_percent',51)]:
   with self.subTest(k=k): self.assertLess(abs(Decimal(self.r[k])-Decimal(n)*100/617),Decimal('.000001'))
 def test_contrasts(self):
  self.assertEqual({k:Decimal(v) for k,v in self.r['adult_minus_youth_printed_mean_points'].items()}, {'motor':Decimal('.95'),'phonic':Decimal('-1.97'),'total_tic':Decimal('-1.02'),'impairment':Decimal('1.77')})
 def test_unknown_not_zero(self): self.assertTrue(all(v is None for v in self.x['ascertainment'].values()))
 def test_no_randomness(self): self.assertIsNone(self.r['seed'])
 def test_nonvalidating_scope(self): self.assertNotIn('subgroup_validation_identified',self.r)
 def test_reproduced(self): self.assertEqual(self.r,json.loads((P/'results.json').read_text()))
if __name__=='__main__':unittest.main()
