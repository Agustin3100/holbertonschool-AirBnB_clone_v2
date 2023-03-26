#!/usr/bin/python3
"""This is the state class"""
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter method if typestorage is FileStorage."""
            return [city for city in models.storage.all(City).values() if
                    city.state_id == self.id]
