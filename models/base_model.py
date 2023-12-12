#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
""" BaseModel class"""


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, **kwargs):
        df = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            dict_copy = kwargs.copy()
            if 'created_at' in dict_copy:
                dict_copy['created_at'] = datetime.strptime(dict_copy['created_at'], df)
            if 'updated_at' in dict_copy:
                dict_copy['updated_at'] = datetime.strptime(dict_copy['updated_at'], df)
            self.__dict__ = dict_copy
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
