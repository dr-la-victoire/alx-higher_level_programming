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

    # adding the new state
    new_state = State(id=6, name='Louisiana')
    session.add(new_state)
    session.commit()

    # printing the new state's id
    the_state = session.query(State).order_by(State.id.desc()).first()
    print("{}".format(the_state.id))
    session.close()
