import json,unittest,copy
from pathlib import Path
from analyze import analyze
P=Path(__file__).resolve().parent
class AuditTests(unittest.TestCase):
 def setUp(self): self.x=json.loads((P/'inputs.json').read_text());self.r=analyze(self.x)
 def test_gaps(self):self.assertEqual(self.r['alpha_minus_omega'],{'TTS':'0.29','GSS':'0.32'})
 def test_lenient(self):self.assertEqual(self.r['cutoff_sensitivity']['lenient']['individual_cutoffs_met'],{'RMSEA':True,'CFI':True,'TLI':False})
 def test_stringent(self):self.assertEqual(self.r['cutoff_sensitivity']['stringent']['count_met'],0)
 def test_neither_joint(self):self.assertFalse(any(y['all_three_met'] for y in self.r['cutoff_sensitivity'].values()))
 def test_rounding(self):
  for k,v in self.r['rounding_sensitivity'].items():
   if isinstance(v,bool):self.assertTrue(v)
 def test_partition(self):self.assertTrue(self.r['diagnosis_partition_matches'])
 def test_boundary_inclusive(self):
  y=copy.deepcopy(self.x);y['fit']={'RMSEA':'0.10','CFI':'0.90','TLI':'0.90'}
  self.assertTrue(analyze(y)['cutoff_sensitivity']['lenient']['all_three_met'])
 def test_directions(self):
  y=copy.deepcopy(self.x);y['fit']={'RMSEA':'0.11','CFI':'0.89','TLI':'0.89'}
  self.assertEqual(analyze(y)['cutoff_sensitivity']['lenient']['count_met'],0)
 def test_not_estimation(self):self.assertIsNone(self.r['random_seed'])
 def test_exact_reproduction(self):self.assertEqual(self.r,json.loads((P/'results.json').read_text()))
if __name__=='__main__':unittest.main()
