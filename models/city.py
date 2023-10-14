#!/usr/bin/python3
"""defines a class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines a class City that inherits from BaseModel
    Args
    BaseModel - superclass"""

    """public class attributes"""
    state_id = ""
    name = ""
