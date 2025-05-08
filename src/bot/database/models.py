from sqlalchemy import Column, String, Integer

from .database import Database

db = Database()


class User(db.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    chat_id = Column(String, nullable=False)
    username = Column(String, nullable=False)
