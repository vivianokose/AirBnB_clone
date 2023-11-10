#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():
    """
    This Script serializes(encode) instances to a JSON file
    and deserializes(decode) JSON file to instances
    """
    __file_path = file.json
    __objects = {}

    def all(self):
        """Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Encodes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dictionary = {key: obj.to_dict()
                for key, obj in self.__objects.items()}
            json.dump(dictionary, f)

    def reload(self):
        """
        Decodes the JSON file to __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        pass
