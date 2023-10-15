#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.place import Place
from time import sleep
from datetime import datetime
import os
import models


class TestPlace(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(Place, type(Place()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(Place(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(Place().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(Place().created_at))

    """to test whether city_id is a public attribute"""
    def test_city_id(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    """to test whether user_id is a public attribute"""
    def test_user_id(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    """to test whether name is a public attribute"""
    def test_name(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    """to test whether description is a public attribute"""
    def description(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("description", pl.__dict__)

    """to test whether number_rooms is a public attribute"""
    def test_number_rooms(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    """to test whether number_rooms is a public attribute"""
    def test_number_bathrooms(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    """to test whether max_guest is a public attribute"""
    def test_max_guest(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    """to test whether price_by_night is a public attribute"""
    def test_price_by_night(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    """to test whether latitude is a public attribute"""
    def test_latitude(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    """to test whether longitude is a public attribute"""
    def test_longitude(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    """to test whether amenity_ids is a public attribute"""
    def test_amenity_ids(self):
        """tests the id attribute"""
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertNotEqual(pl1.created_at, pl2.created_at)

    def test_unique_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertNotEqual(pl1.updated_at, pl2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        pl = Place()
        pl.id = "2468"
        pl.created_at = pl.updated_at = day
        plstr = pl.__str__()
        self.assertIn("[Place] (2468)", plstr)
        self.assertIn("'id': '2468'", plstr)
        self.assertIn("'created_at': " + day_repr, plstr)
        self.assertIn("'updated_at': " + day_repr, plstr)

    """to test unused arguments"""
    def test_no_args(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        pl = Place(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(pl.id, "123")
        self.assertEqual(pl.created_at, day)
        self.assertEqual(pl.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        pl = Place()
        sleep(0.05)
        first_update = pl.updated_at
        pl.save()
        self.assertLess(first_update, pl.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        pl = Place()
        sleep(0.05)
        first_update = pl.updated_at
        pl.save()
        second_update = pl.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        pl.save()
        self.assertLess(second_update, pl.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        pl = Place()
        self.assertTrue(dict, type(pl.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        pl = Place()
        pl.id = "2468"
        pl.created_at = pl.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'Place',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(pl.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        pl = Place()
        pl.name = "Joy"
        pl.number = 4
        self.assertIn("name", pl.to_dict())
        self.assertIn("number", pl.to_dict())


if __name__ == '__main__':
    unittest.main()
