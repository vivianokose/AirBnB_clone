#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():

    """
    This Script serializes(encode) instances to a JSON file
    and deserializes(decode) JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """Encodes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    classes = {
            'BaseModel': BaseModel
            }

    def reload(self):
        """
        Decodes the JSON file to __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    class_name = value["__class__"]
                    if class_name in self.classes:
                        attribute_v = self.classes[class_name](**value)
                        self.__objects[key] = attribute_v
        except FileNotFoundError:
            pass
