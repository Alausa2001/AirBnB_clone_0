#!/usr/bin/python3
"""this module contains a class 'User' and it inherit from basemodel"""


from models.base_model import BaseModel


class User(BaseModel):
    """inherits BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = "" 
