#!/usr/bin/python3
"""defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines a class Review that inherits from BaseModel
    Args
    BaseModel - superclass"""

    """public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
