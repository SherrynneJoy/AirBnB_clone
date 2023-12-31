#!/usr/bin/python3
"""a class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JOSN file and deserializes JSON file to
    instances"""
    __file_path = "file.json"
    __objects = {}

    """public instance methods"""
    def all(self):
        """returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        mydict = FileStorage.__objects
        objdict = {obj: mydict[obj].to_dict() for obj in mydict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
