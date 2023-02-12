#!/usr/bin/python3
"""Object for managing the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city-objects"""

    name = ""
    state_id = ""
