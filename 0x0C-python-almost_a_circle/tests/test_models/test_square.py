#!/usr/bin/python3
"""
Module test_square
Defines class TestSquare
test case for Rectangle class
"""


import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from models.square import Square
from models.square import __doc__


class TestSquare(unittest.TestCase):
    """
    Test methods for class Square
    Functions:
      setUp(self)
      tearDown(self)
      test_docstring(self)
    """
    def setUp(self):
        """sets up test fixture"""
        self.b1 = Square(5)
        self.b2 = Square(8, 1, 0, 12)
        self.b3 = Square(10, 3, 1, 1)
        self.r1 = Square(3, 2, 0, 4)

    def tearDown(self):
        """tears down test fixtures"""
        del self.b1
        del self.b2
        del self.b3
        del self.r1

    def test_docstring(self):
        """tests doc string"""
        self.assertTrue(len(__doc__) > 1)

    def test_square_attr(self):
        """tests rectangles property"""
        self.assertEqual(self.b1.width, 5)
        self.assertEqual(self.b2.height, 8)
        self.assertEqual(self.b3.x, 3)
        self.assertEqual(self.b3.y, 1)
        self.assertTrue(self.b3.id == 1)

    def test_square_default_attr(self):
        """test default attributes of rectangle"""
        self.assertTrue(self.b1.width == 5)
        self.assertTrue(self.b1.height == 5)
        self.assertTrue(self.b1.x == 0)
        self.assertTrue(self.b1.y == 0)
        self.assertTrue(self.b1.id is not None)

    def test_square_area(self):
        """tests areas of a rectangle"""
        self.assertEqual(self.b1.area(), 25)
        self.assertEqual(self.b2.area(), 64)
        self.assertEqual(self.b3.area(), 100)
        self.assertEqual(self.r1.area(), 9)

    def test_square_raises(self):
        """tests raises on rectangle"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('7', 6, 3, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 3, [1, 3])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(9, -1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, '1', 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -4)

    def test_square_attr_access(self):
        """Test private attributes are not accesssible"""
        with self.assertRaises(AttributeError):
            print(Square.__width)
            print(Square.__height)
            print(Square.__x)
            print(Square.__y)

    def test_square_display(self):
        """Tests the output of display"""
        with StringIO() as buf, redirect_stdout(buf):
            Square(2).display()
            self.assertEqual(buf.getvalue(), "##\n##\n")
        with StringIO() as buf, redirect_stdout(buf):
            Square(1, 3, 2).display()
            self.assertEqual(buf.getvalue(), "\n\n   #\n")
        with StringIO() as buf, redirect_stdout(buf):
            Square(3, 1, 1).display()
            self.assertEqual(buf.getvalue(), "\n ###\n ###\n ###\n")

    def test_square_str(self):
        """Tests __str__ of square"""
        self.assertEqual(str(Square(3, 1, 0, 4)),
                         "[Square] (4) 1/0 - 3")

    def test_square_update(self):
        """Tests update on square"""
        self.r1.update(5)
        self.assertEqual(self.r1.id, 5)
        self.b1.update(6, 4, 1)
        self.assertEqual(str(self.b1), "[Square] (6) 1/0 - 4")
        self.b2.update(size=1, y=2, id=7)
        self.assertEqual(str(self.b2), "[Square] (7) 1/2 - 1")
        self.b3.update(44, y=2, x=1)
        self.assertEqual(str(self.b3), "[Square] (44) 3/1 - 10")

    def test_square_to_dict(self):
        """Test to_dictionary method"""
        self.b1.update(6, 4, 1)
        r2 = self.b1.to_dictionary()
        self.assertTrue(type(r2) is dict)
        self.assertEqual(r2["id"], 6)
        self.assertEqual(r2["size"], 4)
        self.assertEqual(r2["x"], 1)
        self.assertEqual(r2["y"], 0)
