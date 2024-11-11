#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.

It connects to the database using the provided credentials and queries the first state
from the table, displaying it in the format `id: name`.
If no state is found, it prints "Nothing".
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to a MySQL database using the provided username, password, and database name.
    Retrieves the first State object, ordered by `id`, and prints it in the format `id: name`.
    If the table is empty, it prints "Nothing".
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
