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
    def __init__(self, state_id="", name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = name
