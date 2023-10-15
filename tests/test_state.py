#!/usr/bin/python3
"""tests the attributes and methods in the BaseModel"""
import unittest
from models.state import State
from time import sleep
from datetime import datetime
import os
import models


class TestState(unittest.TestCase):
    """tests the functionality of the base class"""
    def test_args(self):
        self.assertEqual(State, type(State()))

    """to test whether the instances are stored in objects"""
    def test_instance_storage(self):
        self.assertIn(State(), models.storage.all().values())

    """to test whether the id is a public attribute"""
    def test_public_id(self):
        self.assertEqual(str, type(State().id))

    """to test whether the datetime attributes are public attributes"""
    def test_created_at_public(self):
        self.assertEqual(datetime, type(State().created_at))

    """to test whether two instances have unique ids"""
    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    """to test whether two instances have different daytimes"""
    def test_unique_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_unique_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertNotEqual(state1.updated_at, state2.updated_at)

    """testing the __str__ method"""
    def test_str(self):
        day = datetime.today()
        day_repr = repr(day)
        state = State()
        state.id = "2468"
        state.created_at = state.updated_at = day
        statestr = state.__str__()
        self.assertIn("[State] (2468)", statestr)
        self.assertIn("'id': '2468'", statestr)
        self.assertIn("'created_at': " + day_repr, statestr)
        self.assertIn("'updated_at': " + day_repr, statestr)

    """to test unused arguments"""
    def test_no_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    """testing the use of keyword args"""
    def test_kwargs(self):
        day = datetime.today()
        day_iso = day.isoformat()
        state = State(id="123", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, day)
        self.assertEqual(state.updated_at, day)

    """testing no args"""
    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


"""creating a class to test the save function"""


class test_save(unittest.TestCase):
    """tests the functionality of the save function"""
    def test_update(self):
        state = State()
        sleep(0.05)
        first_update = state.updated_at
        state.save()
        self.assertLess(first_update, state.updated_at)

    """testing the save function when two objects are made"""
    def test_two_updates(self):
        state = State()
        sleep(0.05)
        first_update = state.updated_at
        state.save()
        second_update = state.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        state.save()
        self.assertLess(second_update, state.updated_at)

    """testing whether save works with args"""
    def test_save_args(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)


"""a class to test the __dict__"""


class test_dict(unittest.TestCase):
    """Tests the functionality of the __dict__"""
    def test_type(self):
        state = State()
        self.assertTrue(dict, type(state.to_dict()))

    """testing whether the dictionary has the stipulated keys"""
    def test_right_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    """to test whether datetime attributes are strings"""
    def test_datetime(self):
        """tests the datetime function"""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    """testing the dict output"""
    def test_dict_output(self):
        """tests for correct output"""
        date = datetime.today()
        state = State()
        state.id = "2468"
        state.created_at = state.updated_at = date
        mydict = {
                'id': '2468',
                '__class__': 'State',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(state.to_dict(), mydict)

    """testing the dictionary with args"""
    def test_dict_args(self):
        """testing with args"""
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    """testing for added attributes"""
    def test_added_attributes(self):
        """checks for added attributes"""
        state = State()
        state.name = "Joy"
        state.number = 4
        self.assertIn("name", state.to_dict())
        self.assertIn("number", state.to_dict())


if __name__ == '__main__':
    unittest.main()
