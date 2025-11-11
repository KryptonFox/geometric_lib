import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(12)
        self.assertEqual(res, 144)

    def test_perimeter(self):
        res = perimeter(6)
        self.assertEqual(res, 24)
