#!/usr/bin/python3
"""user class tht inherits from base model"""

from models.base_model import BaseModel


class User(BaseModel):
    """User subclass inherits from the basemodel"""


    email = ""
    password = ""
    first_name = ""
    last_name = "" 
