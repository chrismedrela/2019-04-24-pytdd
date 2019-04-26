import unittest

import calc


class TestAddition(unittest.TestCase):
    def test_addition(self):
        expected = 130.0
        got = calc.add(30.0, 100)
        self.assertAlmostEqual(expected, got)
