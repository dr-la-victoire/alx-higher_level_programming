#!/usr/bin/python3
"""
This module contains the script that prints the first
state from the database
"""
import sys
from model_state import Base, State
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == "“Louisiana").first()
    print("{}".format(state.id))