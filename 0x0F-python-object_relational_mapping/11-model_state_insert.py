#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """connectin to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             argv[1], argv[2], argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
