#!/usr/bin/python3
"""defines unittests for class FileStorage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import models
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstance(unittest.TestCase):
    """tests the instatiation of FileStorage"""
    def testInstantiationWithNoArgs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def testInstatiationWithArg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testPrivateFilePath(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testPrivateFileStorageObjects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorageMethods(unittest.TestCase):
    """tests the public instance methods of FileStorage"""
    @classmethod
    def Setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def Delete(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def testAllWithArgs(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def testNew(self):
        bs = BaseModel()
        u = User()
        St = State()
        Plc = Place()
        Ct = City()
        Amnty = Amenity()
        Rvw = Review()
        models.storage.new(bs)
        models.storage.new(u)
        models.storage.new(St)
        models.storage.new(Plc)
        models.storage.new(Ct)
        models.storage.new(Amnty)
        models.storage.new(Rvw)
        self.assertIn("BaseModel." + bs.id, models.storage.all().keys())
        self.assertIn(bs, models.storage.all().values())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())
        self.assertIn("State." + St.id, models.storage.all().keys())
        self.assertIn(St, models.storage.all().values())
        self.assertIn("Place." + Plc.id, models.storage.all().keys())
        self.assertIn(Plc, models.storage.all().values())
        self.assertIn("City." + Ct.id, models.storage.all().keys())
        self.assertIn(Ct, models.storage.all().values())
        self.assertIn("Amenity." + Amnty.id, models.storage.all().keys())
        self.assertIn(Amnty, models.storage.all().values())
        self.assertIn("Review." + Rvw.id, models.storage.all().keys())
        self.assertIn(Rvw, models.storage.all().values())

        def testWithNew(self):
            with self.assertRaises(TypeError):
                models.storage.new(BaseModel(), 1)

        def testSave(self):
            bs = BaseModel()
            u = User()
            St = State()
            Plc = Place()
            Ct = City()
            Amnty = Amenity()
            Rvw = Review()
            models.storage.new(bs)
            models.storage.new(u)
            models.storage.new(St)
            models.storage.new(Plc)
            models.storage.new(Ct)
            models.storage.new(Amnty)
            models.storage.new(Rvw)
            models.storage.save()
            save_txt = ""
            with open("file.json", "r") as f:
                save_txt = f.read()
                self.assertIn("BaseModel." + bs.id, save_txt)
                self.assertIn("User." + u.id, save_txt)
                self.assertIn("State." + St.id, save_txt)
                self.assertIn("Place." + Plc.id, save_txt)
                self.assertIn("City." + Ct.id, save_txt)
                self.assertIn("Amenity." + Amnty.id, save_txt)
                self.assertIn("Review." + Rvw.id, save_txt)

    def testReload(self):
        bs = BaseModel()
        u = User()
        St = State()
        Plc = Place()
        Ct = City()
        Amnty = Amenity()
        Rvw = Review()
        models.storage.new(bs)
        models.storage.new(u)
        models.storage.new(St)
        models.storage.new(Plc)
        models.storage.new(Ct)
        models.storage.new(Amnty)
        models.storage.new(Rvw)
        models.storage.save()
        models.storage.reload()
        Objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bs.id, Objects)
        self.assertIn("User." + u.id, Objects)
        self.assertIn("State." + St.id, Objects)
        self.assertIn("Place." + Plc.id, Objects)
        self.assertIn("City." + Ct.id, Objects)
        self.assertIn("Amenity." + Amnty.id, Objects)
        self.assertIn("Review." + Rvw.id, Objects)

    def testReloadWithArgs(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == '__main__':
    unittest.main()
