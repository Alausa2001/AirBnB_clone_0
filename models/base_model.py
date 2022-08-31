#!/usr/bin/python3
"""This module contain the parent class from which other classes inherit"""


from datetime import datetime
import uuid

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """initializes the instances with
        -- a unique id
        -- time created
        -- time updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """returns the string representation of the instance attributes"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        dict_copy = self.__dict__
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].strftime(time_format)
        dict_copy['updated_at'] = dict_copy['updated_at'].strftime(time_format)
        return(dict_copy)
