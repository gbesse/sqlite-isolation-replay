import unittest
from sqlite_isolation_replay.core import run
class DomainTests(unittest.TestCase):
 def test_snapshot(self):
  x=run({'value':7});self.assertEqual([x[k]for k in ['before','uncommitted','snapshot_after_commit','fresh_after_restart']],[1,1,1,7]);self.assertIn(x['upgrade_error'],['SQLITE_BUSY_SNAPSHOT','SQLITE_BUSY'])
 def test_negative(self):self.assertEqual(run({'value':-3})['fresh_after_restart'],-3)
 def test_boolean_rejected(self):
  with self.assertRaises(ValueError):run({'value':True})
