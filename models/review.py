#!/usr/bin/python3
"""this module contain a class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """module inherits BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
