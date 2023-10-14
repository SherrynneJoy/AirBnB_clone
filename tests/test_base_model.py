#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
import os
import models


class TestBaseModel(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(BaseModel().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)

    def test_unique_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        base = BaseModel()
        base.id = "2468"
        base.created_at = base.updated_at = day
        basestr = base.__str__()
        self.assertIn("[BaseModel] (2468)", basestr)
        self.assertIn("'id': '2468'", basestr)
        self.assertIn("'created_at': " + day_repr, basestr)
        self.assertIn("'updated_at': " + day_repr, basestr)

    """to test unused arguments"""
    def test_no_args(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        base = BaseModel(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, day)
        self.assertEqual(base.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        base = BaseModel()
        sleep(0.05)
        first_update = base.updated_at
        base.save()
        self.assertLess(first_update, base.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        base = BaseModel()
        sleep(0.05)
        first_update = base.updated_at
        base.save()
        second_update = base.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        base.save()
        self.assertLess(second_update, base.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        base = BaseModel()
        base.id = "2468"
        base.created_at = base.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'BaseModel',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(base.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        base = BaseModel()
        base.name = "Joy"
        base.number = 4
        self.assertIn("name", base.to_dict())
        self.assertIn("number", base.to_dict())
