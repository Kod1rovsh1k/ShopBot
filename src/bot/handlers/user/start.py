from aiogram import Router, types
from aiogram.filters import CommandStart

from ...keyboards import *

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> types.Message:
    return await msg.reply(
        f'Hello, @{msg.from_user.username}',
        reply_markup=user_main_menu_ikb()
    )
