#!/usr/bin/python3
"""
Module test_base
Defines class TestBase
tests Base class
"""


import json
import os
import unittest
from models.base import Base
from models.base import __doc__
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Test case for Base class
    Inherits from unittest.TestCase
    Functions:
      def test_base(self)
    """

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_module_docstring(self):
        self.assertTrue(len(__doc__) > 1)

    def test_base(self):
        """Tests Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(1)
        self.assertEqual(b2.id, 1)
        b3 = Base(4)
        self.assertEqual(b3.id, 4)
        b4 = Base()
        self.assertEqual(b4.id, 2)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_base_JSON_str(self):
        """Tests JSON string fromat"""
        b1 = Rectangle(7, 4, 3, 2, 1)
        dic = b1.to_dictionary()
        self.assertTrue(Base.to_json_string(None) == "[]")
        self.assertTrue(Base.to_json_string([]) == "[]")
        self.assertTrue(type(Base.to_json_string([dic])) is str)

    def test_base_none_to_json_string(self):
        """Test no dict given translates into JSON string of empty dict"""
        d2 = None
        strd2 = Base.to_json_string([d2])
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty dict"""
        d3 = dict()
        strd3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3, "[]")

    def test_base_save_file(self):
        """Tests JSON save to file"""
        b1 = Rectangle(4, 5)
        b2 = Rectangle(8, 7)
        Rectangle.save_to_file([b1, b2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.dumps([b1.to_dictionary(),
                             b2.to_dictionary()]), f.read())

    def test_base_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_base_from_json_string(self):
        """Test from_json_string method"""
        b1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        dic = Base.from_json_string(b1)
        self.assertTrue(type(b1) == str)
        self.assertTrue(type(dic) == list)
        self.assertTrue(type(dic[0]) == dict)
        self.assertEqual(dic[0],
                         {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_base_from_none_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_base_create(self):
        """Tests create method of bass"""
        b1 = Rectangle(3, 4, 1, 0, 90)
        dic = b1.to_dictionary()
        b2 = Rectangle.create(**dic)
        self.assertEqual(str(b1), '[Rectangle] (90) 1/0 - 3/4')
        self.assertEqual(str(b2), '[Rectangle] (90) 1/0 - 3/4')
        self.assertIsNot(b1, b2)

    def test_base_load_from_file(self):
        """Test load from file"""
        b1 = Rectangle(10, 7, 2, 3, 89)
        b2 = Rectangle(8, 9, 0, 1, 90)
        Rectangle.save_to_file([b1, b2])
        dic = Rectangle.load_from_file()
        self.assertEqual(len(dic), 2)
        for k, v in enumerate(dic):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (89) 2/3 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (90) 0/1 - 8/9')

    def test_base_load_from_none_file(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_base_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)
