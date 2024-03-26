#!/usr/bin/python3
"""a child class place of the parent BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """place is a child class of the Base Model"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities_id = []
