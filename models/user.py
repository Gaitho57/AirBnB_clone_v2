#!/usr/bin/python3
""" class User"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of the user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization user"""
        super().__init__(*args, **kwargs)
