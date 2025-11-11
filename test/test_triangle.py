import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(3, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(4, 4)
        self.assertEqual(res, 8)

    def test_area(self):
        res = area(12, 10)
        self.assertEqual(res, 60)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
