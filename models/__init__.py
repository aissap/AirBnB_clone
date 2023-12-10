#!/usr/bin/python3
""" instantiates the storage system """


from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

my_models = ["BaseModel", "User", "Amenity", "City",
             "Place", "Review", "State", "User"]
