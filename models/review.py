#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits attributes and methods of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
