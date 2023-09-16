#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
of the declarative base
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# The instance
Base = declarative_base()

# The class definition


class State(Base):
    """This class inherits from the Base class"""
    # Linking to the table
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
