#!/usr/bin/python3
"""
Module test_rectangle
Defines class TestRectangle
test case for Rectangle class
"""


import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.rectangle import __doc__


class TestRectangle(unittest.TestCase):
    """
    Test methods for class Rectangle
    Functions:
      setUp(self)
      tearDown(self)
      test_docstring(self)
      test_rectangle_attr(self)
    """
    def setUp(self):
        """sets up test fixture"""
        self.b1 = Rectangle(5, 6, 0, 0)
        self.b2 = Rectangle(7, 8, 1, 0)
        self.b3 = Rectangle(10, 3, 1, 1)
        self.r1 = Rectangle(3, 4)

    def tearDown(self):
        """tears down test fixtures"""
        del self.b1
        del self.b2
        del self.b3
        del self.r1

    def test_docstring(self):
        """tests doc string"""
        self.assertTrue(len(__doc__) > 1)

    def test_rectangle_attr(self):
        """tests rectangles property"""
        self.assertEqual(self.b1.width, 5)
        self.assertEqual(self.b2.height, 8)
        self.assertEqual(self.b3.x, 1)
        self.assertEqual(self.b1.y, 0)
        self.assertTrue(self.b1.id > 0)

    def test_rectangle_default_attr(self):
        """test default attributes of rectangle"""
        self.assertTrue(self.r1.width == 3)
        self.assertTrue(self.r1.height == 4)
        self.assertTrue(self.r1.x == 0)
        self.assertTrue(self.r1.y == 0)
        self.assertTrue(self.r1.id is not None)

    def test_rectangle_area(self):
        """tests areas of a rectangle"""
        self.assertEqual(self.b1.area(), 30)
        self.assertEqual(self.b2.area(), 56)
        self.assertEqual(self.b3.area(), 30)
        self.assertEqual(self.r1.area(), 12)

    def test_rectangle_raises(self):
        """tests raises on rectangle"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('7', 6, 3, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -7, 0, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 4, 3, [1, 3])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(9, 4, -1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 4, '1', 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "5")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 2, -4)

    def test_rectangle_attr_access(self):
        """Test private attributes are not accesssible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_rectangle_display(self):
        """Tests the output of __str__"""
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(2, 3).display()
            self.assertEqual(buf.getvalue(), "##\n##\n##\n")
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(1, 1, 3, 2).display()
            self.assertEqual(buf.getvalue(), "\n\n   #\n")
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(2, 2, 1, 1).display()
            self.assertEqual(buf.getvalue(), "\n ##\n ##\n")

    def test_rectangle_str(self):
        """Tests __str__ of rectangle"""
        self.assertEqual(str(Rectangle(3, 4, 0, 0, 4)),
                         "[Rectangle] (4) 0/0 - 3/4")

    def test_rectangle_update(self):
        """Tests update on rectangle"""
        self.r1.update(5)
        self.assertEqual(self.r1.id, 5)
        self.b1.update(6, 4, 5, 1, 0)
        self.assertEqual(str(self.b1), "[Rectangle] (6) 1/0 - 4/5")
        self.b2.update(width=1, y=2, id=7)
        self.assertEqual(str(self.b2), "[Rectangle] (7) 1/2 - 1/8")
        self.b3.update(44, y=2, x=1)
        self.assertEqual(str(self.b3), "[Rectangle] (44) 1/1 - 10/3")

    def test_rectangle_to_dict(self):
        """Tests to_dictionary method of rectangle"""
        self.b1.update(6, 4, 5, 1, 0)
        r2 = self.b1.to_dictionary()
        self.assertTrue(type(r2) is dict)
        self.assertEqual(r2["id"], 6)
        self.assertEqual(r2["width"], 4)
        self.assertEqual(r2["height"], 5)
        self.assertEqual(r2["x"], 1)
        self.assertEqual(r2["y"], 0)
