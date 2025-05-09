from aiogram import Router, F, types

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "profile")
async def cmd_profile(call: types.CallbackQuery) -> types.CallbackQuery:
    await call.message.edit_text(
        f'👤 <b>Profile:</b>\n'
        f'➖➖➖➖➖➖➖➖➖➖\n'
        f'🔑 <b>Chat-ID:</b> <code>{call.from_user.id}</code>\n'
        f'👤 <b>Login:</b> @{call.from_user.username}\n',
        reply_markup=user_profile_ikb()
    )

    return call
