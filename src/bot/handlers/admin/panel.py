from aiogram import Router, F, types
from aiogram.methods import EditMessageText

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "admin-panel")
async def cmd_admin_panel(call: types.CallbackQuery) -> EditMessageText:
    return call.message.edit_text(
        f'🎈 <b>Admin panel:</b>\n',
        reply_markup=admin_main_panel_ikb()
    )
