#!/usr/bin/python3
"""defines a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """creates a sub-class User
    Args
    BaseModel - superclass"""

    """public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
