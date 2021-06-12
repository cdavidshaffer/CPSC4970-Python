import math_tools
import unittest


class MathToolsTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(25, math_tools.square(5))

    def test_square_of_negative(self):
        self.assertEqual(169, math_tools.square(-13))


