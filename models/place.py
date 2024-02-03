#!/usr/bin/python3
""" The Place Modul of our HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                      )


class Place(BaseModel, Base):
    """ The place of acting. """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', cascade='all, delete', backref='place')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False,
            backref='place_amenities')
    else:
        @property
        def reviews(self):
            '''storage linking between place with review. '''

            review_list = []
            review_dict = models.storage.all(models.Review)
            for review in review_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            '''
            Returns a list of amenity instences.
            '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            '''
            Doing the append of the adding of a
            Amenity id to the amenity ides.
            '''
            if isinstance(obj) is models.Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
