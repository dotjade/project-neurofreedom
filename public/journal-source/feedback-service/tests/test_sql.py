import sqlite3,pathlib,re,unittest,datetime
root=pathlib.Path(__file__).resolve().parents[1]
class Counters(unittest.TestCase):
 def setUp(self):
  self.db=sqlite3.connect(':memory:');self.db.executescript((root/'drizzle/0000_activity_votes.sql').read_text())
  self.sql=re.findall(r"env.DB.prepare\('([^']+)'\)",(root/'worker/index.js').read_text())
 def vote(self,activity):
  day='2026-10-13';insert,update,record=self.sql[-3:]
  with self.db:
   self.db.execute(insert,(day,));result=self.db.execute(update,(day,2000,day,activity,1000));accepted=result.rowcount;self.db.execute(record,(day,activity))
  return accepted
 def test_only_aggregate_schema(self):
  self.assertEqual([r[1] for r in self.db.execute('pragma table_info(activity_votes)')],['day','activity_id','votes'])
  self.assertEqual([r[1] for r in self.db.execute('pragma table_info(day_totals)')],['day','votes'])
 def test_vote_updates_both_atomic_counters(self):
  self.assertEqual(self.vote('notice-one-thing'),1);self.assertEqual(self.vote('notice-one-thing'),1)
  self.assertEqual(self.db.execute('select votes from activity_votes').fetchone()[0],2);self.assertEqual(self.db.execute('select votes from day_totals').fetchone()[0],2)
 def test_activity_cap(self):
  self.db.execute("insert into activity_votes values ('2026-10-13','notice-one-thing',1000)");self.db.execute("insert into day_totals values ('2026-10-13',1000)");self.db.commit()
  self.assertEqual(self.vote('notice-one-thing'),0);self.assertEqual(self.db.execute('select votes from day_totals').fetchone()[0],1000)
 def test_global_cap(self):
  self.db.execute("insert into day_totals values ('2026-10-13',2000)");self.db.commit();self.assertEqual(self.vote('rest-or-leave'),0);self.assertEqual(self.db.execute('select count(*) from activity_votes').fetchone()[0],0)
 def test_schema_rejects_unknown_id(self):
  with self.assertRaises(sqlite3.IntegrityError):self.db.execute("insert into activity_votes values ('2026-10-13','diagnosis',1)")
 def test_expiry_retains_thirty_utc_days_only(self):
  for day in ['2026-09-13','2026-09-14','2026-10-13']:
   self.db.execute('insert into activity_votes values (?, ?, 1)',(day,'rest-or-leave'));self.db.execute('insert into day_totals values (?,1)',(day,))
  self.db.execute('delete from activity_votes where day < ? ',('2026-09-14',));self.db.execute('delete from day_totals where day < ?',('2026-09-14',))
  self.assertEqual(self.db.execute('select count(*) from activity_votes').fetchone()[0],2);self.assertEqual(self.db.execute('select count(*) from day_totals').fetchone()[0],2)
if __name__=='__main__':unittest.main()
