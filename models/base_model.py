#!/usr/bin/python3
"""This is the base model class"""


from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """The base model"""
    def __init__(self, *args, **kwargs):
        """initialization"""

        time_fom = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_fom)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new()

    def to_dict(self):
        """converting to a dict for serilization"""
        mod_dict = self.__dict__.copy()
        mod_dict["__class__"] = self.__class__.__name__
        mod_dict["created_at"] = self.created_at.isoformat()
        mod_dict["updated_at"] = self.updated_at.isoformat()
        return mod_dict

    def save(self):
        """updated datime to now"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """converting obj to string represanation"""
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))
