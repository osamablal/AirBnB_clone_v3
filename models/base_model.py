#!/usr/bin/python3
"""
The BaseModel Class Of Module.
"""

import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

"""
    Creating instence of Base Or using the class Base.
"""
if STORAGE_TYPE == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """
        The Attrebutes and func of base-model.
    """

    if STORAGE_TYPE == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
            Instancing or initiating a new base-model.
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()

    def __set_attributes(self, attr_dict):
        """
            Setting attribute to class attribute.
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())
        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.strptime(
                attr_dict['created_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        if 'updated_at' not in attr_dict:
            attr_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['updated_at'], datetime):
            attr_dict['updated_at'] = datetime.strptime(
                attr_dict['updated_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        if STORAGE_TYPE != 'db':
            attr_dict.pop('__class__', None)
        for attr, val in attr_dict.items():
            setattr(self, attr, val)

    def __is_serializable(self, obj_v):
        """
            Knowing if object serializes.
        """
        try:
            obj_to_str = json.dumps(obj_v)
            return obj_to_str is not None and isinstance(obj_to_str, str)
        except:
            return False

    def bm_update(self, attr_dict=None):
        """
            Updating base-model and give true attributes.
        """
        IGNORE = [
            'id', 'created_at', 'updated_at', 'email',
            'state_id', 'user_id', 'city_id', 'place_id'
        ]
        if attr_dict:
            updated_dict = {
                k: v for k, v in attr_dict.items() if k not in IGNORE
            }
            for key, value in updated_dict.items():
                setattr(self, key, value)
            self.save()

    def save(self):
        """
            Changing attribute update to current time.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_json(self, saving_file_storage=False):
        """
            Returning json informing of it.
        """
        obj_class = self.__class__.__name__
        bm_dict = {
            k: v if self.__is_serializable(v) else str(v)
            for k, v in self.__dict__.items()
        }
        bm_dict.pop('_sa_instance_state', None)
        bm_dict.update({
            '__class__': obj_class
            })
        if not saving_file_storage and obj_class == 'User':
            bm_dict.pop('password', None)
        return(bm_dict)

    def __str__(self):
        """
            Returning string type obj form.
        """
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def delete(self):
        """
            Deleting currnt instances of storage.
        """
        models.storage.delete(self)
