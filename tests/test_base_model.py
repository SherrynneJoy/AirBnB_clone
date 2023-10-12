#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.base_model import BaseModel
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
        self.assertIn("'id: 2468'", basestr)
        self.assertIn("'created_at': " + day_repr, basestr)
        self.assertIn("'updated_at': " + day_repr, basestr)

    """to test unused arguments"""
    def test_no_args(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = datetime.isoformat()
        base = BaseModel(id = "123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, day)
        self.assertEqual(base.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

"""creating a class to test the save function"""
class test_save(self):
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
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
