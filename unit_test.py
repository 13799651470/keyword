import unittest

from 关键字 import row_totalnum
from 关键字 import row_switchnum
from 关键字 import row_casenum

class KeywordTest(unittest.TestCase):

    def test_row_totalnum(self):
        totalnum = row_totalnum(['if',' ','else'])
        self.assertEqual(totalnum, 2)  # add assertion here
        totalnum = row_totalnum(['i','love','coding'])
        self.assertEqual(totalnum, 0) 


    def test_row_switchnum(self):
        switchnum = row_switchnum(['case',' ','switch','swutchs','switch'])
        self.assertEqual(switchnum,2)
        switchnum = row_switchnum(['case',' ','switchs','swutchs','switch'])
        self.assertEqual(switchnum,1)

    
    def test_row_casenum(self):
        casenum = row_casenum(['if','case',' '])
        self.assertEqual(casenum,1)
        casenum = row_casenum(['if','case','case'])
        self.assertEqual(casenum,2)



if __name__ == '__main__':
    unittest.main()
