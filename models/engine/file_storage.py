#!/usr/bin/python3
"""The module coatain a class that handles the storing and reloading of data
The flow of serialization and dserialization:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> ->
<class 'BaseModel'>"""


from json import dumps, loads


class FileStorage:
    """This class handles serialzation of instances to json file
    and deserialization of the from json file to instances"""

    __file_path = "file.json"  # path to json file
    __objects = {}  # will store objects by their classname.id

    def all(self):
        """returns the dictionary '__objects'"""
        return (__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        __object[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as file_save:
            file_save.write(dumps(__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file_load:
                file_content = file_load.read()
                py_obj = loads(file_content)
        except Exception:
            pass
















