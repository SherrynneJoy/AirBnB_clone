#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherits attributes and methods of BaseModel"""
    state_id = ""
    name = ""
