#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """returns list of related cities based on state id"""
            from models import storage
            city_all = storage.all(City)
            city_related = []
            for key, val in city_all.items():
                if city_all[key].state_id == self.id:
                    city_related.append(val)
            return city_related
