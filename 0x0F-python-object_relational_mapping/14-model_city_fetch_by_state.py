#!/usr/bin/python3
"""This is a script that prints all the cities from the database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # getting and printing the cities
    cities = session.query(City, State).join(State).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
