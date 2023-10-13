#!/usr/bin/python3
"""defines a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances"""
import json


class FileStorage:
    """serializes instances to a json file and deserializes json file
    to instances"""

    """class attributes
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects"""
    __file_path = "file.json"
    __objects = {}

 
    """public methods"""
    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj
        
    def save(self):
        """serializes __objects to the JSON file"""
        objectdict = FileStorage.__objects
        objdict = {obj: objectdict[obj].to_dict() for obj in objectdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON exists"""
        try:
            with open(FileStorage.__file_path) as f:
                json.load(f)
        except FileNotFoundError:
            return
