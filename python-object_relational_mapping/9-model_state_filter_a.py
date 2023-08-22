#!/usr/bin/python3
"""
Module Docstring: Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine and session to interact with the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display State objects containing the letter 'a'
    states_with_a = (
        session.query(State).filter(State.name.contains("a")).order_by(State.id).all()
    )
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
