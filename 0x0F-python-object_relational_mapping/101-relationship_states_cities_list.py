#!/usr/bin/python3
"""
This module contains the script that prints the first
state from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).all()
    for states in state:
        print("{}: {}".format(states.id, states.name))
        for city in states.cities:
            print("     {}: {}".format(city.id, city.name))
