from datetime import datetime

from aiogram import Router, types
from aiogram.filters import CommandStart

from ...keyboards import *
from ...database import *

now = datetime.now()

router = Router()
user_query = UserQuery()


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> types.Message:
    user_query.addUser(
        chat_id=msg.from_user.id,
        language=msg.from_user.language_code,
        username=msg.from_user.username,
        firstname=msg.from_user.first_name,
        lastname=msg.from_user.last_name,
        date_reg=f"{now:%Y-%m-%d %H:%M:%S}",
    )
    await user_query.check_user_status()

    return await msg.answer(
        f'🎆 <b>Menu:</b>',
        reply_markup=user_main_menu_ikb(msg.from_user.id)
    )
