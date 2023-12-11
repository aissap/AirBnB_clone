#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines the 'city' class"""


class City(BaseModel):
    """
    Class representing cities.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
