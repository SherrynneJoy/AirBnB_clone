#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.amenity import Amenity
from time import sleep
from datetime import datetime
import os
import models


class TestAmenity(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(Amenity().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertNotEqual(am1.created_at, am2.created_at)

    def test_unique_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertNotEqual(am1.updated_at, am2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        am = Amenity()
        am.id = "2468"
        am.created_at = am.updated_at = day
        amstr = am.__str__()
        self.assertIn("[Amenity] (2468)", amstr)
        self.assertIn("'id': '2468'", amstr)
        self.assertIn("'created_at': " + day_repr, amstr)
        self.assertIn("'updated_at': " + day_repr, amstr)

    """to test unused arguments"""
    def test_no_args(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        am = Amenity(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(am.id, "123")
        self.assertEqual(am.created_at, day)
        self.assertEqual(am.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        am = Amenity()
        sleep(0.05)
        first_update = am.updated_at
        am.save()
        self.assertLess(first_update, am.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        am = Amenity()
        sleep(0.05)
        first_update = am.updated_at
        am.save()
        second_update = am.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        am.save()
        self.assertLess(second_update, am.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        am = Amenity()
        self.assertTrue(dict, type(am.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        am = Amenity()
        am.id = "2468"
        am.created_at = am.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'Amenity',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(am.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        am = Amenity()
        am.name = "Joy"
        am.number = 4
        self.assertIn("name", am.to_dict())
        self.assertIn("number", am.to_dict())


if __name__ == '__main__':
    unittest.main()
