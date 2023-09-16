#!/usr/bin/python3
"""
This module contains the script that prints the first
state from the database
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State)
    for state, place in result.all():
        print("{}: ({}) {}".format(place.name, state.id, state.name))
