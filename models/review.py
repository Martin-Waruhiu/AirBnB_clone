#!/usr/bin/python3
"""review a child class of the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a class to show the revies of the specific class"""

    place_id = ""
    user_id = ""
    text = ""
