#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.user import User
from time import sleep
from datetime import datetime
import os
import models


class TestUser(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(User, type(User()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(User(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(User().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(User().created_at))

    """to test whether email is a public attribute"""
    def test_email_public(self):
        self.assertEqual(str, type(User.email))

    """to test whether password is a public attribute"""
    def test_password_public(self):
        self.assertEqual(str, type(User.password))

    """to test whether firstname is a public attribute"""
    def test_first_name_public(self):
        self.assertEqual(str, type(User.first_name))

    """to test whether lastname is a public attribute"""
    def test_last_name_public(self):
        self.assertEqual(str, type(User.last_name))

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertNotEqual(usr1.created_at, usr2.created_at)

    def test_unique_updated_at(self):
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertNotEqual(usr1.updated_at, usr2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        usr = User()
        usr.id = "2468"
        usr.created_at = usr.updated_at = day
        usrstr = usr.__str__()
        self.assertIn("[User] (2468)", usrstr)
        self.assertIn("'id': '2468'", usrstr)
        self.assertIn("'created_at': " + day_repr, usrstr)
        self.assertIn("'updated_at': " + day_repr, usrstr)

    """to test unused arguments"""
    def test_no_args(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        usr = User(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(usr.id, "123")
        self.assertEqual(usr.created_at, day)
        self.assertEqual(usr.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        usr = User()
        sleep(0.05)
        first_update = usr.updated_at
        usr.save()
        self.assertLess(first_update, usr.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        usr = User()
        sleep(0.05)
        first_update = usr.updated_at
        usr.save()
        second_update = usr.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        usr.save()
        self.assertLess(second_update, usr.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        usr = User()
        self.assertTrue(dict, type(usr.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        usr = User()
        usr.id = "2468"
        usr.created_at = usr.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'User',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(usr.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        usr = User()
        usr.name = "Joy"
        usr.number = 4
        self.assertIn("name", usr.to_dict())
        self.assertIn("number", usr.to_dict())


if __name__ == '__main__':
    unittest.main()
