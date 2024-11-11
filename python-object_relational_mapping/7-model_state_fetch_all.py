#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.

It uses SQLAlchemy to connect to the MySQL database and queries the `states` table.
The results are sorted in ascending order by `id` and printed in the format:
    id: state_name
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to a MySQL database using the provided username, password, and database name.
    Creates a session and queries the `State` objects ordered by `id`, displaying them
    in the format `id: name`.
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
