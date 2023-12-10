#!/usr/bin/python3
""" FileStorage class """
import json


class FileStorage:
    """Class for handling serialization and deserialization of objects."""
    def __init__(self):
        """Constructor for FileStorage."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return a dictionary of objects, filtered by the provided class."""

        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary of objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serialize objects to the JSON file."""
        list_objects = {key: value for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(list_objects, file)

    def reload(self):
        """Deserialize objects from the JSON file and reload into __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                objects_json = json.loads(file.read())
                for obj in objects_json.values():
                    key = "{}.{}".format(obj["__class__"], obj["id"])
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def destroy(self, obj):
        """Remove the specified object from __objects."""
        obj_key = "{}.{}".format(obj["__class__"], obj["id"])
        del self.__objects[obj_key]

    def update(self, obj, attribute_key, attribute_value):
        """Update the specified object's attribute."""
        obj_key = "{}.{}".format(obj["__class__"], obj["id"])
        obj[attribute_key] = attribute_value
        self.__objects[obj_key] = obj
