from .models import *


class UserQuery:
    def __init__(self):
        pass

    @staticmethod
    def addUser(chat_id: int, username: str) -> User:
        with db.Session() as session:
            check_user = session.query(User).filter_by(chat_id=chat_id).first()
            if not check_user:
                new_user = User(
                    chat_id=chat_id,
                    username=username,
                )
                session.add(new_user)
                session.commit()
                return new_user
            return check_user
