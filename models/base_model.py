#!/usr/bin/python3
"""a class BaseModel that defines all common attributes/methods for
other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This class lays the foundation for the hbnb application"""
    def __init__(self, *args, **kwargs):
        """Initializes the class BaseModel"""
        self.id = str(uuid4())

        """the time format should be is ISO format"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    """the str method returns unofficial object instances"""
    def __str__(self):
        """prints the class name, id and dict"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__dict__)
        return (string)

    """public instance methods"""
    def save(self):
        """updates the public instance attribute with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    """the dictionary method to store key/value pairs"""
    def to_dict(self):
        """returns key value payirs of __dict__"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return (mydict)
