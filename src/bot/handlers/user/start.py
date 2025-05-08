from aiogram import Router, types
from aiogram.filters import CommandStart

from ...keyboards import *
from ...database import *

router = Router()
user_query = UserQuery()


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> types.Message:
    user_query.addUser(
        chat_id=msg.from_user.id,
        username=msg.from_user.username,
    )

    return await msg.answer(
        f'🎆 <b>Menu:</b>',
        reply_markup=user_main_menu_ikb(msg.from_user.id)
    )
