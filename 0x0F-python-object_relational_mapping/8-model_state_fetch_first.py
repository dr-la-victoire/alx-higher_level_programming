#!/usr/bin/python3
"""This module contains the code that fetches all the states in a database"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # getting and printing the states
    states = session.query(State).first()
    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")