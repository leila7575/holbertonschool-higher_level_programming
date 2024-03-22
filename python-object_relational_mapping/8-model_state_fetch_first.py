#!/usr/bin/python3
"""lists all state objects from database."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')


    Base.metadata.create_all(engine)


    Session = sessionmaker(bind=engine)
    session = Session()


    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
