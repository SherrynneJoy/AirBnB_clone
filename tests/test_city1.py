#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.city import City
from time import sleep
from datetime import datetime
import os
import models


class TestCity(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(City, type(City()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(City(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(City().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(City().created_at))

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertNotEqual(ct1.created_at, ct2.created_at)

    def test_unique_updated_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertNotEqual(ct1.updated_at, ct2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        ct = City()
        ct.id = "2468"
        ct.created_at = ct.updated_at = day
        ctstr = ct.__str__()
        self.assertIn("[City] (2468)", ctstr)
        self.assertIn("'id': '2468'", ctstr)
        self.assertIn("'created_at': " + day_repr, ctstr)
        self.assertIn("'updated_at': " + day_repr, ctstr)

    """to test unused arguments"""
    def test_no_args(self):
        ct = City(None)
        self.assertNotIn(None, ct.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        ct = City(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(ct.id, "123")
        self.assertEqual(ct.created_at, day)
        self.assertEqual(ct.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        ct = City()
        sleep(0.05)
        first_update = ct.updated_at
        ct.save()
        self.assertLess(first_update, ct.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        ct = City()
        sleep(0.05)
        first_update = ct.updated_at
        ct.save()
        second_update = ct.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        ct.save()
        self.assertLess(second_update, ct.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        ct = City()
        with self.assertRaises(TypeError):
            ct.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        ct = City()
        self.assertTrue(dict, type(ct.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        ct = City()
        self.assertIn("id", ct.to_dict())
        self.assertIn("created_at", ct.to_dict())
        self.assertIn("updated_at", ct.to_dict())
        self.assertIn("__class__", ct.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        ct = City()
        ct_dict = ct.to_dict()
        self.assertEqual(str, type(ct_dict["created_at"]))
        self.assertEqual(str, type(ct_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        ct = City()
        ct.id = "2468"
        ct.created_at = ct.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'City',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(ct.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        ct = City()
        with self.assertRaises(TypeError):
            ct.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        ct = City()
        ct.name = "Joy"
        ct.number = 4
        self.assertIn("name", ct.to_dict())
        self.assertIn("number", ct.to_dict())


if __name__ == '__main__':
    unittest.main()
