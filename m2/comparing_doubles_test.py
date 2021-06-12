import unittest


class ComparingDoubles(unittest.TestCase):
    def test_that_fails(self):
        self.assertEqual(0.3, 0.1 + 0.1 + 0.1)

    def test_that_passes(self):
        self.assertAlmostEqual(0.3, 0.1 + 0.1 + 0.1)

    def test_that_specifies_precision(self):
        self.assertAlmostEqual(0.3, 0.1 + 0.1 + 0.1,
                               places=5)


if __name__ == '__main__':
    unittest.main()