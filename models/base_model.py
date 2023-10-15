#!/usr/bin/python3
"""defines a superclass BaseModel that defines all common attributes
/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines a superclass BaseModel & its attributes"""
    def __init__(self, *args, **kwargs):
        """instantiate with public attributes id and datetime"""
        self.id = str(uuid4())
        timefmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    """converting datetime strings into an object"""
                    self.__dict__[k] = datetime.strptime(v, timefmt)
                    self.__dict__[k] = datetime.strptime(v, timeformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    """using the str method to return the unofficial representation
    of object instances"""
    def __str__(self):
        """returns the string representation of the class name, id &
        the dictionary representation"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

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
