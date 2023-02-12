#!/usr/bin/python3
"""
    a class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances:
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        keys = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[keys] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                load_obj = json.load(f)
                for val in load_obj.values():
                    clas = val["__class__"]
                    del val["__class__"]
                    self.new(eval(f"{clas}")(**val))

        except FileNotFoundError:
            return
