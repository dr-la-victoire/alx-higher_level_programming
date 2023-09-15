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
    first_name = session.query(State).order_by(State.id).first()
    if first_name is not None:
        print("{}: {}".format(first_name.id, first_name.name))
    else:
        print("Nothing")
