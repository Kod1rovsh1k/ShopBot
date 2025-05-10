from aiogram import Router, F, types
from aiogram.methods import EditMessageText

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "shop-tools-panel")
async def cmd_shop_tools_panel(call: types.CallbackQuery) -> EditMessageText:
    return call.message.edit_text(
        f'🧰 <b>Shop tools:</b>',
        reply_markup=admin_shop_tools_ikb(),
    )
