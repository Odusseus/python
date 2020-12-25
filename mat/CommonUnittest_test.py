import unittest
import Common    # The code to test

class Test_numberToColumnName(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Common.numberToColumnName(1, 8), 'a')

if __name__ == '__main__':
    unittest.main()