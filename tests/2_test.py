import unittest
import sys
sys.path.append('./src')

from blackjack import *

class VariableTest(unittest.TestCase):
    def test_add_no_numbers(self):
        self.assertEqual(ranks, "J", "Variable named 'rank' should be set to 'J'")

if __name__ == '__main__':
    unittest.main()