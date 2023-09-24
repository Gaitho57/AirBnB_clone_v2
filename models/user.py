#!/usr/bin/python3
"""User class."""
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """Representation of user for a MySQL database.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
