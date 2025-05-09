from sqlalchemy import Column, String, Integer

from .database import Database

db = Database()


class User(db.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    language = Column(String, default='en')
    chat_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False, default='unknown')
    lastname = Column(String, nullable=False, default='unknown')
    status_active = Column(String, default='unknown')
    bot_block = Column(String, default='false')
    date_reg = Column(String, nullable=False)
