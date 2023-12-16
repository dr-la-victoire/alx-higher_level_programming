#!/usr/bin/python3
"""This model contains the State class for the ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This is the State Class"""
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='State', cascade='all, delete-orphan')
