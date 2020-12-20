import Common    # The code to test
import unittest   # The test framework

class Test_numberToColumnName(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Common.numberToColumnName(1), 'a')

if __name__ == '__main__':
    unittest.main()