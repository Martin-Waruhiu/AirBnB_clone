#!/usr/bin/python3
"""the class for serialization and deseriliazation"""

import json
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    "serialazation and deserialization"""

    __file_path = "file_path"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """sets in _-objects the obj as classname.id
        This allows for efficient storage and 
        retrieval of objects within the FileStorage class."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialises __objects to json filepath"""

        js_dict = {}
        for key, obj in FileStorage.__objects.items():
            js_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(js_dict, f)

    def reload(self):
        """deserialzes fro json to objects"""

        try:
            with open(FileStorage.__file_path) as f:
                py_dict = json.load(f)
                for i in py_dict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            print("invalid format")
