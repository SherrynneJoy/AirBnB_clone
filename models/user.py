#!/usr/bin/python3
"""a class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits attributes and methods from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
