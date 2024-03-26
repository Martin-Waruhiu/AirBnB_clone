#!/usr/bin/python3
"""a city class a sublass of Base Model"""

from models.base_model import BaseModel

class City(BaseModel):
    """a subclass city of the Base model"""

    state_id = ""
    name = ""
