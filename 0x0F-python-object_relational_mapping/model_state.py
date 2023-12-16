#!/usr/bin/python3
"""This model contains the State class for the ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This is the State Class"""
    __tablename__ = "states"
    id = Column(
            Integer, nullable=False,
            primary_key=True, unique=True, autoincrememt=True)
    name = Column(String(128), nullable=False)
