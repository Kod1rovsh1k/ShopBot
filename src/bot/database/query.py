import asyncio

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

    import asyncio
    async def check_user_status(self):
        users = self.getAllUsers()
        batch_size = 100  # Размер пакета
        tasks = []
        for i in range(0, len(users), batch_size):
            batch = users[i:i + batch_size]
            tasks.append(self.check_batch_status(batch))
        await asyncio.gather(*tasks)

    async def check_batch_status(self, batch):
        for user in batch:
            await self.check_single_user_status(user)
            await asyncio.sleep(0.1)  # Задержка между отправками

    async def check_single_user_status(self, user):
        try:
            with db.Session() as session:
                user_record = session.query(User).filter_by(chat_id=user.chat_id).first()
                if user_record and user_record.bot_block == 'true':
                    user_record.bot_block = 'false'
                    session.commit()
        except Exception as e:
            if "blocked" in str(e).lower():
                with db.Session() as session:
                    user_record = session.query(User).filter_by(chat_id=user.chat_id).first()
                    if user_record:
                        user_record.bot_block = 'true'
                        session.commit()

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
