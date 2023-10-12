#!/usr/bin/python3
"""a class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""
import JSON
from models import storage
from models.base_model import BaseModel


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
        except FileNotFoundError:
            return
