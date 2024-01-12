#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    stname = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter_by(name=stname).first()
    if not states:
        print("Not found")
    else:
        print(states.id)
