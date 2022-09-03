#!/usr/bin/python3
"""The module coatain a class that handles the storing and reloading of data
The flow of serialization and dserialization:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> ->
<class 'BaseModel'>"""


from json import dumps, loads
from models import base_model


class FileStorage:
    """This class handles serialzation of instances to json file
    and deserialization of the from json file to instances"""

    __file_path = "file.json"  # path to json file
    __objects = {}  # will store objects by their classname.id

    def all(self):
        """returns the dictionary '__objects'"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # in order to make the BaseModel serializable it has to be converted
        # to dictionary

        dict_format = {}  # dict format of FileStorage.__objects
        for key, value in self.__objects.items():
            if value:
                dict_format[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file_save:
            file_save.write(dumps(dict_format, indent=4))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        cls = {'Review': Review, 'Place': Place, 'State': State,
               'BaseModel': BaseModel, 'User': User, 'City': City,
               'Amenity': Amenity}

        try:
            with open(self.__file_path, 'r') as file_load:
                file_content = file_load.read()
                pd = loads(file_content)
                for key in pd.keys():
                    self.__objects[key] = cls[pd[key]['__class__']](**pd[key])
        except Exception:
            pass
