import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
    def test_init(self):
        """Tests that points are initialied with the correct attributes"""
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
    def test_eq(self):
        """Tests that points are equal to each other."""
        self.assertEqual()
        self.assertNotequal()
    def test_equidistant(self):
        """Tests if the points are from equal distance from each other."""
        self.assertEqual()
        self.assertNotEqual()
    def test_within(self):
        """Tests if the points are within a certain criteria."""
        self.assertEqual()
        self.assertNotEqual()


unittest.main()