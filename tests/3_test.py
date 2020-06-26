import unittest
import sys
sys.path.append('./tests')

from utils import *

class VariableTest(unittest.TestCase):
    def test_add_no_numbers(self):
        self.assertEqual(getLastCommand(), "python3 blackjack.py", "entered correct last command")
        self.assertEqual(getCwd(), "/home/strove/project", "entered in correct directory")

if __name__ == '__main__':
    unittest.main()

# solution
