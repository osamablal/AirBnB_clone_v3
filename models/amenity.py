#!/usr/bin/python3
""" The stating Modul of the HBNB project """
import models
from sqlalchemy import Column, String

class Amenity(models.base_model.BaseModel, models.base_model.Base):
    '''The class for Amenity'''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
