from aiogram import Router, F, types

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "back-main-menu")
async def cmd_back_main_menu(call: types.CallbackQuery) -> types.CallbackQuery | bool:
    return await call.message.edit_text(
        f'Hello, @{call.from_user.username}',
        reply_markup=user_main_menu_ikb()
    )
