#!/usr/bin/python3
"""tests for BaseModel class"""
import unittest
from models.base_model import BaseModel
from json import loads


class TESTBASEMODEL(unittest.TestCase):
    """contains fuctions that tests the functionality
    of BaseModel class"""

    def test_save(self):
        """tests the presence of some attributes"""

        self.base = BaseModel()
        self.base.name = 'bola'
        self.base.save()
        filename = 'file.json'
        with open(filename, 'r', encoding='utf-8') as file:
            fil_cnt = file.read()
            dict_cnt = loads(fil_cnt)
        self.assertTrue('{}.{}'.format(type(self.base).__name__,
                        self.base.id) in dict_cnt)

