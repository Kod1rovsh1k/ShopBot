from aiogram import Router, F, types

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "profile")
async def cmd_profile(call: types.CallbackQuery) -> types.CallbackQuery:
    await call.message.edit_text(
        f'Profile',
        reply_markup=user_profile_ikb()
    )

    return call
