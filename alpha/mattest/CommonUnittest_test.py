import unittest
import Common    # The code to test

class Test_idToColumnName(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Common.idToColumnName(1, 8), 'a')

if __name__ == '__main__':
    unittest.main()