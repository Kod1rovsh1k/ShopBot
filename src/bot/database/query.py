from .models import *

from ..configs import *

bot_cfg = BotConfig()


class UserQuery:
    def __init__(self):
        pass

    def getAllUsers(self):
        with db.Session() as session:
            users = session.query(User).all()
            return users

    def addUser(self, chat_id: int, language: str, username: str, firstname: str, lastname: str, date_reg: str) -> User:
        with db.Session() as session:
            check_user = session.query(User).filter_by(chat_id=chat_id).first()
            if not check_user:
                new_user = User(
                    chat_id=chat_id,
                    language=language,
                    username=username,
                    firstname=firstname,
                    lastname=lastname,
                    date_reg=date_reg,
                )
                session.add(new_user)
                session.commit()
                return new_user
            return check_user

    async def userMailing(self, text: str, photo_id: str = None, sender_chat_id: int = None):
        users = self.getAllUsers()
        for user in users:
            try:
                if user.chat_id != sender_chat_id:
                    if photo_id:
                        await bot_cfg.bot.send_photo(chat_id=user.chat_id, photo=photo_id, caption=text,
                                                     parse_mode="HTML")
                    else:
                        await bot_cfg.bot.send_message(chat_id=user.chat_id, text=text, parse_mode="HTML")
            except Exception as e:
                if "blocked" in str(e).lower():
                    with db.Session() as session:
                        user_record = session.query(User).filter_by(chat_id=user.chat_id).first()
                        if user_record:
                            user_record.bot_block = 'true'
                            session.commit()
                else:
                    pass
