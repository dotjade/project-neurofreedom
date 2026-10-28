import unittest,json,pathlib,math
from analyze import run
P=pathlib.Path(__file__).resolve().parent
class Checks(unittest.TestCase):
 def setUp(self):self.c=json.loads((P/'inputs.json').read_text());self.r=run(self.c);self.d={(x['model'],x['context'],x['intervention']):x for x in self.r['scenarios']}
 def v(self,m,c,i):return self.d[m,c,i]['event_probability']
 def test_30_rows(self):self.assertEqual(len(self.d),30)
 def test_same_baseline(self):
  for m in ['single','parallel','coincidence']:
   for c,g in self.c['gate_contexts'].items():self.assertAlmostEqual(self.v(m,c,'none'),.2*g,places=11)
 def test_same_downstream(self):
  for m in ['single','parallel','coincidence']:
   for c,g in self.c['gate_contexts'].items():self.assertAlmostEqual(self.v(m,c,'downstream'),.1*g,places=11)
 def test_block_X_not_unique(self):
  for c,g in self.c['gate_contexts'].items():
   self.assertEqual(self.v('single',c,'block_X'),0);self.assertEqual(self.v('coincidence',c,'block_X'),0);self.assertAlmostEqual(self.v('parallel',c,'block_X'),(1-math.sqrt(.8))*g,places=11)
 def test_block_Z(self):
  for c,g in self.c['gate_contexts'].items():self.assertAlmostEqual(self.v('single',c,'block_Z'),.2*g,places=11);self.assertEqual(self.v('coincidence',c,'block_Z'),0)
 def test_both_zero(self):self.assertTrue(all(x['event_probability']==0 for x in self.r['scenarios'] if x['intervention']=='block_both'))
 def test_ordinary_action_specificity(self):
  for m in ['single','parallel','coincidence']:
   for c,g in self.c['gate_contexts'].items():
    for i in ['none','block_X','block_Z','block_both']:self.assertAlmostEqual(self.d[m,c,i]['ordinary_action_probability'],.4*g)
    self.assertAlmostEqual(self.d[m,c,'downstream']['ordinary_action_probability'],.2*g)
 def test_joint_marginals(self):
  for x in self.r['coincidence_sensitivity']:
   self.assertAlmostEqual(x['p11']+x['p10'],.25);self.assertAlmostEqual(x['p11']+x['p01'],.25);self.assertAlmostEqual(sum(x[k] for k in ['p11','p10','p01','p00']),1);self.assertTrue(all(x[k]>=0 for k in ['p11','p10','p01','p00']))
 def test_output_reproduces(self):self.assertEqual(self.r,json.loads((P/'results.json').read_text()))
 def test_no_random_seed(self):self.assertIsNone(self.r['seed'])
if __name__=='__main__':unittest.main()
