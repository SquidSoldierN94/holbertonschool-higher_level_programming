#!/usr/bin/python3
"""
This module defines a State class and creates an instance of declarative_base().

State class:
    - Inherits from Base, which links to the MySQL table states.
    - Has class attributes id and name.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'.
    
    Attributes:
        id (int): The state's id, primary key, auto-generated.
        name (str): The state's name, can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
