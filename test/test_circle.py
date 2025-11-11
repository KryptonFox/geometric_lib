import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_zero_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(5)
        excepted = math.pi * 25
        self.assertEqual(res, excepted)

    def test_perimeter(self):
        res = perimeter(5)
        excepted = math.pi * 10
        self.assertEqual(res, excepted)
