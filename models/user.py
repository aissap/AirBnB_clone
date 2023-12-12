#!/usr/bin/python3
"""
User class module
"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    def __init__(self, *args, **kwargs):
        """Initialization of the User class"""
        super().__init__(*args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
