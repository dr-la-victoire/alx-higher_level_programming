#!/usr/bin/python3
"""
This module is a script that lists all State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # creating an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()
    state_names = session.query(State).order_by(State.id).all()
    for state in state_names:
        print("{}: {}".format(state.id, state.name))
