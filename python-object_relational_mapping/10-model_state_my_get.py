#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
It connects to the MySQL database using SQLAlchemy, searches for a state by name, and prints its id.
If the state is not found, it prints 'Not found'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the MySQL database using provided credentials, searches for the state by name,
    and prints its id or 'Not found' if no state with the given name exists.
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")
