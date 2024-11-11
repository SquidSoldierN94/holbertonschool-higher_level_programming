#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
It connects to the database using the provided credentials and retrieves states whose name contains 'a'.
The states are ordered by `id` in ascending order and displayed in the format `id: name`.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to a MySQL database using the provided username, password, and database name.
    Retrieves states whose name contains 'a', ordered by `id`, and prints them in the format `id: name`.
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
