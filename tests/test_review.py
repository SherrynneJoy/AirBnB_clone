#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.review import Review
from time import sleep
from datetime import datetime
import os
import models


class TestReview(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(Review, type(Review()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(Review(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(Review().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(Review().created_at))

    """to test whether user_id is a public attribute"""
    def test_user_id(self):
        """tests the id attribute"""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    """to test whether place_id is a public attribute"""
    def test_place_id(self):
        """tests the id attribute"""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    """to test whether text is a public attribute"""
    def test_text(self):
        """tests the id attribute"""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertNotEqual(rv1.created_at, rv2.created_at)

    def test_unique_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertNotEqual(rv1.updated_at, rv2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        rv = Review()
        rv.id = "2468"
        rv.created_at = rv.updated_at = day
        rvstr = rv.__str__()
        self.assertIn("[Review] (2468)", rvstr)
        self.assertIn("'id': '2468'", rvstr)
        self.assertIn("'created_at': " + day_repr, rvstr)
        self.assertIn("'updated_at': " + day_repr, rvstr)

    """to test unused arguments"""
    def test_no_args(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        rv = Review(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(rv.id, "123")
        self.assertEqual(rv.created_at, day)
        self.assertEqual(rv.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        rv = Review()
        sleep(0.05)
        first_update = rv.updated_at
        rv.save()
        self.assertLess(first_update, rv.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        rv = Review()
        sleep(0.05)
        first_update = rv.updated_at
        rv.save()
        second_update = rv.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        rv.save()
        self.assertLess(second_update, rv.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        rv = Review()
        self.assertTrue(dict, type(rv.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        rv = Review()
        rv.id = "2468"
        rv.created_at = rv.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'Review',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(rv.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        rv = Review()
        rv.name = "Joy"
        rv.number = 4
        self.assertIn("name", rv.to_dict())
        self.assertIn("number", rv.to_dict())


if __name__ == '__main__':
    unittest.main()
