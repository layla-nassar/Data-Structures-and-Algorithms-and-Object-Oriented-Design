# 1. import unittest and Import the class that you need to test
import unittest
from Shape import Color, Shape, Rectangle

#2 Create test class and extend unittest.TestCse
class TestColor(unittest.TestCase):
    #3 Create methods(test cases ) that start with word "test" to test each function in the class
    def test_color(self):
        c1 = Color("White")
        self.assertEqual(c1.get_color(), "White")
        c1.set_color("Red")
        self.assertEqual(c1.get_color(), "Red")

class TestShape(unittest.TestCase):
    def test_shape_area(self):
        s1 = Shape()
        self.assertEqual(s1.area(), "Shape area")
    
    def test_shape_color(self):
        s1 = Shape()
        self.assertEqual(s1.get_color(), "White")

class TestRect(unittest.TestCase):
    def test_rect(self):
        r1 = Rectangle(3,4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)

    def test_area123(self):
        r1 =Rectangle(3,4)
        self.assertEqual(r1.area(), 12)

    def test__rep_(self):
        r1 = Rectangle(3,5)
        self.assertEqual(r1.__repr__(), "This is a rectangle of area 15")

if __name__ == "__main__":
    #4 Run the code by calling unittest.main()
    unittest.main()

