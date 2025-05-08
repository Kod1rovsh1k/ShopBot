from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    Engine = create_engine("sqlite:///bot/database/database.db", echo=False)
    Session = sessionmaker(bind=Engine)
    Base = declarative_base()

    def __init__(self):
        self.Base.metadata.create_all(self.Engine)
