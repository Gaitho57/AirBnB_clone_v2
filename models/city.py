#!/usr/bin/python
""" holds class City"""
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Represent city"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """city initialization"""
        super().__init__(*args, **kwargs)
