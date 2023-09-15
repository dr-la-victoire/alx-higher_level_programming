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
    states = session.query(State).filter(State.name.like("%a%")).order_by(
            State.id).all()
    for letter in states:
        print("{}: {}".format(letter.id, letter.name))