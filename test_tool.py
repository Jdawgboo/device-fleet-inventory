import unittest
from tool import summarize
class InventoryTests(unittest.TestCase):
 def test_summary(self):
  report=summarize([{'id':'1','model':'x','firmware':'1','health':'ok'},{'id':'1','model':'x'}]);self.assertEqual(report['models'],{'x':2});self.assertIn('row 1: duplicate id',report['errors']);self.assertIn('row 1: missing firmware',report['errors'])
if __name__=='__main__':unittest.main()
