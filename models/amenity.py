#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchmey import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', backref='amenity', secondary='Amenity') 
